---
description: "Feydelight is a extraordinary food in Andor's Trail. How to get it: quests and dialogue. A popular, but rare, holiday Feygardian treat filled with fig fruit. It provides a rush of sweetness and has been known to cause a burst of energy."
---

# ![](../assets/icons/items/items_newb_840.png){ .sprite } Feydelight

*Extraordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_840.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `feydelight` |
| **Category** | Food |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

> A popular, but rare, holiday Feygardian treat filled with fig fruit. It provides a rush of sweetness and has been known to cause a burst of energy.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Sustenance (magnitude 3, 35 rounds, 100% chance); Haste (magnitude 1, 15 rounds, 100% chance); Sweet tooth (magnitude 1, 10 rounds, 25% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) during [A Feygard delicacy](../quests/feygard_delicacy.md#stage-8) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feydelight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feydelight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feydelight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feydelight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `feydelight` |
    | Category ID | `food` |
    | Icon | `items_newb:840` |
    | Defined in | `res/raw/itemlist_feygard_1.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "feydelight",
     "iconID": "items_newb:840",
     "name": "Feydelight",
     "displaytype": "extraordinary",
     "category": "food",
     "description": "A popular, but rare, holiday Feygardian treat filled with fig fruit. It provides a rush of sweetness and has been known to cause a burst of energy.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 35,
        "chance": "100"
       },
       {
        "condition": "haste",
        "magnitude": 1,
        "duration": 15,
        "chance": "100"
       },
       {
        "condition": "sweet_tooth",
        "magnitude": 1,
        "duration": 10,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
