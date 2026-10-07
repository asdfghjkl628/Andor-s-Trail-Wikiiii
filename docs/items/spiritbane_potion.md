---
description: "Spiritbane potion is a rare potion in Andor's Trail. How to get it: monster drops. A vial of thick, black liquid that smells faintly of sulfur that when consumned will provide temporary immunity to some physical ailments"
---

# ![](../assets/icons/items/items_newb_757.png){ .sprite } Spiritbane potion

*Rare potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_757.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `spiritbane_potion` |
| **Category** | Potion |
| **Rarity** | Rare |
| **Base value** | 1,906 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A vial of thick, black liquid that smells faintly of sulfur that when consumned will provide temporary immunity to some physical ailments

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 10 to 50 |
| On self | Concussion (magnitude -99, 6 rounds, 100% chance); Internal bleeding (magnitude -99, 6 rounds, 100% chance); Fracture (magnitude -99, 6 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Dark spirit](../monsters/crossglen_dark_spirit.md) | 100% | 1 | Crossglen |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spiritbane_potion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spiritbane_potion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spiritbane_potion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spiritbane_potion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `spiritbane_potion` |
    | Category ID | `pot` |
    | Icon | `items_newb:757` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `crossglen_dark_spirit_dl` |

    Raw data:

    ```json
    {
     "id": "spiritbane_potion",
     "iconID": "items_newb:757",
     "name": "Spiritbane potion",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 1906,
     "category": "pot",
     "description": "A vial of thick, black liquid that smells faintly of sulfur that when consumned will provide temporary immunity to some physical ailments",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 10,
       "max": 50
      },
      "conditionsSource": [
       {
        "condition": "concussion",
        "magnitude": -99,
        "duration": 6,
        "chance": "100"
       },
       {
        "condition": "crit1",
        "magnitude": -99,
        "duration": 6,
        "chance": "100"
       },
       {
        "condition": "crit2",
        "magnitude": -99,
        "duration": 6,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
