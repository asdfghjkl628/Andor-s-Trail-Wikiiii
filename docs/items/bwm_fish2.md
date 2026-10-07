---
description: "Cooked inkyfish is a ordinary food in Andor's Trail. How to get it: containers. Typical Blackwater mountain food."
---

# ![](../assets/icons/items/items_omi2_22.png){ .sprite } Cooked inkyfish

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_omi2_22.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bwm_fish2` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 80 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> Typical Blackwater mountain food.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 0 to 5 |
| On self | Sustenance (magnitude 3, 9 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [elm_2f_2](../maps/elm_2f_2.md#container-1) (container 2, 33.3333%)
- [elm_mine5](../maps/elm_mine5.md#container-0) (container 1, 33.3333%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_fish2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_fish2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_fish2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_fish2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bwm_fish2` |
    | Category ID | `food` |
    | Icon | `items_omi2:22` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm_drop1`, `elm2f2_chest` |

    Raw data:

    ```json
    {
     "id": "bwm_fish2",
     "iconID": "items_omi2:22",
     "name": "Cooked inkyfish",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 80,
     "category": "food",
     "description": "Typical Blackwater mountain food.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 5
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 9,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
