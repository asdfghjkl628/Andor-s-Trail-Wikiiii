---
description: "Sheep is an NPC who can also be fought in Andor's Trail, found in Crossroads Guardhouse, waterwayb4, Guynmart Castle, ll2_cyclops_cave, mountainlake27, mountainlake28, fields3."
---

# ![](../assets/icons/monsters/monsters_karvis2_8.png){ .sprite } Sheep

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Crossroads Guardhouse, waterwayb4, Guynmart Castle, ll2_cyclops_cave, mountainlake27, mountainlake28, fields3 |
| **Class** | Animal |
| **HP** | 5 |
| **XP when defeated** | 4 |
| **Entries in game data** | 9 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "9 entries in the game data"
    The game's data files define 9 separate characters named Sheep. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`sheep1`](#v-sheep1) | NPC/Enemy | Crossroads Guardhouse: [fields6](../maps/fields6.md#pin-npc-sheep1) | – | 5 |
| [`cithurnsheep`](#v-cithurnsheep) | NPC | [waterwayb4](../maps/waterwayb4.md#pin-npc-cithurnsheep) | – | – |
| [`guynmart_sheep`](#v-guynmart_sheep) | NPC/Enemy | Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_sheep) | – | 5 |
| [`ll2_cyclops_sheep1`](#v-ll2_cyclops_sheep1) | NPC | [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md#pin-npc-ll2_cyclops_sheep1), [mountainlake27](../maps/mountainlake27.md#pin-npc-ll2_cyclops_sheep1) (+1 more) | – | – |
| [`ll2_cyclops_sheep2`](#v-ll2_cyclops_sheep2) | NPC | [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md#pin-npc-ll2_cyclops_sheep2), [mountainlake27](../maps/mountainlake27.md#pin-npc-ll2_cyclops_sheep2) (+1 more) | – | – |
| [`lostsheep1`](#v-lostsheep1) | NPC/Enemy | Crossroads Guardhouse: [fields1](../maps/fields1.md#pin-npc-lostsheep1) | – | 5 |
| [`lostsheep2`](#v-lostsheep2) | NPC/Enemy | Crossroads Guardhouse: [fields2](../maps/fields2.md#pin-npc-lostsheep2) | – | 5 |
| [`lostsheep3`](#v-lostsheep3) | NPC/Enemy | [fields3](../maps/fields3.md#pin-npc-lostsheep3) | – | 5 |
| [`lostsheep4`](#v-lostsheep4) | NPC/Enemy | Crossroads Guardhouse: [loneford1](../maps/loneford1.md#pin-npc-lostsheep4) | – | 5 |

## Crossroads Guardhouse, Fields6 (sheep1) { #v-sheep1 }

**Entry ID:** `sheep1` · **Type:** NPC/Enemy

**Location:** Crossroads Guardhouse: [fields6](../maps/fields6.md#pin-npc-sheep1)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields6](../maps/fields6.md) | Crossroads Guardhouse | 4 | – |

### Quests

- [Cheap cuts](../quests/benbyr.md): stage 21
- [Lost sheep](../quests/tinlyn.md): stage 60

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_sheep.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sheep1-tinlyn_sheep"></span>**`tinlyn_sheep`** Sheep: “Baah!”

    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk)

    <span id="d-sheep1-tinlyn_lostsheep_atk"></span>**`tinlyn_lostsheep_atk`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Lost sheep](../quests/tinlyn.md#stage-10))* → [tinlyn_lostsheep_atk1](#d-sheep1-tinlyn_lostsheep_atk1)
    - branch 2 → [tinlyn_sheep_atk](#d-sheep1-tinlyn_sheep_atk)

    <span id="d-sheep1-tinlyn_lostsheep_atk1"></span>**`tinlyn_lostsheep_atk1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 60 of [Lost sheep](../quests/tinlyn.md#stage-60)

    - branch 1 → [tinlyn_sheep_atk](#d-sheep1-tinlyn_sheep_atk)

    <span id="d-sheep1-tinlyn_sheep_atk"></span>**`tinlyn_sheep_atk`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21)

    - branch 1 → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (sheep1)"

    | | |
    |---|---|
    | Entry ID | `sheep1` |
    | Spawn group | `tinlyn_sheep` |
    | Loot table | `tinlyn_sheep` |
    | Conversation | `tinlyn_sheep` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "sheep1",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "tinlyn_sheep",
     "phraseID": "tinlyn_sheep",
     "droplistID": "tinlyn_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Waterwayb4 (cithurnsheep) { #v-cithurnsheep }

**Entry ID:** `cithurnsheep` · **Type:** NPC

**Location:** [waterwayb4](../maps/waterwayb4.md#pin-npc-cithurnsheep)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/cithurnsheep.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-cithurnsheep-cithurnsheep"></span>**`cithurnsheep`** Sheep: “Baah!”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (cithurnsheep)"

    | | |
    |---|---|
    | Entry ID | `cithurnsheep` |
    | Spawn group | `cithurnsheep` |
    | Loot table | – |
    | Conversation | `cithurnsheep` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "cithurnsheep",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "unique": 1,
     "monsterClass": "animal",
     "spawnGroup": "cithurnsheep",
     "phraseID": "cithurnsheep"
    }
    ```


## Guynmart Castle, Guynmart wood 9 (guynmart_sheep) { #v-guynmart_sheep }

**Entry ID:** `guynmart_sheep` · **Type:** NPC/Enemy

**Location:** Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_sheep)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_wood_9](../maps/guynmart_wood_9.md) | Guynmart Castle | 25 | – |

### Quests that count defeats

- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that this enemy has been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 25 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 20 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 15 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 10 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 9 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 8 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 7 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 6 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 5 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 4 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 3 of these enemies have been defeated.
- A conversation with [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that at least 2 of these enemies have been defeated.
- [Roses](../quests/guynmart.md#stage-170) with stepping on a trigger on [guynmart_farmhouse](../maps/guynmart_farmhouse.md) checks that this enemy has been defeated.
- A conversation with [Shepherd](../monsters/guynmart_shephard.md) ([guynmart_wood_9](../maps/guynmart_wood_9.md)), [Shepherd](../monsters/guynmart_shephard.md#v-guynmart_shephard2) ([guynmart_main_1](../maps/guynmart_main_1.md)) checks that this enemy has been defeated.
- A conversation with [Shepherd](../monsters/guynmart_shephard.md) ([guynmart_wood_9](../maps/guynmart_wood_9.md)), [Shepherd](../monsters/guynmart_shephard.md#v-guynmart_shephard2) ([guynmart_main_1](../maps/guynmart_main_1.md)) checks that at least 20 of these enemies have been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_sheep_10.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_sheep-guynmart_sheep_10"></span>**`guynmart_sheep_10`** Sheep: “Baah!”

    - “Baah!” → *conversation ends*
    - “You look tasty...” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_sheep)"

    | | |
    |---|---|
    | Entry ID | `guynmart_sheep` |
    | Spawn group | `guynmart_sheep` |
    | Loot table | `guynmart_sheep` |
    | Conversation | `guynmart_sheep_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_sheep",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 0,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "phraseID": "guynmart_sheep_10",
     "droplistID": "guynmart_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Ll2 cyclops cave and 2 more (ll2_cyclops_sheep1) { #v-ll2_cyclops_sheep1 }

**Entry ID:** `ll2_cyclops_sheep1` · **Type:** NPC

**Location:** [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md#pin-npc-ll2_cyclops_sheep1), [mountainlake27](../maps/mountainlake27.md#pin-npc-ll2_cyclops_sheep1), [mountainlake28](../maps/mountainlake28.md#pin-npc-ll2_cyclops_sheep1)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | 5 | Appears later, during a quest |
| [mountainlake27](../maps/mountainlake27.md) | – | 5 | – |
| [mountainlake28](../maps/mountainlake28.md) | – | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_cyclops_sheep.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_cyclops_sheep1-ll2_cyclops_sheep"></span>**`ll2_cyclops_sheep`** Sheep: “Baaah.”




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_cyclops_sheep1)"

    | | |
    |---|---|
    | Entry ID | `ll2_cyclops_sheep1` |
    | Spawn group | `ll2_cyclops_sheep1` |
    | Loot table | – |
    | Conversation | `ll2_cyclops_sheep` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_cyclops_sheep1",
     "name": "Sheep",
     "iconID": "monsters_rltiles2:55",
     "monsterClass": "animal",
     "spawnGroup": "ll2_cyclops_sheep1",
     "horizontalFlipChance": 100,
     "phraseID": "ll2_cyclops_sheep"
    }
    ```


## Ll2 cyclops cave and 2 more (ll2_cyclops_sheep2) { #v-ll2_cyclops_sheep2 }

**Entry ID:** `ll2_cyclops_sheep2` · **Type:** NPC

**Location:** [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md#pin-npc-ll2_cyclops_sheep2), [mountainlake27](../maps/mountainlake27.md#pin-npc-ll2_cyclops_sheep2), [mountainlake28](../maps/mountainlake28.md#pin-npc-ll2_cyclops_sheep2)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | 1 | Appears later, during a quest |
| [mountainlake27](../maps/mountainlake27.md) | – | 1 | Appears later, during a quest |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |

### Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stage 58

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_cyclops_sheep2.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_cyclops_sheep2-ll2_cyclops_sheep2"></span>**`ll2_cyclops_sheep2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 57 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-57))* → [ll2_cyclops_sheep2_10](#d-ll2_cyclops_sheep2-ll2_cyclops_sheep2_10)
    - branch 2 → [ll2_cyclops_sheep](#d-ll2_cyclops_sheep1-ll2_cyclops_sheep) (listed above)

    <span id="d-ll2_cyclops_sheep2-ll2_cyclops_sheep2_10"></span>**`ll2_cyclops_sheep2_10`** Sheep: “Baaah.”

    - “You look strong enough to carry me. I hang down beneath you, and you pull me outwards.” → [ll2_cyclops_sheep2_20](#d-ll2_cyclops_sheep2-ll2_cyclops_sheep2_20)

    <span id="d-ll2_cyclops_sheep2-ll2_cyclops_sheep2_20"></span>**`ll2_cyclops_sheep2_20`** Sheep: “The sheep carries you willingly.” — **effects:** sets stage 58 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-58), removes monsters from ll2_cyclops_cave




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_cyclops_sheep2)"

    | | |
    |---|---|
    | Entry ID | `ll2_cyclops_sheep2` |
    | Spawn group | `ll2_cyclops_sheep2` |
    | Loot table | – |
    | Conversation | `ll2_cyclops_sheep2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_cyclops_sheep2",
     "name": "Sheep",
     "iconID": "monsters_rltiles2:55",
     "monsterClass": "animal",
     "spawnGroup": "ll2_cyclops_sheep2",
     "horizontalFlipChance": 100,
     "phraseID": "ll2_cyclops_sheep2"
    }
    ```


## Crossroads Guardhouse, Fields1 (lostsheep1) { #v-lostsheep1 }

**Entry ID:** `lostsheep1` · **Type:** NPC/Enemy

**Location:** Crossroads Guardhouse: [fields1](../maps/fields1.md#pin-npc-lostsheep1)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields1](../maps/fields1.md) | Crossroads Guardhouse | 1 | – |

### Quests

- [Cheap cuts](../quests/benbyr.md): stage 21
- [Lost sheep](../quests/tinlyn.md): stages 20, 25, 60

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_lostsheep1.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lostsheep1-tinlyn_lostsheep1"></span>**`tinlyn_lostsheep1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Lost sheep](../quests/tinlyn.md#stage-20))* → [tinlyn_lostsheep_y](#d-lostsheep1-tinlyn_lostsheep_y)
    - branch 2 → [tinlyn_lostsheep1_n](#d-lostsheep1-tinlyn_lostsheep1_n)

    <span id="d-lostsheep1-tinlyn_lostsheep_y"></span>**`tinlyn_lostsheep_y`** Sheep: “Baah!”

    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk) (listed above)

    <span id="d-lostsheep1-tinlyn_lostsheep1_n"></span>**`tinlyn_lostsheep1_n`** Sheep: “Baah!”

    - “[Place Tinlyn's bell around the neck of the sheep]” *(if hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md))* → [tinlyn_lostsheep1_place](#d-lostsheep1-tinlyn_lostsheep1_place)
    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk) (listed above)

    <span id="d-lostsheep1-tinlyn_lostsheep1_place"></span>**`tinlyn_lostsheep1_place`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 20 of [Lost sheep](../quests/tinlyn.md#stage-20)

    - branch 1 → [tinlyn_lostsheep_check_1](#d-lostsheep1-tinlyn_lostsheep_check_1)

    <span id="d-lostsheep1-tinlyn_lostsheep_check_1"></span>**`tinlyn_lostsheep_check_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Lost sheep](../quests/tinlyn.md#stage-20))* → [tinlyn_lostsheep_check_2](#d-lostsheep1-tinlyn_lostsheep_check_2)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-lostsheep1-tinlyn_lostsheep_placed_2)

    <span id="d-lostsheep1-tinlyn_lostsheep_check_2"></span>**`tinlyn_lostsheep_check_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Lost sheep](../quests/tinlyn.md#stage-21))* → [tinlyn_lostsheep_check_3](#d-lostsheep1-tinlyn_lostsheep_check_3)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-lostsheep1-tinlyn_lostsheep_placed_2)

    <span id="d-lostsheep1-tinlyn_lostsheep_placed_2"></span>**`tinlyn_lostsheep_placed_2`** Sheep: “[You place one of the bells around the neck of the sheep]”


    <span id="d-lostsheep1-tinlyn_lostsheep_check_3"></span>**`tinlyn_lostsheep_check_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22))* → [tinlyn_lostsheep_check_4](#d-lostsheep1-tinlyn_lostsheep_check_4)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-lostsheep1-tinlyn_lostsheep_placed_2)

    <span id="d-lostsheep1-tinlyn_lostsheep_check_4"></span>**`tinlyn_lostsheep_check_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Lost sheep](../quests/tinlyn.md#stage-23))* → [tinlyn_lostsheep_placed_1](#d-lostsheep1-tinlyn_lostsheep_placed_1)
    - branch 2 → [tinlyn_lostsheep_placed_2](#d-lostsheep1-tinlyn_lostsheep_placed_2)

    <span id="d-lostsheep1-tinlyn_lostsheep_placed_1"></span>**`tinlyn_lostsheep_placed_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 25 of [Lost sheep](../quests/tinlyn.md#stage-25)

    - branch 1 → [tinlyn_lostsheep_placed_2](#d-lostsheep1-tinlyn_lostsheep_placed_2)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “(You place one of the bells around the neck of the sheep.)” → “[You place one of the bells around the neck of the sheep]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lostsheep1)"

    | | |
    |---|---|
    | Entry ID | `lostsheep1` |
    | Spawn group | `tinlyn_lostsheep1` |
    | Loot table | `tinlyn_sheep` |
    | Conversation | `tinlyn_lostsheep1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "lostsheep1",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "tinlyn_lostsheep1",
     "phraseID": "tinlyn_lostsheep1",
     "droplistID": "tinlyn_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Crossroads Guardhouse, Fields2 (lostsheep2) { #v-lostsheep2 }

**Entry ID:** `lostsheep2` · **Type:** NPC/Enemy

**Location:** Crossroads Guardhouse: [fields2](../maps/fields2.md#pin-npc-lostsheep2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields2](../maps/fields2.md) | Crossroads Guardhouse | 1 | – |

### Quests

- [Cheap cuts](../quests/benbyr.md): stage 21
- [Lost sheep](../quests/tinlyn.md): stages 21, 25, 60

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_lostsheep2.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lostsheep2-tinlyn_lostsheep2"></span>**`tinlyn_lostsheep2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Lost sheep](../quests/tinlyn.md#stage-21))* → [tinlyn_lostsheep_y](#d-lostsheep1-tinlyn_lostsheep_y) (listed above)
    - branch 2 → [tinlyn_lostsheep2_n](#d-lostsheep2-tinlyn_lostsheep2_n)

    <span id="d-lostsheep2-tinlyn_lostsheep2_n"></span>**`tinlyn_lostsheep2_n`** Sheep: “Baah!”

    - “[Place Tinlyn's bell around the neck of the sheep]” *(if hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md))* → [tinlyn_lostsheep2_place](#d-lostsheep2-tinlyn_lostsheep2_place)
    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk) (listed above)

    <span id="d-lostsheep2-tinlyn_lostsheep2_place"></span>**`tinlyn_lostsheep2_place`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Lost sheep](../quests/tinlyn.md#stage-21)

    - branch 1 → [tinlyn_lostsheep_check_1](#d-lostsheep1-tinlyn_lostsheep_check_1) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “(You place one of the bells around the neck of the sheep.)” → “[You place one of the bells around the neck of the sheep]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lostsheep2)"

    | | |
    |---|---|
    | Entry ID | `lostsheep2` |
    | Spawn group | `tinlyn_lostsheep2` |
    | Loot table | `tinlyn_sheep` |
    | Conversation | `tinlyn_lostsheep2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "lostsheep2",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "tinlyn_lostsheep2",
     "phraseID": "tinlyn_lostsheep2",
     "droplistID": "tinlyn_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Fields3 (lostsheep3) { #v-lostsheep3 }

**Entry ID:** `lostsheep3` · **Type:** NPC/Enemy

**Location:** [fields3](../maps/fields3.md#pin-npc-lostsheep3)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fields3](../maps/fields3.md) | – | 1 | – |

### Quests

- [Cheap cuts](../quests/benbyr.md): stage 21
- [Lost sheep](../quests/tinlyn.md): stages 22, 25, 60

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_lostsheep3.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lostsheep3-tinlyn_lostsheep3"></span>**`tinlyn_lostsheep3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22))* → [tinlyn_lostsheep_y](#d-lostsheep1-tinlyn_lostsheep_y) (listed above)
    - branch 2 → [tinlyn_lostsheep3_n](#d-lostsheep3-tinlyn_lostsheep3_n)

    <span id="d-lostsheep3-tinlyn_lostsheep3_n"></span>**`tinlyn_lostsheep3_n`** Sheep: “Baah!”

    - “[Place Tinlyn's bell around the neck of the sheep]” *(if hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md))* → [tinlyn_lostsheep3_place](#d-lostsheep3-tinlyn_lostsheep3_place)
    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk) (listed above)

    <span id="d-lostsheep3-tinlyn_lostsheep3_place"></span>**`tinlyn_lostsheep3_place`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22)

    - branch 1 → [tinlyn_lostsheep_check_1](#d-lostsheep1-tinlyn_lostsheep_check_1) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “(You place one of the bells around the neck of the sheep.)” → “[You place one of the bells around the neck of the sheep]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lostsheep3)"

    | | |
    |---|---|
    | Entry ID | `lostsheep3` |
    | Spawn group | `tinlyn_lostsheep3` |
    | Loot table | `tinlyn_sheep` |
    | Conversation | `tinlyn_lostsheep3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "lostsheep3",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "tinlyn_lostsheep3",
     "phraseID": "tinlyn_lostsheep3",
     "droplistID": "tinlyn_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


## Crossroads Guardhouse, Loneford1 (lostsheep4) { #v-lostsheep4 }

**Entry ID:** `lostsheep4` · **Type:** NPC/Enemy

**Location:** Crossroads Guardhouse: [loneford1](../maps/loneford1.md#pin-npc-lostsheep4)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 5 |
| XP when defeated | 4 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 70% | 0 to 3 |
| [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [loneford1](../maps/loneford1.md) | Crossroads Guardhouse | 1 | – |

### Quests

- [Cheap cuts](../quests/benbyr.md): stage 21
- [Lost sheep](../quests/tinlyn.md): stages 23, 25, 60

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Sheep. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/tinlyn_lostsheep4.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lostsheep4-tinlyn_lostsheep4"></span>**`tinlyn_lostsheep4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Lost sheep](../quests/tinlyn.md#stage-23))* → [tinlyn_lostsheep_y](#d-lostsheep1-tinlyn_lostsheep_y) (listed above)
    - branch 2 → [tinlyn_lostsheep4_n](#d-lostsheep4-tinlyn_lostsheep4_n)

    <span id="d-lostsheep4-tinlyn_lostsheep4_n"></span>**`tinlyn_lostsheep4_n`** Sheep: “Baah!”

    - “[Place Tinlyn's bell around the neck of the sheep]” *(if hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md))* → [tinlyn_lostsheep4_place](#d-lostsheep4-tinlyn_lostsheep4_place)
    - “[Attack]” *(if reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20))* → [tinlyn_lostsheep_atk](#d-sheep1-tinlyn_lostsheep_atk) (listed above)

    <span id="d-lostsheep4-tinlyn_lostsheep4_place"></span>**`tinlyn_lostsheep4_place`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 23 of [Lost sheep](../quests/tinlyn.md#stage-23)

    - branch 1 → [tinlyn_lostsheep_check_1](#d-lostsheep1-tinlyn_lostsheep_check_1) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “(You place one of the bells around the neck of the sheep.)” → “[You place one of the bells around the neck of the sheep]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lostsheep4)"

    | | |
    |---|---|
    | Entry ID | `lostsheep4` |
    | Spawn group | `tinlyn_lostsheep4` |
    | Loot table | `tinlyn_sheep` |
    | Conversation | `tinlyn_lostsheep4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "lostsheep4",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "spawnGroup": "tinlyn_lostsheep4",
     "phraseID": "tinlyn_lostsheep4",
     "droplistID": "tinlyn_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
