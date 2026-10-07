---
description: "Obsidian dagger is a extraordinary dagger in Andor's Trail (Attack damage 3 to 6, Move cost 0, Attack cost +4, Attack chance +15). How to get it: monster drops."
---

# ![](../assets/icons/items/items_misc_6_21.png){ .sprite } Obsidian dagger

*Extraordinary dagger.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_21.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `obsidian_dagger` |
| **Category** | Dagger |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Extraordinary |
| **Base value** | 1,500 gold |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 3 to 6 |
| Move cost | 0 |
| Attack cost | +4 |
| Attack chance | +15 |
| Critical skill | +10 |
| Critical multiplier | 3.0 |
| setNonWeaponDamageModifier | +104 |

### On hit

| Stat | Value |
|---|---|
| On target | Bleeding wound (magnitude 3, 5 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Kotheses](../monsters/kotheses.md) | 100% | 1 | laerothprison7 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |
| [v0.8.13](../versions/0.8.13.md) | equipEffect: {"increaseAttackCost": 4, "increaseAtta… → {"increaseAttackChance": 15, "increaseA…; hitEffect: {"conditionsTarget": [{"chance": "20", … → {"conditionsTarget": [{"chance": "20", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=obsidian_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=obsidian_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=obsidian_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=obsidian_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `obsidian_dagger` |
    | Category ID | `dagger` |
    | Icon | `items_misc_6:21` |
    | Defined in | `res/raw/itemlist_laeroth.json` |
    | Loot tables containing it | `kotheses` |

    Raw data:

    ```json
    {
     "id": "obsidian_dagger",
     "iconID": "items_misc_6:21",
     "name": "Obsidian dagger",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 1500,
     "category": "dagger",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 3,
       "max": 6
      },
      "increaseMoveCost": 0,
      "increaseAttackCost": 4,
      "increaseAttackChance": 15,
      "increaseCriticalSkill": 10,
      "setCriticalMultiplier": 3.0,
      "setNonWeaponDamageModifier": 104
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 5,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
