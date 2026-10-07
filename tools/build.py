#!/usr/bin/env python3
"""Andor's Trail wiki builder.

Usage: python tools/build.py <path-to-game-repo-checkout> <version-string>

Reads the game's own data (only the files the game itself loads, per
res/values/loadresources.xml), cross-references it, and writes:
  data/snapshot.json   - normalized data (used to diff the next release)
  docs/**              - MkDocs pages, including cropped item/monster icons
  docs/changelog.md    - prepended with a diff vs. the previous snapshot
"""
import json, os, re, sys, glob, shutil, html, math
from collections import defaultdict, Counter
import xml.etree.ElementTree as ET

REPO, VERSION = sys.argv[1], sys.argv[2]
GAME = os.path.join(REPO, 'AndorsTrail')
RAW = os.path.join(GAME, 'res', 'raw')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
DATA = os.path.join(ROOT, 'data')
JAVA = os.path.join(GAME, 'app', 'src', 'main', 'java', 'com', 'gpl', 'rpg', 'AndorsTrail')

# ---------------------------------------------------------------- loading
ARRAY_NAME = {'itemfilters': 'itemfilters', 'itemlist': 'items', 'monsterlist': 'monsters', 'questlist': 'quests', 'conversationlist': 'conversationlists',
              'droplists': 'droplists', 'itemcategories': 'itemcategories', 'actorconditions': 'actorconditions'}
def loaded_files(kind):
    """Files the game actually loads for a resource kind, per res/values/loadresources.xml (skips debug/test data)."""
    tree = ET.parse(os.path.join(GAME, 'res', 'values', 'loadresources.xml'))
    for arr in tree.getroot():
        if arr.get('name') in (f'loadresource_{kind}', f'loadresource_{ARRAY_NAME.get(kind, kind)}'):
            return [os.path.join(RAW, i.text.split('/')[-1] + '.json') for i in arr if i.text]
    return sorted(glob.glob(os.path.join(RAW, f'{kind}_*.json')))

FILE_OF = {}
def load_all(kind):
    out = {}
    for f in loaded_files(kind):
        if os.path.exists(f):
            for obj in json.load(open(f, encoding='utf-8')):
                out[obj['id']] = obj
                FILE_OF[(kind, obj['id'])] = os.path.basename(f)
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
skill_desc_consts = {}
for m in re.finditer(r'case (\w+):\s*return res\.getString\(R\.string\.(skill_longdescription_\w+)(.*?)\);', sia, re.S):
    sid, key, argsrc = m.groups()
    args = []
    for a in [x.strip() for x in argsrc.split(',') if x.strip()]:
        try: args.append(_java_eval(a.replace('SkillCollection.', ''), consts))
        except Exception: args.append(None); unfilled.append(f'{sid}: {a}')
    if sid in skills and key in strings:
        skills[sid]['long'] = java_format(strings[key], args)
        skill_desc_consts[sid] = [(a.strip().replace('SkillCollection.', ''), v) for a, v in zip([x for x in argsrc.split(',') if x.strip()], args)]
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
def reaches(start, target, limit=5000):
    seen, stack = set(), [start]
    while stack and len(seen) < limit:
        pid = stack.pop()
        if pid == target: return True
        if pid in seen or pid not in conversations: continue
        seen.add(pid)
        for r in conversations[pid].get('replies', []) or []:
            if r.get('nextPhraseID'): stack.append(r['nextPhraseID'])
    return False
def reaches_shop(start, limit=400): return reaches(start, 'S', limit)
shopkeepers = {mid for mid, m in monsters.items() if m.get('phraseID') and reaches_shop(m['phraseID'])}
# NPCs that can be fought (Monster.isAgressive): a conversation that reaches "F" starts combat (endConversationWithCombat),
# and an NPC whose faction the player's standing can drop below 0 becomes hostile (Player.getAlignment(faction) < 0).
_neg_factions = {r.get('rewardID') for c in conversations.values() for r in (c.get('rewards') or [])
                 if r.get('rewardType') in ('alignmentChange', 'alignmentSet') and (r.get('value') or 0) < 0}
fight_by_dialogue = {mid for mid, m in monsters.items() if m.get('phraseID') and reaches(m['phraseID'], 'F')}
fight_by_faction = {mid for mid, m in monsters.items() if m.get('phraseID') and m.get('faction') in _neg_factions}
def kind_of(mid):
    """Enemy: hostile on sight. NPC: has a conversation and can never be attacked. NPC/Enemy: has a conversation but can become hostile."""
    if not monsters[mid].get('phraseID'): return 'Enemy'
    return 'NPC/Enemy' if mid in fight_by_dialogue or mid in fight_by_faction else 'NPC'
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
def cond_text(clist, equip=False):
    """Condition effects as the parsers read them: equip effects default to magnitude 1 (while worn); other effects default to
    magnitude -99 (= remove the condition) and duration 0. Magnitude -99 with a duration is an immunity."""
    parts = []
    for c in clist:
        cid = c.get('condition')
        name = f"[{conditions.get(cid, {}).get('name', cid)}](../conditions/{cid}.md)" if cid in conditions else str(cid)
        mag = c.get('magnitude', 1 if equip else -99)
        dur = 999 if equip else c.get('duration', 0)
        ch = f"{chance_txt(c['chance'])} chance" if 'chance' in c and chance_pct(c['chance']) < 100 else ''
        if mag == -99:
            what = f"removes {name}" if dur == 0 else f"immunity to {name}" + ('' if equip else f" for {dur} rounds" if dur not in (998, 999) else '')
            parts.append(what + (f" ({ch})" if ch else ''))
            continue
        d = '' if equip else ('permanent' if dur == 999 else 'until rest' if dur == 998 else f"{dur} round{'s' if dur != 1 else ''}")
        bits = [f"magnitude {mag}", d, ch]
        parts.append(f"{name} ({', '.join(b for b in bits if b)})")
    return '; '.join(parts)
def effect_rows(eff):
    rows = []
    for k, v in (eff or {}).items():
        label = LABELS.get(k, k)
        val = cond_text(v, k == 'addedConditions') if isinstance(v, list) else rng(v)
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
import history as H
hist = H.update_history(DATA, os.path.join(GAME, 'res'), VERSION)
_names = {'items': {k: v.get('name', k) for k, v in items.items()}, 'monsters': {k: v.get('name', k) for k, v in monsters.items()},
          'quests': {k: v.get('name', k) for k, v in quests.items()}}
def page_exists(kind, oid):
    if kind == 'maps': return os.path.exists(os.path.join(GAME, 'res', 'xml', oid + '.tmx'))
    return oid in {'items': items, 'monsters': monsters, 'quests': quests}.get(kind, {})
def hist_md(kind, oid, dialogue_ids=(), lead=''):
    return H.history_section(hist, kind, oid, VERSION, dialogue_ids, lead)
def comp_md(qid): return H.completability_text(hist, qid, _names['items'], VERSION) if hist else ''
def _monster_icon(mid): return icon(monsters.get(mid, {}).get('iconID'), 'monsters')
def _monster_size(mid):
    rel = _monster_icon(mid)
    if not rel: return (1, 1)
    from PIL import Image
    w, h = Image.open(os.path.join(DOCS, rel)).size
    return (max(1, round(w / 32)), max(1, round(h / 32)))
_map_ctx = dict(GAME=GAME, DOCS=DOCS, VERSION=VERSION, monsters=monsters, droplists=droplists,
    items=items, conversations=conversations, quests=quests, skills=skills, conditions=conditions,
    group_to_monsters=group_to_monsters, write=write, md_esc=md_esc, chance_txt=chance_txt, rng=rng,
    monster_icon=_monster_icon, monster_size=_monster_size, history=lambda *a: hist_md(*a),
    item_icon=lambda iid: icon(items.get(iid, {}).get('iconID'), 'items'))
spawn_maps, n_maps, quest_notes, script_maps, _map_pages = build_maps(_map_ctx)
from notes import Notes
from quests import QuestGraph, write_quest_pages, npc_section
notes = Notes(os.path.join(ROOT, 'notes'))
QG = QuestGraph(dict(conversations=conversations, quests=quests, monsters=monsters, items=items, droplists=droplists,
                     skills=skills, spawn_maps=spawn_maps, script_maps=script_maps, map_notes=quest_notes, VERSION=VERSION))
# dialogue simulator data: one file per conversation starting point used by an NPC
from quests import export_dialogue
item_filters = {f['id']: f.get('include', []) for fn in loaded_files('itemfilters') if os.path.exists(fn)
                for f in json.load(open(fn, encoding='utf-8'))}
shutil.rmtree(os.path.join(DOCS, 'assets', 'dialogue'), ignore_errors=True)
_sk_names = {k: v['name'] for k, v in skills.items()}
_exported = {m['phraseID'] for m in monsters.values() if m.get('phraseID') in conversations}
for _rp in _exported: export_dialogue(QG, _rp, os.path.join(DOCS, 'assets', 'dialogue'), item_filters, _sk_names)
from maps import write_map_pages
def introduced(kind, oid):
    if not hist: return None
    evs = hist['entities'].get(kind, {}).get(oid, [])
    first_added = next((v for v, ev, _ in evs if ev == 'added'), None)
    return f"[v{first_added}](../versions/{first_added}.md)" if first_added else f"v{hist['first']} or earlier"
_map_ctx['verified'] = H.verified

def item_kind(it):
    c = cats.get(it.get('category'), {})
    if c.get('actionType') == 'equip': return 'Equipment'
    if c.get('actionType') == 'use': return 'Consumable'
    return 'Other'

# ---------------------------------------------------------------- indexes for item & monster pages
def crit_pct(cs): return max(0, int(-5 + 2 * math.sqrt(5 * cs))) if cs > 0 else 0
import numpy as _np
def monster_xp(m):
    """MonsterTypeParser.getExpectedMonsterExperience, in single precision like the game."""
    f = _np.float32
    ap, cost = int(m.get('maxAP', 10)), int(m.get('attackCost', 10))
    d = m.get('attackDamage') or {}
    avg = (f(d.get('min', 0)) + f(d.get('max', 0))) / f(2) if d else f(0)
    apt = f(ap // cost if cost else 0)
    att = apt * (f(m.get('attackChance', 0)) / f(100)) * avg * (f(1) + (f(m.get('criticalSkill', 0)) / f(100)) * f(m.get('criticalMultiplier', 0)))
    dfn = f(m.get('maxHP', 1)) * (f(1) + f(m.get('blockChance', 0)) / f(100)) + f(9) * f(m.get('damageResistance', 0))
    bonus = 50 if (m.get('hitEffect') or {}).get('conditionsTarget') else 0
    return int(math.ceil(float((att * f(3) + dfn) * f(0.7)))) + bonus
def region_of(mp):
    pg = _map_pages.get(mp)
    return pg['area'][0] if pg and pg.get('area') and pg['area'][0] else None
def where(mid, n=3):
    mps = sorted(spawn_maps.get(mid, ()))
    if not mps: return ''
    regs = list(dict.fromkeys(r for r in (region_of(x) for x in mps) if r))
    return ', '.join(regs[:n]) if regs else ', '.join(mps[:n])
in_containers = defaultdict(list)          # item -> [(map, container number, chance)]
for mp, pg in _map_pages.items():
    for k, (cid, dl) in enumerate(pg['containers']):
        for e in dl.get('items', []): in_containers[e['itemID']].append((mp, k, e.get('chance')))
dialogue_gives = defaultdict(list)         # item -> [(conversation node, how)]
item_uses = defaultdict(list)              # item -> [(parent node, reply text, requirement type, amount, next node)]
kill_reqs = defaultdict(list)              # monster -> [(parent node, amount, next node)]
for cid, c in conversations.items():
    for r in c.get('rewards') or []:
        if r.get('rewardType') == 'giveItem': dialogue_gives[r.get('rewardID')].append((cid, f"{r.get('value') or 1}×"))
        elif r.get('rewardType') == 'dropList':
            for e in droplists.get(r.get('rewardID'), {}).get('items', []): dialogue_gives[e['itemID']].append((cid, chance_txt(e.get('chance'))))
    for rep in c.get('replies') or []:
        for q in rep.get('requires') or []:
            t, rid = q.get('requireType'), q.get('requireID')
            if t in ('inventoryRemove', 'inventoryKeep', 'wear', 'wearRemove', 'usedItem') and not q.get('negate'):
                for x in (item_filters.get(rid) or [rid]): item_uses[x].append((cid, rep.get('text', ''), t, q.get('value', 1), rep.get('nextPhraseID'), rid if rid in item_filters else None))
            elif t == 'killedMonster' and not q.get('negate'):
                kill_reqs[rid].append((cid, q.get('value', 1), rep.get('nextPhraseID')))
def node_quests(*cids):
    out = []
    for c in cids:
        for r in (conversations.get(c, {}).get('rewards') or []):
            if r.get('rewardType') == 'questProgress' and r.get('rewardID') in quests: out.append((r['rewardID'], r.get('value')))
    return out
def speakers_md(cid):
    sp = [s for rt in QG.routes(cid) for s in rt['speakers']]
    return QG.who(list(dict.fromkeys(sp))[:2]) if sp else 'a scripted event'
def raw_json(o):
    return '    ```json\n' + '\n'.join('    ' + l for l in json.dumps(o, indent=1, ensure_ascii=False).split('\n')) + '\n    ```\n'
def infobox(rows, image=None):
    return ('<div class="infobox" markdown>\n\n' + (f'<p class="ib-img">![]({image}){{ .sprite }}</p>\n\n' if image else '') +
            '| | |\n|---|---|\n' + ''.join(f"| **{k}** | {v} |\n" for k, v in rows if v not in (None, '', 0)) + '\n</div>\n\n')
PROF_SKILL = {**{c: 'weaponProficiencyDagger' for c in ('dagger', 'ssword')}, **{c: 'weaponProficiency1hsword' for c in ('lsword', 'bsword', 'rapier')},
              '2hsword': 'weaponProficiency2hsword', **{c: 'weaponProficiencyAxe' for c in ('axe', 'axe2h')},
              **{c: 'weaponProficiencyBlunt' for c in ('club', 'staff', 'mace', 'scepter', 'hammer', 'hammer2h', 'whip')}, 'pole': 'weaponProficiencyPole'}
def prof_skill(cat_id):
    """SkillController.getProficiencySkillForItemCategory (note: the game maps no proficiency to some weapon categories, e.g. mace2h)."""
    c = cats.get(cat_id, {})
    if c.get('inventorySlot') == 'weapon': return PROF_SKILL.get(cat_id)
    if c.get('inventorySlot') == 'shield': return 'armorProficiencyShield'
    if c.get('inventorySlot') in ('head', 'body', 'hand', 'feet'):
        return {'light': 'armorProficiencyLight', 'std': 'armorProficiencyLight', 'large': 'armorProficiencyHeavy'}.get(c.get('size'))
    return None
WEAPON_PROF = None

# ---- NPC roles: shopkeeper, skill trainer, quest giver (who sets a journal quest's first stage)
trainer_of, giver_of = defaultdict(set), defaultdict(set)
for sid, cids in skill_sources.items():
    for cid in cids:
        for rt in QG.routes(cid):
            for k, x in rt['speakers']:
                if k == 'npc': trainer_of[x].add(sid)
for qid, q in quests.items():
    if not q.get('showInLog', 0): continue
    first = min((st for (qq, st) in QG.triggers if qq == qid), default=None)
    if first is None: continue
    for cid in QG.triggers[(qid, first)]:
        for rt in QG.routes(cid):
            for k, x in rt['speakers']:
                if k == 'npc': giver_of[x].add(qid)
npc_variants = defaultdict(list)
for _mid, _m in monsters.items():
    if _m.get('phraseID') and (_m.get('name') or '').strip(): npc_variants[_m['name'].strip()].append(_mid)
def front(desc):
    """YAML front matter: Material for MkDocs uses it as the page's <meta name="description"> (search-result snippet)."""
    d = ' '.join(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', str(desc)).split())
    if len(d) > 300: d = d[:297].rsplit(' ', 1)[0] + '…'
    return '---\ndescription: ' + json.dumps(d, ensure_ascii=False) + '\n---\n\n'
def place_links(mid, n=4, pin=True):
    """'Region: map' links for where a monster/NPC stands; NPC links jump to its pin on the labelled map."""
    mps = sorted(spawn_maps.get(mid, ()), key=lambda mp: (region_of(mp) is None, region_of(mp) or '', mp))
    out = [f"{region_of(mp) + ': ' if region_of(mp) else ''}[{mp}](../maps/{mp}.md{'#pin-npc-' + mid if pin else ''})" for mp in mps[:n]]
    return ', '.join(out) + (f" (+{len(mps) - n} more)" if len(mps) > n else '')
def role_text(mid, links=True):
    r = []
    if mid in shopkeepers: r.append('shopkeeper')
    if trainer_of.get(mid):
        r.append('teaches ' + ', '.join((f"[{skills[x]['name']}](../skills/{x}.md)" if links else skills[x]['name']) for x in sorted(trainer_of[mid]) if x in skills))
    if giver_of.get(mid):
        gq = sorted(giver_of[mid], key=lambda q: quests[q].get('name', q))
        r.append('starts ' + ', '.join((f"[{quests[q].get('name', q)}](../quests/{q}.md)" if links else quests[q].get('name', q)) for q in gq[:4]) + (f" +{len(gq) - 4}" if len(gq) > 4 else ''))
    return '; '.join(r)

# ---------------------------------------------------------------- item pages
item_rows = []
for iid, it in sorted(items.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
    c = cats.get(it.get('category'), {})
    ic = icon(it.get('iconID'), 'items')
    is_weapon = c.get('inventorySlot') == 'weapon'
    hands = ('Two-handed' if c.get('size') == 'large' else 'One-handed') if is_weapon else None
    info = [('Item ID', f"`{iid}`"), ('Category', c.get('name', it.get('category'))), ('Slot', c.get('inventorySlot')),
            ('Hands', hands), ('Proficiency', (f"[{skills[prof_skill(it.get('category'))]['name']}](../skills/{prof_skill(it.get('category'))}.md)"
                                              if prof_skill(it.get('category')) else ('none (the game assigns no proficiency to this weapon type)' if is_weapon else None))),
            ('Rarity', it.get('displaytype', 'ordinary').capitalize()), ('Base value', f"{it.get('baseMarketCost', 0):,} gold"),
            ('Quest item', 'Yes' if it.get('displaytype') == 'quest' else None), ('Introduced', introduced('items', iid))]
    _src = [w for w, ok in (('monster drops', dropped_by.get(iid)), ('shops', sold_by.get(iid)), ('containers', in_containers.get(iid)), ('quests and dialogue', dialogue_gives.get(iid))) if ok]
    _stats = ', '.join(f"{a} {b}" for a, b in effect_rows(it.get('equipEffect'))[:4])
    L = [front(f"{it.get('name', iid)} is a {it.get('displaytype', 'ordinary')} {(c.get('name') or 'item').lower()} in Andor's Trail" + (f" ({_stats})" if _stats else '') + ". "
               + (f"How to get it: {', '.join(_src)}. " if _src else '') + (it.get('description') or '')),
         f"# {img(ic)} {it.get('name', iid)}\n\n", f"*{it.get('displaytype', 'ordinary').capitalize()} {c.get('name', '').lower() or 'item'}.*\n\n",
         infobox(info, '../../' + ic if ic else None)]
    if it.get('description'): L.append(f"> {it['description']}\n\n")
    stat_md = ''
    for title, key in (('When equipped', 'equipEffect'), ('When used', 'useEffect'), ('On hit', 'hitEffect'),
                       ('On kill', 'killEffect'), ('When hit', 'hitReceivedEffect')):
        rows = effect_rows(it.get(key))
        if rows: stat_md += f"\n### {title}\n\n| Stat | Value |\n|---|---|\n" + ''.join(f"| {md_esc(a)} | {md_esc(b)} |\n" for a, b in rows)
    if stat_md: L.append("## Statistics\n" + stat_md + H.verified("item data", VERSION))
    # ---- acquisition
    acq = []
    srcs = dropped_by.get(iid, [])
    if srcs:
        acq.append("### Dropped by\n\n| Monster | Chance | Qty | Found in |\n|---|---|---|---|\n" + ''.join(
            f"| {link('monsters', mid, monsters[mid].get('name', mid))} | {chance_txt(ch)} | {q} | {where(mid) or '–'} |\n"
            for mid, ch, q in sorted(srcs, key=lambda s: -chance_pct(s[1]))[:40]) + (f"\n*…and {len(srcs) - 40} more.*\n" if len(srcs) > 40 else '') + "\n")
    if sold_by.get(iid):
        acq.append("### Sold by\n\n" + ''.join(f"- {link('monsters', mid, monsters[mid].get('name', mid))}" + (f" ({where(mid)})" if where(mid) else '') + "\n"
                                                for mid in dict.fromkeys(m for m, _, _ in sold_by[iid])) + "\n")
    if in_containers.get(iid):
        acq.append("### Found in containers\n\n" + ''.join(f"- [{mp}](../maps/{mp}.md#container-{k}) (container {k + 1}, {chance_txt(ch)})" + (f", {region_of(mp)}" if region_of(mp) else '') + "\n"
                                                         for mp, k, ch in sorted(in_containers[iid])[:30]) + "\n")
    if dialogue_gives.get(iid):
        rows = []
        for cid, how in dialogue_gives[iid][:20]:
            qs = node_quests(cid)
            rows.append(f"- From {speakers_md(cid)}" + (f" during {QG.qlink(qs[0][0], qs[0][1])}" if qs else '') + f" ({how})\n")
        acq.append("### Quest & dialogue rewards\n\n" + ''.join(dict.fromkeys(rows)) + "\n")
    L.append("## How to get it\n\n" + (''.join(acq) if acq else
             f"As of v{VERSION}, nothing in the game data gives this item: no monster drops it, no shop sells it, no container holds it and no dialogue hands it out."
             + (" It is only listed in an unused placeholder loot table." if any(iid in [e['itemID'] for e in dl.get('items', [])] for d, dl in droplists.items() if 'undropped' in d) else '') + "\n\n"))
    L.append(H.verified("item, loot, map and dialogue data", VERSION))
    # ---- uses
    uses = item_uses.get(iid, [])
    if uses:
        verb = {'inventoryRemove': 'handed over', 'inventoryKeep': 'must be carried', 'wear': 'must be worn', 'wearRemove': 'worn item is taken', 'usedItem': 'must have been used'}
        rows = []
        for par, text, t, val, nxt, filt in uses[:30]:
            qs = node_quests(nxt) or node_quests(par)
            rows.append(f"| {speakers_md(par)} | {QG.qlink(qs[0][0], qs[0][1]) if qs else '–'} | {verb.get(t, t)} ({val}×){' — any item from group `' + filt + '`' if filt else ''} | “{md_esc(re.sub(r'\\{(\\d+)\\}', r'\\1', text or '')[:80]) or '(automatic)'}” |\n")
        L.append("## Uses\n\nWhere the game checks for this item in dialogue:\n\n| With | Quest | What happens to it | Option |\n|---|---|---|---|\n" + ''.join(dict.fromkeys(rows)) +
                 (f"\n*…and {len(uses) - 30} more.*\n" if len(uses) > 30 else '') + H.verified("dialogue data", VERSION))
    L.append(hist_md('items', iid))
    L.append(notes('items', iid, it.get('name', iid)))
    tech = [('Item ID', f"`{iid}`"), ('Category ID', f"`{it.get('category', '–')}`"), ('Icon', f"`{it.get('iconID', '–')}`"),
            ('Defined in', f"`res/raw/{FILE_OF.get(('itemlist', iid), '?')}`"),
            ('Loot tables containing it', ', '.join(f"`{d}`" for d, dl in droplists.items() if any(e['itemID'] == iid for e in dl.get('items', []))) or '–')]
    L.append('\n??? info "Technical information"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {a} | {b} |\n" for a, b in tech) +
             "\n    Raw data:\n\n" + raw_json(it) + '\n')
    L.append(f"\n<small>Data from v{VERSION}</small>\n")
    write(f'items/{iid}.md', ''.join(L))
    item_rows.append((it, c, ic))

# items index, grouped by kind then category
groups = defaultdict(list)
for it, c, ic in item_rows:
    groups[(item_kind(it), c.get('name', it.get('category', 'Uncategorized')))].append((it, ic))
L = [f"# Items\n\nEvery item in Andor's Trail v{VERSION}, all {len(items)} of them. Items are grouped by type and category. Use the search box to find a specific item.\n"]
for kind in ('Equipment', 'Consumable', 'Other'):
    L.append(f"\n## {kind}\n")
    for (k, cname), lst in sorted(groups.items()):
        if k != kind: continue
        L.append(f"\n### {cname}\n\n| | Item | Rarity | Value |\n|---|---|---|---|\n")
        for it, ic in lst:
            L.append(f"| {img(ic)} | [{md_esc(it.get('name', it['id']))}]({it['id']}.md) | {it.get('displaytype', 'ordinary')} | {it.get('baseMarketCost', 0)} |\n")
write('items/index.md', ''.join(L))

# ---------------------------------------------------------------- monster & NPC pages
# One page per character name. The game data often defines several entries with the same name (one per location,
# story stage or behaviour); they are combined here, with a section per entry. Links to the other entry IDs are
# rewritten to point at the combined page (see the end of this script).
def _vsort(x):   # natural order of entry IDs (agent2 before agent10); entries not placed on a map go last
    return (not spawn_maps.get(x), [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', x)])
from maps import _pretty
name_groups = defaultdict(list)
for _mid, _m in monsters.items(): name_groups[(_m.get('name') or '').strip() or _mid].append(_mid)
canon_of, group_ids = {}, {}
for _nm, _ids in name_groups.items():
    _slug = re.sub(r'[^a-z0-9]', '', _nm.lower())
    _c = min(_ids, key=lambda x: (re.sub(r'[^a-z0-9]', '', x.lower()) != _slug, not spawn_maps.get(x), len(x), x))
    group_ids[_c] = [_c] + sorted((x for x in _ids if x != _c), key=_vsort)
    for x in _ids: canon_of[x] = _c
def group_kind(ids):
    ks = {kind_of(x) for x in ids}
    return ks.pop() if len(ks) == 1 else 'NPC/Enemy'
def fight_reason(mid):
    m = monsters[mid]
    if mid in fight_by_dialogue: return "a conversation with this character can end in combat (a dialogue branch leads to a fight)"
    if mid in fight_by_faction: return f"this character belongs to the faction `{m.get('faction')}`, and the game treats members of a faction as hostile once your standing with that faction drops below zero"
    return ''
def span(vals, fmt=str):
    vals = sorted(set(vals))
    return '–' if not vals else (fmt(vals[0]) if len(vals) == 1 else f"{fmt(vals[0])}–{fmt(vals[-1])}")
TYPE_HELP = {'Enemy': 'hostile on sight', 'NPC': 'can be spoken to; cannot be attacked', 'NPC/Enemy': 'can be spoken to, but can also be fought'}
_ENTRY_FIELDS = (('conversation', ('phraseID',)), ('location', None), ('combat statistics', ('maxHP', 'attackDamage', 'attackChance', 'blockChance', 'damageResistance', 'maxAP', 'attackCost', 'criticalSkill', 'criticalMultiplier')),
                 ('loot or shop stock', ('droplistID',)), ('faction', ('faction',)), ('appearance', ('iconID',)), ('movement', ('movementAggressionType',)))
def entry_differences(ids):
    out = []
    for label, keys in _ENTRY_FIELDS:
        vals = {tuple(sorted(spawn_maps.get(x, ()))) for x in ids} if keys is None else {json.dumps([monsters[x].get(k) for k in keys], sort_keys=True) for x in ids}
        if len(vals) > 1: out.append(label)
    return out
def var_label(x):
    mps = sorted(spawn_maps.get(x, ()), key=lambda mp: (region_of(mp) is None, region_of(mp) or '', mp))
    if not mps: return 'Not placed on a map'
    return (f"{region_of(mps[0])}, {_pretty(mps[0])}" if region_of(mps[0]) else _pretty(mps[0])) + (f" and {len(mps) - 1} more" if len(mps) > 1 else '')
def demote(md):
    return re.sub(r'(?m)^(#{2,5}) ', lambda mm: mm.group(1) + '# ', md)

XP_NOTE = ("??? info \"How the XP value is calculated\"\n\n"
           "    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):\n\n"
           "    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉\n\n"
           "    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.\n\n")

def variant_body(x, multi, shown_convs):
    m = monsters[x]; k = kind_of(x)
    P = []
    if multi:
        bits = [f"**Entry ID:** `{x}`", f"**Type:** {k}"] + ([f"**Role:** {role_text(x)[:1].upper() + role_text(x)[1:]}"] if role_text(x) else [])
        P.append(' · '.join(bits) + "\n\n")
        P.append((f"**Location:** {place_links(x, 6, pin=bool(m.get('phraseID')))}" if spawn_maps.get(x) else
                  "**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.") + "\n\n")
    if k == 'NPC/Enemy': P.append(f"!!! warning \"Can be fought\"\n    This entry can be talked to, but it can also become an opponent: {fight_reason(x)}.\n\n")
    if k == 'NPC/Enemy' and 'maxHP' not in m:
        P.append("No combat statistics are defined for this entry in the game data. Where the story leads to a fight, the game normally uses a separate hostile entry"
                 + (" (listed on this page)" if multi else '') + ".\n\n")
    elif k != 'NPC':
        d = m.get('attackDamage') or {}
        ap, cost = m.get('maxAP', 10), m.get('attackCost', 10)
        cs, cmul = m.get('criticalSkill', 0), m.get('criticalMultiplier', 0)
        stats = [('Class', (m.get('monsterClass') or 'humanoid').capitalize()), ('HP', m.get('maxHP', 1)), ('XP when defeated', f"{monster_xp(m):,}"),
                 ('Damage', rng(d) if d else '0'), ('Attack chance', m.get('attackChance', 0)), ('Block chance', m.get('blockChance', 0)),
                 ('Damage resistance', m.get('damageResistance', 0)), ('Max AP', ap), ('Attack cost', f"{cost} AP"),
                 ('Attacks per turn', ap // cost if cost else 0), ('Move cost', f"{m.get('moveCost', 10)} AP"), ('Critical skill', cs),
                 ('Critical multiplier', cmul or '–'),
                 ('Critical hit chance', f"{crit_pct(cs)}%" if cs > 0 and cmul not in (0, 1) else 'None (requires both critical skill and a critical multiplier)')]
        P.append("## Combat statistics\n\n| Statistic | Value |\n|---|---|\n" + ''.join(f"| {a} | {b} |\n" for a, b in stats) + "\n")
        if m.get('monsterClass') in ('ghost', 'construct', 'demon'):
            P.append("!!! note \"Immune to critical hits\"\n    Ghosts, constructs and demons cannot receive critical hits.\n\n")
        for title, key in (('On hit', 'hitEffect'), ('When hit', 'hitReceivedEffect'), ('On death', 'deathEffect')):
            if m.get(key): P.append(f"**{title}:** " + '; '.join(f"{a}: {md_esc(b)}" for a, b in effect_rows(m[key])) + "\n\n")
        P.append(H.verified("monster data and game code (`MonsterTypeParser.java`)", VERSION))
    dl = droplists.get(m.get('droplistID'))
    if dl and (x in shopkeepers or k != 'NPC'):
        P.append("## " + ("Shop stock" if x in shopkeepers else "Drops") + "\n\n| Item | Chance | Qty |\n|---|---|---|\n" + ''.join(
            f"| {link('items', e['itemID'], items.get(e['itemID'], {}).get('name', e['itemID']))} | {chance_txt(e.get('chance'))} | {rng(e.get('quantity', {}))} |\n"
            for e in dl.get('items', [])) + "\n")
    locs = []
    for mp in sorted(spawn_maps.get(x, ())):
        pg = _map_pages.get(mp)
        if not pg: continue
        cnt = sum(qty for o, ms, act, qty in pg['spawns'] if x in ms)
        later = any(not act for o, ms, act, qty in pg['spawns'] if x in ms)
        locs.append(f"| [{mp}](../maps/{mp}.md) | {region_of(mp) or '–'} | {cnt} | {'Appears later, during a quest' if later else '–'} |\n")
    if locs and (k != 'NPC' or len(locs) > 1):
        P.append("## Locations\n\n| Map | Region | Up to | Notes |\n|---|---|---|---|\n" + ''.join(locs[:60]) + (f"\n*{len(locs) - 60} further maps are not listed.*\n" if len(locs) > 60 else '') + "\n")
    if kill_reqs.get(x):
        rows = []
        for par, val, nxt in kill_reqs[x]:
            qs = node_quests(nxt) or node_quests(par)
            rows.append(f"- {QG.qlink(qs[0][0], qs[0][1]) if qs else 'A conversation'} with {speakers_md(par)} checks that {'this enemy has' if val == 1 else f'at least {val} of these enemies have'} been defeated.\n")
        P.append("## Quests that count defeats\n\n" + ''.join(list(dict.fromkeys(rows))[:20]) + "\n")
    rp = m.get('phraseID')
    if rp:
        P.append(npc_section(QG, x, notes, hist_md, prefix=(x + '-') if multi else '', with_notes=False, listed=shown_convs))
    else:
        P.append(hist_md('monsters', x))
    tech = [('Entry ID', f"`{x}`"), ('Spawn group', f"`{m.get('spawnGroup', x)}`"), ('Loot table', f"`{m.get('droplistID')}`" if m.get('droplistID') else '–'),
            ('Conversation', f"`{rp}`" if rp else '–'), ('Faction', f"`{m.get('faction')}`" if m.get('faction') else '–'),
            ('Movement', m.get('movementAggressionType', '–')), ('Icon', f"`{m.get('iconID', '–')}`"),
            ('Defined in', f"`res/raw/{FILE_OF.get(('monsterlist', x), '?')}`")]
    P.append(f'\n??? info "Technical information{(" (" + x + ")") if multi else ""}"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {a} | {b} |\n" for a, b in tech) +
             "\n    Raw data:\n\n" + raw_json(m) + '\n')
    return ''.join(P)

enemy_rows, npc_rows = [], []
for c, ids in group_ids.items():
    m = monsters[c]; nm = (m.get('name') or '').strip() or c
    ic = icon(m.get('iconID'), 'monsters') or next((icon(monsters[x].get('iconID'), 'monsters') for x in ids if icon(monsters[x].get('iconID'), 'monsters')), None)
    gk = group_kind(ids); multi = len(ids) > 1
    fv = [x for x in ids if kind_of(x) != 'NPC']
    fv = [x for x in fv if 'maxHP' in monsters[x]] or fv   # ranges use entries that define combat statistics
    roles = '; '.join(dict.fromkeys(r for x in ids for r in [role_text(x)] if r))
    roles_plain = '; '.join(dict.fromkeys(r for x in ids for r in [role_text(x, False)] if r))
    cap = lambda t: t[:1].upper() + t[1:]
    regs = ', '.join(dict.fromkeys(r for x in ids for r in [where(x)] if r))
    intro_v = [introduced('monsters', x) for x in ids]
    # meta description
    if gk == 'Enemy':
        _top = list(dict.fromkeys(items.get(e['itemID'], {}).get('name', e['itemID']) for x in ids for e in (droplists.get(monsters[x].get('droplistID')) or {}).get('items', [])))[:4]
        desc = (f"{nm} is an enemy in Andor's Trail ({(m.get('monsterClass') or 'humanoid').lower()}) with "
                f"{span([monsters[x].get('maxHP', 1) for x in fv])} HP, worth {span([monster_xp(monsters[x]) for x in fv])} XP"
                + (f", found in {regs}" if regs else '') + '.' + (f" Drops: {', '.join(_top)}." if _top else ''))
    else:
        desc = (f"{nm} is a{' non-player character (NPC)' if gk == 'NPC' else 'n NPC who can also be fought'} in Andor's Trail"
                + (f", found in {regs}" if regs else '') + '. ' + (cap(roles_plain) + '.' if roles_plain else ''))
    info = [('Type', f"{gk} ({TYPE_HELP[gk]})"), ('Role', cap(roles) or None), ('Found in', regs or None)]
    if fv:
        info += [('Class', ', '.join(dict.fromkeys((monsters[x].get('monsterClass') or 'humanoid').capitalize() for x in fv))),
                 ('HP', span([monsters[x].get('maxHP', 1) for x in fv])), ('XP when defeated', span([monster_xp(monsters[x]) for x in fv], lambda v: f"{v:,}")),
                 ('Immune to critical hits', 'Yes' if any(monsters[x].get('monsterClass') in ('ghost', 'construct', 'demon') for x in fv) else None)]
    info += [('Entries in game data', len(ids) if multi else None), ('Entry ID', f"`{c}`" if not multi else None),
             ('Introduced', intro_v[0] if not multi else (sorted(intro_v, key=lambda s: s if s.startswith('v') else '~')[0] if intro_v[0] else None))]
    P = [front(desc), f"# {img(ic)} {nm}\n\n"]
    if not multi:
        if spawn_maps.get(c): P.append(f"**{'Found in' if gk == 'Enemy' else 'Where to find ' + md_esc(nm)}:** {place_links(c, pin=gk != 'Enemy')}\n\n")
        elif gk != 'Enemy': P.append(f"**Where to find {md_esc(nm)}:** not placed on any map; appears through a quest or scripted event.\n\n")
    P.append(infobox(info, '../../' + ic if ic else None))
    if multi:
        diffs = entry_differences(ids)
        P.append(f"!!! info \"{len(ids)} entries in the game data\"\n"
                 f"    The game's data files define {len(ids)} separate characters named {md_esc(nm)}. Andor's Trail stores a character as a new entry whenever it needs "
                 "different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. "
                 "Some entries represent the same person at different points in the story; others are different people who share a generic name. "
                 + (f"Here the entries differ in: {', '.join(diffs)}. " if diffs else "These entries are identical apart from their IDs. ")
                 + "This page combines them; each entry is described in its own section below.\n\n")
        P.append("| Entry | Type | Location | Role |" + (" HP |" if fv else '') + "\n|---|---|---|---|" + ("---|" if fv else '') + "\n" + ''.join(
            f"| [`{x}`](#v-{x}) | {kind_of(x)} | {place_links(x, 2, pin=bool(monsters[x].get('phraseID'))) or 'Not on a map'} | {role_text(x) or '–'} |"
            + (f" {monsters[x].get('maxHP', 1) if kind_of(x) != 'NPC' else '–'} |" if fv else '') + "\n" for x in ids) + "\n")
        shown = {}
        for x in ids:
            P.append(f"## {md_esc(var_label(x))} ({x}) {{ #v-{x} }}\n\n" + demote(variant_body(x, True, shown)) + "\n")
    else:
        P.append(variant_body(c, False, {}))
    if fv: P.append("\n" + XP_NOTE)
    P.append(notes('monsters', c, nm))
    P.append(f"\n<small>Data from v{VERSION}</small>\n")
    write(f'monsters/{c}.md', ''.join(P))
    # index rows
    if gk == 'NPC':
        npc_rows.append((nm.lower(), f"| {img(ic)} | [{md_esc(nm)}]({c}.md) | {roles or '–'} | {regs or '–'} |\n"))
    else:
        fm = [monsters[x] for x in fv]
        _dm = {json.dumps(mm.get('attackDamage') or {}, sort_keys=True) for mm in fm}
        dmg_s = (rng(fm[0].get('attackDamage')) if fm[0].get('attackDamage') else '0') if len(_dm) == 1 else \
            f"{min((mm.get('attackDamage') or {}).get('min', 0) for mm in fm)} to {max((mm.get('attackDamage') or {}).get('max', 0) for mm in fm)}"
        enemy_rows.append(((min(mm.get('maxHP', 1) for mm in fm), nm.lower()),
            f"| {img(ic)} | [{md_esc(nm)}]({c}.md) | {gk} | {', '.join(dict.fromkeys(mm.get('monsterClass') or 'humanoid' for mm in fm))} | {span([mm.get('maxHP', 1) for mm in fm])} | "
            f"{span([monster_xp(mm) for mm in fm], lambda v: f'{v:,}')} | {dmg_s} | "
            f"{span([mm.get('attackChance', 0) for mm in fm])} | {span([mm.get('blockChance', 0) for mm in fm])} | {span([mm.get('damageResistance', 0) for mm in fm])} |\n"))
n_types = Counter(group_kind(ids) for ids in group_ids.values())
write('monsters/index.md', front(f"Every enemy and non-player character in Andor's Trail v{VERSION}, with combat statistics, XP values, locations and roles.") +
      f"# Monsters & NPCs\n\nThis index covers every character in Andor's Trail v{VERSION}: {n_types['Enemy']} enemies, {n_types['NPC/Enemy']} characters who can be "
      f"spoken to and fought, and {n_types['NPC']} non-player characters (NPCs). The game data contains {len(monsters)} entries; entries that share a name are combined on one page.\n\n"
      "| Type | Meaning |\n|---|---|\n| Enemy | Hostile on sight. |\n| NPC/Enemy | Can be spoken to, but can also be fought: a dialogue choice can start combat, "
      "the character becomes hostile when your standing with its faction drops below zero, or another game entry with the same name is a hostile version of the character. |\n"
      "| NPC | Can be spoken to and cannot be attacked, so it has no combat statistics. |\n\n"
      "## Enemies\n\nSorted by HP, lowest first. Where several entries share a name, ranges are shown. AC = attack chance, BC = block chance, DR = damage resistance.\n\n"
      "| | Name | Type | Class | HP | XP | Damage | AC | BC | DR |\n|---|---|---|---|---|---|---|---|---|---|\n" + ''.join(r for _, r in sorted(enemy_rows)) +
      "\n## NPCs\n\nCharacters who cannot be attacked, in alphabetical order. The [Where is…?](../where.md) page lists them by location.\n\n"
      "| | Name | Role | Found in |\n|---|---|---|---|\n" + ''.join(r for _, r in sorted(npc_rows)))
_map_ctx['kind_of'] = kind_of

write_map_pages(_map_pages, _map_ctx, QG, notes, shopkeepers, introduced)

# quests: dependency-graph pages (tools/quests.py)
write_quest_pages(QG, write, VERSION, notes, hist_md, comp_md, H.verified)

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
STAT_SHORT = {'blockChance': 'block chance', 'attackChance': 'attack chance', 'maxHP': 'max HP', 'maxAP': 'max AP',
              'damageResistance': 'damage resistance', 'criticalSkill': 'critical skill'}
def prereq_short(sk):
    if sk['levelUpType'] == 'onlyByQuests':
        parts = ['Quest only']
    elif sk['levelUpType'] == 'firstLevelRequiresQuest':
        parts = ['First level from a quest, then skill points']
    else:
        parts = []
    for r in sk['requirements']:
        if r[0] == 'level' and r[1] + r[2] > 1: parts.append(f"Lv {r[1] + r[2]}+")
        elif r[0] == 'stat': parts.append(f"Base {STAT_SHORT.get(r[1], r[1])} {r[2] + r[3]}+")
        elif r[0] == 'skill': parts.append(f"[{skills.get(r[1], {}).get('name', r[1])}]({r[1]}.md) {r[2]}")
    return ' · '.join(parts) if parts else '–'
# --- who grants each skill: walk dialogue backwards from the granting node to the NPC who owns it
phrase_parents = defaultdict(list)   # phrase -> [(parent phrase, reply text, reply requirements)]
for cid, c in conversations.items():
    for r in c.get('replies') or []:
        if r.get('nextPhraseID'): phrase_parents[r['nextPhraseID']].append((cid, r.get('text', ''), r.get('requires') or []))
phrase_roots = defaultdict(list)     # root phrase -> NPCs who start talking with it
for mid, m in monsters.items():
    if m.get('phraseID'): phrase_roots[m['phraseID']].append(mid)
def npcs_reaching(pid, limit=3000):
    seen, stack, found = set(), [pid], set()
    while stack and len(seen) < limit:
        x = stack.pop()
        if x in seen: continue
        seen.add(x)
        found.update(phrase_roots.get(x, ()))
        stack.extend(par for par, _, _ in phrase_parents.get(x, ()))
    return sorted(found, key=lambda m: monsters[m].get('name', m))
def conv_req(r):
    t, rid, val, neg = r.get('requireType'), r.get('requireID'), r.get('value', 0), r.get('negate')
    nm = lambda i: '[%s](../items/%s.md)' % (items.get(i, {}).get('name', i), i)
    if rid == 'gold' and t in ('inventoryRemove', 'inventoryKeep'):
        return f"{'pay' if t == 'inventoryRemove' else 'have'} {val:,} gold"
    if t == 'inventoryRemove': return f"hand over {val}× {nm(rid)}"
    if t == 'inventoryKeep': return f"{'not ' if neg else ''}carry {val}× {nm(rid)}"
    if t == 'wear': return f"{'not ' if neg else ''}wearing {nm(rid)}"
    if t in ('questProgress', 'questLatestProgress'):
        qn = quests.get(rid, {}).get('name', rid)
        return f"{'not yet ' if neg else ''}reached stage {val} of [{qn}](../quests/{rid}.md)"
    if t == 'skillLevel': return f"{skills.get(rid, {}).get('name', rid)} level {val}+"
    if t == 'killedMonster': return f"killed {val}× {monsters.get(rid, {}).get('name', rid)}"
    return f"{'not ' if neg else ''}{t} {rid or ''} {val or ''}".strip()
def reply_label(t):
    t = re.sub(r'\{(\d+)\}', lambda m: f"{int(m.group(1)):,}", (t or '').strip())
    return '(continue)' if t in ('N', '') else t
def short(t, n=180):
    t = ' '.join(html.unescape(t or '').split())
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '…'

LUT = {'alwaysShown': 'Skill points', 'firstLevelRequiresQuest': 'First level from a quest, then skill points', 'onlyByQuests': 'Quest reward only'}
def level_rows(sk):
    """Per-level requirement table: exactly what the next point needs (value = level x step + start)."""
    reqs = sk['requirements']
    mx = sk['maxLevel']
    shown = list(range(1, (mx if isinstance(mx, int) else 5) + 1))[:10]
    cols = []
    for r in reqs:
        if r[0] == 'level': cols.append(('Character level', lambda n, r=r: n * r[1] + r[2]))
        elif r[0] == 'stat': cols.append((f"Base {STAT_SHORT.get(r[1], r[1])}", lambda n, r=r: n * r[2] + r[3]))
        elif r[0] == 'skill': cols.append((f"[{skills.get(r[1], {}).get('name', r[1])}]({r[1]}.md) level", lambda n, r=r: n * r[2]))
    if not cols and sk['levelUpType'] == 'alwaysShown':
        return "No requirements: any skill point can go here.\n"
    head = "| Skill level |" + ''.join(f" {c[0]} |" for c in cols) + (" Source |" if sk['levelUpType'] != 'alwaysShown' else "")
    out = [head, '|' + '---|' * (len(cols) + 1 + (sk['levelUpType'] != 'alwaysShown'))]
    for n in shown:
        src = ''
        if sk['levelUpType'] == 'onlyByQuests': src = ' Quest reward |'
        elif sk['levelUpType'] == 'firstLevelRequiresQuest': src = (' Quest reward |' if n == 1 else ' Skill point |')
        out.append(f"| {n} |" + ''.join(f" {c[1](n)} |" for c in cols) + src)
    if not isinstance(mx, int):
        out.append("| … |" + ''.join(f" +{c[1](2) - c[1](1)} per level |" for c in cols) + (" Skill point |" if sk['levelUpType'] != 'alwaysShown' else ""))
    return '\n'.join(out) + '\n'

for sid, sk in skills.items():
    first_req = prereq_short(sk) if 'prereq_short' in globals() else ''
    info = [('Category', sk['category'].capitalize()), ('Max level', sk['maxLevel'] if sk['maxLevel'] != 'unlimited' else 'Unlimited'),
            ('Obtained via', LUT.get(sk['levelUpType'], sk['levelUpType'])),
            ('Also from quests', 'Yes' if sid in skill_sources and sk['levelUpType'] == 'alwaysShown' else None),
            ('Unlocks', ', '.join(f"[{skills[u]['name']}]({u}.md)" for u, _ in unlocks.get(sid, [])) or None)]
    P = [f"# {sk['name']}\n\n*{sk['summary']}*\n\n",
         '<div class="infobox" markdown>\n\n| | |\n|---|---|\n' + ''.join(f"| **{k}** | {v} |\n" for k, v in info if v) + '\n</div>\n\n',
         "## Effect\n\n" + (html.unescape(sk['long']).replace('\n', '\n\n') if sk['long'] else sk['short']) + "\n\n",
         "## Requirements per skill level\n\n" + level_rows(sk) + H.verified("game code (`SkillCollection.java`)", VERSION),
         ("See [Conditions](../conditions/index.md#categories-and-resistance) for the conditions this skill affects.\n\n"
          if sid in ('resistanceMental', 'resistancePhysical', 'resistanceBlood', 'shadowBless', 'rejuvenation', 'sporeImmunity') else '')]
    if sk['levelUpType'] == 'firstLevelRequiresQuest':
        P.append("The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.\n\n")
    if unlocks.get(sid):
        P.append("## Unlocks\n\n" + ''.join(f"- [{skills[u]['name']}]({u}.md): needs this skill at level {n}\n" for u, n in unlocks[sid]) + '\n')
    if skill_sources.get(sid):
        P.append("## Relevant quest\n\n")
        groups = defaultdict(list)   # (quest, stage) -> granting nodes
        for cid in sorted(skill_sources[sid]):
            c = conversations[cid]
            qrw = next(((r['rewardID'], r.get('value')) for r in c.get('rewards', []) or []
                        if r.get('rewardType') == 'questProgress' and r.get('rewardID') in quests), (None, None))
            groups[qrw].append(cid)
        for (q, v), cids in groups.items():
            P.append(f"**Quest:** [{quests[q].get('name', q)}](../quests/{q}.md#stage-{v}) (reaching stage {v})\n\n" if q
                     else "**Quest:** none. This is a standalone conversation.\n\n")
            npcs = sorted({n for cid in cids for n in npcs_reaching(cid)}, key=lambda n: monsters[n].get('name', n))
            P.append(("**NPC:** " + ', '.join(f"[{monsters[n].get('name', n)}](../monsters/{n}.md)" +
                      (f" ({', '.join(sorted(spawn_maps[n])[:2])})" if spawn_maps.get(n) else '') for n in npcs[:4]))
                     if npcs else "**Source:** a scripted event, not a regular conversation")
            P.append("\n\n")
            k = 0
            for cid in cids:
                c = conversations[cid]
                amount = next((r.get('value', 1) for r in c.get('rewards', []) if r.get('rewardType') == 'skillIncrease' and r.get('rewardID') == sid), 1)
                for par, text, reqs in (phrase_parents.get(cid) or [(None, '', [])]):
                    k += 1
                    line = f"{k}. " + (f"Choose “{short(reply_label(text), 110)}”" if par else "Triggered automatically")
                    if reqs: line += " — **requires:** " + '; '.join(conv_req(r) for r in reqs)
                    line += f" → +{amount} level{'s' if amount != 1 else ''}"
                    if c.get('message'): line += f". NPC: “{short(c['message'], 120)}”"
                    P.append(line + "\n")
            P.append("\n")
    tech = [('Skill ID', f"`{sid}`"), ('In-game list position', list(skills).index(sid) + 1), ('Level-up type', f"`{sk['levelUpType']}`"),
            ('Category (internal)', f"`{sk['category']}`"),
            ('String keys', f"`skill_title_{SKILL_STRING_KEY.get(sid, sid)}`, `skill_longdescription_{SKILL_STRING_KEY.get(sid, sid)}`"),
            ('Values in description', ', '.join(f"`{a}` = {v}" for a, v in skill_desc_consts.get(sid, [])) or '–'),
            ('Granting dialogue nodes', ', '.join(f"`{c}`" for c in sorted(skill_sources.get(sid, ()))) or '–'),
            ('Source files', '`model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml`')]
    P.append(notes('skills', sid, sk['name']) + '\n')
    P.append('??? info "Technical information"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {k} | {v} |\n" for k, v in tech) + '\n')
    write(f'skills/{sid}.md', ''.join(P))

sp_levels = [l for l in range(LV['first_sp'], 61, LV['every_sp'])]
exp_rows = ''.join(f"| {l} | {exp_to_reach(l):,} | {LV['exp_base'] * l * l:,} |\n" for l in (2, 5, 10, 15, 20, 25, 30, 40, 50, 60))
def hit_f(gap): return 50 * (1 + 2 / math.pi * math.atan((gap - 50) / 40))
hit_rows = ''.join(f"| {g:+d} | {hit_pct(g)}% | +{hit_f(g + 5) - hit_f(g):.1f}% |\n" for g in (-50, 0, 25, 50, 75, 100, 150, 200, 300))
crit_rows = ''.join(f"| {c} | {crit_pct(c)}% |\n" for c in (5, 10, 20, 30, 45, 60, 80, 100, 150))
by_cat = defaultdict(list)
for sid, sk in skills.items(): by_cat[sk['category']].append(sid)


# --- charts (matplotlib, Cobalt colours)
def make_charts():
    import matplotlib; matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    out = os.path.join(DOCS, 'assets', 'charts'); os.makedirs(out, exist_ok=True)
    BG, FG, GRID, OR, CY, GR = '#122438', '#dadada', '#2e4464', '#ffb400', '#5ee3f1', '#8c8c8c'
    def fig(title, xl, yl):
        f, ax = plt.subplots(figsize=(7, 3.6), dpi=110)
        f.patch.set_facecolor(BG); ax.set_facecolor(BG)
        for sp in ax.spines.values(): sp.set_color(GR)
        ax.tick_params(colors=FG); ax.grid(color=GRID, lw=.8)
        ax.set_title(title, color='#fcfcfc', fontsize=12, fontweight='bold'); ax.set_xlabel(xl, color=FG); ax.set_ylabel(yl, color=FG)
        return f, ax
    def save(f, name):
        f.tight_layout(); f.savefig(os.path.join(out, name), facecolor=BG); plt.close(f)
    # hit chance curve
    gaps = list(range(-100, 351, 2)); f, ax = fig('Hit chance vs. attack chance − block chance', 'Your attack chance − target block chance', 'Hit chance (%)')
    ax.axvspan(25, 100, color=OR, alpha=.12); ax.plot(gaps, [hit_f(g) for g in gaps], color=OR, lw=2.5)
    ax.text(62, 8, 'sweet spot', color=OR, ha='center'); ax.set_ylim(0, 100); save(f, 'hit_chance.png')
    # value of +5 attack chance
    f, ax = fig('What +5 attack chance is worth', 'Current gap (attack chance − block chance)', 'Extra hit chance (% points)')
    ax.fill_between(gaps, [hit_f(g + 5) - hit_f(g) for g in gaps], color=CY, alpha=.35); ax.plot(gaps, [hit_f(g + 5) - hit_f(g) for g in gaps], color=CY, lw=2)
    save(f, 'hit_marginal.png')
    # crit chance
    cs = list(range(0, 201)); f, ax = fig('Critical hit chance vs. critical skill', 'Critical skill', 'Crit chance (%)')
    ax.plot(cs, [crit_pct(c) for c in cs], color=OR, lw=2.5, drawstyle='steps-post'); save(f, 'crit_chance.png')
    # attacks per turn heatmap
    costs = list(range(2, 9)); aps = [10, 11, 12]
    f, ax = fig('Attacks per turn', 'Attack cost (AP)', 'Max AP')
    grid = [[ap // c for c in costs] for ap in aps]
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('cobalt', ['#1a3050', '#4a6390', '#ffb400'])
    ax.imshow(grid, cmap=cmap, vmin=1, vmax=6, aspect='auto'); ax.grid(False)
    ax.set_xticks(range(len(costs)), costs); ax.set_yticks(range(len(aps)), aps)
    for i, ap in enumerate(aps):
        for j, c in enumerate(costs): ax.text(j, i, ap // c, ha='center', va='center', color='#0c1828' if ap // c >= 5 else '#fcfcfc', fontweight='bold', fontsize=12)
    save(f, 'attacks_per_turn.png')
    # experience
    lv = list(range(1, 61)); f, ax = fig('Experience needed for the next level', 'Current level', 'XP to next level')
    ax.plot(lv, [LV['exp_base'] * l * l for l in lv], color=CY, lw=2.5)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{int(v):,}')); save(f, 'experience.png')
    # Fortitude vs health level-ups
    L = list(range(1, 51)); f, ax = fig('Bonus max HP: Fortitude vs. health level-ups', 'Character level', 'Bonus max HP')
    fort = lambda starts: [sum(max(0, l - st) * LV['fort'] for st in starts) for l in L]
    ax.plot(L, fort([5]), color=OR, lw=2.5, label='Fortitude 1 (taken at 5)')
    ax.plot(L, fort([5, 20]), color=OR, lw=1.8, ls='--', label='Fortitude 1–2 (5, 20)')
    ax.plot(L, fort([5, 20, 35]), color=OR, lw=1.2, ls=':', label='Fortitude 1–3 (5, 20, 35)')
    ax.plot(L, [LV['hp'] * min(9, max(0, l - 1)) for l in L], color=CY, lw=2, label='9 health level-ups (levels 2–10)')
    ax.legend(facecolor=BG, edgecolor=GR, labelcolor=FG, fontsize=8); save(f, 'fortitude_vs_health.png')
make_charts()
CH = '../assets/charts/'

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

One bonus is chosen at each level-up, and the choice is permanent (the game has no way to reallocate it). These choices form your **base stats**, which are the only values that skill requirements check. Bonuses from equipment and skills do not count toward requirements.

**Skill points:** levels {', '.join(map(str, sp_list))}. That is {len([l for l in sp_levels if l <= 50])} skill points by level 50.
**Experience:** level L → L+1 costs {LV['exp_base']} × L². The cost grows with the square of the level.

![Experience needed per level]({CH}experience.png)

![Fortitude vs health level-ups]({CH}fortitude_vs_health.png)

One point of [Fortitude](fortitude.md) at level 5 out-earns a health level-up by level 10. Add a second level at 20 and it matches nine health level-ups by level 35, while those nine level-ups were free to go into other stats. Details on [Strategy](../strategy/levelling.md).

| Level | Total XP | XP to next |
|---|---|---|
{exp_rows}"""
combat_body = f"""Every attack is resolved in the same four steps, described below. The [stat glossary]({G}) explains each stat.

**1 · Hit?** `hit % = 50 × (1 + (2/π) × arctan((AC − BC − 50) / 40))`

![Hit chance curve]({CH}hit_chance.png)

![Value of +5 attack chance]({CH}hit_marginal.png)

| AC − BC | Hit | +5 AC adds |
|---|---|---|
{hit_rows}
**2 · Damage:** random between min and max attack damage.

**3 · Critical?** Only if you have critical skill above 0 **and** a critical multiplier, which comes from your weapon (or from [Way of the Monk](fightstyleUnarmedUnarmored.md) when fighting unarmed). Without a multiplier, critical skill has no effect. Ghosts, constructs and demons are immune to critical hits. `crit % = −5 + 2 × √(5 × critical skill)`, then damage × multiplier.

![Crit chance curve]({CH}crit_chance.png)

| Crit skill | Crit % |
|---|---|
{crit_rows}
**4 · Armor:** the target's damage resistance is subtracted from the result, with a minimum of 0, so a hit can deal no damage at all.

**Attacks per turn** = max AP ÷ attack cost, rounded down.

![Attacks per turn by AP and attack cost]({CH}attacks_per_turn.png)"""
def skill_row(sid, star=False):
    sk = skills[sid]
    mx = sk['maxLevel'] if sk['maxLevel'] != 'unlimited' else '∞'
    return f"| [{md_esc(sk['name'])}]({sid}.md){'\\*' if star else ''} | {mx} | {prereq_short(sk)} | {md_esc(sk['summary'])} |\n"
points_skills = [sid for sid, sk in skills.items() if sk['levelUpType'] == 'alwaysShown']
quest_skills = [sid for sid, sk in skills.items() if sk['levelUpType'] != 'alwaysShown']
hdr = "| Skill | Max | Prerequisite | What it does |\n|---|---|---|---|\n"
skill_body = ("**Learned with skill points** (in the order the game lists them)\n\n" + hdr +
              ''.join(skill_row(x, x in skill_sources) for x in points_skills) +
              "\n\\* Some quests also reward a level of this skill directly, without spending a skill point.\n\n**Unlocked through quests**\n\n" + hdr +
              ''.join(skill_row(x) for x in quest_skills) +
              "\n")
write('skills/index.md', f"""# Stats & Skills

How character statistics, levelling and combat work in v{VERSION}, as implemented in the game's source code. Each section can be collapsed by clicking its heading. For recommendations on how to use this information, see [Strategy](../strategy/index.md).
""" + section('Starting stats (level 1)', start_tbl) + section('Levelling up', level_body)
  + section('How combat works', combat_body) + section(f'All skills ({len(skills)})', skill_body))

# --- stat glossary (what each stat does)
write('skills/stats.md', f"""# Stat glossary

The effect of each character statistic in v{VERSION}. Starting values live on [Stats & Skills](index.md).

## Max HP
Your maximum health. When current HP reaches 0, the character is defeated. Raised by the **max health** level-up (+{LV['hp']}), by [Fortitude](fortitude.md) (+{LV['fort']} per skill level on every later level-up), and by some equipment. See [Strategy](../strategy/levelling.md) for a comparison of Fortitude and health level-ups.

## Max AP
Action points per combat turn. Attacking, moving and using items all cost AP. [Combat Speed](speed.md) adds +1 per level, up to 2.

## Attack chance
Your accuracy. It is compared with the target's block chance to determine whether an attack hits, using a curve with diminishing returns at both ends ([details](index.md)). Raised by the **attack chance** level-up (+{LV['ac']}), [Weapon Accuracy](weaponChance.md) (+12 per level), weapons and proficiencies.

## Attack damage
Each hit rolls a random number between your minimum and maximum damage. The **attack damage** level-up adds +{LV['dmg']} to both. [Hard Hit](weaponDmg.md) adds +2 to the maximum only, which raises average damage by 1.

## Block chance
Your evasion. It is compared with the attacker's attack chance using the same curve. Raised by the **block chance** level-up (+{LV['bc']}), [Dodge](dodge.md) (+9 per level), shields and armor. Only block chance from level-ups counts toward skill requirements such as [Bark Skin](barkSkin.md); block chance from shields and armor does not.

## Damage resistance
Subtracted from every hit you take, after critical multipliers. Damage cannot go below 0, so damage resistance is most effective against enemies that deal many small hits and less effective against enemies that deal large hits. Raised by [Bark Skin](barkSkin.md) (+1 per level), shields and armor.

## Critical skill
Determines your critical hit chance: `−5 + 2 × √(5 × critical skill)`. Because of the square root, each additional point adds less than the previous one. It has **no effect** unless you also have a critical multiplier (from your weapon, or [Way of the Monk](fightstyleUnarmedUnarmored.md)). [More Criticals](moreCriticals.md) raises it by 20% per level.

## Critical multiplier
How hard a critical hit lands (e.g. ×2). Weapons provide it. Unarmed attacks have none, so an unarmed character cannot land critical hits unless they learn [Way of the Monk](fightstyleUnarmedUnarmored.md), which grants ×1.25 per level. [Better Criticals](betterCriticals.md) raises it by 25% per level.

## Attack cost
AP spent per attack: {LV['atk_cost']} unarmed, or whatever your weapon says. Attacks per turn = max AP ÷ attack cost, rounded down, so reducing attack cost by one point either adds a full attack per turn or has no effect, depending on the values involved.

## Move cost
AP to move one tile during combat. Heavy armor increases it.

## Use item cost
AP to use an item, e.g. drinking a potion in the middle of a fight.

## Re-equip cost
AP to change equipment during combat. Changing equipment during combat is possible but uses AP that could otherwise be spent attacking.
""")
# ---------------------------------------------------------------- "Where is…?" page
def _letter(n): c = (n[:1] or '#').upper(); return c if c.isalpha() else '#'
people = defaultdict(list)
for mid, m in monsters.items():
    if m.get('phraseID') and (m.get('name') or '').strip(): people[m['name'].strip()].append(mid)
W = [front("Where to find every NPC, shop, skill trainer, quest giver and place in Andor's Trail, with map links that jump straight to them."),
     f"# Where is…?\n\nEvery named character, shop, skill trainer, quest giver and place in Andor's Trail v{VERSION}. "
     "Map links open the labelled map and jump to that character's pin. Press **Ctrl+F** (or use the search box) to find a name.\n\n"
     "**Jump to:** [People](#people) · [Shops by region](#shops-by-region) · [Skill trainers](#skill-trainers) · [Quest givers](#quest-givers) · [Places](#places)\n\n"]
W.append("## People\n\n")
by_letter = defaultdict(list)
for nm in sorted(people, key=str.lower): by_letter[_letter(nm)].append(nm)
W.append(' · '.join(f"[{L_}](#people-{L_.lower() if L_ != '#' else 'other'})" for L_ in sorted(by_letter)) + "\n\n")
for L_ in sorted(by_letter):
    W.append(f'<h3 id="people-{L_.lower() if L_ != "#" else "other"}">{L_}</h3>\n\n| Name | Where | Role |\n|---|---|---|\n')
    for nm in by_letter[L_]:
        ids = people[nm]
        placed = [x for x in ids if spawn_maps.get(x)]
        if not placed: where_md = '*not on any map; appears through an event*'
        else:
            pairs = []
            for x in placed:
                for mp in sorted(spawn_maps[x]): pairs.append((region_of(mp), mp, x))
            pairs = sorted(set(pairs), key=lambda p: (p[0] is None, p[0] or '', p[1]))
            where_md = ', '.join(f"{(p[0] + ': ') if p[0] else ''}[{p[1]}](maps/{p[1]}.md#pin-npc-{p[2]})" for p in pairs[:3]) + (f" (+{len(pairs) - 3} more)" if len(pairs) > 3 else '')
        roles = '; '.join(dict.fromkeys(r for x in ids for r in [role_text(x).replace('](../', '](')] if r))
        link = f"[{md_esc(nm)}](monsters/{canon_of[ids[0]]}.md)"
        W.append(f"| {link} | {where_md} | {roles or '–'} |\n")
    W.append("\n")
W.append("## Shops by region\n\n| Region | Shopkeepers |\n|---|---|\n")
shop_reg = defaultdict(set)
for x in shopkeepers:
    for mp in spawn_maps.get(x, ()): shop_reg[region_of(mp) or 'Elsewhere'].add(x)
for reg in sorted(shop_reg, key=lambda r: (r == 'Elsewhere', r)):
    W.append(f"| {reg} | " + ', '.join(dict.fromkeys(f"[{md_esc(monsters[x].get('name') or x)}](monsters/{canon_of[x]}.md)" for x in sorted(shop_reg[reg], key=lambda x: monsters[x].get('name') or x))) + " |\n")
W.append("\n## Skill trainers\n\nCharacters who can grant a skill level in conversation (usually as part of a quest).\n\n| Skill | Who | Where |\n|---|---|---|\n")
for sid in skills:
    who = sorted({x for x, sk in trainer_of.items() if sid in sk}, key=lambda x: monsters[x].get('name') or x)
    if who:
        W.append(f"| [{skills[sid]['name']}](skills/{sid}.md) | " + ', '.join(dict.fromkeys(f"[{md_esc(monsters[x].get('name') or x)}](monsters/{canon_of[x]}.md)" for x in who)) +
                 " | " + ', '.join(dict.fromkeys(r for x in who for r in [where(x)] if r)) + " |\n")
W.append("\n## Quest givers\n\nWho starts each journal quest, and where.\n\n| Quest | Starts with | Where |\n|---|---|---|\n")
for qid in sorted((q for q in quests if quests[q].get('showInLog', 0)), key=lambda q: quests[q].get('name', q).lower()):
    who = sorted({x for x, qs in giver_of.items() if qid in qs}, key=lambda x: monsters[x].get('name') or x)
    if who:
        W.append(f"| [{md_esc(quests[qid].get('name', qid))}](quests/{qid}.md) | " + ', '.join(dict.fromkeys(f"[{md_esc(monsters[x].get('name') or x)}](monsters/{canon_of[x]}.md)" for x in who[:3])) +
                 " | " + ', '.join(dict.fromkeys(r for x in who for r in [where(x)] if r)) + " |\n")
W.append("\n## Places\n\nNamed towns and landmarks, with every map that belongs to them.\n\n| Place | Type | Maps |\n|---|---|---|\n")
area_maps = defaultdict(list)
for mp, pg in _map_pages.items():
    if pg.get('area') and pg['area'][0] and pg['area'][2] == 'in': area_maps[(pg['area'][0], pg['area'][1])].append(mp)
for (nm, typ), mps in sorted(area_maps.items(), key=lambda kv: kv[0][0].lower()):
    mps = sorted(mps, key=lambda mp: (not _map_pages[mp]['outdoors'], mp))
    W.append(f"| **{md_esc(nm)}** | {typ or '–'} | " + ', '.join(f"[{mp}](maps/{mp}.md)" for mp in mps[:8]) + (f" (+{len(mps) - 8} more)" if len(mps) > 8 else '') + " |\n")
W.append(H.verified("monster, map, dialogue and world-map data", VERSION))
write('where.md', ''.join(W))

# ---------------------------------------------------------------- build calculator data + page
def _eqstats(e):
    e = e or {}
    d = e.get('increaseAttackDamage') or {}
    return {'hp': e.get('increaseMaxHP', 0), 'ap': e.get('increaseMaxAP', 0), 'mv': e.get('increaseMoveCost', 0), 'use': e.get('increaseUseItemCost', 0),
            're': e.get('increaseReequipCost', 0), 'atk': e.get('increaseAttackCost', 0), 'ac': e.get('increaseAttackChance', 0),
            'bc': e.get('increaseBlockChance', 0), 'dmin': d.get('min', 0), 'dmax': d.get('max', 0), 'nwdm': e.get('setNonWeaponDamageModifier', 100),
            'cs': e.get('increaseCriticalSkill', 0), 'cm': e.get('setCriticalMultiplier', 0), 'dr': e.get('increaseDamageResistance', 0)}
calc_items = {}
for iid, it in items.items():
    c = cats.get(it.get('category'), {})
    if c.get('actionType') != 'equip': continue
    calc_items[iid] = {'n': it.get('name', iid), 'cat': it.get('category'), 'r': it.get('displaytype', 'ordinary'),
                       's': _eqstats(it.get('equipEffect')) if it.get('equipEffect') else None,
                       'cond': [conditions.get(x.get('condition'), {}).get('name', x.get('condition')) for x in (it.get('equipEffect') or {}).get('addedConditions', [])]}
calc_cats = {cid: {'slot': c.get('inventorySlot'), 'size': c.get('size'), 'prof': prof_skill(cid)} for cid, c in cats.items() if c.get('actionType') == 'equip'}
calc_mons = []
for mid, m in monsters.items():
    if kind_of(mid) == 'NPC': continue
    d = m.get('attackDamage') or {}
    calc_mons.append([mid, m.get('name') or mid, m.get('maxHP', 1), m.get('attackChance', 0), m.get('blockChance', 0), m.get('damageResistance', 0),
                      d.get('min', 0), d.get('max', 0), m.get('maxAP', 10), m.get('attackCost', 10), m.get('criticalSkill', 0), m.get('criticalMultiplier', 0), m.get('monsterClass')])
calc = {'v': VERSION,
        'base': {'maxHP': base.get('maxHP', 25), 'maxAP': base.get('maxAP', 10), 'attackChance': base.get('attackChance', 60), 'dmin': base_dmg_min, 'dmax': base_dmg_max,
                 'blockChance': base.get('blockChance', 0), 'damageResistance': base.get('damageResistance', 0), 'moveCost': base.get('moveCost', 6),
                 'attackCost': LV['atk_cost'], 'useItemCost': base.get('useItemCost', 5), 'reequipCost': base.get('reequipCost', 5),
                 'criticalSkill': base.get('criticalSkill', 0), 'criticalMultiplier': base.get('criticalMultiplier', 1)},
        'lv': {'hp': LV['hp'], 'ac': LV['ac'], 'dmg': LV['dmg'], 'bc': LV['bc'], 'first': LV['first_sp'], 'every': LV['every_sp'], 'fort': LV['fort']},
        'c': {k: v for k, v in consts.items() if k.startswith(('PER_SKILLPOINT', 'DUALWIELD'))},
        'skills': [{'id': sid, 'name': sk['name'], 'max': sk['maxLevel'] if isinstance(sk['maxLevel'], int) else 0, 'type': sk['levelUpType'],
                    'reqs': [list(r) for r in sk['requirements']], 'sum': sk['summary']} for sid, sk in skills.items()],
        'items': calc_items, 'cats': calc_cats, 'mons': calc_mons}
os.makedirs(os.path.join(DOCS, 'assets', 'calc'), exist_ok=True)
json.dump(calc, open(os.path.join(DOCS, 'assets', 'calc', 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
write('skills/calculator.md', f"""# Build calculator

Plan a character before spending level-ups and skill points. Pick a level, split your level-ups, choose skills and gear, and see your final stats, worked out
**the same way the game does it**: the formulas below are a line-by-line port of the game's own stat code for v{VERSION}.

<div class="build-calc" data-src="../../assets/calc/data.json" markdown="0"><noscript>The calculator needs JavaScript.</noscript></div>

??? info "How the numbers are calculated"

    In the order the game applies them (`ActorStatsController.recalculatePlayerStats`):

    1. **Base stats + level-ups.** Starting stats, plus each level-up choice. [Fortitude](fortitude.md) adds HP to every level-up *after* you learn it; the calculator assumes you learn each level as early as allowed.
    2. **Main weapon** sets your attack cost and critical multiplier, then its stats are added.
    3. **Off-hand.** A shield adds its stats directly. A second weapon is blended in by [Dual Wield](fightstyleDualWield.md) at 25 / 50 / 100% efficiency (level 0 / 1 / 2).
    4. **Fighting styles:** two-handed, weapon & shield, dual wield, or [Way of the Monk](fightstyleUnarmedUnarmored.md) (no weapon, no off-hand, no weighted armor).
    5. **Armor and jewelry** stats are added.
    6. **Proficiencies** boost your main weapon's, shield's and armor's own bonuses by a percentage.
    7. **Skills:** Weapon Accuracy, Hard Hit, Dodge, Bark Skin, More/Better Criticals, Combat Speed.
    8. **Damage modifier.** Some weapons scale your *non-weapon* damage (base, level-ups, rings, skills) up or down.
    9. **Caps:** attack chance can't go below 0, and neither can damage.

    Percentages round down, as in the game. Effects from potions and other temporary conditions aren't included.

<p class="verified">Verified against v{VERSION} game code (ActorStatsController, ItemController, SkillController, CombatController) and item data.</p>
""")

# ---------------------------------------------------------------- conditions (tools/conditions.py)
from conditions import write_condition_pages
shutil.rmtree(os.path.join(DOCS, 'conditions'), ignore_errors=True)
write_condition_pages(dict(conditions=conditions, items=items, monsters=monsters, conversations=conversations, skills=skills,
    write=write, md_esc=md_esc, chance_txt=chance_txt, chance_pct=chance_pct, icon=icon, VERSION=VERSION, consts=consts, canon_of=canon_of,
    where=where, speakers_md=speakers_md, node_quests=node_quests, QG=QG, verified=H.verified, notes=notes, file_of=FILE_OF,
    front=front, img=img, infobox=infobox, raw_json=raw_json, section=section))

# ---------------------------------------------------------------- version history pages
if hist:
    shutil.rmtree(os.path.join(DOCS, 'versions'), ignore_errors=True)
    H.write_version_pages(hist, write, _names, VERSION, page_exists)
    H.growth_chart(hist, os.path.join(DOCS, 'assets', 'charts', 'growth.png'))

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
header = "# Changelog\n\nWhat changed in each release, worked out by comparing the game's data before and after. This page is generated automatically.\n"
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
    body = f"\n## v{VERSION}\n\nFirst version tracked by this changelog. Earlier releases are covered on the [Version history](versions/index.md) pages.\n" + body
write('changelog.md', header + body)
json.dump(snap, open(snap_path, 'w'), indent=0, sort_keys=True)
open(os.path.join(DATA, 'VERSION'), 'w').write(VERSION + '\n')

# home page stats
n_rings = sum(1 for it in items.values() if it.get('category') == 'ring')
write('index.md', front(f"An unofficial reference wiki for Andor's Trail v{VERSION}: items, monsters and NPCs, skills, quests and maps, generated from the game's data files.") + f"""# Andor's Trail Wiki

A reference wiki for **Andor's Trail**, an open-source role-playing game in which the player searches for their missing brother, Andor.

All content is generated from the game's own data files and source code, so values on this wiki match those used by the game. When the developers publish a new release, the wiki is rebuilt automatically within an hour. Each page states the game version it describes. This build covers **v{VERSION}**, with version history back to v0.7.0.

<div class="grid cards" markdown>

- **[Items](items/index.md)**<br>{len(items)} items, including weapons, armor, jewelry and consumables
- **[Monsters & NPCs](monsters/index.md)**<br>Every enemy and non-player character, with statistics, locations and roles
- **[Stats & Skills](skills/index.md)**<br>Character statistics, levelling, combat formulas and all {len(skills)} skills
- **[Conditions](conditions/index.md)**<br>All {len(conditions)} conditions, such as poison, bleeding and blessings: effects, causes and remedies
- **[Strategy](strategy/index.md)**<br>Guidance on character builds, levelling and combat
- **[Quests](quests/index.md)**<br>{sum(1 for q in quests.values() if q.get('showInLog', 0))} journal quests with every stage, plus the hidden quest flags behind them
- **[World map](maps/index.md)**<br>{n_maps} maps with enemies, NPCs, containers and connections
- **[Version history](versions/index.md)**<br>Changes in every release since v0.7.0

</div>

<small>Game data © the Andor's Trail contributors, used under the project's open-source licenses. This is an unofficial fan wiki and is not affiliated with the developers.</small>
""")
# point links at non-canonical entry IDs to the combined character page (section anchor #v-<id>)
_alias = {x: c for x, c in canon_of.items() if x != c}
_mlink = re.compile(r'(monsters/)([A-Za-z0-9_\-]+)(\.md|/)(?![#\w])')
def _fix_links(mm):
    x = mm.group(2)
    return f"{mm.group(1)}{_alias[x]}{mm.group(3)}#v-{x}" if x in _alias else mm.group(0)
for _f in glob.glob(os.path.join(DOCS, '**', '*.md'), recursive=True):
    _t = open(_f, encoding='utf-8').read()
    _n = _mlink.sub(_fix_links, _t)
    if _n != _t: open(_f, 'w', encoding='utf-8').write(_n)
_left = [os.path.relpath(f, DOCS) for f in glob.glob(os.path.join(DOCS, '**', '*.md'), recursive=True)
         if re.search(r'%\d+\$[,.\d]*[dsf]', open(f, encoding='utf-8').read())]
for f in _left: print(f"::warning file=docs/{f}::Unfilled text placeholder (e.g. %1$d) left on this page")
print(f"Built v{VERSION}: {len(items)} items, {len(monsters)} monsters, {len(skills)} skills, {len(quests)} quests, {n_maps} maps")
