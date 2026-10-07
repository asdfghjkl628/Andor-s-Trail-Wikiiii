---
description: "Nasty cave snake is an enemy in Andor's Trail (reptile) with 30 HP, worth 117 XP, found in Roundlings, 4 wells, Bloskelt + Roskelt, Roundlings, Labyrinth. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_rltiles2_25.png){ .sprite } Nasty cave snake

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_25.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Roundlings, 4 wells, Bloskelt + Roskelt, Roundlings, Labyrinth |
| **Class** | Reptile |
| **HP** | 30 |
| **XP when defeated** | 117 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Nasty cave snake. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`cavesnake5`](#v-cavesnake5) | Enemy | 4 wells: [ratdom_maze_567](../maps/ratdom_maze_567.md), 4 wells: [ratdom_maze_658](../maps/ratdom_maze_658.md) (+7 more) | – | 30 |
| [`ratdom_m3b`](#v-ratdom_m3b) | Enemy | Bloskelt + Roskelt: [ratdom_maze_525](../maps/ratdom_maze_525.md), Bloskelt + Roskelt: [ratdom_maze_526](../maps/ratdom_maze_526.md) (+8 more) | – | 30 |

## 4 wells, Ratdom maze 567 and 8 more (cavesnake5) { #v-cavesnake5 }

**Entry ID:** `cavesnake5` · **Type:** Enemy

**Location:** 4 wells: [ratdom_maze_567](../maps/ratdom_maze_567.md), 4 wells: [ratdom_maze_658](../maps/ratdom_maze_658.md), 4 wells: [ratdom_maze_768](../maps/ratdom_maze_768.md), Roundlings: [ratdom_maze_527](../maps/ratdom_maze_527.md), Roundlings: [ratdom_maze_538](../maps/ratdom_maze_538.md), Roundlings: [ratdom_maze_628](../maps/ratdom_maze_628.md) (+3 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 30 |
| XP when defeated | 117 |
| Damage | 5 |
| Attack chance | 110 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

**On hit:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_527](../maps/ratdom_maze_527.md) | Roundlings | 2 | – |
| [ratdom_maze_538](../maps/ratdom_maze_538.md) | Roundlings | 2 | – |
| [ratdom_maze_567](../maps/ratdom_maze_567.md) | 4 wells | 2 | – |
| [ratdom_maze_628](../maps/ratdom_maze_628.md) | Roundlings | 2 | – |
| [ratdom_maze_638](../maps/ratdom_maze_638.md) | Roundlings | 2 | – |
| [ratdom_maze_646](../maps/ratdom_maze_646.md) | Roundlings | 1 | – |
| [ratdom_maze_647](../maps/ratdom_maze_647.md) | Roundlings | 2 | – |
| [ratdom_maze_658](../maps/ratdom_maze_658.md) | 4 wells | 2 | – |
| [ratdom_maze_768](../maps/ratdom_maze_768.md) | 4 wells | 5 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (cavesnake5)"

    | | |
    |---|---|
    | Entry ID | `cavesnake5` |
    | Spawn group | `cavesnake4` |
    | Loot table | `snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:25` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "cavesnake5",
     "name": "Nasty cave snake",
     "iconID": "monsters_rltiles2:25",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "cavesnake4",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Bloskelt + Roskelt, Ratdom maze 525 and 9 more (ratdom_m3b) { #v-ratdom_m3b }

**Entry ID:** `ratdom_m3b` · **Type:** Enemy

**Location:** Bloskelt + Roskelt: [ratdom_maze_525](../maps/ratdom_maze_525.md), Bloskelt + Roskelt: [ratdom_maze_526](../maps/ratdom_maze_526.md), Bloskelt + Roskelt: [ratdom_maze_636](../maps/ratdom_maze_636.md), Entry: [ratdom_maze_635](../maps/ratdom_maze_635.md), Entry: [ratdom_maze_644](../maps/ratdom_maze_644.md), Entry: [ratdom_maze_645](../maps/ratdom_maze_645.md) (+4 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 30 |
| XP when defeated | 117 |
| Damage | 5 |
| Attack chance | 110 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

**On hit:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_525](../maps/ratdom_maze_525.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_526](../maps/ratdom_maze_526.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_537](../maps/ratdom_maze_537.md) | Roundlings | 2 | – |
| [ratdom_maze_547](../maps/ratdom_maze_547.md) | Labyrinth | 2 | – |
| [ratdom_maze_635](../maps/ratdom_maze_635.md) | Entry | 2 | – |
| [ratdom_maze_636](../maps/ratdom_maze_636.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_644](../maps/ratdom_maze_644.md) | Entry | 2 | – |
| [ratdom_maze_645](../maps/ratdom_maze_645.md) | Entry | 2 | – |
| [ratdom_maze_655](../maps/ratdom_maze_655.md) | Waterway | 2 | – |
| [ratdom_maze_664](../maps/ratdom_maze_664.md) | Waterway | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_m3b)"

    | | |
    |---|---|
    | Entry ID | `ratdom_m3b` |
    | Spawn group | `ratdom_m3` |
    | Loot table | `snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:2` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_m3b",
     "name": "Nasty cave snake",
     "iconID": "monsters_snakes:2",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "ratdom_m3",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavesnake5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavesnake5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavesnake5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=cavesnake5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
