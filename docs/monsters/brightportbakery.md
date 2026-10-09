---
description: "Hortensia is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld_edit_3.png){ .sprite } Hortensia

**Where to find Hortensia:** Brightport: [Brightport bakery](../maps/brightport_bakery.md#pin-npc-brightportbakery)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld_edit_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportbakery` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 35

## Dialogue simulator

Set your quest stages and items, then talk to Hortensia. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_hortensia.json" data-npc="Hortensia" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_hortensia"></span>**`brightport_hortensia`** Hortensia: “Hello, today's astronomy class at the Academy will be held in the evening, you musn't miss it.”

    - “I don't have time to attend classes, I must find my brother Andor.” *(if NOT reached stage 900 of [Main quest endings (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_hortensia1](#d-brightport_hortensia1)
    - “Academy, where is that?” *(if NOT reached stage 231 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-231))* → [brightport_hortensia3](#d-brightport_hortensia3)
    - “Sorry to disturb your meal. [Leave]” → *conversation ends*

    <span id="d-brightport_hortensia1"></span>**`brightport_hortensia1`** Hortensia: “That boy Andor? He was a bit unremarkable but he had a real passion for astronomy. What has happened to him?”

    - “He has been missing for a while, and so my father sent me out to search for him. Have you seen him?” → [brightport_hortensia2](#d-brightport_hortensia2)

    <span id="d-brightport_hortensia3"></span>**`brightport_hortensia3`** Hortensia: “It is surprising for someone visiting Brightport not to know about its Academy, and here I thought you were a student. Head to the western part of town, and you will find it.”

    - “I don't have time to attend classes, I must find my brother Andor.” *(if NOT reached stage 900 of [Main quest endings (hidden flag)](../quests/andor_ending.md#stage-900))* → [brightport_hortensia1](#d-brightport_hortensia1)
    - “Thanks, bye.” → *conversation ends*

    <span id="d-brightport_hortensia2"></span>**`brightport_hortensia2`** Hortensia: “I'm afraid I cannot be of much help. I haven't seen Andor since his days at the Brightport academy. I hope you find him soon.” — **effects:** sets stage 35 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-35)

    - “I hope so too.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportbakery` |
    | Spawn group | `brightportbakery` |
    | Loot table | – |
    | Conversation | `brightport_hortensia` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld_edit:3` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportbakery",
     "name": "Hortensia",
     "iconID": "monsters_ld_edit:3",
     "unique": 1,
     "phraseID": "brightport_hortensia"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakery.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
