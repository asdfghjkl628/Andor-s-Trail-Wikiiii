---
description: "Strong maonit brute is an enemy in Andor's Trail (giant) with 320–620 HP, worth 384–636 XP, found in Lake Laeroth. Drops: Gold coins, Meat, Animal hair, Crude ring of block."
---

# ![](../assets/icons/monsters/monsters_rltiles1_107.png){ .sprite } Strong maonit brute

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_107.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Giant |
| **HP** | 320–620 |
| **XP when defeated** | 384–636 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Strong maonit brute. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`maonit_6`](#v-maonit_6) | Enemy | Lake Laeroth: [mountainlake3](../maps/mountainlake3.md), [mountainlake4](../maps/mountainlake4.md) (+2 more) | – | 320 |
| [`maonit_cr`](#v-maonit_cr) | Enemy | Lake Laeroth: [mountainlake1](../maps/mountainlake1.md) | – | 620 |

## Lake Laeroth, Mountainlake3 and 3 more (maonit_6) { #v-maonit_6 }

**Entry ID:** `maonit_6` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake3](../maps/mountainlake3.md), [mountainlake4](../maps/mountainlake4.md), [mountainlake5](../maps/mountainlake5.md), [waytolake11](../maps/waytolake11.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 320 |
| XP when defeated | 384 |
| Damage | 1 to 20 |
| Attack chance | 65 |
| Block chance | 20 |
| Damage resistance | 6 |
| Max AP | 5 |
| Attack cost | 4 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Critical hit chance | 19% |

**On hit:** On target: Stunned (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 7 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 10% | 1 |
| [Crude ring of block](../items/ring_crude_block.md) | 1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake3](../maps/mountainlake3.md) | Lake Laeroth | 4 | – |
| [mountainlake4](../maps/mountainlake4.md) | – | 3 | – |
| [mountainlake5](../maps/mountainlake5.md) | – | 2 | – |
| [waytolake11](../maps/waytolake11.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 10, "c… → {"conditionsTarget": [{"chance": "10", …; name: Strong Maonit brute → Strong maonit brute |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 5 → 4 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (maonit_6)"

    | | |
    |---|---|
    | Entry ID | `maonit_6` |
    | Spawn group | `maonit_3` |
    | Loot table | `maonit` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:107` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "maonit_6",
     "name": "Strong maonit brute",
     "iconID": "monsters_rltiles1:107",
     "maxHP": 320,
     "maxAP": 5,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 1,
      "max": 20
     },
     "spawnGroup": "maonit_3",
     "droplistID": "maonit",
     "attackCost": 4,
     "attackChance": 65,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 20,
     "damageResistance": 6,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Lake Laeroth, Mountainlake1 (maonit_cr) { #v-maonit_cr }

**Entry ID:** `maonit_cr` · **Type:** Enemy

**Location:** Lake Laeroth: [mountainlake1](../maps/mountainlake1.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 620 |
| XP when defeated | 636 |
| Damage | 1 to 20 |
| Attack chance | 65 |
| Block chance | 20 |
| Damage resistance | 6 |
| Max AP | 5 |
| Attack cost | 4 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Critical hit chance | 19% |

**On hit:** On target: Stunned (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake1](../maps/mountainlake1.md) | Lake Laeroth | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 10, "c… → {"conditionsTarget": [{"chance": "10", …; name: Strong Maonit brute → Strong maonit brute |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 5 → 4 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (maonit_cr)"

    | | |
    |---|---|
    | Entry ID | `maonit_cr` |
    | Spawn group | `maonit_cr` |
    | Loot table | `oegyth1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:107` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "maonit_cr",
     "name": "Strong maonit brute",
     "iconID": "monsters_rltiles1:107",
     "maxHP": 620,
     "maxAP": 5,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 1,
      "max": 20
     },
     "spawnGroup": "maonit_cr",
     "droplistID": "oegyth1",
     "attackCost": 4,
     "attackChance": 65,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 20,
     "damageResistance": 6,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
