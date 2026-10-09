---
description: "Olwyn's curse is a rare warhammer in Andor's Trail (Attack damage 10 to 17, Attack cost +8, Attack chance +14, Block chance -7). How to get it: monster drops."
---

# ![](../assets/icons/items/items_misc_5_36.png){ .sprite } Olwyn's curse

*Rare warhammer.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_36.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `hmr_olwyns` |
| **Category** | Warhammer |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Rare |
| **Base value** | 2,502 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 10 to 17 |
| Attack cost | +8 |
| Attack chance | +14 |
| Block chance | -7 |
| Damage resistance | -1 |
| setNonWeaponDamageModifier | +320 |
| Grants | [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Tiqui](../monsters/tiqui.md) | 100% | 1 | Lodar 14 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (320) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hmr_olwyns.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hmr_olwyns.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hmr_olwyns.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hmr_olwyns.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `hmr_olwyns` |
    | Category ID | `hammer` |
    | Icon | `items_misc_5:36` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `tiqui` |

    Raw data:

    ```json
    {
     "id": "hmr_olwyns",
     "iconID": "items_misc_5:36",
     "name": "Olwyn's curse",
     "displaytype": "rare",
     "baseMarketCost": 2502,
     "category": "hammer",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 10,
       "max": 17
      },
      "increaseAttackCost": 8,
      "increaseAttackChance": 14,
      "increaseBlockChance": -7,
      "increaseDamageResistance": -1,
      "setNonWeaponDamageModifier": 320,
      "addedConditions": [
       {
        "condition": "feebleness_minor",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
