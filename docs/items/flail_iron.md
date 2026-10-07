---
description: "Iron flail is a ordinary mace in Andor's Trail (Attack damage 6 to 14, Attack cost +6, Attack chance +8, Critical skill +10). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_3_13.png){ .sprite } Iron flail

*Ordinary mace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_13.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `flail_iron` |
| **Category** | Mace |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 6 to 14 |
| Attack cost | +6 |
| Attack chance | +8 |
| Critical skill | +10 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +135 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Cornith](../monsters/stoutford_smith.md) (Stoutford)
- [Lamberta](../monsters/sullengard_lamberta.md) (Sullengard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.7.8](../versions/0.7.8.md) | equipEffect: {"increaseAttackCost": 6, "increaseAtta… → {"increaseAttackChance": 8, "increaseAt… |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 8, "increaseAt… → {"increaseAttackChance": 8, "increaseAt… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `flail_iron` |
    | Category ID | `mace` |
    | Icon | `items_weapons_3:13` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cornith`, `sullengard_lamberta_dl` |

    Raw data:

    ```json
    {
     "id": "flail_iron",
     "iconID": "items_weapons_3:13",
     "name": "Iron flail",
     "displaytype": "ordinary",
     "category": "mace",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 6,
       "max": 14
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 8,
      "increaseCriticalSkill": 10,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 135
     }
    }
    ```


<small>Data from v0.8.18</small>
