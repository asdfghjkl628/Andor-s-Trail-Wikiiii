---
description: "Horn player is an NPC who can also be fought in Andor's Trail, found in Skeleton dance, Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_fatboy73_43.png){ .sprite } Horn player

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_fatboy73_43.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Skeleton dance, Flagstone Prison |
| **Class** | Undead |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! info "4 entries in the game data"
    The game's data files define 4 separate characters named Horn player. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ratdom_skel_horn`](#v-ratdom_skel_horn) | Enemy | Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | 1 |
| [`erwyn_skel_hornet`](#v-erwyn_skel_hornet) | NPC | Flagstone Prison: [stoutford_castle_shed](../maps/stoutford_castle_shed.md#pin-npc-erwyn_skel_hornet) | – | – |
| [`ratdom_skel_horn1`](#v-ratdom_skel_horn1) | Enemy | Not on a map | – | 1 |
| [`ratdom_skel_horn2`](#v-ratdom_skel_horn2) | Enemy | Not on a map | – | 1 |

## Skeleton dance, Ratdom maze 543d (ratdom_skel_horn) { #v-ratdom_skel_horn }

**Entry ID:** `ratdom_skel_horn` · **Type:** Enemy

**Location:** Skeleton dance: [ratdom_maze_543d](../maps/ratdom_maze_543d.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | Skeleton dance | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_horn)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_horn` |
    | Spawn group | `ratdom_skel_horn` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:43` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_horn",
     "name": "Horn player",
     "iconID": "monsters_fatboy73:43",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_horn"
    }
    ```


## Flagstone Prison, Stoutford castle shed (erwyn_skel_hornet) { #v-erwyn_skel_hornet }

**Entry ID:** `erwyn_skel_hornet` · **Type:** NPC

**Location:** Flagstone Prison: [stoutford_castle_shed](../maps/stoutford_castle_shed.md#pin-npc-erwyn_skel_hornet)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Horn player. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/erwyn_skel_band.json" data-npc="Horn player" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-erwyn_skel_hornet-erwyn_skel_band"></span>**`erwyn_skel_band`** Horn player: “Please don't disturb. We have to practice.”




### Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (erwyn_skel_hornet)"

    | | |
    |---|---|
    | Entry ID | `erwyn_skel_hornet` |
    | Spawn group | `erwyn_skel_hornet` |
    | Loot table | – |
    | Conversation | `erwyn_skel_band` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:43` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_skel_hornet",
     "name": "Horn player",
     "iconID": "monsters_fatboy73:43",
     "monsterClass": "undead",
     "spawnGroup": "erwyn_skel_hornet",
     "phraseID": "erwyn_skel_band"
    }
    ```


## Not placed on a map (ratdom_skel_horn1) { #v-ratdom_skel_horn1 }

**Entry ID:** `ratdom_skel_horn1` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_horn1)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_horn1` |
    | Spawn group | `ratdom_skel_horn1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:43` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_horn1",
     "name": "Horn player",
     "iconID": "monsters_fatboy73:43",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_horn1"
    }
    ```


## Not placed on a map (ratdom_skel_horn2) { #v-ratdom_skel_horn2 }

**Entry ID:** `ratdom_skel_horn2` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_skel_horn2)"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_horn2` |
    | Spawn group | `ratdom_skel_horn2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:42` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_horn2",
     "name": "Horn player",
     "iconID": "monsters_fatboy73:42",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_horn2"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_horn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_horn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_horn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_horn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
