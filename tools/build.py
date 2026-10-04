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
    _v = ''.join(s.itertext()).replace("\\'", "'").replace('\\n', '\n').replace('\\"', '"').strip()
    strings[s.get('name')] = _v[1:-1] if len(_v) > 1 and _v[0] == '"' and _v[-1] == '"' else _v

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
for name, expr in re.findall(r'(?:public|private) static final (?:int|float) (\w+) = ([^;]+);', sc, re.S):
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

# Fill the "%1$,d"-style blanks in skill descriptions with the constants the app passes in
def java_format(fmt, args):
    def sub(m):
        i = int(m.group(1)) - 1
        if i >= len(args) or args[i] is None: return m.group(0)
        v = args[i]
        if m.group(3) == 'd': return f"{int(v):,}" if m.group(2) == ',' else str(int(v))
        return f"{v:g}" if isinstance(v, float) else str(v)
    return re.sub(r'%(\d+)\$(,?)[.\d]*([dsf])', sub, fmt).replace('%%', '%')
sia = open(os.path.join(JAVA, 'activity', 'SkillInfoActivity.java'), encoding='utf-8').read()
unfilled = []
for m in re.finditer(r'case (\w+):\s*return res\.getString\(R\.string\.(skill_longdescription_\w+)(.*?)\);', sia, re.S):
    sid, key, argsrc = m.groups()
    args = []
    for a in [x.strip() for x in argsrc.split(',') if x.strip()]:
        try: args.append(_java_eval(a.replace('SkillCollection.', ''), consts))
        except Exception: args.append(None); unfilled.append(f'{sid}: {a}')
    if sid in skills and key in strings:
        skills[sid]['long'] = java_format(strings[key], args)
for sid, sk in skills.items():
    first = re.split(r'(?<=\.)\s', html.unescape(sk['long']).strip(), maxsplit=1)[0] if sk['long'] else ''
    sk['summary'] = (first if len(first) <= 170 else first[:167].rsplit(' ', 1)[0] + '…') or sk['short']
if unfilled: print('WARNING: could not evaluate skill description values:', unfilled)

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
def _monster_icon(mid): return icon(monsters.get(mid, {}).get('iconID'), 'monsters')
def _monster_size(mid):
    rel = _monster_icon(mid)
    if not rel: return (1, 1)
    from PIL import Image
    w, h = Image.open(os.path.join(DOCS, rel)).size
    return (max(1, round(w / 32)), max(1, round(h / 32)))
spawn_maps, n_maps, quest_notes = build_maps(dict(GAME=GAME, DOCS=DOCS, VERSION=VERSION, monsters=monsters, droplists=droplists,
    items=items, conversations=conversations, quests=quests, skills=skills, conditions=conditions,
    group_to_monsters=group_to_monsters, write=write, md_esc=md_esc, chance_txt=chance_txt, rng=rng,
    monster_icon=_monster_icon, monster_size=_monster_size,
    item_icon=lambda iid: icon(items.get(iid, {}).get('iconID'), 'items')))

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
L = [f"# Items\n\nEvery item in Andor's Trail v{VERSION}, all {len(items)} of them. The search box is your friend; scrolling through this whole list is not.\n"]
for kind in ('Equipment', 'Consumable', 'Other'):
    L.append(f"\n## {kind}\n")
    for (k, cname), lst in sorted(groups.items()):
        if k != kind: continue
        L.append(f"\n### {cname}\n\n| | Item | Rarity | Value |\n|---|---|---|---|\n")
        for it, ic in lst:
            L.append(f"| {img(ic)} | [{md_esc(it.get('name', it['id']))}]({it['id']}.md) | {it.get('displaytype', 'ordinary')} | {it.get('baseMarketCost', 0)} |\n")
write('items/index.md', ''.join(L))

# monsters
L = [f"# Monsters\n\nAll {len(monsters)} monsters and NPCs, sorted by HP, weakest first. The ones at the bottom of the list are there for a reason.\n\n| | Name | Class | HP | Attack | AC | BC | DR | Crit |\n|---|---|---|---|---|---|---|---|---|\n"]
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
        P.append("\n!!! note \"Immune to critical hits\"\n    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.\n")
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

# quests (every quest gets a page, including hidden story flags, so map links always resolve)
L = ["# Quests\n\nEvery quest that shows up in your journal, plus, at the bottom, the hidden story flags the game uses to keep track of you without telling you.\n\n| Quest | Stages |\n|---|---|\n"]
hidden_rows = []
for qid, q in sorted(quests.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
    visible = bool(q.get('showInLog', 0))
    notes = quest_notes.get(qid, {})
    P = [f"# {q.get('name', qid)}\n\n"]
    if not visible:
        P.append("!!! info \"Hidden story flag\"\n    An internal quest the game uses to track your progress behind the scenes. "
                 "It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.\n\n")
    P.append("| Progress | Journal entry |\n|---|---|\n")
    stages = {st.get('progress') for st in q.get('stages', [])}
    for st in q.get('stages', []):
        pr = st.get('progress')
        extra = ''.join(f"<br><span class=\"qnote\">{n}</span>" for n in sorted(notes.get(pr, ())))
        P.append(f"| <span id=\"stage-{pr}\"></span>{pr} | {md_esc(st.get('logText', ''))}"
                 f"{' **(completes quest)**' if st.get('finishesQuest') else ''}{extra} |\n")
    orphan = {v: n for v, n in notes.items() if v not in stages}
    if orphan:
        P.append("\n## Other map events\n\n| Progress | Event |\n|---|---|\n")
        for v in sorted(orphan):
            P.append(f"| <span id=\"stage-{v}\"></span>{v} | " + '<br>'.join(sorted(orphan[v])) + " |\n")
    P.append(f"\n<small>Quest ID: `{qid}` · Data from v{VERSION}</small>\n")
    write(f'quests/{qid}.md', ''.join(P))
    row = f"| [{md_esc(q.get('name', qid))}]({qid}.md) | {len(q.get('stages', []))} |\n"
    (L if visible else hidden_rows).append(row)
if hidden_rows:
    L.append("\n## Hidden story flags\n\nInternal progress trackers that never appear in your journal, but quietly decide which doors open "
             "and which events fire. The names were not written with human readers in mind.\n\n| Flag | Stages |\n|---|---|\n" + ''.join(hidden_rows))
write('quests/index.md', ''.join(L))

# ---------------------------------------------------------------- stats & skills
import math
pj = open(os.path.join(JAVA, 'model', 'actor', 'Player.java'), encoding='utf-8').read()
cj = open(os.path.join(JAVA, 'controller', 'Constants.java'), encoding='utf-8').read()
def jint(src, name, default=0):
    m = re.search(rf'\b{name}\s*=\s*(-?\d+)', src); return int(m.group(1)) if m else default
base = {k: int(v) for k, v in re.findall(r'baseTraits\.(\w+)\s*=\s*(-?\d+);', pj)}
dmg = re.search(r'baseTraits\.damagePotential\.set\((\d+),\s*(\d+)\)', pj)
base_dmg_max, base_dmg_min = (int(dmg.group(1)), int(dmg.group(2))) if dmg else (1, 1)
LV = dict(hp=jint(cj, 'LEVELUP_EFFECT_HEALTH', 5), ac=jint(cj, 'LEVELUP_EFFECT_ATK_CH', 5),
          dmg=jint(cj, 'LEVELUP_EFFECT_ATK_DMG', 1), bc=jint(cj, 'LEVELUP_EFFECT_DEF_CH', 3),
          first_sp=jint(cj, 'FIRST_SKILL_POINT_IS_GIVEN_AT_LEVEL', 4), every_sp=jint(cj, 'NEW_SKILL_POINT_EVERY_N_LEVELS', 4),
          exp_base=jint(pj, 'EXP_base', 55), atk_cost=jint(pj, 'DEFAULT_PLAYER_ATTACKCOST', 4),
          fort=consts.get('PER_SKILLPOINT_INCREASE_FORTITUDE_HEALTH', 1))
def exp_to_reach(level): return sum(LV['exp_base'] * i * i for i in range(1, level))
def hit_pct(gap): return int(50 * (1 + 2 / math.pi * math.atan((gap - 50) / 40)))
def crit_pct(cs): return max(0, int(-5 + 2 * math.sqrt(5 * cs))) if cs > 0 else 0
STAT_NAMES = {'blockChance': 'Block chance', 'attackChance': 'Attack chance', 'maxHP': 'Max HP', 'maxAP': 'Max AP',
              'damageResistance': 'Damage resistance', 'criticalSkill': 'Critical skill', 'damagePotentialMax': 'Max damage',
              'damagePotentialMin': 'Min damage', 'criticalMultiplier': 'Critical multiplier'}

def req_text(r, max_level):
    """Requirement for skill level N is (N x per_level) + starting amount, per SkillInfo.SkillLevelRequirement."""
    more = max_level == 'unlimited' or (isinstance(max_level, int) and max_level > 1)
    if r[0] == 'skill':
        nm = link('skills', r[1], skills.get(r[1], {}).get('name', r[1]))
        return f"{nm} level {r[2]}" + (f" (each further level needs {r[2]} more)" if more else '')
    if r[0] == 'level':
        first = r[1] + r[2]
        return f"Character level {first}" + (f"; level 2 needs {2 * r[1] + r[2]}, level 3 needs {3 * r[1] + r[2]}, and so on" if more and r[1] else '')
    nm = STAT_NAMES.get(r[1], r[1]); first = r[2] + r[3]
    return (f"{nm} of at least {first} from level-ups (gear and skills don't count)" +
            (f"; each further level needs {r[2]} more" if more and r[2] else ''))

unlocks = defaultdict(list)  # skill -> skills that require it
for sid, sk in skills.items():
    for r in sk['requirements']:
        if r[0] == 'skill': unlocks[r[1]].append((sid, r[2]))
skill_quests = defaultdict(set)  # skill -> quests advanced in the same dialogue node that grants it
for sid, cids in skill_sources.items():
    for cid in cids:
        for r in conversations[cid].get('rewards', []) or []:
            if r.get('rewardType') == 'questProgress' and r.get('rewardID') in quests:
                skill_quests[sid].add(r['rewardID'])

LUT = {'alwaysShown': 'Skill points', 'firstLevelRequiresQuest': 'First level from a quest, then skill points', 'onlyByQuests': 'Quest reward only'}
for sid, sk in skills.items():
    P = [f"# {sk['name']}\n\n*{sk['summary']}*\n\n",
         f"**Category:** {sk['category']} · **Max level:** {sk['maxLevel']} · **Obtained via:** {LUT.get(sk['levelUpType'], sk['levelUpType'])}\n\n"]
    if sk['requirements']:
        P.append("## Requirements\n\n" + ''.join(f"- {req_text(r, sk['maxLevel'])}\n" for r in sk['requirements']) + '\n')
    if unlocks.get(sid):
        P.append("## Unlocks\n\nPoints spent here also count toward:\n\n" + ''.join(
            f"- {link('skills', u, skills[u]['name'])} (needs this skill at level {n})\n" for u, n in unlocks[sid]) + '\n')
    if sk['long']: P.append("## Description\n\n" + html.unescape(sk['long']).replace('\n', '\n\n') + '\n')
    if skill_sources.get(sid):
        qs = sorted(skill_quests.get(sid, ()), key=lambda q: quests[q].get('name', q))
        P.append("\n## Where to learn it\n\n" + (
            "Granted by an NPC as part of: " + ', '.join(link('quests', q, quests[q].get('name', q)) for q in qs) if qs
            else f"Granted by an NPC during a conversation ({len(skill_sources[sid])} place(s) in the game).") + '\n')
    write(f'skills/{sid}.md', ''.join(P))

sp_levels = [l for l in range(LV['first_sp'], 61, LV['every_sp'])]
exp_rows = ''.join(f"| {l} | {exp_to_reach(l):,} | {LV['exp_base'] * l * l:,} |\n" for l in (2, 5, 10, 15, 20, 25, 30, 40, 50, 60))
def hit_f(gap): return 50 * (1 + 2 / math.pi * math.atan((gap - 50) / 40))
hit_rows = ''.join(f"| {g:+d} | {hit_pct(g)}% | +{hit_f(g + 5) - hit_f(g):.1f}% |\n" for g in (-50, 0, 25, 50, 75, 100, 150, 200, 300))
crit_rows = ''.join(f"| {c} | {crit_pct(c)}% |\n" for c in (5, 10, 20, 30, 45, 60, 80, 100, 150))
by_cat = defaultdict(list)
for sid, sk in skills.items(): by_cat[sk['category']].append(sid)

# --- Cobalt UI frames, taken straight from the game (9-patch guide pixels stripped)
from PIL import Image as _Img
os.makedirs(os.path.join(DOCS, 'assets', 'ui'), exist_ok=True)
for nm in ('stdframe', 'richframe', 'lightframe', 'tabframe', 'textbutton_enabled_unpressed', 'textbutton_enabled_pressed'):
    src = os.path.join(GAME, 'res', 'drawable', f'ui_blue_{nm}.9.png')
    if os.path.exists(src):
        im = _Img.open(src).convert('RGBA'); im.crop((1, 1, im.width - 1, im.height - 1)).save(os.path.join(DOCS, 'assets', 'ui', f'{nm}.png'))

def section(title, body, open_=True):
    """A collapsible block (pymdownx.details); body is indented so it renders inside the block."""
    ind = '\n'.join(('    ' + ln) if ln.strip() else '' for ln in body.strip('\n').split('\n'))
    return f'\n{"???+" if open_ else "???"} section "{title}"\n\n{ind}\n'

G = 'stats.md'  # glossary page, linked from stat names
start_pairs = [('Max HP', base.get('maxHP', 25), 'max-hp'), ('Max AP', base.get('maxAP', 10), 'max-ap'),
               ('Attack chance', base.get('attackChance', 60), 'attack-chance'), ('Attack damage', f'{base_dmg_min}–{base_dmg_max}', 'attack-damage'),
               ('Block chance', base.get('blockChance', 9), 'block-chance'), ('Damage resistance', base.get('damageResistance', 0), 'damage-resistance'),
               ('Critical skill', base.get('criticalSkill', 0), 'critical-skill'), ('Critical multiplier', '–', 'critical-multiplier'),
               ('Attack cost', f"{LV['atk_cost']} AP", 'attack-cost'), ('Move cost', f"{base.get('moveCost', 6)} AP", 'move-cost'),
               ('Use item cost', f"{base.get('useItemCost', 5)} AP", 'use-item-cost'), ('Re-equip cost', f"{base.get('reequipCost', 5)} AP", 're-equip-cost')]
half = (len(start_pairs) + 1) // 2
start_tbl = "| Stat | Lv 1 | Stat | Lv 1 |\n|---|---|---|---|\n" + ''.join(
    f"| [{a[0]}]({G}#{a[2]}) | {a[1]} | " + (f"[{b[0]}]({G}#{b[2]}) | {b[1]} |" if b else " | |") + "\n"
    for a, b in zip(start_pairs[:half], start_pairs[half:] + [None]))
sp_list = [l for l in sp_levels if l <= 60]
level_body = f"""| Choice each level-up | Bonus |
|---|---|
| Max health | +{LV['hp']} HP |
| Attack chance | +{LV['ac']} |
| Attack damage | +{LV['dmg']} min & max |
| Block chance | +{LV['bc']} |

Pick **one** per level-up. There's no respec, so choose like you mean it. These picks form your **base stats**, which are the only values skill requirements look at. Gear and skills don't count, however shiny.

**Skill points:** levels {', '.join(map(str, sp_list))}. That's {len([l for l in sp_levels if l <= 50])} by level 50, and every one of them will feel like a hard decision.
**Experience:** level L → L+1 costs {LV['exp_base']} × L². Quadratic growth, so the grind gets real.

| Level | Total XP | XP to next |
|---|---|---|
{exp_rows}"""
combat_body = f"""Every attack goes through the same four steps. No hidden dice, no secret modifiers; this is the whole thing. The [stat glossary]({G}) explains each stat.

**1 · Hit?** `hit % = 50 × (1 + (2/π) × arctan((AC − BC − 50) / 40))`

| AC − BC | Hit | +5 AC adds |
|---|---|---|
{hit_rows}
**2 · Damage:** random between min and max attack damage.

**3 · Critical?** Only if you have critical skill above 0 **and** a critical multiplier, which comes from your weapon (or from [Way of the Monk](fightstyleUnarmedUnarmored.md) when fighting unarmed). No multiplier, no crits, no matter how much critical skill you pile up. Ghosts, constructs and demons are immune either way. `crit % = −5 + 2 × √(5 × critical skill)`, then damage × multiplier.

| Crit skill | Crit % |
|---|---|
{crit_rows}
**4 · Armor:** the target's damage resistance is subtracted from the result, with a floor of 0. Yes, a hit can do zero damage, and yes, it's as annoying as it sounds.

**Attacks per turn** = max AP ÷ attack cost, rounded down."""
STAT_SHORT = {'blockChance': 'block chance', 'attackChance': 'attack chance', 'maxHP': 'max HP', 'maxAP': 'max AP',
              'damageResistance': 'damage resistance', 'criticalSkill': 'critical skill'}
def prereq_short(sk):
    if sk['levelUpType'] in ('onlyByQuests', 'firstLevelRequiresQuest'):
        parts = ['Quest']
    else:
        parts = []
    for r in sk['requirements']:
        if r[0] == 'level' and r[1] + r[2] > 1: parts.append(f"Lv {r[1] + r[2]}+")
        elif r[0] == 'stat': parts.append(f"Base {STAT_SHORT.get(r[1], r[1])} {r[2] + r[3]}+")
        elif r[0] == 'skill': parts.append(f"[{skills.get(r[1], {}).get('name', r[1])}]({r[1]}.md) {r[2]}")
    return ' · '.join(parts) if parts else '–'
def skill_row(sid, star=False):
    sk = skills[sid]
    mx = sk['maxLevel'] if sk['maxLevel'] != 'unlimited' else '∞'
    return f"| [{md_esc(sk['name'])}]({sid}.md){'\\*' if star else ''} | {mx} | {prereq_short(sk)} | {md_esc(sk['summary'])} |\n"
points_skills = [sid for sid, sk in skills.items() if sk['levelUpType'] == 'alwaysShown']
quest_skills = [sid for sid, sk in skills.items() if sk['levelUpType'] != 'alwaysShown']
hdr = "| Skill | Max | Prerequisite | What it does |\n|---|---|---|---|\n"
skill_body = ("**Learned with skill points** (in the order the game lists them)\n\n" + hdr +
              ''.join(skill_row(x, x in skill_sources) for x in points_skills) +
              "\n\\* Extra levels can also be earned from quests.\n\n**Unlocked through quests**\n\n" + hdr +
              ''.join(skill_row(x) for x in quest_skills) +
              "\n*Quest* = the first level comes from a quest; for proficiencies, later levels cost skill points as usual.\n")
write('skills/index.md', f"""# Stats & Skills

How your hero's numbers actually work in v{VERSION}, pulled straight from the game's source code rather than from forum folklore. Click a heading to fold it away. Wondering what to *do* with all this? That's what [Strategy](../strategy/index.md) is for.
""" + section('Starting stats (level 1)', start_tbl) + section('Levelling up', level_body)
  + section('How combat works', combat_body) + section(f'All skills ({len(skills)})', skill_body))

# --- stat glossary (what each stat does)
write('skills/stats.md', f"""# Stat glossary

What each stat actually does in v{VERSION}. Starting values live on [Stats & Skills](index.md).

## Max HP
Your health. Hit 0 and you're done. Raised by the **max health** level-up (+{LV['hp']}), by [Fortitude](fortitude.md) (+{LV['fort']} per skill level on every later level-up), and by some gear. Most experienced players get theirs almost entirely from Fortitude; see [Strategy](../strategy/levelling.md) for why.

## Max AP
Action points per combat turn. Attacking, moving and drinking potions all cost AP, and running out mid-fight is a classic way to die. [Combat Speed](speed.md) adds +1 per level, up to 2.

## Attack chance
Your accuracy. It's compared with the target's block chance to decide whether you hit, through a curve with heavy diminishing returns at both ends ([details](index.md)). Raised by the **attack chance** level-up (+{LV['ac']}), [Weapon Accuracy](weaponChance.md) (+12 per level), weapons and proficiencies.

## Attack damage
Each hit rolls a random number between your minimum and maximum damage. The **attack damage** level-up adds +{LV['dmg']} to both. [Hard Hit](weaponDmg.md) adds +2 to the maximum only, which sounds better than it is: your average goes up by just 1.

## Block chance
Your evasion: the same curve as attack chance, pointed the other way. Raised by the **block chance** level-up (+{LV['bc']}), [Dodge](dodge.md) (+9 per level), shields and armor. Only level-up block chance counts toward skill requirements like [Bark Skin](barkSkin.md), so your fancy shield doesn't help there.

## Damage resistance
Subtracted from every hit you take, after critical multipliers. Damage can't go below 0, so it shines against monsters that nibble at you with lots of small hits and does much less against ones that hit like a truck. Raised by [Bark Skin](barkSkin.md) (+1 per level), shields and armor.

## Critical skill
Sets your critical hit chance: `−5 + 2 × √(5 × critical skill)`. The square root means each extra point helps less than the one before. It does **nothing** unless you also have a critical multiplier (from your weapon, or [Way of the Monk](fightstyleUnarmedUnarmored.md)). [More Criticals](moreCriticals.md) raises it by 20% per level.

## Critical multiplier
How hard a critical hit lands (e.g. ×2). Weapons provide it. Bare fists have none, so unarmed heroes can't crit at all, unless they learn [Way of the Monk](fightstyleUnarmedUnarmored.md), which grants ×1.25 per level. [Better Criticals](betterCriticals.md) raises it by 25% per level.

## Attack cost
AP spent per attack: {LV['atk_cost']} unarmed, or whatever your weapon says. Attacks per turn = max AP ÷ attack cost, rounded down, so a single point here can be worth an entire extra attack every turn, or absolutely nothing.

## Move cost
AP to move one tile during combat. Heavy armor raises it, which is the price of looking like a walking tank.

## Use item cost
AP to use an item, e.g. drinking a potion in the middle of a fight.

## Re-equip cost
AP to change equipment during combat. Possible, but rarely a good use of your turn.
""")
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
header = "# Changelog\n\nWhat changed in each release, worked out by comparing the game's data before and after. It's generated automatically, so it's thorough, if not exactly poetic.\n"
_old = open(clog_path, encoding='utf-8').read() if os.path.exists(clog_path) else ''
body = _old[_old.index('\n## v'):] if '\n## v' in _old else ''
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
    body = f"\n## v{VERSION}\n\nFirst version tracked by this wiki. Anything before this is lost to history.\n" + body
write('changelog.md', header + body)
json.dump(snap, open(snap_path, 'w'), indent=0, sort_keys=True)
open(os.path.join(DATA, 'VERSION'), 'w').write(VERSION + '\n')

# home page stats
n_rings = sum(1 for it in items.values() if it.get('category') == 'ring')
write('index.md', f"""# Andor's Trail Wiki

A wiki for **Andor's Trail**, the open-source pixel RPG where you set out to find your missing brother Andor and somehow end up running errands for half the continent.

Everything here is generated straight from the game's own data files, so the numbers are exactly what the game uses. No "I think it was around 30%?" guesswork. When the developers tag a new release, the wiki rebuilds itself within the hour. It currently describes **v{VERSION}**.

<div class="grid cards" markdown>

- **[Items](items/index.md)**<br>{len(items)} items, including {n_rings} different rings, which is apparently how many one hero needs
- **[Monsters](monsters/index.md)**<br>{len(monsters)} monsters and NPCs. Most want you dead; the rest want you to fetch something
- **[Stats & Skills](skills/index.md)**<br>How the numbers work, plus the {len(skills)} skills you'll agonize over
- **[Strategy](strategy/index.md)**<br>Hand-written advice. Opinionated, as advertised
- **[Quests](quests/index.md)**<br>{sum(1 for q in quests.values() if q.get('showInLog', 0))} quests and every journal entry, plus the hidden flags behind them
- **[World map](maps/index.md)**<br>{n_maps} maps, every monster, every chest
- **[Changelog](changelog.md)**<br>What each release changed, down to the last gold coin

</div>

<small>Game data © the Andor's Trail contributors, used under the project's open-source licenses. This is an unofficial fan wiki, not affiliated with the developers.</small>
""")
_left = [os.path.relpath(f, DOCS) for f in glob.glob(os.path.join(DOCS, '**', '*.md'), recursive=True)
         if re.search(r'%\d+\$[,.\d]*[dsf]', open(f, encoding='utf-8').read())]
for f in _left: print(f"::warning file=docs/{f}::Unfilled text placeholder (e.g. %1$d) left on this page")
print(f"Built v{VERSION}: {len(items)} items, {len(monsters)} monsters, {len(skills)} skills, {len(quests)} quests, {n_maps} maps")
