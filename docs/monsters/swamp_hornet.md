---
description: "Swamp hornet is an enemy in Andor's Trail (insect) with 99 HP, worth 481 XP, found in Galmore 17, Galmore 18, Galmore 27."
---

# ![](../assets/icons/monsters/monsters_rltiles2_113.png){ .sprite } Swamp hornet

**Found in:** [Galmore 17](../maps/galmore_17.md), [Galmore 18](../maps/galmore_18.md), [Galmore 27](../maps/galmore_27.md), [Galmore 28](../maps/galmore_28.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_113.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Galmore 17, Galmore 18, Galmore 27 |
| **Class** | Insect |
| **HP** | 99 |
| **XP when defeated** | 481 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 99 |
| XP when defeated | 481 |
| Damage | 12 to 15 |
| AC | 170 |
| BC | 225 |
| DR | 5 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |

**Its hits:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 7, 5 rounds, 65% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 17](../maps/galmore_17.md) | – | 10 | – |
| [Galmore 18](../maps/galmore_18.md) | – | 12 | – |
| [Galmore 27](../maps/galmore_27.md) | – | 6 | – |
| [Galmore 28](../maps/galmore_28.md) | – | 13 | – |
| [Galmore 38](../maps/galmore_38.md) | – | 9 | – |
| [Galmore 39](../maps/galmore_39.md) | – | 10 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

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
    | Entry ID | `swamp_hornet` |
    | Type (wiki) | Enemy |
    | Spawn group | `swamp_hornet` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:113` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "swamp_hornet",
     "name": "Swamp hornet",
     "iconID": "monsters_rltiles2:113",
     "maxHP": 99,
     "moveCost": 3,
     "monsterClass": "insect",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 12,
      "max": 15
     },
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 225,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 7,
        "duration": 5,
        "chance": "65"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=swamp_hornet.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
