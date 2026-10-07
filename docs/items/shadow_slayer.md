---
description: "Shadow of the slayer is a extraordinary greataxe in Andor's Trail (Attack damage 5 to 9, Max AP +2, Attack cost +7, Attack chance +25). How to get it: monster drops."
---

# ![](../assets/icons/items/items_weapons_60.png){ .sprite } Shadow of the slayer

*Extraordinary greataxe.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_60.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `shadow_slayer` |
| **Category** | Greataxe |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Axe proficiency](../skills/weaponProficiencyAxe.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 5 to 9 |
| Max AP | +2 |
| Attack cost | +7 |
| Attack chance | +25 |
| Critical skill | +10 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +185 |

### On kill

| Stat | Value |
|---|---|
| Heal HP | 1 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Kazaul guardian](../monsters/kazaul_guardian.md) | 100% | 1 | blackwater_mountain42 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 25, "increaseA… → {"increaseAttackChance": 25, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shadow_slayer.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shadow_slayer.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shadow_slayer.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shadow_slayer.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `shadow_slayer` |
    | Category ID | `axe2h` |
    | Icon | `items_weapons:60` |
    | Defined in | `res/raw/itemlist_v069.json` |
    | Loot tables containing it | `kazaul_guardian` |

    Raw data:

    ```json
    {
     "id": "shadow_slayer",
     "iconID": "items_weapons:60",
     "name": "Shadow of the slayer",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 0,
     "category": "axe2h",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 5,
       "max": 9
      },
      "increaseMaxAP": 2,
      "increaseAttackCost": 7,
      "increaseAttackChance": 25,
      "increaseCriticalSkill": 10,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 185
     },
     "killEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
