---
description: "Lowyna's foul brew is a ordinary drink in Andor's Trail. How to get it: shops."
---

# ![](../assets/icons/items/items_tometik1_3.png){ .sprite } Lowyna's foul brew

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_3.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `drink_lowyn1` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 430 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 to 7 |
| On self | Sustenance (magnitude 2, 5 rounds, 100% chance); Intoxicated (magnitude 1, 20 rounds, 100% chance); Intoxicated (magnitude 3, 20 rounds, 30% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Lowyna](../monsters/lowyna.md) (Fallhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | useEffect: {"conditionsSource": [{"chance": 100, "… → {"conditionsSource": [{"chance": "100",… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `drink_lowyn1` |
    | Category ID | `drink` |
    | Icon | `items_tometik1:3` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_lowyna` |

    Raw data:

    ```json
    {
     "id": "drink_lowyn1",
     "iconID": "items_tometik1:3",
     "name": "Lowyna's foul brew",
     "hasManualPrice": 1,
     "baseMarketCost": 430,
     "category": "drink",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 7
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 1,
        "duration": 20,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 3,
        "duration": 20,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
