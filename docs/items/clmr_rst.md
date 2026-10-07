---
description: "Rusty claymore is a ordinary two-handed sword in Andor's Trail (Attack damage 1 to 6, Max HP +2, Attack cost +7, Attack chance +23). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_3_26.png){ .sprite } Rusty claymore

*Ordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_26.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clmr_rst` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md) |
| **Rarity** | Ordinary |
| **Base value** | 36 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 6 |
| Max HP | +2 |
| Attack cost | +7 |
| Attack chance | +23 |
| Critical skill | +4 |
| Damage resistance | -1 |
| Critical multiplier | 1.2 |
| setNonWeaponDamageModifier | +155 |
| Grants | [Dazed](../conditions/dazed.md) (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Audir](../monsters/audir.md)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | When equipped, critical multiplier: 1.2 → 1.2 |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (155) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_rst.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_rst.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_rst.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_rst.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clmr_rst` |
    | Category ID | `2hsword` |
    | Icon | `items_weapons_3:26` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_audir` |

    Raw data:

    ```json
    {
     "id": "clmr_rst",
     "iconID": "items_weapons_3:26",
     "name": "Rusty claymore",
     "baseMarketCost": 36,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 6
      },
      "increaseMaxHP": 2,
      "increaseAttackCost": 7,
      "increaseAttackChance": 23,
      "increaseCriticalSkill": 4,
      "increaseDamageResistance": -1,
      "setCriticalMultiplier": 1.2,
      "setNonWeaponDamageModifier": 155,
      "addedConditions": [
       {
        "condition": "dazed",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
