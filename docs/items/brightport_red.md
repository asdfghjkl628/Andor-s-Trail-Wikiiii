---
description: "Stuffed pepper is a rare food in Andor's Trail. How to get it: quests and dialogue. A traditional Crossglen recipe. Perhaps a bit too spicy."
---

# ![](../assets/icons/items/items_consumables_18.png){ .sprite } Stuffed pepper

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_18.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `brightport_red` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 66 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> A traditional Crossglen recipe. Perhaps a bit too spicy.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Ablaze (magnitude 1, 2 rounds, 30% chance); Sustenance (magnitude 5, 10 rounds, 100% chance); Sated (magnitude 1, 1 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Crescenzio](../monsters/brightport_chef2.md) ([brightport_bakery1](../maps/brightport_bakery1.md)) (1×)
- From [Crescenzio](../monsters/brightport_chef2.md) ([brightport_bakery1](../maps/brightport_bakery1.md)) (5×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_red.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_red.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_red.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_red.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brightport_red` |
    | Category ID | `food` |
    | Icon | `items_consumables:18` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "brightport_red",
     "iconID": "items_consumables:18",
     "name": "Stuffed pepper",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 66,
     "category": "food",
     "description": "A traditional Crossglen recipe. Perhaps a bit too spicy.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "fire",
        "magnitude": 1,
        "duration": 2,
        "chance": "30"
       },
       {
        "condition": "food",
        "magnitude": 5,
        "duration": 10,
        "chance": "100"
       },
       {
        "condition": "sated",
        "magnitude": 1,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
