---
description: "Small vial of mountain water is a ordinary potion in Andor's Trail. How to get it: monster drops, quests and dialogue. Picked up directly from the heart of the mountain."
---

# ![](../assets/icons/items/items_omi2_14.png){ .sprite } Small vial of mountain water

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_omi2_14.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bwm_water0` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> Picked up directly from the heart of the mountain.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 5 to 10 |
| On self | [Satiety](../conditions/satiety.md) (magnitude 1, 3 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Contaminated miner's skeleton](../monsters/elm_miner3.md) | 5% | 1 | Elm 5f 1, Elm 5f 2, Elm 4f 1 |
| [Prim guard skeleton](../monsters/elm_miner4.md) | 5% | 1 | Elm 5f 1, Elm 5f 2, Elm 4f 1 |

### Quest & dialogue rewards

- From walking into a blocked passage on [Elm 2f 1](../maps/elm_2f_1.md) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_water0.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_water0.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_water0.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_water0.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bwm_water0` |
    | Category ID | `pot` |
    | Icon | `items_omi2:14` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm_miner2` |

    Raw data:

    ```json
    {
     "id": "bwm_water0",
     "iconID": "items_omi2:14",
     "name": "Small vial of mountain water",
     "displaytype": "ordinary",
     "category": "pot",
     "description": "Picked up directly from the heart of the mountain.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 10
      },
      "conditionsSource": [
       {
        "condition": "satiety",
        "magnitude": 1,
        "duration": 3,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
