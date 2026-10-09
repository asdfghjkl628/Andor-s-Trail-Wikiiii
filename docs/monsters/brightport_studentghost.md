---
description: "Erelyn is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_36.png){ .sprite } Erelyn

**Where to find Erelyn:** Brightport: [Brightport grave](../maps/brightport_grave.md#pin-npc-brightport_studentghost), Brightport: [Brightport school 8](../maps/brightport_school8.md#pin-npc-brightport_studentghost)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_36.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightport_studentghost` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport grave](../maps/brightport_grave.md) | Brightport | 1 | – |
| [Brightport school 8](../maps/brightport_school8.md) | Brightport | 1 | Appears later, during a quest |

## Dialogue simulator

Set your quest stages and items, then talk to Erelyn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_studentghost_selector.json" data-npc="Erelyn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_studentghost_selector"></span>**`brightport_studentghost_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 238 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_studentghost_1](#d-brightport_studentghost_1)
    - Next → [brightport_studentghost_2](#d-brightport_studentghost_2)

    <span id="d-brightport_studentghost_1"></span>**`brightport_studentghost_1`** Erelyn: “Eek!”

    - Next → [brightport_studentghost2](#d-brightport_studentghost2)

    <span id="d-brightport_studentghost_2"></span>**`brightport_studentghost_2`** Erelyn: “Thank the Shadow you were there to save us. Mom always told me to never go grave robbing.”


    <span id="d-brightport_studentghost2"></span>**`brightport_studentghost2`** [Dummy NPC](../monsters/none.md): “The kid seems too shocked to move.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_studentghost` |
    | Spawn group | `brightport_studentghost` |
    | Loot table | – |
    | Conversation | `brightport_studentghost_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:36` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_studentghost",
     "name": "Erelyn",
     "iconID": "monsters_ld1:36",
     "phraseID": "brightport_studentghost_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
