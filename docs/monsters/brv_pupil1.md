---
description: "Pupil is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_19.png){ .sprite } Pupil

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_19.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven |
| **Entries in game data** | 8 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "8 entries in the game data"
    The game data defines 8 separate characters named Pupil. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`brv_pupil1`](#v-brv_pupil1) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil1) | – |
| [`brv_pupil2`](#v-brv_pupil2) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil2) | – |
| [`brv_pupil3`](#v-brv_pupil3) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil3) | – |
| [`brv_pupil4`](#v-brv_pupil4) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil4) | – |
| [`brv_pupil5`](#v-brv_pupil5) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil5) | – |
| [`brv_pupil6`](#v-brv_pupil6) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil6) | – |
| [`brv_pupil7`](#v-brv_pupil7) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil7) | – |
| [`brv_pupil8`](#v-brv_pupil8) | NPC | Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil8) | – |

## Brimhaven, Brimhaven school (brv_pupil1) { #v-brv_pupil1 }

**Entry ID:** `brv_pupil1` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil1)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_pupil1-brv_school_pupil"></span>**`brv_school_pupil`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60))* → [brv_school_pupil_60_10](#d-brv_pupil1-brv_school_pupil_60_10)
    - branch 2 → [brv_school_pupil_10](#d-brv_pupil1-brv_school_pupil_10)

    <span id="d-brv_pupil1-brv_school_pupil_60_10"></span>**`brv_school_pupil_60_10`** [Dummy NPC](../monsters/none.md): “As you approach the little student, horror spreads on his face.”

    - “Don't panic. I'll go away again.” → *conversation ends*
    - “Wait, I'll show you...” → [brv_school_pupil_60_20](#d-brv_pupil1-brv_school_pupil_60_20)

    <span id="d-brv_pupil1-brv_school_pupil_10"></span>**`brv_school_pupil_10`** Pupil: “Hello, big one.”


    <span id="d-brv_pupil1-brv_school_pupil_60_20"></span>**`brv_school_pupil_60_20`** Pupil: “[He jumps up and runs screaming out of the room. The other little students follow in panic.]” — **effects:** sets stage 110 of [Lessons learned](../quests/brv_school2.md#stage-110), sets stage 50 of [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50), removes monsters from brimhaven_school




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil1)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil1` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:19` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil1",
     "name": "Pupil",
     "iconID": "monsters_ld1:19",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil2) { #v-brv_pupil2 }

**Entry ID:** `brv_pupil2` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil2)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil2)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil2` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:34` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil2",
     "name": "Pupil",
     "iconID": "monsters_ld1:34",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil3) { #v-brv_pupil3 }

**Entry ID:** `brv_pupil3` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil3)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil3)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil3` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil3",
     "name": "Pupil",
     "iconID": "monsters_ld1:62",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil4) { #v-brv_pupil4 }

**Entry ID:** `brv_pupil4` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil4)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil4)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil4` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:63` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil4",
     "name": "Pupil",
     "iconID": "monsters_ld1:63",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil5) { #v-brv_pupil5 }

**Entry ID:** `brv_pupil5` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil5)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil5)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil5` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:88` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil5",
     "name": "Pupil",
     "iconID": "monsters_ld1:88",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil6) { #v-brv_pupil6 }

**Entry ID:** `brv_pupil6` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil6)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil6)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil6` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:229` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil6",
     "name": "Pupil",
     "iconID": "monsters_ld1:229",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil7) { #v-brv_pupil7 }

**Entry ID:** `brv_pupil7` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil7)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil7)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil7` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:207` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil7",
     "name": "Pupil",
     "iconID": "monsters_ld1:207",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```


## Brimhaven, Brimhaven school (brv_pupil8) { #v-brv_pupil8 }

**Entry ID:** `brv_pupil8` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven school](../maps/brimhaven_school.md#pin-npc-brv_pupil8)

### Quests

- [Lessons learned](../quests/brv_school2.md): stage 110
- [Brimhaven story flags 2 (hidden flag)](../quests/brv_nondisplay2.md): stage 50

### Dialogue simulator

Set your quest stages and items, then talk to Pupil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_school_pupil.json" data-npc="Pupil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_school_pupil](#d-brv_pupil1-brv_school_pupil).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_pupil8)"

    | | |
    |---|---|
    | Entry ID | `brv_pupil8` |
    | Spawn group | `brv_school_pupil` |
    | Loot table | – |
    | Conversation | `brv_school_pupil` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:17` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_pupil8",
     "name": "Pupil",
     "iconID": "monsters_ld1:17",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_school_pupil",
     "phraseID": "brv_school_pupil"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_pupil1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
