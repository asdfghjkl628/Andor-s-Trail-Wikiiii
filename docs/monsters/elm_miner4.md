---
description: "Prim guard skeleton is an enemy in Andor's Trail (undead) with 104–364 HP, worth 399–894 XP, found in elm5f_1, elm5f_2, elm_4f_1, elm5f_2. Drops: Bone, Human skull, Gold coins, Small empty vial."
---

# ![](../assets/icons/monsters/monsters_omi2_19.png){ .sprite } Prim guard skeleton

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_19.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | elm5f_1, elm5f_2, elm_4f_1, elm5f_2 |
| **Class** | Undead |
| **HP** | 104–364 |
| **XP when defeated** | 399–894 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Prim guard skeleton. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`elm_miner4`](#v-elm_miner4) | Enemy | [elm5f_1](../maps/elm5f_1.md), [elm5f_2](../maps/elm5f_2.md) (+3 more) | – | 104 |
| [`elm_miner4a`](#v-elm_miner4a) | Enemy | [elm5f_2](../maps/elm5f_2.md) | – | 364 |

## Elm5f 1 and 4 more (elm_miner4) { #v-elm_miner4 }

**Entry ID:** `elm_miner4` · **Type:** Enemy

**Location:** [elm5f_1](../maps/elm5f_1.md), [elm5f_2](../maps/elm5f_2.md), [elm_4f_1](../maps/elm_4f_1.md), [elm_4f_3](../maps/elm_4f_3.md), [elm_4f_4](../maps/elm_4f_4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 104 |
| XP when defeated | 399 |
| Damage | 12 to 16 |
| Attack chance | 172 |
| Block chance | 144 |
| Damage resistance | 7 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 2.5 |
| Critical hit chance | 9% |

**On hit:** Heal HP: 2 to 4; On target: Bleeding wound (magnitude 5, 2 rounds, 25% chance)

**When hit:** On target: Nausea (magnitude 5, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 16.6667% | 1 to 3 |
| [Human skull](../items/skull1.md) | 16.6667% | 1 |
| [Gold coins](../items/gold.md) | 100% | 8 to 21 |
| [Small empty vial](../items/vial_empty1.md) | 11.1111% | 1 |
| [Small vial of mountain water](../items/bwm_water0.md) | 5% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 2.5% | 1 |
| [Pine spear](../items/spear1.md) | 0.8% | 1 |
| [Steel cuirass](../items/cuirass_steel.md) | 0.4% | 1 |
| [Blackwater rusted pickaxe](../items/bwm_pick.md) | 0.8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [elm5f_1](../maps/elm5f_1.md) | – | 8 | – |
| [elm5f_2](../maps/elm5f_2.md) | – | 7 | – |
| [elm_4f_1](../maps/elm_4f_1.md) | – | 2 | – |
| [elm_4f_3](../maps/elm_4f_3.md) | – | 2 | – |
| [elm_4f_4](../maps/elm_4f_4.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (elm_miner4)"

    | | |
    |---|---|
    | Entry ID | `elm_miner4` |
    | Spawn group | `elm_mine5` |
    | Loot table | `elm_miner2` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_omi2:19` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner4",
     "name": "Prim guard skeleton",
     "iconID": "monsters_omi2:19",
     "maxHP": 104,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 16
     },
     "spawnGroup": "elm_mine5",
     "droplistID": "elm_miner2",
     "attackCost": 5,
     "attackChance": 172,
     "criticalSkill": 10,
     "criticalMultiplier": 2.5,
     "blockChance": 144,
     "damageResistance": 7,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "deathEffect": {}
    }
    ```


## Elm5f 2 (elm_miner4a) { #v-elm_miner4a }

**Entry ID:** `elm_miner4a` · **Type:** Enemy

**Location:** [elm5f_2](../maps/elm5f_2.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 364 |
| XP when defeated | 894 |
| Damage | 12 to 16 |
| Attack chance | 182 |
| Block chance | 154 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 2.5 |
| Critical hit chance | 9% |

**On hit:** Heal HP: 2 to 4; On target: Bleeding wound (magnitude 5, 2 rounds, 25% chance)

**When hit:** On target: Nausea (magnitude 5, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 100% | 1 to 2 |
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 60 to 180 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [elm5f_2](../maps/elm5f_2.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.8.5](../versions/0.8.5.md) | maxHP: 104 → 364 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (elm_miner4a)"

    | | |
    |---|---|
    | Entry ID | `elm_miner4a` |
    | Spawn group | `elm_mine4a` |
    | Loot table | `elm_miner4a` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_omi2:19` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "elm_miner4a",
     "name": "Prim guard skeleton",
     "iconID": "monsters_omi2:19",
     "maxHP": 364,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 16
     },
     "spawnGroup": "elm_mine4a",
     "droplistID": "elm_miner4a",
     "attackCost": 5,
     "attackChance": 182,
     "criticalSkill": 10,
     "criticalMultiplier": 2.5,
     "blockChance": 154,
     "damageResistance": 10,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 5,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 5,
        "duration": 2,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elm_miner4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
