---
description: "Specially peppered lamb meat is a extraordinary food in Andor's Trail. How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_japozero_517.png){ .sprite } Specially peppered lamb meat

*Extraordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_517.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `lamb_meat2` |
| **Category** | Food |
| **Rarity** | Extraordinary |
| **Base value** | 310 gold |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 10 |
| On self | [Sustenance](../conditions/food.md) (magnitude 6, 10 rounds); [Thirst](../conditions/thirst.md) (magnitude 1, 12 rounds); [Minor berserker rage](../conditions/rage_minor.md) (magnitude 2, 11 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) during [It makes no fence](../quests/tunlon_fence.md#stage-250) (100%)
- From [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `lamb_meat2` |
    | Category ID | `food` |
    | Icon | `items_japozero:517` |
    | Defined in | `res/raw/itemlist_bwmfill.json` |
    | Loot tables containing it | `tunlon_quest` |

    Raw data:

    ```json
    {
     "id": "lamb_meat2",
     "iconID": "items_japozero:517",
     "name": "Specially peppered lamb meat",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 310,
     "category": "food",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 10,
       "max": 10
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 6,
        "duration": 10,
        "chance": "100"
       },
       {
        "condition": "thirst",
        "magnitude": 1,
        "duration": 12,
        "chance": "100"
       },
       {
        "condition": "rage_minor",
        "magnitude": 2,
        "duration": 11,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
