# ![](../assets/icons/items/items_tometik1_9.png){ .sprite } Dark Beer Sour

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_9.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sullengard_dark_beer_sour` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> Not for the faint of heart, but the Bruyere family takes pride in it.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 10 to 15 |
| On self | Sustenance (magnitude 2, 3 rounds, 100% chance); Intoxicated (magnitude 2, 5 rounds, 70% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Oakleigh](../monsters/sullengard_bartender.md) | 100% | 10-12 | Sullengard |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.18](../versions/0.8.18.md) | category: food → drink |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_dark_beer_sour.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_dark_beer_sour.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_dark_beer_sour.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengard_dark_beer_sour.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sullengard_dark_beer_sour` |
    | Category ID | `drink` |
    | Icon | `items_tometik1:9` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_bartender_dl` |

    Raw data:

    ```json
    {
     "id": "sullengard_dark_beer_sour",
     "iconID": "items_tometik1:9",
     "name": "Dark Beer Sour",
     "displaytype": "ordinary",
     "category": "drink",
     "description": "Not for the faint of heart, but the Bruyere family takes pride in it.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 10,
       "max": 15
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 3,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 2,
        "duration": 5,
        "chance": "70"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
