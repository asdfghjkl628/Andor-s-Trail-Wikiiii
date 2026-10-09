---
description: "Queen spider is an enemy in Andor's Trail (insect) with 135 HP, worth 502 XP, found in Laerothcave 2, Secretpassage 1, Undertell 1 1. Drops: Spider fang, Insect shell, Gold coins."
---

# ![](../assets/icons/monsters/monsters_redshrike1_4.png){ .sprite } Queen spider

**Found in:** [Laerothcave 2](../maps/laerothcave2.md), [Secretpassage 1](../maps/secretpassage1.md), [Undertell 1 1](../maps/undertell_1_1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_redshrike1_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Laerothcave 2, Secretpassage 1, Undertell 1 1 |
| **Class** | Insect |
| **HP** | 135 |
| **XP when defeated** | 502 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 135 |
| XP when defeated | 502 |
| Damage | 8 to 19 |
| AC | 135 |
| BC | 150 |
| DR | 5 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 32% (×2.0) |

**Its hits:** On target: [Spider bite](../conditions/spider_bite.md) (magnitude 3, 5 rounds, 70% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 65% | 1 to 2 |
| [Insect shell](../items/shell.md) | 20% | 1 |
| [Gold coins](../items/gold.md) | 90% | 5 to 20 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothcave 2](../maps/laerothcave2.md) | – | 1 | – |
| [Secretpassage 1](../maps/secretpassage1.md) | – | 1 | – |
| [Undertell 1 1](../maps/undertell_1_1.md) | – | 2 | – |


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
    | Entry ID | `spider_queen` |
    | Type (wiki) | Enemy |
    | Spawn group | `spider_queen` |
    | Loot table | `spider_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_redshrike1:4` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "spider_queen",
     "name": "Queen spider",
     "iconID": "monsters_redshrike1:4",
     "maxHP": 135,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 8,
      "max": 19
     },
     "spawnGroup": "spider_queen",
     "droplistID": "spider_2",
     "attackCost": 5,
     "attackChance": 135,
     "criticalSkill": 70,
     "criticalMultiplier": 2.0,
     "blockChance": 150,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "spider_bite",
        "magnitude": 3,
        "duration": 5,
        "chance": "70"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
