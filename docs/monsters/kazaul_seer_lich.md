---
description: "Kazaul seer lich is an enemy in Andor's Trail (undead) with 295 HP, worth 842 XP, found in undertell_4_01, undertell_5, undertell_4_00, undertell_4_11, undertell_7_11, undertell_4_00, undertell_4_01, undertell_4_10, undertell_4_00, undertell_4_10, undertell_4_11. Drops: Gold coins, Lich dust,…"
---

# ![](../assets/icons/monsters/monsters_antison_3.png){ .sprite } Kazaul seer lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_antison_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | undertell_4_01, undertell_5, undertell_4_00, undertell_4_11, undertell_7_11, undertell_4_00, undertell_4_01, undertell_4_10, undertell_4_00, undertell_4_10, undertell_4_11 |
| **Class** | Undead |
| **HP** | 295 |
| **XP when defeated** | 842 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "4 entries in the game data"
    The game's data files define 4 separate characters named Kazaul seer lich. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`kazaul_seer_lich`](#v-kazaul_seer_lich) | Enemy | [undertell_4_01](../maps/undertell_4_01.md), [undertell_5](../maps/undertell_5.md) | – | 295 |
| [`kazaul_seer_lich_help_liches`](#v-kazaul_seer_lich_help_liches) | Enemy | [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_11](../maps/undertell_4_11.md) (+1 more) | – | 295 |
| [`kazaul_seer_lich_help_others`](#v-kazaul_seer_lich_help_others) | Enemy | [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_01](../maps/undertell_4_01.md) (+3 more) | – | 295 |
| [`kazaul_seer_lich_help_plague`](#v-kazaul_seer_lich_help_plague) | Enemy | [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_10](../maps/undertell_4_10.md) (+5 more) | – | 295 |

## Undertell 4 01 and 1 more (kazaul_seer_lich) { #v-kazaul_seer_lich }

**Entry ID:** `kazaul_seer_lich` · **Type:** Enemy

**Location:** [undertell_4_01](../maps/undertell_4_01.md), [undertell_5](../maps/undertell_5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 295 |
| XP when defeated | 842 |
| Damage | 10 to 12 |
| Attack chance | 208 |
| Block chance | 190 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 14 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Mind fog](../conditions/mind_fog.md) (magnitude 1, 2 rounds, 18% chance)

**When hit:** On target: [Kazaul possession](../conditions/kazarite_misery.md) (magnitude 1, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 9 to 10 |
| [Lich dust](../items/lich_dust.md) | 11% | 1 |
| [Major potion of health](../items/health_major2.md) | 40% | 2 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 9% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_4_01](../maps/undertell_4_01.md) | – | 2 | – |
| [undertell_5](../maps/undertell_5.md) | – | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (kazaul_seer_lich)"

    | | |
    |---|---|
    | Entry ID | `kazaul_seer_lich` |
    | Spawn group | `kazaul_seer_lich` |
    | Loot table | `undertell_level4_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_antison:3` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_seer_lich",
     "name": "Kazaul seer lich",
     "iconID": "monsters_antison:3",
     "maxHP": 295,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "droplistID": "undertell_level4_lich_dl",
     "attackCost": 4,
     "attackChance": 208,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 190,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 1,
        "duration": 2,
        "chance": "18"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "kazarite_misery",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Undertell 4 00 and 2 more (kazaul_seer_lich_help_liches) { #v-kazaul_seer_lich_help_liches }

**Entry ID:** `kazaul_seer_lich_help_liches` · **Type:** Enemy

**Location:** [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_11](../maps/undertell_4_11.md), [undertell_7_11](../maps/undertell_7_11.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 295 |
| XP when defeated | 842 |
| Damage | 10 to 12 |
| Attack chance | 208 |
| Block chance | 190 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 14 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Mind fog](../conditions/mind_fog.md) (magnitude 1, 2 rounds, 18% chance)

**When hit:** On target: [Kazaul possession](../conditions/kazarite_misery.md) (magnitude 1, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 9 to 10 |
| [Lich dust](../items/lich_dust.md) | 11% | 1 |
| [Major potion of health](../items/health_major2.md) | 40% | 2 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 9% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_4_00](../maps/undertell_4_00.md) | – | 1 | – |
| [undertell_4_11](../maps/undertell_4_11.md) | – | 1 | – |
| [undertell_7_11](../maps/undertell_7_11.md) | – | 4 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (kazaul_seer_lich_help_liches)"

    | | |
    |---|---|
    | Entry ID | `kazaul_seer_lich_help_liches` |
    | Spawn group | `helpLich` |
    | Loot table | `undertell_level4_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_antison:3` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_seer_lich_help_liches",
     "name": "Kazaul seer lich",
     "iconID": "monsters_antison:3",
     "maxHP": 295,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "spawnGroup": "helpLich",
     "droplistID": "undertell_level4_lich_dl",
     "attackCost": 4,
     "attackChance": 208,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 190,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 1,
        "duration": 2,
        "chance": "18"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "kazarite_misery",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Undertell 4 00 and 4 more (kazaul_seer_lich_help_others) { #v-kazaul_seer_lich_help_others }

**Entry ID:** `kazaul_seer_lich_help_others` · **Type:** Enemy

**Location:** [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_01](../maps/undertell_4_01.md), [undertell_4_10](../maps/undertell_4_10.md), [undertell_4_11](../maps/undertell_4_11.md), [undertell_7_01](../maps/undertell_7_01.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 295 |
| XP when defeated | 842 |
| Damage | 10 to 12 |
| Attack chance | 208 |
| Block chance | 190 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 14 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Mind fog](../conditions/mind_fog.md) (magnitude 1, 2 rounds, 18% chance)

**When hit:** On target: [Kazaul possession](../conditions/kazarite_misery.md) (magnitude 1, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 9 to 10 |
| [Lich dust](../items/lich_dust.md) | 11% | 1 |
| [Major potion of health](../items/health_major2.md) | 40% | 2 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 9% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_4_00](../maps/undertell_4_00.md) | – | 1 | – |
| [undertell_4_01](../maps/undertell_4_01.md) | – | 2 | – |
| [undertell_4_10](../maps/undertell_4_10.md) | – | 1 | – |
| [undertell_4_11](../maps/undertell_4_11.md) | – | 1 | – |
| [undertell_7_01](../maps/undertell_7_01.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (kazaul_seer_lich_help_others)"

    | | |
    |---|---|
    | Entry ID | `kazaul_seer_lich_help_others` |
    | Spawn group | `helpOthers` |
    | Loot table | `undertell_level4_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_antison:3` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_seer_lich_help_others",
     "name": "Kazaul seer lich",
     "iconID": "monsters_antison:3",
     "maxHP": 295,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "spawnGroup": "helpOthers",
     "droplistID": "undertell_level4_lich_dl",
     "attackCost": 4,
     "attackChance": 208,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 190,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 1,
        "duration": 2,
        "chance": "18"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "kazarite_misery",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Undertell 4 00 and 6 more (kazaul_seer_lich_help_plague) { #v-kazaul_seer_lich_help_plague }

**Entry ID:** `kazaul_seer_lich_help_plague` · **Type:** Enemy

**Location:** [undertell_4_00](../maps/undertell_4_00.md), [undertell_4_10](../maps/undertell_4_10.md), [undertell_4_11](../maps/undertell_4_11.md), [undertell_7_00](../maps/undertell_7_00.md), [undertell_7_01](../maps/undertell_7_01.md), [undertell_7_10](../maps/undertell_7_10.md) (+1 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 295 |
| XP when defeated | 842 |
| Damage | 10 to 12 |
| Attack chance | 208 |
| Block chance | 190 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 14 |
| Critical multiplier | 2.0 |
| Critical hit chance | 11% |

**On hit:** On target: [Mind fog](../conditions/mind_fog.md) (magnitude 1, 2 rounds, 18% chance)

**When hit:** On target: [Kazaul possession](../conditions/kazarite_misery.md) (magnitude 1, 2 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 9 to 10 |
| [Lich dust](../items/lich_dust.md) | 11% | 1 |
| [Major potion of health](../items/health_major2.md) | 40% | 2 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 9% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_4_00](../maps/undertell_4_00.md) | – | 1 | – |
| [undertell_4_10](../maps/undertell_4_10.md) | – | 2 | – |
| [undertell_4_11](../maps/undertell_4_11.md) | – | 1 | – |
| [undertell_7_00](../maps/undertell_7_00.md) | – | 2 | – |
| [undertell_7_01](../maps/undertell_7_01.md) | – | 2 | – |
| [undertell_7_10](../maps/undertell_7_10.md) | – | 3 | – |
| [undertell_7_11](../maps/undertell_7_11.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (kazaul_seer_lich_help_plague)"

    | | |
    |---|---|
    | Entry ID | `kazaul_seer_lich_help_plague` |
    | Spawn group | `helpPlagueLich` |
    | Loot table | `undertell_level4_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_antison:3` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_seer_lich_help_plague",
     "name": "Kazaul seer lich",
     "iconID": "monsters_antison:3",
     "maxHP": 295,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 12
     },
     "spawnGroup": "helpPlagueLich",
     "droplistID": "undertell_level4_lich_dl",
     "attackCost": 4,
     "attackChance": 208,
     "criticalSkill": 14,
     "criticalMultiplier": 2.0,
     "blockChance": 190,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 1,
        "duration": 2,
        "chance": "18"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "kazarite_misery",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_seer_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_seer_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_seer_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_seer_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
