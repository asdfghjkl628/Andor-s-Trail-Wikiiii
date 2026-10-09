---
description: "Serpent meat is a ordinary food in Andor's Trail. How to get it: monster drops."
---

# ![](../assets/icons/items/items_misc_6_25.png){ .sprite } Serpent meat

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_25.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `serpent_meat` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | removes [Blindness](../conditions/blindness.md); [Sustenance](../conditions/food.md) (magnitude 2, 5 rounds); [Food-poisoning](../conditions/foodp.md) (magnitude 2, 8 rounds, 8% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Cave worm](../monsters/cave_worm.md) | 70% | 1-2 | Laerothcave 1, Laerothtomb 0 |
| [Vicious cave worm](../monsters/cave_worm_vicious.md) | 70% | 1-2 | Laerothcave 1, Laerothtomb 0 |
| [Aggressive spitting serpent](../monsters/spit_serpent_3.md) | 15% | 1 | Lake Laeroth |
| [Spitting serpent](../monsters/spit_serpent_1.md) | 10% | 1 | Lake Laeroth |
| [Young spitting serpent](../monsters/spit_serpent_2.md) | 5% | 1 | Lake Laeroth |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=serpent_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=serpent_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=serpent_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=serpent_meat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `serpent_meat` |
    | Category ID | `food` |
    | Icon | `items_misc_6:25` |
    | Defined in | `res/raw/itemlist_laeroth.json` |
    | Loot tables containing it | `serpent_1`, `serpent_2`, `serpent_3`, `cave_worm` |

    Raw data:

    ```json
    {
     "id": "serpent_meat",
     "iconID": "items_misc_6:25",
     "name": "Serpent meat",
     "displaytype": "ordinary",
     "category": "food",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "blindness",
        "chance": "100"
       },
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "foodp",
        "magnitude": 2,
        "duration": 8,
        "chance": "8"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
