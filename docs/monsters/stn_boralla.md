---
description: "Boralla is a non-player character (NPC) in Andor's Trail, found in Stoutford."
---

# ![](../assets/icons/monsters/monsters_tometik2_54.png){ .sprite } Boralla

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_54.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Stoutford |
| **Entries in game data** | 8 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "8 entries in the game data"
    The game data defines 8 separate characters named Boralla. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`stn_boralla`](#v-stn_boralla) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla) | – |
| [`stn_boralla1`](#v-stn_boralla1) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla1) | – |
| [`stn_boralla2`](#v-stn_boralla2) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla2) | – |
| [`stn_boralla3`](#v-stn_boralla3) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla3) | – |
| [`stn_boralla4`](#v-stn_boralla4) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla4) | – |
| [`stn_boralla5`](#v-stn_boralla5) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla5) | – |
| [`stn_boralla6`](#v-stn_boralla6) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla6) | – |
| [`stn_boralla7`](#v-stn_boralla7) | NPC | Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla7) | – |

## Stoutford, Stoutford north-east (stn_boralla) { #v-stn_boralla }

**Entry ID:** `stn_boralla` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla-stn_boralla"></span>**`stn_boralla`** Boralla: “Hi kid, should we play hide and seek?”

    - “Oh yes, I love hide and seek!” → [stn_boralla_10](#d-stn_boralla-stn_boralla_10)
    - “Leave me alone, I am too old for silly games.” → *conversation ends*

    <span id="d-stn_boralla-stn_boralla_10"></span>**`stn_boralla_10`** Boralla: “Great! Count to ten, then I will hide.”

    - “OK, I'll close my eyes now. 1, 2, 3...” → [stn_boralla_12](#d-stn_boralla-stn_boralla_12)

    <span id="d-stn_boralla-stn_boralla_12"></span>**`stn_boralla_12`** Boralla: “I am ready!” — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - “... 10 OK - coming!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla` |
    | Spawn group | `stn_boralla` |
    | Loot table | – |
    | Conversation | `stn_boralla` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 0,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla",
     "phraseID": "stn_boralla"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla1) { #v-stn_boralla1 }

**Entry ID:** `stn_boralla1` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla1)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla1.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla1-stn_boralla1"></span>**`stn_boralla1`** Boralla: “You found me too quickly! Once more, please. Count to ten again!”

    - “OK. 1, 2, 3...” → [stn_boralla1_12](#d-stn_boralla1-stn_boralla1_12)

    <span id="d-stn_boralla1-stn_boralla1_12"></span>**`stn_boralla1_12`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla1)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla1` |
    | Spawn group | `stn_boralla1` |
    | Loot table | – |
    | Conversation | `stn_boralla1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla1",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla1",
     "phraseID": "stn_boralla1"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla2) { #v-stn_boralla2 }

**Entry ID:** `stn_boralla2` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla2)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla2.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla2-stn_boralla2"></span>**`stn_boralla2`** Boralla: “Hey, you found me again! Once more?”

    - “Why not. 1, 2...” → [stn_boralla2_12](#d-stn_boralla2-stn_boralla2_12)

    <span id="d-stn_boralla2-stn_boralla2_12"></span>**`stn_boralla2_12`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla2)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla2` |
    | Spawn group | `stn_boralla2` |
    | Loot table | – |
    | Conversation | `stn_boralla2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla2",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla2",
     "phraseID": "stn_boralla2"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla3) { #v-stn_boralla3 }

**Entry ID:** `stn_boralla3` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla3)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla3.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla3-stn_boralla3"></span>**`stn_boralla3`** Boralla: “You didn't count to 10! Don't cheat. Another time!”

    - “OK. 1, 2, 3, 4...” → [stn_boralla3_12](#d-stn_boralla3-stn_boralla3_12)

    <span id="d-stn_boralla3-stn_boralla3_12"></span>**`stn_boralla3_12`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla3)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla3` |
    | Spawn group | `stn_boralla3` |
    | Loot table | – |
    | Conversation | `stn_boralla3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla3",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla3",
     "phraseID": "stn_boralla3"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla4) { #v-stn_boralla4 }

**Entry ID:** `stn_boralla4` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla4)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla4.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla4-stn_boralla4"></span>**`stn_boralla4`** Boralla: “Are you sure you didn't cheat this time?”

    - “Of course not. So go and hide again, quick! 1, 2, 3...” → [stn_boralla4_12](#d-stn_boralla4-stn_boralla4_12)

    <span id="d-stn_boralla4-stn_boralla4_12"></span>**`stn_boralla4_12`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla4)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla4` |
    | Spawn group | `stn_boralla4` |
    | Loot table | – |
    | Conversation | `stn_boralla4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla4",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla4",
     "phraseID": "stn_boralla4"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla5) { #v-stn_boralla5 }

**Entry ID:** `stn_boralla5` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla5)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla5.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla5-stn_boralla5"></span>**`stn_boralla5`** Boralla: “You found me again! Once...”

    - “...more, I know. 1, 2, 3, 4...” → [stn_boralla5_12](#d-stn_boralla5-stn_boralla5_12)

    <span id="d-stn_boralla5-stn_boralla5_12"></span>**`stn_boralla5_12`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla5)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla5` |
    | Spawn group | `stn_boralla5` |
    | Loot table | – |
    | Conversation | `stn_boralla5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla5",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla5",
     "phraseID": "stn_boralla5"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla6) { #v-stn_boralla6 }

**Entry ID:** `stn_boralla6` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla6)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla6.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla6-stn_boralla6"></span>**`stn_boralla6`** Boralla: “How did you know I'm here?”

    - “I won't reveal my secrets so easily. Now disappear, I'm already counting. 1, 2, 3...” → [stn_boralla6_12](#d-stn_boralla6-stn_boralla6_12)

    <span id="d-stn_boralla6-stn_boralla6_12"></span>**`stn_boralla6_12`** Boralla: “No! Wait!” — **effects:** spawns monsters on stoutford_ne, removes monsters from stoutford_ne

    - “...9, 10 Coming!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla6)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla6` |
    | Spawn group | `stn_boralla6` |
    | Loot table | – |
    | Conversation | `stn_boralla6` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla6",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla6",
     "phraseID": "stn_boralla6"
    }
    ```


## Stoutford, Stoutford north-east (stn_boralla7) { #v-stn_boralla7 }

**Entry ID:** `stn_boralla7` · **Type:** NPC

**Location:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stn_boralla7)

### Dialogue simulator

Set your quest stages and items, then talk to Boralla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_boralla7.json" data-npc="Boralla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_boralla7-stn_boralla7"></span>**`stn_boralla7`** Boralla: “That time it took you a bit longer to find me!”

    - “Indeed. Once more?” → [stn_boralla_end](#d-stn_boralla7-stn_boralla_end)

    <span id="d-stn_boralla7-stn_boralla_end"></span>**`stn_boralla_end`** Boralla: “Ha ha - no! I have to go home for lunch now. What a pity. I had fun with you! See you!” — **effects:** removes monsters from stoutford_ne

    - “Yes, bye.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stn_boralla7)"

    | | |
    |---|---|
    | Entry ID | `stn_boralla7` |
    | Spawn group | `stn_boralla7` |
    | Loot table | – |
    | Conversation | `stn_boralla7` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:54` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_boralla7",
     "name": "Boralla",
     "iconID": "monsters_tometik2:54",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stn_boralla7",
     "phraseID": "stn_boralla7"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_boralla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_boralla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_boralla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_boralla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
