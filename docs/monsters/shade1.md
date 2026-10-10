---
description: "Forsaken shade is an NPC you can also fight in Andor's Trail, found in Undertell 3 02, Undertell 3 12, Undertell 3 13, Undertell 3 11, Undertell 3 00, Undertell 3 10, Undertell 3 03."
---

# ![](../assets/icons/monsters/monsters_newb_1_663.png){ .sprite } Forsaken shade

**Where to find Forsaken shade:** [Undertell 3 02](#v-shade1), [Undertell 3 02](#v-shade2), [Undertell 3 12](#v-shade3), [Undertell 3 12](#v-shade4), [Undertell 3 13](#v-shade5), [Undertell 3 11](#v-shade6), [Undertell 3 00](#v-shade7), [Undertell 3 00](#v-shade8), [Undertell 3 00](#v-shade9), [Undertell 3 10](#v-shade10), [Undertell 3 03](#v-shade11)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_663.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Undertell 3 02, Undertell 3 12, Undertell 3 13, Undertell 3 11, Undertell 3 00, Undertell 3 10, Undertell 3 03 |
| **Class** | Ghost |
| **HP** | 431 |
| **XP when defeated** | 1,221–1,231 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Undertell 3 02 { #v-shade1 }

**Where:** [Undertell 3 02](../maps/undertell_3_02.md#pin-npc-shade1)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,231 |
| Damage | 6 to 8 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-1) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade1_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (38 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade1-shade1_selector"></span>**`shade1_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 140 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140))* → [shade_fight](#d-shade1-shade_fight)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_1](#d-shade1-shade_return_wearing_ring_1)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade1_initial](#d-shade1-shade1_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3)
    - branch 6 → [shade1_initial](#d-shade1-shade1_initial)

    <span id="d-shade1-shade_fight"></span>**`shade_fight`** Forsaken shade: “Your life ends now, mortal.”

    - “I don't think so!” → *fight starts*

    <span id="d-shade1-shade_return_wearing_ring_1"></span>**`shade_return_wearing_ring_1`** Forsaken shade: “Something about you is different, but what?” — **effects:** faction “currentShade” set to 1

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template)

    <span id="d-shade1-shade1_initial"></span>**`shade1_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade1_dismiss_10](#d-shade1-shade1_dismiss_10)

    <span id="d-shade1-shade_retry2"></span>**`shade_retry2`** Forsaken shade: “Go away!”

    - “Wait...” → [shade_retry_dismiss](#d-shade1-shade_retry_dismiss)

    <span id="d-shade1-shade_retry3"></span>**`shade_retry3`** Forsaken shade: “Go away!”

    - “But...I just want to...” → [shade_retry3_dismiss](#d-shade1-shade_retry3_dismiss)

    <span id="d-shade1-shade_dialog_template"></span>**`shade_dialog_template`** Forsaken shade: “Ah! You have overcome our safeguards.”

    - “Your time has come to an end.” → [shade_offer_mercy](#d-shade1-shade_offer_mercy)

    <span id="d-shade1-shade1_dismiss_10"></span>**`shade1_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade raises a translucent hand. A ripple of cold air rolls across the chamber, and space bends around you. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector)

    <span id="d-shade1-shade_retry_dismiss"></span>**`shade_retry_dismiss`** [Dummy NPC](../monsters/none.md): “The shade flickers with annoyance. A dull pulse of power washes over you, pushing you from this place once more.”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector)

    <span id="d-shade1-shade_retry3_dismiss"></span>**`shade_retry3_dismiss`** [Dummy NPC](../monsters/none.md): “The shade shudders in irritation. A wave of cold force swells outward, hurling you from the cavern yet again.”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector)

    <span id="d-shade1-shade_offer_mercy"></span>**`shade_offer_mercy`** Forsaken shade: “Spare us, and we shall reward you when you get out of here. Are we truly monsters or are those who rule and oppress us the true monsters?”

    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 1)* → [shade_freed_1](#d-shade1-shade_freed_1)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 2)* → [shade_freed_2](#d-shade1-shade_freed_2)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 3)* → [shade_freed_3](#d-shade1-shade_freed_3)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 4)* → [shade_freed_4](#d-shade1-shade_freed_4)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 5)* → [shade_freed_5](#d-shade1-shade_freed_5)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 6)* → [shade_freed_6](#d-shade1-shade_freed_6)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 7)* → [shade_freed_7](#d-shade1-shade_freed_7)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 8)* → [shade_freed_8](#d-shade1-shade_freed_8)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 9)* → [shade_freed_9](#d-shade1-shade_freed_9)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 10)* → [shade_freed_10](#d-shade1-shade_freed_10)
    - “[Let it go.] You deserve freedom.” *(if faction “currentShade” = 11)* → [shade_freed_11](#d-shade1-shade_freed_11)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 1)* → [shade_kill_1](#d-shade1-shade_kill_1)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 2)* → [shade_kill_2](#d-shade1-shade_kill_2)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 3)* → [shade_kill_3](#d-shade1-shade_kill_3)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 4)* → [shade_kill_4](#d-shade1-shade_kill_4)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 5)* → [shade_kill_5](#d-shade1-shade_kill_5)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 6)* → [shade_kill_6](#d-shade1-shade_kill_6)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 7)* → [shade_kill_7](#d-shade1-shade_kill_7)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 8)* → [shade_kill_8](#d-shade1-shade_kill_8)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 9)* → [shade_kill_9](#d-shade1-shade_kill_9)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 10)* → [shade_kill_10](#d-shade1-shade_kill_10)
    - “I know my history. You shall cease to exist.” *(if faction “currentShade” = 11)* → [shade_kill_11](#d-shade1-shade_kill_11)
    - “Let me think...” → *conversation ends*

    <span id="d-shade1-undertell_shade_teleport_loc_selector"></span>**`undertell_shade_teleport_loc_selector`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 20 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-20)

    - Next *(if random chance (1/4%))* → [mt_galmore1_h1](#d-shade1-mt_galmore1_h1)
    - Next *(if random chance (1/3%))* → [mt_galmore0_h2](#d-shade1-mt_galmore0_h2)
    - Next *(if random chance (1/2%))* → [mt_galmore1_h5](#d-shade1-mt_galmore1_h5)
    - Next *(if random chance (1/1%))* → [galmore_58](#d-shade1-galmore_58)

    <span id="d-shade1-shade_freed_1"></span>**`shade_freed_1`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 120 of [Devotion](../quests/devotion.md#stage-120), removes monsters from undertell_3_02


    <span id="d-shade1-shade_freed_2"></span>**`shade_freed_2`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 150 of [Devotion](../quests/devotion.md#stage-150), removes monsters from undertell_3_02


    <span id="d-shade1-shade_freed_3"></span>**`shade_freed_3`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 180 of [Devotion](../quests/devotion.md#stage-180), removes monsters from undertell_3_12


    <span id="d-shade1-shade_freed_4"></span>**`shade_freed_4`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 210 of [Devotion](../quests/devotion.md#stage-210), removes monsters from undertell_3_12


    <span id="d-shade1-shade_freed_5"></span>**`shade_freed_5`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 240 of [Devotion](../quests/devotion.md#stage-240), removes monsters from undertell_3_13


    <span id="d-shade1-shade_freed_6"></span>**`shade_freed_6`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 270 of [Devotion](../quests/devotion.md#stage-270), removes monsters from undertell_3_11


    <span id="d-shade1-shade_freed_7"></span>**`shade_freed_7`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 300 of [Devotion](../quests/devotion.md#stage-300), removes monsters from undertell_3_00


    <span id="d-shade1-shade_freed_8"></span>**`shade_freed_8`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 330 of [Devotion](../quests/devotion.md#stage-330), removes monsters from undertell_3_00


    <span id="d-shade1-shade_freed_9"></span>**`shade_freed_9`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 360 of [Devotion](../quests/devotion.md#stage-360), removes monsters from undertell_3_00


    <span id="d-shade1-shade_freed_10"></span>**`shade_freed_10`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 390 of [Devotion](../quests/devotion.md#stage-390), removes monsters from undertell_3_10


    <span id="d-shade1-shade_freed_11"></span>**`shade_freed_11`** Forsaken shade: “Thank you.” — **effects:** faction “shadeSetFreeCount” +1, sets stage 420 of [Devotion](../quests/devotion.md#stage-420), removes monsters from undertell_3_03


    <span id="d-shade1-shade_kill_1"></span>**`shade_kill_1`** Forsaken shade: “You shall not live.” — **effects:** sets stage 140 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_2"></span>**`shade_kill_2`** Forsaken shade: “You shall not live.” — **effects:** sets stage 170 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_3"></span>**`shade_kill_3`** Forsaken shade: “You shall not live.” — **effects:** sets stage 200 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_4"></span>**`shade_kill_4`** Forsaken shade: “You shall not live.” — **effects:** sets stage 230 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_5"></span>**`shade_kill_5`** Forsaken shade: “You shall not live.” — **effects:** sets stage 260 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_6"></span>**`shade_kill_6`** Forsaken shade: “You shall not live.” — **effects:** sets stage 290 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_7"></span>**`shade_kill_7`** Forsaken shade: “You shall not live.” — **effects:** sets stage 320 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_8"></span>**`shade_kill_8`** Forsaken shade: “You shall not live.” — **effects:** sets stage 350 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_9"></span>**`shade_kill_9`** Forsaken shade: “You shall not live.” — **effects:** sets stage 380 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_10"></span>**`shade_kill_10`** Forsaken shade: “You shall not live.” — **effects:** sets stage 410 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410)

    - “We will see!” → *fight starts*

    <span id="d-shade1-shade_kill_11"></span>**`shade_kill_11`** Forsaken shade: “You shall not live.” — **effects:** sets stage 440 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440)

    - “We will see!” → *fight starts*

    <span id="d-shade1-mt_galmore1_h1"></span>**`mt_galmore1_h1`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [Mt galmore 1 h 1](../maps/mt_galmore1_h1.md)


    <span id="d-shade1-mt_galmore0_h2"></span>**`mt_galmore0_h2`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [Mt galmore 0 h 2](../maps/mt_galmore0_h2.md)


    <span id="d-shade1-mt_galmore1_h5"></span>**`mt_galmore1_h5`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [Mt galmore 1 h 5](../maps/mt_galmore1_h5.md)


    <span id="d-shade1-galmore_58"></span>**`galmore_58`** *(silent check: the first matching branch below is taken)* — **effects:** moves you to [Galmore 58](../maps/galmore_58.md)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 02 (2) { #v-shade2 }

**Where:** [Undertell 3 02](../maps/undertell_3_02.md#pin-npc-shade2)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-2) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade2_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade2-shade2_selector"></span>**`shade2_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 170 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_2](#d-shade2-shade_return_wearing_ring_2)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade2_initial](#d-shade2-shade2_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade2_initial](#d-shade2-shade2_initial)

    <span id="d-shade2-shade_return_wearing_ring_2"></span>**`shade_return_wearing_ring_2`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 2

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade2-shade2_initial"></span>**`shade2_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade2_dismiss_10](#d-shade2-shade2_dismiss_10)

    <span id="d-shade2-shade2_dismiss_10"></span>**`shade2_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade exhales a thin whisper that becomes a howling wind. The cavern blurs, tearing free from your senses. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 12 { #v-shade3 }

**Where:** [Undertell 3 12](../maps/undertell_3_12.md#pin-npc-shade3)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-3) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade3_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade3-shade3_selector"></span>**`shade3_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_3](#d-shade3-shade_return_wearing_ring_3)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade3_initial](#d-shade3-shade3_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade3_initial](#d-shade3-shade3_initial)

    <span id="d-shade3-shade_return_wearing_ring_3"></span>**`shade_return_wearing_ring_3`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 3

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade3-shade3_initial"></span>**`shade3_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade3_dismiss_10](#d-shade3-shade3_dismiss_10)

    <span id="d-shade3-shade3_dismiss_10"></span>**`shade3_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade digs its fingers into thin air, pulling a seam in reality itself. The world folds and casts you aside. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 12 (2) { #v-shade4 }

**Where:** [Undertell 3 12](../maps/undertell_3_12.md#pin-npc-shade4)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-4) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade4_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade4-shade4_selector"></span>**`shade4_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 230 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_4](#d-shade4-shade_return_wearing_ring_4)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade4_initial](#d-shade4-shade4_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade4_initial](#d-shade4-shade4_initial)

    <span id="d-shade4-shade_return_wearing_ring_4"></span>**`shade_return_wearing_ring_4`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 4

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade4-shade4_initial"></span>**`shade4_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade4_dismiss_10](#d-shade4-shade4_dismiss_10)

    <span id="d-shade4-shade4_dismiss_10"></span>**`shade4_dismiss_10`** [Dummy NPC](../monsters/none.md): “A pulse of violet light bursts from the shade's chest. Your vision fractures into shards, then reassembles elsewhere. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 13 { #v-shade5 }

**Where:** [Undertell 3 13](../maps/undertell_3_13.md#pin-npc-shade5)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-5) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade5_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade5-shade5_selector"></span>**`shade5_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 260 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_5](#d-shade5-shade_return_wearing_ring_5)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade5_initial](#d-shade5-shade5_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade5_initial](#d-shade5-shade5_initial)

    <span id="d-shade5-shade_return_wearing_ring_5"></span>**`shade_return_wearing_ring_5`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 5

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade5-shade5_initial"></span>**`shade5_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade5_dismiss_10](#d-shade5-shade5_dismiss_10)

    <span id="d-shade5-shade5_dismiss_10"></span>**`shade5_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade snaps its head toward you. A ring of symbols ignites beneath your feet, swallowing you whole. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 11 { #v-shade6 }

**Where:** [Undertell 3 11](../maps/undertell_3_11.md#pin-npc-shade6)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-6) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade6_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade6-shade6_selector"></span>**`shade6_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 290 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_6](#d-shade6-shade_return_wearing_ring_6)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade6_initial](#d-shade6-shade6_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade6_initial](#d-shade6-shade6_initial)

    <span id="d-shade6-shade_return_wearing_ring_6"></span>**`shade_return_wearing_ring_6`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 6

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade6-shade6_initial"></span>**`shade6_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade6_dismiss_10](#d-shade6-shade6_dismiss_10)

    <span id="d-shade6-shade6_dismiss_10"></span>**`shade6_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade whispers a single forgotten word. The cavern lurches, twisting like a dream unspooling. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 00 { #v-shade7 }

**Where:** [Undertell 3 00](../maps/undertell_3_00.md#pin-npc-shade7)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-7) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade7_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade7-shade7_selector"></span>**`shade7_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 320 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_7](#d-shade7-shade_return_wearing_ring_7)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade7_initial](#d-shade7-shade7_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade7_initial](#d-shade7-shade7_initial)

    <span id="d-shade7-shade_return_wearing_ring_7"></span>**`shade_return_wearing_ring_7`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 7

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade7-shade7_initial"></span>**`shade7_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade7_dismiss_10](#d-shade7-shade7_dismiss_10)

    <span id="d-shade7-shade7_dismiss_10"></span>**`shade7_dismiss_10`** [Dummy NPC](../monsters/none.md): “Frost forms midair around the shade. A shattering crack erupts, and you vanish with the falling ice. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 00 (2) { #v-shade8 }

**Where:** [Undertell 3 00](../maps/undertell_3_00.md#pin-npc-shade8)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-8) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade8_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade8-shade8_selector"></span>**`shade8_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 350 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_8](#d-shade8-shade_return_wearing_ring_8)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade8_initial](#d-shade8-shade8_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade8_initial](#d-shade8-shade8_initial)

    <span id="d-shade8-shade_return_wearing_ring_8"></span>**`shade_return_wearing_ring_8`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 8

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade8-shade8_initial"></span>**`shade8_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade8_dismiss_10](#d-shade8-shade8_dismiss_10)

    <span id="d-shade8-shade8_dismiss_10"></span>**`shade8_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade rises taller, its shadow stretching unnaturally. The darkness swallows you and spits you back out above ground. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 00 (3) { #v-shade9 }

**Where:** [Undertell 3 00](../maps/undertell_3_00.md#pin-npc-shade9)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-9) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade9_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade9-shade9_selector"></span>**`shade9_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 380 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_9](#d-shade9-shade_return_wearing_ring_9)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade9_initial](#d-shade9-shade9_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade9_initial](#d-shade9-shade9_initial)

    <span id="d-shade9-shade_return_wearing_ring_9"></span>**`shade_return_wearing_ring_9`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 9

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade9-shade9_initial"></span>**`shade9_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade9_dismiss_10](#d-shade9-shade9_dismiss_10)

    <span id="d-shade9-shade9_dismiss_10"></span>**`shade9_dismiss_10`** [Dummy NPC](../monsters/none.md): “A gust of heated air erupts from the shade, bending the cavern like molten glass. In an instant, you are elsewhere. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 10 { #v-shade10 }

**Where:** [Undertell 3 10](../maps/undertell_3_10.md#pin-npc-shade10)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-10) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade10_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade10-shade10_selector"></span>**`shade10_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 410 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_10](#d-shade10-shade_return_wearing_ring_10)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade10_initial](#d-shade10-shade10_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade10_initial](#d-shade10-shade10_initial)

    <span id="d-shade10-shade_return_wearing_ring_10"></span>**`shade_return_wearing_ring_10`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 10

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade10-shade10_initial"></span>**`shade10_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade10_dismiss_10](#d-shade10-shade10_dismiss_10)

    <span id="d-shade10-shade10_dismiss_10"></span>**`shade10_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade presses its palms together. A ringing sound spreads outward like a bell, and the world slips out from under you. The next thing you know...”

    - branch 1 → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 03 { #v-shade11 }

**Where:** [Undertell 3 03](../maps/undertell_3_03.md#pin-npc-shade11)

!!! warning "You can fight Forsaken shade"
    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-410) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-380) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-350) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-320) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-290) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-260) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-230) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-200) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-170) starts a fight with Forsaken shade.

    Answering “We will see!” during [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-140) starts a fight with Forsaken shade.

    Answering “I don't think so!” starts a fight with Forsaken shade.

### Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,221 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 6, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests that count defeats

- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-11) with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.

### Quests

- [Devotion](../quests/devotion.md): stages 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420
- [Devotion story flags (hidden flag)](../quests/hidden_devotion.md): stages 20, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440

### Dialogue simulator

Set your quest stages and items, then talk to Forsaken shade. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/shade11_selector.json" data-npc="Forsaken shade" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shade11-shade11_selector"></span>**`shade11_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 440 of [Devotion story flags (hidden flag)](../quests/hidden_devotion.md#stage-440))* → [shade_fight](#d-shade1-shade_fight) (listed above)
    - branch 2 *(if reached stage 110 of [Devotion](../quests/devotion.md#stage-110); wearing [Elythara's ring](../items/elythara_ring.md))* → [shade_return_wearing_ring_11](#d-shade11-shade_return_wearing_ring_11)
    - branch 3 *(if NOT reached stage 40 of [Devotion](../quests/devotion.md#stage-40))* → [shade11_initial](#d-shade11-shade11_initial)
    - branch 4 *(if reached stage 40 of [Devotion](../quests/devotion.md#stage-40); NOT reached stage 60 of [Devotion](../quests/devotion.md#stage-60))* → [shade_retry2](#d-shade1-shade_retry2) (listed above)
    - branch 5 *(if reached stage 60 of [Devotion](../quests/devotion.md#stage-60); NOT reached stage 80 of [Devotion](../quests/devotion.md#stage-80))* → [shade_retry3](#d-shade1-shade_retry3) (listed above)
    - branch 6 → [shade11_initial](#d-shade11-shade11_initial)

    <span id="d-shade11-shade_return_wearing_ring_11"></span>**`shade_return_wearing_ring_11`** Forsaken shade: “You have returned to us.” — **effects:** faction “currentShade” set to 11

    - Next → [shade_dialog_template](#d-shade1-shade_dialog_template) (listed above)

    <span id="d-shade11-shade11_initial"></span>**`shade11_initial`** Forsaken shade: “Go away!”

    - “But I want to...” → [shade11_dismiss_10](#d-shade11-shade11_dismiss_10)

    <span id="d-shade11-shade11_dismiss_10"></span>**`shade11_dismiss_10`** [Dummy NPC](../monsters/none.md): “The shade curls into a spiral of mist. The spiral snaps outward, hurling your consciousness into a different part of Undertell entirely. The next thing you know...”

    - Next → [undertell_shade_teleport_loc_selector](#d-shade1-undertell_shade_teleport_loc_selector) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**11 entries.** The game data defines 11 separate characters named Forsaken shade. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics.

| Entry | Type | Section |
|---|---|---|
| `shade1` | NPC/Enemy | [Undertell 3 02](#v-shade1) |
| `shade2` | NPC/Enemy | [Undertell 3 02](#v-shade2) |
| `shade3` | NPC/Enemy | [Undertell 3 12](#v-shade3) |
| `shade4` | NPC/Enemy | [Undertell 3 12](#v-shade4) |
| `shade5` | NPC/Enemy | [Undertell 3 13](#v-shade5) |
| `shade6` | NPC/Enemy | [Undertell 3 11](#v-shade6) |
| `shade7` | NPC/Enemy | [Undertell 3 00](#v-shade7) |
| `shade8` | NPC/Enemy | [Undertell 3 00](#v-shade8) |
| `shade9` | NPC/Enemy | [Undertell 3 00](#v-shade9) |
| `shade10` | NPC/Enemy | [Undertell 3 10](#v-shade10) |
| `shade11` | NPC/Enemy | [Undertell 3 03](#v-shade11) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: shade1"

    | | |
    |---|---|
    | Entry ID | `shade1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade1` |
    | Loot table | – |
    | Conversation | `shade1_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade1",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 6,
      "max": 8
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade1_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade2"

    | | |
    |---|---|
    | Entry ID | `shade2` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade2` |
    | Loot table | – |
    | Conversation | `shade2_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade2",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade2_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade3"

    | | |
    |---|---|
    | Entry ID | `shade3` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade3` |
    | Loot table | – |
    | Conversation | `shade3_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade3",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade3_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade4"

    | | |
    |---|---|
    | Entry ID | `shade4` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade4` |
    | Loot table | – |
    | Conversation | `shade4_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade4",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade4_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade5"

    | | |
    |---|---|
    | Entry ID | `shade5` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade5` |
    | Loot table | – |
    | Conversation | `shade5_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade5",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade5_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade6"

    | | |
    |---|---|
    | Entry ID | `shade6` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade6` |
    | Loot table | – |
    | Conversation | `shade6_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade6",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade6_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade7"

    | | |
    |---|---|
    | Entry ID | `shade7` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade7` |
    | Loot table | – |
    | Conversation | `shade7_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade7",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade7_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade8"

    | | |
    |---|---|
    | Entry ID | `shade8` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade8` |
    | Loot table | – |
    | Conversation | `shade8_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade8",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade8_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade9"

    | | |
    |---|---|
    | Entry ID | `shade9` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade9` |
    | Loot table | – |
    | Conversation | `shade9_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade9",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade9_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade10"

    | | |
    |---|---|
    | Entry ID | `shade10` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade10` |
    | Loot table | – |
    | Conversation | `shade10_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade10",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade10_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```

??? info "Technical information: shade11"

    | | |
    |---|---|
    | Entry ID | `shade11` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shade11` |
    | Loot table | – |
    | Conversation | `shade11_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shade11",
     "name": "Forsaken shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "horizontalFlipChance": 50,
     "phraseID": "shade11_selector",
     "attackCost": 5,
     "attackChance": 230,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "vulnerability",
        "magnitude": 6,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shade1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
