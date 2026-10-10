---
description: "Giant ogre is an enemy in Andor's Trail (giant) with 590 HP, worth 1005 XP, found in Ratdom maze 517a. Drops: Gold coins, Iron club."
---

# ![](../assets/icons/monsters/monsters_cyclops_0.png){ .sprite } Giant ogre

**Found in:** [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_cyclops_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Ratdom maze 517a |
| **Class** | Giant |
| **HP** | 590 |
| **XP when defeated** | 1,005 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 590 |
| XP when defeated | 1,005 |
| Damage | 20 to 60 |
| AC | 90 |
| BC | 90 |
| DR | 15 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Stunned](../conditions/stunned.md) (magnitude 1, 5 rounds, 5% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1000 to 5000 |
| [Iron club](../items/club3.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

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
    | Entry ID | `ratdom_troll_9` |
    | Type (wiki) | Enemy |
    | Spawn group | `ratdom_troll_9` |
    | Loot table | `ratdom_troll_9` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_cyclops:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_troll_9",
     "name": "Giant ogre",
     "iconID": "monsters_cyclops:0",
     "maxHP": 590,
     "maxAP": 10,
     "moveCost": 8,
     "unique": 1,
     "monsterClass": "giant",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 20,
      "max": 60
     },
     "spawnGroup": "ratdom_troll_9",
     "droplistID": "ratdom_troll_9",
     "attackCost": 9,
     "attackChance": 90,
     "blockChance": 90,
     "damageResistance": 15,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 5,
        "chance": "5"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_troll_9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_troll_9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_troll_9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_troll_9.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
