---
description: "Mountain eel meat is a ordinary edible animal part in Andor's Trail. How to get it: monster drops. A half-digested eel, possibly nutritious."
---

# ![](../assets/icons/items/items_misc_3_65.png){ .sprite } Mountain eel meat

*Ordinary edible animal part.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_misc_3_65.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `eel_meat` |
| **Category** | Edible animal part |
| **Rarity** | Ordinary |
| **Base value** | 42 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A half-digested eel, possibly nutritious.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 to 4 |
| On self | [Sustenance](../conditions/food.md) (magnitude 7, 2 rounds, 60% chance); [Food-poisoning](../conditions/foodp.md) (magnitude 2, 9 rounds, 30% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [River wretch](../monsters/river_wretch.md) | 8% | 1 | Mt. Galmore |
| [River wretch](../monsters/river_wretch.md#v-river_wretch2) | 8% | 1 | Mt. Galmore |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=eel_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=eel_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=eel_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=eel_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `eel_meat` |
    | Category ID | `animal_e` |
    | Icon | `items_misc_3:65` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `river_wretch_dl` |

    Raw data:

    ```json
    {
     "id": "eel_meat",
     "iconID": "items_misc_3:65",
     "name": "Mountain eel meat",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 42,
     "category": "animal_e",
     "description": "A half-digested eel, possibly nutritious.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 4
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 7,
        "duration": 2,
        "chance": "60"
       },
       {
        "condition": "foodp",
        "magnitude": 2,
        "duration": 9,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
