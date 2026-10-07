"""Map rendering for the wiki (imported by build.py).

For every map the game loads:
  * renders its visible tile layers to docs/assets/maps/<map>.webp
  * writes docs/maps/<map>.md: the image with clickable, colour-coded overlays for
    spawns, exits (linking to the destination map), signs, rests, containers, keys,
    scripts and replace areas, plus the monster table
Plus docs/maps/index.md: one clickable world-map image per worldmap.xml segment.
"""
import base64, gzip, html, os, re, zlib
import xml.etree.ElementTree as ET
from collections import defaultdict
from PIL import Image

TILE = 32
FLIP_MASK = 0x1FFFFFFF
DRAW_ORDER = ('base', 'ground', 'objects', 'above', 'top')  # Tiled stores flip flags in the top 3 bits
_tileset_cache = {}

def _tileset_img(path):
    if path not in _tileset_cache:
        _tileset_cache[path] = Image.open(path).convert('RGBA') if os.path.exists(path) else None
    return _tileset_cache[path]

def _decode(data_el, n):
    enc, comp = data_el.get('encoding'), data_el.get('compression')
    text = (data_el.text or '').strip()
    if enc == 'csv':
        return [int(x) for x in text.replace('\n', '').split(',') if x.strip()]
    raw = base64.b64decode(text)
    if comp == 'zlib': raw = zlib.decompress(raw)
    elif comp == 'gzip': raw = gzip.decompress(raw)
    return [int.from_bytes(raw[i:i + 4], 'little') for i in range(0, min(len(raw), n * 4), 4)]

def parse_tmx(path):
    root = ET.parse(path).getroot()
    w, h = int(root.get('width')), int(root.get('height'))
    tilesets = []
    for ts in root.findall('tileset'):
        im = ts.find('image')
        if im is None: continue
        src = os.path.normpath(os.path.join(os.path.dirname(path), im.get('source')))
        tilesets.append((int(ts.get('firstgid')), src, int(im.get('width')) // TILE))
    tilesets.sort()
    # The game draws only these layers, in this order (TMXMapTranslator.defaultLayerNames);
    # anything else (Light*, *_replace, Breadcrumb...) is an editor helper and must be skipped.
    by_name = {(l.get('name') or '').lower(): l for l in root.findall('layer') if l.find('data') is not None}
    layers = [(n, _decode(by_name[n].find('data'), w * h)) for n in DRAW_ORDER if n in by_name]
    walkable = _decode(by_name['walkable'].find('data'), w * h) if 'walkable' in by_name else None
    objects = []
    for og in root.findall('objectgroup'):
        for o in og.findall('object'):
            props = {p.get('name'): p.get('value') for p in o.iter('property')}
            objects.append(dict(type=(o.get('type') or '').lower(), name=o.get('name') or '',
                                x=float(o.get('x', 0)), y=float(o.get('y', 0)),
                                w=float(o.get('width', TILE)), h=float(o.get('height', TILE)), props=props))
    mprops = {p.get('name'): p.get('value') for p in root.find('properties').iter('property')} if root.find('properties') is not None else {}
    return dict(w=w, h=h, tilesets=tilesets, layers=layers, walkable=walkable, objects=objects, props=mprops)

def render(tmx, out_path):
    img = Image.new('RGBA', (tmx['w'] * TILE, tmx['h'] * TILE), (0, 0, 0, 255))
    ts = tmx['tilesets']
    tile_cache = {}
    for _, data in tmx['layers']:
        for i, gid in enumerate(data):
            gid &= FLIP_MASK
            if not gid: continue
            if gid not in tile_cache:
                tile = None
                for first, src, cols in reversed(ts):
                    if gid >= first:
                        sheet = _tileset_img(src)
                        if sheet is not None and cols:
                            k = gid - first
                            box = ((k % cols) * TILE, (k // cols) * TILE, (k % cols + 1) * TILE, (k // cols + 1) * TILE)
                            if box[3] <= sheet.height: tile = sheet.crop(box)
                        break
                tile_cache[gid] = tile
            tile = tile_cache[gid]
            if tile is not None:
                img.alpha_composite(tile, ((i % tmx['w']) * TILE, (i // tmx['w']) * TILE))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.convert('RGB').save(out_path, 'WEBP', quality=72, method=4)
    return img

LEGEND = [('spawn', 'Red', 'Monsters / NPCs', True), ('mapchange', 'Blue', 'Exit to another map', True),
          ('container', 'Yellow', 'Container (click to see contents)', True), ('sign', 'Purple', 'Sign', True),
          ('rest', 'Green', 'Resting place', True), ('key', 'Orange dashed', 'Blocked until a quest step / item', True),
          ('script', 'Grey dotted', 'Scripted event', False), ('replace', 'White dotted', 'Changes during a quest', False)]
LEGEND_TYPES = {l[0] for l in LEGEND}

_COMPASS = {'nw': 'north-west', 'ne': 'north-east', 'sw': 'south-west', 'se': 'south-east', 'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
def _pretty(name):
    words = (name or '').replace('_', ' ').strip().split(' ')
    return ' '.join(_COMPASS.get(w.lower(), w) if i else w for i, w in enumerate(words)).capitalize()
def _esc(s): return html.escape(str(s), quote=True)

class QuestInfo:
    """Turns requirement/reward data into readable text + links, and collects notes for quest pages."""
    def __init__(self, ctx):
        self.q, self.items, self.monsters = ctx['quests'], ctx['items'], ctx['monsters']
        self.skills, self.conditions = ctx.get('skills', {}), ctx.get('conditions', {})
        self.notes = defaultdict(lambda: defaultdict(set))   # quest -> stage -> {markdown note}
    def name(self, qid):
        q = self.q.get(qid)
        if not q: return qid
        return q.get('name', qid) if q.get('showInLog', 0) else f'hidden story flag “{qid}”'
    def stage_text(self, qid, val):
        for st in self.q.get(qid, {}).get('stages', []):
            if st.get('progress') == val: return st.get('logText', '')
        return ''
    def url(self, qid, val): return f'../../quests/{qid}/' + (f'#stage-{val}' if val else '')
    def req(self, t, rid, val, neg, verb_ok, verb_neg):
        """Return (tooltip, href) for one requirement."""
        t = t or 'questProgress'
        if t in ('questProgress', 'questLatestProgress') and rid:
            st = self.stage_text(rid, val)
            tip = f"{verb_neg if neg else verb_ok} the quest: {self.name(rid)}" + (f' (stage {val}: “{st}”)' if st else f' (stage {val})')
            return tip, self.url(rid, val) if rid in self.q else None
        if t in ('inventoryKeep', 'inventoryRemove', 'wear', 'usedItem') and rid:
            nm = self.items.get(rid, {}).get('name', rid)
            what = 'wearing' if t == 'wear' else 'carrying'
            return (f"Passable only while not {what}: {nm}" if neg else f"Requires {what}: {nm}"), f'../../items/{rid}/'
        if t == 'killedMonster' and rid:
            nm = self.monsters.get(rid, {}).get('name', rid)
            return f"Opens after killing {val}× {nm}", (f'../../monsters/{rid}/' if rid in self.monsters else None)
        if t == 'skillLevel' and rid:
            return f"Requires the skill {self.skills.get(rid, {}).get('name', rid)} level {val}", f'../../skills/{rid}/'
        if t in ('factionScore', 'factionScoreEquals'):
            return f"Depends on your standing with the “{rid}” faction ({'=' if t.endswith('Equals') else '≥'} {val})", None
        if t == 'hasActorCondition':
            nm = self.conditions.get(rid, {}).get('name', rid)
            return (f"Only while not affected by {nm}" if neg else f"Only while affected by {nm}"), None
        if t == 'timerElapsed':
            return f"Changes after time passes ({val} rounds since an event)", None
        return f"Condition: {t} {rid or ''} {val or ''}".strip(), None
    def note(self, qid, val, text):
        if qid in self.q: self.notes[qid][val].add(text)

def _walk_script(convs, start, limit=60):
    """Collect quest requirements and quest rewards reachable from a script phrase."""
    reqs, rewards, other, seen, stack, first_msg = [], [], [], set(), [start], ''
    while stack and len(seen) < limit:
        pid = stack.pop()
        if pid in seen or pid not in convs: continue
        seen.add(pid); c = convs[pid]
        if not first_msg and c.get('message'): first_msg = c['message']
        for r in c.get('rewards') or []:
            if r.get('rewardType') == 'questProgress': rewards.append((r.get('rewardID'), r.get('value', 0)))
            elif r.get('rewardType') == 'mapchange': other.append(f"moves you to {_pretty(r.get('rewardID', '').split(':')[0] or r.get('mapName', ''))}")
            elif r.get('rewardType') == 'giveItem': other.append('gives you an item')
            elif r.get('rewardType') == 'spawnAll': other.append('makes monsters appear')
        for rep in c.get('replies') or []:
            for rq in rep.get('requires') or []:
                if rq.get('requireType') in ('questProgress', 'questLatestProgress'):
                    reqs.append((rq.get('requireID'), rq.get('value', 0), bool(rq.get('negate'))))
            if rep.get('nextPhraseID'): stack.append(rep['nextPhraseID'])
    return reqs, rewards, other, first_msg

def _place_monsters(t, spawns, ctx, seed):
    """Pick a fixed, non-overlapping tile for every monster a spawn area can hold."""
    import random
    rnd = random.Random(seed)
    W, H = t['w'], t['h']
    blocked = set()
    if t.get('walkable'):
        blocked = {i for i, g in enumerate(t['walkable']) if g & FLIP_MASK}
    occupied, placed = set(), []
    for o, mids, active in spawns:
        if not mids: continue
        x0, y0 = int(o['x'] // TILE), int(o['y'] // TILE)
        x1, y1 = max(x0 + 1, int(-(-(o['x'] + o['w']) // TILE))), max(y0 + 1, int(-(-(o['y'] + o['h']) // TILE)))
        cells = [(x, y) for y in range(y0, min(y1, H)) for x in range(x0, min(x1, W))]
        rnd.shuffle(cells)
        try: qty = max(1, int(o['props'].get('quantity', 1)))
        except ValueError: qty = 1
        order = sorted(mids)
        for n in range(qty):
            mid = order[(n + rnd.randrange(len(order))) % len(order)] if len(order) > 1 else order[0]
            fw, fh = ctx['monster_size'](mid)
            def fits(x, y, strict):
                fp = [(x + dx, y + dy) for dx in range(fw) for dy in range(fh)]
                if any(px >= W or py >= H for px, py in fp) or any(p in occupied for p in fp): return None
                if strict and any(py * W + px in blocked for px, py in fp): return None
                return fp
            spot = next(((x, y, fp) for strict in (True, False) for x, y in cells for fp in [fits(x, y, strict)] if fp), None)
            if not spot: break
            x, y, fp = spot
            occupied.update(fp)
            placed.append((mid, x, y, fw, fh, active))
    return placed

def build_maps(ctx):
    """ctx: GAME, DOCS, VERSION, monsters, droplists, items, conversations, quests, skills, conditions,
    group_to_monsters, write, md_esc, monster_icon(mid)->rel path or None, monster_size(mid)->(w,h) tiles."""
    GAME, DOCS = ctx['GAME'], ctx['DOCS']
    monsters, droplists, items, convs = ctx['monsters'], ctx['droplists'], ctx['items'], ctx['conversations']
    QI = QuestInfo(ctx)
    xml_dir = os.path.join(GAME, 'res', 'xml')
    lr = ET.parse(os.path.join(GAME, 'res', 'values', 'loadresources.xml')).getroot()
    map_names = [i.text.split('/')[-1] for arr in lr if arr.get('name') == 'loadresource_maps' for i in arr if i.text]
    map_names = [m for m in map_names if os.path.exists(os.path.join(xml_dir, m + '.tmx'))]

    parsed, spawn_maps, sizes = {}, defaultdict(set), {}
    script_maps = defaultdict(set)   # phrase -> {(map, how)}: conversations started by map objects
    for m in map_names:
        try: parsed[m] = parse_tmx(os.path.join(xml_dir, m + '.tmx'))
        except Exception as e: print('  skip map', m, e)

    thumbs = {}
    for m, t in parsed.items():
        full = render(t, os.path.join(DOCS, 'assets', 'maps', m + '.webp'))
        thumbs[m] = full.convert('RGB').resize((t['w'] * 4, t['h'] * 4), Image.BILINEAR)
        sizes[m] = (t['w'], t['h'])

    def spawn_mids(o):
        grp = o['props'].get('spawngroup', o['name'])
        return ctx['group_to_monsters'].get(grp, []) or ([grp] if grp in monsters else [])

    # ------------------------------------------------ world map segments
    wm = ET.parse(os.path.join(xml_dir, 'worldmap.xml')).getroot()
    on_world, seg_md = {}, []
    for seg in wm.findall('segment'):
        entries = [(mp.get('id'), int(mp.get('x')), int(mp.get('y'))) for mp in seg.findall('map') if mp.get('id') in thumbs]
        if not entries: continue
        minx = min(x for _, x, _ in entries); miny = min(y for _, _, y in entries)
        maxx = max(x + sizes[i][0] for i, x, _ in entries); maxy = max(y + sizes[i][1] for i, _, y in entries)
        canvas = Image.new('RGB', ((maxx - minx) * 4, (maxy - miny) * 4), (24, 20, 16))
        zones = []
        for mid, x, y in entries:
            canvas.paste(thumbs[mid], ((x - minx) * 4, (y - miny) * 4))
            on_world[mid] = seg.get('id')
            zones.append(f'<a class="wm-zone" href="{mid}/" title="{_esc(_pretty(mid))}" style="left:{(x-minx)/(maxx-minx)*100:.3f}%;top:{(y-miny)/(maxy-miny)*100:.3f}%;width:{sizes[mid][0]/(maxx-minx)*100:.3f}%;height:{sizes[mid][1]/(maxy-miny)*100:.3f}%"></a>')
        seg_id = seg.get('id')
        canvas.save(os.path.join(DOCS, 'assets', 'maps', f'_world_{seg_id}.webp'), 'WEBP', quality=70)
        seg_md.append((len(entries), f'\n## {_pretty(seg_id)}\n\n<div class="map-wrap world" markdown="0"><img src="../assets/maps/_world_{seg_id}.webp" alt="{seg_id}" loading="lazy">{"".join(zones)}</div>\n'))
    seg_md.sort(key=lambda s: -s[0])
    idx = [f"# World map\n\nEvery region of v{ctx['VERSION']}, assembled from the game's own map files. "
           "Hover over a map to see its name, and click it to open that map's page.\n"] + [s[1] for s in seg_md]
    idx.append("\n## All maps (A–Z)\n\n" + ''.join(f"- [{_pretty(m)}]({m}.md)\n" for m in sorted(parsed)))
    ctx['write']('maps/index.md', ''.join(idx))

    # ------------------------------------------------ per map: collect (pages are written later by write_map_pages)
    area_of = {mp.get('id'): mp.get('area') for seg in wm.findall('segment') for mp in seg.findall('map') if mp.get('area')}
    seg_of = {mp.get('id'): (seg.get('id'), int(mp.get('x')), int(mp.get('y'))) for seg in wm.findall('segment') for mp in seg.findall('map')}
    area_names = {na.get('id'): (na.get('name', '').strip(), na.get('type', '')) for seg in wm.findall('segment') for na in seg.findall('namedarea')}
    pages = {}
    for m, t in parsed.items():
        W, H = t['w'] * TILE, t['h'] * TILE
        pct = lambda x, y, w, h: f"left:{x/W*100:.3f}%;top:{y/H*100:.3f}%;width:{max(w,8)/W*100:.3f}%;height:{max(h,8)/H*100:.3f}%"
        mlink = f'[{_pretty(m)}](../maps/{m}.md)'
        boxes, here, exits, containers, spawns, pois, qroles = [], set(), [], [], [], [], defaultdict(set)
        for n, o in enumerate(t['objects']):
            typ = o['type']
            if typ not in LEGEND_TYPES: continue
            cx, cy = o['x'] + o['w'] / 2, o['y'] + o['h'] / 2
            tip, href, attrs, extra_cls = _pretty(o['name']), None, '', ''
            if typ == 'spawn':
                ms = spawn_mids(o)
                active = str(o['props'].get('active', 'true')).lower() != 'false'
                try: qty = max(1, int(o['props'].get('quantity', 1)))
                except ValueError: qty = 1
                here.update(ms); spawns.append((o, ms, active, qty))
                for x in ms: spawn_maps[x].add(m)
                names = sorted({monsters[x].get('name', x) for x in ms})
                tip = 'Spawns: ' + (', '.join(names) if names else o['name']) + ('' if active else ' (only appears later, during a quest)')
            elif typ == 'mapchange':
                dest, place = o['props'].get('map'), o['props'].get('place')
                attrs = f' id="place-{_esc(o["name"])}"'
                if dest:
                    tip = f'Exit to {_pretty(dest)}'; href = f'../{dest}/' + (f'#place-{place}' if place else '')
                    exits.append(dict(dest=dest, place=place, name=o['name'], x=cx, y=cy, tx=cx / TILE, ty=cy / TILE))
            elif typ == 'container':
                dl = droplists.get(o['name'])
                if not dl: continue
                k = len(containers); containers.append((o['name'], dl))
                tip = 'Container: click to see what\'s inside'; href = f'#container-{k}'
                attrs = f' data-container="container-{k}"'
                pois.append(dict(kind='container', x=cx, y=cy, label=f'Container {k + 1}', href=f'#container-{k}',
                                 detail=', '.join(items.get(e['itemID'], {}).get('name', e['itemID']) for e in dl.get('items', [])[:6])))
            elif typ == 'sign':
                script_maps[o['name']].add((m, 'sign'))
                text = convs.get(o['name'], {}).get('message') or ''
                tip = 'Sign: ' + (text or o['name'])
                pois.append(dict(kind='sign', x=cx, y=cy, label='Sign', detail=f'“{text}”' if text else 'A sign'))
            elif typ == 'rest':
                tip = 'Resting place (respawn point)'
                pois.append(dict(kind='rest', x=cx, y=cy, label='Resting place', detail='Rest here to heal and set your respawn point'))
            elif typ == 'key':
                p = o['props']
                if p.get('phrase'): script_maps[p['phrase']].add((m, 'key'))
                val = int(p.get('requireValue') or 0) if str(p.get('requireValue', '0')).lstrip('-').isdigit() else 0
                neg = str(p.get('requireNegation', 'false')).lower() == 'true'
                tip, href = QI.req(p.get('requireType'), p.get('requireId'), val, neg,
                                   'Unlocked during', 'Closed off once you reach this point in')
                if (p.get('requireType') or 'questProgress').startswith('quest'):
                    QI.note(p.get('requireId'), val, f"🔓 You can finally access a previously blocked area on {mlink}." if not neg
                            else f"🔒 An area on {mlink} becomes blocked off.")
                    qroles[p.get('requireId')].add(f"blocked passage {'opens' if not neg else 'closes'} at stage {val}")
                pois.append(dict(kind='key', x=cx, y=cy, label='Blocked passage', detail=tip, href=href))
            elif typ == 'replace':
                p = o['props']
                if p.get('requireType') or p.get('requireId'):
                    val = int(p.get('requireValue') or 0) if str(p.get('requireValue', '0')).lstrip('-').isdigit() else 0
                    neg = str(p.get('requireNegation', 'false')).lower() == 'true'
                    tip, href = QI.req(p.get('requireType'), p.get('requireId'), val, neg,
                                       'This area changes during', 'This area changes back during')
                    if (p.get('requireType') or 'questProgress').startswith('quest'):
                        QI.note(p.get('requireId'), val, f"🗺️ Part of {mlink} visibly changes.")
                        qroles[p.get('requireId')].add(f"part of the map changes at stage {val}")
                        pois.append(dict(kind='replace', x=cx, y=cy, label='Changes during a quest', detail=tip, href=href))
                else:
                    tip = 'This area changes when a scripted event activates it'
            elif typ == 'script':
                script_maps[o['name']].add((m, 'script'))
                reqs, rewards, other, first = _walk_script(convs, o['name'])
                if rewards:
                    qid, val = rewards[0]
                    tip = f"Scripted event: advances the quest: {QI.name(qid)} to stage {val}"
                    st = QI.stage_text(qid, val)
                    if st: tip += f' (“{st}”)'
                    if len({r[0] for r in rewards}) > 1: tip += f" (+{len({r[0] for r in rewards}) - 1} more quest(s))"
                    href = QI.url(qid, val) if qid in QI.q else None
                    for q2, v2 in set(rewards):
                        QI.note(q2, v2, f"👣 Reached by stepping onto a trigger spot on {mlink}.")
                        qroles[q2].add(f"stepping on a trigger here sets stage {v2}")
                    pois.append(dict(kind='script', x=cx, y=cy, label='Quest trigger', detail=tip, href=href))
                elif reqs:
                    qid, val, neg = reqs[0]
                    tip = f"Scripted event that only happens during the quest: {QI.name(qid)} (stage {val})"
                    href = QI.url(qid, val) if qid in QI.q else None
                    for q2, v2, n2 in set(reqs):
                        if not n2:
                            QI.note(q2, v2, f"⚡ A scripted event can now trigger on {mlink}.")
                            qroles[q2].add(f"a scripted event can trigger here from stage {v2}")
                else:
                    tip = 'Scripted event' + (': ' + other[0] if other else (': “' + first[:90] + ('…' if len(first) > 90 else '') + '”' if first else ''))
            tag = 'a' if href else 'span'
            h = f' href="{_esc(href)}"' if href else ''
            boxes.append(f'<{tag}{attrs} class="mo mo-{typ}{extra_cls}"{h} title="{_esc(tip)}" style="{pct(o["x"], o["y"], o["w"], o["h"])}"></{tag}>')
        placed = _place_monsters(t, [(o, ms, act) for o, ms, act, _ in spawns], ctx, seed=m)
        pages[m] = dict(t=t, W=W, H=H, boxes=boxes, here=here, exits=exits, containers=containers, spawns=spawns,
                        pois=pois, qroles=qroles, placed=placed)

    # ------------------------------------------------ regions: named area, else inherited through doors (indoor maps)
    adj = defaultdict(set)
    for m, pg in pages.items():
        for e in pg['exits']:
            if e['dest'] in pages: adj[m].add(e['dest']); adj[e['dest']].add(m)
    def region(m):
        if m in area_of: return area_of[m], 'in'
        seen, frontier = {m}, [m]
        for depth in range(3):
            nxt = []
            for x in frontier:
                for y in sorted(adj[x]):
                    if y in seen: continue
                    seen.add(y)
                    if y in area_of: return area_of[y], ('in' if parsed[m]['props'].get('outdoors') != '1' else 'near')
                    nxt.append(y)
            frontier = nxt
        return None, None
    for m, pg in pages.items():
        aid, rel = region(m)
        pg['area'] = (area_names.get(aid, (aid, ''))[0] if aid else None, area_names.get(aid, ('', ''))[1] if aid else None, rel)
        pg['segment'] = seg_of.get(m) or ((on_world.get(m), None, None) if m in on_world else None)
        pg['outdoors'] = parsed[m]['props'].get('outdoors') == '1'
    ctx['_map_pages'] = pages
    return spawn_maps, len(parsed), QI.notes, script_maps, pages


# ======================================================================== pass 2: location pages
DIR_ORDER = ['North', 'Northeast', 'East', 'Southeast', 'South', 'Southwest', 'West', 'Northwest']
UNDERGROUND = re.compile(r'cave|mine|dungeon|cellar|crypt|tunnel|well|basement|sewer|underground|hole|catacomb|tomb|lair|pit', re.I)


def exit_direction(pg, e, pages):
    """Edge exits get a compass direction; exits inside the map are doors, cave entrances, stairs or paths."""
    w, h = pg['t']['w'], pg['t']['h']
    ns = 'North' if e['ty'] < 2.5 else ('South' if e['ty'] > h - 2.5 else '')
    ew = 'West' if e['tx'] < 2.5 else ('East' if e['tx'] > w - 2.5 else '')
    if ns or ew: return (ns + ew.lower()) if ns and ew else (ns or ew)
    here_out, dest_out = pg['outdoors'], pages.get(e['dest'], {}).get('outdoors', False)
    if here_out and not dest_out: return 'Cave entrance' if UNDERGROUND.search(e['dest']) else 'Door'
    if not here_out and dest_out: return 'Exit outside'
    if not here_out and not dest_out: return 'Stairs / passage'
    return 'Path'


def write_map_pages(pages, ctx, QG, notes, shopkeepers, introduced):
    monsters, items, write, VERSION = ctx['monsters'], ctx['items'], ctx['write'], ctx['VERSION']
    md = ctx['md_esc']
    qb = defaultdict(set)                       # conversation start -> quests it can advance
    for (q, s), cids in QG.triggers.items():
        for cid in cids:
            for rp in QG.paths.get(cid, {}): qb[rp].add(q)
    map_roots = defaultdict(set)                # map -> conversation starts placed on it (signs, triggers, blocked passages)
    for ph, places in QG.script_maps.items():
        for mp, how in places: map_roots[mp].add(ph)

    for m, pg in pages.items():
        t, W, H = pg['t'], pg['W'], pg['H']
        pctp = lambda x, y: f"left:{x / W * 100:.3f}%;top:{y / H * 100:.3f}%"
        pct = lambda x, y, w, h: f"left:{x/W*100:.3f}%;top:{y/H*100:.3f}%;width:{max(w,8)/W*100:.3f}%;height:{max(h,8)/H*100:.3f}%"
        npcs = sorted({x for x in pg['here'] if monsters[x].get('phraseID')}, key=lambda x: monsters[x].get('name', x))
        enemies = sorted({x for x in pg['here'] if not monsters[x].get('phraseID')}, key=lambda x: monsters[x].get('maxHP', 0))
        first_pos = {}
        for mid, x, y, fw, fh, active in pg['placed']:
            first_pos.setdefault(mid, ((x + fw / 2) * TILE, (y + fh / 2) * TILE))
        for o, ms, active, qty in pg['spawns']:
            for x in ms: first_pos.setdefault(x, (o['x'] + o['w'] / 2, o['y'] + o['h'] / 2))
        npc_quests = {x: qb.get(monsters[x]['phraseID'], set()) for x in npcs}

        # ---------- numbered key: exits, NPCs, then points of interest
        key, pins = [], []
        key_num, pin_xy = {}, []
        def add_pin(kind, x, y, what, detail, anchor=None):
            """Identical points (same thing, same details) share one number; each spot still gets a pin."""
            n = key_num.get((what, detail))
            if n is None:
                n = len(key) + 1
                if n > 80: return None
                key_num[(what, detail)] = n
                key.append((n, what, detail))
            # nudge pins that would sit on top of an earlier one (about 22 px apart), staying inside the map
            r, x0, y0 = 22, x, y
            free = lambda a, b: all((a - px) ** 2 + (b - py) ** 2 >= r * r for px, py in pin_xy)
            k = 0
            while not free(x, y) and k < 60:      # golden-angle spiral around the true spot
                k += 1
                ang, rad = k * 2.39996, r * (0.6 + 0.35 * k ** 0.5)
                x = min(W - 10, max(10, x0 + rad * __import__('math').cos(ang)))
                y = min(H - 10, max(10, y0 + rad * __import__('math').sin(ang)))
            pin_xy.append((x, y))
            pins.append(f'<a{f' id="{anchor}"' if anchor else ''} class="pin pin-{kind}" href="#key-{n}" style="{pctp(x, y)}" title="{_esc(re.sub(r"[\\[\\]]|\\(\\.\\./[^)]*\\)|\\([^)\\s]*\\.md[^)\\s]*\\)", "", what + ": " + detail))}">{n}</a>')
            return n
        conn = defaultdict(list)
        for e in sorted(pg['exits'], key=lambda e: (DIR_ORDER.index(d) if (d := exit_direction(pg, e, pages)) in DIR_ORDER else 99, e['dest'])):
            d = exit_direction(pg, e, pages)
            n = add_pin('exit', e['x'], e['y'], f"Exit ({d.lower()})", f"to [{_pretty(e['dest'])}]({e['dest']}.md)")
            if n not in conn[(d, e['dest'])]: conn[(d, e['dest'])].append(n)
        npc_num = {}
        for x in npcs:
            px, py = first_pos.get(x, (W / 2, H / 2))
            role = []
            if x in shopkeepers: role.append('shopkeeper')
            vq = [q for q in npc_quests[x] if QG.quests[q].get('showInLog', 0)]
            if vq: role.append(f"{len(vq)} quest{'s' if len(vq) != 1 else ''}")
            npc_num[x] = add_pin('npc', px, py, f"[{md(monsters[x].get('name', x))}](../../monsters/{x}.md)", ', '.join(role) or 'NPC', anchor=f"pin-npc-{x}")
        for p in pg['pois']:
            add_pin(p['kind'], p['x'], p['y'], p['label'], p.get('detail', ''))
        num_of_poi = {id(p): i for i, p in enumerate(pg['pois'])}

        # ---------- sprites standing in their spawn areas
        mobs = []
        for mid, x, y, fw, fh, active in pg['placed']:
            ic = ctx['monster_icon'](mid)
            if not ic: continue
            nm = monsters[mid].get('name', mid)
            mobs.append(f'<a class="mob{"" if active else " mob-later"}" href="../../monsters/{mid}/" title="{_esc(nm + ("" if active else " (appears later in a quest)"))}" '
                        f'style="{pct(x*TILE, y*TILE, fw*TILE, fh*TILE)}"><img src="../../{ic}" alt="{_esc(nm)}"></a>')

        # ---------- quests connected to this map
        quests_here = defaultdict(set)
        for x in npcs:
            for q in npc_quests[x]: quests_here[q].add(f"[{md(monsters[x].get('name', x))}](../monsters/{x}.md) is involved")
        for ph in map_roots.get(m, ()):
            for q in qb.get(ph, ()): quests_here[q].add('something on this map advances it')
        for q, roles in pg['qroles'].items():
            if q in QG.quests: quests_here[q].update(roles)
        qlist = sorted(quests_here, key=lambda q: (0 if QG.quests[q].get('showInLog', 0) else 1, QG.quests[q].get('name', q).lower()))

        # ---------- page
        area, atype, rel = pg['area']
        region = (f"{'In' if rel == 'in' else 'Near'} {area}" + (f" ({atype})" if atype else '')) if area else None
        seg = pg['segment']
        intro_v = introduced('maps', m) if introduced else None
        info = [('Map ID', f"`{m}`"), ('Region', region), ('Type', 'Outdoors' if pg['outdoors'] else 'Indoors / underground'),
                ('Size', f"{t['w']}×{t['h']} tiles"),
                ('World map', f"[{_pretty(seg[0])}](index.md)" if seg and seg[0] else None),
                ('Introduced', intro_v), ('NPCs', str(len(npcs)) if npcs else None),
                ('Enemy types', str(len(enemies)) if enemies else None),
                ('Quests', str(sum(1 for q in qlist if QG.quests[q].get('showInLog', 0))) or None),
                ('Containers', str(len(pg['containers'])) if pg['containers'] else None)]
        dests = list(dict.fromkeys(d for (_, d) in conn))
        overview = (f"**{_pretty(m)}** is an {'outdoor' if pg['outdoors'] else 'indoor'} map" + (f", {region[0].lower() + region[1:]}" if region else '') + ". "
                    + (f"It has {len(npcs)} NPC{'s' if len(npcs) != 1 else ''}" if npcs else "It has no NPCs")
                    + (f" and {len(enemies)} kind{'s' if len(enemies) != 1 else ''} of enemy" if enemies else ", and no enemies") + ". "
                    + (f"Exits lead to {', '.join(_pretty(d) for d in dests[:4])}" + (f" and {len(dests) - 4} more" if len(dests) > 4 else '') + '.' if dests else ''))
        legend = ''.join(f'<label class="lg"><input type="checkbox" data-t="{k}"{" checked" if on else ""}>'
                         f'<span class="sw sw-{k}"></span><b>{color}</b>&nbsp;{label}</label>' for k, color, label, on in LEGEND + PIN_LEGEND)
        hidden = ' '.join(f'hide-{k}' for k, _, _, on in LEGEND + PIN_LEGEND if not on)
        _d = (f"{_pretty(m)} is {'an outdoor' if pg['outdoors'] else 'an indoor'} location in Andor's Trail" + (f", {region[0].lower() + region[1:]}" if region else '') + ". "
              + (f"NPCs: {', '.join(monsters[x].get('name') or x for x in npcs[:5])}. " if npcs else '')
              + (f"Enemies: {', '.join(dict.fromkeys(monsters[x].get('name') or x for x in enemies[:5]))}. " if enemies else '')
              + (f"Exits to {', '.join(_pretty(d) for d in dests[:4])}." if dests else ''))
        P = ['---\ndescription: ' + __import__('json').dumps(_d[:297] + ('…' if len(_d) > 297 else ''), ensure_ascii=False) + '\n---\n\n', f"# {_pretty(m)}\n\n",
             '<div class="infobox" markdown>\n\n| | |\n|---|---|\n' + ''.join(f"| **{a}** | {b} |\n" for a, b in info if b) + '\n</div>\n\n',
             overview + "\n\n",
             "## Map\n\n",
             f'<div class="map-legend" markdown="0">{legend}</div>\n\n',
             f'<div class="map-wrap {hidden}" markdown="0"><img src="../../assets/maps/{m}.webp" alt="Map of {_esc(_pretty(m))}" width="{W}" height="{H}" loading="lazy">'
             f'{"".join(pg["boxes"])}{"".join(mobs)}{"".join(pins)}</div>\n\n']
        if key:
            P.append("??? abstract \"Key to the numbers on the map\"\n\n    | # | What | Details |\n    |---|---|---|\n" +
                     ''.join(f"    | <span id=\"key-{n}\"></span>{n} | {what.replace('../../', '../')} | {md(detail).replace('../../', '../')} |\n" for n, what, detail in key) + "\n")
        P.append(ctx['verified']("map data", VERSION))
        if conn:
            P.append("## Connections\n\n| Direction | Leads to | Region there | Map # |\n|---|---|---|---|\n")
            for (d, dest), nums in sorted(conn.items(), key=lambda kv: (DIR_ORDER.index(kv[0][0]) if kv[0][0] in DIR_ORDER else 99, kv[0][1])):
                da = pages.get(dest, {}).get('area', (None, None, None))
                P.append(f"| {d} | [{_pretty(dest)}]({dest}.md) | {da[0] or '–'} | {', '.join(map(str, nums))} |\n")
            P.append("\n")
        if npcs:
            P.append("## NPCs\n\n" + ''.join(
                f"- [{md(monsters[x].get('name', x))}](../monsters/{x}.md)" + (" — shopkeeper" if x in shopkeepers else '') +
                (" — can be fought" if ctx.get('kind_of') and ctx['kind_of'](x) == 'NPC/Enemy' else '') +
                (f" — quests: {', '.join(QG.qlink(q, None, '../quests/') for q in sorted(npc_quests[x], key=lambda q: QG.quests[q].get('name', q)) if QG.quests[q].get('showInLog', 0))}"
                 if any(QG.quests[q].get('showInLog', 0) for q in npc_quests[x]) else '') +
                (f" (#{npc_num[x]})" if npc_num.get(x) else '') + "\n" for x in npcs) + "\n")
        if enemies:
            maxq = defaultdict(int); later = set(); shared = defaultdict(set)
            for o, ms, active, qty in pg['spawns']:
                for x in ms:
                    maxq[x] += qty
                    if not active: later.add(x)
                    if len(ms) > 1: shared[x].update(y for y in ms if y != x)
            P.append("## Enemies\n\n| Enemy | HP | Damage | Up to | Notes |\n|---|---|---|---|---|\n")
            for x in enemies:
                mm = monsters[x]; dmg = mm.get('attackDamage', {})
                notes_ = []
                if x in later: notes_.append('appears later, during a quest')
                if shared[x]: notes_.append('shares spawn with ' + ', '.join(sorted({monsters[y].get('name', y) for y in shared[x]}))[:120])
                P.append(f"| [{md(mm.get('name', x))}](../monsters/{x}.md) | {mm.get('maxHP', 0)} | {dmg.get('min', 0)}–{dmg.get('max', 0)} | {maxq[x]} | {'; '.join(notes_) or '–'} |\n")
            P.append("\n<small>“Up to” is the most that can be alive at once from the spawn areas on this map.</small>\n\n")
        shops = [x for x in npcs if x in shopkeepers]
        if pg['containers'] or shops:
            P.append("## Items & containers\n\n")
            if shops: P.append("**Shops:** " + ', '.join(f"[{md(monsters[x].get('name', x))}](../monsters/{x}.md)" for x in shops) + "\n\n")
            for k, (cid, dl) in enumerate(pg['containers']):
                rows = ''.join(
                    f'<li><a href="../../items/{e["itemID"]}/">' + (f'<img class="sprite" src="../../{ctx["item_icon"](e["itemID"])}" alt="">' if ctx['item_icon'](e['itemID']) else '') +
                    f'{_esc(items.get(e["itemID"], {}).get("name", e["itemID"]))}</a> <small>{_esc(ctx["chance_txt"](e.get("chance")))}'
                    + (f' · ×{_esc(ctx["rng"](e.get("quantity")))}' if e.get('quantity') and ctx['rng'](e.get('quantity')) != '1' else '') + '</small></li>'
                    for e in dl.get('items', []))
                P.append(f'<div class="container-list" id="container-{k}" markdown="0"><b>Container {k + 1}</b><ul>{rows}</ul></div>\n\n')
        if qlist:
            P.append("## Quests\n\n" + ''.join(f"- {QG.qlink(q, None, '../quests/')}: {'; '.join(sorted(quests_here[q]))}\n" for q in qlist[:40]) + "\n")
        poi_kinds = [p for p in pg['pois'] if p['kind'] in ('sign', 'rest', 'key', 'script', 'replace')]
        if poi_kinds:
            P.append("## Points of interest\n\n")
            seen_poi = set()
            for p in poi_kinds:
                k2 = (p['label'], p.get('detail', ''))
                if k2 in seen_poi: continue
                seen_poi.add(k2)
                n = key_num.get(k2)
                P.append(f"- **{p['label']}**{f' (#{n})' if n else ''}: {md(p.get('detail', '')).replace('../../', '../')}\n")
            P.append("\n")
        if ctx.get('history'): P.append(ctx['history']('maps', m, (), ''))
        P.append(notes('maps', m, _pretty(m)))
        from collections import Counter
        objc = Counter(o['type'] or 'other' for o in t['objects'])
        tech = [('Map ID', f"`{m}`"), ('File', f"`res/xml/{m}.tmx`"), ('Size', f"{t['w']}×{t['h']} tiles ({W}×{H} px)"),
                ('outdoors property', t['props'].get('outdoors', '–')),
                ('Layers drawn', ', '.join(n for n, _ in t['layers'])),
                ('Tilesets', ', '.join(sorted({os.path.basename(src).replace('.png', '') for _, src, _ in t['tilesets']}))),
                ('Map objects', ', '.join(f"{k}: {v}" for k, v in objc.most_common())),
                ('World map position', f"segment `{seg[0]}`, x {seg[1]}, y {seg[2]}" if seg and seg[1] is not None else '–')]
        P.append('\n??? info "Technical information"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {a} | {b} |\n" for a, b in tech) + '\n')
        P.append(f"\n<small>Data from v{VERSION}</small>\n")
        write(f'maps/{m}.md', ''.join(P))


PIN_LEGEND = [('pin', 'Numbers', 'Numbered key points (see the key below the map)', True)]
