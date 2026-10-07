---
description: "Drybone lich is an enemy in Andor's Trail (undead) with 212 HP, worth 614 XP, found in undertell_00, undertell_10, undertell_11. Drops: Gold coins, Tattered coin purse, Lich dust, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_tometik8_48.png){ .sprite } Drybone lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_48.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | undertell_00, undertell_10, undertell_11 |
| **Class** | Undead |
| **HP** | 212 |
| **XP when defeated** | 614 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Drybone lich. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`drybone_lich`](#v-drybone_lich) | Enemy | [undertell_00](../maps/undertell_00.md), [undertell_10](../maps/undertell_10.md) (+8 more) | – | 212 |
| [`drybone_lich_help_liches`](#v-drybone_lich_help_liches) | Enemy | Not on a map | – | 212 |

## Undertell 00 and 9 more (drybone_lich) { #v-drybone_lich }

**Entry ID:** `drybone_lich` · **Type:** Enemy

**Location:** [undertell_00](../maps/undertell_00.md), [undertell_10](../maps/undertell_10.md), [undertell_11](../maps/undertell_11.md), [undertell_12](../maps/undertell_12.md), [undertell_13](../maps/undertell_13.md), [undertell_21](../maps/undertell_21.md) (+4 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 212 |
| XP when defeated | 614 |
| Damage | 8 to 10 |
| Attack chance | 198 |
| Block chance | 185 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |

**On hit:** On target: Withering Focus (magnitude 4, 2 rounds, 22% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 6 to 12 |
| [Tattered coin purse](../items/lich_purse.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 5% | 1 |
| [Tonic of blood](../items/tonic_of_blood.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_00](../maps/undertell_00.md) | – | 3 | – |
| [undertell_10](../maps/undertell_10.md) | – | 4 | – |
| [undertell_11](../maps/undertell_11.md) | – | 5 | – |
| [undertell_12](../maps/undertell_12.md) | – | 5 | – |
| [undertell_13](../maps/undertell_13.md) | – | 2 | – |
| [undertell_21](../maps/undertell_21.md) | – | 2 | – |
| [undertell_22](../maps/undertell_22.md) | – | 1 | – |
| [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 1 | – |
| [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 1 | – |
| [undertell_3_lava_11](../maps/undertell_3_lava_11.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (drybone_lich)"

    | | |
    |---|---|
    | Entry ID | `drybone_lich` |
    | Spawn group | `lich_spawn1` |
    | Loot table | `drybone_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:48` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "drybone_lich",
     "name": "Drybone lich",
     "iconID": "monsters_tometik8:48",
     "maxHP": 212,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
     "spawnGroup": "lich_spawn1",
     "droplistID": "drybone_lich_dl",
     "attackCost": 4,
     "attackChance": 198,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 185,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "withering_focus",
        "magnitude": 4,
        "duration": 2,
        "chance": "22"
       }
      ]
     }
    }
    ```


## Not placed on a map (drybone_lich_help_liches) { #v-drybone_lich_help_liches }

**Entry ID:** `drybone_lich_help_liches` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 212 |
| XP when defeated | 614 |
| Damage | 8 to 10 |
| Attack chance | 198 |
| Block chance | 185 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |

**On hit:** On target: Withering Focus (magnitude 4, 2 rounds, 22% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 6 to 12 |
| [Tattered coin purse](../items/lich_purse.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 5% | 1 |
| [Tonic of blood](../items/tonic_of_blood.md) | 10% | 1 |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (drybone_lich_help_liches)"

    | | |
    |---|---|
    | Entry ID | `drybone_lich_help_liches` |
    | Spawn group | `helpLich` |
    | Loot table | `drybone_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:48` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "drybone_lich_help_liches",
     "name": "Drybone lich",
     "iconID": "monsters_tometik8:48",
     "maxHP": 212,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 10
     },
     "spawnGroup": "helpLich",
     "droplistID": "drybone_lich_dl",
     "attackCost": 4,
     "attackChance": 198,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 185,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "withering_focus",
        "magnitude": 4,
        "duration": 2,
        "chance": "22"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drybone_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drybone_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drybone_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drybone_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
