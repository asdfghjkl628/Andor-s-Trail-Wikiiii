---
description: "Death mace is a ordinary mace in Andor's Trail (Attack damage 7 to 13, Attack cost +6, Attack chance +10, Critical skill +11). How to get it: monster drops."
---

# ![](../assets/icons/items/items_misc_6_16.png){ .sprite } Death mace

*Ordinary mace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_16.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `death_mace` |
| **Category** | Mace |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 7 to 13 |
| Attack cost | +6 |
| Attack chance | +10 |
| Critical skill | +11 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +120 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Death wrecker](../monsters/death_wrecker.md) | 5% | 1 | haunted_house, haunted_house_basement, haunted_underground_1 |
| [Mindless disgrace](../monsters/mindless_disgrace.md) | 5% | 1 | haunted_house, haunted_house_basement, haunted_underground_1 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=death_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=death_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=death_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=death_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `death_mace` |
    | Category ID | `mace` |
    | Icon | `items_misc_6:16` |
    | Defined in | `res/raw/itemlist_haunted_forest.json` |
    | Loot tables containing it | `death_wrecker_dl`, `mindless_disgrace_dl` |

    Raw data:

    ```json
    {
     "id": "death_mace",
     "iconID": "items_misc_6:16",
     "name": "Death mace",
     "displaytype": "ordinary",
     "category": "mace",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 7,
       "max": 13
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 11,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 120
     }
    }
    ```


<small>Data from v0.8.18</small>
