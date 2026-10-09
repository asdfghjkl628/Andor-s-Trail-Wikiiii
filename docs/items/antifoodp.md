---
description: "Antidote is a ordinary potion in Andor's Trail. How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_consumables_67.png){ .sprite } Antidote

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_67.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `antifoodp` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 79 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | removes [Food-poisoning](../conditions/foodp.md) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Potion merchant](../monsters/potion_merchant.md) ([Fallhaven potions](../maps/fallhaven_potions.md)) during [Taste is everything](../quests/antifoodp.md#stage-35) (100%)
- From [Potion merchant](../monsters/potion_merchant.md) ([Fallhaven potions](../maps/fallhaven_potions.md)) (100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | When used, condition on self: [Food-poisoning](../conditions/foodp.md) (magnitude -99) → (magnitude -99) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=antifoodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=antifoodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=antifoodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=antifoodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `antifoodp` |
    | Category ID | `pot` |
    | Icon | `items_consumables:67` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `antifoodp`, `antifoodp_x5`, `antifoodp_x10` |

    Raw data:

    ```json
    {
     "id": "antifoodp",
     "iconID": "items_consumables:67",
     "name": "Antidote",
     "hasManualPrice": 1,
     "baseMarketCost": 79,
     "category": "pot",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "foodp",
        "magnitude": -99,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
