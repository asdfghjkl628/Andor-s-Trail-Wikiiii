---
description: "Loudmouth is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_85.png){ .sprite } Loudmouth

**Where to find Loudmouth:** Brightport: [Brightport thieves](../maps/brightport_thieves.md#pin-npc-brightportthieves)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_85.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportthieves` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Loudmouth. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_loudmouth.json" data-npc="Loudmouth" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_loudmouth"></span>**`brightport_loudmouth`** [Loudmouth](../monsters/brightportthieves.md): “Hey kid, have you met my brother outside? Haha, that guy's a real scrooge. They say we're nothing alike. I'm telling you, he's just like mom - we'd ask her to tell us a bedtime story, and she'd have us pay for it with shiny stones or…”

    - “I'm all ears.” → [brightport_loudmouth1](#d-brightport_loudmouth1)
    - “I'm afraid if I let you speak it will never end.” → [brightport_loudmouth3](#d-brightport_loudmouth3)

    <span id="d-brightport_loudmouth1"></span>**`brightport_loudmouth1`** [Loudmouth](../monsters/brightportthieves.md): “I once heard a story about a guy who visited a kingdom ruled by rats - They call it "Ratdom"! Haha! People say he disappeared as a child and reappeared a decade later, wearing clothes made entirely of ratskin. He even spoke Rattish!…”

    - Next → [brightport_loudmouth2](#d-brightport_loudmouth2)

    <span id="d-brightport_loudmouth3"></span>**`brightport_loudmouth3`** [Loudmouth](../monsters/brightportthieves.md): “Speaking of "never ending", I was assigned to a job a while ago, up in the north. On my way there, I encountered a small critter. Eager for some fresh meat, I slew it, but what came next was, quite literally, never ending. A whole group…”

    - “Interesting, but I must go now.” → *conversation ends*

    <span id="d-brightport_loudmouth2"></span>**`brightport_loudmouth2`** [Loudmouth](../monsters/brightportthieves.md): “Those folks from Brimhaven! I'd refrain from rudely calling them ra... Mice. But if anyone resembles a mouse, it would be them. We got a job offer from... Hic. I'm professional enough not to reveal our clients... Long story short, we…”

    - “Interesting, but I must go now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportthieves` |
    | Spawn group | `brightportthieves` |
    | Loot table | – |
    | Conversation | `brightport_loudmouth` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:85` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportthieves",
     "name": "Loudmouth",
     "iconID": "monsters_ld1:85",
     "unique": 1,
     "phraseID": "brightport_loudmouth"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
