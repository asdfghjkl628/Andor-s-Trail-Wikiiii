---
description: "Blue cheese is a ordinary food in Andor's Trail. How to get it: shops, quests and dialogue. It looks like moldy cheese."
---

# ![](../assets/icons/items/items_rijackson_1_5.png){ .sprite } Blue cheese

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_rijackson_1_5.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `cheese_blue` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 45 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> It looks like moldy cheese.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 4 rounds) |

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
| [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) | – | handed over (1×) | “Starving? I have some moldy blue cheese for you here.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_blue.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_blue.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_blue.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cheese_blue.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `cheese_blue` |
    | Category ID | `food` |
    | Icon | `items_rijackson_1:5` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cadoren` |

    Raw data:

    ```json
    {
     "id": "cheese_blue",
     "iconID": "items_rijackson_1:5",
     "name": "Blue cheese",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 45,
     "category": "food",
     "description": "It looks like moldy cheese.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 4,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
