# ![](../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite } Dun olm

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `bwm_olm1` |
| **Type** | Enemy |
| **Class** | Animal |
| **HP** | 61 |
| **XP when killed** | 196 |
| **Found in** | blackwater_mountain74, blackwater_mountain74_h, blackwater_mountain75 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 61 |
| Damage | 5 to 10 |
| Attack chance | 110 |
| Block chance | 130 |
| Damage resistance | 6 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 1.5 |
| Crit chance | 9% |

**When hit:** On self: Panic (magnitude 1, 1 rounds, 20% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain74](../maps/blackwater_mountain74.md) | – | 7 | – |
| [blackwater_mountain74_h](../maps/blackwater_mountain74_h.md) | – | 3 | – |
| [blackwater_mountain75](../maps/blackwater_mountain75.md) | – | 8 | – |
| [elm5f_1](../maps/elm5f_1.md) | – | 1 | – |
| [elm_2f_1](../maps/elm_2f_1.md) | – | 2 | – |
| [elm_mine2](../maps/elm_mine2.md) | – | 6 | – |
| [elm_mine3](../maps/elm_mine3.md) | – | 2 | – |
| [elm_mine4](../maps/elm_mine4.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `bwm_olm1` |
    | Spawn group | `bwm_olm` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:21` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_olm1",
     "name": "Dun olm",
     "iconID": "monsters_rltiles2:21",
     "maxHP": 61,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 10
     },
     "spawnGroup": "bwm_olm",
     "attackCost": 4,
     "attackChance": 110,
     "criticalSkill": 10,
     "criticalMultiplier": 1.5,
     "blockChance": 130,
     "damageResistance": 6,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "panic",
        "magnitude": 1,
        "duration": 1,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
