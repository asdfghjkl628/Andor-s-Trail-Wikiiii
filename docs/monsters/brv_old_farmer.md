---
description: "Peasant grandfather is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_karvis2_5.png){ .sprite } Peasant grandfather

**Where to find Peasant grandfather:** Brimhaven: [Brimhaven 2 farmhouse](../maps/brimhaven2_farmhouse.md#pin-npc-brv_old_farmer)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Brimhaven |
| **Entry ID** | `brv_old_farmer` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Cheese](../items/cheese.md) | 100% | 5 |
| [Green apple](../items/apple_green.md) | 100% | 25 |
| [Red apple](../items/apple_red.md) | 100% | 25 |
| [Carrot](../items/carrot.md) | 100% | 20 |
| [Eggs](../items/eggs.md) | 100% | 10 |
| [Pear](../items/pear.md) | 100% | 20 |
| [Radish](../items/radish.md) | 100% | 20 |
| [Strawberry](../items/strawberry.md) | 100% | 25 |

## Dialogue simulator

Set your quest stages and items, then talk to Peasant grandfather. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_old_farmer_0.json" data-npc="Peasant grandfather" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_old_farmer_0"></span>**`brv_old_farmer_0`** Peasant grandfather: “What are you doing in my house?”

    - “Nothing, sorry I will leave.” → *conversation ends*
    - “I am just looking around.” → [brv_old_farmer_1](#d-brv_old_farmer_1)
    - “Can I buy some of your food?” → [brv_old_farmer_2](#d-brv_old_farmer_2)

    <span id="d-brv_old_farmer_1"></span>**`brv_old_farmer_1`** Peasant grandfather: “Please leave my house.”

    - “Can I buy some of your food?” → [brv_old_farmer_2](#d-brv_old_farmer_2)

    <span id="d-brv_old_farmer_2"></span>**`brv_old_farmer_2`** Peasant grandfather: “Normally we sell to the market. But OK, let's trade.”

    - “Thanks” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_old_farmer` |
    | Spawn group | `brv_old_farmer` |
    | Loot table | `brv_farmer` |
    | Conversation | `brv_old_farmer_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:5` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_old_farmer",
     "name": "Peasant grandfather",
     "iconID": "monsters_karvis2:5",
     "phraseID": "brv_old_farmer_0",
     "droplistID": "brv_farmer"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
