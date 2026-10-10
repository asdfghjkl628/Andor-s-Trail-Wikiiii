---
description: "Deebo's apple juice is a rare food in Andor's Trail. How to get it: shops. A desireable choice of many Sullengard residence."
---

# ![](../assets/icons/items/items_tometik1_35.png){ .sprite } Deebo's apple juice

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_tometik1_35.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `apple_orchard_juice` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 97 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> A desireable choice of many Sullengard residence.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 12 rounds); immunity to [Vulnerability](../conditions/vulnerability.md) for 2 rounds (30% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Deebo](../monsters/deebo_orchard_deebo.md) (Deebo's Orchard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.5](../versions/0.8.5.md) | Base value (gold): 45 → 97<br>When used, condition on self: added [Vulnerability](../conditions/vulnerability.md) (magnitude -99, 2 rounds, 30% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=apple_orchard_juice.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=apple_orchard_juice.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=apple_orchard_juice.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=apple_orchard_juice.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `apple_orchard_juice` |
    | Category ID | `food` |
    | Icon | `items_tometik1:35` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `deebo_orchard_dl` |

    Raw data:

    ```json
    {
     "id": "apple_orchard_juice",
     "iconID": "items_tometik1:35",
     "name": "Deebo's apple juice",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 97,
     "category": "food",
     "description": "A desireable choice of many Sullengard residence.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 12,
        "chance": "100"
       },
       {
        "condition": "vulnerability",
        "magnitude": -99,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
