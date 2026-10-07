---
description: "Plaguestrider master is an enemy in Andor's Trail (undead) with 65–365 HP, worth 311–921 XP, found in waytolake5. Drops: Regular potion of health, Small empty vial, Silk robe of Valugha, Valugha's shimmering hat."
---

# ![](../assets/icons/monsters/monsters_rltiles2_38.png){ .sprite } Plaguestrider master

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_38.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | waytolake5 |
| **Class** | Undead |
| **HP** | 65–365 |
| **XP when defeated** | 311–921 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Plaguestrider master. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`plaguesp_13`](#v-plaguesp_13) | Enemy | [waytolake5](../maps/waytolake5.md) | – | 65 |
| [`plaguesp_cr`](#v-plaguesp_cr) | Enemy | [waytolake5](../maps/waytolake5.md) | – | 365 |

## Waytolake5 (plaguesp_13) { #v-plaguesp_13 }

**Entry ID:** `plaguesp_13` · **Type:** Enemy

**Location:** [waytolake5](../maps/waytolake5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 65 |
| XP when defeated | 311 |
| Damage | 2 to 8 |
| Attack chance | 85 |
| Block chance | 175 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 120 |
| Critical multiplier | 3.0 |
| Critical hit chance | 43% |

**On hit:** On target: Insect contagion (magnitude 7, 5 rounds, 70% chance); Blistering skin (magnitude 6, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Regular potion of health](../items/health.md) | 10% | 0 to 1 |
| [Small empty vial](../items/vial_empty1.md) | 5% | 1 |
| [Silk robe of Valugha](../items/valugha_gown.md) | 0.1% | 1 |
| [Valugha's shimmering hat](../items/valugha_hat.md) | 0.1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytolake5](../maps/waytolake5.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 70, "c… → {"conditionsTarget": [{"chance": "70", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (plaguesp_13)"

    | | |
    |---|---|
    | Entry ID | `plaguesp_13` |
    | Spawn group | `plaguespider_6` |
    | Loot table | `plaguespider_b` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:38` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "plaguesp_13",
     "name": "Plaguestrider master",
     "iconID": "monsters_rltiles2:38",
     "maxHP": 65,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 8
     },
     "spawnGroup": "plaguespider_6",
     "droplistID": "plaguespider_b",
     "attackCost": 3,
     "attackChance": 85,
     "criticalSkill": 120,
     "criticalMultiplier": 3.0,
     "blockChance": 175,
     "damageResistance": 2,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 7,
        "duration": 5,
        "chance": "70"
       },
       {
        "condition": "blister",
        "magnitude": 6,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Waytolake5 (plaguesp_cr) { #v-plaguesp_cr }

**Entry ID:** `plaguesp_cr` · **Type:** Enemy

**Location:** [waytolake5](../maps/waytolake5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 365 |
| XP when defeated | 921 |
| Damage | 2 to 8 |
| Attack chance | 85 |
| Block chance | 175 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 160 |
| Critical multiplier | 3.0 |
| Critical hit chance | 51% |

**On hit:** On target: Insect contagion (magnitude 4, 5 rounds, 70% chance); Blistering skin (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytolake5](../maps/waytolake5.md) | – | 1 | – |

### Quests that count defeats

- A conversation with stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 70, "c… → {"conditionsTarget": [{"chance": "70", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (plaguesp_cr)"

    | | |
    |---|---|
    | Entry ID | `plaguesp_cr` |
    | Spawn group | `plaguespider_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:38` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "plaguesp_cr",
     "name": "Plaguestrider master",
     "iconID": "monsters_rltiles2:38",
     "maxHP": 365,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 8
     },
     "spawnGroup": "plaguespider_cr",
     "droplistID": "oegyth1",
     "attackCost": 3,
     "attackChance": 85,
     "criticalSkill": 160,
     "criticalMultiplier": 3.0,
     "blockChance": 175,
     "damageResistance": 2,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 4,
        "duration": 5,
        "chance": "70"
       },
       {
        "condition": "blister",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_13.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_13.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_13.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_13.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
