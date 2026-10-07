---
description: "Angry skeleton is an enemy in Andor's Trail (undead) with 80 HP, worth 107–140 XP, found in Skeleton dance. Drops: Gold coins, Bone."
---

# ![](../assets/icons/monsters/monsters_tometik8_35.png){ .sprite } Angry skeleton

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Skeleton dance |
| **Class** | Undead |
| **HP** | 80 |
| **XP when defeated** | 107–140 |
| **Entries in game data** | 7 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! info "7 entries in the game data"
    The game's data files define 7 separate characters named Angry skeleton. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: combat statistics, loot or shop stock, appearance, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ratdom_skel_dance21`](#v-ratdom_skel_dance21) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance22`](#v-ratdom_skel_dance22) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance23`](#v-ratdom_skel_dance23) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance24`](#v-ratdom_skel_dance24) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance25`](#v-ratdom_skel_dance25) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance26`](#v-ratdom_skel_dance26) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |
| [`ratdom_skel_dance27`](#v-ratdom_skel_dance27) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 80 |

## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance21) { #v-ratdom_skel_dance21 }

**Entry ID:** `ratdom_skel_dance21` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 107 |
| Damage | 10 to 20 |
| Attack chance | 80 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 2 to 3 |
| [Bone](../items/bone.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |
| [v0.8.12.1](../versions/0.8.12.1.md) | droplistID added (ratdom_skeleton_bone) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance21)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance21` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | `ratdom_skeleton_bone` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:35` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance21",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:35",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "droplistID": "ratdom_skeleton_bone",
     "attackCost": 5,
     "attackChance": 80
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance22) { #v-ratdom_skel_dance22 }

**Entry ID:** `ratdom_skel_dance22` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 107 |
| Damage | 10 to 20 |
| Attack chance | 80 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 2 to 3 |
| [Bone](../items/bone.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |
| [v0.8.12.1](../versions/0.8.12.1.md) | droplistID added (ratdom_skeleton_bone) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance22)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance22` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | `ratdom_skeleton_bone` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:36` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance22",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:36",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "droplistID": "ratdom_skeleton_bone",
     "attackCost": 5,
     "attackChance": 80
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance23) { #v-ratdom_skel_dance23 }

**Entry ID:** `ratdom_skel_dance23` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 107 |
| Damage | 10 to 20 |
| Attack chance | 80 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 2 to 3 |
| [Bone](../items/bone.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |
| [v0.8.12.1](../versions/0.8.12.1.md) | droplistID added (ratdom_skeleton_bone) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance23)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance23` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | `ratdom_skeleton_bone` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:37` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance23",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:37",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "droplistID": "ratdom_skeleton_bone",
     "attackCost": 5,
     "attackChance": 80
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance24) { #v-ratdom_skel_dance24 }

**Entry ID:** `ratdom_skel_dance24` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 107 |
| Damage | 10 to 20 |
| Attack chance | 80 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance24)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance24` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:38` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance24",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:38",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "attackCost": 5,
     "attackChance": 80
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance25) { #v-ratdom_skel_dance25 }

**Entry ID:** `ratdom_skel_dance25` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 107 |
| Damage | 10 to 20 |
| Attack chance | 80 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance25)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance25` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik8:39` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance25",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:39",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "attackCost": 5,
     "attackChance": 80
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance26) { #v-ratdom_skel_dance26 }

**Entry ID:** `ratdom_skel_dance26` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 140 |
| Damage | 10 to 30 |
| Attack chance | 100 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance26)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance26` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:40` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance26",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:40",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "attackCost": 5,
     "attackChance": 100
    }
    ```


## Skeleton dance, Ratdom maze 543d (ratdom_skel_dance27) { #v-ratdom_skel_dance27 }

**Entry ID:** `ratdom_skel_dance27` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 80 |
| XP when defeated | 140 |
| Damage | 10 to 30 |
| Attack chance | 100 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 25 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_dance27)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_dance27` |
    | Spawn group | `ratdom_skel_dance2_grp` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:57` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_dance27",
     "name": "Angry skeleton",
     "iconID": "monsters_tometik8:57",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_skel_dance2_grp",
     "attackCost": 5,
     "attackChance": 100
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_dance21.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_dance21.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_dance21.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_dance21.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
