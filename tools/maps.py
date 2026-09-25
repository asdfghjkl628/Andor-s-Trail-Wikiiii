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
    objects = []
    for og in root.findall('objectgroup'):
        for o in og.findall('object'):
            props = {p.get('name'): p.get('value') for p in o.iter('property')}
            objects.append(dict(type=(o.get('type') or '').lower(), name=o.get('name') or '',
                                x=float(o.get('x', 0)), y=float(o.get('y', 0)),
                                w=float(o.get('width', TILE)), h=float(o.get('height', TILE)), props=props))
    mprops = {p.get('name'): p.get('value') for p in root.find('properties').iter('property')} if root.find('properties') is not None else {}
    return dict(w=w, h=h, tilesets=tilesets, layers=layers, objects=objects, props=mprops)

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

LEGEND = [('spawn', 'Monsters / NPCs', True), ('mapchange', 'Exit to another map', True), ('container', 'Container', True),
          ('sign', 'Sign', True), ('rest', 'Resting place', True), ('key', 'Blocked / needs key or quest', True),
          ('script', 'Scripted event', False), ('replace', 'Changes after a quest', False)]

def _pretty(name): return name.replace('_', ' ').strip().capitalize()

def build_maps(ctx):
    """ctx: dict with GAME, DOCS, VERSION, monsters, droplists, items, conversations, group_to_monsters, write, md_esc."""
    GAME, DOCS = ctx['GAME'], ctx['DOCS']
    monsters, droplists, items, convs = ctx['monsters'], ctx['droplists'], ctx['items'], ctx['conversations']
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
        thumbs[m] = full.convert('RGB').resize((t['w'] * 4, t['h'] * 4), Image.BILINEAR)  # 4px per tile for the world map
        sizes[m] = (t['w'], t['h'])
        for o in t['objects']:
            if o['type'] == 'spawn':
                grp = o['props'].get('spawngroup', o['name'])
                for mid in ctx['group_to_monsters'].get(grp, []) or ([grp] if grp in monsters else []):
                    spawn_maps[mid].add(m)

    # ------------------------------------------------ world map segments
    wm = ET.parse(os.path.join(xml_dir, 'worldmap.xml')).getroot()
    on_world = {}
    seg_md = []
    for seg in wm.findall('segment'):
        entries = [(mp.get('id'), int(mp.get('x')), int(mp.get('y'))) for mp in seg.findall('map') if mp.get('id') in thumbs]
        if not entries: continue
        minx = min(x for _, x, _ in entries); miny = min(y for _, _, y in entries)
        maxx = max(x + sizes[i][0] for i, x, _ in entries); maxy = max(y + sizes[i][1] for i, _, y in entries)
        W, H = (maxx - minx) * 4, (maxy - miny) * 4
        canvas = Image.new('RGB', (W, H), (24, 20, 16))
        zones = []
        for mid, x, y in entries:
            canvas.paste(thumbs[mid], ((x - minx) * 4, (y - miny) * 4))
            on_world[mid] = seg.get('id')
            zones.append(f'<a class="wm-zone" href="{mid}/" title="{html.escape(_pretty(mid))}" style="left:{(x-minx)/(maxx-minx)*100:.3f}%;top:{(y-miny)/(maxy-miny)*100:.3f}%;width:{sizes[mid][0]/(maxx-minx)*100:.3f}%;height:{sizes[mid][1]/(maxy-miny)*100:.3f}%"></a>')
        seg_id = seg.get('id')
        canvas.save(os.path.join(DOCS, 'assets', 'maps', f'_world_{seg_id}.webp'), 'WEBP', quality=70)
        seg_md.append((len(entries), seg_id,
            f'\n## {_pretty(seg_id)}\n\n<div class="map-wrap world" markdown="0"><img src="../assets/maps/_world_{seg_id}.webp" alt="{seg_id}" loading="lazy">{"".join(zones)}</div>\n'))
    seg_md.sort(key=lambda s: -s[0])  # largest region (the overworld) first

    idx = [f"# World map\n\nEvery region of Andor's Trail v{ctx['VERSION']}, assembled from the game's own map files. "
           "Hover to see a map's name; click it to open that map.\n"]
    idx += [s[2] for s in seg_md]
    idx.append("\n## All maps (A–Z)\n\n" + ''.join(f"- [{_pretty(m)}]({m}.md)\n" for m in sorted(parsed)))
    ctx['write']('maps/index.md', ''.join(idx))

    # ------------------------------------------------ one page per map
    for m, t in parsed.items():
        W, H = t['w'] * TILE, t['h'] * TILE
        boxes, here, exits = [], set(), []
        for n, o in enumerate(t['objects']):
            typ = o['type'] if o['type'] in dict((l[0], 1) for l in LEGEND) else None
            if not typ: continue
            style = f"left:{o['x']/W*100:.3f}%;top:{o['y']/H*100:.3f}%;width:{max(o['w'],8)/W*100:.3f}%;height:{max(o['h'],8)/H*100:.3f}%"
            tip, href, anchor = _pretty(o['name']), None, ''
            if typ == 'spawn':
                grp = o['props'].get('spawngroup', o['name'])
                ms = ctx['group_to_monsters'].get(grp, []) or ([grp] if grp in monsters else [])
                here.update(ms)
                names = sorted({monsters[x].get('name', x) for x in ms})
                tip = 'Spawns: ' + (', '.join(names) if names else grp)
                if len(ms) == 1: href = f'../../monsters/{ms[0]}/'
            elif typ == 'mapchange':
                dest, place = o['props'].get('map'), o['props'].get('place')
                anchor = f' id="place-{html.escape(o["name"])}"'
                if dest:
                    tip = f'Exit to {_pretty(dest)}'; href = f'../{dest}/#place-{place}' if place else f'../{dest}/'
                    exits.append(dest)
            elif typ == 'container':
                dl = droplists.get(o['name'], {})
                tip = 'Container: ' + (', '.join(items.get(e['itemID'], {}).get('name', e['itemID']) for e in dl.get('items', [])) or o['name'])
            elif typ == 'sign':
                c = convs.get(o['name'], {})
                tip = 'Sign: ' + (c.get('message') or o['name'])
            elif typ == 'rest':
                tip = 'Resting place (respawn point)'
            elif typ == 'key':
                req = o['props']
                tip = 'Blocked: ' + (f"needs {req.get('requireType','')} {req.get('requireId','')} {req.get('requireValue','')}".strip() if req else o['name'])
            tag = 'a' if href else 'span'
            h = f' href="{href}"' if href else ''
            boxes.append(f'<{tag}{anchor} class="mo mo-{typ}"{h} title="{html.escape(tip)}" style="{style}"></{tag}>')
        legend = ''.join(f'<label class="lg lg-{k}"><input type="checkbox" data-t="{k}"{" checked" if on else ""}> {label}</label>'
                         for k, label, on in LEGEND)
        hidden = ' '.join(f'hide-{k}' for k, _, on in LEGEND if not on)
        P = [f"# {_pretty(m)}\n\n",
             f"{t['w']}×{t['h']} tiles" + (" · outdoors" if t['props'].get('outdoors') == '1' else '') +
             (f" · part of [{_pretty(on_world[m])}](index.md)" if m in on_world else '') + "\n\n",
             f'<div class="map-legend" markdown="0">{legend}</div>\n\n',
             f'<div class="map-wrap {hidden}" markdown="0"><img src="../../assets/maps/{m}.webp" alt="{m}" width="{W}" height="{H}" loading="lazy">{"".join(boxes)}</div>\n\n']
        if exits:
            P.append("## Exits\n\n" + ''.join(f"- [{_pretty(d)}]({d}.md)\n" for d in sorted(set(exits))) + '\n')
        if here:
            P.append("## Monsters & NPCs here\n\n| Name | HP |\n|---|---|\n" + ''.join(
                f"| [{ctx['md_esc'](monsters[x].get('name', x))}](../monsters/{x}.md) | {monsters[x].get('maxHP', 0)} |\n"
                for x in sorted(here, key=lambda x: monsters[x].get('maxHP', 0))))
        P.append(f"\n<small>Map ID: `{m}` · Data from v{ctx['VERSION']}</small>\n")
        ctx['write'](f'maps/{m}.md', ''.join(P))
    return spawn_maps, len(parsed)
