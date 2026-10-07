---
description: "Prim resident is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_karvis2_2.png){ .sprite } Prim resident

**Where to find Prim resident:** Prim: [blackwater_mountain11](../maps/blackwater_mountain11.md#pin-npc-prim_resident)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Prim |
| **Entry ID** | `prim_resident` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Climbing up is forbidden](../quests/Omi2_bwm1.md): stage 21

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Prim resident. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_commoner3.json" data-npc="Prim resident" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_commoner3"></span>**`prim_commoner3`** Prim resident: “Hello. Welcome to Prim.”

    - “Do you know anything about Lorn's accident?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → [prim_commoner3_2](#d-prim_commoner3_2)
    - “Thank you for the hints, bye.” *(if reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → *conversation ends*

    <span id="d-prim_commoner3_2"></span>**`prim_commoner3_2`** Prim resident: “Oh, poor Lorn. I heard that he fell off the mountain.”

    - “Anything more?” → [prim_commoner3_3](#d-prim_commoner3_3)
    - “People say he was quite skilled at climbing.” *(if reached stage 9 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-9))* → [prim_commoner3_4](#d-prim_commoner3_4)

    <span id="d-prim_commoner3_3"></span>**`prim_commoner3_3`** Prim resident: “No, sorry. I didn't know him much.”

    - “Thank you anyway, bye.” → *conversation ends*
    - “Thank you. Shadow be with you.” → *conversation ends*

    <span id="d-prim_commoner3_4"></span>**`prim_commoner3_4`** Prim resident: “Was he? Well, maybe he might've had bad luck...”

    - Next → [prim_commoner3_5](#d-prim_commoner3_5)

    <span id="d-prim_commoner3_5"></span>**`prim_commoner3_5`** Prim resident: “You might ask in the tavern. He was a regular there, like most guards.” — **effects:** sets stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21), spawns monsters on blackwater_mountain22

    - “Thank you. Shadow be with you.” → *conversation ends*
    - “Finally, a hint. Thank you.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_resident` |
    | Spawn group | `prim_commoner3` |
    | Loot table | – |
    | Conversation | `prim_commoner3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_resident",
     "name": "Prim resident",
     "iconID": "monsters_karvis2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_commoner3",
     "phraseID": "prim_commoner3"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_resident.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_resident.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_resident.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_resident.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
