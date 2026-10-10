---
description: "Gison and Nimael's soup of the forest is a rare food in Andor's Trail. How to get it: shops. A delicious soup."
---

# ![](../assets/icons/items/items_tometik1_21.png){ .sprite } Gison and Nimael's soup of the forest

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_tometik1_21.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `soup_forest` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 54 gold |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

> A delicious soup.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 3 |
| On self | [Sustenance](../conditions/food.md) (magnitude 3, 7 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Bela](../monsters/bela.md#v-bela_2)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Gael](../monsters/gael.md) ([Mywild 20 houseright](../maps/mywild20_houseright.md)) | – | must be carried (1×) | “(automatic)” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=soup_forest.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=soup_forest.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=soup_forest.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=soup_forest.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `soup_forest` |
    | Category ID | `food` |
    | Icon | `items_tometik1:21` |
    | Defined in | `res/raw/itemlist_fungi_panic.json` |
    | Loot tables containing it | `shop_bela_2` |

    Raw data:

    ```json
    {
     "id": "soup_forest",
     "iconID": "items_tometik1:21",
     "name": "Gison and Nimael's soup of the forest",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 54,
     "category": "food",
     "description": "A delicious soup.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 3
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 7,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
