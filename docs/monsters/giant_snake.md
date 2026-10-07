# ![](../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite } Giant snake

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `giant_snake` |
| **Type** | Enemy |
| **Class** | Animal |
| **HP** | 250 |
| **XP when killed** | 510 |
| **Found in** | Fallhaven |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 250 |
| Damage | 8 to 22 |
| Attack chance | 150 |
| Block chance | 60 |
| Damage resistance | 12 |
| Max AP | 10 |
| Attack cost | 8 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 3.0 |
| Crit chance | 23% |

**On hit:** On target: Venom (magnitude 2, 4 rounds, 50% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 500 to 3000 |
| [Meat](../items/meat.md) | 90% | 3 to 7 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gapfiller2](../maps/gapfiller2.md) | Fallhaven | 1 | appears later in a quest |


## Quests that count kills

- A conversation with [Bela](../monsters/bela.md) checks that you've killed at least 1


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=giant_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `giant_snake` |
    | Spawn group | `giant_snake` |
    | Loot table | `giant_snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:21` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "giant_snake",
     "name": "Giant snake",
     "iconID": "monsters_rltiles2:21",
     "maxHP": 250,
     "maxAP": 10,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 8,
      "max": 22
     },
     "spawnGroup": "giant_snake",
     "droplistID": "giant_snake",
     "attackCost": 8,
     "attackChance": 150,
     "criticalSkill": 40,
     "criticalMultiplier": 3.0,
     "blockChance": 60,
     "damageResistance": 12,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "venom",
        "magnitude": 2,
        "duration": 4,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
