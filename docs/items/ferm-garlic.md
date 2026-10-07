---
description: "Fermented garlic is a rare food in Andor's Trail. How to get it: shops. Hopefully this tastes better than it smells!"
---

# ![](../assets/icons/items/items_rijackson_1_2.png){ .sprite } Fermented garlic

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_rijackson_1_2.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ferm-garlic` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 25 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> Hopefully this tastes better than it smells!

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | removes [Food-poisoning](../conditions/foodp.md); [Nausea](../conditions/nausea.md) (magnitude 1, 5 rounds); [Sustenance](../conditions/food.md) (magnitude 1, 2 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Cadoren](../monsters/stoutford_cook.md) (Stoutford)
- [Horfael](../monsters/ratdom_rat_pub_owner.md) (Pub)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | When used, condition on self: [Sustenance](../conditions/food.md) (magnitude 1, 1 rounds) → (magnitude 1, 2 rounds) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ferm-garlic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ferm-garlic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ferm-garlic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ferm-garlic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ferm-garlic` |
    | Category ID | `food` |
    | Icon | `items_rijackson_1:2` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cadoren`, `ratdom_rat_pub_owner` |

    Raw data:

    ```json
    {
     "id": "ferm-garlic",
     "iconID": "items_rijackson_1:2",
     "name": "Fermented garlic",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 25,
     "category": "food",
     "description": "Hopefully this tastes better than it smells!",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "foodp",
        "magnitude": -99,
        "chance": "100"
       },
       {
        "condition": "nausea",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "food",
        "magnitude": 1,
        "duration": 2,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
