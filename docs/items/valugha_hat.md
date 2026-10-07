---
description: "Valugha's shimmering hat is a extraordinary headwear, cloth in Andor's Trail (Attack damage -2, Max HP +3, Move cost -1, Attack chance +15). How to get it: monster drops, quests and dialogue."
---

# ![](../assets/icons/items/items_armours_3_1.png){ .sprite } Valugha's shimmering hat

*Extraordinary headwear, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_3_1.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `valugha_hat` |
| **Category** | Headwear, cloth |
| **Slot** | head |
| **Rarity** | Extraordinary |
| **Base value** | 648 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | -2 |
| Max HP | +3 |
| Move cost | -1 |
| Attack chance | +15 |
| Block chance | -5 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Plaguestrider master](../monsters/plaguesp_13.md) | 0.1% | 1 | waytolake5 |

### Quest & dialogue rewards

- From [Halvor](../monsters/halvor.md) ([blackwater_mountain4](../maps/blackwater_mountain4.md)) during [Surprise?](../quests/halvor_surprise.md#stage-114) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_hat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_hat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_hat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_hat.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `valugha_hat` |
    | Category ID | `hd_cloth` |
    | Icon | `items_armours_3:1` |
    | Defined in | `res/raw/itemlist_v0611_1.json` |
    | Loot tables containing it | `plaguespider_b` |

    Raw data:

    ```json
    {
     "id": "valugha_hat",
     "iconID": "items_armours_3:1",
     "name": "Valugha's shimmering hat",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 648,
     "category": "hd_cloth",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": -2,
       "max": -2
      },
      "increaseMaxHP": 3,
      "increaseMoveCost": -1,
      "increaseAttackChance": 15,
      "increaseBlockChance": -5
     }
    }
    ```


<small>Data from v0.8.18</small>
