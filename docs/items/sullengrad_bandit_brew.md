---
description: "Bandit's Brew is a ordinary drink in Andor's Trail. How to get it: monster drops. A Thieve's guild original, produced by the Brueria family. It was named in their honor for years of reliable service to Sullengard."
---

# ![](../assets/icons/items/items_misc_6_23.png){ .sprite } Bandit's Brew

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_23.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sullengrad_bandit_brew` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> A Thieve's guild original, produced by the Brueria family. It was named in their honor for years of reliable service to Sullengard.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 5 |
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 3 rounds); [Intoxicated](../conditions/intoxicated.md) (magnitude 1, 3 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Oakleigh](../monsters/sullengard_bartender.md) | 100% | 5-7 | Sullengard |
| [Highwayman](../monsters/highwayman.md#v-sullengard_highwayman) | 10% | 1 | way_to_sullengard_east9 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_bandit_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_bandit_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_bandit_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sullengrad_bandit_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sullengrad_bandit_brew` |
    | Category ID | `drink` |
    | Icon | `items_misc_6:23` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_bartender_dl`, `sullengard_highwayman_drop` |

    Raw data:

    ```json
    {
     "id": "sullengrad_bandit_brew",
     "iconID": "items_misc_6:23",
     "name": "Bandit's Brew",
     "displaytype": "ordinary",
     "category": "drink",
     "description": "A Thieve's guild original, produced by the Brueria family. It was named in their honor for years of reliable service to Sullengard.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 5
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 3,
        "chance": "100"
       },
       {
        "condition": "intoxicated",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
