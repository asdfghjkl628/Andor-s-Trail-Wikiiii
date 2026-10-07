---
description: "Drendolas is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Drendolas

**Where to find Drendolas:** Brightport: [brightport_grave](../maps/brightport_grave.md#pin-npc-brightport_studentghost1), Brightport: [brightport_school8](../maps/brightport_school8.md#pin-npc-brightport_studentghost1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightport_studentghost1` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_grave](../maps/brightport_grave.md) | Brightport | 1 | – |
| [brightport_school8](../maps/brightport_school8.md) | Brightport | 1 | Appears later, during a quest |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Drendolas. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_studentghost1_selector.json" data-npc="Drendolas" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_studentghost1_selector"></span>**`brightport_studentghost1_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_studentghost1_1](#d-brightport_studentghost1_1)
    - Next → [brightport_studentghost1_4](#d-brightport_studentghost1_4)

    <span id="d-brightport_studentghost1_1"></span>**`brightport_studentghost1_1`** Drendolas: “W-we weren't trying to steal anything!”

    - “What is that ghost?” → [brightport_studentghost1_2](#d-brightport_studentghost1_2)

    <span id="d-brightport_studentghost1_4"></span>**`brightport_studentghost1_4`** Drendolas: “We didn't get to say thank you. You were really brave back there.”

    - “No problem.” → *conversation ends*

    <span id="d-brightport_studentghost1_2"></span>**`brightport_studentghost1_2`** Drendolas: “I don't know, It came out of nowhere!”

    - Next → [brightport_studentghost1_3](#d-brightport_studentghost1_3)

    <span id="d-brightport_studentghost1_3"></span>**`brightport_studentghost1_3`** Drendolas: “You can help us right? Please distract it and we'll find a moment to run away.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_studentghost1` |
    | Spawn group | `brightport_studentghost1` |
    | Loot table | – |
    | Conversation | `brightport_studentghost1_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_studentghost1",
     "name": "Drendolas",
     "iconID": "monsters_ld1:20",
     "phraseID": "brightport_studentghost1_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_studentghost1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
