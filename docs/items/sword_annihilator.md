---
description: "Sword of the annihilator is a extraordinary two-handed sword in Andor's Trail (Attack damage 5 to 28, Attack cost +13, Attack chance +22, Critical skill +1). How to get it: monster drops."
---

# ![](../assets/icons/items/items_misc_5_42.png){ .sprite } Sword of the annihilator

*Extraordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_42.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sword_annihilator` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 5 to 28 |
| Attack cost | +13 |
| Attack chance | +22 |
| Critical skill | +1 |
| Block chance | -5 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +320 |

### On hit

| Stat | Value |
|---|---|
| On target | Stunned (magnitude 1, 2 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Cave troll leader](../monsters/cave_troll_5.md) | 100% | 1 | lakecave2 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 22, "increaseA… → {"increaseAttackChance": 22, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_annihilator.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_annihilator.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_annihilator.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_annihilator.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sword_annihilator` |
    | Category ID | `2hsword` |
    | Icon | `items_misc_5:42` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `cave_troll_4` |

    Raw data:

    ```json
    {
     "id": "sword_annihilator",
     "iconID": "items_misc_5:42",
     "name": "Sword of the annihilator",
     "displaytype": "extraordinary",
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 5,
       "max": 28
      },
      "increaseAttackCost": 13,
      "increaseAttackChance": 22,
      "increaseCriticalSkill": 1,
      "increaseBlockChance": -5,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 320
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
