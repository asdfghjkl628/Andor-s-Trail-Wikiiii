---
description: "Arngyr is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite } Arngyr

**Where to find Arngyr:** Loneford: [Loneford 10](../maps/loneford10.md#pin-npc-arngyr)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Loneford |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [General story flags (hidden flag)](../quests/nondisplay.md): stage 19

## Dialogue simulator

Set your quest stages and items, then talk to Arngyr. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/arngyr.json" data-npc="Arngyr" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-arngyr"></span>**`arngyr`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 19 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-19))* → [arngyr_back_1](#d-arngyr_back_1)
    - branch 2 → [arngyr_1](#d-arngyr_1)

    <span id="d-arngyr_back_1"></span>**`arngyr_back_1`** Arngyr: “Hello again. I hope the bed is comfortable enough.”


    <span id="d-arngyr_1"></span>**`arngyr_1`** Arngyr: “Yes, can I help you?”

    - “Mind if I use one of the beds back there?” → [arngyr_2](#d-arngyr_2)

    <span id="d-arngyr_2"></span>**`arngyr_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 55 of [Flows through the veins](../quests/loneford.md#stage-55))* → [arngyr_3](#d-arngyr_3)
    - branch 2 → [arngyr_4](#d-arngyr_4)

    <span id="d-arngyr_3"></span>**`arngyr_3`** Arngyr: “Oh no, not at all. Go ahead. After all you have done for us here in Loneford, it would be a privilege to be able to give something back to you.” — **effects:** sets stage 19 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-19)

    - Next → [arngyr_6](#d-arngyr_6)

    <span id="d-arngyr_4"></span>**`arngyr_4`** Arngyr: “These beds are mostly used by us guards. But I guess I could make an exception since you're just a kid. Shall we say, 600 gold and you may use it?”

    - “Sure, here is the gold.” *(if pay 600 gold)* → [arngyr_5](#d-arngyr_5)
    - “What?! That's a bit much, don't you think?” → [arngyr_7](#d-arngyr_7)

    <span id="d-arngyr_6"></span>**`arngyr_6`** Arngyr: “Use the bed in the back over there as much as you like.”

    - “Thanks.” → *conversation ends*

    <span id="d-arngyr_5"></span>**`arngyr_5`** Arngyr: “Thank you.” — **effects:** sets stage 19 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-19)

    - Next → [arngyr_6](#d-arngyr_6)

    <span id="d-arngyr_7"></span>**`arngyr_7`** Arngyr: “Look, kid. I make the rules around here. If that's my price then that's my price. Take it or leave it.”

    - “Fine, here is the gold.” *(if pay 600 gold)* → [arngyr_5](#d-arngyr_5)
    - “Never mind then.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `arngyr` |
    | Type (wiki) | NPC |
    | Spawn group | `arngyr` |
    | Loot table | – |
    | Conversation | `arngyr` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:65` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "arngyr",
     "name": "Arngyr",
     "iconID": "monsters_rltiles1:65",
     "monsterClass": "humanoid",
     "spawnGroup": "arngyr",
     "phraseID": "arngyr"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arngyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arngyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arngyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arngyr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
