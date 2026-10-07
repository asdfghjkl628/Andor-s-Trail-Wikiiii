"""Conditions (actor conditions): one page per condition plus an overview, built from res/raw/actorconditions*.json
and the rules in ActorStatsController, SkillController, ConversationController and the item/monster parsers."""
from collections import defaultdict

FOREVER, UNTIL_SLEEP, REMOVE = 999, 998, -99
CATEGORY = {
    'physical': ('Physical', 'resistancePhysical'),
    'mental': ('Mental', 'resistanceMental'),
    'blood': ('Blood', 'resistanceBlood'),
    'spiritual': ('Spiritual', None),
}
STAT = {'increaseMaxHP': 'Max HP', 'increaseMaxAP': 'Max AP', 'increaseAttackChance': 'Attack chance', 'increaseAttackDamage': 'Attack damage',
        'increaseBlockChance': 'Block chance', 'increaseDamageResistance': 'Damage resistance', 'increaseCriticalSkill': 'Critical skill',
        'increaseAttackCost': 'Attack cost (AP)', 'increaseMoveCost': 'Move cost (AP)', 'increaseUseItemCost': 'Use item cost (AP)',
        'increaseReequipCost': 'Re-equip cost (AP)'}
SHORT = {'increaseMaxHP': 'max HP', 'increaseMaxAP': 'max AP', 'increaseAttackChance': 'attack chance', 'increaseAttackDamage': 'damage',
         'increaseBlockChance': 'block chance', 'increaseDamageResistance': 'damage resistance', 'increaseCriticalSkill': 'critical skill',
         'increaseAttackCost': 'attack cost', 'increaseMoveCost': 'move cost', 'increaseUseItemCost': 'item use cost', 'increaseReequipCost': 're-equip cost'}
# effect blocks: (owner kind, block, list key) -> (who receives it, how it happens)
ITEM_BLOCKS = {('useEffect', 'conditionsSource'): ('you', 'when used'),
               ('equipEffect', 'addedConditions'): ('you', 'while equipped'),
               ('hitEffect', 'conditionsSource'): ('you', 'when you hit with it'),
               ('hitEffect', 'conditionsTarget'): ('enemy', 'on the enemy you hit'),
               ('missEffect', 'conditionsSource'): ('you', 'when you miss with it'),
               ('missEffect', 'conditionsTarget'): ('enemy', 'on the enemy you miss'),
               ('killEffect', 'conditionsSource'): ('you', 'when you defeat an enemy'),
               ('hitReceivedEffect', 'conditionsSource'): ('you', 'when you are hit'),
               ('hitReceivedEffect', 'conditionsTarget'): ('enemy', 'on the enemy that hits you'),
               ('missReceivedEffect', 'conditionsSource'): ('you', 'when an attack misses you'),
               ('missReceivedEffect', 'conditionsTarget'): ('enemy', 'on the enemy that misses you')}
MONSTER_BLOCKS = {('hitEffect', 'conditionsTarget'): ('you', 'when it hits you'),
                  ('hitEffect', 'conditionsSource'): ('enemy', 'on itself, when it hits you'),
                  ('missEffect', 'conditionsTarget'): ('you', 'when it misses you'),
                  ('missEffect', 'conditionsSource'): ('enemy', 'on itself, when it misses you'),
                  ('hitReceivedEffect', 'conditionsTarget'): ('you', 'when you hit it'),
                  ('hitReceivedEffect', 'conditionsSource'): ('enemy', 'on itself, when you hit it'),
                  ('missReceivedEffect', 'conditionsTarget'): ('you', 'when you miss it'),
                  ('missReceivedEffect', 'conditionsSource'): ('enemy', 'on itself, when you miss it'),
                  ('deathEffect', 'conditionsSource'): ('you', 'when you defeat it')}
SKILL_SOURCES = {'crit1': ('crit1', 'PER_SKILLPOINT_INCREASE_CRIT1_CHANCE', 'on a critical hit'),
                 'crit2': ('crit2', 'PER_SKILLPOINT_INCREASE_CRIT2_CHANCE', 'on a critical hit'),
                 'concussion': ('concussion', 'PER_SKILLPOINT_INCREASE_CONCUSSION_CHANCE', 'on a hit when your attack chance exceeds the target\'s block chance by more than {CONCUSSION_THRESHOLD}')}


def _sign(v): return f"+{v}" if v > 0 else f"−{-v}" if v < 0 else "0"
def _rng(d):
    if isinstance(d, dict):
        a, b = d.get('min', 0), d.get('max', 0)
        return _sign(a) if a == b else f"{_sign(a)} to {_sign(b)}"
    return _sign(d)


def effect_kind(e, equip):
    """(action, magnitude, duration) following the parsers' defaults: equip effects default to magnitude 1 and last while worn;
    other effects default to magnitude −99 (remove) and duration 0."""
    if equip:
        mag = e.get('magnitude', 1)
        return ('immunity' if mag == REMOVE else 'apply'), mag, FOREVER
    mag, dur = e.get('magnitude', REMOVE), e.get('duration', 0)
    if mag == REMOVE: return ('remove' if dur == 0 else 'immunity'), mag, dur
    return 'apply', mag, dur


def dur_text(d, equip=False):
    if equip: return 'While equipped'
    if d == FOREVER: return 'Permanent'
    if d == UNTIL_SLEEP: return 'Until you rest'
    return f"{d} round{'s' if d != 1 else ''}"


def stat_rows(c):
    rows = []
    for k, lab in STAT.items():
        v = (c.get('abilityEffect') or {}).get(k)
        if v: rows.append((lab, _rng(v)))
    for blk, when in (('roundEffect', 'every round'), ('fullRoundEffect', 'every 25 seconds (outside combat)')):
        for k, lab in (('increaseCurrentHP', 'HP'), ('increaseCurrentAP', 'AP')):
            v = (c.get(blk) or {}).get(k)
            if v: rows.append((f"{lab} {when}", _rng(v)))
    return rows


def summary(c):
    parts = []
    for k, lab in SHORT.items():
        v = (c.get('abilityEffect') or {}).get(k)
        if v: parts.append(f"{lab} {_rng(v)}")
    for blk, when in (('roundEffect', 'per round'), ('fullRoundEffect', 'per 25 s')):
        for k, lab in (('increaseCurrentHP', 'HP'), ('increaseCurrentAP', 'AP')):
            v = (c.get(blk) or {}).get(k)
            if v: parts.append(f"{_rng(v)} {lab} {when}")
    return ', '.join(parts) or 'no direct statistical effect'


def write_condition_pages(X):
    conditions, items, monsters, conversations, skills = X['conditions'], X['items'], X['monsters'], X['conversations'], X['skills']
    write, md_esc, chance_txt, icon, VERSION, consts = X['write'], X['md_esc'], X['chance_txt'], X['icon'], X['VERSION'], X['consts']
    canon_of, where, speakers_md, node_quests, QG, verified, notes = X['canon_of'], X['where'], X['speakers_md'], X['node_quests'], X['QG'], X['verified'], X['notes']
    file_of = X['file_of']

    # ---- collect every place a condition is applied, removed, granted as immunity, or checked
    src = defaultdict(list)      # cid -> [dict(kind, who, how, action, mag, dur, chance, ...)]
    for iid, it in items.items():
        for (blk, key), (who, how) in ITEM_BLOCKS.items():
            for e in ((it.get(blk) or {}).get(key) or []):
                act, mag, dur = effect_kind(e, blk == 'equipEffect')
                src[e.get('condition')].append(dict(kind='item', id=iid, who=who, how=how, action=act, mag=mag, dur=dur,
                                                    equip=blk == 'equipEffect', chance=None if blk == 'equipEffect' else e.get('chance', '100')))
    for mid, m in monsters.items():
        for (blk, key), (who, how) in MONSTER_BLOCKS.items():
            for e in ((m.get(blk) or {}).get(key) or []):
                act, mag, dur = effect_kind(e, False)
                src[e.get('condition')].append(dict(kind='monster', id=mid, who=who, how=how, action=act, mag=mag, dur=dur, equip=False, chance=e.get('chance', '100')))
    checks = defaultdict(list)
    for cid, cv in conversations.items():
        for r in cv.get('rewards') or []:
            t = r.get('rewardType')
            if t == 'actorCondition':
                v = r.get('value', 0)
                act = 'remove' if v == REMOVE else 'apply'
                src[r.get('rewardID')].append(dict(kind='dialogue', id=cid, who='you', how='dialogue or event', action=act, mag=1 if act == 'apply' else REMOVE,
                                                   dur=v if act == 'apply' else 0, equip=False, chance='100'))
            elif t == 'actorConditionImmunity':
                src[r.get('rewardID')].append(dict(kind='dialogue', id=cid, who='you', how='dialogue or event', action='immunity', mag=REMOVE,
                                                   dur=r.get('value', 0), equip=False, chance='100'))
        for rep in cv.get('replies') or []:
            for q in rep.get('requires') or []:
                if q.get('requireType') == 'hasActorCondition':
                    checks[q.get('requireID')].append((cid, bool(q.get('negate')), rep.get('nextPhraseID')))
    for cid, (sid, const, how) in SKILL_SOURCES.items():
        if cid in conditions and sid in skills:
            src[cid].append(dict(kind='skill', id=sid, who='enemy', how=how.format(**{k: consts.get(k, '?') for k in ('CONCUSSION_THRESHOLD',)}),
                                 action='apply', mag=1, dur=5, equip=False, chance=f"{consts.get(const, '?')}% per skill level"))

    def ilink(i): return f"[{md_esc(items.get(i, {}).get('name', i))}](../items/{i}.md)"
    def mlink(i): return f"[{md_esc((monsters.get(i, {}).get('name') or i).strip())}](../monsters/{canon_of.get(i, i)}.md)"
    def chance_of(s): return s['chance'] if s['kind'] == 'skill' else ('–' if s['chance'] is None else chance_txt(s['chance']))

    def affects(cid):
        w = {s['who'] for s in src.get(cid, []) if s['action'] == 'apply'}
        return 'You and enemies' if w == {'you', 'enemy'} else 'You' if w == {'you'} else 'Enemies' if w == {'enemy'} else 'Not applied by any game data'

    def rest_text(cid):
        durs = {s['dur'] for s in src.get(cid, []) if s['action'] == 'apply'}
        out = []
        if any(d != FOREVER for d in durs): out.append('timed ones wear off, or rest them away')
        if FOREVER in durs: out.append('permanent ones (equipment, story events) stay through rest')
        return out

    # ---- per-condition pages
    rows = {True: defaultdict(list), False: defaultdict(list)}
    _namecount = defaultdict(int)
    for _c in conditions.values(): _namecount[(_c.get('name') or '').strip()] += 1
    for cid, c in sorted(conditions.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
        nm = c.get('name') or cid
        cat_name, res_skill = CATEGORY.get(c.get('category'), (str(c.get('category')).capitalize(), None))
        pos = bool(c.get('isPositive'))
        ic = icon(c.get('iconID'), 'conditions')
        S = src.get(cid, [])
        applied = [s for s in S if s['action'] == 'apply']
        removers = [s for s in S if s['action'] == 'remove']
        immun = [s for s in S if s['action'] == 'immunity']
        srt = stat_rows(c)
        P = [X['front'](f"{nm} is a {'beneficial' if pos else 'harmful'} {cat_name.lower()} condition in Andor's Trail: {summary(c)}."
                        + (f" Caused by: {', '.join(dict.fromkeys({'item': 'items', 'monster': 'enemies', 'dialogue': 'dialogue and events', 'skill': 'skills'}[s['kind']] for s in applied))}." if applied else '')),
             f"# {X['img'](ic)} {nm}\n\n",
             f"*{'Beneficial' if pos else 'Harmful'} {cat_name.lower()} condition.*\n\n"]
        info = [('Type', 'Beneficial' if pos else 'Harmful'), ('Category', f"[{cat_name}](index.md#categories-and-resistance)"),
                ('Affects', affects(cid)), ('Stacking', 'Yes' if c.get('isStacking') else 'No'),
                ('Resisted by', (f"[{skills[res_skill]['name']}](../skills/{res_skill}.md)" if res_skill and res_skill in skills else 'No resistance skill')),
                ('Condition ID', f"`{cid}`")]
        P.append(X['infobox'](info, '../../' + ic if ic else None))
        if c.get('description'): P.append(f"> {c['description']}\n\n")
        _same = [x for x, cc in conditions.items() if x != cid and (cc.get('name') or '').strip() == nm.strip()]
        if _same: P.append(f"!!! note \"Other conditions named {md_esc(nm)}\"\n    The game data defines {len(_same) + 1} separate conditions with this name, each with its own effects: "
                           + ', '.join(f"[`{x}`]({x}.md)" for x in _same) + ".\n\n")
        P.append("## Effects\n\n")
        if srt:
            P.append("| Effect | Per magnitude level |\n|---|---|\n" + ''.join(f"| {a} | {b} |\n" for a, b in srt) + "\n")
            P.append("Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.\n\n")
        else:
            P.append("No direct stat effect. It matters elsewhere, e.g. dialogue that checks for it (see below).\n\n")
        P.append("**Stacking:** " + ("Yes (same duration → magnitudes add up)." if c.get('isStacking') else "No (only a stronger or longer application replaces it).") + "\n\n")
        P.append(verified("condition data and game code (`ActorStatsController.java`)", VERSION))

        # sources
        def src_table(lst, who):
            groups = defaultdict(lambda: [])
            for s in lst:
                if s['who'] != who: continue
                groups[s['kind']].append(s)
            out = []
            if groups.get('item'):
                r = sorted(dict.fromkeys(f"| {ilink(s['id'])} | {s['how'].capitalize()} | {s['mag']} | {dur_text(s['dur'], s['equip'])} | {chance_of(s)} |\n" for s in groups['item']), key=str.lower)
                out.append("**Items**\n\n| Item | When | Magnitude | Duration | Chance |\n|---|---|---|---|---|\n" + ''.join(r[:60]) +
                           (f"\n*{len(r) - 60} further items are not listed.*\n" if len(r) > 60 else '') + "\n")
            if groups.get('monster'):
                seen, r = set(), []
                for s in sorted(groups['monster'], key=lambda s: ((monsters[s['id']].get('name') or s['id']).lower(), s['id'])):
                    key = (canon_of.get(s['id'], s['id']), s['how'], s['mag'], s['dur'], s['chance'])
                    if key in seen: continue
                    seen.add(key)
                    r.append(f"| {mlink(s['id'])} | {s['how'].capitalize()} | {s['mag']} | {dur_text(s['dur'])} | {chance_of(s)} | {where(s['id']) or '–'} |\n")
                out.append("**Enemies**\n\n| Enemy | When | Magnitude | Duration | Chance | Found in |\n|---|---|---|---|---|---|\n" + ''.join(r[:80]) +
                           (f"\n*{len(r) - 80} further enemies are not listed.*\n" if len(r) > 80 else '') + "\n")
            if groups.get('dialogue'):
                r = []
                for s in groups['dialogue']:
                    qs = node_quests(s['id'])
                    r.append(f"| {speakers_md(s['id'])} | {QG.qlink(qs[0][0], qs[0][1]) if qs else '–'} | {dur_text(s['dur'])} |\n")
                r = list(dict.fromkeys(r))
                out.append("**Dialogue and scripted events**\n\n| From | Quest | Duration |\n|---|---|---|\n" + ''.join(r[:40]) +
                           (f"\n*{len(r) - 40} further events are not listed.*\n" if len(r) > 40 else '') + "\n")
            if groups.get('skill'):
                out.append("**Skills**\n\n| Skill | When | Magnitude | Duration | Chance |\n|---|---|---|---|---|\n" + ''.join(
                    f"| [{skills[s['id']]['name']}](../skills/{s['id']}.md) | {s['how'].capitalize()} | {s['mag']} | {dur_text(s['dur'])} | {s['chance']} |\n"
                    for s in groups['skill']) + "\n")
            return ''.join(out)
        yours, theirs = src_table(applied, 'you'), src_table(applied, 'enemy')
        P.append("## How you get it\n\n" + (yours or "Nothing in the game data applies this condition to you.\n\n"))
        if theirs: P.append("## Applied to enemies\n\n" + theirs)
        if applied: P.append(verified("item, monster, dialogue and skill data", VERSION))

        # removal & protection
        R = []
        if any(s['who'] == 'you' and s['kind'] != 'skill' and s['chance'] is not None and X['chance_pct'](s['chance']) < 100 for s in applied):
            caveat = (" Yes, it also lowers your chance of getting this *beneficial* one." if pos else '')
            if res_skill and res_skill in skills:
                R.append(f"- **Resistance:** [{skills[res_skill]['name']}](../skills/{res_skill}.md), "
                         f"−{consts.get('PER_SKILLPOINT_INCREASE_RESISTANCE_CHANCE_PERCENT', 10)}% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted." + caveat)
            else:
                R.append("- **Resistance:** none; spiritual conditions ignore resistance skills.")
            if 'shadowBless' in skills:
                R.append(f"- **[{skills['shadowBless']['name']}](../skills/shadowBless.md)** −{consts.get('PER_SKILLPOINT_INCREASE_RESISTANCE_SHADOW_BLESS', 5)}% of the chance for any condition.")
            if cid == 'spore_poison' and 'sporeImmunity' in skills:
                R.append(f"- **[{skills['sporeImmunity']['name']}](../skills/sporeImmunity.md)** prevents this condition entirely (unless the chance is 100%).")
        if not pos and c.get('category') != 'spiritual' and 'rejuvenation' in skills and any(s['dur'] != FOREVER for s in applied if s['who'] == 'you'):
            R.append(f"- **[{skills['rejuvenation']['name']}](../skills/rejuvenation.md):** each round, a {consts.get('PER_SKILLPOINT_INCREASE_REJUVENATION_CHANCE', 20)}% chance per round to weaken one timed harmful condition by 1.")
        for s in removers:
            if s['kind'] == 'item': R.append(f"- **Removed by** {ilink(s['id'])} ({s['how']}).")
            elif s['kind'] == 'dialogue':
                qs = node_quests(s['id'])
                R.append(f"- **Removed by** {speakers_md(s['id'])}" + (f" during {QG.qlink(qs[0][0], qs[0][1])}" if qs else '') + ".")
        for s in immun:
            d = 'while equipped' if s['equip'] else dur_text(s['dur']).lower()
            if s['kind'] == 'item': R.append(f"- **Immunity** from {ilink(s['id'])} ({s['how']}; {d}).")
            elif s['kind'] == 'monster': R.append(f"- **Immunity** for {mlink(s['id'])} ({s['how']}; {d}).")
            else: R.append(f"- **Immunity** from {speakers_md(s['id'])} ({d}).")
        rt = rest_text(cid)
        if rt: R.append("- **Duration and rest:** " + '; '.join(rt) + ".")
        P.append("## Removal and protection\n\n" + ('\n'.join(dict.fromkeys(R)) if R else "No item, skill or event in the game data removes or prevents this condition.") + "\n\n")

        if checks.get(cid):
            r = []
            for pc, neg, nxt in checks[cid]:
                qs = node_quests(nxt) or node_quests(pc)
                r.append(f"- {speakers_md(pc)}" + (f" ({QG.qlink(qs[0][0], qs[0][1])})" if qs else '') +
                         f" checks whether you {'do not ' if neg else ''}have this condition.\n")
            P.append("## Checked in dialogue\n\n" + ''.join(list(dict.fromkeys(r))[:20]) + "\n")

        P.append(notes('conditions', cid, nm))
        tech = [('Condition ID', f"`{cid}`"), ('Category (internal)', f"`{c.get('category')}`"), ('Icon', f"`{c.get('iconID', '–')}`"),
                ('Defined in', f"`res/raw/{file_of.get(('actorconditions', cid), '?')}`")]
        P.append('\n??? info "Technical information"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {a} | {b} |\n" for a, b in tech) +
                 "\n    Raw data:\n\n" + X['raw_json'](c) + '\n')
        P.append(f"\n<small>Data from v{VERSION}</small>\n")
        write(f'conditions/{cid}.md', ''.join(P))
        kinds = defaultdict(int)
        for s in applied:
            kinds[s['kind']] += 1
        how = ', '.join(f"{n} {k + ('ies' if n != 1 else 'y') if k == 'enem' else k + ('s' if n != 1 else '')}" for k, n in (('item', len({s['id'] for s in applied if s['kind'] == 'item'})),
                                                                     ('enem', len({canon_of.get(s['id'], s['id']) for s in applied if s['kind'] == 'monster'})),
                                                                     ('event', len({s['id'] for s in applied if s['kind'] == 'dialogue'})),
                                                                     ('skill', len({s['id'] for s in applied if s['kind'] == 'skill'}))) if n)
        rows[pos][cat_name].append(f"| {X['img'](ic)} | [{md_esc(nm)}]({cid}.md){f' <small>(`{cid}`)</small>' if _namecount[nm.strip()] > 1 else ''} | {md_esc(summary(c))} | {how or '–'} |\n")

    # ---- overview
    res = lambda key: (f"[{skills[key]['name']}](../skills/{key}.md)" if key and key in skills else '–')
    L = [X['front'](f"All {len(conditions)} conditions in Andor's Trail v{VERSION} (poison, bleeding, blessings, food effects and more): what each does, what causes it, and how to remove or resist it."),
         f"# Conditions\n\nPoison, bleeding, blessings, food effects: all {len(conditions)} conditions in v{VERSION}, what they do, what causes them and how to get rid of them. "
         "~~Yes, food poisoning from raw meat is a real risk.~~\n\n"
         "**Jump to:** [How conditions work](#how-conditions-work) · [Harmful conditions](#harmful-conditions) · [Beneficial conditions](#beneficial-conditions)\n\n",
         "## How conditions work\n\n"]
    L.append('\n<span id="categories-and-resistance"></span>\n'); L.append(X['section']('Categories and resistance', "Each category has its own resistance skill (spiritual has none).\n\n"
             "| Category | Resistance skill | Count |\n|---|---|---|\n" + ''.join(
                 f"| {CATEGORY[k][0]} | {res(CATEGORY[k][1]) if CATEGORY[k][1] else 'None'} | {sum(1 for c in conditions.values() if c.get('category') == k)} |\n" for k in CATEGORY) +
             f"\nEach resistance level cuts the chance by {consts.get('PER_SKILLPOINT_INCREASE_RESISTANCE_CHANCE_PERCENT', 10)}% *of its value*: a 30% poison chance becomes 27% at level 1 "
             f"and 9% at the max ({consts.get('MAX_LEVEL_RESISTANCE', 7)}). 100% chances can't be resisted. Resistance also lowers your chance of getting *beneficial* conditions "
             f"of that category ~~thanks, I hate it~~. {res('shadowBless')}: −{consts.get('PER_SKILLPOINT_INCREASE_RESISTANCE_SHADOW_BLESS', 5)}% of the value for every category."))
    L.append('\n<span id="magnitude-duration-and-timing"></span>\n'); L.append(X['section']('Magnitude, duration and timing',
             "- **Magnitude** multiplies every effect (magnitude 3 poison = 3× the damage).\n"
             "- **Duration** is in rounds: one combat turn, or 6 seconds outside combat.\n"
             "- *Every 25 seconds* effects only tick outside combat.\n"
             "- **Permanent** = from equipment or story events (duration 999); duration 998 = until you rest.\n"))
    L.append('\n<span id="stacking"></span>\n'); L.append(X['section']('Stacking',
             "- **Stacking:** same duration → magnitudes add up; different duration → separate instance.\n"
             "- **Non-stacking:** only a higher magnitude (or same magnitude, longer duration) replaces the current one.\n"))
    L.append('\n<span id="removal-and-immunity"></span>\n'); L.append(X['section']('Removal and immunity',
             "- **Resting** clears all timed conditions. Permanent ones stay.\n"
             "- Some items and events **remove** a condition outright; others give **immunity** (while equipped, or for some rounds).\n"
             f"- {res('rejuvenation')}: each round, a chance to weaken one timed harmful condition by 1 (not spiritual ones).\n"))
    L.append(verified("game code (`ActorStatsController.java`, `SkillController.java`, `GameRoundController.java`, `Constants.java`)", VERSION))
    hdr = "| | Condition | Effect per magnitude level | Applied by |\n|---|---|---|---|\n"
    for pos, title in ((False, 'Harmful conditions'), (True, 'Beneficial conditions')):
        L.append(f"## {title}\n\n")
        for k in CATEGORY:
            cn = CATEGORY[k][0]
            if rows[pos].get(cn): L.append(f"### {cn}\n\n" + hdr + ''.join(rows[pos][cn]) + "\n")
    write('conditions/index.md', ''.join(L))
    return src
