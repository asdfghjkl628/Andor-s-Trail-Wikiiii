---
description: "Laeroth prisoner is a non-player character (NPC) in Andor's Trail, found in Laerothprison 4. Starts Shadow of the torturer."
---

# ![](../assets/icons/monsters/monsters_newb_1_652.png){ .sprite } Laeroth prisoner

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_652.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Shadow of the torturer](../quests/lae_torturer.md) |
| **Found in** | Laerothprison 4 |
| **Entries in game data** | 11 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

!!! info "11 entries in the game data"
    The game data defines 11 separate characters named Laeroth prisoner. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`lae_prisoner`](#v-lae_prisoner) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner) | – |
| [`lae_prisoner1`](#v-lae_prisoner1) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner1) | – |
| [`lae_prisoner2`](#v-lae_prisoner2) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2) | – |
| [`lae_prisoner2a`](#v-lae_prisoner2a) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2a) | – |
| [`lae_prisoner2i`](#v-lae_prisoner2i) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2i) | – |
| [`lae_prisoner3`](#v-lae_prisoner3) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3) | – |
| [`lae_prisoner3a`](#v-lae_prisoner3a) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3a) | – |
| [`lae_prisoner3i`](#v-lae_prisoner3i) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3i) | – |
| [`lae_prisoner4`](#v-lae_prisoner4) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner4) | starts [Shadow of the torturer](../quests/lae_torturer.md) |
| [`lae_prisoner4i`](#v-lae_prisoner4i) | NPC | [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner4i) | starts [Shadow of the torturer](../quests/lae_torturer.md) |
| [`lae_prisoner4a`](#v-lae_prisoner4a) | NPC | Not on a map | starts [Shadow of the torturer](../quests/lae_torturer.md) |

## Laerothprison 4 (lae_prisoner) { #v-lae_prisoner }

**Entry ID:** `lae_prisoner` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_prisoner-lae_prison1"></span>**`lae_prison1`** Laeroth prisoner: “Please help us!”




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner` |
    | Spawn group | `lae_prisoner` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:652` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner",
     "name": "Laeroth prisoner",
     "iconID": "monsters_newb_1:652",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner1) { #v-lae_prisoner1 }

**Entry ID:** `lae_prisoner1` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner1)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner1)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner1` |
    | Spawn group | `lae_prisoner1` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:175` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner1",
     "name": "Laeroth prisoner",
     "iconID": "monsters_ld2:175",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner2) { #v-lae_prisoner2 }

**Entry ID:** `lae_prisoner2` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner2)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner2` |
    | Spawn group | `lae_prisoner2` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:652` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner2",
     "name": "Laeroth prisoner",
     "iconID": "monsters_newb_1:652",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner2a) { #v-lae_prisoner2a }

**Entry ID:** `lae_prisoner2a` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2a)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner2a)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner2a` |
    | Spawn group | `lae_prisoner2a` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:652` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner2a",
     "name": "Laeroth prisoner",
     "iconID": "monsters_newb_1:652",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner2i) { #v-lae_prisoner2i }

**Entry ID:** `lae_prisoner2i` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner2i)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner2i)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner2i` |
    | Spawn group | `lae_prisoner2i` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:652` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner2i",
     "name": "Laeroth prisoner",
     "iconID": "monsters_newb_1:652",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner3) { #v-lae_prisoner3 }

**Entry ID:** `lae_prisoner3` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner3)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner3` |
    | Spawn group | `lae_prisoner3` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:142` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner3",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles2:142",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner3a) { #v-lae_prisoner3a }

**Entry ID:** `lae_prisoner3a` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3a)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner3a)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner3a` |
    | Spawn group | `lae_prisoner3a` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:142` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner3a",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles2:142",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner3i) { #v-lae_prisoner3i }

**Entry ID:** `lae_prisoner3i` · **Type:** NPC

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner3i)

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison1.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison1](#d-lae_prisoner-lae_prison1).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner3i)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner3i` |
    | Spawn group | `lae_prisoner3i` |
    | Loot table | – |
    | Conversation | `lae_prison1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:142` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner3i",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles2:142",
     "monsterClass": "undead",
     "phraseID": "lae_prison1"
    }
    ```


## Laerothprison 4 (lae_prisoner4) { #v-lae_prisoner4 }

**Entry ID:** `lae_prisoner4` · **Type:** NPC · **Role:** Starts [Shadow of the torturer](../quests/lae_torturer.md)

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner4)

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stages 5, 10, 20, 80, 130

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison_01.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_prisoner4-lae_prison_01"></span>**`lae_prison_01`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25))* → [lae_prison_end](#d-lae_prisoner4-lae_prison_end)
    - branch 2 *(if reached stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34))* → [lae_prison_02](#d-lae_prisoner4-lae_prison_02)
    - branch 3 → [lae_prison_01a](#d-lae_prisoner4-lae_prison_01a)

    <span id="d-lae_prisoner4-lae_prison_end"></span>**`lae_prison_end`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Kotheses](../monsters/kotheses.md); NOT reached stage 80 of [Shadow of the torturer](../quests/lae_torturer.md#stage-80))* → [lae_prison_end_10](#d-lae_prisoner4-lae_prison_end_10)
    - branch 2 *(if killed 1× [Kotheses](../monsters/kotheses.md))* → [lae_prison_end_20](#d-lae_prisoner4-lae_prison_end_20)
    - branch 3 *(if reached stage 114 of [Shadow of the torturer](../quests/lae_torturer.md#stage-114); NOT reached stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130))* → [lae_prison_end_30](#d-lae_prisoner4-lae_prison_end_30)
    - branch 4 *(if reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); NOT killed 1× [Kotheses](../monsters/kotheses.md))* → [lae_prison_3a](#d-lae_prisoner4-lae_prison_3a)

    <span id="d-lae_prisoner4-lae_prison_02"></span>**`lae_prison_02`** Laeroth prisoner: “Please, can you help us?”

    - “What sort of help?” → [lae_prison_02a](#d-lae_prisoner4-lae_prison_02a)

    <span id="d-lae_prisoner4-lae_prison_01a"></span>**`lae_prison_01a`** Laeroth prisoner: “Please, can you help us?”

    - “What sort of help?” → [lae_prison_01b](#d-lae_prisoner4-lae_prison_01b)

    <span id="d-lae_prisoner4-lae_prison_end_10"></span>**`lae_prison_end_10`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Oh, the kid is back. Just look!”

    - “You can finally find peace. Kotheses, the torturer is dead.” → [lae_prison_end_20](#d-lae_prisoner4-lae_prison_end_20)

    <span id="d-lae_prisoner4-lae_prison_end_20"></span>**`lae_prison_end_20`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Ooooh! We are eternally grateful!” — **effects:** sets stage 80 of [Shadow of the torturer](../quests/lae_torturer.md#stage-80)


    <span id="d-lae_prisoner4-lae_prison_end_30"></span>**`lae_prison_end_30`** Laeroth prisoner: “Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.” — **effects:** sets stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130)

    - Next → [lae_prison_3a](#d-lae_prisoner4-lae_prison_3a)

    <span id="d-lae_prisoner4-lae_prison_3a"></span>**`lae_prison_3a`** [Laeroth prisoner](../monsters/lae_prisoner.md): “Ohhh! What will become of us?” — **effects:** sets stage 20 of [Shadow of the torturer](../quests/lae_torturer.md#stage-20)


    <span id="d-lae_prisoner4-lae_prison_02a"></span>**`lae_prison_02a`** Laeroth prisoner: “The prison torturer died, but he took the life force of us prisoners in the hope to live again.”

    - Next → [lae_prison_02b](#d-lae_prisoner4-lae_prison_02b)

    <span id="d-lae_prisoner4-lae_prison_01b"></span>**`lae_prison_01b`** Laeroth prisoner: “Please open the other cells and free us all! Hurry! Then come back to me.”

    - “OK, just a second ...” → *conversation ends*

    <span id="d-lae_prisoner4-lae_prison_02b"></span>**`lae_prison_02b`** Laeroth prisoner: “It didn't work, because we had so little life left anyway.” — **effects:** sets stage 5 of [Shadow of the torturer](../quests/lae_torturer.md#stage-5), changes map laerothprison4

    - Next → [lae_prison_02c](#d-lae_prisoner4-lae_prison_02c)

    <span id="d-lae_prisoner4-lae_prison_02c"></span>**`lae_prison_02c`** Laeroth prisoner: “But now we cannot rest in peace, because he is still here, somewhere in the lower caves. He needs to be destroyed, but we cannot do it because he has control over us.”

    - “OK. I'll do it. I am not afraid of a few monsters!” *(if NOT reached stage 20 of [Shadow of the torturer](../quests/lae_torturer.md#stage-20))* → [lae_prison_03](#d-lae_prisoner4-lae_prison_03)
    - “No thanks. Seems dangerous, and there's nothing in it for me.” *(if NOT reached stage 10 of [Shadow of the torturer](../quests/lae_torturer.md#stage-10))* → [lae_prison_3a](#d-lae_prisoner4-lae_prison_3a)

    <span id="d-lae_prisoner4-lae_prison_03"></span>**`lae_prison_03`** Laeroth prisoner: “Thank you! But beware! He has guards that are like him. They may appear to be human at first glance, but they are not!” — **effects:** sets stage 10 of [Shadow of the torturer](../quests/lae_torturer.md#stage-10)




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner4)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner4` |
    | Spawn group | `lae_prisoner4` |
    | Loot table | – |
    | Conversation | `lae_prison_01` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:75` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner4",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles1:75",
     "monsterClass": "undead",
     "phraseID": "lae_prison_01"
    }
    ```


## Laerothprison 4 (lae_prisoner4i) { #v-lae_prisoner4i }

**Entry ID:** `lae_prisoner4i` · **Type:** NPC · **Role:** Starts [Shadow of the torturer](../quests/lae_torturer.md)

**Location:** [Laerothprison 4](../maps/laerothprison4.md#pin-npc-lae_prisoner4i)

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stages 5, 10, 20, 80, 130

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison_01.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison_01](#d-lae_prisoner4-lae_prison_01).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner4i)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner4i` |
    | Spawn group | `lae_prisoner4i` |
    | Loot table | – |
    | Conversation | `lae_prison_01` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:75` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner4i",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles1:75",
     "monsterClass": "undead",
     "phraseID": "lae_prison_01"
    }
    ```


## Not placed on a map (lae_prisoner4a) { #v-lae_prisoner4a }

**Entry ID:** `lae_prisoner4a` · **Type:** NPC · **Role:** Starts [Shadow of the torturer](../quests/lae_torturer.md)

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Quests

- [Shadow of the torturer](../quests/lae_torturer.md): stages 5, 10, 20, 80, 130

### Dialogue simulator

Set your quest stages and items, then talk to Laeroth prisoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_prison_01.json" data-npc="Laeroth prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [lae_prison_01](#d-lae_prisoner4-lae_prison_01).


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_prisoner4a)"

    | | |
    |---|---|
    | Entry ID | `lae_prisoner4a` |
    | Spawn group | `lae_prisoner4a` |
    | Loot table | – |
    | Conversation | `lae_prison_01` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:75` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_prisoner4a",
     "name": "Laeroth prisoner",
     "iconID": "monsters_rltiles1:75",
     "monsterClass": "undead",
     "phraseID": "lae_prison_01"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
