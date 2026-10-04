"""Version history for the wiki.

  python tools/history.py <git-clone-of-andors-trail>   # one-off: rebuild data/history.json from every release tag
  (build.py calls update_history() on each new release to append just that release)

A snapshot is the game's data reduced to {kind: {id: canonical JSON}}; history is the diff between
consecutive releases, stored per entity as [version, event, details].
"""
import glob, gzip, json, os, re, subprocess, sys
import xml.etree.ElementTree as ET

KINDS = ('items', 'monsters', 'quests', 'dialogue', 'droplists', 'maps')
FILEKIND = {'itemlist': 'items', 'monsterlist': 'monsters', 'questlist': 'quests',
            'conversationlist': 'dialogue', 'droplists': 'droplists'}
FIRST_TRACKED = '0.7.0'


def vkey(v): return tuple(int(x) for x in re.findall(r'\d+', v))


def _loaded(game_res):
    """{resource kind: [json paths]} honoring loadresources.xml (skips debug/test data)."""
    raw, out = os.path.join(game_res, 'raw'), {}
    lr = os.path.join(game_res, 'values', 'loadresources.xml')
    if os.path.exists(lr):
        for arr in ET.parse(lr).getroot():
            name = (arr.get('name') or '').replace('loadresource_', '')
            name = {'items': 'itemlist', 'monsters': 'monsterlist', 'quests': 'questlist', 'conversationlists': 'conversationlist'}.get(name, name)
            if name in FILEKIND:
                out[name] = [os.path.join(raw, i.text.split('/')[-1] + '.json') for i in arr if i.text]
    for k in FILEKIND:
        if not out.get(k):
            out[k] = [f for f in glob.glob(os.path.join(raw, f'{k}_*.json')) + glob.glob(os.path.join(raw, f'{k}.json')) if 'debug' not in f]
    return out


def snapshot(game_res, tmx_shas=None):
    """Normalize one release. game_res = path to AndorsTrail/res. tmx_shas = {map: git blob sha} (else file hashes)."""
    snap = {k: {} for k in KINDS}
    for k, files in _loaded(game_res).items():
        for f in files:
            if not os.path.exists(f): continue
            try: data = json.load(open(f, encoding='utf-8'))
            except Exception: continue
            for obj in data if isinstance(data, list) else []:
                if not isinstance(obj, dict) or 'id' not in obj: continue
                o = {x: y for x, y in obj.items() if x != 'iconID'}  # sprite moves are noise
                snap[FILEKIND[k]][obj['id']] = json.dumps(o, sort_keys=True, ensure_ascii=False)
    if tmx_shas is None:
        import hashlib
        def blob_sha(path):
            b = open(path, 'rb').read(); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
        tmx_shas = {os.path.basename(p)[:-4]: blob_sha(p) for p in glob.glob(os.path.join(game_res, 'xml', '*.tmx'))}
    lr = os.path.join(game_res, 'values', 'loadresources.xml')
    loaded_maps = set()
    if os.path.exists(lr):
        for arr in ET.parse(lr).getroot():
            if arr.get('name') == 'loadresource_maps':
                loaded_maps = {i.text.split('/')[-1] for i in arr if i.text}
    snap['maps'] = {m: h for m, h in tmx_shas.items() if not loaded_maps or m in loaded_maps}
    return snap


def completable(snap):
    """{quest: None if finishable, else the reason it can't be finished} for journal quests in this release.
    Finishable = some dialogue sets a quest-finishing stage, and every item that route consumes or checks can be
    obtained (appears in a loot table other than the 'undropped' placeholder, or is handed out in dialogue)."""
    convs = {i: json.loads(s) for i, s in snap['dialogue'].items()}
    setters = {}
    for cid, c in convs.items():
        for r in c.get('rewards') or []:
            if r.get('rewardType') == 'questProgress': setters.setdefault((r.get('rewardID'), r.get('value')), []).append(cid)
    incoming = {}
    for cid, c in convs.items():
        for rep in c.get('replies') or []:
            incoming.setdefault(rep.get('nextPhraseID'), []).append(rep.get('requires') or [])
    obtainable = {r.get('rewardID') for c in convs.values() for r in c.get('rewards') or [] if r.get('rewardType') == 'giveItem'}
    for d, s in snap['droplists'].items():
        if 'undropped' in d: continue
        obtainable.update(e.get('itemID') for e in json.loads(s).get('items', []))
    out = {}
    for qid, s in snap['quests'].items():
        q = json.loads(s)
        if not q.get('showInLog', 0): continue
        finals = [st.get('progress') for st in q.get('stages', []) if st.get('finishesQuest')]
        if not finals: out[qid] = 'it had no ending yet'; continue
        reason = None
        for v in finals:
            for cid in setters.get((qid, v), []):
                routes = incoming.get(cid) or [[]]
                for reqs in routes:
                    missing = [r.get('requireID') for r in reqs if r.get('requireType', '').startswith('inventory')
                               and not r.get('negate') and r.get('requireID') not in obtainable and r.get('requireID') != 'gold']
                    if not missing: return_ok = True; break
                    reason = reason or f"its final step needed {', '.join(missing)}, which could not be obtained anywhere"
                else: continue
                break
            else: continue
            break
        else:
            out[qid] = reason or 'nothing in the game set its final stage'
            continue
    return out


def _t(v, n=90):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n - 1] + '…'


def _diff(kind, a, b):
    """Short, human-readable list of what changed in one entity."""
    if kind == 'maps': return ['map layout or objects changed']
    A, B = json.loads(a), json.loads(b)
    if kind == 'quests':
        out = []
        if A.get('name') != B.get('name'): out.append(f"renamed “{_t(A.get('name'))}” → “{_t(B.get('name'))}”")
        if A.get('showInLog') != B.get('showInLog'): out.append('journal visibility changed')
        sa = {s.get('progress'): s for s in A.get('stages', [])}; sb = {s.get('progress'): s for s in B.get('stages', [])}
        add, rem = sorted(set(sb) - set(sa)), sorted(set(sa) - set(sb))
        if add: out.append('stages added: ' + ', '.join(map(str, add)))
        if rem: out.append('stages removed: ' + ', '.join(map(str, rem)))
        for p in sorted(set(sa) & set(sb)):
            if sa[p].get('logText') != sb[p].get('logText'): out.append(f"stage {p} journal text changed")
            if bool(sa[p].get('finishesQuest')) != bool(sb[p].get('finishesQuest')):
                out.append(f"stage {p} {'now' if sb[p].get('finishesQuest') else 'no longer'} completes the quest")
            if sa[p].get('rewardExperience') != sb[p].get('rewardExperience'):
                out.append(f"stage {p} XP {sa[p].get('rewardExperience', 0)} → {sb[p].get('rewardExperience', 0)}")
        return out or ['minor data change']
    if kind == 'dialogue':
        out = []
        if A.get('message') != B.get('message'): out.append(f"text: “{_t(A.get('message'), 70)}” → “{_t(B.get('message'), 70)}”")
        if A.get('replies') != B.get('replies'): out.append('choices or their conditions changed')
        if A.get('rewards') != B.get('rewards'): out.append('effects changed')
        return out or ['minor data change']
    out = []
    for f in sorted(set(A) | set(B)):
        if A.get(f) != B.get(f) and f != 'id':
            out.append(f"{f}: {_t(A.get(f), 40)} → {_t(B.get(f), 40)}" if f in A and f in B else
                       (f"{f} added ({_t(B.get(f), 40)})" if f in B else f"{f} removed"))
    return out or ['minor data change']


def diff(prev, cur, version, hist):
    """Append events for one release to hist (in place)."""
    ent = hist.setdefault('entities', {})
    summary = {}
    for k in KINDS:
        P, C, E = prev.get(k, {}) if prev else {}, cur.get(k, {}), ent.setdefault(k, {})
        added = [i for i in C if i not in P] if prev else []
        removed = [i for i in P if i not in C]
        changed = [i for i in C if i in P and P[i] != C[i]]
        for i in added: E.setdefault(i, []).append([version, 'added', []])
        for i in removed: E.setdefault(i, []).append([version, 'removed', []])
        for i in changed: E.setdefault(i, []).append([version, 'changed', _diff(k, P[i], C[i])])
        if prev: summary[k] = [len(added), len(changed), len(removed)]
        if prev and k == 'quests':
            vis = lambda i, S: bool(json.loads(S[i]).get('showInLog', 0))
            summary['journal_quests'] = [sum(vis(i, C) for i in added), sum(vis(i, C) for i in changed), sum(vis(i, P) for i in removed)]
    hist.setdefault('summary', {})[version] = summary
    hist.setdefault('incompletable', {})[version] = completable(cur)
    tot = {k: len(cur[k]) for k in KINDS}
    tot['journal_quests'] = sum(1 for x in cur['quests'].values() if json.loads(x).get('showInLog', 0))
    hist.setdefault('totals', {})[version] = tot
    hist.pop('completable', None)
    if version not in hist.setdefault('versions', []): hist['versions'].append(version)
    if not prev: hist['first'] = version


def save(path, obj):
    if path.endswith('.gz'):
        with gzip.open(path, 'wt', encoding='utf-8') as f: json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))
    else:
        with open(path, 'w', encoding='utf-8') as f: json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))


def load(path):
    if not os.path.exists(path): return None
    if path.endswith('.gz'):
        with gzip.open(path, 'rt', encoding='utf-8') as f: return json.load(f)
    return json.load(open(path, encoding='utf-8'))


def update_history(data_dir, game_res, version):
    """Called by build.py: append the current release if it's new. Returns the history dict (or None)."""
    hp, sp = os.path.join(data_dir, 'history.json'), os.path.join(data_dir, 'history_snapshot.json.gz')
    hist, prev = load(hp), load(sp)
    if hist is None: return None
    if version in hist['versions']: return hist
    cur = snapshot(game_res)
    diff(prev, cur, version, hist)
    save(hp, hist); save(sp, cur)
    return hist


if __name__ == '__main__':  # full rebuild from every tag in a (blobless) git clone
    repo, out = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'data'
    tags = subprocess.run(['git', '-C', repo, 'tag'], capture_output=True, text=True).stdout.split()
    by_commit = {}
    for t in tags:
        v = t.lstrip('vV')
        if not re.fullmatch(r'\d+(\.\d+)+', v) or vkey(v) < vkey(FIRST_TRACKED): continue
        c = subprocess.run(['git', '-C', repo, 'rev-parse', t + '^{commit}'], capture_output=True, text=True).stdout.strip()
        if c not in by_commit or vkey(v) < vkey(by_commit[c][0]): by_commit[c] = (v, t)
    releases = sorted(by_commit.values(), key=lambda x: vkey(x[0]))
    hist, prev = {'versions': []}, None
    for v, t in releases:
        subprocess.run(['git', '-C', repo, 'checkout', '-q', '-f', t], check=True)
        res = os.path.join(repo, 'AndorsTrail', 'res')
        tree = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', t, 'AndorsTrail/res/xml/'], capture_output=True, text=True).stdout
        shas = {m.group(2): m.group(1) for m in re.finditer(r'blob (\w+)\t\S*/(\w+)\.tmx', tree)}
        cur = snapshot(res, shas)
        diff(prev, cur, v, hist)
        print(v, {k: len(cur[k]) for k in KINDS}, hist['summary'][v], flush=True)
        prev = cur
    os.makedirs(out, exist_ok=True)
    save(os.path.join(out, 'history.json'), hist)
    save(os.path.join(out, 'history_snapshot.json.gz'), prev)


# ======================================================================== rendering
def vlink(v, pre='../'): return f"[v{v}]({pre}versions/{v}.md)"


def verified(what, version):
    return f"\n<p class=\"verified\">Verified against v{version} {what}.</p>\n\n"


def _dialogue_rows(hist, node_ids):
    """Per release: how the given dialogue lines changed."""
    rows = {}
    E = hist['entities'].get('dialogue', {})
    for nid in node_ids:
        for v, ev, det in E.get(nid, []):
            r = rows.setdefault(v, {'added': 0, 'changed': 0, 'removed': 0, 'texts': []})
            if v == hist.get('first') and ev == 'added': continue
            r[ev] += 1
            r['texts'].extend(d for d in det if d.startswith('text:'))
    out = {}
    for v, r in rows.items():
        parts = [f"{r[k]} line{'s' if r[k] != 1 else ''} {k}" for k in ('added', 'changed', 'removed') if r[k]]
        if parts:
            out[v] = 'Dialogue: ' + ', '.join(parts) + (''.join(f"<br>· {t}" for t in r['texts'][:2]))
    return out


def completability_text(hist, qid, names, version):
    """Version-anchored statement about whether the quest could be finished, e.g. 'Before v0.8.18 …'."""
    runs, cur = [], None
    present = [v for v in hist['versions'] if _exists(hist, 'quests', qid, v)]
    for v in present:
        why = hist.get('incompletable', {}).get(v, {}).get(qid)
        key = why or ''
        if cur and cur[0] == key: cur[2] = v
        else: cur = [key, v, v]; runs.append(cur)
    if not runs or all(r[0] == '' for r in runs): return ''
    def nice(why):
        for iid, nm in names.items(): why = why.replace(iid, nm)
        return why
    out = []
    for i, (why, a, b) in enumerate(runs):
        span = f"v{a}" if a == b else f"v{a} to v{b}"
        if why and i + 1 < len(runs):
            out.append(f"From {span}, this quest could not be completed: {nice(why)}. It became completable in {vlink(runs[i + 1][1])}.")
        elif why:
            out.append(f"As of v{b}, this quest cannot be completed: {nice(why)}." + (f" This has been the case since v{a}." if a != b else ''))
    return ' '.join(out)


def _exists(hist, kind, oid, v):
    evs = hist['entities'].get(kind, {}).get(oid, [])
    alive = bool(evs) and evs[0][1] != 'added'   # no 'added' event = it was already in the baseline release
    if not evs: return False
    for ver, ev, _ in evs:
        if vkey(ver) > vkey(v): break
        alive = ev != 'removed'
    return alive


def history_section(hist, kind, oid, version, dialogue_ids=(), lead=''):
    if not hist: return ''
    evs = hist['entities'].get(kind, {}).get(oid, [])
    rows = {}
    if not evs or evs[0][1] != 'added':
        rows[hist['first']] = f"Present in v{hist['first']} (earliest release tracked)"
    for v, ev, det in evs:
        if ev == 'added':
            rows[v] = f"Present in v{v} (earliest release tracked)" if v == hist.get('first') else 'Added'
        elif ev == 'removed': rows[v] = 'Removed from the game'
        else: rows[v] = '; '.join(det[:6]) + (f" (+{len(det) - 6} more)" if len(det) > 6 else '')
    for v, t in _dialogue_rows(hist, dialogue_ids).items():
        rows[v] = (rows[v] + '<br>' + t) if v in rows else t
    if not rows and not lead: return ''
    body = "| Version | Change |\n|---|---|\n" + ''.join(
        f"| {vlink(v)} | {t.replace('|', '/')} |\n" for v, t in sorted(rows.items(), key=lambda kv: vkey(kv[0])))
    return (f"\n## Version history\n\n" + (lead + "\n\n" if lead else '') + body +
            verified(f"and every earlier release back to v{hist.get('first')} (game data compared release by release)", version))


def write_version_pages(hist, write, names, version, page_exists):
    """versions/index.md (overview + growth chart) and versions/<v>.md (everything that changed)."""
    if not hist: return
    vs = hist['versions']
    L = ["# Version history\n\nWhat every release of Andor's Trail changed, worked out by comparing the game's own data "
         f"release by release, from v{hist['first']} to v{vs[-1]}. Older versions still show up in search results, so if "
         "something you read elsewhere doesn't match your game, the answer is probably here.\n\n"
         "![Content growth](../assets/charts/growth.png)\n\n"
         "| Version | New journal quests | New items | New monsters & NPCs | New maps | Dialogue lines added / changed |\n|---|---|---|---|---|---|\n"]
    for v in reversed(vs):
        sm = hist['summary'].get(v, {})
        g = lambda k, i=0: sm.get(k, [0, 0, 0])[i]
        if v == hist['first']:
            L.append(f"| {vlink(v, '')} | (baseline: {hist['totals'][v]['journal_quests']} quests) | {hist['totals'][v]['items']} | {hist['totals'][v]['monsters']} | {hist['totals'][v]['maps']} | – |\n"); continue
        L.append(f"| [v{v}]({v}.md) | {g('journal_quests')} | {g('items')} | {g('monsters')} | {g('maps')} | {g('dialogue')} / {g('dialogue', 1)} |\n")
    L.append(verified("and every earlier release (counts come from the game data, so they can differ slightly from the official release notes)", version))
    write('versions/index.md', ''.join(L).replace("](../versions/", "]("))
    labels = {'items': 'items', 'monsters': 'monsters & NPCs', 'quests': 'quests', 'maps': 'maps', 'droplists': 'loot tables'}
    for i, v in enumerate(vs):
        prev = vs[i - 1] if i else None
        P = [f"# Version {v}\n\n" + (f"Changes from v{prev} to v{v}, read from the game data. " if prev else
             "The earliest release tracked here; everything below existed in it. ") +
             (f"[← v{prev}]({prev}.md)" if prev else '') + (f" · [v{vs[i + 1]} →]({vs[i + 1]}.md)" if i + 1 < len(vs) else '') + "\n\n"]
        if prev:
            # quests
            inc_prev, inc_now = hist['incompletable'].get(prev, {}), hist['incompletable'].get(v, {})
            fixed = [q for q in inc_prev if q not in inc_now and _exists(hist, 'quests', q, v)]
            if fixed:
                P.append("## Quests that became completable\n\n" + ''.join(f"- {_name(names, 'quests', q, page_exists)}: previously {_nice(inc_prev[q], names)}\n" for q in fixed) + "\n")
            for kind in ('quests', 'items', 'monsters', 'maps'):
                E = hist['entities'].get(kind, {})
                add = sorted(i for i, evs in E.items() for ver, ev, _ in evs if ver == v and ev == 'added')
                ch = sorted((i, det) for i, evs in E.items() for ver, ev, det in evs if ver == v and ev == 'changed')
                rem = sorted(i for i, evs in E.items() for ver, ev, _ in evs if ver == v and ev == 'removed')
                if not (add or ch or rem): continue
                P.append(f"## {labels[kind].capitalize()}\n\n")
                if add: P.append(f"**Added ({len(add)}):** " + ', '.join(_name(names, kind, x, page_exists) for x in add) + "\n\n")
                if rem: P.append(f"**Removed ({len(rem)}):** " + ', '.join(_name(names, kind, x, page_exists) for x in rem) + "\n\n")
                if ch:
                    body = ''.join(f"    - {_name(names, kind, x, page_exists)}: {'; '.join(d[:4]).replace('|', '/')}\n" for x, d in ch)
                    P.append(f"??? note \"Changed ({len(ch)})\"\n\n{body}\n")
            sm = hist['summary'].get(v, {}).get('dialogue', [0, 0, 0])
            P.append(f"## Dialogue\n\n{sm[0]} lines added, {sm[1]} changed, {sm[2]} removed. Each NPC's and quest's page lists the changes that affect it.\n")
        P.append(verified(f"and v{prev} data" if prev else "data", v))
        write(f'versions/{v}.md', ''.join(P))


def _nice(why, names):
    for iid, nm in names.get('items', {}).items():
        why = re.sub(rf'\b{re.escape(iid)}\b', nm, why)
    return why


def _name(names, kind, oid, page_exists):
    nm = names.get(kind, {}).get(oid, oid)
    return f"[{nm}](../{kind}/{oid}.md)" if page_exists(kind, oid) else f"{nm} (`{oid}`)"


def growth_chart(hist, out_png):
    import matplotlib; matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    vs = hist['versions']; T = hist['totals']
    BG, FG, GR = '#122438', '#dadada', '#8c8c8c'
    f, ax = plt.subplots(figsize=(8, 3.8), dpi=110); f.patch.set_facecolor(BG); ax.set_facecolor(BG)
    for sp in ax.spines.values(): sp.set_color(GR)
    ax.tick_params(colors=FG, labelsize=7); ax.grid(color='#2e4464', lw=.7)
    x = range(len(vs))
    for k, col, lab in (('maps', '#5ee3f1', 'Maps'), ('items', '#ffb400', 'Items'), ('monsters', '#e04b3a', 'Monsters & NPCs')):
        ax.plot(x, [T[v][k] for v in vs], color=col, lw=2, label=lab)
    ax2 = ax.twinx(); ax2.plot(x, [T[v]['journal_quests'] for v in vs], color='#5fd068', lw=2.5, ls='--', label='Journal quests (right axis)')
    ax2.tick_params(colors=FG, labelsize=7)
    for sp in ax2.spines.values(): sp.set_color(GR)
    ax.set_xticks(list(x), [f"v{v}" for v in vs], rotation=70)
    ax.set_title("Andor's Trail content growth by release", color='#fcfcfc', fontweight='bold')
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, facecolor=BG, edgecolor=GR, labelcolor=FG, fontsize=7, loc='upper left')
    f.tight_layout(); f.savefig(out_png, facecolor=BG); plt.close(f)
