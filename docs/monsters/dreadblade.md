---
description: "Dreadstaff lich is an enemy in Andor's Trail (undead) with 285 HP, worth 822 XP, found in undertell_3_lava_10, undertell_3_lava_11, undertell_4_11, undertell_3_lava_00, undertell_3_lava_01, undertell_3_lava_10. Drops: Gold coins, Lich dust, Major potion of health, Kazaul bonemeal."
---

# ![](../assets/icons/monsters/monsters_antison_2.png){ .sprite } Dreadstaff lich

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_antison_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | undertell_3_lava_10, undertell_3_lava_11, undertell_4_11, undertell_3_lava_00, undertell_3_lava_01, undertell_3_lava_10 |
| **Class** | Undead |
| **HP** | 285 |
| **XP when defeated** | 822 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Dreadstaff lich. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`dreadblade`](#v-dreadblade) | Enemy | [undertell_3_lava_10](../maps/undertell_3_lava_10.md), [undertell_3_lava_11](../maps/undertell_3_lava_11.md) (+3 more) | – | 285 |
| [`dreadstaff_help_liches`](#v-dreadstaff_help_liches) | Enemy | [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 285 |
| [`dreadstaff_help_plague`](#v-dreadstaff_help_plague) | Enemy | [undertell_3_lava_01](../maps/undertell_3_lava_01.md), [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 285 |

## Undertell 3 lava 10 and 4 more (dreadblade) { #v-dreadblade }

**Entry ID:** `dreadblade` · **Type:** Enemy

**Location:** [undertell_3_lava_10](../maps/undertell_3_lava_10.md), [undertell_3_lava_11](../maps/undertell_3_lava_11.md), [undertell_4_11](../maps/undertell_4_11.md), [undertell_5](../maps/undertell_5.md), [undertell_7_01](../maps/undertell_7_01.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 285 |
| XP when defeated | 822 |
| Damage | 10 to 13 |
| Attack chance | 210 |
| Block chance | 185 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 2.1 |
| Critical hit chance | 12% |

**On hit:** On target: Kazaul exposure (magnitude 2, 3 rounds, 18% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 9 to 12 |
| [Lich dust](../items/lich_dust.md) | 10% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 1 | – |
| [undertell_3_lava_11](../maps/undertell_3_lava_11.md) | – | 1 | – |
| [undertell_4_11](../maps/undertell_4_11.md) | – | 1 | – |
| [undertell_5](../maps/undertell_5.md) | – | 5 | – |
| [undertell_7_01](../maps/undertell_7_01.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dreadblade)"

    | | |
    |---|---|
    | Entry ID | `dreadblade` |
    | Spawn group | `dreadblade` |
    | Loot table | `dreadblade_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_antison:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "dreadblade",
     "name": "Dreadstaff lich",
     "iconID": "monsters_antison:2",
     "maxHP": 285,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "horizontalFlipChance": 50,
     "droplistID": "dreadblade_lich_dl",
     "attackCost": 4,
     "attackChance": 210,
     "criticalSkill": 15,
     "criticalMultiplier": 2.1,
     "blockChance": 185,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 2,
        "duration": 3,
        "chance": "18"
       }
      ]
     }
    }
    ```


## Undertell 3 lava 00 (dreadstaff_help_liches) { #v-dreadstaff_help_liches }

**Entry ID:** `dreadstaff_help_liches` · **Type:** Enemy

**Location:** [undertell_3_lava_00](../maps/undertell_3_lava_00.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 285 |
| XP when defeated | 822 |
| Damage | 10 to 13 |
| Attack chance | 210 |
| Block chance | 185 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 2.1 |
| Critical hit chance | 12% |

**On hit:** On target: Kazaul exposure (magnitude 2, 3 rounds, 18% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 9 to 12 |
| [Lich dust](../items/lich_dust.md) | 10% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dreadstaff_help_liches)"

    | | |
    |---|---|
    | Entry ID | `dreadstaff_help_liches` |
    | Spawn group | `helpLich` |
    | Loot table | `dreadblade_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_antison:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "dreadstaff_help_liches",
     "name": "Dreadstaff lich",
     "iconID": "monsters_antison:2",
     "maxHP": 285,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "spawnGroup": "helpLich",
     "horizontalFlipChance": 50,
     "droplistID": "dreadblade_lich_dl",
     "attackCost": 4,
     "attackChance": 210,
     "criticalSkill": 15,
     "criticalMultiplier": 2.1,
     "blockChance": 185,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 2,
        "duration": 3,
        "chance": "18"
       }
      ]
     }
    }
    ```


## Undertell 3 lava 01 and 1 more (dreadstaff_help_plague) { #v-dreadstaff_help_plague }

**Entry ID:** `dreadstaff_help_plague` · **Type:** Enemy

**Location:** [undertell_3_lava_01](../maps/undertell_3_lava_01.md), [undertell_3_lava_10](../maps/undertell_3_lava_10.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 285 |
| XP when defeated | 822 |
| Damage | 10 to 13 |
| Attack chance | 210 |
| Block chance | 185 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 15 |
| Critical multiplier | 2.1 |
| Critical hit chance | 12% |

**On hit:** On target: Kazaul exposure (magnitude 2, 3 rounds, 18% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 9 to 12 |
| [Lich dust](../items/lich_dust.md) | 10% | 1 |
| [Major potion of health](../items/health_major2.md) | 30% | 1 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 2 | – |
| [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dreadstaff_help_plague)"

    | | |
    |---|---|
    | Entry ID | `dreadstaff_help_plague` |
    | Spawn group | `helpPlagueLich` |
    | Loot table | `dreadblade_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_antison:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "dreadstaff_help_plague",
     "name": "Dreadstaff lich",
     "iconID": "monsters_antison:2",
     "maxHP": 285,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "spawnGroup": "helpPlagueLich",
     "horizontalFlipChance": 50,
     "droplistID": "dreadblade_lich_dl",
     "attackCost": 4,
     "attackChance": 210,
     "criticalSkill": 15,
     "criticalMultiplier": 2.1,
     "blockChance": 185,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "kazaul_exposure",
        "magnitude": 2,
        "duration": 3,
        "chance": "18"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadblade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadblade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadblade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadblade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
