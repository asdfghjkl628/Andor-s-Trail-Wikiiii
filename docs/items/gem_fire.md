# ![](../assets/icons/items/items_misc_5_26.png){ .sprite } Gem of warmth

*Extraordinary gem.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_26.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `gem_fire` |
| **Category** | Gem |
| **Rarity** | Extraordinary |
| **Base value** | 25 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Young ash spawn](../monsters/ash5.md) | 0.1% | 1 | Charwood |
| [Ash spawn](../monsters/ash6.md) | 0.1% | 1 | Charwood |
| [Tough ash spawn](../monsters/ash7.md) | 0.1% | 1 | lostmine5, lostmine6, lostmine7 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Road rondel](../monsters/road_rondel_blocker.md) ([wayto_feygard_duleian_1](../maps/wayto_feygard_duleian_1.md)) | – | must be carried (1×) | “Step aside before I am forced to reunite you two.” |
| [Local artist](../monsters/stoutford_artist.md) ([stoutford_artist](../maps/stoutford_artist.md)) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-58) | must be carried (1×) | “Oh, but I can stay.” |
| walking into a blocked passage on [brightport_bakery1](../maps/brightport_bakery1.md) | – | must be carried (1×) | “N” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | displaytype added (extraordinary) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gem_fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gem_fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gem_fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gem_fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `gem_fire` |
    | Category ID | `gem` |
    | Icon | `items_misc_5:26` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `ashsp` |

    Raw data:

    ```json
    {
     "id": "gem_fire",
     "iconID": "items_misc_5:26",
     "name": "Gem of warmth",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 25,
     "category": "gem"
    }
    ```


<small>Data from v0.8.18</small>
