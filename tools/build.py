#!/usr/bin/env python3
"""Andor's Trail wiki builder.

Usage: python tools/build.py <path-to-game-repo-checkout> <version-string>

Reads the game's own data (only the files the game itself loads, per
res/values/loadresources.xml), cross-references it, and writes:
  data/snapshot.json   - normalized data (used to diff the next release)
  docs/**              - MkDocs pages, including cropped item/monster icons
  docs/changelog.md    - prepended with a diff vs. the previous snapshot
"""
import json, os, re, sys, glob, shutil, html
from collections import defaultdict
import xml.etree.ElementTree as ET

REPO, VERSION = sys.argv[1], sys.argv[2]
GAME = os.path.join(REPO, 'AndorsTrail')
RAW = os.path.join(GAME, 'res', 'raw')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
DATA = os.path.join(ROOT, 'data')
JAVA = os.path.join(GAME, 'app', 'src', 'main', 'java', 'com', 'gpl', 'rpg', 'AndorsTrail')

# ---------------------------------------------------------------- loading
def loaded_files(kind):
    """Files the game actually loads for a resource kind (skips debug/test data)."""
    tree = ET.parse(os.path.join(GAME, 'res', 'values', 'loadresources.xml'))
    for arr in tree.getroot():
        if arr.get('name') == f'loadresource_{kind}':
            return [os.path.join(RAW, i.text.split('/')[-1] + '.json') for i in arr if i.text]
    return sorted(glob.glob(os.path.join(RAW, f'{kind}_*.json')))

def load_all(kind):
    out = {}
    for f in loaded_files(kind):
        if os.path.exists(f):
            for obj in json.load(open(f, encoding='utf-8')):
                out[obj['id']] = obj
    return out

strings = {}
for s in ET.parse(os.path.join(GAME, 'res', 'values', 'strings.xml')).getroot().iter('string'):
    strings[s.get('name')] = ''.join(s.itertext()).replace("\\'", "'").replace('\\n', '\n')

items = load_all('itemlist')
cats = load_all('itemcategories')
monsters = load_all('monsterlist')
droplists = load_all('droplists')
quests = load_all('questlist')
conditions = load_all('actorconditions')
conversations = {}
for f in loaded_files('conversationlist'):
    if os.path.exists(f):
        for c in json.load(open(f, encoding='utf-8')):
            conversations[c['id']] = c

# ---------------------------------------------------------------- skills (from Java source)
sc = open(os.path.join(JAVA, 'model', 'ability', 'SkillCollection.java'), encoding='utf-8').read()
consts = {}
def _java_eval(expr, env):
    e = expr.replace('(int)', '').replace('(float)', '').replace('Math.floor', 'floor').replace('Math.max', 'max')
    e = re.sub(r'Constants\.(\w+)', lambda m: str(env.get('C_' + m.group(1), 0)), e)
    return int(eval(e, {'floor': __import__('math').floor, 'max': max}, env))
cst = open(os.path.join(JAVA, 'controller', 'Constants.java'), encoding='utf-8').read()
for name, expr in re.findall(r'static final (?:int|float) (\w+) = ([^;]+);', cst):
    try: consts['C_' + name] = _java_eval(expr, consts)
    except Exception: pass
for name, expr in re.findall(r'(?:public|private) static final int (\w+) = ([^;]+);', sc, re.S):
    try: consts[name] = _java_eval(' '.join(expr.split()), consts)
    except Exception: pass
SKILL_STRING_KEY = {  # enum name -> strings.xml suffix
 'weaponChance':'weapon_chance','weaponDmg':'weapon_dmg','barter':'barter','dodge':'dodge','barkSkin':'barkskin',
 'moreCriticals':'more_criticals','betterCriticals':'better_criticals','speed':'speed','coinfinder':'coinfinder',
 'moreExp':'more_exp','cleave':'cleave','eater':'eater','fortitude':'fortitude','evasion':'evasion',
 'regeneration':'regeneration','lowerExploss':'lower_exploss','magicfinder':'magicfinder',
 'resistanceMental':'resistance_mental','resistancePhysical':'resistance_physical_capacity',
 'resistanceBlood':'resistance_blood_disorder','shadowBless':'shadow_bless','crit1':'crit1','crit2':'crit2',
 'rejuvenation':'rejuvenation','taunt':'taunt','concussion':'concussion',
 'weaponProficiencyDagger':'weapon_prof_dagger','weaponProficiency1hsword':'weapon_prof_1hsword',
 'weaponProficiency2hsword':'weapon_prof_2hsword','weaponProficiencyAxe':'weapon_prof_axe',
 'weaponProficiencyBlunt':'weapon_prof_blunt','weaponProficiencyUnarmed':'weapon_prof_unarmed',
 'weaponProficiencyPole':'weapon_prof_pole','armorProficiencyShield':'armor_prof_shield',
 'armorProficiencyUnarmored':'armor_prof_unarmored','armorProficiencyLight':'armor_prof_light',
 'armorProficiencyHeavy':'armor_prof_heavy','fightstyleDualWield':'fightstyle_dualwield',
 'fightstyle2hand':'fightstyle_2hand','fightstyleWeaponShield':'fightstyle_weapon_shield',
 'fightstyleUnarmedUnarmored':'fightstyle_unarmed_unarmored','specializationDualWield':'specialization_dualwield',
 'specialization2hand':'specialization_2hand','specializationWeaponShield':'specialization_weapon_shield',
 'sporeImmunity':'spore_immunity'}
skills = {}
for m in re.finditer(r'new SkillInfo\(SkillID\.(\w+),\s*([\w.]+),\s*SkillInfo\.LevelUpType\.(\w+),\s*SkillCategory\.(\w+),\s*(null|new SkillLevelRequirement\[\]\s*\{(.*?)\})', sc, re.S):
    sid, maxl, lut, cat, _, reqs = m.groups()
    maxl = 'unlimited' if maxl.endswith('MAXLEVEL_NONE') else (int(maxl) if maxl.isdigit() else consts.get(maxl, maxl))
    req_list = []
    for r in re.findall(r'SkillLevelRequirement\.(\w+)\(([^)]*)\)', reqs or ''):
        kind, args = r
        a = [x.strip() for x in args.split(',')]
        if kind == 'requireOtherSkill': req_list.append(('skill', a[0].split('.')[-1], int(a[1])))
        elif kind == 'requireExperienceLevels': req_list.append(('level', int(a[0]), int(a[1])))
        elif kind == 'requirePlayerStats': req_list.append(('stat', a[0].split('.')[-1], int(a[1]), int(a[2])))
    k = SKILL_STRING_KEY.get(sid, sid)
    skills[sid] = dict(id=sid, name=strings.get(f'skill_title_{k}', sid), maxLevel=maxl, levelUpType=lut,
                       category=cat, requirements=req_list,
                       short=strings.get(f'skill_shortdescription_{k}', ''),
                       long=strings.get(f'skill_longdescription_{k}', ''))

# ---------------------------------------------------------------- cross references
# map spawns are computed by tools/maps.py (which also renders the maps)
group_to_monsters = defaultdict(list)
for mid, m in monsters.items():
    group_to_monsters[m.get('spawnGroup', mid)].append(mid)

# shopkeepers: NPCs whose dialogue can reach the shop screen ("S")
def reaches_shop(start, limit=400):
    seen, stack = set(), [start]
    while stack and len(seen) < limit:
        pid = stack.pop()
        if pid == 'S': return True
        if pid in seen or pid not in conversations: continue
        seen.add(pid)
        for r in conversations[pid].get('replies', []) or []:
            if r.get('nextPhraseID'): stack.append(r['nextPhraseID'])
    return False
shopkeepers = {mid for mid, m in monsters.items() if m.get('phraseID') and reaches_shop(m['phraseID'])}
sold_by = defaultdict(list)
# drops: item -> [(monster, chance, qty)]
dropped_by = defaultdict(list)
for mid, m in monsters.items():
    dl = droplists.get(m.get('droplistID'))
    for e in (dl or {}).get('items', []):
        q = e.get('quantity', {})
        (sold_by if mid in shopkeepers else dropped_by)[e['itemID']].append((mid, str(e.get('chance', '')), f"{q.get('min', 1)}-{q.get('max', 1)}" if q.get('min') != q.get('max') else str(q.get('min', 1))))

# skills granted by conversations (quest rewards)
skill_sources = defaultdict(set)
for cid, c in conversations.items():
    for r in c.get('rewards', []) or []:
        if r.get('rewardType') == 'skillIncrease':
            skill_sources[r['rewardID']].add(cid)

# ---------------------------------------------------------------- icons
tilesets = {}
rl = open(os.path.join(JAVA, 'resource', 'ResourceLoader.java'), encoding='utf-8').read()
sizes = {f'sz{a}x{b}': (int(a), int(b)) for a, b in re.findall(r'sz(\d+)x(\d+) = new Size', rl)}
for name, grid in re.findall(r'prepareTileset\(R\.drawable\.\w+,\s*"(\w+)",\s*(new Size\(\d+,\s*\d+\)|sz\d+x\d+)', rl):
    g = re.findall(r'\d+', grid) if grid.startswith('new') else sizes.get(grid)
    tilesets[name] = tuple(int(x) for x in g)

def icon(icon_id, kind):
    """Crop a sprite to docs/assets/icons/<kind>/<sheet>_<n>.png; return site-relative path or None."""
    if not icon_id or ':' not in icon_id: return None
    sheet, idx = icon_id.split(':'); idx = int(idx)
    rel = f'assets/icons/{kind}/{sheet}_{idx}.png'
    out = os.path.join(DOCS, rel)
    if os.path.exists(out): return rel
    src = os.path.join(GAME, 'res', 'drawable', sheet + '.png')
    if sheet not in tilesets or not os.path.exists(src): return None
    try:
        from PIL import Image
        img = Image.open(src); cols, rows = tilesets[sheet]
        w, h = img.width // cols, img.height // rows
        x, y = (idx % cols) * w, (idx // cols) * h
        os.makedirs(os.path.dirname(out), exist_ok=True)
        img.crop((x, y, x + w, y + h)).save(out)
        return rel
    except Exception:
        return None

# ---------------------------------------------------------------- formatting helpers
LABELS = {'increaseMaxHP':'Max HP','increaseMaxAP':'Max AP','increaseMoveCost':'Move cost','increaseAttackCost':'Attack cost',
 'increaseAttackChance':'Attack chance','increaseCriticalSkill':'Critical skill','setCriticalMultiplier':'Critical multiplier',
 'increaseAttackDamage':'Attack damage','increaseBlockChance':'Block chance','increaseDamageResistance':'Damage resistance',
 'increaseUseItemCost':'Use item cost','increaseReequipCost':'Re-equip cost','increaseCurrentHP':'Heal HP',
 'increaseCurrentAP':'Restore AP','addedConditions':'Grants','conditionsSource':'On self','conditionsTarget':'On target'}
def rng(v):
    if isinstance(v, dict) and 'min' in v:
        return str(v['min']) if v.get('min') == v.get('max') else f"{v.get('min')} to {v.get('max')}"
    return str(v)
def cond_text(clist):
    parts = []
    for c in clist:
        name = conditions.get(c.get('condition'), {}).get('name', c.get('condition'))
        bits = [f"magnitude {c['magnitude']}" if 'magnitude' in c else '', f"{c['duration']} rounds" if c.get('duration') else '',
                f"{c['chance']}% chance" if 'chance' in c else '']
        parts.append(f"{name} ({', '.join(b for b in bits if b)})")
    return '; '.join(parts)
def effect_rows(eff):
    rows = []
    for k, v in (eff or {}).items():
        label = LABELS.get(k, k)
        val = cond_text(v) if isinstance(v, list) else rng(v)
        if isinstance(v, (int, float)) and not isinstance(v, bool) and k != 'setCriticalMultiplier' and v > 0: val = f'+{v}'
        rows.append((label, val))
    return rows
def chance_pct(c):
    c = str(c).strip()
    try:
        if '/' in c:
            a, b = c.split('/'); return float(a) / float(b) * 100
        return float(c)
    except ValueError:
        return 0.0
def chance_txt(c):
    v = chance_pct(c); return f"{v:g}%" if v >= 1 else f"{v:.2g}%"
def md_esc(s): return str(s).replace('|', '\\|').replace('\n', ' ')
def link(kind, oid, text): return f'[{md_esc(text)}](../{kind}/{oid}.md)'
def img(rel, depth=1):
    return f'![](' + '../' * depth + rel + '){ .sprite }' if rel else ''

# ---------------------------------------------------------------- page writers
def write(path, text):
    full = os.path.join(DOCS, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(text)

for d in ('items', 'monsters', 'quests', 'skills', 'maps', 'assets/maps'):
    shutil.rmtree(os.path.join(DOCS, d), ignore_errors=True)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from maps import build_maps
spawn_maps, n_maps = build_maps(dict(GAME=GAME, DOCS=DOCS, VERSION=VERSION, monsters=monsters, droplists=droplists,
    items=items, conversations=conversations, group_to_monsters=group_to_monsters, write=write, md_esc=md_esc))

def item_kind(it):
    c = cats.get(it.get('category'), {})
    if c.get('actionType') == 'equip': return 'Equipment'
    if c.get('actionType') == 'use': return 'Consumable'
    return 'Other'

item_rows = []
for iid, it in sorted(items.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
    c = cats.get(it.get('category'), {})
    ic = icon(it.get('iconID'), 'items')
    L = [f"# {img(ic)} {it.get('name', iid)}\n", f"*{it.get('displaytype', 'ordinary').capitalize()}* · {c.get('name', it.get('category', '?'))} · value {it.get('baseMarketCost', 0)} gold\n\n"]
    if it.get('description'): L.append(f"> {it['description']}\n\n")
    if c.get('inventorySlot'): L.append(f"**Slot:** {c['inventorySlot']}" + (f" · **Size:** {c['size']}" if c.get('size') else '') + '\n\n')
    for title, key in (('When equipped', 'equipEffect'), ('When used', 'useEffect'), ('On hit', 'hitEffect'),
                       ('On kill', 'killEffect'), ('When hit', 'hitReceivedEffect')):
        rows = effect_rows(it.get(key))
        if rows:
            L.append(f"\n## {title}\n\n| Stat | Value |\n|---|---|\n" + ''.join(f"| {md_esc(a)} | {md_esc(b)} |\n" for a, b in rows))
    srcs = dropped_by.get(iid, [])
    if srcs:
        L.append("\n## Dropped by\n\n| Monster | Chance | Qty |\n|---|---|---|\n")
        for mid, ch, q in sorted(srcs, key=lambda s: -chance_pct(s[1])):
            L.append(f"| {link('monsters', mid, monsters[mid].get('name', mid))} | {chance_txt(ch)} | {q} |\n")
    if sold_by.get(iid):
        L.append("\n## Sold by\n\n" + ''.join(f"- {link('monsters', mid, monsters[mid].get('name', mid))}\n" for mid, _, _ in sold_by[iid]))
    L.append(f"\n<small>Item ID: `{iid}` · Data from v{VERSION}</small>\n")
    write(f'items/{iid}.md', ''.join(L))
    item_rows.append((it, c, ic))

# items index, grouped by kind then category
groups = defaultdict(list)
for it, c, ic in item_rows:
    groups[(item_kind(it), c.get('name', it.get('category', 'Uncategorized')))].append((it, ic))
L = [f"# Items\n\nEvery item in Andor's Trail v{VERSION} ({len(items)} total). Use the search box to find one quickly.\n"]
for kind in ('Equipment', 'Consumable', 'Other'):
    L.append(f"\n## {kind}\n")
    for (k, cname), lst in sorted(groups.items()):
        if k != kind: continue
        L.append(f"\n### {cname}\n\n| | Item | Rarity | Value |\n|---|---|---|---|\n")
        for it, ic in lst:
            L.append(f"| {img(ic)} | [{md_esc(it.get('name', it['id']))}]({it['id']}.md) | {it.get('displaytype', 'ordinary')} | {it.get('baseMarketCost', 0)} |\n")
write('items/index.md', ''.join(L))

# monsters
L = [f"# Monsters\n\nAll {len(monsters)} monsters and NPCs, sorted by HP.\n\n| | Name | Class | HP | Attack | AC | BC | DR | Crit |\n|---|---|---|---|---|---|---|---|---|\n"]
for mid, m in sorted(monsters.items(), key=lambda kv: (kv[1].get('maxHP', 0), kv[1].get('name', ''))):
    ic = icon(m.get('iconID'), 'monsters')
    dmg = rng(m.get('attackDamage', {'min': 0, 'max': 0}))
    crit = f"{m.get('criticalSkill', 0)} / x{m.get('criticalMultiplier', 1)}" if m.get('criticalSkill') else '–'
    stats = [('Class', m.get('monsterClass', '?')), ('HP', m.get('maxHP', 0)), ('Max AP', m.get('maxAP', 10)),
             ('Attack cost', m.get('attackCost', 10)), ('Move cost', m.get('moveCost', 10)), ('Damage', dmg),
             ('Attack chance', m.get('attackChance', 0)), ('Block chance', m.get('blockChance', 0)),
             ('Damage resistance', m.get('damageResistance', 0)), ('Critical skill', m.get('criticalSkill', 0)),
             ('Critical multiplier', m.get('criticalMultiplier', 0))]
    P = [f"# {img(ic)} {m.get('name', mid)}\n\n", "| Stat | Value |\n|---|---|\n", ''.join(f"| {a} | {b} |\n" for a, b in stats)]
    if m.get('monsterClass') in ('ghost', 'construct', 'demon'):
        P.append("\n!!! note \"Immune to critical hits\"\n    Monsters of this class cannot be critically hit.\n")
    if m.get('hitEffect'):
        P.append("\n## On hit\n\n" + ''.join(f"- **{a}:** {md_esc(b)}\n" for a, b in effect_rows(m['hitEffect'])))
    dl = droplists.get(m.get('droplistID'))
    if dl:
        P.append("\n## " + ("Shop stock" if mid in shopkeepers else "Drops") + "\n\n| Item | Chance | Qty |\n|---|---|---|\n")
        for e in dl.get('items', []):
            q = e.get('quantity', {})
            P.append(f"| {link('items', e['itemID'], items.get(e['itemID'], {}).get('name', e['itemID']))} | {chance_txt(e.get('chance'))} | {rng(q)} |\n")
    if spawn_maps.get(mid):
        P.append("\n## Found on\n\n" + ''.join(f"- {link('maps', mp, mp)}\n" for mp in sorted(spawn_maps[mid])))
    P.append(f"\n<small>Monster ID: `{mid}` · Data from v{VERSION}</small>\n")
    write(f'monsters/{mid}.md', ''.join(P))
    L.append(f"| {img(ic)} | [{md_esc(m.get('name', mid))}]({mid}.md) | {m.get('monsterClass', '?')} | {m.get('maxHP', 0)} | {dmg} | {m.get('attackChance', 0)} | {m.get('blockChance', 0)} | {m.get('damageResistance', 0)} | {crit} |\n")
write('monsters/index.md', ''.join(L))

# quests
L = ["# Quests\n\n| Quest | Stages |\n|---|---|\n"]
for qid, q in sorted(quests.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
    if not q.get('showInLog', 1): continue
    P = [f"# {q.get('name', qid)}\n\n| Progress | Journal entry |\n|---|---|\n"]
    for s in q.get('stages', []):
        P.append(f"| {s.get('progress')} | {md_esc(s.get('logText', ''))}{' **(completes quest)**' if s.get('finishesQuest') else ''} |\n")
    P.append(f"\n<small>Quest ID: `{qid}` · Data from v{VERSION}</small>\n")
    write(f'quests/{qid}.md', ''.join(P))
    L.append(f"| [{md_esc(q.get('name', qid))}]({qid}.md) | {len(q.get('stages', []))} |\n")
write('quests/index.md', ''.join(L))

# skills
def req_text(r):
    if r[0] == 'skill': return f"{link('skills', r[1], skills.get(r[1], {}).get('name', r[1]))} level {r[2]}"
    if r[0] == 'level': return f"character level {r[1]}" + (f" (+{r[2]} per skill level)" if r[2] else '')
    return f"{r[1]} ≥ {r[2]}" + (f" (+{r[3]} per skill level)" if r[3] else '')
LUT = {'alwaysShown': 'Skill points', 'firstLevelRequiresQuest': 'First level from a quest, then skill points', 'onlyByQuests': 'Quest reward only'}
L = ["# Skills\n\n| Skill | Category | Max level | How obtained |\n|---|---|---|---|\n"]
for sid, s in skills.items():
    P = [f"# {s['name']}\n\n*{s['short']}*\n\n", f"**Category:** {s['category']} · **Max level:** {s['maxLevel']} · **Obtained via:** {LUT.get(s['levelUpType'], s['levelUpType'])}\n\n"]
    if s['requirements']:
        P.append("## Requirements\n\n" + ''.join(f"- {req_text(r)}\n" for r in s['requirements']) + '\n')
    if s['long']: P.append("## Description\n\n" + html.unescape(s['long']).replace('\n', '\n\n') + '\n')
    if skill_sources.get(sid):
        P.append(f"\n## Granted in conversations\n\nGranted by {len(skill_sources[sid])} dialogue node(s): " + ', '.join(f'`{c}`' for c in sorted(skill_sources[sid])) + '\n')
    write(f'skills/{sid}.md', ''.join(P))
    L.append(f"| [{md_esc(s['name'])}]({sid}.md) | {s['category']} | {s['maxLevel']} | {LUT.get(s['levelUpType'], s['levelUpType'])} |\n")
write('skills/index.md', ''.join(L))

# ---------------------------------------------------------------- snapshot + changelog
snap = {'version': VERSION,
        'items': {k: {x: v[x] for x in v if x not in ('iconID',)} for k, v in items.items()},
        'monsters': {k: {x: v[x] for x in v if x not in ('iconID',)} for k, v in monsters.items()},
        'quests': {k: v.get('name') for k, v in quests.items()},
        'skills': {k: {'maxLevel': v['maxLevel'], 'requirements': v['requirements']} for k, v in skills.items()}}
os.makedirs(DATA, exist_ok=True)
snap_path = os.path.join(DATA, 'snapshot.json')
old = json.load(open(snap_path)) if os.path.exists(snap_path) else None
clog_path = os.path.join(DOCS, 'changelog.md')
header = "# Changelog\n\nAutomatically generated whenever a new release is published.\n"
body = open(clog_path, encoding='utf-8').read().replace(header, '') if os.path.exists(clog_path) else ''
if old and old.get('version') != VERSION:
    E = [f"\n## v{VERSION} (from v{old['version']})\n"]
    for sec, namekey in (('items', 'name'), ('monsters', 'name')):
        o, n = old.get(sec, {}), snap[sec]
        added = [k for k in n if k not in o]; removed = [k for k in o if k not in n]
        changed = [k for k in n if k in o and n[k] != o[k]]
        if added: E.append(f"\n**New {sec} ({len(added)}):** " + ', '.join(link(sec, k, n[k].get(namekey, k)).replace('../', '') for k in added) + '\n')
        if removed: E.append(f"\n**Removed {sec} ({len(removed)}):** " + ', '.join(o[k].get(namekey, k) for k in removed) + '\n')
        for k in changed:
            diffs = [f"{f}: `{json.dumps(o[k].get(f))}` → `{json.dumps(n[k].get(f))}`" for f in sorted(set(o[k]) | set(n[k])) if o[k].get(f) != n[k].get(f)]
            E.append(f"- {link(sec, k, n[k].get(namekey, k)).replace('../', '')}: " + '; '.join(diffs) + '\n')
    newq = [k for k in snap['quests'] if k not in old.get('quests', {})]
    if newq: E.append(f"\n**New quests ({len(newq)}):** " + ', '.join(snap['quests'][k] or k for k in newq) + '\n')
    body = ''.join(E) + body
elif not old:
    body = f"\n## v{VERSION}\n\nFirst version tracked by this wiki.\n" + body
write('changelog.md', header + body)
json.dump(snap, open(snap_path, 'w'), indent=0, sort_keys=True)
open(os.path.join(DATA, 'VERSION'), 'w').write(VERSION + '\n')

# home page stats
write('index.md', f"""# Andor's Trail Wiki

An always-current reference for **Andor's Trail**, generated straight from the game's own open-source data.
This wiki currently describes **v{VERSION}**, the latest release, and rebuilds itself automatically when a new version is tagged.

<div class="grid cards" markdown>

- **[Items](items/index.md)**<br>{len(items)} items, with stats and drop sources
- **[Monsters](monsters/index.md)**<br>{len(monsters)} monsters and NPCs, with drops and locations
- **[Skills](skills/index.md)**<br>{len(skills)} skills, with requirements
- **[Quests](quests/index.md)**<br>{sum(1 for q in quests.values() if q.get('showInLog', 1))} quests and their journal stages
- **[World map](maps/index.md)**<br>{n_maps} maps, plus a clickable world map
- **[Changelog](changelog.md)**<br>What changed in each release

</div>

<small>Game data © the Andor's Trail contributors, used under the project's open-source licenses. This is an unofficial fan wiki.</small>
""")
print(f"Built v{VERSION}: {len(items)} items, {len(monsters)} monsters, {len(skills)} skills, {len(quests)} quests, {n_maps} maps")
