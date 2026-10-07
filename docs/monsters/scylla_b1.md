---
description: "Furious Scylla is an enemy in Andor's Trail (animal) with 180 HP, worth 1972 XP, found in mountainlake32."
---

# ![](../assets/icons/monsters/monsters_ld2_18.png){ .sprite } Furious Scylla

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | mountainlake32 |
| **Class** | Animal |
| **HP** | 180 |
| **XP when defeated** | 1,972 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Furious Scylla. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`scylla_b1`](#v-scylla_b1) | Enemy | [mountainlake32](../maps/mountainlake32.md) | – | 180 |
| [`scylla_b2`](#v-scylla_b2) | Enemy | [mountainlake32](../maps/mountainlake32.md) | – | 180 |

## Mountainlake32 (scylla_b1) { #v-scylla_b1 }

**Entry ID:** `scylla_b1` · **Type:** Enemy

**Location:** [mountainlake32](../maps/mountainlake32.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 180 |
| XP when defeated | 1,972 |
| Damage | 1 to 15 |
| Attack chance | 250 |
| Block chance | 600 |
| Damage resistance | 150 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 1.2 |
| Critical hit chance | 9% |

**On hit:** Heal HP: 180; On target: [Scylla's bite](../conditions/scylla.md) (magnitude 3, 1 round)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake32](../maps/mountainlake32.md) | – | 6 | Appears later, during a quest |

### Quests that count defeats

- [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-66) with stepping on a trigger on [mountainlake32](../maps/mountainlake32.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (scylla_b1)"

    | | |
    |---|---|
    | Entry ID | `scylla_b1` |
    | Spawn group | `scylla_b` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "scylla_b1",
     "name": "Furious Scylla",
     "iconID": "monsters_ld2:18",
     "maxHP": 180,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 15
     },
     "spawnGroup": "scylla_b",
     "attackCost": 5,
     "attackChance": 250,
     "criticalSkill": 10,
     "criticalMultiplier": 1.2,
     "blockChance": 600,
     "damageResistance": 150,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 180,
       "max": 180
      },
      "conditionsTarget": [
       {
        "condition": "scylla",
        "magnitude": 3,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Mountainlake32 (scylla_b2) { #v-scylla_b2 }

**Entry ID:** `scylla_b2` · **Type:** Enemy

**Location:** [mountainlake32](../maps/mountainlake32.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 180 |
| XP when defeated | 1,972 |
| Damage | 1 to 15 |
| Attack chance | 250 |
| Block chance | 600 |
| Damage resistance | 150 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 1.2 |
| Critical hit chance | 9% |

**On hit:** Heal HP: 180; On target: [Scylla's bite](../conditions/scylla.md) (magnitude 3, 1 round)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake32](../maps/mountainlake32.md) | – | 6 | Appears later, during a quest |

### Quests that count defeats

- [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-66) with stepping on a trigger on [mountainlake32](../maps/mountainlake32.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (scylla_b2)"

    | | |
    |---|---|
    | Entry ID | `scylla_b2` |
    | Spawn group | `scylla_b` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:19` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "scylla_b2",
     "name": "Furious Scylla",
     "iconID": "monsters_ld2:19",
     "maxHP": 180,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 15
     },
     "spawnGroup": "scylla_b",
     "attackCost": 5,
     "attackChance": 250,
     "criticalSkill": 10,
     "criticalMultiplier": 1.2,
     "blockChance": 600,
     "damageResistance": 150,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 180,
       "max": 180
      },
      "conditionsTarget": [
       {
        "condition": "scylla",
        "magnitude": 3,
        "duration": 1,
        "chance": "100"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_b1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_b1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_b1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_b1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
