---
description: "Lesser wight is an enemy in Andor's Trail (undead) with 130 HP, worth 174 XP, found in laerothprison6, laerothprison5. Drops: Gold coins, Small rock, Bone."
---

# ![](../assets/icons/monsters/monsters_tometik7_13.png){ .sprite } Lesser wight

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_13.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | laerothprison6, laerothprison5 |
| **Class** | Undead |
| **HP** | 130 |
| **XP when defeated** | 174 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Lesser wight. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`wight_lesser`](#v-wight_lesser) | Enemy | [laerothprison6](../maps/laerothprison6.md) | – | 130 |
| [`wight_lesser5`](#v-wight_lesser5) | Enemy | [laerothprison5](../maps/laerothprison5.md) | – | 130 |
| [`wight_lesser5b`](#v-wight_lesser5b) | Enemy | [laerothprison5](../maps/laerothprison5.md) | – | 130 |

## Laerothprison6 (wight_lesser) { #v-wight_lesser }

**Entry ID:** `wight_lesser` · **Type:** Enemy

**Location:** [laerothprison6](../maps/laerothprison6.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| Attack chance | 65 |
| Block chance | 70 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** Heal HP: 0

**When hit:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothprison6](../maps/laerothprison6.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (wight_lesser)"

    | | |
    |---|---|
    | Entry ID | `wight_lesser` |
    | Spawn group | `wight` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


## Laerothprison5 (wight_lesser5) { #v-wight_lesser5 }

**Entry ID:** `wight_lesser5` · **Type:** Enemy

**Location:** [laerothprison5](../maps/laerothprison5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| Attack chance | 65 |
| Block chance | 70 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** Heal HP: 0

**When hit:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothprison5](../maps/laerothprison5.md) | – | 17 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (wight_lesser5)"

    | | |
    |---|---|
    | Entry ID | `wight_lesser5` |
    | Spawn group | `wight_lesser5` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser5",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight_lesser5",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


## Laerothprison5 (wight_lesser5b) { #v-wight_lesser5b }

**Entry ID:** `wight_lesser5b` · **Type:** Enemy

**Location:** [laerothprison5](../maps/laerothprison5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| Attack chance | 65 |
| Block chance | 70 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** Heal HP: 0

**When hit:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothprison5](../maps/laerothprison5.md) | – | 5 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (wight_lesser5b)"

    | | |
    |---|---|
    | Entry ID | `wight_lesser5b` |
    | Spawn group | `wight_lesser5b` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser5b",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight_lesser5b",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
