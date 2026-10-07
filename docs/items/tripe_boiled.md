---
description: "Boiled tripe is a ordinary food in Andor's Trail. How to get it: shops. This looks disgusting, but cheap."
---

# ![](../assets/icons/items/items_rijackson_1_14.png){ .sprite } Boiled tripe

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_rijackson_1_14.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `tripe_boiled` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 8 gold |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

> This looks disgusting, but cheap.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Sustenance (magnitude 1, 9 rounds, 100% chance); Nausea (magnitude 2, 3 rounds, 3% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Waitress](../monsters/brv_tavern_west_waitress.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=tripe_boiled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=tripe_boiled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=tripe_boiled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=tripe_boiled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `tripe_boiled` |
    | Category ID | `food` |
    | Icon | `items_rijackson_1:14` |
    | Defined in | `res/raw/itemlist_brimhaven.json` |
    | Loot tables containing it | `brv_tavern_west_waitress` |

    Raw data:

    ```json
    {
     "id": "tripe_boiled",
     "iconID": "items_rijackson_1:14",
     "name": "Boiled tripe",
     "hasManualPrice": 1,
     "baseMarketCost": 8,
     "category": "food",
     "description": "This looks disgusting, but cheap.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 1,
        "duration": 9,
        "chance": "100"
       },
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 3,
        "chance": "3"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
