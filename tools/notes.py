"""Community notes: hand-written content that survives rebuilds.

Write notes in  notes/<type>/<id>.md  (e.g. notes/quests/charwood1.md) using '## Section' headings.
The build merges each section into the matching generated page. Empty sections show a short
invitation with a link that opens the file on GitHub, prefilled, ready to edit.
"""
import os, re, urllib.parse

SECTIONS = {
    'quests':   ['Walkthrough', 'Lore', 'Trivia', 'Bugs', 'Theory / speculation'],
    'monsters': ['Observations', 'Lore', 'Trivia', 'Theory / speculation'],
    'skills':   ['Strategy', 'Trivia'],
    'maps':     ['Observations', 'Lore', 'Trivia', 'Theory / speculation'],
}
HINTS = {
    'Walkthrough': 'step-by-step help for players',
    'Observations': 'what players notice in-game',
    'Lore': 'the in-world story',
    'Trivia': 'real-world facts, references, development history',
    'Bugs': 'known glitches and workarounds',
    'Theory / speculation': 'unconfirmed ideas; may just be unfinished content',
    'Strategy': 'how and when to use it',
}


class Notes:
    def __init__(self, root, repo=None, branch=None):
        self.root = root
        self.repo = repo or os.environ.get('GITHUB_REPOSITORY', '')
        self.branch = branch or os.environ.get('GITHUB_REF_NAME', 'main')

    def _read(self, kind, oid):
        path = os.path.join(self.root, kind, f'{oid}.md')
        if not os.path.exists(path): return None, {}
        text = open(path, encoding='utf-8').read()
        parts = re.split(r'^##\s+(.+?)\s*$', text, flags=re.M)
        found = {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
        return path, found

    def _link(self, kind, oid, exists):
        if not self.repo: return None
        if exists:
            return f"https://github.com/{self.repo}/edit/{self.branch}/notes/{kind}/{oid}.md"
        template = '\n\n'.join(f"## {s}\n\n<!-- {HINTS.get(s, '')} -->" for s in SECTIONS[kind]) + '\n'
        return (f"https://github.com/{self.repo}/new/{self.branch}/notes/{kind}?filename={urllib.parse.quote(oid)}.md"
                f"&value={urllib.parse.quote(template)}")

    def __call__(self, kind, oid, title=''):
        path, found = self._read(kind, oid)
        link = self._link(kind, oid, bool(path))
        invite = (f"*Nothing here yet. Know something? [Add it]({link}).*" if link
                  else f"*Nothing here yet. Add it in `notes/{kind}/{oid}.md`.*")
        out = ["\n## Community notes\n\n<small>Written by players, not generated from game data. "
               + ' · '.join(f"**{s}**: {HINTS[s]}" for s in SECTIONS[kind]) + "</small>\n\n"]
        for s in SECTIONS[kind]:
            body = found.get(s, '')
            body = re.sub(r'<!--.*?-->', '', body, flags=re.S).strip()
            body = render_tags(body)
            out.append(f"### {s}\n\n{body if body else invite}\n\n")
        return ''.join(out)


def render_tags(text):
    """[verified: v0.8.18 | gameplay]  [interpretation]  [unverified]  [developer: https://...]"""
    text = re.sub(r'\[verified:\s*([^|\]]+?)\s*\|\s*([^\]]+?)\s*\]',
                  lambda m: f'<span class="verified">Verified in {m.group(1)} · Source: {m.group(2)}</span>', text)
    text = re.sub(r'\[developer:\s*([^\]]+?)\s*\]', lambda m: f'<span class="verified">Source: [developer statement]({m.group(1)})</span>', text)
    text = text.replace('[interpretation]', '<span class="interp">Interpretation; not confirmed by game data.</span>')
    text = text.replace('[unverified]', '<span class="interp">Unverified; please confirm in-game.</span>')
    return text
