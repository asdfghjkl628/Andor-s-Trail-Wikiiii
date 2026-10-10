---
description: "Commoner is a non-player character (NPC) in Andor's Trail, found in Remgard, Brimhaven, Stoutford."
---

# ![](../assets/icons/monsters/monsters_ld1_132.png){ .sprite } Commoner

**Where to find Commoner:** [Remgard, Remgard 0](#v-rg_villager1), [Brimhaven, Brimhaven 3 and 1 more](#v-brv_villager1), [Brimhaven, Brimhaven 4](#v-brv_villager2), [Brimhaven, Brimhaven 3 and 1 more](#v-brv_villager4), [Brimhaven, Brimhaven 4](#v-brv_villager5), [Brimhaven, Brimhaven 2](#v-brv_villager6), [Brimhaven, Brimhaven 2](#v-brv_villager7), [Brimhaven, Brimhaven 2](#v-brv_villager8), [Brimhaven, Brimhaven 1](#v-brv_villager9), [Brimhaven, Brimhaven 2](#v-brv_villager10), [Brimhaven, Brimhaven 1](#v-brv_villager11), [Brimhaven, Brimhaven 3](#v-brv_villager14), [Brimhaven, Brimhaven 3](#v-brv_villager15), [Remgard, Remgard 1](#v-rg_villager2), [Remgard, Remgard 4](#v-rg_villager3), [Remgard, Remgard 1](#v-rg_villager4), [Remgard, Remgard 2](#v-rg_villager5), [Remgard, Remgard 2](#v-rg_villager6), [Remgard, Remgard 3](#v-rg_villager7), [Remgard, Remgard 4](#v-rg_villager8), [Stoutford, Stoutford gate](#v-stoutford_commoner), [Stoutford, Stoutford north-east](#v-stoutford_commoner2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_132.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Remgard, Brimhaven, Stoutford |
| **Introduced** | v0.7.0 or earlier |

</div>

## Remgard, Remgard 0 { #v-rg_villager1 }

**Where:** Remgard: [Remgard 0](../maps/remgard0.md#pin-npc-rg_villager1)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager1.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager1-remgard_villager1"></span>**`remgard_villager1`** Commoner: “I don't recognize you. You're not from Remgard, are you?”

    - “No, I am from a small settlement called Crossglen, and I am looking for my brother Andor.” → [remgard_villager1_2](#d-rg_villager1-remgard_villager1_2)

    <span id="d-rg_villager1-remgard_villager1_2"></span>**`remgard_villager1_2`** Commoner: “OK then. Good luck with that.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Ok then. Good luck with that.” → “OK then. Good luck with that.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 3 and 1 more { #v-brv_villager1 }

**Where:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_villager1), Brimhaven: [Brimhaven 4](../maps/brimhaven4.md#pin-npc-brv_villager1)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven 3](../maps/brimhaven3.md) | Brimhaven | 1 | – |
| [Brimhaven 4](../maps/brimhaven4.md) | Brimhaven | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager1.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager1-brv_villager1"></span>**`brv_villager1`** Commoner: “Hello.”

    - “I'm wondering, do you know anything about Lawellyn's death?” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [brv_asd_no_info_10](#d-brv_villager1-brv_asd_no_info_10)

    <span id="d-brv_villager1-brv_asd_no_info_10"></span>**`brv_asd_no_info_10`** Commoner: “No, I am sorry, I don't.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “No, I am sorry, I don't” → “No, I am sorry, I don't.” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line changed<br>· text: “Hello” → “Hello.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 4 { #v-brv_villager2 }

**Where:** Brimhaven: [Brimhaven 4](../maps/brimhaven4.md#pin-npc-brv_villager2)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager2.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager2-brv_villager2"></span>**`brv_villager2`** Commoner: “If you want to make some money. Go to the tavern.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 3 and 1 more (2) { #v-brv_villager4 }

**Where:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_villager4), Brimhaven: [Brimhaven 4](../maps/brimhaven4.md#pin-npc-brv_villager4)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven 3](../maps/brimhaven3.md) | Brimhaven | 1 | – |
| [Brimhaven 4](../maps/brimhaven4.md) | Brimhaven | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager4.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager4-brv_villager4"></span>**`brv_villager4`** Commoner: “Excuse me, I have no time to talk.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 4 (2) { #v-brv_villager5 }

**Where:** Brimhaven: [Brimhaven 4](../maps/brimhaven4.md#pin-npc-brv_villager5)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager5.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager5-brv_villager5"></span>**`brv_villager5`** Commoner: “Good day.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 2 { #v-brv_villager6 }

**Where:** Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_villager6)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager6.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager6-brv_villager6"></span>**`brv_villager6`** Commoner: “Don't get in my way. Are you one of those guys from the east side of the town, without manners?”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 2 (2) { #v-brv_villager7 }

**Where:** Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_villager7)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager7.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager7-brv_villager7"></span>**`brv_villager7`** Commoner: “I don't recognize you. Are you one of those people from the east part of the town, who send their children wearing cheap clothes to our school?”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 2 (3) { #v-brv_villager8 }

**Where:** Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_villager8)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager8.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager8-brv_villager8"></span>**`brv_villager8`** Commoner: “You look a bit old for a pupil.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 1 { #v-brv_villager9 }

**Where:** Brimhaven: [Brimhaven 1](../maps/brimhaven1.md#pin-npc-brv_villager9)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager9.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager9-brv_villager9"></span>**`brv_villager9`** Commoner: “Hello. Great dam. Isn't it? We people from the west side of the town paid for the dam because the people from the east side can't afford it.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 2 (4) { #v-brv_villager10 }

**Where:** Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_villager10)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager10.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager10-brv_villager10"></span>**`brv_villager10`** Commoner: “Taking our good water? Go to the east side of the town. Oh, I forgot... you can't afford a well of your own.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 1 (2) { #v-brv_villager11 }

**Where:** Brimhaven: [Brimhaven 1](../maps/brimhaven1.md#pin-npc-brv_villager11)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager11.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager11-brv_villager11"></span>**`brv_villager11`** Commoner: “The people from the west side of town forced us to support the dam, but we don't get any benefit from it and they took all the good land.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 3 { #v-brv_villager14 }

**Where:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_villager14)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager14.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager14-brv_villager14"></span>**`brv_villager14`** Commoner: “Get out of my way. Do you think you are better than me just because you are one of those rich guys from the western part of the town?”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven 3 (2) { #v-brv_villager15 }

**Where:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_villager15)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_villager15.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_villager15-brv_villager15"></span>**`brv_villager15`** Commoner: “If you need a place to sleep, visit the inn. There are beds available for rent.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 1 { #v-rg_villager2 }

**Where:** Remgard: [Remgard 1](../maps/remgard1.md#pin-npc-rg_villager2)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager2.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager2-remgard_villager2"></span>**`remgard_villager2`** Commoner: “Don't get in my way, I'm trying to walk here, don't you see?”

    - “No problem, please go ahead.” → *conversation ends*
    - “No, you get out of *my* way!” → [remgard_villager2_2](#d-rg_villager2-remgard_villager2_2)

    <span id="d-rg_villager2-remgard_villager2_2"></span>**`remgard_villager2_2`** Commoner: “Hah! *snort*”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 4 { #v-rg_villager3 }

**Where:** Remgard: [Remgard 4](../maps/remgard4.md#pin-npc-rg_villager3)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager3.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager3-remgard_villager3"></span>**`remgard_villager3`** Commoner: “Have you seen my ring? I dropped it among these trees, I am sure. That was a pretty ring.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 1 (2) { #v-rg_villager4 }

**Where:** Remgard: [Remgard 1](../maps/remgard1.md#pin-npc-rg_villager4)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager4.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager4-remgard_villager4"></span>**`remgard_villager4`** Commoner: “Good day.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 2 { #v-rg_villager5 }

**Where:** Remgard: [Remgard 2](../maps/remgard2.md#pin-npc-rg_villager5)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager5.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager5-remgard_villager5"></span>**`remgard_villager5`** Commoner: “Excuse me, I have no time to talk.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 2 (2) { #v-rg_villager6 }

**Where:** Remgard: [Remgard 2](../maps/remgard2.md#pin-npc-rg_villager6)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager6.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager6-remgard_villager6"></span>**`remgard_villager6`** Commoner: “You are not from around here, are you? If you ever need a place to stay, visit the tavern. I hear that Kendelow has a room available for rent.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 3 { #v-rg_villager7 }

**Where:** Remgard: [Remgard 3](../maps/remgard3.md#pin-npc-rg_villager7)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager7.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager7-remgard_villager7"></span>**`remgard_villager7`** Commoner: “I have heard strange noises from across the water of lake Laeroth. I wonder what lurks on the shores of the other side.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 4 (2) { #v-rg_villager8 }

**Where:** Remgard: [Remgard 4](../maps/remgard4.md#pin-npc-rg_villager8)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_villager8.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rg_villager8-remgard_villager8"></span>**`remgard_villager8`** Commoner: “Hello.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Stoutford, Stoutford gate { #v-stoutford_commoner }

**Where:** Stoutford: [Stoutford gate](../maps/stoutford_gate.md#pin-npc-stoutford_commoner)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_commoner_0.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_commoner-stoutford_commoner_0"></span>**`stoutford_commoner_0`** Commoner: “Welcome to Stoutford kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Stoutford, Stoutford north-east { #v-stoutford_commoner2 }

**Where:** Stoutford: [Stoutford north-east](../maps/stoutford_ne.md#pin-npc-stoutford_commoner2)

### Dialogue simulator

Set your quest stages and items, then talk to Commoner. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_commoner_0.json" data-npc="Commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stoutford_commoner_0](#d-stoutford_commoner-stoutford_commoner_0).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**22 entries.** The game data defines 22 separate characters named Commoner. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `rg_villager1` | NPC | [Remgard, Remgard 0](#v-rg_villager1) |
| `brv_villager1` | NPC | [Brimhaven, Brimhaven 3 and 1 more](#v-brv_villager1) |
| `brv_villager2` | NPC | [Brimhaven, Brimhaven 4](#v-brv_villager2) |
| `brv_villager4` | NPC | [Brimhaven, Brimhaven 3 and 1 more](#v-brv_villager4) |
| `brv_villager5` | NPC | [Brimhaven, Brimhaven 4](#v-brv_villager5) |
| `brv_villager6` | NPC | [Brimhaven, Brimhaven 2](#v-brv_villager6) |
| `brv_villager7` | NPC | [Brimhaven, Brimhaven 2](#v-brv_villager7) |
| `brv_villager8` | NPC | [Brimhaven, Brimhaven 2](#v-brv_villager8) |
| `brv_villager9` | NPC | [Brimhaven, Brimhaven 1](#v-brv_villager9) |
| `brv_villager10` | NPC | [Brimhaven, Brimhaven 2](#v-brv_villager10) |
| `brv_villager11` | NPC | [Brimhaven, Brimhaven 1](#v-brv_villager11) |
| `brv_villager14` | NPC | [Brimhaven, Brimhaven 3](#v-brv_villager14) |
| `brv_villager15` | NPC | [Brimhaven, Brimhaven 3](#v-brv_villager15) |
| `rg_villager2` | NPC | [Remgard, Remgard 1](#v-rg_villager2) |
| `rg_villager3` | NPC | [Remgard, Remgard 4](#v-rg_villager3) |
| `rg_villager4` | NPC | [Remgard, Remgard 1](#v-rg_villager4) |
| `rg_villager5` | NPC | [Remgard, Remgard 2](#v-rg_villager5) |
| `rg_villager6` | NPC | [Remgard, Remgard 2](#v-rg_villager6) |
| `rg_villager7` | NPC | [Remgard, Remgard 3](#v-rg_villager7) |
| `rg_villager8` | NPC | [Remgard, Remgard 4](#v-rg_villager8) |
| `stoutford_commoner` | NPC | [Stoutford, Stoutford gate](#v-stoutford_commoner) |
| `stoutford_commoner2` | NPC | [Stoutford, Stoutford north-east](#v-stoutford_commoner2) |

??? info "Technical information: rg_villager1"

    | | |
    |---|---|
    | Entry ID | `rg_villager1` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager1` |
    | Loot table | – |
    | Conversation | `remgard_villager1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager1",
     "name": "Commoner",
     "iconID": "monsters_ld1:132",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager1",
     "phraseID": "remgard_villager1"
    }
    ```

??? info "Technical information: brv_villager1"

    | | |
    |---|---|
    | Entry ID | `brv_villager1` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager1` |
    | Loot table | – |
    | Conversation | `brv_villager1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager1",
     "name": "Commoner",
     "iconID": "monsters_ld1:132",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager1",
     "phraseID": "brv_villager1"
    }
    ```

??? info "Technical information: brv_villager2"

    | | |
    |---|---|
    | Entry ID | `brv_villager2` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager2` |
    | Loot table | – |
    | Conversation | `brv_villager2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager2",
     "name": "Commoner",
     "iconID": "monsters_ld1:20",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager2",
     "phraseID": "brv_villager2"
    }
    ```

??? info "Technical information: brv_villager4"

    | | |
    |---|---|
    | Entry ID | `brv_villager4` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager4` |
    | Loot table | – |
    | Conversation | `brv_villager4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:74` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager4",
     "name": "Commoner",
     "iconID": "monsters_rltiles1:74",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager4",
     "phraseID": "brv_villager4"
    }
    ```

??? info "Technical information: brv_villager5"

    | | |
    |---|---|
    | Entry ID | `brv_villager5` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager5` |
    | Loot table | – |
    | Conversation | `brv_villager5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:186` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager5",
     "name": "Commoner",
     "iconID": "monsters_ld1:186",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager5",
     "phraseID": "brv_villager5"
    }
    ```

??? info "Technical information: brv_villager6"

    | | |
    |---|---|
    | Entry ID | `brv_villager6` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager6` |
    | Loot table | – |
    | Conversation | `brv_villager6` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:206` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager6",
     "name": "Commoner",
     "iconID": "monsters_ld1:206",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager6",
     "phraseID": "brv_villager6"
    }
    ```

??? info "Technical information: brv_villager7"

    | | |
    |---|---|
    | Entry ID | `brv_villager7` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager7` |
    | Loot table | – |
    | Conversation | `brv_villager7` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:6` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager7",
     "name": "Commoner",
     "iconID": "monsters_karvis2:6",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager7",
     "phraseID": "brv_villager7"
    }
    ```

??? info "Technical information: brv_villager8"

    | | |
    |---|---|
    | Entry ID | `brv_villager8` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager8` |
    | Loot table | – |
    | Conversation | `brv_villager8` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:83` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager8",
     "name": "Commoner",
     "iconID": "monsters_ld1:83",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager8",
     "phraseID": "brv_villager8"
    }
    ```

??? info "Technical information: brv_villager9"

    | | |
    |---|---|
    | Entry ID | `brv_villager9` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager9` |
    | Loot table | – |
    | Conversation | `brv_villager9` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:62` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager9",
     "name": "Commoner",
     "iconID": "monsters_ld1:62",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager9",
     "phraseID": "brv_villager9"
    }
    ```

??? info "Technical information: brv_villager10"

    | | |
    |---|---|
    | Entry ID | `brv_villager10` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager10` |
    | Loot table | – |
    | Conversation | `brv_villager10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager10",
     "name": "Commoner",
     "iconID": "monsters_ld1:132",
     "monsterClass": "humanoid",
     "spawnGroup": "brv_villager10",
     "phraseID": "brv_villager10"
    }
    ```

??? info "Technical information: brv_villager11"

    | | |
    |---|---|
    | Entry ID | `brv_villager11` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager11` |
    | Loot table | – |
    | Conversation | `brv_villager11` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:82` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager11",
     "name": "Commoner",
     "iconID": "monsters_ld1:82",
     "phraseID": "brv_villager11"
    }
    ```

??? info "Technical information: brv_villager14"

    | | |
    |---|---|
    | Entry ID | `brv_villager14` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager14` |
    | Loot table | – |
    | Conversation | `brv_villager14` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:60` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager14",
     "name": "Commoner",
     "iconID": "monsters_tometik1:60",
     "phraseID": "brv_villager14"
    }
    ```

??? info "Technical information: brv_villager15"

    | | |
    |---|---|
    | Entry ID | `brv_villager15` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_villager15` |
    | Loot table | – |
    | Conversation | `brv_villager15` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:10` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_villager15",
     "name": "Commoner",
     "iconID": "monsters_tometik6:10",
     "phraseID": "brv_villager15"
    }
    ```

??? info "Technical information: rg_villager2"

    | | |
    |---|---|
    | Entry ID | `rg_villager2` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager2` |
    | Loot table | – |
    | Conversation | `remgard_villager2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager2",
     "name": "Commoner",
     "iconID": "monsters_ld1:20",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager2",
     "phraseID": "remgard_villager2"
    }
    ```

??? info "Technical information: rg_villager3"

    | | |
    |---|---|
    | Entry ID | `rg_villager3` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager3` |
    | Loot table | – |
    | Conversation | `remgard_villager3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:134` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager3",
     "name": "Commoner",
     "iconID": "monsters_ld1:134",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager3",
     "phraseID": "remgard_villager3"
    }
    ```

??? info "Technical information: rg_villager4"

    | | |
    |---|---|
    | Entry ID | `rg_villager4` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager4` |
    | Loot table | – |
    | Conversation | `remgard_villager4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:164` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager4",
     "name": "Commoner",
     "iconID": "monsters_ld1:164",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager4",
     "phraseID": "remgard_villager4"
    }
    ```

??? info "Technical information: rg_villager5"

    | | |
    |---|---|
    | Entry ID | `rg_villager5` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager5` |
    | Loot table | – |
    | Conversation | `remgard_villager5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:148` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager5",
     "name": "Commoner",
     "iconID": "monsters_ld1:148",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager5",
     "phraseID": "remgard_villager5"
    }
    ```

??? info "Technical information: rg_villager6"

    | | |
    |---|---|
    | Entry ID | `rg_villager6` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager6` |
    | Loot table | – |
    | Conversation | `remgard_villager6` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:188` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager6",
     "name": "Commoner",
     "iconID": "monsters_ld1:188",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager6",
     "phraseID": "remgard_villager6"
    }
    ```

??? info "Technical information: rg_villager7"

    | | |
    |---|---|
    | Entry ID | `rg_villager7` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager7` |
    | Loot table | – |
    | Conversation | `remgard_villager7` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:10` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager7",
     "name": "Commoner",
     "iconID": "monsters_ld1:10",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager7",
     "phraseID": "remgard_villager7"
    }
    ```

??? info "Technical information: rg_villager8"

    | | |
    |---|---|
    | Entry ID | `rg_villager8` |
    | Type (wiki) | NPC |
    | Spawn group | `remgard_villager8` |
    | Loot table | – |
    | Conversation | `remgard_villager8` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:18` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rg_villager8",
     "name": "Commoner",
     "iconID": "monsters_rltiles3:18",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_villager8",
     "phraseID": "remgard_villager8"
    }
    ```

??? info "Technical information: stoutford_commoner"

    | | |
    |---|---|
    | Entry ID | `stoutford_commoner` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_commoner` |
    | Loot table | – |
    | Conversation | `stoutford_commoner_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_commoner",
     "name": "Commoner",
     "iconID": "monsters_karvis2:2",
     "phraseID": "stoutford_commoner_0"
    }
    ```

??? info "Technical information: stoutford_commoner2"

    | | |
    |---|---|
    | Entry ID | `stoutford_commoner2` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_commoner2` |
    | Loot table | – |
    | Conversation | `stoutford_commoner_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:0` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_commoner2",
     "name": "Commoner",
     "iconID": "monsters_tometik5:0",
     "phraseID": "stoutford_commoner_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rg_villager1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rg_villager1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rg_villager1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rg_villager1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
