---
description: "Dun olm is an enemy in Andor's Trail (animal) with 61 HP, worth 196 XP, found in blackwater_mountain74, blackwater_mountain74_h, blackwater_mountain75."
---

# ![](../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite } Dun olm

**Found in:** [blackwater_mountain74](../maps/blackwater_mountain74.md), [blackwater_mountain74_h](../maps/blackwater_mountain74_h.md), [blackwater_mountain75](../maps/blackwater_mountain75.md), [elm5f_1](../maps/elm5f_1.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_21.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | blackwater_mountain74, blackwater_mountain74_h, blackwater_mountain75 |
| **Class** | Animal |
| **HP** | 61 |
| **XP when defeated** | 196 |
| **Entry ID** | `bwm_olm1` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 61 |
| XP when defeated | 196 |
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
| Critical hit chance | 9% |

**When hit:** On self: [Panic](../conditions/panic.md) (magnitude 1, 1 round, 20% chance)


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


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bwm_olm1` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
