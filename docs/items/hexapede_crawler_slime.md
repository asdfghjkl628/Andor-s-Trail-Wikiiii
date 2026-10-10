---
description: "Hexapede crawler slime is a ordinary potion in Andor's Trail. How to get it: monster drops. Provides temporary immunity to Rootsnare, but at a cost."
---

# ![](../assets/icons/items/items_newb_760.png){ .sprite } Hexapede crawler slime

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_newb_760.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `hexapede_crawler_slime` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

> Provides temporary immunity to Rootsnare, but at a cost.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | immunity to [Rootsnare](../conditions/rootsnare.md) for 5 rounds; [Bad taste](../conditions/bad_taste.md) (magnitude 2, 5 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Hexapede crawler](../monsters/hexapede_crawler.md) | 8% | 1 | Flagstone Prison |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hexapede_crawler_slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hexapede_crawler_slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hexapede_crawler_slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hexapede_crawler_slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `hexapede_crawler_slime` |
    | Category ID | `pot` |
    | Icon | `items_newb:760` |
    | Defined in | `res/raw/itemlist_mt_galmore.json` |
    | Loot tables containing it | `hexapede_crawler_dl` |

    Raw data:

    ```json
    {
     "id": "hexapede_crawler_slime",
     "iconID": "items_newb:760",
     "name": "Hexapede crawler slime",
     "displaytype": "ordinary",
     "category": "pot",
     "description": "Provides temporary immunity to Rootsnare, but at a cost.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "rootsnare",
        "magnitude": -99,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "bad_taste",
        "magnitude": 2,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
