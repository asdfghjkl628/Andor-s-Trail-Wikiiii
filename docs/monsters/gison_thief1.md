---
description: "Thief is an NPC who can also be fought in Andor's Trail, found in Mywildcave 4."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Thief

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Mywildcave 4 |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 114 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

!!! info "3 entries in the game data"
    The game data defines 3 separate characters named Thief. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, appearance. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`gison_thief1`](#v-gison_thief1) | NPC/Enemy | [Mywildcave 4](../maps/mywildcave4.md#pin-npc-gison_thief1) | – | 60 |
| [`gison_thief2`](#v-gison_thief2) | Enemy | [Mywildcave 4](../maps/mywildcave4.md) | – | 60 |
| [`gison_thief3`](#v-gison_thief3) | Enemy | Not on a map | – | 60 |

## Mywildcave 4 (gison_thief1) { #v-gison_thief1 }

**Entry ID:** `gison_thief1` · **Type:** NPC/Enemy

**Location:** [Mywildcave 4](../maps/mywildcave4.md#pin-npc-gison_thief1)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 114 |
| Damage | 3 to 8 |
| Attack chance | 105 |
| Block chance | 85 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 33% | 2 to 12 |
| [Ruby gem](../items/gem2.md) | 20% | 1 |
| [Polished gem](../items/gem3.md) | 20% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mywildcave 4](../maps/mywildcave4.md) | – | 1 | – |

### Quests

- [A raid for a cookbook](../quests/gison_cookbook.md): stage 40

### Dialogue simulator

Set your quest stages and items, then talk to Thief. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/gison_thief1.json" data-npc="Thief" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gison_thief1-gison_thief1"></span>**`gison_thief1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 62 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-62))* → [gison_thief1_20](#d-gison_thief1-gison_thief1_20)
    - branch 2 → [gison_thief1_10](#d-gison_thief1-gison_thief1_10)

    <span id="d-gison_thief1-gison_thief1_20"></span>**`gison_thief1_20`** Thief: “We agreed that there was nothing to see here. So get out of here.”

    - “Of course. Sorry, I forgot.” → *conversation ends*
    - “So what? I have changed my mind. Move aside if you love your life!” → [gison_thief1_22](#d-gison_thief1-gison_thief1_22)

    <span id="d-gison_thief1-gison_thief1_10"></span>**`gison_thief1_10`** Thief: “Let's pretend that you have not seen my master over there, practicing dark magic with the old spell in this book we have stolen. Go away!” — **effects:** sets stage 40 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-40)

    - “Hmm, maybe that is a good idea. I'll tell Gison that you have destroyed the book.” → [gison_thief1_12](#d-gison_thief1-gison_thief1_12)
    - “No way! Attack!” → *fight starts*

    <span id="d-gison_thief1-gison_thief1_22"></span>**`gison_thief1_22`** Thief: “Hahaha! You are funny. Hahahaha!”

    - “Attack!” → *fight starts*

    <span id="d-gison_thief1-gison_thief1_12"></span>**`gison_thief1_12`** Thief: “Do that. And now be gone!”




### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gison_thief1)"

    | | |
    |---|---|
    | Entry ID | `gison_thief1` |
    | Spawn group | `gison_thief1` |
    | Loot table | `gison_thief` |
    | Conversation | `gison_thief1` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gison_thief1",
     "name": "Thief",
     "iconID": "monsters_ld1:65",
     "maxHP": 60,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "gison_thief1",
     "phraseID": "gison_thief1",
     "droplistID": "gison_thief",
     "attackCost": 5,
     "attackChance": 105,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 85,
     "damageResistance": 1
    }
    ```


## Mywildcave 4 (gison_thief2) { #v-gison_thief2 }

**Entry ID:** `gison_thief2` · **Type:** Enemy

**Location:** [Mywildcave 4](../maps/mywildcave4.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 114 |
| Damage | 3 to 8 |
| Attack chance | 105 |
| Block chance | 85 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 33% | 2 to 12 |
| [Ruby gem](../items/gem2.md) | 20% | 1 |
| [Polished gem](../items/gem3.md) | 20% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mywildcave 4](../maps/mywildcave4.md) | – | 5 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gison_thief2)"

    | | |
    |---|---|
    | Entry ID | `gison_thief2` |
    | Spawn group | `gison_thief2` |
    | Loot table | `gison_thief` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:85` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gison_thief2",
     "name": "Thief",
     "iconID": "monsters_ld1:85",
     "maxHP": 60,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "gison_thief2",
     "droplistID": "gison_thief",
     "attackCost": 5,
     "attackChance": 105,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 85,
     "damageResistance": 1
    }
    ```


## Not placed on a map (gison_thief3) { #v-gison_thief3 }

**Entry ID:** `gison_thief3` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 114 |
| Damage | 3 to 8 |
| Attack chance | 105 |
| Block chance | 85 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 33% | 2 to 12 |
| [Ruby gem](../items/gem2.md) | 20% | 1 |
| [Polished gem](../items/gem3.md) | 20% | 1 |


### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gison_thief3)"

    | | |
    |---|---|
    | Entry ID | `gison_thief3` |
    | Spawn group | `gison_thief3` |
    | Loot table | `gison_thief` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gison_thief3",
     "name": "Thief",
     "iconID": "monsters_ld1:65",
     "maxHP": 60,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "gison_thief3",
     "droplistID": "gison_thief",
     "attackCost": 5,
     "attackChance": 105,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 85,
     "damageResistance": 1
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thief1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thief1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thief1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thief1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
