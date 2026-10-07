# ![](../assets/icons/items/items_newb_48.png){ .sprite } Armored boots

*Rare footwear, metal (heavy).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_48.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `armored_boots` |
| **Category** | Footwear, metal (heavy) |
| **Slot** | feet |
| **Rarity** | Rare |
| **Base value** | 1,868 gold |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Move cost | +1 |
| Use item cost | 0 |
| Attack cost | +1 |
| Attack chance | -1 |
| Block chance | +14 |

### When hit

| Stat | Value |
|---|---|
| On self | Minor increased defense (magnitude 1, 1 rounds, 3% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [gamjee_well_exit](../maps/gamjee_well_exit.md#container-1) (container 2, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_boots.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_boots.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_boots.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_boots.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `armored_boots` |
    | Category ID | `feet_mtl_hv` |
    | Icon | `items_newb:48` |
    | Defined in | `res/raw/itemlist_feygard_1.json` |
    | Loot tables containing it | `gamjee_well_exit_dl` |

    Raw data:

    ```json
    {
     "id": "armored_boots",
     "iconID": "items_newb:48",
     "name": "Armored boots",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 1868,
     "category": "feet_mtl_hv",
     "equipEffect": {
      "increaseMoveCost": 1,
      "increaseUseItemCost": 0,
      "increaseAttackCost": 1,
      "increaseAttackChance": -1,
      "increaseBlockChance": 14
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "minor_increased_defense",
        "magnitude": 1,
        "duration": 1,
        "chance": "3"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
