---
description: "Guynmart guard is an NPC you can also fight in Andor's Trail, found in Guynmart Castle. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_0.png){ .sprite } Guynmart guard

**Where to find Guynmart guard:** [Guynmart Castle, Guynmart](#v-guynmart_gguard), [Guynmart Castle, Guynmart gate 2](#v-guynmart_gateguard), [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_arms), [Guynmart Castle, Guynmart](#v-guynmart_guard_guide), [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_store), [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_storea), [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_storea2), [Guynmart Castle, Guynmart main 2](#v-guynmart_mguard), [Guynmart Castle, Guynmart](#v-guynmart_player), [Guynmart Castle, Guynmart main 1](#v-guynmart_tguard), [Guynmart Castle, Guynmart main 1](#v-guynmart_tguard2), [Guynmart Castle, Guynmart and 1 more](#v-guynmart_wguard), [Guynmart Castle, Guynmart](#v-guynmart_wguard1), [Guynmart Castle, Guynmart and 1 more](#v-guynmart_wguard9a)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Guynmart Castle |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when defeated** | 269 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Guynmart Castle, Guynmart { #v-guynmart_gguard }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_gguard) · **Role:** Shopkeeper

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 12 |

### Quests

- [Roses](../quests/guynmart.md): stages 30, 32
- [Guynmart garden guard (hidden flag)](../quests/guynmart_quest_gguard.md): stages 1, 82

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_gguard_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (43 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_gguard-guynmart_gguard_10"></span>**`guynmart_gguard_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [Guynmart garden guard (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1))* → [guynmart_gguard_919](#d-guynmart_gguard-guynmart_gguard_919)
    - branch 2 *(if reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 2 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-2))* → [guynmart_gguard_400](#d-guynmart_gguard-guynmart_gguard_400)
    - branch 3 *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_gguard_220](#d-guynmart_gguard-guynmart_gguard_220)
    - branch 4 → [guynmart_gguard_20](#d-guynmart_gguard-guynmart_gguard_20)

    <span id="d-guynmart_gguard-guynmart_gguard_919"></span>**`guynmart_gguard_919`** Guynmart guard: “...nine...”

    - Next → [guynmart_gguard_919](#d-guynmart_gguard-guynmart_gguard_919)

    <span id="d-guynmart_gguard-guynmart_gguard_400"></span>**`guynmart_gguard_400`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Tell me, did many people pass by today?” → [guynmart_gguard_410](#d-guynmart_gguard-guynmart_gguard_410)

    <span id="d-guynmart_gguard-guynmart_gguard_220"></span>**`guynmart_gguard_220`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Here are 100 gold.” → [guynmart_gguard_248](#d-guynmart_gguard-guynmart_gguard_248)
    - “Do you not know me anymore? I've already given you enough gold.” → [guynmart_gguard_242](#d-guynmart_gguard-guynmart_gguard_242)
    - “I would like to pass through again.” → [guynmart_gguard_250](#d-guynmart_gguard-guynmart_gguard_250)
    - “May I pick a rose?” *(if NOT carry 1× [Rose](../items/guynmart_rose.md); NOT reached stage 100 of [Roses](../quests/guynmart.md#stage-100))* → [guynmart_gguard_350](#d-guynmart_gguard-guynmart_gguard_350)

    <span id="d-guynmart_gguard-guynmart_gguard_20"></span>**`guynmart_gguard_20`** Guynmart guard: “No trespassing! Especially for kids!”

    - “Here is 100 gold.” *(if reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “Who are you?” → [guynmart_gguard_30](#d-guynmart_gguard-guynmart_gguard_30)
    - “What are you doing here?” → [guynmart_gguard_40](#d-guynmart_gguard-guynmart_gguard_40)
    - “I just want to pass through.” → [guynmart_gguard_22](#d-guynmart_gguard-guynmart_gguard_22)
    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard-guynmart_gguard_50)

    <span id="d-guynmart_gguard-guynmart_gguard_410"></span>**`guynmart_gguard_410`** Guynmart guard: “Now that you mention it - not a single one. Bad business today.”

    - “No wonder with the main gate open.” → [guynmart_gguard_420](#d-guynmart_gguard-guynmart_gguard_420)

    <span id="d-guynmart_gguard-guynmart_gguard_248"></span>**`guynmart_gguard_248`** Guynmart guard: “Well, everything is getting more expensive nowadays. So 200 pieces of gold, please.”

    - “Here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “Forget it. This is outrageous.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_242"></span>**`guynmart_gguard_242`** Guynmart guard: “Gold can never be enough. So it is 200 pieces of gold now.”

    - Next → [guynmart_gguard_244](#d-guynmart_gguard-guynmart_gguard_244)

    <span id="d-guynmart_gguard-guynmart_gguard_250"></span>**`guynmart_gguard_250`** Guynmart guard: “I am not allowed to let anyone in or out. And I am incorruptable below 200 pieces of gold.”

    - “Here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “Well, I will really look for another entrance now.” → *conversation ends*
    - “200 gold? Last time it was 100 gold.” → [guynmart_gguard_248](#d-guynmart_gguard-guynmart_gguard_248)
    - “Sorry, I don't have that much gold with me.” → [guynmart_gguard_930](#d-guynmart_gguard-guynmart_gguard_930)

    <span id="d-guynmart_gguard-guynmart_gguard_350"></span>**`guynmart_gguard_350`** Guynmart guard: “Pick? A rose? You? No way! All flowers in this garden are the personal property of Lady Hannah.”

    - “Come on. With so many plants she will not miss a single flower.” → [guynmart_gguard_70](#d-guynmart_gguard-guynmart_gguard_70)
    - “But Lady Hannah herself told me to get her one.” *(if NOT reached stage 132 of [Roses](../quests/guynmart.md#stage-132))* → [guynmart_gguard_360](#d-guynmart_gguard-guynmart_gguard_360)

    <span id="d-guynmart_gguard-guynmart_gguard_900"></span>**`guynmart_gguard_900`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [Guynmart garden guard (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1), sets stage 30 of [Roses](../quests/guynmart.md#stage-30)

    - branch 1 *(if NOT reached stage 10 of [Roses](../quests/guynmart.md#stage-10); NOT reached stage 32 of [Roses](../quests/guynmart.md#stage-32))* → [guynmart_gguard_902](#d-guynmart_gguard-guynmart_gguard_902)
    - branch 2 → [guynmart_gguard_910](#d-guynmart_gguard-guynmart_gguard_910)

    <span id="d-guynmart_gguard-guynmart_gguard_30"></span>**`guynmart_gguard_30`** Guynmart guard: “Mind your own business. I hate kids. Just disappear!”

    - “Wait!” → [guynmart_gguard_20](#d-guynmart_gguard-guynmart_gguard_20)
    - “OK, I'll leave.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_40"></span>**`guynmart_gguard_40`** Guynmart guard: “I am standing around kicking my heels and answering stupid questions.”

    - “Here is 100 gold.” *(if reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “Who are you?” → [guynmart_gguard_30](#d-guynmart_gguard-guynmart_gguard_30)
    - “What are you doing here?” → [guynmart_gguard_40](#d-guynmart_gguard-guynmart_gguard_40)
    - “I want to pass through.” → [guynmart_gguard_22](#d-guynmart_gguard-guynmart_gguard_22)
    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard-guynmart_gguard_50)

    <span id="d-guynmart_gguard-guynmart_gguard_22"></span>**`guynmart_gguard_22`** Guynmart guard: “I am not allowed to let anyone in or out. And I am incorruptable below 100 pieces of gold.”

    - “Here is 100 gold.” *(if pay 100 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “Well, I think I'll look for another entrance.” → *conversation ends*
    - “Sorry, I don't have that much gold with me.” → [guynmart_gguard_930](#d-guynmart_gguard-guynmart_gguard_930)

    <span id="d-guynmart_gguard-guynmart_gguard_50"></span>**`guynmart_gguard_50`** Guynmart guard: “Pick? A rose? You? No way! All flowers in this garden are the personal property of Lady Hannah.”

    - “Who is Lady Hannah?” → [guynmart_gguard_60](#d-guynmart_gguard-guynmart_gguard_60)
    - “Come on. With so many plants she will not miss a single flower.” → [guynmart_gguard_70](#d-guynmart_gguard-guynmart_gguard_70)

    <span id="d-guynmart_gguard-guynmart_gguard_420"></span>**`guynmart_gguard_420`** Guynmart guard: “Ah, that is why. OK. I am not allowed to let anyone in or out. And I am incorruptable below 2 pieces of gold.”

    - “Here is 2 gold.” *(if pay 2 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “You never give up, do you?” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_244"></span>**`guynmart_gguard_244`** Guynmart guard: “So do you want to go through or not?”

    - “Outrageous! But OK, here is 200 gold.” *(if pay 200 gold)* → [guynmart_gguard_900](#d-guynmart_gguard-guynmart_gguard_900)
    - “I have to think about it.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_930"></span>**`guynmart_gguard_930`** Guynmart guard: “Hmm, you may have not enough money, but you have some nice things with you. I might give you a good price.”

    - “We'll see. Let's have a look at my belongings.” → *shop opens*
    - “I would rather starve here on the spot than sell you a single thing.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_70"></span>**`guynmart_gguard_70`** Guynmart guard: “Hannah knows every single plant in her garden. Nobody but herself and old Nuik may touch the plants.”

    - “Who is Nuik again?” → [guynmart_gguard_80](#d-guynmart_gguard-guynmart_gguard_80)

    <span id="d-guynmart_gguard-guynmart_gguard_360"></span>**`guynmart_gguard_360`** Guynmart guard: “Anyone could say that. But maybe...”

    - “Yes?” → [guynmart_gguard_362](#d-guynmart_gguard-guynmart_gguard_362)

    <span id="d-guynmart_gguard-guynmart_gguard_902"></span>**`guynmart_gguard_902`** Guynmart guard: “[Gold taken] Very good. Before you enter maybe you should also know the family names: Lord Guynmart, his beautiful but complicated daughter Hannah and his annoying son Rob. Got it?” — **effects:** sets stage 32 of [Roses](../quests/guynmart.md#stage-32)

    - Next → [guynmart_gguard_904](#d-guynmart_gguard-guynmart_gguard_904)

    <span id="d-guynmart_gguard-guynmart_gguard_910"></span>**`guynmart_gguard_910`** Guynmart guard: “[Gold taken] Very good. I will close my eyes now and count to 10.”

    - Next → [guynmart_gguard_911](#d-guynmart_gguard-guynmart_gguard_911)

    <span id="d-guynmart_gguard-guynmart_gguard_60"></span>**`guynmart_gguard_60`** Guynmart guard: “Hannah is Guynmart's daughter.”

    - “May I pick a rose?” → [guynmart_gguard_50](#d-guynmart_gguard-guynmart_gguard_50)
    - “And Guynmart is...?” → [guynmart_gguard_90](#d-guynmart_gguard-guynmart_gguard_90)
    - “Guynmart has a daughter?” → [guynmart_gguard_100](#d-guynmart_gguard-guynmart_gguard_100)

    <span id="d-guynmart_gguard-guynmart_gguard_80"></span>**`guynmart_gguard_80`** Guynmart guard: “Nuik has been a gardener here for as long as I can remember. And now disappear!”

    - “I have another question.” → [guynmart_gguard_10](#d-guynmart_gguard-guynmart_gguard_10)
    - “OK, OK, I'll leave.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_362"></span>**`guynmart_gguard_362`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 100 gold)* → [guynmart_gguard_370](#d-guynmart_gguard-guynmart_gguard_370)
    - branch 2 → [guynmart_gguard_364](#d-guynmart_gguard-guynmart_gguard_364)

    <span id="d-guynmart_gguard-guynmart_gguard_904"></span>**`guynmart_gguard_904`** Guynmart guard: “Rob is always playing some stupid game, and Hannah is always having problems. See?”

    - “Ah.” → [guynmart_gguard_906](#d-guynmart_gguard-guynmart_gguard_906)

    <span id="d-guynmart_gguard-guynmart_gguard_911"></span>**`guynmart_gguard_911`** Guynmart guard: “...one...”

    - Next → [guynmart_gguard_912](#d-guynmart_gguard-guynmart_gguard_912)

    <span id="d-guynmart_gguard-guynmart_gguard_90"></span>**`guynmart_gguard_90`** Guynmart guard: “Don't you know anything? Guynmart has been Lord of Guynmart castle for as long as I remember. His wife died early, during the birth of their daughter.”

    - “Guynmart has a daughter?” → [guynmart_gguard_100](#d-guynmart_gguard-guynmart_gguard_100)

    <span id="d-guynmart_gguard-guynmart_gguard_100"></span>**`guynmart_gguard_100`** Guynmart guard: “Hannah's beauty is well known all over the country. Many young men asked to marry her. But she only has eyes for Lovis.”

    - “Ah.” → [guynmart_gguard_110](#d-guynmart_gguard-guynmart_gguard_110)
    - “And who is Lovis?” → [guynmart_gguard_110](#d-guynmart_gguard-guynmart_gguard_110)
    - “This is getting boring.” → [guynmart_gguard_110](#d-guynmart_gguard-guynmart_gguard_110)

    <span id="d-guynmart_gguard-guynmart_gguard_370"></span>**`guynmart_gguard_370`** Guynmart guard: “for 100 gold...”

    - “I understand. Here, 100 gold.” *(if pay 100 gold)* → [guynmart_gguard_380](#d-guynmart_gguard-guynmart_gguard_380)
    - “Oh you greedy, filthy, ...” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_364"></span>**`guynmart_gguard_364`** Guynmart guard: “Nothing. You don't seem to have enough money. Forget it.”

    - “Oh.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_906"></span>**`guynmart_gguard_906`** Guynmart guard: “Enough talk. No trespassing! I will close my eyes now and count to 10.”

    - Next → [guynmart_gguard_911](#d-guynmart_gguard-guynmart_gguard_911)

    <span id="d-guynmart_gguard-guynmart_gguard_912"></span>**`guynmart_gguard_912`** Guynmart guard: “...two...”

    - Next → [guynmart_gguard_913](#d-guynmart_gguard-guynmart_gguard_913)

    <span id="d-guynmart_gguard-guynmart_gguard_110"></span>**`guynmart_gguard_110`** Guynmart guard: “Lovis is a good boy. I have not seen him for a while.”

    - “Whatever.” → [guynmart_gguard_120](#d-guynmart_gguard-guynmart_gguard_120)
    - “La la la ... I'm not listening anymore...” → [guynmart_gguard_120](#d-guynmart_gguard-guynmart_gguard_120)

    <span id="d-guynmart_gguard-guynmart_gguard_380"></span>**`guynmart_gguard_380`** Guynmart guard: “And here is the rose. Don't tell anybody that you got it from me.” — **effects:** gives [Rose](../items/guynmart_rose.md), sets stage 82 of [Guynmart garden guard (hidden flag)](../quests/guynmart_quest_gguard.md#stage-82)

    - “OK.” → *conversation ends*
    - “Hmm, we will see.” → *conversation ends*

    <span id="d-guynmart_gguard-guynmart_gguard_913"></span>**`guynmart_gguard_913`** Guynmart guard: “...three...”

    - Next → [guynmart_gguard_914](#d-guynmart_gguard-guynmart_gguard_914)

    <span id="d-guynmart_gguard-guynmart_gguard_120"></span>**`guynmart_gguard_120`** Guynmart guard: “But when Lovis is back, I am sure he will marry Hannah immediately.”

    - “This is all very interesting. Are you letting me through now?” → [guynmart_gguard_130](#d-guynmart_gguard-guynmart_gguard_130)

    <span id="d-guynmart_gguard-guynmart_gguard_914"></span>**`guynmart_gguard_914`** Guynmart guard: “...four...”

    - Next → [guynmart_gguard_915](#d-guynmart_gguard-guynmart_gguard_915)

    <span id="d-guynmart_gguard-guynmart_gguard_130"></span>**`guynmart_gguard_130`** Guynmart guard: “What? No, of course not!”

    - Next → [guynmart_gguard_10](#d-guynmart_gguard-guynmart_gguard_10)

    <span id="d-guynmart_gguard-guynmart_gguard_915"></span>**`guynmart_gguard_915`** Guynmart guard: “...five...”

    - Next → [guynmart_gguard_916](#d-guynmart_gguard-guynmart_gguard_916)

    <span id="d-guynmart_gguard-guynmart_gguard_916"></span>**`guynmart_gguard_916`** Guynmart guard: “...six...”

    - Next → [guynmart_gguard_917](#d-guynmart_gguard-guynmart_gguard_917)

    <span id="d-guynmart_gguard-guynmart_gguard_917"></span>**`guynmart_gguard_917`** Guynmart guard: “...eh, now seven, I think...”

    - Next → [guynmart_gguard_918](#d-guynmart_gguard-guynmart_gguard_918)

    <span id="d-guynmart_gguard-guynmart_gguard_918"></span>**`guynmart_gguard_918`** Guynmart guard: “...eight...”

    - Next → [guynmart_gguard_919](#d-guynmart_gguard-guynmart_gguard_919)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 43 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart gate 2 { #v-guynmart_gateguard }

**Where:** Guynmart Castle: [Guynmart gate 2](../maps/guynmart_gate_2.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 269 |
| Damage | 5 to 20 |
| AC | 40 |
| BC | 150 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 12 to 36 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart gate 2](../maps/guynmart_gate_2.md) | Guynmart Castle | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 { #v-guynmart_guard_arms }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_guard_arms)

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_arms_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_guard_arms-guynmart_guard_arms_10"></span>**`guynmart_guard_arms_10`** Guynmart guard: “You are too young to be here. Sharp swords are stored in this room.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart (2) { #v-guynmart_guard_guide }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_guard_guide)

### Quests

- [Roses](../quests/guynmart.md): stages 16, 18

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_guide_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_guard_guide-guynmart_guard_guide_10"></span>**`guynmart_guard_guide_10`** Guynmart guard: “Hi, kid. Wanna visit Guynmart Castle? Ancient walls, and sometimes a ghost at midnight?”

    - “No, thank you.” → *conversation ends*
    - “Might be interesting. And an easy way to get in...” → [guynmart_guard_guide_20](#d-guynmart_guard_guide-guynmart_guard_guide_20)

    <span id="d-guynmart_guard_guide-guynmart_guard_guide_20"></span>**`guynmart_guard_guide_20`** Guynmart guard: “Great choice, you won't regret it. Adults 20 gold, kids 12 gold. Bilingual guide would be 3 gold extra.”

    - “OK, one kid, without guide, please.” *(if pay 12 gold)* → [guynmart_guard_guide_30](#d-guynmart_guard_guide-guynmart_guard_guide_30)
    - “One kid and a guide, please.” *(if pay 15 gold)* → [guynmart_guard_guide_32](#d-guynmart_guard_guide-guynmart_guard_guide_32)
    - “I changed my mind. Bye.” → *conversation ends*

    <span id="d-guynmart_guard_guide-guynmart_guard_guide_30"></span>**`guynmart_guard_guide_30`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 16 of [Roses](../quests/guynmart.md#stage-16), removes monsters from guynmart

    - branch 1 → [guynmart_guard_guide_40](#d-guynmart_guard_guide-guynmart_guard_guide_40)

    <span id="d-guynmart_guard_guide-guynmart_guard_guide_32"></span>**`guynmart_guard_guide_32`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 18 of [Roses](../quests/guynmart.md#stage-18), removes monsters from guynmart

    - branch 1 → [guynmart_guard_guide_40](#d-guynmart_guard_guide-guynmart_guard_guide_40)

    <span id="d-guynmart_guard_guide-guynmart_guard_guide_40"></span>**`guynmart_guard_guide_40`** Guynmart guard: “[Gold taken] HAHAHA! Once again some stupid person with more money than brains! HAHAHA!”

    - “Hey!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 (2) { #v-guynmart_guard_store }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_guard_store)

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_guard_store-guynmart_guard_10"></span>**`guynmart_guard_10`** Guynmart guard: “Go away, kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 (3) { #v-guynmart_guard_storea }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 269 |
| Damage | 5 to 20 |
| AC | 40 |
| BC | 150 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 12 to 36 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart main 1](../maps/guynmart_main_1.md) | Guynmart Castle | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 (4) { #v-guynmart_guard_storea2 }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 269 |
| Damage | 5 to 20 |
| AC | 40 |
| BC | 150 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 12 to 36 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart main 1](../maps/guynmart_main_1.md) | Guynmart Castle | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 2 { #v-guynmart_mguard }

**Where:** Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_mguard)

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_guard_10](#d-guynmart_guard_store-guynmart_guard_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart (3) { #v-guynmart_player }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_player)

### Quests

- [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md): stages 1, 2
- [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md): stages 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_player_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (28 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_player-guynmart_player_10"></span>**`guynmart_player_10`** Guynmart guard: “Hi kid! Would you like to play a card game?”

    - “Sure!” → [guynmart_player_20](#d-guynmart_player-guynmart_player_20)
    - “No, not today!” → *conversation ends*
    - “No thanks. My father warned me that certain card games can become a bad habit.” → *conversation ends*

    <span id="d-guynmart_player-guynmart_player_20"></span>**`guynmart_player_20`** Guynmart guard: “We always play card color guessing. Do you have any money?”

    - “Of course I have.” *(if have 100 gold)* → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)
    - “I would never play for money.” → *conversation ends*
    - “Please explain the rules to me.” → [guynmart_player_30](#d-guynmart_player-guynmart_player_30)

    <span id="d-guynmart_player-guynmart_player_80"></span>**`guynmart_player_80`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 100 gold)* → [guynmart_player_80_2](#d-guynmart_player-guynmart_player_80_2)
    - branch 2 → [guynmart_player_80_1](#d-guynmart_player-guynmart_player_80_1)

    <span id="d-guynmart_player-guynmart_player_30"></span>**`guynmart_player_30`** Guynmart guard: “I will draw a card, and you have to guess whether it is Red or Black.”

    - Next → [guynmart_player_32](#d-guynmart_player-guynmart_player_32)

    <span id="d-guynmart_player-guynmart_player_80_2"></span>**`guynmart_player_80_2`** Guynmart guard: “OK. I have drawn a card. Which color is it?”

    - “Red” → [guynmart_player_84](#d-guynmart_player-guynmart_player_84)
    - “Black” → [guynmart_player_86](#d-guynmart_player-guynmart_player_86)
    - “Blue” *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); reached stage 3 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-3))* → [guynmart_player_82](#d-guynmart_player-guynmart_player_82)
    - “Blue” *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); reached stage 7 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-7))* → [guynmart_player_82](#d-guynmart_player-guynmart_player_82)

    <span id="d-guynmart_player-guynmart_player_80_1"></span>**`guynmart_player_80_1`** Guynmart guard: “Hey, you look like you have no money left.”

    - “Yes indeed, I'm broke. Sorry, then I have to leave.” → *conversation ends*

    <span id="d-guynmart_player-guynmart_player_32"></span>**`guynmart_player_32`** Guynmart guard: “If you get it right, I will give you gold 100 coins. If your guess is wrong, you owe me 100.”

    - “OK, got it.” → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)
    - “Eh, could you explain once more?” → [guynmart_player_30](#d-guynmart_player-guynmart_player_30)

    <span id="d-guynmart_player-guynmart_player_84"></span>**`guynmart_player_84`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1), clears stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2)

    - branch 1 → [guynmart_player_90](#d-guynmart_player-guynmart_player_90)

    <span id="d-guynmart_player-guynmart_player_86"></span>**`guynmart_player_86`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2), clears stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1)

    - branch 1 → [guynmart_player_90](#d-guynmart_player-guynmart_player_90)

    <span id="d-guynmart_player-guynmart_player_82"></span>**`guynmart_player_82`** Guynmart guard: “Oh dear. Just Red or Black. Please try to remember. *Sigh*”

    - “Yes. Sorry.” → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)

    <span id="d-guynmart_player-guynmart_player_90"></span>**`guynmart_player_90`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 12 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-12))* → [guynmart_player_112](#d-guynmart_player-guynmart_player_112)
    - branch 2 *(if reached stage 11 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-11))* → [guynmart_player_111](#d-guynmart_player-guynmart_player_111)
    - branch 3 *(if reached stage 10 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-10))* → [guynmart_player_110](#d-guynmart_player-guynmart_player_110)
    - branch 4 *(if reached stage 9 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-9))* → [guynmart_player_109](#d-guynmart_player-guynmart_player_109)
    - branch 5 *(if reached stage 8 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-8))* → [guynmart_player_108](#d-guynmart_player-guynmart_player_108)
    - branch 6 *(if reached stage 7 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-7))* → [guynmart_player_107](#d-guynmart_player-guynmart_player_107)
    - branch 7 *(if reached stage 6 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-6))* → [guynmart_player_106](#d-guynmart_player-guynmart_player_106)
    - branch 8 *(if reached stage 5 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-5))* → [guynmart_player_105](#d-guynmart_player-guynmart_player_105)
    - branch 9 *(if reached stage 4 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-4))* → [guynmart_player_104](#d-guynmart_player-guynmart_player_104)
    - branch 10 *(if reached stage 3 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-3))* → [guynmart_player_103](#d-guynmart_player-guynmart_player_103)
    - branch 11 *(if reached stage 2 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-2))* → [guynmart_player_102](#d-guynmart_player-guynmart_player_102)
    - branch 12 *(if reached stage 1 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-1))* → [guynmart_player_101](#d-guynmart_player-guynmart_player_101)
    - branch 13 → [guynmart_player_100](#d-guynmart_player-guynmart_player_100)

    <span id="d-guynmart_player-guynmart_player_112"></span>**`guynmart_player_112`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 12 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-12), sets stage 1 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-1)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_111"></span>**`guynmart_player_111`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 11 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-11), sets stage 12 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-12)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_110"></span>**`guynmart_player_110`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 10 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-10), sets stage 11 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-11)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_109"></span>**`guynmart_player_109`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 9 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-9), sets stage 10 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-10)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_108"></span>**`guynmart_player_108`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 8 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-8), sets stage 9 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-9)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_107"></span>**`guynmart_player_107`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 7 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-7), sets stage 8 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-8)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_106"></span>**`guynmart_player_106`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 6 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-6), sets stage 7 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-7)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_105"></span>**`guynmart_player_105`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 5 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-5), sets stage 6 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-6)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_104"></span>**`guynmart_player_104`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 4 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-4), sets stage 5 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-5)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_103"></span>**`guynmart_player_103`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 3 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-3), sets stage 4 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-4)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_102"></span>**`guynmart_player_102`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 2 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-2), sets stage 3 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-3)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_101"></span>**`guynmart_player_101`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 1 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-1), sets stage 2 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-2)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay 100 gold)* → [guynmart_player_151](#d-guynmart_player-guynmart_player_151)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay 100 gold)* → [guynmart_player_152](#d-guynmart_player-guynmart_player_152)

    <span id="d-guynmart_player-guynmart_player_100"></span>**`guynmart_player_100`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [Guynmart Castle step 2 (hidden flag)](../quests/guynmart_q2.md#stage-1)

    - branch 1 *(if reached stage 1 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-1); pay -100 gold)* → [guynmart_player_161](#d-guynmart_player-guynmart_player_161)
    - branch 2 *(if reached stage 2 of [Guynmart Castle step 1 (hidden flag)](../quests/guynmart_q1.md#stage-2); pay -100 gold)* → [guynmart_player_162](#d-guynmart_player-guynmart_player_162)

    <span id="d-guynmart_player-guynmart_player_161"></span>**`guynmart_player_161`** Guynmart guard: “Red! How did you know? Here you get 100 again. [Gold received] Can you do this again?”

    - Next → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)

    <span id="d-guynmart_player-guynmart_player_162"></span>**`guynmart_player_162`** Guynmart guard: “Black! You guessed it right again. Here you get 100 gold. [Gold received] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)

    <span id="d-guynmart_player-guynmart_player_151"></span>**`guynmart_player_151`** Guynmart guard: “I have Black! Sorry for you, kid. I get 100 now. [Gold taken] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)

    <span id="d-guynmart_player-guynmart_player_152"></span>**`guynmart_player_152`** Guynmart guard: “I have Red! Sorry for you, kid. I get 100. [Gold taken] Let's try another card.”

    - Next → [guynmart_player_80](#d-guynmart_player-guynmart_player_80)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 28 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 (5) { #v-guynmart_tguard }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_tguard)

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_tguard_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_tguard-guynmart_tguard_10"></span>**`guynmart_tguard_10`** Guynmart guard: “No entry!”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 (6) { #v-guynmart_tguard2 }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_tguard2)

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_tguard2_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_tguard2-guynmart_tguard2_10"></span>**`guynmart_tguard2_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32))* → [guynmart_tguard2_30](#d-guynmart_tguard2-guynmart_tguard2_30)
    - branch 2 → [guynmart_tguard2_20](#d-guynmart_tguard2-guynmart_tguard2_20)

    <span id="d-guynmart_tguard2-guynmart_tguard2_30"></span>**`guynmart_tguard2_30`** Guynmart guard: “You made a good choice.”


    <span id="d-guynmart_tguard2-guynmart_tguard2_20"></span>**`guynmart_tguard2_20`** Guynmart guard: “Come in, and take your time! You may choose one of three things.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart and 1 more { #v-guynmart_wguard }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_wguard), Guynmart Castle: [Guynmart tower 2](../maps/guynmart_tower_2.md#pin-npc-guynmart_wguard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 3 | – |
| [Guynmart tower 2](../maps/guynmart_tower_2.md) | Guynmart Castle | 2 | – |

### Dialogue simulator

Talk to Guynmart guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_10.json" data-npc="Guynmart guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_guard_10](#d-guynmart_guard_store-guynmart_guard_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart (4) { #v-guynmart_wguard1 }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 269 |
| Damage | 5 to 20 |
| AC | 40 |
| BC | 150 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 12 to 36 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart and 1 more (2) { #v-guynmart_wguard9a }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md), Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 269 |
| Damage | 5 to 20 |
| AC | 40 |
| BC | 150 |
| DR | 6 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 12 to 36 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 5 | Appears later, during a quest |
| [Guynmart main 2](../maps/guynmart_main_2.md) | Guynmart Castle | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**14 entries.** The game data defines 14 separate characters named Guynmart guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock, movement.

| Entry | Type | Section |
|---|---|---|
| `guynmart_gguard` | NPC | [Guynmart Castle, Guynmart](#v-guynmart_gguard) |
| `guynmart_gateguard` | Enemy | [Guynmart Castle, Guynmart gate 2](#v-guynmart_gateguard) |
| `guynmart_guard_arms` | NPC | [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_arms) |
| `guynmart_guard_guide` | NPC | [Guynmart Castle, Guynmart](#v-guynmart_guard_guide) |
| `guynmart_guard_store` | NPC | [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_store) |
| `guynmart_guard_storea` | Enemy | [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_storea) |
| `guynmart_guard_storea2` | Enemy | [Guynmart Castle, Guynmart main 1](#v-guynmart_guard_storea2) |
| `guynmart_mguard` | NPC | [Guynmart Castle, Guynmart main 2](#v-guynmart_mguard) |
| `guynmart_player` | NPC | [Guynmart Castle, Guynmart](#v-guynmart_player) |
| `guynmart_tguard` | NPC | [Guynmart Castle, Guynmart main 1](#v-guynmart_tguard) |
| `guynmart_tguard2` | NPC | [Guynmart Castle, Guynmart main 1](#v-guynmart_tguard2) |
| `guynmart_wguard` | NPC | [Guynmart Castle, Guynmart and 1 more](#v-guynmart_wguard) |
| `guynmart_wguard1` | Enemy | [Guynmart Castle, Guynmart](#v-guynmart_wguard1) |
| `guynmart_wguard9a` | Enemy | [Guynmart Castle, Guynmart and 1 more](#v-guynmart_wguard9a) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: guynmart_gguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_gguard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_gguard` |
    | Loot table | `guynmart_drp_gguard` |
    | Conversation | `guynmart_gguard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_gguard",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_gguard_10",
     "droplistID": "guynmart_drp_gguard"
    }
    ```

??? info "Technical information: guynmart_gateguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_gateguard` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_gateguard` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_gateguard",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "droplistID": "guynmart_drp_guard",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```

??? info "Technical information: guynmart_guard_arms"

    | | |
    |---|---|
    | Entry ID | `guynmart_guard_arms` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_guard_arms` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_guard_arms_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_guard_arms",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_arms_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_guard_guide"

    | | |
    |---|---|
    | Entry ID | `guynmart_guard_guide` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_guard_guide` |
    | Loot table | – |
    | Conversation | `guynmart_guard_guide_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_guard_guide",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_guide_10"
    }
    ```

??? info "Technical information: guynmart_guard_store"

    | | |
    |---|---|
    | Entry ID | `guynmart_guard_store` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_guard_store` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_guard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_guard_store",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_guard_storea"

    | | |
    |---|---|
    | Entry ID | `guynmart_guard_storea` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_guard_storea` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_guard_storea",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "droplistID": "guynmart_drp_guard",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```

??? info "Technical information: guynmart_guard_storea2"

    | | |
    |---|---|
    | Entry ID | `guynmart_guard_storea2` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_guard_storea2` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_guard_storea2",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "droplistID": "guynmart_drp_guard",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```

??? info "Technical information: guynmart_mguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_mguard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_mguard` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_guard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_mguard",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_player"

    | | |
    |---|---|
    | Entry ID | `guynmart_player` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_player` |
    | Loot table | – |
    | Conversation | `guynmart_player_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_player",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_player_10"
    }
    ```

??? info "Technical information: guynmart_tguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_tguard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_tguard` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_tguard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_tguard",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_tguard_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_tguard2"

    | | |
    |---|---|
    | Entry ID | `guynmart_tguard2` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_tguard2` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_tguard2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_tguard2",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_tguard2_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_wguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_wguard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_wguard` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | `guynmart_guard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_wguard",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_10",
     "droplistID": "guynmart_drp_guard"
    }
    ```

??? info "Technical information: guynmart_wguard1"

    | | |
    |---|---|
    | Entry ID | `guynmart_wguard1` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_wguard_a` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_wguard1",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "spawnGroup": "guynmart_wguard_a",
     "droplistID": "guynmart_drp_guard",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```

??? info "Technical information: guynmart_wguard9a"

    | | |
    |---|---|
    | Entry ID | `guynmart_wguard9a` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_wguard9a` |
    | Loot table | `guynmart_drp_guard` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_wguard9a",
     "name": "Guynmart guard",
     "iconID": "monsters_ld1:0",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 5,
      "max": 20
     },
     "droplistID": "guynmart_drp_guard",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 6
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_gguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
