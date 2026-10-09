---
description: "Tough cave snake is an enemy in Andor's Trail (reptile) with 21 HP, worth 30 XP, found in Brimhaven, Bloskelt + Roskelt, Entry. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_snakes_3.png){ .sprite } Tough cave snake

**Found in:** Blackwater Mountain: [Snakecave 2](../maps/snakecave2.md), Bloskelt + Roskelt: [Ratdom maze 417](../maps/ratdom_maze_417.md), Bloskelt + Roskelt: [Ratdom maze 436](../maps/ratdom_maze_436.md), Bloskelt + Roskelt: [Ratdom maze 437](../maps/ratdom_maze_437.md) (+18 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_snakes_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brimhaven, Bloskelt + Roskelt, Entry |
| **Class** | Reptile |
| **HP** | 21 |
| **XP when defeated** | 30 |
| **Entry ID** | `tough_cave_snake` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 21 |
| XP when defeated | 30 |
| Damage | 2 |
| Attack chance | 110 |
| Block chance | 15 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Basiliskcave 1](../maps/basiliskcave1.md) | Brimhaven | 2 | – |
| [Basiliskcave 1 1 2](../maps/basiliskcave1_1_2.md) | – | 4 | – |
| [Basiliskcave 1 1 3](../maps/basiliskcave1_1_3.md) | – | 1 | – |
| [Ratdom maze 417](../maps/ratdom_maze_417.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 427](../maps/ratdom_maze_427.md) | Entry | 2 | – |
| [Ratdom maze 428](../maps/ratdom_maze_428.md) | Entry | 2 | – |
| [Ratdom maze 436](../maps/ratdom_maze_436.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 437](../maps/ratdom_maze_437.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 438](../maps/ratdom_maze_438.md) | Entry | 2 | – |
| [Ratdom maze 446](../maps/ratdom_maze_446.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 447](../maps/ratdom_maze_447.md) | Entry | 2 | – |
| [Ratdom maze 458](../maps/ratdom_maze_458.md) | Entry | 3 | – |
| [Ratdom maze 516](../maps/ratdom_maze_516.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 517](../maps/ratdom_maze_517.md) | Entry | 2 | – |
| [Ratdom maze 555](../maps/ratdom_maze_555.md) | Instrument maker | 2 | – |
| [Ratdom maze 568](../maps/ratdom_maze_568.md) | Labyrinth | 7 | – |
| [Ratdom maze 616](../maps/ratdom_maze_616.md) | Pub | 3 | – |
| [Ratdom maze 626](../maps/ratdom_maze_626.md) | Pub | 5 | – |
| [Ratdom maze 635](../maps/ratdom_maze_635.md) | Entry | 1 | – |
| [Ratdom maze 705](../maps/ratdom_maze_705.md) | Pub | 4 | – |
| [Snakecave 2](../maps/snakecave2.md) | Blackwater Mountain | 7 | – |
| [Snakecave 3](../maps/snakecave3.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Tough Cave Snake” → “Tough cave snake” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `tough_cave_snake` |
    | Spawn group | `cavesnake2` |
    | Loot table | `snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:3` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "tough_cave_snake",
     "name": "Tough cave snake",
     "iconID": "monsters_snakes:3",
     "maxHP": 21,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 2
     },
     "spawnGroup": "cavesnake2",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 15
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tough_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
