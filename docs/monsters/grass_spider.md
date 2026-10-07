# ![](../assets/icons/monsters/monsters_tometik10_56.png){ .sprite } Grass spider

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_56.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `grass_spider` |
| **Type** | Enemy |
| **Class** | Insect |
| **HP** | 79 |
| **XP when killed** | 307 |
| **Found in** | Mt. Galmore, Flagstone Prison, Wexlow Village |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 79 |
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
| Crit chance | none (needs critical skill and a multiplier) |

**On hit:** On target: Insect contagion (magnitude 4, 6 rounds, 40% chance); Spider bite (magnitude 1, 4 rounds, 15% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider fang](../items/spider_fang.md) | 34% | 1 |
| [Insect shell](../items/shell.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_10](../maps/galmore_10.md) | – | 6 | – |
| [galmore_11](../maps/galmore_11.md) | – | 4 | – |
| [galmore_35](../maps/galmore_35.md) | Mt. Galmore | 6 | – |
| [galmore_9](../maps/galmore_9.md) | Flagstone Prison | 3 | – |
| [way_to_wexlow1](../maps/way_to_wexlow1.md) | Wexlow Village | 6 | – |
| [way_to_wexlow2](../maps/way_to_wexlow2.md) | Wexlow Village | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=grass_spider.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `grass_spider` |
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


<small>Data from v0.8.18</small>
