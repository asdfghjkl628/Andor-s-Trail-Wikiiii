---
description: "Cave fern is a rare food in Andor's Trail. How to get it: containers. A fern inside a cave is something unusual, not seen every day."
---

# ![](../assets/icons/items/items_japozero_579.png){ .sprite } Cave fern

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_japozero_579.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `elm_fern` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 132 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> A fern inside a cave is something unusual, not seen every day.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 3 to 12 |
| On self | immunity to [Putrefaction](../conditions/putrefaction.md) for 10 rounds |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [Elm 4f 4](../maps/elm_4f_4.md#container-0) (container 1, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.7.17](../versions/0.7.17.md) | Description text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_fern.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_fern.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_fern.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_fern.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `elm_fern` |
    | Category ID | `food` |
    | Icon | `items_japozero:579` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm4f5_herbs` |

    Raw data:

    ```json
    {
     "id": "elm_fern",
     "iconID": "items_japozero:579",
     "name": "Cave fern",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 132,
     "category": "food",
     "description": "A fern inside a cave is something unusual, not seen every day.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 12
      },
      "conditionsSource": [
       {
        "condition": "putrefaction",
        "magnitude": -99,
        "duration": 10,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
