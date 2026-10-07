---
description: "Giant's flail is a extraordinary two-handed mace in Andor's Trail (Attack damage 11 to 40, Attack cost +14, Attack chance +20, Critical skill +5). How to get it: monster drops. This is a very heavy weapon!"
---

# ![](../assets/icons/items/items_misc_6_16.png){ .sprite } Giant's flail

*Extraordinary two-handed mace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_16.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `flail_giant` |
| **Category** | Two-handed mace |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | none (the game assigns no proficiency to this weapon type) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

> This is a very heavy weapon!

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 11 to 40 |
| Attack cost | +14 |
| Attack chance | +20 |
| Critical skill | +5 |
| Critical multiplier | 3.0 |
| setNonWeaponDamageModifier | +320 |

### On hit

| Stat | Value |
|---|---|
| On target | [Dazed](../conditions/dazed.md) (magnitude 1, 3 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Arulir Pack Leader](../monsters/arulir_leader.md) | 100% | 1 | arulircave6 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (320) |
| [v0.8.14](../versions/0.8.14.md) | Category: mace → mace2h |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=flail_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `flail_giant` |
    | Category ID | `mace2h` |
    | Icon | `items_misc_6:16` |
    | Defined in | `res/raw/itemlist_arulir_mountain.json` |
    | Loot tables containing it | `arulir_leader` |

    Raw data:

    ```json
    {
     "id": "flail_giant",
     "iconID": "items_misc_6:16",
     "name": "Giant's flail",
     "displaytype": "extraordinary",
     "category": "mace2h",
     "description": "This is a very heavy weapon!",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 11,
       "max": 40
      },
      "increaseAttackCost": 14,
      "increaseAttackChance": 20,
      "increaseCriticalSkill": 5,
      "setCriticalMultiplier": 3.0,
      "setNonWeaponDamageModifier": 320
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
