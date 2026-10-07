---
description: "Skeleton is an NPC who can also be fought in Andor's Trail, found in Flagstone Prison, Guynmart Castle, Bloskelt + Roskelt."
---

# ![](../assets/icons/monsters/monsters_skeleton1_0.png){ .sprite } Skeleton

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_skeleton1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Flagstone Prison, Guynmart Castle, Bloskelt + Roskelt |
| **Class** | Construct |
| **HP** | 35–100 |
| **XP when defeated** | 38–190 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 6 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "6 entries in the game data"
    The game's data files define 6 separate characters named Skeleton. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, faction, appearance, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`skeleton`](#v-skeleton) | Enemy | Flagstone Prison: [flagstone2](../maps/flagstone2.md), [hauntedhouse3](../maps/hauntedhouse3.md) (+1 more) | – | 35 |
| [`guynmart_skeleton`](#v-guynmart_skeleton) | Enemy | Guynmart Castle: [guynmart_passage](../maps/guynmart_passage.md) | – | 60 |
| [`guynmart_skeleton2`](#v-guynmart_skeleton2) | NPC/Enemy | Guynmart Castle: [guynmart_passage](../maps/guynmart_passage.md#pin-npc-guynmart_skeleton2) | – | 60 |
| [`ratdom_skeleton1`](#v-ratdom_skeleton1) | NPC/Enemy | Bloskelt + Roskelt: [ratdom_maze_415](../maps/ratdom_maze_415.md#pin-npc-ratdom_skeleton1), Bloskelt + Roskelt: [ratdom_maze_425](../maps/ratdom_maze_425.md#pin-npc-ratdom_skeleton1) | – | 60 |
| [`ratdom_skeleton2`](#v-ratdom_skeleton2) | NPC/Enemy | Bloskelt + Roskelt: [ratdom_maze_416](../maps/ratdom_maze_416.md#pin-npc-ratdom_skeleton2), Bloskelt + Roskelt: [ratdom_maze_426](../maps/ratdom_maze_426.md#pin-npc-ratdom_skeleton2) | – | 60 |
| [`stn_colonel_mons2`](#v-stn_colonel_mons2) | Enemy | Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md) | – | 100 |

## Flagstone Prison, Flagstone2 and 2 more (skeleton) { #v-skeleton }

**Entry ID:** `skeleton` · **Type:** Enemy

**Location:** Flagstone Prison: [flagstone2](../maps/flagstone2.md), [hauntedhouse3](../maps/hauntedhouse3.md), [hauntedhouse4](../maps/hauntedhouse4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 35 |
| XP when defeated | 38 |
| Damage | 1 to 4 |
| Attack chance | 60 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 16 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [flagstone2](../maps/flagstone2.md) | Flagstone Prison | 1 | – |
| [hauntedhouse3](../maps/hauntedhouse3.md) | – | 2 | – |
| [hauntedhouse4](../maps/hauntedhouse4.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (skeleton)"

    | | |
    |---|---|
    | Entry ID | `skeleton` |
    | Spawn group | `skeleton1` |
    | Loot table | `skeleton` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_skeleton1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_animals.json` |

    Raw data:

    ```json
    {
     "id": "skeleton",
     "name": "Skeleton",
     "iconID": "monsters_skeleton1:0",
     "maxHP": 35,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "skeleton1",
     "droplistID": "skeleton",
     "attackCost": 9,
     "attackChance": 60,
     "blockChance": 40
    }
    ```


## Guynmart Castle, Guynmart passage (guynmart_skeleton) { #v-guynmart_skeleton }

**Entry ID:** `guynmart_skeleton` · **Type:** Enemy

**Location:** Guynmart Castle: [guynmart_passage](../maps/guynmart_passage.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 60 |
| XP when defeated | 164 |
| Damage | 5 to 20 |
| Attack chance | 40 |
| Block chance | 150 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 50% | 1 |
| [Gold coins](../items/gold.md) | 33% | 2 to 9 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_passage](../maps/guynmart_passage.md) | Guynmart Castle | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_skeleton)"

    | | |
    |---|---|
    | Entry ID | `guynmart_skeleton` |
    | Spawn group | `guynmart_skeleton` |
    | Loot table | `guynmart_drp_skeleton` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:31` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_skeleton",
     "name": "Skeleton",
     "iconID": "monsters_tometik8:31",
     "maxHP": 60,
     "maxAP": 10,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "droplistID": "guynmart_drp_skeleton",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```


## Guynmart Castle, Guynmart passage (guynmart_skeleton2) { #v-guynmart_skeleton2 }

**Entry ID:** `guynmart_skeleton2` · **Type:** NPC/Enemy

**Location:** Guynmart Castle: [guynmart_passage](../maps/guynmart_passage.md#pin-npc-guynmart_skeleton2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 60 |
| XP when defeated | 164 |
| Damage | 5 to 20 |
| Attack chance | 40 |
| Block chance | 150 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 50% | 1 |
| [Gold coins](../items/gold.md) | 33% | 2 to 9 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_passage](../maps/guynmart_passage.md) | Guynmart Castle | 3 | Appears later, during a quest |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Skeleton. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_skeleton2_10.json" data-npc="Skeleton" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_skeleton2-guynmart_skeleton2_10"></span>**`guynmart_skeleton2_10`** Skeleton: “The ring. This human wears the ring of bone. Let him pass.”

    - “A bit scary - but really useful, this ring.” → *conversation ends*
    - “You are in my way. Attack!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_skeleton2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_skeleton2` |
    | Spawn group | `guynmart_skeleton2` |
    | Loot table | `guynmart_drp_skeleton` |
    | Conversation | `guynmart_skeleton2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:31` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_skeleton2",
     "name": "Skeleton",
     "iconID": "monsters_tometik8:31",
     "maxHP": 60,
     "maxAP": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "phraseID": "guynmart_skeleton2_10",
     "droplistID": "guynmart_drp_skeleton",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```


## Bloskelt + Roskelt, Ratdom maze 415 and 1 more (ratdom_skeleton1) { #v-ratdom_skeleton1 }

**Entry ID:** `ratdom_skeleton1` · **Type:** NPC/Enemy

**Location:** Bloskelt + Roskelt: [ratdom_maze_415](../maps/ratdom_maze_415.md#pin-npc-ratdom_skeleton1), Bloskelt + Roskelt: [ratdom_maze_425](../maps/ratdom_maze_425.md#pin-npc-ratdom_skeleton1)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 60 |
| XP when defeated | 118 |
| Damage | 10 to 20 |
| Attack chance | 100 |
| Block chance | 0 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_415](../maps/ratdom_maze_415.md) | Bloskelt + Roskelt | 4 | – |
| [ratdom_maze_425](../maps/ratdom_maze_425.md) | Bloskelt + Roskelt | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Skeleton. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_skeleton1.json" data-npc="Skeleton" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_skeleton1-ratdom_skeleton1"></span>**`ratdom_skeleton1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Old man's ring of bone](../items/guynmart_bonering.md))* → [ratdom_skeleton_10](#d-ratdom_skeleton1-ratdom_skeleton_10)
    - branch 2 → [ratdom_skeleton1_20](#d-ratdom_skeleton1-ratdom_skeleton1_20)

    <span id="d-ratdom_skeleton1-ratdom_skeleton_10"></span>**`ratdom_skeleton_10`** Skeleton: “The ring. This human wears the ring of bone. Let him pass.”

    - “A bit scary - but really useful, this ring.” → *conversation ends*
    - “You are in my way. Attack!” → *fight starts*

    <span id="d-ratdom_skeleton1-ratdom_skeleton1_20"></span>**`ratdom_skeleton1_20`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_skeleton1” +10

    - branch 1 → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skeleton1)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skeleton1` |
    | Spawn group | `ratdom_skeleton1` |
    | Loot table | – |
    | Conversation | `ratdom_skeleton1` |
    | Faction | `ratdom_skeleton1` |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:35` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skeleton1",
     "name": "Skeleton",
     "iconID": "monsters_tometik8:35",
     "maxHP": 60,
     "maxAP": 10,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skeleton1",
     "faction": "ratdom_skeleton1",
     "phraseID": "ratdom_skeleton1",
     "attackCost": 5,
     "attackChance": 100,
     "damageResistance": 2
    }
    ```


## Bloskelt + Roskelt, Ratdom maze 416 and 1 more (ratdom_skeleton2) { #v-ratdom_skeleton2 }

**Entry ID:** `ratdom_skeleton2` · **Type:** NPC/Enemy

**Location:** Bloskelt + Roskelt: [ratdom_maze_416](../maps/ratdom_maze_416.md#pin-npc-ratdom_skeleton2), Bloskelt + Roskelt: [ratdom_maze_426](../maps/ratdom_maze_426.md#pin-npc-ratdom_skeleton2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 60 |
| XP when defeated | 118 |
| Damage | 10 to 20 |
| Attack chance | 100 |
| Block chance | 0 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_416](../maps/ratdom_maze_416.md) | Bloskelt + Roskelt | 4 | – |
| [ratdom_maze_426](../maps/ratdom_maze_426.md) | Bloskelt + Roskelt | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Skeleton. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_skeleton2.json" data-npc="Skeleton" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_skeleton2-ratdom_skeleton2"></span>**`ratdom_skeleton2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Old man's ring of bone](../items/guynmart_bonering.md))* → [ratdom_skeleton_10](#d-ratdom_skeleton1-ratdom_skeleton_10) (listed above)
    - branch 2 → [ratdom_skeleton2_20](#d-ratdom_skeleton2-ratdom_skeleton2_20)

    <span id="d-ratdom_skeleton2-ratdom_skeleton2_20"></span>**`ratdom_skeleton2_20`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_skeleton2” +10

    - branch 1 → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skeleton2)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skeleton2` |
    | Spawn group | `ratdom_skeleton2` |
    | Loot table | – |
    | Conversation | `ratdom_skeleton2` |
    | Faction | `ratdom_skeleton2` |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:35` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skeleton2",
     "name": "Skeleton",
     "iconID": "monsters_tometik8:35",
     "maxHP": 60,
     "maxAP": 10,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_skeleton2",
     "faction": "ratdom_skeleton2",
     "phraseID": "ratdom_skeleton2",
     "attackCost": 5,
     "attackChance": 100,
     "damageResistance": 2
    }
    ```


## Flagstone Prison, Waytogalmore0 (stn_colonel_mons2) { #v-stn_colonel_mons2 }

**Entry ID:** `stn_colonel_mons2` · **Type:** Enemy

**Location:** Flagstone Prison: [waytogalmore0](../maps/waytogalmore0.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 100 |
| XP when defeated | 190 |
| Damage | 1 to 4 |
| Attack chance | 40 |
| Block chance | 120 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytogalmore0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |

### Quests that count defeats

- [Colonel Lutarc](../quests/stn_colonel.md#stage-122) with stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_colonel_mons2)"

    | | |
    |---|---|
    | Entry ID | `stn_colonel_mons2` |
    | Spawn group | `stn_colonel_mons2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:177` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_colonel_mons2",
     "name": "Skeleton",
     "iconID": "monsters_rltiles2:177",
     "maxHP": 100,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 120,
     "damageResistance": 5
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeleton.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeleton.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeleton.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=skeleton.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
