---
description: "Greater wight is an enemy in Andor's Trail (undead) with 150 HP, worth 227 XP, found in Laerothprison 6, Laerothprison 7. Drops: Gold coins, Bone, Reinforced leather buckler."
---

# ![](../assets/icons/monsters/monsters_tometik7_14.png){ .sprite } Greater wight

**Found in:** [Laerothprison 6](../maps/laerothprison6.md), [Laerothprison 7](../maps/laerothprison7.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Laerothprison 6, Laerothprison 7 |
| **Class** | Undead |
| **HP** | 150 |
| **XP when defeated** | 227 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 150 |
| XP when defeated | 227 |
| Damage | 2 to 17 |
| AC | 70 |
| BC | 65 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×1.3) |

**Its hits:** Heal HP: 1

**When you hit it:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 5 to 15 |
| [Bone](../items/bone.md) | 70% | 1 |
| [Reinforced leather buckler](../items/shield_leather.md) | 6% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 6](../maps/laerothprison6.md) | – | 3 | – |
| [Laerothprison 7](../maps/laerothprison7.md) | – | 17 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wight_greater` |
    | Type (wiki) | Enemy |
    | Spawn group | `wight` |
    | Loot table | `wight2` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik7:14` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_greater",
     "name": "Greater wight",
     "iconID": "monsters_tometik7:14",
     "maxHP": 150,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 2,
      "max": 17
     },
     "spawnGroup": "wight",
     "droplistID": "wight2",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 10,
     "criticalMultiplier": 1.3,
     "blockChance": 65,
     "damageResistance": 1,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_greater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_greater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_greater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_greater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
