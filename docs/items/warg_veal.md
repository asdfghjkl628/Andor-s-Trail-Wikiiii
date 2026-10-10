---
description: "Warg veal is a ordinary food in Andor's Trail. How to get it: monster drops. There's just something about meat from a young warg that makes it just a little bit better."
---

# ![](../assets/icons/items/items_consumables_25.png){ .sprite } Warg veal

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_consumables_25.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `warg_veal` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 49 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> There's just something about meat from a young warg that makes it just a little bit better.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 to 2 |
| Restore AP | -1 to 1 |
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 8 rounds); [Food-poisoning](../conditions/foodp.md) (magnitude 3, 6 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Orphaned warg pup](../monsters/orphaned_warg_pup.md) | 8% | 1 | Mt. Galmore |
| [Galmore wolf's pup](../monsters/mg2_wolves_pup.md) | 8% | 1 | Mt. Galmore |
| [Warg pup](../monsters/warg_pup.md) | 8% | 1 | – |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=warg_veal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=warg_veal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=warg_veal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=warg_veal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `warg_veal` |
    | Category ID | `food` |
    | Icon | `items_consumables:25` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `orphaned_warg_pup_dl` |

    Raw data:

    ```json
    {
     "id": "warg_veal",
     "iconID": "items_consumables:25",
     "name": "Warg veal",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 49,
     "category": "food",
     "description": "There's just something about meat from a young warg that makes it just a little bit better.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 2
      },
      "increaseCurrentAP": {
       "min": -1,
       "max": 1
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 8,
        "chance": "100"
       },
       {
        "condition": "foodp",
        "magnitude": 3,
        "duration": 6,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
