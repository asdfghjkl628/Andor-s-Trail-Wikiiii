---
description: "Alduan is a non-player character (NPC) in Andor's Trail, found in Deebo's Orchard."
---

# ![](../assets/icons/monsters/monsters_ld_edit_74.png){ .sprite } Alduan

**Where to find Alduan:** Deebo's Orchard: [Sullengard apple farm west](../maps/sullengard_apple_farm_west.md#pin-npc-brightport_orchardsupervisor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld_edit_74.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Deebo's Orchard |
| **Entry ID** | `brightport_orchardsupervisor` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [Bread and circus](../quests/brightport_bakery.md): stage 50

## Dialogue simulator

Set your quest stages and items, then talk to Alduan. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_alduan.json" data-npc="Alduan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_alduan"></span>**`brightport_alduan`** Alduan: “Ah, nothing like a good sweat in the sun. Not my sweat, of course.”

    - “Deebo told me to get the 30 apples from you.” *(if NOT reached stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50); reached stage 45 of [Bread and circus](../quests/brightport_bakery.md#stage-45))* → [brightport_alduan_selector](#d-brightport_alduan_selector)

    <span id="d-brightport_alduan_selector"></span>**`brightport_alduan_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT 3 rounds passed since timer “brightport_apple”)* → [brightport_alduan1](#d-brightport_alduan1)
    - Next *(if 3 rounds passed since timer “brightport_apple”)* → [brightport_alduan2](#d-brightport_alduan2)

    <span id="d-brightport_alduan1"></span>**`brightport_alduan1`** Alduan: “The workers here are very lazy. I'll do my best to hurry them up a little, nothing a good earful won't do.”


    <span id="d-brightport_alduan2"></span>**`brightport_alduan2`** Alduan: “Here are the 30 apples, good sir. I hope one day to visit the bakery in person and savor those sweet pastries made from our apples.” — **effects:** gives 30× [Orchard apple](../items/deebo_apples.md), sets stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_orchardsupervisor` |
    | Spawn group | `brightport_orchardsupervisor` |
    | Loot table | – |
    | Conversation | `brightport_alduan` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld_edit:74` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_orchardsupervisor",
     "name": "Alduan",
     "iconID": "monsters_ld_edit:74",
     "phraseID": "brightport_alduan"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_orchardsupervisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_orchardsupervisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_orchardsupervisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_orchardsupervisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
