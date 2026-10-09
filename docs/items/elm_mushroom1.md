---
description: "Boletus spelunca is a rare food in Andor's Trail. How to get it: containers. Rare mushroom only found in caves with high humidity and temperature."
---

# ![](../assets/icons/items/items_japozero_501.png){ .sprite } Boletus spelunca

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_501.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `elm_mushroom1` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 191 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> Rare mushroom only found in caves with high humidity and  temperature.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 18 to 20 |
| On self | immunity to [Nausea](../conditions/nausea.md) for 75 rounds; [Sustenance](../conditions/food.md) (magnitude 1, 30 rounds); immunity to [Confusion](../conditions/confusion.md) for 10 rounds (50% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [Elm 2f 2](../maps/elm_2f_2.md#container-0) (container 1, 100%)
- [Elm 4f 3](../maps/elm_4f_3.md#container-0) (container 1, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_mushroom1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_mushroom1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_mushroom1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=elm_mushroom1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `elm_mushroom1` |
    | Category ID | `food` |
    | Icon | `items_japozero:501` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm_mushroom` |

    Raw data:

    ```json
    {
     "id": "elm_mushroom1",
     "iconID": "items_japozero:501",
     "name": "Boletus spelunca",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 191,
     "category": "food",
     "description": "Rare mushroom only found in caves with high humidity and  temperature.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 18,
       "max": 20
      },
      "conditionsSource": [
       {
        "condition": "nausea",
        "magnitude": -99,
        "duration": 75,
        "chance": "100"
       },
       {
        "condition": "food",
        "magnitude": 1,
        "duration": 30,
        "chance": "100"
       },
       {
        "condition": "confusion",
        "magnitude": -99,
        "duration": 10,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
