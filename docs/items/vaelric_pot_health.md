# ![](../assets/icons/items/items_newb_740.png){ .sprite } Vaelric's elixir of vitality

*Rare potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_740.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `vaelric_pot_health` |
| **Category** | Potion |
| **Rarity** | Rare |
| **Base value** | 90 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A rare and refined potion of health that not only restores a greater amount of vitality instantly but also accelerates natural healing for a short duration.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 20 to 30 |
| On self | Regeneration (magnitude 5, 6 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Vaelric](../monsters/vaelric.md) (galmore_17_house)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_pot_health.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_pot_health.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_pot_health.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_pot_health.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `vaelric_pot_health` |
    | Category ID | `pot` |
    | Icon | `items_newb:740` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `mg_vaelric_dl` |

    Raw data:

    ```json
    {
     "id": "vaelric_pot_health",
     "iconID": "items_newb:740",
     "name": "Vaelric's elixir of vitality",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 90,
     "category": "pot",
     "description": "A rare and refined potion of health that not only restores a greater amount of vitality instantly but also accelerates natural healing for a short duration.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 20,
       "max": 30
      },
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 5,
        "duration": 6,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
