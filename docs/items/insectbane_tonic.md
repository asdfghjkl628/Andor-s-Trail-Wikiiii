---
description: "Insectbane tonic is a rare potion in Andor's Trail. How to get it: quests and dialogue. A thick herbal brew that fortifies the body against insect-borne afflictions."
---

# ![](../assets/icons/items/items_tometik1_31.png){ .sprite } Insectbane tonic

*Rare potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_31.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `insectbane_tonic` |
| **Category** | Potion |
| **Rarity** | Rare |
| **Base value** | 480 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A thick herbal brew that fortifies the body against insect-borne afflictions.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Insect contagion (magnitude -99, 100% chance); Insect contagion (magnitude -99, 15 rounds, 100% chance); Bad taste (magnitude 10, 1 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) (10×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=insectbane_tonic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=insectbane_tonic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=insectbane_tonic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=insectbane_tonic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `insectbane_tonic` |
    | Category ID | `pot` |
    | Icon | `items_tometik1:31` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "insectbane_tonic",
     "iconID": "items_tometik1:31",
     "name": "Insectbane tonic",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 480,
     "category": "pot",
     "description": "A thick herbal brew that fortifies the body against insect-borne afflictions.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "contagion",
        "magnitude": -99,
        "chance": "100"
       },
       {
        "condition": "contagion",
        "magnitude": -99,
        "duration": 15,
        "chance": "100"
       },
       {
        "condition": "bad_taste",
        "magnitude": 10,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
