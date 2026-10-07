---
description: "Gallain is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Gallain

**Where to find Gallain:** Crossroads Guardhouse: [houseatcrossroads0](../maps/houseatcrossroads0.md#pin-npc-gallain)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Crossroads Guardhouse |
| **Entry ID** | `gallain` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Bread](../items/bread.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Gallain. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/gallain.json" data-npc="Gallain" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gallain"></span>**`gallain`** Gallain: “Welcome to the Crossroads guardhouse. I am Gallain, the proprietor of this place.”

    - Next → [gallain_1](#d-gallain_1)

    <span id="d-gallain_1"></span>**`gallain_1`** Gallain: “How may I help you?”

    - “Do you have anything to eat around here?” → [gallain_trade_1](#d-gallain_trade_1)
    - “Is there any place I can rest here?” → [gallain_rest_1](#d-gallain_rest_1)
    - “What is this place?” → [gallain_cr_1](#d-gallain_cr_1)

    <span id="d-gallain_trade_1"></span>**`gallain_trade_1`** Gallain: “Here, have a look.”

    - “Trade” → *shop opens*

    <span id="d-gallain_rest_1"></span>**`gallain_rest_1`** Gallain: “The guards have set up some beds downstairs. Go check with them.”

    - Next → [gallain_1](#d-gallain_1)

    <span id="d-gallain_cr_1"></span>**`gallain_cr_1`** Gallain: “As I said, this is the Crossroads guardhouse. The guards from Feygard are using this place as a place to rest and gear up.”

    - Next → [gallain_cr_2](#d-gallain_cr_2)

    <span id="d-gallain_cr_2"></span>**`gallain_cr_2`** Gallain: “Because of this, it is also a safe haven for merchants travelling through here. We get a lot of those.”

    - Next → [gallain_1](#d-gallain_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `gallain` |
    | Spawn group | `gallain` |
    | Loot table | `shop_gallain` |
    | Conversation | `gallain` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "gallain",
     "name": "Gallain",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "gallain",
     "phraseID": "gallain",
     "droplistID": "shop_gallain"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gallain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gallain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gallain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gallain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
