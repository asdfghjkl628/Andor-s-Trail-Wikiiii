---
description: "Spider eggs is a ordinary edible animal part in Andor's Trail. How to get it: monster drops, containers. Better served cooked, but some like to eat these raw."
---

# ![](../assets/icons/items/items_misc_3_126.png){ .sprite } Spider eggs

*Ordinary edible animal part.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_3_126.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `spider_eggs` |
| **Category** | Edible animal part |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

> Better served cooked, but some like to eat these raw.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Food-poisoning](../conditions/foodp.md) (magnitude 3, 10 rounds, 5% chance); [Sustenance](../conditions/food.md) (magnitude 6, 3 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Forest hunter](../monsters/forest_hunter.md) | 25% | 1-2 | Haunted forest 1, Haunted forest 13, Haunted forest 14 |

### Found in containers

- [Haunted house](../maps/haunted_house.md#container-0) (container 1, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spider_eggs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spider_eggs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spider_eggs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spider_eggs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `spider_eggs` |
    | Category ID | `animal_e` |
    | Icon | `items_misc_3:126` |
    | Defined in | `res/raw/itemlist_haunted_forest.json` |
    | Loot tables containing it | `forest_hunter_dl`, `haunted_house_dl` |

    Raw data:

    ```json
    {
     "id": "spider_eggs",
     "iconID": "items_misc_3:126",
     "name": "Spider eggs",
     "displaytype": "ordinary",
     "category": "animal_e",
     "description": "Better served cooked, but some like to eat these raw.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "foodp",
        "magnitude": 3,
        "duration": 10,
        "chance": "5"
       },
       {
        "condition": "food",
        "magnitude": 6,
        "duration": 3,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
