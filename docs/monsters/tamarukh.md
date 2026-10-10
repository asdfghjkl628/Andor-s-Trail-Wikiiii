---
description: "Tamarukh is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_ld1_141.png){ .sprite } Tamarukh

**Where to find Tamarukh:** Loneford: [Waytobrimhaven 2](../maps/waytobrimhaven2.md#pin-npc-tamarukh)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_141.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Loneford |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 88

## Dialogue simulator

Set your quest stages and items, then talk to Tamarukh. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tamarukh.json" data-npc="Tamarukh" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tamarukh"></span>**`tamarukh`** Tamarukh: “Isn't it a pity to see all that fertile land wasted?”

    - “Do you mean the lake?” → [tamarukh_10](#d-tamarukh_10)

    <span id="d-tamarukh_10"></span>**`tamarukh_10`** Tamarukh: “Sure. We had built this dam in Brimhaven to get more space for arable land, but someone must have sabotaged it.”

    - “Would you like to repair the dam again?” → [tamarukh_20](#d-tamarukh_20)

    <span id="d-tamarukh_20"></span>**`tamarukh_20`** Tamarukh: “Yes, I would see to it, if I had enough money.”

    - “Everyone wants my money. I better go.” → *conversation ends*
    - “It should not fail because of a lack of money. Here you have 2,500 gold.” *(if pay 2,500 gold)* → [tamarukh_30](#d-tamarukh_30)

    <span id="d-tamarukh_30"></span>**`tamarukh_30`** Tamarukh: “That is very noble of you. I will take care of it.” — **effects:** sets stage 88 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-88)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Sure. We had built this dam in Brimhaven to get more space for arable…” → “Sure. We had built this dam in Brimhaven to get more space for arable…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `tamarukh` |
    | Type (wiki) | NPC |
    | Spawn group | `tamarukh` |
    | Loot table | – |
    | Conversation | `tamarukh` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:141` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "tamarukh",
     "name": "Tamarukh",
     "iconID": "monsters_ld1:141",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "tamarukh",
     "phraseID": "tamarukh"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
