# ![](../assets/icons/items/items_misc_5_38.png){ .sprite } Two-handed iron sword

*Ordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_38.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clmr_irn1` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Two-handed sword |
| **Rarity** | Ordinary |
| **Base value** | 92 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 6 |
| Attack cost | +5 |
| Attack chance | +9 |
| Critical skill | +1 |
| Block chance | -5 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +116 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Audir](../monsters/audir.md)
- [Cornith](../monsters/stoutford_smith.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | equipEffect: {"increaseAttackChance": 9, "increaseAt… → {"increaseAttackChance": 9, "increaseAt… |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 9, "increaseAt… → {"increaseAttackChance": 9, "increaseAt… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_irn1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clmr_irn1` |
    | Category ID | `2hsword` |
    | Icon | `items_misc_5:38` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_audir`, `shop_cornith` |

    Raw data:

    ```json
    {
     "id": "clmr_irn1",
     "iconID": "items_misc_5:38",
     "name": "Two-handed iron sword",
     "baseMarketCost": 92,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 6
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 9,
      "increaseCriticalSkill": 1,
      "increaseBlockChance": -5,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 116
     }
    }
    ```


<small>Data from v0.8.18</small>
