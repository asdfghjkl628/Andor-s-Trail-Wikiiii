---
description: "Spotted tentaslime is an enemy in Andor's Trail (construct) with 150 HP, worth 333 XP, found in gamjee_well_1_1, gamjee_well_2_1, gamjee_well_3_1. Drops: Gold coins, Small rock, Slime essence."
---

# ![](../assets/icons/monsters/monsters_rltiles1_145.png){ .sprite } Spotted tentaslime

**Found in:** [gamjee_well_1_1](../maps/gamjee_well_1_1.md), [gamjee_well_2_1](../maps/gamjee_well_2_1.md), [gamjee_well_3_1](../maps/gamjee_well_3_1.md), [gamjee_well_4_1](../maps/gamjee_well_4_1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_145.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | gamjee_well_1_1, gamjee_well_2_1, gamjee_well_3_1 |
| **Class** | Construct |
| **HP** | 150 |
| **XP when defeated** | 333 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `spotted_tentaslime` |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 150 |
| XP when defeated | 333 |
| Damage | 8 to 14 |
| Attack chance | 107 |
| Block chance | 85 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 6 AP |
| Critical skill | 7 |
| Critical multiplier | 2.0 |
| Critical hit chance | 6% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: Corrosive slime (magnitude 3, 5 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 3 to 15 |
| [Small rock](../items/rock.md) | 45% | 1 to 2 |
| [Slime essence](../items/slime_essence.md) | 2% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gamjee_well_1_1](../maps/gamjee_well_1_1.md) | – | 1 | – |
| [gamjee_well_2_1](../maps/gamjee_well_2_1.md) | – | 4 | – |
| [gamjee_well_3_1](../maps/gamjee_well_3_1.md) | – | 2 | – |
| [gamjee_well_4_1](../maps/gamjee_well_4_1.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `spotted_tentaslime` |
    | Spawn group | `spotted_tentaslime` |
    | Loot table | `spotted_tentaslime_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:145` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "spotted_tentaslime",
     "name": "Spotted tentaslime",
     "iconID": "monsters_rltiles1:145",
     "maxHP": 150,
     "moveCost": 6,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 8,
      "max": 14
     },
     "droplistID": "spotted_tentaslime_dl",
     "attackCost": 5,
     "attackChance": 107,
     "criticalSkill": 7,
     "criticalMultiplier": 2.0,
     "blockChance": 85,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "slime",
        "magnitude": 3,
        "duration": 5,
        "chance": "40"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spotted_tentaslime.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spotted_tentaslime.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spotted_tentaslime.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spotted_tentaslime.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
