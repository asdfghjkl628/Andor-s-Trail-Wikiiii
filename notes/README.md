# Community notes

Hand-written content that the wiki build merges into its generated pages. Everything else on the
wiki is regenerated from the game's data on every release, so **anything typed directly into `docs/`
is overwritten**. Notes in this folder are kept.

## How it works

Create `notes/<type>/<id>.md`, where `<id>` is the ID shown in the page's *Technical information* box:

| Page type | Folder | Sections |
|---|---|---|
| Quest | `notes/quests/` | Walkthrough, Lore, Trivia, Bugs, Theory / speculation |
| Monster or NPC | `notes/monsters/` | Observations, Lore, Trivia, Theory / speculation |
| Skill | `notes/skills/` | Strategy, Trivia |

Each section starts with a `## Heading` using exactly those names. Missing or empty sections show a
short "Add it" invitation on the page. The easiest way to start is to click that link on the wiki page.

## Keep the categories separate

- **Observations**: what you saw in-game.
- **Lore**: what the story and dialogue say.
- **Trivia**: real-world facts, references, development history.
- **Bugs**: glitches and workarounds.
- **Theory / speculation**: anything unconfirmed. Something mysterious may simply be unfinished content.

## Say where a claim comes from

For anything non-obvious, and especially on complicated quests, tag the claim with its source. The tags render
as small italic labels:

| Write this | Shows as |
|---|---|
| `[verified: v0.8.18 \| gameplay]` | *Verified in v0.8.18 · Source: gameplay* |
| `[verified: v0.8.18 \| game files]` | *Verified in v0.8.18 · Source: game files* |
| `[developer: https://link]` | *Source: developer statement* (linked) |
| `[unverified]` | *Unverified; please confirm in-game.* |
| `[interpretation]` | *Interpretation; not confirmed by game data.* |

Example:

```markdown
Killing the Thief leader does not stop Gison's quest from starting. [verified: v0.8.18 | game files]

The skeletons here may be the cave's missing miners. [interpretation]
```

Always name the version. Old versions still show up in search results, so "currently" or "can't be
done" ages badly. Write "Before v0.8.18 this couldn't be done; since v0.8.18 it can."

Game mechanics, requirements and rewards are generated from the data. If they look wrong, report it
rather than writing around it in a note.
