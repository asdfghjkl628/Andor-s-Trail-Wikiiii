# ![](../assets/icons/items/items_newb_686.png){ .sprite } Leech

*Ordinary edible animal part.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_686.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `leech_usable` |
| **Category** | Edible animal part |
| **Rarity** | Ordinary |
| **Base value** | 10 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A valuable tool for healing bleeding wounds, thanks to Vaelric's teachings.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Bleeding wound (magnitude -99, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Swamp lizard](../monsters/swamp_lizard_leech.md) | 5% | 1-2 | galmore_18, galmore_28, galmore_38 |
| [Bog eel](../monsters/bog_eel_leech.md) | 5% | 1-2 | galmore_18, galmore_28, galmore_38 |

### Quest & dialogue rewards

- From [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) during [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59) (1×)
- From stepping on a trigger on [galmore_17_house](../maps/galmore_17_house.md) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=leech_usable.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=leech_usable.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=leech_usable.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=leech_usable.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `leech_usable` |
    | Category ID | `animal_e` |
    | Icon | `items_newb:686` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `swamp_lizard_leetch_dl`, `swamp_eel_leech_dl` |

    Raw data:

    ```json
    {
     "id": "leech_usable",
     "iconID": "items_newb:686",
     "name": "Leech",
     "hasManualPrice": 1,
     "baseMarketCost": 10,
     "category": "animal_e",
     "description": "A valuable tool for healing bleeding wounds, thanks to Vaelric's teachings.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "bleeding_wound",
        "magnitude": -99,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
