---
description: "Harlenn is an NPC who can also be fought in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_men2_6.png){ .sprite } Harlenn

**Where to find Harlenn:** Prim: [Blackwater mountain 45](../maps/blackwater_mountain45.md#pin-npc-harlenn)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 80 |
| **XP when defeated** | 146 |
| **Entry ID** | `harlenn` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 80 |
| XP when defeated | 146 |
| Damage | 4 to 9 |
| Attack chance | 70 |
| Block chance | 80 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Harlenn's ring](../items/harlenn_id.md) | 100% | 1 |
| [Ring of Shadow embrace](../items/ring_shadow_embrace.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 20 to 50 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 45](../maps/blackwater_mountain45.md) | Prim | 1 | – |

## Quests

- [Clouded intent](../quests/prim_hunt.md): stages 30, 90, 91, 250
- [The agent and the beast](../quests/bwm_agent.md): stages 65, 66, 70, 90, 95, 110, 120, 149, 150, 240, 250, 251

## Dialogue simulator

Set your quest stages and items, then talk to Harlenn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/harlenn_start.json" data-npc="Harlenn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (73 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-harlenn_start"></span>**`harlenn_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 91 of [Clouded intent](../quests/prim_hunt.md#stage-91))* → [harlenn_sentbyprim_8](#d-harlenn_sentbyprim_8)
    - branch 2 *(if reached stage 90 of [Clouded intent](../quests/prim_hunt.md#stage-90))* → [harlenn_sentbyprim_2](#d-harlenn_sentbyprim_2)
    - branch 3 *(if reached stage 80 of [Clouded intent](../quests/prim_hunt.md#stage-80))* → [harlenn_sentbyprim_1](#d-harlenn_sentbyprim_1)
    - branch 4 *(if reached stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251))* → [harlenn_return_1](#d-harlenn_return_1)
    - branch 5 *(if reached stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250))* → [harlenn_return_1](#d-harlenn_return_1)
    - branch 6 *(if reached stage 150 of [The agent and the beast](../quests/bwm_agent.md#stage-150))* → [harlenn_completed](#d-harlenn_completed)
    - branch 7 *(if reached stage 149 of [The agent and the beast](../quests/bwm_agent.md#stage-149))* → [harlenn_killguth_3](#d-harlenn_killguth_3)
    - branch 8 *(if reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50))* → [harlenn_workingforprim_1](#d-harlenn_workingforprim_1)
    - branch 9 *(if reached stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120))* → [harlenn_killguth_1](#d-harlenn_killguth_1)
    - branch 10 *(if reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95))* → [harlenn_lookforsigns_1](#d-harlenn_lookforsigns_1)
    - branch 11 *(if reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70))* → [harlenn_return_3](#d-harlenn_return_3)
    - branch 12 *(if reached stage 65 of [The agent and the beast](../quests/bwm_agent.md#stage-65))* → [harlenn_return_2](#d-harlenn_return_2)
    - branch 13 → [harlenn_1](#d-harlenn_1)

    <span id="d-harlenn_sentbyprim_8"></span>**`harlenn_sentbyprim_8`** Harlenn: “Thank you friend, for talking some sense into me.” — **effects:** sets stage 91 of [Clouded intent](../quests/prim_hunt.md#stage-91)

    - “You are welcome.” → *NPC leaves*

    <span id="d-harlenn_sentbyprim_2"></span>**`harlenn_sentbyprim_2`** Harlenn: “Stop me?! Ha ha. Very well, let's see who is the one being stopped here.” — **effects:** sets stage 90 of [Clouded intent](../quests/prim_hunt.md#stage-90), faction “fct_bwm” set to -10

    - “For the Shadow!” → *fight starts*
    - “Let's fight!” → *fight starts*

    <span id="d-harlenn_sentbyprim_1"></span>**`harlenn_sentbyprim_1`** Harlenn: “Your expression tells me you have blood on your mind.”

    - “I am sent by the people of Prim to stop you.” → [harlenn_sentbyprim_2](#d-harlenn_sentbyprim_2)
    - “I am sent by the people of Prim to stop you. However, I have decided not to kill you.” → [harlenn_sentbyprim_3](#d-harlenn_sentbyprim_3)

    <span id="d-harlenn_return_1"></span>**`harlenn_return_1`** Harlenn: “You again? I want no business with you. Leave me.”

    - “Why are you people attacking the village of Prim?” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_1](#d-harlenn_prim_1)

    <span id="d-harlenn_completed"></span>**`harlenn_completed`** Harlenn: “Thank you, friend. Your help is greatly appreciated. Everyone in the Blackwater mountain settlement will want to talk to you now.” — **effects:** sets stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240)

    - Next → [harlenn_completed_1](#d-harlenn_completed_1)

    <span id="d-harlenn_killguth_3"></span>**`harlenn_killguth_3`** Harlenn: “They will no longer attack us now that their lying leader is gone!”

    - Next → [harlenn_killguth_4](#d-harlenn_killguth_4)

    <span id="d-harlenn_workingforprim_1"></span>**`harlenn_workingforprim_1`** Harlenn: “My scouts have given me a most interesting report. They say you are working for Prim.”

    - Next → [harlenn_workingforprim_2](#d-harlenn_workingforprim_2)

    <span id="d-harlenn_killguth_1"></span>**`harlenn_killguth_1`** Harlenn: “Hello again. Have you gotten rid of that lying Guthbered down in Prim?”

    - “Not yet, but I am working on it.” → [harlenn_lookforsigns_11](#d-harlenn_lookforsigns_11)
    - “What was I supposed to do again?” → [harlenn_lookforsigns_7](#d-harlenn_lookforsigns_7)
    - “Yes, he is dead.” *(if hand over 1× [Guthbered's ring](../items/guthbered_id.md))* → [harlenn_killguth_2](#d-harlenn_killguth_2)
    - “Yes, he is gone.” *(if reached stage 131 of [The agent and the beast](../quests/bwm_agent.md#stage-131))* → [harlenn_killguth_2](#d-harlenn_killguth_2)

    <span id="d-harlenn_lookforsigns_1"></span>**`harlenn_lookforsigns_1`** Harlenn: “Hello again. Did you find any clues in Prim that they are planning to attack us?”

    - “No, not yet.” → [harlenn_lookforsigns_2](#d-harlenn_lookforsigns_2)
    - “Yes. I found plans that they are recruiting mercenaries and will attack your settlement.” *(if reached stage 100 of [The agent and the beast](../quests/bwm_agent.md#stage-100))* → [harlenn_lookforsigns_3](#d-harlenn_lookforsigns_3)
    - “What was I supposed to do again?” → [harlenn_talkedto_guth_8](#d-harlenn_talkedto_guth_8)

    <span id="d-harlenn_return_3"></span>**`harlenn_return_3`** Harlenn: “Welcome back, traveller. Did you talk to that deceiving Guthbered down in Prim?”

    - “What was I supposed to do again?” → [harlenn_20](#d-harlenn_20)
    - “No, not yet.” → [harlenn_22](#d-harlenn_22)
    - “Yes, I talked to him. He denies that they are behind any of the attacks.” *(if reached stage 80 of [The agent and the beast](../quests/bwm_agent.md#stage-80))* → [harlenn_talkedto_guth_1](#d-harlenn_talkedto_guth_1)
    - “I talked to Guthbered in Prim. They say you are the ones doing the attacks, and that you are behind the gornaud…” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_1](#d-harlenn_prim_1)

    <span id="d-harlenn_return_2"></span>**`harlenn_return_2`** Harlenn: “Welcome back, traveller. What's on your mind?”

    - “I talked to Guthbered in Prim. They say you are attacking Prim, and that you are behind the gornaud attacks on Prim.” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_1](#d-harlenn_prim_1)
    - “What was that you said earlier about the monsters that are attacking your settlement?” → [harlenn_9](#d-harlenn_9)

    <span id="d-harlenn_1"></span>**`harlenn_1`** Harlenn: “Welcome, traveller.”

    - Next → [harlenn_2](#d-harlenn_2)

    <span id="d-harlenn_sentbyprim_3"></span>**`harlenn_sentbyprim_3`** Harlenn: “How interesting... Please continue.”

    - “It's obvious that this conflict will only end in more bloodshed. That should stop here.” → [harlenn_sentbyprim_4](#d-harlenn_sentbyprim_4)

    <span id="d-harlenn_prim_1"></span>**`harlenn_prim_1`** Harlenn: “We?! Hah! It figures he would say that. They are always lying and cheating to get things their way. We have certainly not attacked them!”

    - Next → [harlenn_prim_2](#d-harlenn_prim_2)

    <span id="d-harlenn_completed_1"></span>**`harlenn_completed_1`** Harlenn: “I'm sure the monster attacks will stop now when we kill the last few monsters that are outside the settlement.” — **effects:** sets stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250)


    <span id="d-harlenn_killguth_4"></span>**`harlenn_killguth_4`** Harlenn: “Thank you friend. Here, have these items as a token of our appreciation for your help.” — **effects:** sets stage 150 of [The agent and the beast](../quests/bwm_agent.md#stage-150), gives [Sword of Shadow's rage](../items/clouded_rage.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md)

    - Next → [harlenn_completed](#d-harlenn_completed)

    <span id="d-harlenn_workingforprim_2"></span>**`harlenn_workingforprim_2`** Harlenn: “Of course we can't have that here. We can't have a spy in our midst. You should leave our settlement while you still can, traitor.” — **effects:** sets stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251)


    <span id="d-harlenn_lookforsigns_11"></span>**`harlenn_lookforsigns_11`** Harlenn: “Excellent. Return to me once the deed is done.” — **effects:** sets stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120)


    <span id="d-harlenn_lookforsigns_7"></span>**`harlenn_lookforsigns_7`** Harlenn: “An old saying goes something like 'The only way to truly kill the Gorgon is by removing the head'. In this case, the head of those bastards down in Prim is that fellow Guthbered.”

    - Next → [harlenn_lookforsigns_8](#d-harlenn_lookforsigns_8)

    <span id="d-harlenn_killguth_2"></span>**`harlenn_killguth_2`** Harlenn: “Ha ha! He is finally gone! Now we can rest comfortably in our settlement.” — **effects:** sets stage 149 of [The agent and the beast](../quests/bwm_agent.md#stage-149)

    - Next → [harlenn_killguth_3](#d-harlenn_killguth_3)

    <span id="d-harlenn_lookforsigns_2"></span>**`harlenn_lookforsigns_2`** Harlenn: “Keep looking. I am sure they are planning something wicked.”


    <span id="d-harlenn_lookforsigns_3"></span>**`harlenn_lookforsigns_3`** Harlenn: “I knew it! I knew they were up to something.”

    - Next → [harlenn_lookforsigns_4](#d-harlenn_lookforsigns_4)

    <span id="d-harlenn_talkedto_guth_8"></span>**`harlenn_talkedto_guth_8`** Harlenn: “We believe they are planning to attack us any day now. But we lack the proof that we would need to do anything about it.”

    - Next → [harlenn_talkedto_guth_9](#d-harlenn_talkedto_guth_9)

    <span id="d-harlenn_20"></span>**`harlenn_20`** Harlenn: “OK, this is the plan. I want you to go talk to Guthbered down in Prim, and give him our ultimatum:”

    - Next → [harlenn_21](#d-harlenn_21)

    <span id="d-harlenn_22"></span>**`harlenn_22`** Harlenn: “Good. Now hurry! We don't know how much time we have left before they attack again.” — **effects:** sets stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70)


    <span id="d-harlenn_talkedto_guth_1"></span>**`harlenn_talkedto_guth_1`** Harlenn: “He denies it?! Bah, that treacherous fool. I should have known that he wouldn't dare tell the truth.”

    - Next → [harlenn_talkedto_guth_2](#d-harlenn_talkedto_guth_2)

    <span id="d-harlenn_9"></span>**`harlenn_9`** Harlenn: “Those damn beasts outside our very settlement. The white wyrms and the aulaeth, and their trainers are even deadlier.”

    - “Those? They were no match for me.” → [harlenn_11](#d-harlenn_11)
    - “I can see where this is going. You need me to deal with them for you I guess?” → [harlenn_10](#d-harlenn_10)
    - “At least they aren't anything like those gornaud beasts at the bottom of the mountain.” → [harlenn_12](#d-harlenn_12)

    <span id="d-harlenn_2"></span>**`harlenn_2`** Harlenn: “You must be the newcomer that I heard about that traveled up the mountainside.”

    - Next → [harlenn_3](#d-harlenn_3)

    <span id="d-harlenn_sentbyprim_4"></span>**`harlenn_sentbyprim_4`** Harlenn: “What are you proposing?”

    - “My proposal is that you leave this settlement and find a new home somewhere else.” → [harlenn_sentbyprim_5](#d-harlenn_sentbyprim_5)

    <span id="d-harlenn_prim_2"></span>**`harlenn_prim_2`** Harlenn: “It is, of course, *they* who are the ones causing all the trouble.” — **effects:** sets stage 30 of [Clouded intent](../quests/prim_hunt.md#stage-30)

    - Next → [harlenn_prim_3](#d-harlenn_prim_3)

    <span id="d-harlenn_lookforsigns_8"></span>**`harlenn_lookforsigns_8`** Harlenn: “We should do something about him. You have proven your worth so far. This will be your final assignment.”

    - Next → [harlenn_lookforsigns_9](#d-harlenn_lookforsigns_9)

    <span id="d-harlenn_lookforsigns_4"></span>**`harlenn_lookforsigns_4`** Harlenn: “Oh that lying pig Guthbered.”

    - Next → [harlenn_lookforsigns_5](#d-harlenn_lookforsigns_5)

    <span id="d-harlenn_talkedto_guth_9"></span>**`harlenn_talkedto_guth_9`** Harlenn: “This is where I think an outsider like you might help.”

    - Next → [harlenn_talkedto_guth_10](#d-harlenn_talkedto_guth_10)

    <span id="d-harlenn_21"></span>**`harlenn_21`** Harlenn: “Either they stop their attacks, or we will have to deal with them.”

    - “Sure. I will go tell him your ultimatum.” → [harlenn_22](#d-harlenn_22)
    - “No. In fact, I think I should help the people of Prim instead.” → [harlenn_prim_7](#d-harlenn_prim_7)

    <span id="d-harlenn_talkedto_guth_2"></span>**`harlenn_talkedto_guth_2`** Harlenn: “I am still sure that they somehow are behind all these attacks on us. Who else could there be? There are no other settlements around here for quite a walk.”

    - Next → [harlenn_talkedto_guth_3](#d-harlenn_talkedto_guth_3)

    <span id="d-harlenn_11"></span>**`harlenn_11`** Harlenn: “You sound like my kind of type!”

    - Next → [harlenn_13](#d-harlenn_13)

    <span id="d-harlenn_10"></span>**`harlenn_10`** Harlenn: “Well, yes. But just killing them won't have any effect. We have tried that, to no avail. They just keep coming back.”

    - Next → [harlenn_13](#d-harlenn_13)

    <span id="d-harlenn_12"></span>**`harlenn_12`** Harlenn: “Gornaud? I haven't heard about those. But I'm sure they couldn't possibly be worse than these beasts up here.”

    - Next → [harlenn_13](#d-harlenn_13)

    <span id="d-harlenn_3"></span>**`harlenn_3`** Harlenn: “We need your help in dealing with some ... problems.”

    - “Who are you?” → [harlenn_4](#d-harlenn_4)

    <span id="d-harlenn_sentbyprim_5"></span>**`harlenn_sentbyprim_5`** Harlenn: “Now why would I want to do that?”

    - “These two towns will always fight each other. By you leaving, they will think they have won, and stop their attacks.” → [harlenn_sentbyprim_6](#d-harlenn_sentbyprim_6)

    <span id="d-harlenn_prim_3"></span>**`harlenn_prim_3`** Harlenn: “They even captured one of our fellow scouts. Who knows what they have done to him.”

    - Next → [harlenn_prim_3_1](#d-harlenn_prim_3_1)

    <span id="d-harlenn_lookforsigns_9"></span>**`harlenn_lookforsigns_9`** Harlenn: “I want you to go ... deal ... with him. Guthbered. Preferably in the most painful and gruesome way you can think of.”

    - “No problem.” → [harlenn_lookforsigns_11](#d-harlenn_lookforsigns_11)
    - “Are you sure more violence will really solve this conflict?” → [harlenn_lookforsigns_10](#d-harlenn_lookforsigns_10)
    - “He is as good as dead.” → [harlenn_lookforsigns_11](#d-harlenn_lookforsigns_11)

    <span id="d-harlenn_lookforsigns_5"></span>**`harlenn_lookforsigns_5`** Harlenn: “Anyway, thank you for your help in finding this evidence.” — **effects:** sets stage 110 of [The agent and the beast](../quests/bwm_agent.md#stage-110)

    - Next → [harlenn_lookforsigns_6](#d-harlenn_lookforsigns_6)

    <span id="d-harlenn_talkedto_guth_10"></span>**`harlenn_talkedto_guth_10`** Harlenn: “I want you to go investigate Prim for any signs that you might find of them preparing an attack on us.”

    - “Sure, sounds easy.” → [harlenn_talkedto_guth_11](#d-harlenn_talkedto_guth_11)

    <span id="d-harlenn_prim_7"></span>**`harlenn_prim_7`** Harlenn: “Bah. Then you are useless to me. Why did you even bother to come up here and waste my time? Begone.” — **effects:** sets stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250)


    <span id="d-harlenn_talkedto_guth_3"></span>**`harlenn_talkedto_guth_3`** Harlenn: “Besides, they have always been treacherous. No, of course they are behind the attacks.” — **effects:** sets stage 90 of [The agent and the beast](../quests/bwm_agent.md#stage-90)

    - Next → [harlenn_talkedto_guth_4](#d-harlenn_talkedto_guth_4)

    <span id="d-harlenn_13"></span>**`harlenn_13`** Harlenn: “Anyway, the beasts are really starting to cut down our numbers. But they are not our only concern.”

    - Next → [harlenn_14](#d-harlenn_14)

    <span id="d-harlenn_4"></span>**`harlenn_4`** Harlenn: “Oh sorry, I did not introduce myself properly. I am Harlenn, battle master of the people living in this mountain settlement.”

    - “I was told to see you by the guide that led me up the mountain.” → [harlenn_5](#d-harlenn_5)

    <span id="d-harlenn_sentbyprim_6"></span>**`harlenn_sentbyprim_6`** Harlenn: “Hmm, you might have a point there.”

    - Next → [harlenn_sentbyprim_7](#d-harlenn_sentbyprim_7)

    <span id="d-harlenn_prim_3_1"></span>**`harlenn_prim_3_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [The agent and the beast](../quests/bwm_agent.md#stage-90))* → *conversation ends*
    - branch 2 *(if reached stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251))* → *conversation ends*
    - branch 3 *(if reached stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250))* → *conversation ends*
    - branch 4 → [harlenn_prim_4](#d-harlenn_prim_4)

    <span id="d-harlenn_lookforsigns_10"></span>**`harlenn_lookforsigns_10`** Harlenn: “You saw the plans yourself. They are going to attack us if we don't do something about them. Of course we have to kill him!”

    - “I will remove him, but I will try to find a peaceful solution to this.” → [harlenn_lookforsigns_12](#d-harlenn_lookforsigns_12)
    - “Very well. He is as good as dead.” → [harlenn_lookforsigns_11](#d-harlenn_lookforsigns_11)

    <span id="d-harlenn_lookforsigns_6"></span>**`harlenn_lookforsigns_6`** Harlenn: “This calls for drastic measures. We have to act quickly before they can have time to complete their plan.”

    - Next → [harlenn_lookforsigns_7](#d-harlenn_lookforsigns_7)

    <span id="d-harlenn_talkedto_guth_11"></span>**`harlenn_talkedto_guth_11`** Harlenn: “Good. Try not to be seen. You should go look for any clues around where that deceiving Guthbered stays.” — **effects:** sets stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95)


    <span id="d-harlenn_talkedto_guth_4"></span>**`harlenn_talkedto_guth_4`** Harlenn: “OK, this leaves us with no choice. We will have to step this up to another level.”

    - Next → [harlenn_talkedto_guth_5](#d-harlenn_talkedto_guth_5)

    <span id="d-harlenn_14"></span>**`harlenn_14`** Harlenn: “On top of that, we are being attacked by raids from those bastards down in that low-life town of Prim at the base of the mountain.” — **effects:** sets stage 65 of [The agent and the beast](../quests/bwm_agent.md#stage-65)

    - Next → [harlenn_15](#d-harlenn_15)

    <span id="d-harlenn_5"></span>**`harlenn_5`** Harlenn: “Oh yes, we are lucky he found you. You see, we seldom travel that far down the mountain.”

    - Next → [harlenn_6](#d-harlenn_6)

    <span id="d-harlenn_sentbyprim_7"></span>**`harlenn_sentbyprim_7`** Harlenn: “OK, you have convinced me. I will leave this settlement for another to find my home. The survival of my people here is more important than me.”

    - Next → [harlenn_sentbyprim_8](#d-harlenn_sentbyprim_8)

    <span id="d-harlenn_prim_4"></span>**`harlenn_prim_4`** Harlenn: “I'm telling you, they are treacherous and lying!”

    - “Sure, I believe you. What do you need from me?” → [harlenn_prim_6](#d-harlenn_prim_6)
    - “What would I gain by helping you instead of them?” → [harlenn_prim_5](#d-harlenn_prim_5)
    - “I'm not buying this. I think I would rather help the people of Prim than you people.” → [harlenn_prim_7](#d-harlenn_prim_7)

    <span id="d-harlenn_lookforsigns_12"></span>**`harlenn_lookforsigns_12`** Harlenn: “Fine. Do whatever you need to remove him, but I don't want to deal with their attacks anymore.” — **effects:** sets stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120)


    <span id="d-harlenn_talkedto_guth_5"></span>**`harlenn_talkedto_guth_5`** Harlenn: “Are you sure you are up to it? You are not one of their spies are you? If you are working for them, then you should know that they are not to be trusted!”

    - “I am ready for anything. I will help your settlement.” → [harlenn_talkedto_guth_7](#d-harlenn_talkedto_guth_7)
    - “Actually, now that you mention it...” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_talkedto_guth_6](#d-harlenn_talkedto_guth_6)
    - “Yes, I am working for Prim also. They seem like sensible people.” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_7](#d-harlenn_prim_7)

    <span id="d-harlenn_15"></span>**`harlenn_15`** Harlenn: “Oh, those treacherous, fake bastards.”

    - “What have they done?” → [harlenn_16](#d-harlenn_16)
    - “I talked to Guthbered in Prim. They say you are the ones doing the attacks, and that you are behind the gornaud…” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_1](#d-harlenn_prim_1)
    - “Is there anything I can do to help?” → [harlenn_18](#d-harlenn_18)

    <span id="d-harlenn_6"></span>**`harlenn_6`** Harlenn: “We spend most of our time in the settlement up here on the mountain.”

    - Next → [harlenn_7](#d-harlenn_7)

    <span id="d-harlenn_prim_6"></span>**`harlenn_prim_6`** Harlenn: “Good. We will need an able fighter to help us deal with the monsters and the Prim bandits.”

    - Next → [harlenn_19](#d-harlenn_19)

    <span id="d-harlenn_prim_5"></span>**`harlenn_prim_5`** Harlenn: “Gain? Our trust of course. You would always be welcome here in our camp. Our traders have some excellent equipment.”

    - “OK, I'll help you deal with them.” → [harlenn_prim_6](#d-harlenn_prim_6)
    - “I'm still not convinced, but I'll help you for now.” → [harlenn_prim_6](#d-harlenn_prim_6)

    <span id="d-harlenn_talkedto_guth_7"></span>**`harlenn_talkedto_guth_7`** Harlenn: “Good.”

    - Next → [harlenn_talkedto_guth_8](#d-harlenn_talkedto_guth_8)

    <span id="d-harlenn_talkedto_guth_6"></span>**`harlenn_talkedto_guth_6`** Harlenn: “What? Are you working for them or not?”

    - “No, never mind. I am ready to help your settlement.” → [harlenn_talkedto_guth_7](#d-harlenn_talkedto_guth_7)
    - “I was. But I have decided to help you instead.” → [harlenn_talkedto_guth_7](#d-harlenn_talkedto_guth_7)
    - “Yes. I am helping them get rid of you people.” → [harlenn_prim_7](#d-harlenn_prim_7)

    <span id="d-harlenn_16"></span>**`harlenn_16`** Harlenn: “They come here at night and sabotage our supplies.”

    - Next → [harlenn_17](#d-harlenn_17)

    <span id="d-harlenn_18"></span>**`harlenn_18`** Harlenn: “Why, yes. Of course. If you are up to it.”

    - Next → [harlenn_19](#d-harlenn_19)

    <span id="d-harlenn_7"></span>**`harlenn_7`** Harlenn: “However, recent events have forced us to send for help. We are lucky you found us.”

    - “What problems are you referring to?” → [harlenn_8](#d-harlenn_8)
    - “What is happening up here?” → [harlenn_8](#d-harlenn_8)

    <span id="d-harlenn_19"></span>**`harlenn_19`** Harlenn: “Considering you made it up here alive, I'm pretty sure you can handle yourself.”

    - Next → [harlenn_20](#d-harlenn_20)

    <span id="d-harlenn_17"></span>**`harlenn_17`** Harlenn: “We are almost certain they are the ones behind these monsters also.” — **effects:** sets stage 66 of [The agent and the beast](../quests/bwm_agent.md#stage-66)

    - “I talked to Guthbered in Prim. They say you are the ones doing the attacks, and that you are behind the gornaud…” *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [harlenn_prim_1](#d-harlenn_prim_1)
    - “Is there anything I can do to help?” → [harlenn_18](#d-harlenn_18)

    <span id="d-harlenn_8"></span>**`harlenn_8`** Harlenn: “I am sure you noticed just by getting here. The monsters of course!”

    - Next → [harlenn_9](#d-harlenn_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Faction: added (fct_bwm)<br>Dialogue: 23 lines changed<br>· text: “Hm, you might have a point there.” → “Hmm, you might have a point there.”<br>· text: “Ok, this leaves us with no choice. We will have to step this up to an…” → “OK, this leaves us with no choice. We will have to step this up to an…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `harlenn` |
    | Spawn group | `harlenn` |
    | Loot table | `harlenn` |
    | Conversation | `harlenn_start` |
    | Faction | `fct_bwm` |
    | Movement | – |
    | Icon | `monsters_men2:6` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "harlenn",
     "name": "Harlenn",
     "iconID": "monsters_men2:6",
     "maxHP": 80,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 4,
      "max": 9
     },
     "spawnGroup": "harlenn",
     "faction": "fct_bwm",
     "phraseID": "harlenn_start",
     "droplistID": "harlenn",
     "attackCost": 5,
     "attackChance": 70,
     "blockChance": 80,
     "damageResistance": 4
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=harlenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=harlenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=harlenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=harlenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
