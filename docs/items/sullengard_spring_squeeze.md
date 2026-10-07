---
description: "Spring Squeeze is a ordinary drink in Andor's Trail. How to get it: monster drops. A little bit of spring in every sip. Brewed by the Brewere family."
---

# ![](../assets/icons/items/items_misc_6_23.png){ .sprite } Spring Squeeze

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_23.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sullengard_spring_squeeze` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> A little bit of spring in every sip. Brewed by the Brewere family.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 2 to 4 |
| On self | Sustenance (magnitude 2, 2 rounds, 100% chance); Intoxicated (magnitude 1, 4 rounds, 25% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Oakleigh](../monsters/sullengard_bartender.md) | 100% | 4 | Sullengard |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | description: A little bit of spring in ever sip. Bre… → A little bit of spring in every sip. Br… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_spring_squeeze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_spring_squeeze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_spring_squeeze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_spring_squeeze.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sullengard_spring_squeeze` |
    | Category ID | `drink` |
    | Icon | `items_misc_6:23` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_bartender_dl` |

    Raw data:

    ```json
    {
     "id": "sullengard_spring_squeeze",
     "iconID": "items_misc_6:23",
     "name": "Spring Squeeze",
     "displaytype": "ordinary",
     "category": "drink",
     "description": "A little bit of spring in every sip. Brewed by the Brewere family.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 2,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 1,
        "duration": 4,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
