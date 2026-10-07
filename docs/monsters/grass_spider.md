---
description: "Grass spider is an enemy in Andor's Trail (insect) with 79 HP, worth 307 XP, found in Mt. Galmore, Flagstone Prison, Wexlow Village. Drops: Spider fang, Insect shell."
---

# ![](../assets/icons/monsters/monsters_tometik10_56.png){ .sprite } Grass spider

**Found in:** Flagstone Prison: [Galmore 9](../maps/galmore_9.md), Mt. Galmore: [Galmore 35](../maps/galmore_35.md), Wexlow Village: [Way to wexlow 1](../maps/way_to_wexlow1.md), Wexlow Village: [Way to wexlow 2](../maps/way_to_wexlow2.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_56.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore, Flagstone Prison, Wexlow Village |
| **Class** | Insect |
| **HP** | 79 |
| **XP when defeated** | 307 |
| **Entry ID** | `grass_spider` |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 79 |
| XP when defeated | 307 |
| Damage | 4 to 6 |
| Attack chance | 100 |
| Block chance | 170 |
| Damage resistance | 12 |
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
| [Galmore 10](../maps/galmore_10.md) | – | 6 | – |
| [Galmore 11](../maps/galmore_11.md) | – | 4 | – |
| [Galmore 35](../maps/galmore_35.md) | Mt. Galmore | 6 | – |
| [Galmore 9](../maps/galmore_9.md) | Flagstone Prison | 3 | – |
| [Way to wexlow 1](../maps/way_to_wexlow1.md) | Wexlow Village | 6 | – |
| [Way to wexlow 2](../maps/way_to_wexlow2.md) | Wexlow Village | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `grass_spider` |
    | Spawn group | `` |
    | Loot table | `spider` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik10:56` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "grass_spider",
     "name": "Grass spider",
     "iconID": "monsters_tometik10:56",
     "maxHP": 79,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 4,
      "max": 6
     },
     "spawnGroup": "",
     "droplistID": "spider",
     "attackCost": 3,
     "attackChance": 100,
     "blockChance": 170,
     "damageResistance": 12,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
