---
description: "Venomous Dagger is a extraordinary dagger in Andor's Trail (Attack damage 1 to 2, Attack cost +4, Attack chance +10, Critical skill +5). How to get it: monster drops."
---

# ![](../assets/icons/items/items_weapons_17.png){ .sprite } Venomous Dagger

*Extraordinary dagger.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_17.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `dagger_venom` |
| **Category** | Dagger |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Extraordinary |
| **Base value** | 15 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 2 |
| Attack cost | +4 |
| Attack chance | +10 |
| Critical skill | +5 |
| Critical multiplier | 2.0 |

### On hit

| Stat | Value |
|---|---|
| On target | [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 2 rounds, 35% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Snake master](../monsters/snake_master.md) | 100% | 1 | Snakecave 3 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |
| [v0.7.15](../versions/0.7.15.md) | On hit, condition on target: added [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 2 rounds, 35% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `dagger_venom` |
    | Category ID | `dagger` |
    | Icon | `items_weapons:17` |
    | Defined in | `res/raw/itemlist_quest.json` |
    | Loot tables containing it | `snakemaster` |

    Raw data:

    ```json
    {
     "id": "dagger_venom",
     "iconID": "items_weapons:17",
     "name": "Venomous Dagger",
     "displaytype": "extraordinary",
     "baseMarketCost": 15,
     "category": "dagger",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 2
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 5,
      "setCriticalMultiplier": 2.0
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 2,
        "chance": "35"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
