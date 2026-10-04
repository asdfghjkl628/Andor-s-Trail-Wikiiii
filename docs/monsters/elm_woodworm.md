# ![](../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite } Contaminated woodworm

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_162.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `elm_woodworm` |
| **Type** | Enemy |
| **Class** | Animal |
| **HP** | 76 |
| **XP when killed** | 292 |
| **Found in** | elm_2f_1, elm_3f, elm_4f_1 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 76 |
| Damage | 6 to 9 |
| Attack chance | 90 |
| Block chance | 144 |
| Damage resistance | 7 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** Heal HP: -1; On target: Bleeding wound (magnitude 1, 2 rounds, 20% chance)

**When hit:** Heal HP: 1; On target: Nausea (magnitude 2, 3 rounds, 30% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Claws](../items/claws.md) | 33.3333% | 1 |
| [Rotten meat](../items/meat2.md) | 10% | 1 |
| [Worm meat](../items/meat3.md) | 20% | 1 |
| [Gold coins](../items/gold.md) | 100% | 1 to 12 |
| [Small rock](../items/rock.md) | 12.5% | 1 to 3 |
| [Small empty vial](../items/vial_empty1.md) | 12.5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [elm_2f_1](../maps/elm_2f_1.md) | – | 19 | – |
| [elm_3f](../maps/elm_3f.md) | – | 9 | – |
| [elm_4f_1](../maps/elm_4f_1.md) | – | 6 | – |
| [elm_4f_2](../maps/elm_4f_2.md) | – | 7 | – |
| [elm_4f_3](../maps/elm_4f_3.md) | – | 2 | – |
| [elm_4f_4](../maps/elm_4f_4.md) | – | 3 | – |
| [elm_4f_5](../maps/elm_4f_5.md) | – | 3 | – |
| [elm_mine5](../maps/elm_mine5.md) | – | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_woodworm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `elm_woodworm` |
    | Spawn group | `elm_mine1` |
    | Loot table | `elm_woodworm` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:162` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_woodworm",
     "name": "Contaminated woodworm",
     "iconID": "monsters_rltiles2:162",
     "maxHP": 76,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "animal",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 9
     },
     "spawnGroup": "elm_mine1",
     "droplistID": "elm_woodworm",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 144,
     "damageResistance": 7,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 1,
        "duration": 2,
        "chance": "20"
       }
      ]
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
