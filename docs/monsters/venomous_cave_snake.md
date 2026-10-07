# ![](../assets/icons/monsters/monsters_snakes_3.png){ .sprite } Venomous cave snake

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_snakes_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `venomous_cave_snake` |
| **Type** | Enemy |
| **Class** | Reptile |
| **HP** | 15 |
| **XP when killed** | 79 |
| **Found in** | Brimhaven, Bloskelt + Roskelt, Entry |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 15 |
| Damage | 2 |
| Attack chance | 110 |
| Block chance | 10 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Crit chance | 23% |

**On hit:** On target: Weak Poison (magnitude 1, 1 rounds, 10% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

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
| [basiliskcave1](../maps/basiliskcave1.md) | Brimhaven | 2 | – |
| [basiliskcave1_1_2](../maps/basiliskcave1_1_2.md) | – | 4 | – |
| [basiliskcave1_1_3](../maps/basiliskcave1_1_3.md) | – | 1 | – |
| [ratdom_maze_417](../maps/ratdom_maze_417.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_427](../maps/ratdom_maze_427.md) | Entry | 2 | – |
| [ratdom_maze_428](../maps/ratdom_maze_428.md) | Entry | 2 | – |
| [ratdom_maze_436](../maps/ratdom_maze_436.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_437](../maps/ratdom_maze_437.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_438](../maps/ratdom_maze_438.md) | Entry | 2 | – |
| [ratdom_maze_446](../maps/ratdom_maze_446.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_447](../maps/ratdom_maze_447.md) | Entry | 2 | – |
| [ratdom_maze_458](../maps/ratdom_maze_458.md) | Entry | 3 | – |
| [ratdom_maze_516](../maps/ratdom_maze_516.md) | Bloskelt + Roskelt | 2 | – |
| [ratdom_maze_517](../maps/ratdom_maze_517.md) | Entry | 2 | – |
| [ratdom_maze_555](../maps/ratdom_maze_555.md) | Instrument maker | 2 | – |
| [ratdom_maze_568](../maps/ratdom_maze_568.md) | Labyrinth | 7 | – |
| [ratdom_maze_616](../maps/ratdom_maze_616.md) | Pub | 3 | – |
| [ratdom_maze_626](../maps/ratdom_maze_626.md) | Pub | 5 | – |
| [ratdom_maze_635](../maps/ratdom_maze_635.md) | Entry | 1 | – |
| [ratdom_maze_705](../maps/ratdom_maze_705.md) | Pub | 4 | – |
| [snakecave2](../maps/snakecave2.md) | Blackwater Mountain | 7 | – |
| [snakecave3](../maps/snakecave3.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 10, "c… → {"conditionsTarget": [{"chance": "10", …; name: Venomous Cave Snake → Venomous cave snake |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=venomous_cave_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `venomous_cave_snake` |
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
     "id": "venomous_cave_snake",
     "name": "Venomous cave snake",
     "iconID": "monsters_snakes:3",
     "maxHP": 15,
     "maxAP": 10,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 2
     },
     "spawnGroup": "cavesnake2",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 10,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 1,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
