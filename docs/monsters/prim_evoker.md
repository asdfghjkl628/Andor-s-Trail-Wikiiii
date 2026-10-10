---
description: "Prim evoker is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_84.png){ .sprite } Prim evoker

**Where to find Prim evoker:** Prim: [Blackwater mountain 11](../maps/blackwater_mountain11.md#pin-npc-prim_evoker)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_84.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Prim |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md): stage 10

## Dialogue simulator

Talk to Prim evoker as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_commoner4.json" data-npc="Prim evoker" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_commoner4"></span>**`prim_commoner4`** Prim evoker: “Hello. Who are you? Are you here to help us?”

    - “I am looking for my brother. Would you by any chance have happened to see him around here?” → [prim_commoner4_1](#d-prim_commoner4_1)
    - “Yes, I have come to help your village.” → [prim_commoner4_3](#d-prim_commoner4_3)
    - “[Lie] Yes, I have come to help your village.” → [prim_commoner4_3](#d-prim_commoner4_3)
    - “What do you know about Lorn's accident?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21))* → [prim_commoner4_4](#d-prim_commoner4_4)

    <span id="d-prim_commoner4_1"></span>**`prim_commoner4_1`** Prim evoker: “Your brother? Son, you should know that we do not get many visitors around here.”

    - Next → [prim_commoner4_2](#d-prim_commoner4_2)

    <span id="d-prim_commoner4_3"></span>**`prim_commoner4_3`** Prim evoker: “Oh thank you. We could really use some help around here.”


    <span id="d-prim_commoner4_4"></span>**`prim_commoner4_4`** Prim evoker: “Lorn? Nothing. I barely know him, or his comrades, Duala and...sorry, I forget the name. What's wrong with him?”

    - “He was killed several days ago.” → [prim_commoner4_5a](#d-prim_commoner4_5a)
    - “He had an accident while climbing down the mountain.” → [prim_commoner4_5b](#d-prim_commoner4_5b)

    <span id="d-prim_commoner4_2"></span>**`prim_commoner4_2`** Prim evoker: “So, no. I cannot help you.”


    <span id="d-prim_commoner4_5a"></span>**`prim_commoner4_5a`** Prim evoker: “Oh. I'm sorry. May the Shadow guide his way to a better world.”

    - “Right, uhm...don't you remember anything about him?” → [prim_commoner4_6](#d-prim_commoner4_6)

    <span id="d-prim_commoner4_5b"></span>**`prim_commoner4_5b`** Prim evoker: “Yes, that's why climbing up the mountain is forbidden now.”

    - “Anything more?” → [prim_commoner4_6](#d-prim_commoner4_6)

    <span id="d-prim_commoner4_6"></span>**`prim_commoner4_6`** Prim evoker: “Uhm, well. I heard Lorn was popular among the children here in Prim because of his scary stories about, you know, the monsters.” — **effects:** sets stage 10 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-10)

    - “Gonna ask some child. Thanks.” → *conversation ends*
    - “My father probably told me scarier stories. Bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_evoker` |
    | Type (wiki) | NPC |
    | Spawn group | `prim_commoner4` |
    | Loot table | – |
    | Conversation | `prim_commoner4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:84` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_evoker",
     "name": "Prim evoker",
     "iconID": "monsters_rltiles1:84",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_commoner4",
     "phraseID": "prim_commoner4"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_evoker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
