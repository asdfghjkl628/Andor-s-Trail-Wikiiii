---
description: "Brightport commoner is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Brightport commoner

**Where to find Brightport commoner:** [Brightport, Brightport 1 and 1 more](#v-brightportcitizen), [Brightport, Brightport 5](#v-brightportcitizen1)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_man1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Brightport, Brightport 1 and 1 more { #v-brightportcitizen }

**Where:** Brightport: [Brightport 1](../maps/brightport1.md#pin-npc-brightportcitizen), Brightport: [Brightport 3](../maps/brightport3.md#pin-npc-brightportcitizen)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport 1](../maps/brightport1.md) | Brightport | 1 | – |
| [Brightport 3](../maps/brightport3.md) | Brightport | 2 | – |

### Dialogue simulator

Talk to Brightport commoner as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_citizen0.json" data-npc="Brightport commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportcitizen-brightport_citizen0"></span>**`brightport_citizen0`** [Brightport commoner](../monsters/brightportcitizen.md): “Excuse me, I have no time for discussion.”

    - “Neither do I.” → *conversation ends*
    - “How boorish.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brightport, Brightport 5 { #v-brightportcitizen1 }

**Where:** Brightport: [Brightport 5](../maps/brightport5.md#pin-npc-brightportcitizen1)

### Dialogue simulator

Talk to Brightport commoner as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_citizen.json" data-npc="Brightport commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportcitizen1-brightport_citizen"></span>**`brightport_citizen`** [Brightport commoner](../monsters/brightportcitizen.md#v-brightportcitizen1): “Sigh. Nowadays, the streets are always bustling with clamor, and everyone seems to be in a hurry. I miss the days when I could quietly sit and gaze at the lake.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Brightport commoner. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `brightportcitizen` | NPC | [Brightport, Brightport 1 and 1 more](#v-brightportcitizen) |
| `brightportcitizen1` | NPC | [Brightport, Brightport 5](#v-brightportcitizen1) |

??? info "Technical information: brightportcitizen"

    | | |
    |---|---|
    | Entry ID | `brightportcitizen` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportcitizen` |
    | Loot table | – |
    | Conversation | `brightport_citizen0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportcitizen",
     "name": "Brightport commoner",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "phraseID": "brightport_citizen0"
    }
    ```

??? info "Technical information: brightportcitizen1"

    | | |
    |---|---|
    | Entry ID | `brightportcitizen1` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportcitizen1` |
    | Loot table | – |
    | Conversation | `brightport_citizen` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:12` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportcitizen1",
     "name": "Brightport commoner",
     "iconID": "monsters_ld1:12",
     "unique": 1,
     "phraseID": "brightport_citizen"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
