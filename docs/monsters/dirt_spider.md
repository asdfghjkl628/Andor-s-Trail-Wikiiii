---
description: "Dirt spider is an enemy in Andor's Trail (insect) with 82 HP, worth 331 XP, found in Stoutford, Mt. Galmore. Drops: Spider fang, Insect shell."
---

# ![](../assets/icons/monsters/monsters_tometik10_53.png){ .sprite } Dirt spider

**Found in:** Mt. Galmore: [galmore_35](../maps/galmore_35.md), Mt. Galmore: [galmore_44](../maps/galmore_44.md), Mt. Galmore: [galmore_45](../maps/galmore_45.md), Stoutford: [galmore_12](../maps/galmore_12.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_53.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford, Mt. Galmore |
| **Class** | Insect |
| **HP** | 82 |
| **XP when defeated** | 331 |
| **Entry ID** | `dirt_spider` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 82 |
| XP when defeated | 331 |
| Damage | 5 to 7 |
| Attack chance | 107 |
| Block chance | 175 |
| Damage resistance | 13 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 4, 6 rounds, 40% chance); [Spider bite](../conditions/spider_bite.md) (magnitude 1, 4 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 34% | 1 |
| [Insect shell](../items/shell.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_10](../maps/galmore_10.md) | – | 1 | – |
| [galmore_11](../maps/galmore_11.md) | – | 1 | – |
| [galmore_12](../maps/galmore_12.md) | Stoutford | 7 | – |
| [galmore_12a](../maps/galmore_12a.md) | Stoutford | 11 | – |
| [galmore_13](../maps/galmore_13.md) | Stoutford | 1 | – |
| [galmore_15](../maps/galmore_15.md) | – | 3 | – |
| [galmore_23](../maps/galmore_23.md) | – | 2 | – |
| [galmore_35](../maps/galmore_35.md) | Mt. Galmore | 8 | – |
| [galmore_44](../maps/galmore_44.md) | Mt. Galmore | 6 | – |
| [galmore_45](../maps/galmore_45.md) | Mt. Galmore | 3 | – |
| [rat_mountain_8](../maps/rat_mountain_8.md) | – | 5 | – |
| [stoutford_filler_1](../maps/stoutford_filler_1.md) | Stoutford | 10 | – |
| [stoutford_filler_2](../maps/stoutford_filler_2.md) | Stoutford | 12 | – |
| [stoutford_filler_3](../maps/stoutford_filler_3.md) | Stoutford | 13 | – |
| [stoutford_filler_4](../maps/stoutford_filler_4.md) | – | 10 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dirt_spider` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
