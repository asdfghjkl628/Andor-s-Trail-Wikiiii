---
description: "Potion of heightened senses is a rare potion in Andor's Trail. How to get it: shops."
---

# ![](../assets/icons/items/items_tometik1_56.png){ .sprite } Potion of heightened senses

*Rare potion.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_tometik1_56.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `pot_senses` |
| **Category** | Potion |
| **Rarity** | Rare |
| **Base value** | 1,570 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Heightened senses](../conditions/sense_1.md) (magnitude 3, 20 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Lodar](../monsters/lodar.md) (Prim)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Drunkard](../monsters/drunkard.md) ([Fallhaven north-west](../maps/fallhaven_nw.md)) | – | must be carried (1×) | “No, I am here to give you something.” |
| [Drunkard](../monsters/drunkard.md) ([Fallhaven north-west](../maps/fallhaven_nw.md)) | [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-55) | handed over (1×) | “No. I have a potion that will make you recover. Shannal's ghost has asked that y” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | When used, condition on self: [Heightened senses](../conditions/sense_1.md) (magnitude 3, 20 rounds) → (magnitude 3, 20 rounds) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_senses.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_senses.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_senses.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_senses.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `pot_senses` |
    | Category ID | `pot` |
    | Icon | `items_tometik1:56` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_lodar` |

    Raw data:

    ```json
    {
     "id": "pot_senses",
     "iconID": "items_tometik1:56",
     "name": "Potion of heightened senses",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 1570,
     "category": "pot",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "sense_1",
        "magnitude": 3,
        "duration": 20,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
