---
description: "Rat's artifact is a extraordinary food in Andor's Trail. How to get it: quests and dialogue. A hard, dry cheese wheel that seems to last almost forever."
---

# ![](../assets/icons/items/items_consumables_23.png){ .sprite } Rat's artifact

*Extraordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_23.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ratdom_artefact` |
| **Category** | Food |
| **Rarity** | Extraordinary |
| **Base value** | 3,000 gold |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

> A hard, dry cheese wheel that seems to last almost forever.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Sustenance (magnitude 2, 400 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) during [Yellow is it](../quests/ratdom_quest.md#stage-950) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) | [Yellow is it](../quests/ratdom_quest.md#stage-948) | must be carried (1×) | “(automatic)” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ratdom_artefact.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ratdom_artefact.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ratdom_artefact.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ratdom_artefact.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ratdom_artefact` |
    | Category ID | `food` |
    | Icon | `items_consumables:23` |
    | Defined in | `res/raw/itemlist_ratdom.json` |
    | Loot tables containing it | `ratdom_artefact` |

    Raw data:

    ```json
    {
     "id": "ratdom_artefact",
     "iconID": "items_consumables:23",
     "name": "Rat's artifact",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 3000,
     "category": "food",
     "description": "A hard, dry cheese wheel that seems to last almost forever.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 400,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
