---
description: "Prim citizen is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Prim citizen

**Where to find Prim citizen:** Prim: [Blackwater mountain 11](../maps/blackwater_mountain11.md#pin-npc-prim_citizen)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Prim |
| **Entry ID** | `prim_citizen` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Clouded intent](../quests/prim_hunt.md): stages 11, 15

## Dialogue simulator

Set your quest stages and items, then talk to Prim citizen. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_commoner1.json" data-npc="Prim citizen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_commoner1"></span>**`prim_commoner1`** Prim citizen: “Hello there. Welcome to Prim. Are you here to help us?”

    - “Yes, I am here to help your village.” → [prim_commoner1_2](#d-prim_commoner1_2)
    - “[Lie] Yes, I am here to help your village.” → [prim_commoner1_2](#d-prim_commoner1_2)
    - “Maybe, but first tell me what do you know about Lorn's crew accident?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → [prim_commoner1_5](#d-prim_commoner1_5)

    <span id="d-prim_commoner1_2"></span>**`prim_commoner1_2`** Prim citizen: “Thank you. We really need your help.” — **effects:** sets stage 11 of [Clouded intent](../quests/prim_hunt.md#stage-11)

    - Next → [prim_commoner1_3](#d-prim_commoner1_3)

    <span id="d-prim_commoner1_5"></span>**`prim_commoner1_5`** Prim citizen: “Lorn's crew accident you say? No idea. They are still missing, officially.”

    - “And unofficially?” → [prim_commoner1_6](#d-prim_commoner1_6)
    - “I see, thanks for nothing.” → *conversation ends*

    <span id="d-prim_commoner1_3"></span>**`prim_commoner1_3`** Prim citizen: “You should speak to Guthbered if you haven't done so already.”

    - “Will do, goodbye.” → *conversation ends*
    - “Where can I find him?” → [prim_commoner1_4](#d-prim_commoner1_4)

    <span id="d-prim_commoner1_6"></span>**`prim_commoner1_6`** Prim citizen: “Sorry child, I do not pay attention to the local gossip. Ask around.”

    - “Thank you, Shadow be with you.” → *conversation ends*
    - “What a waste of time, tsch.” → *conversation ends*

    <span id="d-prim_commoner1_4"></span>**`prim_commoner1_4`** Prim citizen: “He is in the main hall right over there. The large stone house.” — **effects:** sets stage 15 of [Clouded intent](../quests/prim_hunt.md#stage-15)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_citizen` |
    | Spawn group | `prim_commoner1` |
    | Loot table | – |
    | Conversation | `prim_commoner1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:6` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_citizen",
     "name": "Prim citizen",
     "iconID": "monsters_karvis2:6",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_commoner1",
     "phraseID": "prim_commoner1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
