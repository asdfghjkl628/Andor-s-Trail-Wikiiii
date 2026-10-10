---
description: "Lowyna is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Lowyna

**Where to find Lowyna:** Fallhaven: [Woodhouse 2](../maps/woodhouse2.md#pin-npc-lowyna)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Fallhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Apple juice](../items/drink_applej.md) | 100% | 5 to 20 |
| [Prune juice](../items/drink_prunej.md) | 100% | 5 to 20 |
| [Lowyna's foul brew](../items/drink_lowyn1.md) | 100% | 5 to 20 |
| [Lowyna's special brew](../items/drink_lowyn2.md) | 100% | 5 to 20 |
| [Lowyna's rat poison](../items/drink_lowyn3.md) | 100% | 5 to 20 |

## Quests

- [Sweet sweet rat poison](../quests/lowyna.md): stage 20

## Dialogue simulator

Set your quest stages and items, then talk to Lowyna. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lowyna.json" data-npc="Lowyna" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lowyna"></span>**`lowyna`** Lowyna: “Uh. Hello.”

    - Next → [lowyna_1](#d-lowyna_1)

    <span id="d-lowyna_1"></span>**`lowyna_1`** Lowyna: “Whoa, you look small. I must be seeing things. That last batch I did must have gotten stronger than usual.”

    - “Who are you?” → [lowyna_3](#d-lowyna_3)
    - “What are you people doing here?” → [lowyna_2](#d-lowyna_2)
    - “What is that smell?” → [lowyna_4](#d-lowyna_4)
    - “Can I look at your wares again?” *(if reached stage 20 of [Sweet sweet rat poison](../quests/lowyna.md#stage-20))* → *shop opens*

    <span id="d-lowyna_3"></span>**`lowyna_3`** Lowyna: “I am Lowyna, of course. These people that you see in here and in the other huts, you could say that we're sort of in the same ... family.”

    - “What are you people doing here?” → [lowyna_2](#d-lowyna_2)

    <span id="d-lowyna_2"></span>**`lowyna_2`** Lowyna: “He he, this and that.”

    - “I see a lot of potion bottles around. Is that what you do?” → [lowyna_5](#d-lowyna_5)
    - “What is that smell?” → [lowyna_4](#d-lowyna_4)

    <span id="d-lowyna_4"></span>**`lowyna_4`** Lowyna: “What smell? I can't smell anything out of the ordinary. It must be you.”

    - “What are you people doing here?” → [lowyna_2](#d-lowyna_2)
    - “Who are you?” → [lowyna_3](#d-lowyna_3)

    <span id="d-lowyna_5"></span>**`lowyna_5`** Lowyna: “It's that obvious eh?”

    - Next → [lowyna_6](#d-lowyna_6)

    <span id="d-lowyna_6"></span>**`lowyna_6`** Lowyna: “I really shouldn't be discussing this with you. You look way too inexperienced for this.”

    - “I can handle myself!” → [lowyna_7](#d-lowyna_7)
    - “Two-teeth sent me to get some rat poison.” *(if reached stage 10 of [Sweet sweet rat poison](../quests/lowyna.md#stage-10))* → [lowyna_8](#d-lowyna_8)

    <span id="d-lowyna_7"></span>**`lowyna_7`** Lowyna: “Hah! How about no?”


    <span id="d-lowyna_8"></span>**`lowyna_8`** Lowyna: “I'm amazed he's still around, good old two-teeth.”

    - Next → [lowyna_9](#d-lowyna_9)

    <span id="d-lowyna_9"></span>**`lowyna_9`** Lowyna: “For his sake, I'll let you browse my wares.” — **effects:** sets stage 20 of [Sweet sweet rat poison](../quests/lowyna.md#stage-20)

    - “Let's see what you have.” *(if reached stage 20 of [Sweet sweet rat poison](../quests/lowyna.md#stage-20))* → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “I am Lowyna, of course. These people that you see in here and in the …” → “I am Lowyna, of course. These people that you see in here and in the …” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “I really shouldn't be discussing this with you. You look way to inexp…” → “I really shouldn't be discussing this with you. You look way too inex…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lowyna` |
    | Type (wiki) | NPC |
    | Spawn group | `lowyna` |
    | Loot table | `shop_lowyna` |
    | Conversation | `lowyna` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:94` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "lowyna",
     "name": "Lowyna",
     "iconID": "monsters_rltiles1:94",
     "phraseID": "lowyna",
     "droplistID": "shop_lowyna"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lowyna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lowyna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lowyna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lowyna.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
