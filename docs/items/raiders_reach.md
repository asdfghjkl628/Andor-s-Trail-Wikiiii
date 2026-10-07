---
description: "Raider's reach is a rare whip in Andor's Trail (Attack damage 1 to 3, Max HP +3, Attack cost +5, Attack chance +6). How to get it: monster drops."
---

# ![](../assets/icons/items/items_newb_493.png){ .sprite } Raider's reach

*Rare whip.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_493.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `raiders_reach` |
| **Category** | Whip |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Rare |
| **Base value** | 6,700 gold |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 3 |
| Max HP | +3 |
| Attack cost | +5 |
| Attack chance | +6 |
| Critical skill | +2 |
| Block chance | +6 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +130 |

### On hit

| Stat | Value |
|---|---|
| On target | Minor sting (magnitude 1, 2 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Dorhantarh](../monsters/lae_island_boss.md) | 100% | 1 | final_cave2 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |
| [v0.8.12.1](../versions/0.8.12.1.md) | equipEffect: {"increaseAttackChance": 6, "increaseAt… → {"increaseAttackChance": 6, "increaseAt… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=raiders_reach.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=raiders_reach.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=raiders_reach.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=raiders_reach.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `raiders_reach` |
    | Category ID | `whip` |
    | Icon | `items_newb:493` |
    | Defined in | `res/raw/itemlist_laeroth.json` |
    | Loot tables containing it | `lae_island_boss` |

    Raw data:

    ```json
    {
     "id": "raiders_reach",
     "iconID": "items_newb:493",
     "name": "Raider's reach",
     "displaytype": "rare",
     "baseMarketCost": 6700,
     "category": "whip",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 3
      },
      "increaseMaxHP": 3,
      "increaseAttackCost": 5,
      "increaseAttackChance": 6,
      "increaseCriticalSkill": 2,
      "increaseBlockChance": 6,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 130
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "sting_minor",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
