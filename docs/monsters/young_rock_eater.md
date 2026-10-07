---
description: "Young rock eater is an enemy in Andor's Trail (construct) with 303 HP, worth 744 XP, found in Undertell 12, Undertell 13, Undertell 14. Drops: Small rock, Gold coins."
---

# ![](../assets/icons/monsters/monsters_rltiles1_55.png){ .sprite } Young rock eater

**Found in:** [Undertell 12](../maps/undertell_12.md), [Undertell 13](../maps/undertell_13.md), [Undertell 14](../maps/undertell_14.md), [Undertell 15](../maps/undertell_15.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_55.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 12, Undertell 13, Undertell 14 |
| **Class** | Construct |
| **HP** | 303 |
| **XP when defeated** | 744 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `young_rock_eater` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 303 |
| XP when defeated | 744 |
| Damage | 8 to 10 |
| Attack chance | 228 |
| Block chance | 165 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 17 |
| Critical multiplier | 1.8 |
| Critical hit chance | 13% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On self: [Petristill](../conditions/petristill.md) (magnitude 1, 5 rounds, 45% chance); On target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 1, 1 round, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 65% | 3 to 6 |
| [Gold coins](../items/gold.md) | 35% | 4 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 12](../maps/undertell_12.md) | – | 3 | – |
| [Undertell 13](../maps/undertell_13.md) | – | 4 | – |
| [Undertell 14](../maps/undertell_14.md) | – | 3 | – |
| [Undertell 15](../maps/undertell_15.md) | – | 1 | – |
| [Undertell 22](../maps/undertell_22.md) | – | 2 | – |
| [Undertell 23](../maps/undertell_23.md) | – | 1 | – |
| [Undertell 24](../maps/undertell_24.md) | – | 1 | – |
| [Undertell 3 00](../maps/undertell_3_00.md) | – | 3 | – |
| [Undertell 3 01](../maps/undertell_3_01.md) | – | 6 | – |
| [Undertell 3 03](../maps/undertell_3_03.md) | – | 4 | – |
| [Undertell 3 10](../maps/undertell_3_10.md) | – | 3 | – |
| [Undertell 3 11](../maps/undertell_3_11.md) | – | 3 | – |
| [Undertell 3 12](../maps/undertell_3_12.md) | – | 4 | – |
| [Undertell 3 13](../maps/undertell_3_13.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `young_rock_eater` |
    | Spawn group | `young_rock_eater` |
    | Loot table | `young_rock_eater_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:55` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "young_rock_eater",
     "name": "Young rock eater",
     "iconID": "monsters_rltiles1:55",
     "maxHP": 303,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
     "droplistID": "young_rock_eater_dl",
     "attackCost": 5,
     "attackChance": 228,
     "criticalSkill": 17,
     "criticalMultiplier": 1.8,
     "blockChance": 165,
     "damageResistance": 11,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "petristill",
        "magnitude": 1,
        "duration": 5,
        "chance": "45"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 1,
        "duration": 1,
        "chance": "25"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
