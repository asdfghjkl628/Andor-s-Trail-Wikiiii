# ![](../assets/icons/monsters/monsters_redshrike1_4.png){ .sprite } Queen spider

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_redshrike1_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `spider_queen` |
| **Type** | Enemy |
| **Class** | Insect |
| **HP** | 135 |
| **XP when killed** | 502 |
| **Found in** | laerothcave2, secretpassage1, undertell_1_1 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 135 |
| Damage | 8 to 19 |
| Attack chance | 135 |
| Block chance | 150 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 70 |
| Critical multiplier | 2.0 |
| Crit chance | 32% |

**On hit:** On target: Spider bite (magnitude 3, 5 rounds, 70% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 65% | 1 to 2 |
| [Insect shell](../items/shell.md) | 20% | 1 |
| [Gold coins](../items/gold.md) | 90% | 5 to 20 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothcave2](../maps/laerothcave2.md) | – | 1 | – |
| [secretpassage1](../maps/secretpassage1.md) | – | 1 | – |
| [undertell_1_1](../maps/undertell_1_1.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spider_queen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `spider_queen` |
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


<small>Data from v0.8.18</small>
