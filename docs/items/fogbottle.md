# ![](../assets/icons/items/items_consumables_58.png){ .sprite } Fog in a bottle

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_58.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `fogbottle` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 17 gold |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

> An angry-looking fog contained within a bottle. Though it may be defeated, it always retreats back into the vessel.

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 0 to 1 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Wobbling foggerlump](../monsters/feygard_fogmonster1.md) | 100% | 1-2 | Guynmart Castle |
| [Icy foggerlump](../monsters/feygard_fogmonster2.md) | 100% | 1-2 | swamp2 |
| [Wet foggerlump](../monsters/feygard_fogmonster3.md) | 100% | 1-2 | swamp4 |
| [Dizzy foggerlump](../monsters/feygard_fogmonster4.md) | 100% | 1-2 | swamp5 |
| [Dense foggerlump](../monsters/feygard_fogmonster5.md) | 100% | 1-2 | swamp6 |
| [Shiny Foggerlump](../monsters/feygard_fogmonster9.md) | 100% | 1-2 | Guynmart Castle |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fogbottle.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fogbottle.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fogbottle.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fogbottle.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `fogbottle` |
    | Category ID | `pot` |
    | Icon | `items_consumables:58` |
    | Defined in | `res/raw/itemlist_next_release.json` |
    | Loot tables containing it | `feygard_fogmonster` |

    Raw data:

    ```json
    {
     "id": "fogbottle",
     "iconID": "items_consumables:58",
     "name": "Fog in a bottle",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 17,
     "category": "pot",
     "description": "An angry-looking fog contained within a bottle. Though it may be defeated, it always retreats back into the vessel.",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
