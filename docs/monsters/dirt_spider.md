---
description: "Dirt spider is an enemy in Andor's Trail (insect) with 82 HP, worth 331 XP, found in Stoutford, Mt. Galmore. Drops: Spider fang, Insect shell."
---

# ![](../assets/icons/monsters/monsters_tometik10_53.png){ .sprite } Dirt spider

**Found in:** Mt. Galmore: [Galmore 35](../maps/galmore_35.md), Mt. Galmore: [Galmore 44](../maps/galmore_44.md), Mt. Galmore: [Galmore 45](../maps/galmore_45.md), Stoutford: [Galmore 12](../maps/galmore_12.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik10_53.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford, Mt. Galmore |
| **Class** | Insect |
| **HP** | 82 |
| **XP when defeated** | 331 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 82 |
| XP when defeated | 331 |
| Damage | 5 to 7 |
| AC | 107 |
| BC | 175 |
| DR | 13 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 4, 6 rounds, 40% chance); [Spider bite](../conditions/spider_bite.md) (magnitude 1, 4 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 34% | 1 |
| [Insect shell](../items/shell.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 10](../maps/galmore_10.md) | – | 1 | – |
| [Galmore 11](../maps/galmore_11.md) | – | 1 | – |
| [Galmore 12](../maps/galmore_12.md) | Stoutford | 7 | – |
| [Galmore 12a](../maps/galmore_12a.md) | Stoutford | 11 | – |
| [Galmore 13](../maps/galmore_13.md) | Stoutford | 1 | – |
| [Galmore 15](../maps/galmore_15.md) | – | 3 | – |
| [Galmore 23](../maps/galmore_23.md) | – | 2 | – |
| [Galmore 35](../maps/galmore_35.md) | Mt. Galmore | 8 | – |
| [Galmore 44](../maps/galmore_44.md) | Mt. Galmore | 6 | – |
| [Galmore 45](../maps/galmore_45.md) | Mt. Galmore | 3 | – |
| [Rat mountain 8](../maps/rat_mountain_8.md) | – | 5 | – |
| [Stoutford filler 1](../maps/stoutford_filler_1.md) | Stoutford | 10 | – |
| [Stoutford filler 2](../maps/stoutford_filler_2.md) | Stoutford | 12 | – |
| [Stoutford filler 3](../maps/stoutford_filler_3.md) | Stoutford | 13 | – |
| [Stoutford filler 4](../maps/stoutford_filler_4.md) | – | 10 | – |


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
    | Entry ID | `dirt_spider` |
    | Type (wiki) | Enemy |
    | Spawn group | `dirt_spider` |
    | Loot table | `spider` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik10:53` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "dirt_spider",
     "name": "Dirt spider",
     "iconID": "monsters_tometik10:53",
     "maxHP": 82,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "spawnGroup": "dirt_spider",
     "droplistID": "spider",
     "attackCost": 3,
     "attackChance": 107,
     "blockChance": 175,
     "damageResistance": 13,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 4,
        "duration": 6,
        "chance": "40"
       },
       {
        "condition": "spider_bite",
        "magnitude": 1,
        "duration": 4,
        "chance": "15"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirt_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirt_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirt_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirt_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
