# ![](../assets/icons/items/items_japozero_248.png){ .sprite } Ring of poison immunity

*Extraordinary ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_248.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ring_antipoison` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Extraordinary |
| **Base value** | 23,000 gold |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Grants | Weak Poison (magnitude -99); Irdegh poison (magnitude -99); Venom (magnitude -99) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Shop Owner](../monsters/brv_shop_owner.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.7.15](../versions/0.7.15.md) | equipEffect: {"addedConditions": [{"condition": "poi… → {"addedConditions": [{"condition": "poi… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_antipoison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_antipoison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_antipoison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_antipoison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ring_antipoison` |
    | Category ID | `ring` |
    | Icon | `items_japozero:248` |
    | Defined in | `res/raw/itemlist_brimhaven.json` |
    | Loot tables containing it | `brv_jewelery` |

    Raw data:

    ```json
    {
     "id": "ring_antipoison",
     "iconID": "items_japozero:248",
     "name": "Ring of poison immunity",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 23000,
     "category": "ring",
     "equipEffect": {
      "addedConditions": [
       {
        "condition": "poison_weak",
        "magnitude": -99
       },
       {
        "condition": "poison_irdegh",
        "magnitude": -99
       },
       {
        "condition": "venom",
        "magnitude": -99
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
