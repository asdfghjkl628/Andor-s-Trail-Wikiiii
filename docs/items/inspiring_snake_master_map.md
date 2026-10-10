---
description: "Ewmondold's map is a quest other in Andor's Trail. How to get it: monster drops. Written in a language you do not understand, this appears to be a map. But to where? You do not know."
---

# ![](../assets/icons/items/items_japozero_422.png){ .sprite } Ewmondold's map

*Quest other.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_japozero_422.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `inspiring_snake_master_map` |
| **Category** | Other |
| **Rarity** | Quest |
| **Base value** | 0 gold |
| **Quest item** | Yes |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

> Written in a language you do not understand, this appears to be a map.  But to where? You do not know.

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Snake master](../monsters/snake_master.md) | 100% | 1 | Snakecave 3 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Arcir](../monsters/arcir.md) | – | must be carried (1×) | “I have found some valuable-looking map. Want to have a look?” |
| [Arcir](../monsters/arcir.md) | – | handed over (1×) | “OK. Here is Ewmondold's map.” |
| [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) ([Wild 2](../maps/wild2.md)) | [Perception is not reality](../quests/new_snake_master.md#stage-20) | handed over (1×) | “N” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=inspiring_snake_master_map.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=inspiring_snake_master_map.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=inspiring_snake_master_map.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=inspiring_snake_master_map.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `inspiring_snake_master_map` |
    | Category ID | `other` |
    | Icon | `items_japozero:422` |
    | Defined in | `res/raw/itemlist_brimhaven_2.json` |
    | Loot tables containing it | `snakemaster` |

    Raw data:

    ```json
    {
     "id": "inspiring_snake_master_map",
     "iconID": "items_japozero:422",
     "name": "Ewmondold's map",
     "displaytype": "quest",
     "hasManualPrice": 1,
     "baseMarketCost": 0,
     "category": "other",
     "description": "Written in a language you do not understand, this appears to be a map.  But to where? You do not know."
    }
    ```


<small>Data from v0.8.18</small>
