---
description: "Bone-Marshal lich is an enemy in Andor's Trail (undead) with 232 HP, worth 693 XP, found in undertell_11, undertell_12, undertell_21, undertell_00, undertell_10, undertell_12, undertell_11, undertell_10, undertell_11, undertell_21, undertell_21, undertell_3_lava_01, undertell_4_01. Drops: Gold…"
---

# ![](../assets/icons/monsters/monsters_tometik8_42.png){ .sprite } Bone-Marshal lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_42.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | undertell_11, undertell_12, undertell_21, undertell_00, undertell_10, undertell_12, undertell_11, undertell_10, undertell_11, undertell_21, undertell_21, undertell_3_lava_01, undertell_4_01 |
| **Class** | Undead |
| **HP** | 232 |
| **XP when defeated** | 693 |
| **Entries in game data** | 5 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "5 entries in the game data"
    The game's data files define 5 separate characters named Bone-Marshal lich. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, loot or shop stock, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`bone_marshal_lich`](#v-bone_marshal_lich) | Enemy | [undertell_11](../maps/undertell_11.md), [undertell_12](../maps/undertell_12.md) (+1 more) | – | 232 |
| [`bone_marshal_lich_help_liches`](#v-bone_marshal_lich_help_liches) | Enemy | [undertell_00](../maps/undertell_00.md), [undertell_10](../maps/undertell_10.md) (+1 more) | – | 232 |
| [`bone_marshal_lich_help_others`](#v-bone_marshal_lich_help_others) | Enemy | [undertell_11](../maps/undertell_11.md) | – | 232 |
| [`bone_marshal_lich_help_plague`](#v-bone_marshal_lich_help_plague) | Enemy | [undertell_10](../maps/undertell_10.md), [undertell_11](../maps/undertell_11.md) (+1 more) | – | 232 |
| [`bone_marshal_lich_pearl`](#v-bone_marshal_lich_pearl) | Enemy | [undertell_21](../maps/undertell_21.md), [undertell_3_lava_01](../maps/undertell_3_lava_01.md) (+3 more) | – | 232 |

## Undertell 11 and 2 more (bone_marshal_lich) { #v-bone_marshal_lich }

**Entry ID:** `bone_marshal_lich` · **Type:** Enemy

**Location:** [undertell_11](../maps/undertell_11.md), [undertell_12](../maps/undertell_12.md), [undertell_21](../maps/undertell_21.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 232 |
| XP when defeated | 693 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 9 to 13 |
| [Marshal sigil](../items/marshal_sigil.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_11](../maps/undertell_11.md) | – | 1 | – |
| [undertell_12](../maps/undertell_12.md) | – | 2 | – |
| [undertell_21](../maps/undertell_21.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bone_marshal_lich)"

    | | |
    |---|---|
    | Entry ID | `bone_marshal_lich` |
    | Spawn group | `lich_spawn1` |
    | Loot table | `marshal_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "lich_spawn1",
     "droplistID": "marshal_lich_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Undertell 00 and 2 more (bone_marshal_lich_help_liches) { #v-bone_marshal_lich_help_liches }

**Entry ID:** `bone_marshal_lich_help_liches` · **Type:** Enemy

**Location:** [undertell_00](../maps/undertell_00.md), [undertell_10](../maps/undertell_10.md), [undertell_12](../maps/undertell_12.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 232 |
| XP when defeated | 693 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 9 to 13 |
| [Marshal sigil](../items/marshal_sigil.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_00](../maps/undertell_00.md) | – | 1 | – |
| [undertell_10](../maps/undertell_10.md) | – | 1 | – |
| [undertell_12](../maps/undertell_12.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bone_marshal_lich_help_liches)"

    | | |
    |---|---|
    | Entry ID | `bone_marshal_lich_help_liches` |
    | Spawn group | `helpLich` |
    | Loot table | `marshal_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich_help_liches",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "helpLich",
     "droplistID": "marshal_lich_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Undertell 11 (bone_marshal_lich_help_others) { #v-bone_marshal_lich_help_others }

**Entry ID:** `bone_marshal_lich_help_others` · **Type:** Enemy

**Location:** [undertell_11](../maps/undertell_11.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 232 |
| XP when defeated | 693 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 9 to 13 |
| [Marshal sigil](../items/marshal_sigil.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_11](../maps/undertell_11.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bone_marshal_lich_help_others)"

    | | |
    |---|---|
    | Entry ID | `bone_marshal_lich_help_others` |
    | Spawn group | `helpOthers` |
    | Loot table | `marshal_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich_help_others",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "helpOthers",
     "droplistID": "marshal_lich_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Undertell 10 and 2 more (bone_marshal_lich_help_plague) { #v-bone_marshal_lich_help_plague }

**Entry ID:** `bone_marshal_lich_help_plague` · **Type:** Enemy

**Location:** [undertell_10](../maps/undertell_10.md), [undertell_11](../maps/undertell_11.md), [undertell_21](../maps/undertell_21.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 232 |
| XP when defeated | 693 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 35% | 9 to 13 |
| [Marshal sigil](../items/marshal_sigil.md) | 1% | 1 |
| [Lich dust](../items/lich_dust.md) | 8% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_10](../maps/undertell_10.md) | – | 1 | – |
| [undertell_11](../maps/undertell_11.md) | – | 1 | – |
| [undertell_21](../maps/undertell_21.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bone_marshal_lich_help_plague)"

    | | |
    |---|---|
    | Entry ID | `bone_marshal_lich_help_plague` |
    | Spawn group | `helpPlagueLich` |
    | Loot table | `marshal_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich_help_plague",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "helpPlagueLich",
     "droplistID": "marshal_lich_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Undertell 21 and 4 more (bone_marshal_lich_pearl) { #v-bone_marshal_lich_pearl }

**Entry ID:** `bone_marshal_lich_pearl` · **Type:** Enemy

**Location:** [undertell_21](../maps/undertell_21.md), [undertell_3_lava_01](../maps/undertell_3_lava_01.md), [undertell_4_01](../maps/undertell_4_01.md), [undertell_5](../maps/undertell_5.md), [undertell_7_10](../maps/undertell_7_10.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 232 |
| XP when defeated | 693 |
| Damage | 9 to 11 |
| Attack chance | 202 |
| Block chance | 195 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 13 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: Kazaul exposure (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Soul pearl](../items/soul_pearl.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_21](../maps/undertell_21.md) | – | 1 | Appears later, during a quest |
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 1 | Appears later, during a quest |
| [undertell_4_01](../maps/undertell_4_01.md) | – | 1 | Appears later, during a quest |
| [undertell_5](../maps/undertell_5.md) | – | 1 | Appears later, during a quest |
| [undertell_7_10](../maps/undertell_7_10.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (bone_marshal_lich_pearl)"

    | | |
    |---|---|
    | Entry ID | `bone_marshal_lich_pearl` |
    | Spawn group | `lich_spawn1` |
    | Loot table | `soul_pearl_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:42` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "bone_marshal_lich_pearl",
     "name": "Bone-Marshal lich",
     "iconID": "monsters_tometik8:42",
     "maxHP": 232,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "lich_spawn1",
     "horizontalFlipChance": 50,
     "droplistID": "soul_pearl_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 195,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 1,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bone_marshal_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
