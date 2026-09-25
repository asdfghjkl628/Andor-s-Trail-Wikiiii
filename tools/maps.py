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

def _pretty(name): return name.replace('_', ' ').strip().capitalize()
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
    idx = [f"# World map\n\nEvery region of Andor's Trail v{ctx['VERSION']}, assembled from the game's own map files. "
           "Hover to see a map's name; click it to open that map.\n"] + [s[1] for s in seg_md]
    idx.append("\n## All maps (A–Z)\n\n" + ''.join(f"- [{_pretty(m)}]({m}.md)\n" for m in sorted(parsed)))
    ctx['write']('maps/index.md', ''.join(idx))

    # ------------------------------------------------ one page per map
    for m, t in parsed.items():
        W, H = t['w'] * TILE, t['h'] * TILE
        pct = lambda x, y, w, h: f"left:{x/W*100:.3f}%;top:{y/H*100:.3f}%;width:{max(w,8)/W*100:.3f}%;height:{max(h,8)/H*100:.3f}%"
        mlink = f'[{_pretty(m)}](../maps/{m}.md)'
        boxes, mobs, here, exits, containers, spawns = [], [], set(), [], [], []
        for n, o in enumerate(t['objects']):
            typ = o['type']
            if typ not in LEGEND_TYPES: continue
            tip, href, attrs, extra_cls = _pretty(o['name']), None, '', ''
            if typ == 'spawn':
                ms = spawn_mids(o)
                active = str(o['props'].get('active', 'true')).lower() != 'false'
                here.update(ms); spawns.append((o, ms, active))
                for x in ms: spawn_maps[x].add(m)
                names = sorted({monsters[x].get('name', x) for x in ms})
                tip = 'Spawns: ' + (', '.join(names) if names else o['name']) + ('' if active else ' (only appears later, during a quest)')
            elif typ == 'mapchange':
                dest, place = o['props'].get('map'), o['props'].get('place')
                attrs = f' id="place-{_esc(o["name"])}"'
                if dest:
                    tip = f'Exit to {_pretty(dest)}'; href = f'../{dest}/' + (f'#place-{place}' if place else '')
                    exits.append(dest)
            elif typ == 'container':
                dl = droplists.get(o['name'])
                if not dl: continue
                k = len(containers); containers.append(dl)
                tip = 'Container: click to see what\'s inside'; href = f'#container-{k}'
                attrs = f' data-container="container-{k}"'
            elif typ == 'sign':
                tip = 'Sign: ' + (convs.get(o['name'], {}).get('message') or o['name'])
            elif typ == 'rest':
                tip = 'Resting place (respawn point)'
            elif typ == 'key':
                p = o['props']
                val = int(p.get('requireValue') or 0) if str(p.get('requireValue', '0')).lstrip('-').isdigit() else 0
                neg = str(p.get('requireNegation', 'false')).lower() == 'true'
                tip, href = QI.req(p.get('requireType'), p.get('requireId'), val, neg,
                                   'Unlocked during', 'Closed off once you reach this point in')
                if (p.get('requireType') or 'questProgress').startswith('quest'):
                    QI.note(p.get('requireId'), val, f"🔓 You can finally access a previously blocked area on {mlink}." if not neg
                            else f"🔒 An area on {mlink} becomes blocked off.")
            elif typ == 'replace':
                p = o['props']
                if p.get('requireType') or p.get('requireId'):
                    val = int(p.get('requireValue') or 0) if str(p.get('requireValue', '0')).lstrip('-').isdigit() else 0
                    neg = str(p.get('requireNegation', 'false')).lower() == 'true'
                    tip, href = QI.req(p.get('requireType'), p.get('requireId'), val, neg,
                                       'This area changes during', 'This area changes back during')
                    if (p.get('requireType') or 'questProgress').startswith('quest'):
                        QI.note(p.get('requireId'), val, f"🗺️ Part of {mlink} visibly changes.")
                else:
                    tip = 'This area changes when a scripted event activates it'
            elif typ == 'script':
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
                elif reqs:
                    qid, val, neg = reqs[0]
                    tip = f"Scripted event that only happens during the quest: {QI.name(qid)} (stage {val})"
                    href = QI.url(qid, val) if qid in QI.q else None
                    for q2, v2, n2 in set(reqs):
                        if not n2: QI.note(q2, v2, f"⚡ A scripted event can now trigger on {mlink}.")
                else:
                    tip = 'Scripted event' + (': ' + other[0] if other else (': “' + first[:90] + ('…' if len(first) > 90 else '') + '”' if first else ''))
            tag = 'a' if href else 'span'
            h = f' href="{_esc(href)}"' if href else ''
            boxes.append(f'<{tag}{attrs} class="mo mo-{typ}{extra_cls}"{h} title="{_esc(tip)}" style="{pct(o["x"], o["y"], o["w"], o["h"])}"></{tag}>')

        # monsters standing in their spawn areas
        for mid, x, y, fw, fh, active in _place_monsters(t, spawns, ctx, seed=m):
            ic = ctx['monster_icon'](mid)
            if not ic: continue
            nm = monsters[mid].get('name', mid)
            mobs.append(f'<a class="mob{"" if active else " mob-later"}" href="../../monsters/{mid}/" title="{_esc(nm + ("" if active else " (appears later in a quest)"))}" '
                        f'style="{pct(x*TILE, y*TILE, fw*TILE, fh*TILE)}"><img src="../../{ic}" alt="{_esc(nm)}"></a>')

        legend = ''.join(f'<label class="lg"><input type="checkbox" data-t="{k}"{" checked" if on else ""}>'
                         f'<span class="sw sw-{k}"></span><b>{color}</b>&nbsp;{label}</label>' for k, color, label, on in LEGEND)
        hidden = ' '.join(f'hide-{k}' for k, _, _, on in LEGEND if not on)
        P = [f"# {_pretty(m)}\n\n",
             f"{t['w']}×{t['h']} tiles" + (" · outdoors" if t['props'].get('outdoors') == '1' else '') +
             (f" · part of [{_pretty(on_world[m])}](index.md)" if m in on_world else '') + "\n\n",
             f'<div class="map-legend" markdown="0">{legend}</div>\n\n',
             f'<div class="map-wrap {hidden}" markdown="0"><img src="../../assets/maps/{m}.webp" alt="{m}" width="{W}" height="{H}" loading="lazy">{"".join(boxes)}{"".join(mobs)}</div>\n\n']
        if containers:
            P.append("## Containers\n\n")
            for k, dl in enumerate(containers):
                rows = ''.join(
                    f'<li><a href="../../items/{e["itemID"]}/">' + (f'<img class="sprite" src="../../{ctx["item_icon"](e["itemID"])}" alt="">' if ctx['item_icon'](e['itemID']) else '') +
                    f'{_esc(items.get(e["itemID"], {}).get("name", e["itemID"]))}</a> <small>{_esc(ctx["chance_txt"](e.get("chance")))}'
                    + (f' · ×{_esc(ctx["rng"](e.get("quantity")))}' if e.get('quantity') and ctx['rng'](e.get('quantity')) != '1' else '') + '</small></li>'
                    for e in dl.get('items', []))
                P.append(f'<div class="container-list" id="container-{k}" markdown="0"><b>Container {k + 1}</b><ul>{rows}</ul></div>\n\n')
        if exits:
            P.append("## Exits\n\n" + ''.join(f"- [{_pretty(d)}]({d}.md)\n" for d in sorted(set(exits))) + '\n')
        if here:
            P.append("## Monsters & NPCs here\n\n| Name | HP |\n|---|---|\n" + ''.join(
                f"| [{ctx['md_esc'](monsters[x].get('name', x))}](../monsters/{x}.md) | {monsters[x].get('maxHP', 0)} |\n"
                for x in sorted(here, key=lambda x: monsters[x].get('maxHP', 0))))
        P.append(f"\n<small>Map ID: `{m}` · Data from v{ctx['VERSION']}</small>\n")
        ctx['write'](f'maps/{m}.md', ''.join(P))
    return spawn_maps, len(parsed), QI.notes
