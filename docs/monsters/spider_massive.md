---
description: "Giant spider is an enemy in Andor's Trail (insect) with 104 HP, worth 382 XP, found in Lake Laeroth. Drops: Spider fang, Insect shell."
---

# ![](../assets/icons/monsters/monsters_rltiles4_45.png){ .sprite } Giant spider

**Found in:** Lake Laeroth: [Laerothbarn 0](../maps/laerothbarn0.md), Lake Laeroth: [Laerothbarn 1](../maps/laerothbarn1.md), Lake Laeroth: [Laerothbasement 0](../maps/laerothbasement0.md), Lake Laeroth: [Laerothbasement 1](../maps/laerothbasement1.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles4_45.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Insect |
| **HP** | 104 |
| **XP when defeated** | 382 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 104 |
| XP when defeated | 382 |
| Damage | 8 to 15 |
| AC | 120 |
| BC | 145 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 29% (×2.0) |

**Its hits:** On target: [Spider bite](../conditions/spider_bite.md) (magnitude 2, 4 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 34% | 1 |
| [Insect shell](../items/shell.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothbarn 0](../maps/laerothbarn0.md) | Lake Laeroth | 1 | – |
| [Laerothbarn 1](../maps/laerothbarn1.md) | Lake Laeroth | 5 | – |
| [Laerothbasement 0](../maps/laerothbasement0.md) | Lake Laeroth | 4 | – |
| [Laerothbasement 1](../maps/laerothbasement1.md) | Lake Laeroth | 3 | – |
| [Laerothcave 3](../maps/laerothcave3.md) | – | 1 | – |
| [Laerothcave 4](../maps/laerothcave4.md) | – | 2 | – |
| [Laerothprison 0](../maps/laerothprison0.md) | Lake Laeroth | 4 | – |
| [Laerothprison 1](../maps/laerothprison1.md) | Lake Laeroth | 5 | – |
| [Laerothsmith 0](../maps/laerothsmith0.md) | Lake Laeroth | 4 | – |


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
    | Entry ID | `spider_massive` |
    | Type (wiki) | Enemy |
    | Spawn group | `spider_massive` |
    | Loot table | `spider` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:45` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "spider_massive",
     "name": "Giant spider",
     "iconID": "monsters_rltiles4:45",
     "maxHP": 104,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 8,
      "max": 15
     },
     "droplistID": "spider",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 60,
     "criticalMultiplier": 2.0,
     "blockChance": 145,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "spider_bite",
        "magnitude": 2,
        "duration": 4,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_massive.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_massive.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_massive.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_massive.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
