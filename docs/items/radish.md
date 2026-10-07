---
description: "Radish is a ordinary food in Andor's Trail. How to get it: shops."
---

# ![](../assets/icons/items/items_consumables_14.png){ .sprite } Radish

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_14.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `radish` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 6 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Sustenance](../conditions/food.md) (magnitude 1, 4 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Potion merchant](../monsters/potion_merchant.md) (Fallhaven)
- [Birgil](../monsters/birgil.md) (Prim)
- [Peasant grandfather](../monsters/brv_old_farmer.md) (Brimhaven)
- [Rosmara](../monsters/rosmara.md) (Wayto feygard duleian 2)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | When used, condition on self: [Sustenance](../conditions/food.md) (magnitude 1, 4 rounds) → (magnitude 1, 4 rounds) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=radish.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=radish.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=radish.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=radish.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `radish` |
    | Category ID | `food` |
    | Icon | `items_consumables:14` |
    | Defined in | `res/raw/itemlist_food.json` |
    | Loot tables containing it | `shop_birgil`, `shop_fallhaven_potions`, `brv_farmer`, `rosmara_dl` |

    Raw data:

    ```json
    {
     "id": "radish",
     "iconID": "items_consumables:14",
     "name": "Radish",
     "hasManualPrice": 1,
     "baseMarketCost": 6,
     "category": "food",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 1,
        "duration": 4,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
