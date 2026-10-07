---
description: "Terrified teenager is an NPC who can also be fought in Andor's Trail, found in undertell_3_12."
---

# ![](../assets/icons/monsters/monsters_gisons_14.png){ .sprite } Terrified teenager

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | undertell_3_12 |
| **Class** | Ghost |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Terrified teenager. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`about_a_girl1`](#v-about_a_girl1) | NPC | [undertell_3_12](../maps/undertell_3_12.md#pin-npc-about_a_girl1) | – | – |
| [`about_a_girl_flee`](#v-about_a_girl_flee) | Enemy | [undertell_3_12](../maps/undertell_3_12.md) | – | 1 |
| [`about_a_girl_hidden`](#v-about_a_girl_hidden) | Enemy | [undertell_3_12](../maps/undertell_3_12.md) | – | 1 |

## Undertell 3 12 (about_a_girl1) { #v-about_a_girl1 }

**Entry ID:** `about_a_girl1` · **Type:** NPC

**Location:** [undertell_3_12](../maps/undertell_3_12.md#pin-npc-about_a_girl1)

### Quests

- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stage 90

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Terrified teenager. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/about_girl_scream_10.json" data-npc="Terrified teenager" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-about_a_girl1-about_girl_scream_10"></span>**`about_girl_scream_10`** [Terrified teenager](../monsters/about_a_girl1.md#v-about_a_girl_hidden): “HELP! SOMEBODY HELP ME!”

    - “What is wrong?” → [about_girl_scream_20](#d-about_a_girl1-about_girl_scream_20)

    <span id="d-about_a_girl1-about_girl_scream_20"></span>**`about_girl_scream_20`** Terrified teenager: “STAY AWAY FROM ME!” — **effects:** removes monsters from undertell_3_12, spawns monsters on undertell_3_12, sets stage 90 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-90)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl1)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl1` |
    | Spawn group | `about_a_girl1` |
    | Loot table | – |
    | Conversation | `about_girl_scream_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl1",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 50,
     "phraseID": "about_girl_scream_10"
    }
    ```


## Undertell 3 12 (about_a_girl_flee) { #v-about_a_girl_flee }

**Entry ID:** `about_a_girl_flee` · **Type:** Enemy

**Location:** [undertell_3_12](../maps/undertell_3_12.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
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

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_12](../maps/undertell_3_12.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl_flee)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_flee` |
    | Spawn group | `about_a_girl_flee` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | flee |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_flee",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "movementAggressionType": "flee",
     "horizontalFlipChance": 50
    }
    ```


## Undertell 3 12 (about_a_girl_hidden) { #v-about_a_girl_hidden }

**Entry ID:** `about_a_girl_hidden` · **Type:** Enemy

**Location:** [undertell_3_12](../maps/undertell_3_12.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
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

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_3_12](../maps/undertell_3_12.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl_hidden)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_hidden` |
    | Spawn group | `about_a_girl_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_hidden",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 0
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
