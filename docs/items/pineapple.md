# ![](../assets/icons/items/items_consumables_11.png){ .sprite } Pineapple

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_11.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `pineapple` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 211 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A spiky golden fruit with sweet, rejuvenating juice, the Pineapple restores health when consumed, its vibrant flavor said to invigorate the soul.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 to 5 |
| On self | Sustenance (magnitude 5, 8 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [mt_galmore_railhouse](../maps/mt_galmore_railhouse.md#container-0) (container 1, 100%), Mt. Galmore


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pineapple.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pineapple.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pineapple.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pineapple.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `pineapple` |
    | Category ID | `food` |
    | Icon | `items_consumables:11` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `mt_galmore_tropics_treasure` |

    Raw data:

    ```json
    {
     "id": "pineapple",
     "iconID": "items_consumables:11",
     "name": "Pineapple",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 211,
     "category": "food",
     "description": "A spiky golden fruit with sweet, rejuvenating juice, the Pineapple restores health when consumed, its vibrant flavor said to invigorate the soul.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 5
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 5,
        "duration": 8,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
