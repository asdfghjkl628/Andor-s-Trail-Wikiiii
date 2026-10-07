---
description: "brv_wh_item_20 is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_guynmart_8.png){ .sprite } brv_wh_item_20

**Where to find brv_wh_item_20:** Brimhaven: [brimhaven_warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_20)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_guynmart_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven |
| **Entry ID** | `brv_wh_item_20` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [Inventory](../quests/brv_wh.md): stage 100

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with brv_wh_item_20. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_20.json" data-npc="brv_wh_item_20" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_wh_item_20"></span>**`brv_wh_item_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 100)* → [brv_wh_item_00_1](#d-brv_wh_item_00_1)
    - branch 2 *(if faction “brv_wh_aln” = 120)* → [brv_wh_item_xx_2](#d-brv_wh_item_xx_2)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_xx_3)
    - branch 4 → [brv_wh_item_20_4](#d-brv_wh_item_20_4)

    <span id="d-brv_wh_item_00_1"></span>**`brv_wh_item_00_1`** brv_wh_item_20: “You have found the second crystal globe. Now that's a pair!” — **effects:** sets stage 100 of [Inventory](../quests/brv_wh.md#stage-100), gives 2× [Crystal globe](../items/brv_wh_item_00.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_xx_2"></span>**`brv_wh_item_xx_2`** brv_wh_item_20: “You put it back to its former place.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_xx_3"></span>**`brv_wh_item_xx_3`** brv_wh_item_20: “No, this is not what you're looking for. You put both items back to their bin.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_20_4"></span>**`brv_wh_item_20_4`** brv_wh_item_20: “You take the item.” — **effects:** faction “brv_wh_aln” set to 120




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_20` |
    | Spawn group | `brv_wh_item_20` |
    | Loot table | – |
    | Conversation | `brv_wh_item_20` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_20",
     "name": "brv_wh_item_20",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_20",
     "phraseID": "brv_wh_item_20"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_20.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_20.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_20.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_20.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
