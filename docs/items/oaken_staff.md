---
description: "Oaken staff is a rare quarterstaff in Andor's Trail (Attack damage 3 to 8, Attack cost +5, Attack chance +7, Critical skill +3). How to get it: monster drops."
---

# ![](../assets/icons/items/items_rijackson_1_17.png){ .sprite } Oaken staff

*Rare quarterstaff.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_rijackson_1_17.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `oaken_staff` |
| **Category** | Quarterstaff |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Rare |
| **Base value** | 2,562 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 3 to 8 |
| Attack cost | +5 |
| Attack chance | +7 |
| Critical skill | +3 |
| Block chance | +10 |
| Damage resistance | +1 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +131 |

### On hit

| Stat | Value |
|---|---|
| On target | [Baited strike](../conditions/baited_strike.md) (magnitude 3, 2 rounds, 20% chance) |

### On kill

| Stat | Value |
|---|---|
| On self | [Splinter](../conditions/splinter.md) (magnitude 1, 3 rounds, 13% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Egrinda](../monsters/egrinda.md) | 100% | 1 | Way to sullengard west 3 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=oaken_staff.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=oaken_staff.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=oaken_staff.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=oaken_staff.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `oaken_staff` |
    | Category ID | `staff` |
    | Icon | `items_rijackson_1:17` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `egrinda_dl` |

    Raw data:

    ```json
    {
     "id": "oaken_staff",
     "iconID": "items_rijackson_1:17",
     "name": "Oaken staff",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 2562,
     "category": "staff",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 3,
       "max": 8
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 7,
      "increaseCriticalSkill": 3,
      "increaseBlockChance": 10,
      "increaseDamageResistance": 1,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 131
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "baited_strike",
        "magnitude": 3,
        "duration": 2,
        "chance": "20"
       }
      ]
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "splinter",
        "magnitude": 1,
        "duration": 3,
        "chance": "13"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
