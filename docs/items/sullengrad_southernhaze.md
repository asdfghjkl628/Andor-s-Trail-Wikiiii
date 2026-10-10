---
description: "Southernhaze is a ordinary drink in Andor's Trail. How to get it: monster drops. The reigning champion of the 'Best beer in festival' competition. Product of the Bruyere family"
---

# ![](../assets/icons/items/items_misc_6_23.png){ .sprite } Southernhaze

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_misc_6_23.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `sullengrad_southernhaze` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> The reigning champion of the 'Best beer in festival' competition. Product of the Bruyere family

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 8 |
| On self | [Sustenance](../conditions/food.md) (magnitude 3, 1 round); [Intoxicated](../conditions/intoxicated.md) (magnitude 1, 2 rounds, 40% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Oakleigh](../monsters/sullengard_bartender.md) | 100% | 4-5 | Sullengard |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_southernhaze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_southernhaze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_southernhaze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_southernhaze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sullengrad_southernhaze` |
    | Category ID | `drink` |
    | Icon | `items_misc_6:23` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_bartender_dl` |

    Raw data:

    ```json
    {
     "id": "sullengrad_southernhaze",
     "iconID": "items_misc_6:23",
     "name": "Southernhaze",
     "displaytype": "ordinary",
     "category": "drink",
     "description": "The reigning champion of the 'Best beer in festival' competition. Product of the Bruyere family",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 8,
       "max": 8
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 1,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 1,
        "duration": 2,
        "chance": "40"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
