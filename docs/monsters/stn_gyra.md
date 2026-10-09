---
description: "Gyra is a non-player character (NPC) in Andor's Trail, found in Stoutford castle 1, Flagstone Prison, Stoutford, Prim, Flagstone Prison, Stoutford, Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_ld1_158.png){ .sprite } Gyra

**Where to find Gyra:** [Stoutford castle 1](#v-stn_gyra), [Flagstone Prison, Flagstone 0 and 17 more](#v-stn_gyra1), [Flagstone Prison, Flagstone 0 and 10 more](#v-stn_gyra2), [Flagstone Prison, Stoutford castle 0 and 6 more](#v-stn_gyra3), [Flagstone Prison, Stoutford castle 0 and 5 more](#v-stn_gyra4), [Flagstone Prison, Waytogalmore 0 and 2 more](#v-stn_gyra5), [Flagstone Prison, Waytogalmore 1](#v-stn_gyra6), [Flagstone Prison, Waytogalmore 1](#v-stn_gyra7), [Flagstone Prison, Waytogalmore 1](#v-stn_gyra8), [Flagstone Prison, Waytogalmore 1](#v-stn_gyra9), [Flagstone Prison, Waytogalmore 1](#v-stn_gyraA), [Flagstone Prison, Waytogalmore 1](#v-stn_gyraB), [Flagstone Prison, Waytogalmore 1](#v-stn_gyraC)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_158.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Stoutford castle 1, Flagstone Prison, Stoutford, Prim, Flagstone Prison, Stoutford, Flagstone Prison |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Stoutford castle 1 { #v-stn_gyra }

**Where:** [Stoutford castle 1](../maps/stoutford_castle1.md#pin-npc-stn_gyra)

### Quests

- [Lost girl looking for lost things](../quests/stn_quest_gyra.md): stages 20, 30
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 11

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra_init.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_gyra-stn_gyra_init"></span>**`stn_gyra_init`** Gyra: “Help! You must help me! Please!”

    - “What is your problem, my little one?” → [stn_gyra_init_10](#d-stn_gyra-stn_gyra_init_10)

    <span id="d-stn_gyra-stn_gyra_init_10"></span>**`stn_gyra_init_10`** Gyra: “I am Gyra, Odirath's daughter. My father is the armorer of Stoutford, a very important man.”

    - Next → [stn_gyra_init_12](#d-stn_gyra-stn_gyra_init_12)

    <span id="d-stn_gyra-stn_gyra_init_12"></span>**`stn_gyra_init_12`** Gyra: “I was looking for Lord Bourbon's helmet, when I was surprised by these monsters.” — **effects:** sets stage 20 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-20)

    - Next → [stn_gyra_init_20](#d-stn_gyra-stn_gyra_init_20)

    <span id="d-stn_gyra-stn_gyra_init_20"></span>**`stn_gyra_init_20`** Gyra: “So I hid here in the storeroom and didn't dare to leave the hiding place.”

    - “Eh, I will be back soon. Maybe. But ... probably not, no. I hate kids.” → *conversation ends*
    - “Of course I will help you. Just follow me.” → [stn_gyra_init_50](#d-stn_gyra-stn_gyra_init_50)

    <span id="d-stn_gyra-stn_gyra_init_50"></span>**`stn_gyra_init_50`** Gyra: “Great! It is so important that Lord Bourbon gets his helmet. Then he will drive out these monsters!”

    - Next → [stn_gyra_init_52](#d-stn_gyra-stn_gyra_init_52)

    <span id="d-stn_gyra-stn_gyra_init_52"></span>**`stn_gyra_init_52`** Gyra: “I started to look in the main house, but maybe we have to search the whole castle.” — **effects:** sets stage 30 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-30), sets stage 11 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-11), starts timer “stn_gyra_hint”, removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1

    - “Let's go then.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Flagstone 0 and 17 more { #v-stn_gyra1 }

**Where:** Flagstone Prison: [Flagstone 0](../maps/flagstone0.md#pin-npc-stn_gyra1), Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-stn_gyra1), Flagstone Prison: [Stoutford castle shop](../maps/stoutford_castle_shop.md#pin-npc-stn_gyra1), Flagstone Prison: [Stoutford castle stable](../maps/stoutford_castle_stable.md#pin-npc-stn_gyra1), Flagstone Prison: [Stoutford castle tower 0](../maps/stoutford_castle_tower0.md#pin-npc-stn_gyra1), Flagstone Prison: [Stoutford castle tower 1](../maps/stoutford_castle_tower1.md#pin-npc-stn_gyra1) (+12 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle 1](../maps/stoutford_castle1.md) | – | 1 | Appears later, during a quest |
| [Stoutford castle 2](../maps/stoutford_castle2.md) | – | 1 | Appears later, during a quest |
| [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md) | Stoutford | 1 | Appears later, during a quest |
| [Stoutford castle barrack 1](../maps/stoutford_castle_barrack1.md) | Stoutford | 1 | Appears later, during a quest |
| [Stoutford castle barrack 2](../maps/stoutford_castle_barrack2.md) | Prim | 1 | Appears later, during a quest |
| [Stoutford castle shop](../maps/stoutford_castle_shop.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle stable](../maps/stoutford_castle_stable.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle tower 0](../maps/stoutford_castle_tower0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle tower 1](../maps/stoutford_castle_tower1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford tower 3](../maps/stoutford_tower3.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford tower 4](../maps/stoutford_tower4.md) | – | 1 | Appears later, during a quest |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 19](../maps/wild19.md) | Stoutford | 1 | Appears later, during a quest |
| [Wild 22](../maps/wild22.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stn_gyra1-stn_gyra"></span>**`stn_gyra`** Gyra: “Please go ahead. I will follow you, probably.”

    - “Probably?” → [stn_gyra_20](#d-stn_gyra1-stn_gyra_20)
    - “OK, just stay close to me.” → *conversation ends*
    - “Let me carry you for a while.” → [stn_gyra_10](#d-stn_gyra1-stn_gyra_10)

    <span id="d-stn_gyra1-stn_gyra_20"></span>**`stn_gyra_20`** Gyra: “I will follow you wherever you go. Only if I'm too scared, then I will stay where I am. For example, I will never go to Flagstone.”

    - Next → [stn_gyra_22](#d-stn_gyra1-stn_gyra_22)

    <span id="d-stn_gyra1-stn_gyra_10"></span>**`stn_gyra_10`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 29 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-29), applies condition fatigue_minor

    - branch 1 → *NPC leaves*

    <span id="d-stn_gyra1-stn_gyra_22"></span>**`stn_gyra_22`** Gyra: “You may have to carry me from time to time. I'll jump off your back again when I'm rested.”

    - “OK, let's go then.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Flagstone 0 and 10 more { #v-stn_gyra2 }

**Where:** Flagstone Prison: [Flagstone 0](../maps/flagstone0.md#pin-npc-stn_gyra2), Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-stn_gyra2), Flagstone Prison: [Stoutford castle stable](../maps/stoutford_castle_stable.md#pin-npc-stn_gyra2), Flagstone Prison: [Stoutford tower 3](../maps/stoutford_tower3.md#pin-npc-stn_gyra2), Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md#pin-npc-stn_gyra2), Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra2) (+5 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle 1](../maps/stoutford_castle1.md) | – | 1 | Appears later, during a quest |
| [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md) | Stoutford | 1 | Appears later, during a quest |
| [Stoutford castle stable](../maps/stoutford_castle_stable.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford tower 3](../maps/stoutford_tower3.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 19](../maps/wild19.md) | Stoutford | 1 | Appears later, during a quest |
| [Wild 22](../maps/wild22.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Stoutford castle 0 and 6 more { #v-stn_gyra3 }

**Where:** Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-stn_gyra3), Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md#pin-npc-stn_gyra3), Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra3), Flagstone Prison: [Wild 18](../maps/wild18.md#pin-npc-stn_gyra3), Stoutford: [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md#pin-npc-stn_gyra3), Stoutford: [Wild 22](../maps/wild22.md#pin-npc-stn_gyra3) (+1 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle 1](../maps/stoutford_castle1.md) | – | 1 | Appears later, during a quest |
| [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md) | Stoutford | 1 | Appears later, during a quest |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 22](../maps/wild22.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Stoutford castle 0 and 5 more { #v-stn_gyra4 }

**Where:** Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-stn_gyra4), Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md#pin-npc-stn_gyra4), Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra4), Flagstone Prison: [Wild 18](../maps/wild18.md#pin-npc-stn_gyra4), Stoutford: [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md#pin-npc-stn_gyra4), Stoutford: [Wild 22](../maps/wild22.md#pin-npc-stn_gyra4)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Stoutford castle barrack 0](../maps/stoutford_castle_barrack0.md) | Stoutford | 1 | Appears later, during a quest |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 22](../maps/wild22.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 0 and 2 more { #v-stn_gyra5 }

**Where:** Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md#pin-npc-stn_gyra5), Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra5), Stoutford: [Wild 22](../maps/wild22.md#pin-npc-stn_gyra5)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 1 | Appears later, during a quest |
| [Wild 22](../maps/wild22.md) | Stoutford | 1 | Appears later, during a quest |

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 { #v-stn_gyra6 }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra6)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (2) { #v-stn_gyra7 }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra7)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (3) { #v-stn_gyra8 }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra8)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (4) { #v-stn_gyra9 }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyra9)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (5) { #v-stn_gyraA }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyraA)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (6) { #v-stn_gyraB }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyraB)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 1 (7) { #v-stn_gyraC }

**Where:** Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-stn_gyraC)

### Quests

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 29

### Dialogue simulator

Set your quest stages and items, then talk to Gyra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stn_gyra.json" data-npc="Gyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stn_gyra](#d-stn_gyra1-stn_gyra).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**13 entries.** The game data defines 13 separate characters named Gyra. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, movement.

| Entry | Type | Section |
|---|---|---|
| `stn_gyra` | NPC | [Stoutford castle 1](#v-stn_gyra) |
| `stn_gyra1` | NPC | [Flagstone Prison, Flagstone 0 and 17 more](#v-stn_gyra1) |
| `stn_gyra2` | NPC | [Flagstone Prison, Flagstone 0 and 10 more](#v-stn_gyra2) |
| `stn_gyra3` | NPC | [Flagstone Prison, Stoutford castle 0 and 6 more](#v-stn_gyra3) |
| `stn_gyra4` | NPC | [Flagstone Prison, Stoutford castle 0 and 5 more](#v-stn_gyra4) |
| `stn_gyra5` | NPC | [Flagstone Prison, Waytogalmore 0 and 2 more](#v-stn_gyra5) |
| `stn_gyra6` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyra6) |
| `stn_gyra7` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyra7) |
| `stn_gyra8` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyra8) |
| `stn_gyra9` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyra9) |
| `stn_gyraA` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyraA) |
| `stn_gyraB` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyraB) |
| `stn_gyraC` | NPC | [Flagstone Prison, Waytogalmore 1](#v-stn_gyraC) |

??? info "Technical information: stn_gyra"

    | | |
    |---|---|
    | Entry ID | `stn_gyra` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra` |
    | Loot table | – |
    | Conversation | `stn_gyra_init` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "stn_gyra_init"
    }
    ```

??? info "Technical information: stn_gyra1"

    | | |
    |---|---|
    | Entry ID | `stn_gyra1` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra1` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra1",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra2"

    | | |
    |---|---|
    | Entry ID | `stn_gyra2` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra2` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra2",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra3"

    | | |
    |---|---|
    | Entry ID | `stn_gyra3` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra3` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra3",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra4"

    | | |
    |---|---|
    | Entry ID | `stn_gyra4` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra4` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra4",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra5"

    | | |
    |---|---|
    | Entry ID | `stn_gyra5` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra5` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra5",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra6"

    | | |
    |---|---|
    | Entry ID | `stn_gyra6` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra6` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra6",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra7"

    | | |
    |---|---|
    | Entry ID | `stn_gyra7` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra7` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra7",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra8"

    | | |
    |---|---|
    | Entry ID | `stn_gyra8` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra8` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra8",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyra9"

    | | |
    |---|---|
    | Entry ID | `stn_gyra9` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyra9` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyra9",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyraA"

    | | |
    |---|---|
    | Entry ID | `stn_gyraA` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyraA` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyraA",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyraB"

    | | |
    |---|---|
    | Entry ID | `stn_gyraB` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyraB` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyraB",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```

??? info "Technical information: stn_gyraC"

    | | |
    |---|---|
    | Entry ID | `stn_gyraC` |
    | Type (wiki) | NPC |
    | Spawn group | `stn_gyraC` |
    | Loot table | – |
    | Conversation | `stn_gyra` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:158` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_gyraC",
     "name": "Gyra",
     "iconID": "monsters_ld1:158",
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "phraseID": "stn_gyra"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_gyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
