---
description: "Hat of the protector is a rare headwear, cloth in Andor's Trail (Attack damage 0 to 2, Max HP -5, Move cost -1, Attack chance 0). How to get it: shops."
---

# ![](../assets/icons/items/items_japozero_96.png){ .sprite } Hat of the protector

*Rare headwear, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_96.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `hat_of_protector` |
| **Category** | Headwear, cloth |
| **Slot** | head |
| **Rarity** | Rare |
| **Base value** | 4,496 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 to 2 |
| Max HP | -5 |
| Move cost | -1 |
| Attack chance | 0 |
| Critical skill | 0 |
| Block chance | +10 |
| Damage resistance | +2 |
| Critical multiplier | 0.0 |

### On kill

| Stat | Value |
|---|---|
| On self | [Courage](../conditions/courage.md) (magnitude 1, 3 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Kealwea](../monsters/sullengard_priest.md) (Sullengard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hat_of_protector.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hat_of_protector.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hat_of_protector.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hat_of_protector.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `hat_of_protector` |
    | Category ID | `hd_cloth` |
    | Icon | `items_japozero:96` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_kealwea_dl` |

    Raw data:

    ```json
    {
     "id": "hat_of_protector",
     "iconID": "items_japozero:96",
     "name": "Hat of the protector",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 4496,
     "category": "hd_cloth",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 2
      },
      "increaseMaxHP": -5,
      "increaseMoveCost": -1,
      "increaseAttackChance": 0,
      "increaseCriticalSkill": 0,
      "increaseBlockChance": 10,
      "increaseDamageResistance": 2,
      "setCriticalMultiplier": 0.0
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "courage",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
