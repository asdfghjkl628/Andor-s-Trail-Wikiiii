# ![](../assets/icons/monsters/monsters_arulirs_13.png){ .sprite } Giant Golden Arulir

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_arulirs_13.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `arulir_6` |
| **Type** | Enemy |
| **Class** | Giant |
| **HP** | 501 |
| **XP when killed** | 674 |
| **Found in** | arulircave4, arulircave5, arulircave6 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 501 |
| Damage | 4 to 27 |
| Attack chance | 110 |
| Block chance | 29 |
| Damage resistance | 13 |
| Max AP | 5 |
| Attack cost | 5 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 50 |
| Critical multiplier | 3.0 |
| Crit chance | 26% |

**On hit:** On target: Stunned (magnitude 1, 4 rounds, 30% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 12 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 10% | 1 |
| [Arulir skin](../items/arulir_skin.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [arulircave4](../maps/arulircave4.md) | – | 4 | – |
| [arulircave5](../maps/arulircave5.md) | – | 3 | – |
| [arulircave6](../maps/arulircave6.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `arulir_6` |
    | Spawn group | `arulir_3` |
    | Loot table | `arulir` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_arulirs:13` |
    | Defined in | `res/raw/monsterlist_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "arulir_6",
     "name": "Giant Golden Arulir",
     "iconID": "monsters_arulirs:13",
     "maxHP": 501,
     "maxAP": 5,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 4,
      "max": 27
     },
     "spawnGroup": "arulir_3",
     "droplistID": "arulir",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 50,
     "criticalMultiplier": 3.0,
     "blockChance": 29,
     "damageResistance": 13,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 4,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
