---
description: "Goat cheese is a ordinary food in Andor's Trail. How to get it: shops, quests and dialogue."
---

# ![](../assets/icons/items/items_japozero_511.png){ .sprite } Goat cheese

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_511.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `cheese_goat` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 50 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Sustenance (magnitude 2, 5 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Cadoren](../monsters/stoutford_cook.md) (Stoutford)

### Quest & dialogue rewards

- From [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| walking into a blocked passage on [ratdom_maze_624](../maps/ratdom_maze_624.md) | – | handed over (1×) | “(automatic)” |
| [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) | – | handed over (1×) | “Starving? I have some goat cheese for you here. It smells only slightly.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_goat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_goat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_goat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_goat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `cheese_goat` |
    | Category ID | `food` |
    | Icon | `items_japozero:511` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cadoren` |

    Raw data:

    ```json
    {
     "id": "cheese_goat",
     "iconID": "items_japozero:511",
     "name": "Goat cheese",
     "hasManualPrice": 1,
     "baseMarketCost": 50,
     "category": "food",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
