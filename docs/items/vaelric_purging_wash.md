# ![](../assets/icons/items/items_japozero_467.png){ .sprite } Vaelric's purging wash

*Rare healing item.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_467.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `vaelric_purging_wash` |
| **Category** | Healing item |
| **Rarity** | Rare |
| **Base value** | 419 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A potent alchemical wash designed to counteract corrosive slime. Pour it over yourself to dissolve the toxic residue and cleanse your body.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 5 to 15 |
| On self | Corrosive slime (90% chance) |

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

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_purging_wash.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_purging_wash.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_purging_wash.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=vaelric_purging_wash.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `vaelric_purging_wash` |
    | Category ID | `healing` |
    | Icon | `items_japozero:467` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `mg_vaelric_dl` |

    Raw data:

    ```json
    {
     "id": "vaelric_purging_wash",
     "iconID": "items_japozero:467",
     "name": "Vaelric's purging wash",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 419,
     "category": "healing",
     "description": "A potent alchemical wash designed to counteract corrosive slime. Pour it over yourself to dissolve the toxic residue and cleanse your body.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 15
      },
      "conditionsSource": [
       {
        "condition": "slime",
        "chance": "90"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
