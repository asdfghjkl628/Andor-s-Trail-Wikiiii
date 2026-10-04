"""Quests as a dependency graph, plus NPC dialogue (imported by build.py).

How the game runs a conversation (controller/ConversationController.java):
  * a phrase WITH a message shows it; the player then picks one of the replies whose requirements are met
    ("N" = the Next button);
  * a phrase WITHOUT a message is a silent router: the first reply (in order) whose requirements are met is taken;
  * special targets: X = conversation ends, S = shop opens, F = fight starts, R = the NPC leaves.
Rewards on a phrase are applied when it is reached.
"""
import html, os, re
from collections import defaultdict, deque

SPECIAL = {'X': 'conversation ends', 'S': 'shop opens', 'F': 'fight starts', 'R': 'NPC leaves'}
MAX_DIALOGUE_NODES = 150


def _short(t, n=160):
    t = ' '.join(html.unescape(str(t or '')).split())
    t = re.sub(r'\{(\d+)\}', lambda m: f"{int(m.group(1)):,}", t)
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '…'


def _md(t): return str(t).replace('|', '\\|').replace('\n', ' ')


class QuestGraph:
    def __init__(self, ctx):
        self.c = ctx
        self.convs, self.quests, self.monsters = ctx['conversations'], ctx['quests'], ctx['monsters']
        self.items, self.droplists, self.skills = ctx['items'], ctx['droplists'], ctx['skills']
        self.spawn_maps, self.script_maps, self.map_notes = ctx['spawn_maps'], ctx['script_maps'], ctx['map_notes']
        self._roots()
        self._reach()
        self._triggers()
        self._dependencies()

    # ------------------------------------------------------------ graph construction
    def _roots(self):
        """Every conversation starts from an NPC (monster phraseID) or a map script object."""
        self.roots = defaultdict(list)
        for mid, m in self.monsters.items():
            if m.get('phraseID') in self.convs: self.roots[m['phraseID']].append(('npc', mid))
        for ph, places in self.script_maps.items():
            if ph in self.convs:
                for mp, how in sorted(places): self.roots[ph].append(('map', (mp, how)))

    def _reach(self):
        """BFS from each root: shortest dialogue path to every reachable phrase."""
        self.paths = defaultdict(dict)   # phrase -> {root phrase: prev-map}
        self.root_nodes = {}            # root phrase -> every phrase reachable from it
        for rp in self.roots:
            prev, q = {rp: None}, deque([rp])
            while q:
                x = q.popleft()
                for i, r in enumerate(self.convs[x].get('replies') or []):
                    n = r.get('nextPhraseID')
                    if n in self.convs and n not in prev:
                        prev[n] = (x, i); q.append(n)
            for node in prev: self.paths[node][rp] = prev
            self.root_nodes[rp] = set(prev)

    def path_edges(self, node, rp):
        prev, out, x = self.paths[node][rp], [], node
        while prev.get(x):
            par, i = prev[x]; out.append((par, i, self.convs[par]['replies'][i])); x = par
        return list(reversed(out))

    def speakers(self, rp):
        return self.roots.get(rp, [])

    def _triggers(self):
        """(quest, stage) -> list of trigger records; also removals."""
        self.triggers, self.removals = defaultdict(list), defaultdict(list)
        for cid, c in self.convs.items():
            for r in c.get('rewards') or []:
                if r.get('rewardType') == 'questProgress' and r.get('rewardID') in self.quests:
                    self.triggers[(r['rewardID'], r.get('value', 0))].append(cid)
                elif r.get('rewardType') == 'removeQuestProgress' and r.get('rewardID') in self.quests:
                    self.removals[(r['rewardID'], r.get('value', 0))].append(cid)

    def routes(self, cid):
        """How a phrase is reached: one record per starting point (NPC/map), with the player's choice and all path conditions."""
        out = []
        for rp, _ in sorted(self.paths.get(cid, {}).items(), key=lambda kv: kv[0]):
            edges = self.path_edges(cid, rp)
            reqs, choice = [], None
            for par, i, rep in edges:
                reqs.extend(rep.get('requires') or [])
                t = (rep.get('text') or '').strip()
                if t and t not in ('N', '.', '*'): choice = t
            out.append(dict(root=rp, speakers=self.speakers(rp), reqs=reqs, choice=choice, steps=len(edges)))
        return out

    def _dependencies(self):
        """Cross-quest edges from the conditions on the dialogue path that sets each stage."""
        self.needs = defaultdict(set)     # Q -> {(P, t, Qstage)}           Q's stage needs P at t
        self.blocked = defaultdict(set)   # Q -> {(P, t, Qstage)}           Q's stage needs P NOT at t
        self.unlocks = defaultdict(set)   # P -> {(Q, Qstage, t)}           reciprocal of needs
        self.blocks = defaultdict(set)    # P -> {(Q, Qstage, t)}           reciprocal of blocked
        self.internal = defaultdict(set)  # (Q, s) -> {t}                   same-quest ordering
        self.items_needed = defaultdict(set)
        for (q, s), cids in self.triggers.items():
            for cid in cids:
                for rt in self.routes(cid):
                    for r in rt['reqs']:
                        t, p, v, neg = r.get('requireType'), r.get('requireID'), r.get('value', 0), bool(r.get('negate'))
                        if t in ('questProgress', 'questLatestProgress') and p in self.quests:
                            if p == q:
                                if not neg and v != s: self.internal[(q, s)].add(v)
                            elif neg:
                                self.blocked[q].add((p, v, s)); self.blocks[p].add((q, s, v))
                            else:
                                self.needs[q].add((p, v, s)); self.unlocks[p].add((q, s, v))
                        elif t in ('inventoryRemove', 'inventoryKeep', 'wear') and p and not neg:
                            self.items_needed[(q, s)].add((t, p, v))

    # ------------------------------------------------------------ text helpers
    def qlink(self, q, stage=None, pre='../quests/'):
        nm = self.quests.get(q, {}).get('name', q)
        if not self.quests.get(q, {}).get('showInLog', 0): nm = f"{nm} (hidden flag)"
        return f"[{_md(nm)}]({pre}{q}.md" + (f"#stage-{stage}" if stage is not None else '') + ")"

    def mlink(self, mid, pre='../monsters/'):
        return f"[{_md(self.monsters.get(mid, {}).get('name', mid))}]({pre}{mid}.md)"

    def ilink(self, iid, pre='../items/'):
        return f"[{_md(self.items.get(iid, {}).get('name', iid))}]({pre}{iid}.md)"

    def who(self, speakers, pre='../'):
        parts = []
        for kind, x in speakers[:3]:
            if kind == 'npc':
                where = sorted(self.spawn_maps.get(x, ()))[:1]
                parts.append(self.mlink(x, pre + 'monsters/') + (f" ([{where[0]}]({pre}maps/{where[0]}.md))" if where else ''))
            else:
                mp, how = x
                verb = {'script': 'stepping on a trigger', 'key': 'walking into a blocked passage', 'sign': 'reading a sign'}.get(how, 'an event')
                parts.append(f"{verb} on [{mp}]({pre}maps/{mp}.md)")
        if len(speakers) > 3: parts.append(f"+{len(speakers) - 3} more")
        return ', '.join(parts) or 'an unknown source'

    def req(self, r, pre='../'):
        t, rid, val, neg = r.get('requireType'), r.get('requireID'), r.get('value', 0), bool(r.get('negate'))
        no = 'NOT ' if neg else ''
        if rid == 'gold' and t in ('inventoryRemove', 'inventoryKeep'):
            return f"{no}{'pay' if t == 'inventoryRemove' else 'have'} {val:,} gold"
        if t == 'questProgress': return f"{no}reached stage {val} of {self.qlink(rid, val, pre + 'quests/')}"
        if t == 'questLatestProgress': return f"{no}latest stage of {self.qlink(rid, val, pre + 'quests/')} is {val}"
        if t == 'inventoryRemove': return f"{no}hand over {val}× {self.ilink(rid, pre + 'items/')}"
        if t == 'inventoryKeep': return f"{no}carry {val}× {self.ilink(rid, pre + 'items/')}"
        if t == 'wear': return f"{no}wearing {self.ilink(rid, pre + 'items/')}"
        if t == 'wearRemove': return f"{no}wearing (and give up) {self.ilink(rid, pre + 'items/')}"
        if t == 'usedItem': return f"{no}used {val}× {self.ilink(rid, pre + 'items/')}"
        if t == 'killedMonster': return f"{no}killed {val}× {self.mlink(rid, pre + 'monsters/')}"
        if t == 'random': return f"random chance ({rid or val}%)"
        if t in ('factionScore', 'factionScoreEquals'): return f"{no}faction “{rid}” {'=' if t.endswith('Equals') else '≥'} {val}"
        if t == 'timerElapsed': return f"{no}{val} rounds passed since timer “{rid}”"
        if t == 'hasActorCondition': return f"{no}affected by {rid}"
        if t == 'skillLevel': return f"{no}{self.skills.get(rid, {}).get('name', rid)} level {val}+"
        if t == 'consumedBonemeals': return f"{no}eaten {val}+ bonemeals"
        return f"{no}{t} {rid or ''} {val or ''}".strip()

    def rewards(self, c, pre='../', skip_quest=None):
        out = []
        for r in c.get('rewards') or []:
            t, rid, val = r.get('rewardType'), r.get('rewardID'), r.get('value')
            if t == 'questProgress' and rid != skip_quest: out.append(f"sets stage {val} of {self.qlink(rid, val, pre + 'quests/')}")
            elif t == 'removeQuestProgress': out.append(f"clears stage {val} of {self.qlink(rid, val, pre + 'quests/')}")
            elif t == 'giveItem': out.append(f"gives {val or 1}× {self.ilink(rid, pre + 'items/')}")
            elif t == 'dropList':
                its = [e['itemID'] for e in self.droplists.get(rid, {}).get('items', [])]
                out.append("gives " + (', '.join(self.ilink(i, pre + 'items/') for i in its[:6]) if its else f"loot table `{rid}`"))
            elif t == 'skillIncrease': out.append(f"+{val or 1} [{self.skills.get(rid, {}).get('name', rid)}]({pre}skills/{rid}.md)")
            elif t in ('alignmentChange',): out.append(f"faction “{rid}” {'+' if (val or 0) >= 0 else ''}{val}")
            elif t == 'alignmentSet': out.append(f"faction “{rid}” set to {val}")
            elif t == 'actorCondition': out.append(f"applies condition {rid}")
            elif t == 'mapchange': out.append(f"moves you to [{r.get('mapName') or rid}]({pre}maps/{r.get('mapName') or rid}.md)")
            elif t == 'spawnAll': out.append(f"spawns monsters on {r.get('mapName') or 'the map'}")
            elif t in ('removeSpawnArea', 'deactivateSpawnArea'): out.append(f"removes monsters from {r.get('mapName') or 'the map'}")
            elif t in ('activateMapObjectGroup', 'deactivateMapObjectGroup'): out.append(f"changes map {r.get('mapName') or ''}".strip())
            elif t == 'createTimer': out.append(f"starts timer “{rid}”")
        return out


# ---------------------------------------------------------------- quest pages
def write_quest_pages(G, write, VERSION, notes, history=None, comp_text=None, verified=lambda w, v: ''):
    L = ["# Quests\n\nEvery quest that shows up in your journal, plus, at the bottom, the hidden story flags the game uses to keep track of you without telling you. "
         "Each quest page shows what starts it, what each stage needs, what it unlocks and what it locks you out of.\n\n"
         "| Quest | Stages | Starts with |\n|---|---|---|\n"]
    hidden_rows = []
    for qid, q in sorted(G.quests.items(), key=lambda kv: kv[1].get('name', kv[0]).lower()):
        visible = bool(q.get('showInLog', 0))
        stages = q.get('stages', [])
        st_vals = sorted({s.get('progress') for s in stages} | {s for (qq, s) in G.triggers if qq == qid})
        first = min((s for (qq, s) in G.triggers if qq == qid), default=None)
        starters = []
        if first is not None:
            for cid in G.triggers[(qid, first)]:
                for rt in G.routes(cid): starters.extend(rt['speakers'])
        npcs = sorted({x for (qq, s), cids in G.triggers.items() if qq == qid for cid in cids
                       for rt in G.routes(cid) for k, x in rt['speakers'] if k == 'npc'}, key=lambda m: G.monsters[m].get('name', m))
        locs = sorted({mp for n in npcs for mp in G.spawn_maps.get(n, ())})
        xp = sum(s.get('rewardExperience', 0) for s in stages)
        done = [s.get('progress') for s in stages if s.get('finishesQuest')]
        related = {p for p, _, _ in G.needs[qid] | G.blocked[qid]} | {x for x, _, _ in G.unlocks[qid] | G.blocks[qid]}
        mutual = {p for p, _, _ in G.blocked[qid]} & {x for x, _, _ in G.blocks[qid]}

        P = [f"# {q.get('name', qid)}\n\n"]
        if not visible:
            P.append("!!! info \"Hidden story flag\"\n    An internal quest the game uses to track your progress behind the scenes. "
                     "It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.\n\n")
        info = [('Quest ID', f"`{qid}`"), ('In journal', 'Yes' if visible else 'No (hidden flag)'),
                ('Stages', f"{len(stages)}" + (f" (completes at {', '.join(map(str, done))})" if done else '')),
                ('Started by', G.who(starters[:2]) if starters else None),
                ('NPCs involved', ', '.join(G.mlink(n) for n in npcs[:6]) + (f" +{len(npcs) - 6}" if len(npcs) > 6 else '') if npcs else None),
                ('Locations', ', '.join(f"[{m}](../maps/{m}.md)" for m in locs[:4]) if locs else None),
                ('Total XP', f"{xp:,}" if xp else None), ('Related quests', str(len(related)) if related else None)]
        P.append('<div class="infobox" markdown>\n\n| | |\n|---|---|\n' + ''.join(f"| **{k}** | {v} |\n" for k, v in info if v) + '\n</div>\n\n')
        if comp_text and comp_text(qid):
            P.append(f"!!! history \"Version note\"\n    {comp_text(qid)}\n\n")
        intro = next((s.get('logText') for s in sorted(stages, key=lambda s: s.get('progress', 0)) if s.get('logText')), '')
        if intro: P.append(f"## Overview\n\n> {_short(intro, 400)}\n\n")

        # ---- prerequisites to start: every condition on each route to the first stage
        if first is not None:
            pre_routes = []
            for cid in G.triggers[(qid, first)]:
                for rt in G.routes(cid):
                    conds = list(dict.fromkeys(G.req(r) for r in rt['reqs']))
                    pre_routes.append((G.who(rt['speakers'][:1]), conds))
            uniq = list(dict.fromkeys((w, tuple(c)) for w, c in pre_routes))
            P.append("## Prerequisites to start\n\n")
            if all(not c for _, c in uniq):
                P.append(f"None: talk to {uniq[0][0]} to begin.\n\n" if uniq else "None found.\n\n")
            else:
                for i, (w, c) in enumerate(uniq[:6], 1):
                    P.append((f"**Route {i}** ({w}):\n\n" if len(uniq) > 1 else f"Start with {w}. Required:\n\n") +
                             (''.join(f"- {x}\n" for x in c) if c else "- nothing\n") + "\n")

        if first is not None: P.append(verified("quest and dialogue data", VERSION))

        # ---- dependencies (quest logic)
        P.append("## Dependencies\n\n*Quest logic, read from the dialogue conditions.*\n\n")
        def grouped(edges):
            g = defaultdict(set)
            for a, b, c in edges: g[(a, b)].add(c)
            return sorted(g.items())
        def st(xs): return ('stage ' if len(xs) == 1 else 'stages ') + ', '.join(map(str, sorted(xs)))
        rows = []
        for (p, t), ss in grouped(G.needs[qid]): rows.append(('Requires', G.qlink(p, t, ''), f"stage {t} reached, for {st(ss)} here"))
        for (p, t), ss in grouped(G.blocked[qid]): rows.append(('Mutually exclusive' if p in mutual else 'Blocked by', G.qlink(p, t, ''), f"stage {t} must NOT be reached, for {st(ss)} here"))
        for (x, s2), ts in grouped(G.unlocks[qid]): rows.append(('Unlocks', G.qlink(x, s2, ''), f"stage {s2} there needs {st(ts)} here"))
        for (x, s2), ts in grouped(G.blocks[qid]):
            if x not in mutual: rows.append(('Blocks', G.qlink(x, s2, ''), f"reaching {st(ts)} here closes stage {s2} there"))
        P.append(("| Relationship | Quest | Detail |\n|---|---|---|\n" + ''.join(f"| {a} | {b} | {c} |\n" for a, b, c in rows[:60])
                  + (f"\n*…and {len(rows) - 60} more.*\n" if len(rows) > 60 else '')) if rows else
                 "No links to other quests were found in the dialogue conditions.\n")
        P.append("\n")

        # ---- stages
        untraced = False
        P.append("## Stages\n\n| Stage | Journal entry | Triggered by | Needs | Rewards |\n|---|---|---|---|---|\n")
        by_val = {s.get('progress'): s for s in stages}
        for v in st_vals:
            s = by_val.get(v, {})
            trig, needs, rew = [], set(), []
            for cid in G.triggers.get((qid, v), []):
                for rt in G.routes(cid): trig.append(G.who(rt['speakers'][:1]))
                rew.extend(G.rewards(G.convs[cid], skip_quest=qid))
            for t in sorted(G.internal.get((qid, v), ())): needs.add(f"stage {t}")
            for t, p, val in sorted(G.items_needed.get((qid, v), ())): needs.add(G.req({'requireType': t, 'requireID': p, 'value': val}))
            if s.get('rewardExperience'): rew.insert(0, f"{s['rewardExperience']:,} XP")
            mapn = sorted(G.map_notes.get(qid, {}).get(v, ()))
            jt = _md(s.get('logText', '')) + (' **(completes quest)**' if s.get('finishesQuest') else '') + ''.join(f"<br><span class=\"qnote\">{n}</span>" for n in mapn)
            trig_u = list(dict.fromkeys(trig))
            if not trig_u:
                cids = G.triggers.get((qid, v), [])
                trig_u = [f"dialogue `{cids[0]}`, which nothing in the data starts directly"] if cids else \
                         ["*no trigger in the game data or code* <sup>[?](#untraced)</sup>"]
                untraced = True
            P.append(f"| <span id=\"stage-{v}\"></span>{v} | {jt} | {'<br>'.join(trig_u[:3]) + (f'<br>+{len(trig_u) - 3} more' if len(trig_u) > 3 else '')} "
                     f"| {', '.join(sorted(needs)) or '–'} | {'<br>'.join(dict.fromkeys(rew)) or '–'} |\n")
        if untraced:
            P.append(f"\n<span id=\"untraced\"></span>*No trigger*: as of v{VERSION}, nothing in the game's dialogue, maps or code sets this stage. "
                     "It may be unused or unfinished content, or set in a way this wiki can't trace yet. "
                     "That doesn't make it a secret: treat anything you hear about it as speculation.\n")
        P.append(verified("quest, dialogue and map data", VERSION))

        # ---- every dialogue route to every stage (preserves alternative paths)
        route_md = []
        for v in st_vals:
            cids = G.triggers.get((qid, v), [])
            if not cids: continue
            lines, k = [], 0
            for cid in cids:
                c = G.convs[cid]
                for rt in G.routes(cid):
                    k += 1
                    who = G.who(rt['speakers'][:1])
                    act = f"choose “{_short(rt['choice'], 110)}”" if rt['choice'] else "the conversation leads here automatically"
                    cond = ('; '.join(dict.fromkeys(G.req(r) for r in rt['reqs']))) if rt['reqs'] else ''
                    extra = G.rewards(c, skip_quest=qid)
                    lines.append(f"    {k}. {'Talk to ' if rt['speakers'] and rt['speakers'][0][0] == 'npc' else ''}{who} → {act}" + (f" — **conditions:** {cond}" if cond else '') +
                                 f" → **stage {v}**" + (f"; also {', '.join(extra)}" if extra else '') +
                                 (f". NPC: “{_short(c['message'], 120)}”" if c.get('message') else '') + "\n")
            if lines:
                route_md.append(f"???+ note \"Stage {v}: {len(lines)} route{'s' if len(lines) != 1 else ''}\"\n\n" + ''.join(lines[:25])
                                + (f"    *…and {len(lines) - 25} more routes.*\n" if len(lines) > 25 else '') + "\n")
        if route_md:
            P.append("## How each stage is reached\n\n*Every dialogue route found in the game data, including alternatives that end up in the same place. "
                     "\"Conditions\" are everything checked along that dialogue path.*\n\n" + ''.join(route_md))

        if route_md: P.append(verified("dialogue data", VERSION))
        removed = [(v, cid) for (qq, v), cids in G.removals.items() if qq == qid for cid in cids]
        if history:
            dlg = {c for (qq, v), cids in list(G.triggers.items()) + list(G.removals.items()) if qq == qid for c in cids}
            lead = comp_text(qid) if comp_text else ''
            P.append(history('quests', qid, dlg, (f"**Completability:** {lead}" if lead else '')))
        P.append(notes('quests', qid, q.get('name', qid)))
        tech = [('Quest ID', f"`{qid}`"), ('showInLog', q.get('showInLog', 0)),
                ('Stage IDs', ', '.join(map(str, st_vals)) or '–'),
                ('Dialogue nodes setting stages', ', '.join(f"{v}: `{c}`" for (qq, v), cids in sorted(G.triggers.items()) if qq == qid for c in cids[:3]) or '–'),
                ('Dialogue nodes clearing stages', ', '.join(f"{v}: `{c}`" for v, c in removed[:10]) or '–'),
                ('Source files', '`res/raw/questlist*.json`, `res/raw/conversationlist*.json`')]
        P.append('\n??? info "Technical information"\n\n    | | |\n    |---|---|\n' + ''.join(f"    | {a} | {b} |\n" for a, b in tech) + '\n')
        P.append(f"\n<small>Data from v{VERSION}</small>\n")
        write(f'quests/{qid}.md', ''.join(P))
        who0 = G.who(starters[:1]) if starters else '–'
        row = f"| [{_md(q.get('name', qid))}]({qid}.md) | {len(stages)} | {who0} |\n"
        (L if visible else hidden_rows).append(row)
    if hidden_rows:
        L.append("\n## Hidden story flags\n\nInternal progress trackers that never appear in your journal, but quietly decide which doors open "
                 "and which events fire. The names were not written with human readers in mind.\n\n| Flag | Stages | Set by |\n|---|---|---|\n" + ''.join(hidden_rows))
    write('quests/index.md', ''.join(L).replace('](../monsters/', '](../monsters/'))


# ---------------------------------------------------------------- NPC dialogue section (appended to monster pages)
def npc_section(G, mid, notes, history=None):
    m = G.monsters[mid]
    rp = m.get('phraseID')
    if rp not in G.convs: return ''
    out = []
    quests_here = sorted({q for (q, s), cids in G.triggers.items() for cid in cids if rp in G.paths.get(cid, {})},
                         key=lambda q: G.quests[q].get('name', q))
    vis = [q for q in quests_here if G.quests[q].get('showInLog', 0)]
    if quests_here:
        out.append("## Quests\n\n" + ''.join(f"- {G.qlink(q)}: stages " + ', '.join(
            str(s) for (qq, s), cids in sorted(G.triggers.items()) if qq == q and any(rp in G.paths.get(c, {}) for c in cids)) + "\n"
            for q in (vis + [q for q in quests_here if q not in vis])[:30]) + "\n")
    # dialogue: breadth-first from the NPC's first phrase, each phrase once, with anchors
    order, seen, dq = [], {rp}, deque([rp])
    while dq and len(order) < MAX_DIALOGUE_NODES:
        x = dq.popleft(); order.append(x)
        for r in G.convs[x].get('replies') or []:
            n = r.get('nextPhraseID')
            if n in G.convs and n not in seen: seen.add(n); dq.append(n)
    shown = set(order)
    D = []
    for x in order:
        c = G.convs[x]
        rw = G.rewards(c)
        head = f"<span id=\"d-{x}\"></span>**`{x}`** "
        if c.get('message'): head += f"{_md(m.get('name', mid)) if not c.get('switchToNPC') else G.mlink(c['switchToNPC'])}: “{_short(c['message'], 240)}”"
        else: head += "*(silent check: the first matching branch below is taken)*"
        if rw: head += f" — **effects:** {', '.join(rw)}"
        D.append("    " + head + "\n\n")
        for i, r in enumerate(c.get('replies') or [], 1):
            n, t = r.get('nextPhraseID', ''), (r.get('text') or '').strip()
            label = ('Next' if t == 'N' else f"“{_short(t, 120)}”") if t else f"branch {i}"
            cond = '; '.join(G.req(r2) for r2 in r.get('requires') or [])
            tgt = (f"[{n}](#d-{n})" if n in shown else (f"`{n}`" if n in G.convs else f"*{SPECIAL.get(n, n or 'ends')}*"))
            D.append(f"    - {label}" + (f" *(if {cond})*" if cond else '') + f" → {tgt}\n")
        D.append("\n")
    total = len([1 for _ in seen]) if len(order) < MAX_DIALOGUE_NODES else None
    out.append(f"??? quote \"Dialogue ({len(order)} lines{'+' if total is None else ''})\"\n\n"
               "    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*\n\n" + ''.join(D) +
               ("    *Dialogue continues beyond this point (truncated).*\n" if total is None else '') + "\n")
    if history: out.append(history('monsters', mid, G.root_nodes.get(rp, ()), ''))
    out.append(notes('monsters', mid, m.get('name', mid)))
    return ''.join(out)
