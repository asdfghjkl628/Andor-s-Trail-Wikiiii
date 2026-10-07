---
description: "Dark watch is an NPC who can also be fought in Andor's Trail, found in Laerothprison 7, Laerothprison 4, Laerothprison 5."
---

# ![](../assets/icons/monsters/monsters_ld2_238.png){ .sprite } Dark watch

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_238.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Laerothprison 7, Laerothprison 4, Laerothprison 5 |
| **Class** | Demon |
| **HP** | 180 |
| **XP when defeated** | 313 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 10 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

!!! info "10 entries in the game data"
    The game data defines 10 separate characters named Dark watch. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, faction, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`lae_demon4`](#v-lae_demon4) | NPC/Enemy | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon4) | – | 180 |
| [`lae_demon4_safe`](#v-lae_demon4_safe) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_demon4_safe) | – | – |
| [`lae_demon4b`](#v-lae_demon4b) | NPC/Enemy | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon4b) | – | 180 |
| [`lae_demon4b_safe`](#v-lae_demon4b_safe) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_demon4b_safe) | – | – |
| [`lae_demon5`](#v-lae_demon5) | NPC/Enemy | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon5) | – | 180 |
| [`lae_demon5_safe`](#v-lae_demon5_safe) | NPC | [Laerothprison 5](../maps/laerothprison5.md#pin-npc-lae_demon5_safe) | – | – |
| [`lae_demon7`](#v-lae_demon7) | NPC/Enemy | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon7) | – | 180 |
| [`lae_demon7_safe`](#v-lae_demon7_safe) | NPC | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon7_safe) | – | – |
| [`lae_demon9`](#v-lae_demon9) | NPC/Enemy | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon9) | – | 180 |
| [`lae_demon9_safe`](#v-lae_demon9_safe) | NPC | [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon9_safe) | – | – |

## Laerothprison 7 (lae_demon4) { #v-lae_demon4 }

**Entry ID:** `lae_demon4` · **Type:** NPC/Enemy

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon4)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_demon`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| Attack chance | 90 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2

**When hit:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 7](../maps/laerothprison7.md) | – | 3 | Appears later, during a quest |

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stage 114

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon4.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_demon4-lae_demon4"></span>**`lae_demon4`** Dark watch: “Command us!” — **effects:** sets stage 114 of [Shadow of the torturer](../quests/lae_torturer.md#stage-114), removes monsters from laerothprison7, removes monsters from laerothprison7, spawns monsters on laerothprison4, spawns monsters on laerothprison4, changes map laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, clears stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31), clears stage 32 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-32), clears stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33), clears stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)

    - “You go and watch over the prisoners in the cells.” → [lae_demon4_10](#d-lae_demon4-lae_demon4_10)

    <span id="d-lae_demon4-lae_demon4_10"></span>**`lae_demon4_10`** Dark watch: “As you wish.”




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon4)"

    | | |
    |---|---|
    | Entry ID | `lae_demon4` |
    | Spawn group | `lae_demon4` |
    | Loot table | `lae_demon` |
    | Conversation | `lae_demon4` |
    | Faction | `lae_demon` |
    | Movement | wholeMap |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon4",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "maxHP": 180,
     "moveCost": 5,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "faction": "lae_demon",
     "phraseID": "lae_demon4",
     "droplistID": "lae_demon",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Laerothprison 4 (lae_demon4_safe) { #v-lae_demon4_safe }

**Entry ID:** `lae_demon4_safe` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_demon4_safe)

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_demon4_safe-lae_demon"></span>**`lae_demon`** Dark watch: “We are legion. Fear us.”




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon4_safe)"

    | | |
    |---|---|
    | Entry ID | `lae_demon4_safe` |
    | Spawn group | `lae_demon4_safe` |
    | Loot table | – |
    | Conversation | `lae_demon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon4_safe",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "moveCost": 5,
     "monsterClass": "demon",
     "phraseID": "lae_demon"
    }
    ```


## Laerothprison 7 (lae_demon4b) { #v-lae_demon4b }

**Entry ID:** `lae_demon4b` · **Type:** NPC/Enemy

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon4b)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_demon`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| Attack chance | 90 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2

**When hit:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 7](../maps/laerothprison7.md) | – | 2 | Appears later, during a quest |

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stage 114

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon4.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_demon4](#d-lae_demon4-lae_demon4).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon4b)"

    | | |
    |---|---|
    | Entry ID | `lae_demon4b` |
    | Spawn group | `lae_demon4b` |
    | Loot table | `lae_demon` |
    | Conversation | `lae_demon4` |
    | Faction | `lae_demon` |
    | Movement | wholeMap |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon4b",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "maxHP": 180,
     "moveCost": 5,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "faction": "lae_demon",
     "phraseID": "lae_demon4",
     "droplistID": "lae_demon",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Laerothprison 4 (lae_demon4b_safe) { #v-lae_demon4b_safe }

**Entry ID:** `lae_demon4b_safe` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_demon4b_safe)

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_demon](#d-lae_demon4_safe-lae_demon).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon4b_safe)"

    | | |
    |---|---|
    | Entry ID | `lae_demon4b_safe` |
    | Spawn group | `lae_demon4b_safe` |
    | Loot table | – |
    | Conversation | `lae_demon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon4b_safe",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "moveCost": 5,
     "monsterClass": "demon",
     "phraseID": "lae_demon"
    }
    ```


## Laerothprison 7 (lae_demon5) { #v-lae_demon5 }

**Entry ID:** `lae_demon5` · **Type:** NPC/Enemy

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon5)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_demon`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| Attack chance | 90 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2

**When hit:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 7](../maps/laerothprison7.md) | – | 2 | Appears later, during a quest |

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon5.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_demon5-lae_demon5"></span>**`lae_demon5`** Dark watch: “Command us!” — **effects:** removes monsters from laerothprison7, spawns monsters on laerothprison5, removes monsters from laerothprison5, removes monsters from laerothprison5, removes monsters from laerothprison5, removes monsters from laerothprison5, spawns monsters on laerothprison5

    - “You stand guard in the hall under the cell block.” → [lae_demon4_10](#d-lae_demon4-lae_demon4_10) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon5)"

    | | |
    |---|---|
    | Entry ID | `lae_demon5` |
    | Spawn group | `lae_demon5` |
    | Loot table | `lae_demon` |
    | Conversation | `lae_demon5` |
    | Faction | `lae_demon` |
    | Movement | wholeMap |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon5",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "maxHP": 180,
     "moveCost": 5,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "faction": "lae_demon",
     "phraseID": "lae_demon5",
     "droplistID": "lae_demon",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Laerothprison 5 (lae_demon5_safe) { #v-lae_demon5_safe }

**Entry ID:** `lae_demon5_safe` · **Type:** NPC

**Location:** [Laerothprison 5](../maps/laerothprison5.md#pin-npc-lae_demon5_safe)

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_demon](#d-lae_demon4_safe-lae_demon).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon5_safe)"

    | | |
    |---|---|
    | Entry ID | `lae_demon5_safe` |
    | Spawn group | `lae_demon5_safe` |
    | Loot table | – |
    | Conversation | `lae_demon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon5_safe",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "moveCost": 5,
     "monsterClass": "demon",
     "phraseID": "lae_demon"
    }
    ```


## Laerothprison 7 (lae_demon7) { #v-lae_demon7 }

**Entry ID:** `lae_demon7` · **Type:** NPC/Enemy

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon7)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_demon`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| Attack chance | 90 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2

**When hit:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 7](../maps/laerothprison7.md) | – | 2 | Appears later, during a quest |

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon7.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_demon7-lae_demon7"></span>**`lae_demon7`** Dark watch: “Command us!” — **effects:** removes monsters from laerothprison7, spawns monsters on laerothprison7

    - “You protect Kotheses in case the prisoners get here.” → [lae_demon4_10](#d-lae_demon4-lae_demon4_10) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon7)"

    | | |
    |---|---|
    | Entry ID | `lae_demon7` |
    | Spawn group | `lae_demon7` |
    | Loot table | `lae_demon` |
    | Conversation | `lae_demon7` |
    | Faction | `lae_demon` |
    | Movement | wholeMap |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon7",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "maxHP": 180,
     "moveCost": 5,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "faction": "lae_demon",
     "phraseID": "lae_demon7",
     "droplistID": "lae_demon",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Laerothprison 7 (lae_demon7_safe) { #v-lae_demon7_safe }

**Entry ID:** `lae_demon7_safe` · **Type:** NPC

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon7_safe)

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_demon](#d-lae_demon4_safe-lae_demon).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon7_safe)"

    | | |
    |---|---|
    | Entry ID | `lae_demon7_safe` |
    | Spawn group | `lae_demon7_safe` |
    | Loot table | – |
    | Conversation | `lae_demon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon7_safe",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "moveCost": 5,
     "monsterClass": "demon",
     "phraseID": "lae_demon"
    }
    ```


## Laerothprison 7 (lae_demon9) { #v-lae_demon9 }

**Entry ID:** `lae_demon9` · **Type:** NPC/Enemy

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon9)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_demon`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 180 |
| XP when defeated | 313 |
| Damage | 3 to 20 |
| Attack chance | 90 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 1.5 |
| Critical hit chance | 12% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2

**When hit:** Heal HP: 2; increaseAttackerCurrentHP: -2


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 100% | 1 |
| [Oegyth crystal](../items/oegyth.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 7](../maps/laerothprison7.md) | – | 1 | Appears later, during a quest |

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stage 110

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon9.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_demon9-lae_demon9"></span>**`lae_demon9`** Dark watch: “[hollow voice] Take back your glass ball, brave little human.” — **effects:** gives 1× [Oegyth crystal](../items/oegyth.md), sets stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110), removes monsters from laerothprison7, spawns monsters on laerothprison7

    - “Th ... thanks.” → [lae_demon](#d-lae_demon4_safe-lae_demon) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon9)"

    | | |
    |---|---|
    | Entry ID | `lae_demon9` |
    | Spawn group | `lae_demon9` |
    | Loot table | `lae_demon9` |
    | Conversation | `lae_demon9` |
    | Faction | `lae_demon` |
    | Movement | wholeMap |
    | Icon | `monsters_ld2:239` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon9",
     "name": "Dark watch",
     "iconID": "monsters_ld2:239",
     "maxHP": 180,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 3,
      "max": 20
     },
     "faction": "lae_demon",
     "phraseID": "lae_demon9",
     "droplistID": "lae_demon9",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      },
      "increaseAttackerCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


## Laerothprison 7 (lae_demon9_safe) { #v-lae_demon9_safe }

**Entry ID:** `lae_demon9_safe` · **Type:** NPC

**Location:** [Laerothprison 7](../maps/laerothprison7.md#pin-npc-lae_demon9_safe)

### Dialogue simulator

Set your quest stages and items, then talk to Dark watch. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_demon.json" data-npc="Dark watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_demon](#d-lae_demon4_safe-lae_demon).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_demon9_safe)"

    | | |
    |---|---|
    | Entry ID | `lae_demon9_safe` |
    | Spawn group | `lae_demon9_safe` |
    | Loot table | – |
    | Conversation | `lae_demon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:238` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_demon9_safe",
     "name": "Dark watch",
     "iconID": "monsters_ld2:238",
     "moveCost": 5,
     "monsterClass": "demon",
     "phraseID": "lae_demon"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_demon4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_demon4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_demon4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_demon4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
