---
description: "Two-handed iron claymore is a ordinary two-handed sword in Andor's Trail (Attack damage 3 to 4, Attack cost +5, Attack chance +12, Critical skill +6). How to get it: shops."
---

# ![](../assets/icons/items/items_misc_5_38.png){ .sprite } Two-handed iron claymore

*Ordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_38.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clmr_irn2` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md) |
| **Rarity** | Ordinary |
| **Base value** | 854 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 3 to 4 |
| Attack cost | +5 |
| Attack chance | +12 |
| Critical skill | +6 |
| Block chance | -5 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +118 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Minarra](../monsters/minarra.md) (Houseatcrossroads 4)
- [Fiamma](../monsters/brightportsmith.md) (Brightport)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (118) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clmr_irn2` |
    | Category ID | `2hsword` |
    | Icon | `items_misc_5:38` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_minarra`, `fiamma_shop` |

    Raw data:

    ```json
    {
     "id": "clmr_irn2",
     "iconID": "items_misc_5:38",
     "name": "Two-handed iron claymore",
     "baseMarketCost": 854,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 3,
       "max": 4
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 12,
      "increaseCriticalSkill": 6,
      "increaseBlockChance": -5,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 118
     }
    }
    ```


<small>Data from v0.8.18</small>
