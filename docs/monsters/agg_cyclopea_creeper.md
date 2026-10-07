# ![](../assets/icons/monsters/monsters_newb_1_1091.png){ .sprite } Crimoculus Cyclopea creeper

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1091.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `agg_cyclopea_creeper` |
| **Type** | Enemy |
| **Class** | Reptile |
| **HP** | 245 |
| **XP when killed** | 626 |
| **Found in** | nw_sullengard_1 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 245 |
| Damage | 6 |
| Attack chance | 155 |
| Block chance | 191 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 6 AP |
| Critical skill | 12 |
| Critical multiplier | 2.5 |
| Crit chance | 10% |

**On hit:** On target: Rootsnare (magnitude 1, 4 rounds, 25% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Cyclopean eye gem](../items/cyclopean_eye_gem.md) | 3% | 1 |
| [Cyclopea root](../items/cyclopea_root.md) | 5% | 1 |
| [Photosynthetic leaf](../items/photosynthetic_leaf.md) | 6% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [nw_sullengard_1](../maps/nw_sullengard_1.md) | – | 9 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agg_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agg_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agg_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agg_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `agg_cyclopea_creeper` |
    | Spawn group | `agg_cyclopea_creeper` |
    | Loot table | `cyclopea_creeper_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_newb_1:1091` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "agg_cyclopea_creeper",
     "name": "Crimoculus Cyclopea creeper",
     "iconID": "monsters_newb_1:1091",
     "maxHP": 245,
     "maxAP": 12,
     "moveCost": 6,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 6
     },
     "droplistID": "cyclopea_creeper_dl",
     "attackCost": 4,
     "attackChance": 155,
     "criticalSkill": 12,
     "criticalMultiplier": 2.5,
     "blockChance": 191,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "rootsnare",
        "magnitude": 1,
        "duration": 4,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
