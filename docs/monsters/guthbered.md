---
description: "Guthbered is an NPC who can also be fought in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_92.png){ .sprite } Guthbered

**Where to find Guthbered:** Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-guthbered)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_92.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 80 |
| **XP when defeated** | 146 |
| **Entry ID** | `guthbered` |
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
| [Guthbered's ring](../items/guthbered_id.md) | 100% | 1 |
| [Barbed dagger](../items/dagger_barbed.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 20 to 50 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain29](../maps/blackwater_mountain29.md) | Prim | 1 | – |

## Quests

- [Clouded intent](../quests/prim_hunt.md): stages 11, 20, 25, 40, 50, 70, 80, 99, 100, 240, 250, 251
- [The agent and the beast](../quests/bwm_agent.md): stages 25, 80, 130, 131, 250

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guthbered. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guthbered_start.json" data-npc="Guthbered" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (83 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guthbered_start"></span>**`guthbered_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 131 of [The agent and the beast](../quests/bwm_agent.md#stage-131))* → [guthbered_sentbybwm_leave](#d-guthbered_sentbybwm_leave)
    - branch 2 *(if reached stage 130 of [The agent and the beast](../quests/bwm_agent.md#stage-130))* → [guthbered_sentbybwm_fight](#d-guthbered_sentbybwm_fight)
    - branch 3 *(if reached stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120))* → [guthbered_sentbybwm_1](#d-guthbered_sentbybwm_1)
    - branch 4 *(if reached stage 251 of [Clouded intent](../quests/prim_hunt.md#stage-251))* → [guthbered_reject](#d-guthbered_reject)
    - branch 5 *(if reached stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250))* → [guthbered_reject](#d-guthbered_reject)
    - branch 6 *(if reached stage 100 of [Clouded intent](../quests/prim_hunt.md#stage-100))* → [guthbered_completed](#d-guthbered_completed)
    - branch 7 *(if reached stage 99 of [Clouded intent](../quests/prim_hunt.md#stage-99))* → [guthbered_killharl_2](#d-guthbered_killharl_2)
    - branch 8 *(if reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95))* → [guthbered_workingforbwm_2](#d-guthbered_workingforbwm_2)
    - branch 9 *(if reached stage 80 of [Clouded intent](../quests/prim_hunt.md#stage-80))* → [guthbered_killharl_1](#d-guthbered_killharl_1)
    - branch 10 *(if reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50))* → [guthbered_lookforsigns_1](#d-guthbered_lookforsigns_1)
    - branch 11 *(if reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25))* → [guthbered_return_1_1](#d-guthbered_return_1_1)
    - branch 12 → [guthbered_1](#d-guthbered_1)

    <span id="d-guthbered_sentbybwm_leave"></span>**`guthbered_sentbybwm_leave`** Guthbered: “Thank you friend, for talking some sense into me.” — **effects:** sets stage 131 of [The agent and the beast](../quests/bwm_agent.md#stage-131)

    - “You are welcome.” → *NPC leaves*

    <span id="d-guthbered_sentbybwm_fight"></span>**`guthbered_sentbybwm_fight`** Guthbered: “I had hoped it would not come to this. I'm afraid that you will not survive this encounter. Yet another life on my hands.” — **effects:** sets stage 130 of [The agent and the beast](../quests/bwm_agent.md#stage-130), faction “fct_prim” set to -10

    - “For the Shadow!” → *fight starts*
    - “Brave words, let's see if you can back them up with anything.” → *fight starts*
    - “Great, I have been longing to kill you.” → *fight starts*
    - “Let's fight!” → *fight starts*

    <span id="d-guthbered_sentbybwm_1"></span>**`guthbered_sentbybwm_1`** Guthbered: “The glow in your eyes frightens me.”

    - “I am sent by the Blackwater mountain settlement to stop you.” → [guthbered_sentbybwm_fight](#d-guthbered_sentbybwm_fight)
    - “I am sent by the Blackwater mountain settlement to stop you. However, I have decided not to kill you.” → [guthbered_sentbybwm_3](#d-guthbered_sentbybwm_3)

    <span id="d-guthbered_reject"></span>**`guthbered_reject`** Guthbered: “You again? Leave this place and go to your friends up in the Blackwater mountain settlement instead. We want no business with you.”

    - “I am here to give you a message from the Blackwater mountain settlement.” *(if reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70))* → [guthbered_attacks](#d-guthbered_attacks)

    <span id="d-guthbered_completed"></span>**`guthbered_completed`** Guthbered: “Hello again my friend. Thank you for your help in dealing with the bandits up in Blackwater mountain.”

    - Next → [guthbered_completed_1](#d-guthbered_completed_1)

    <span id="d-guthbered_killharl_2"></span>**`guthbered_killharl_2`** Guthbered: “While I am grateful for this news in knowing that he is dead, I am also saddened that it had to come to this.” — **effects:** sets stage 99 of [Clouded intent](../quests/prim_hunt.md#stage-99)

    - Next → [guthbered_killharl_4](#d-guthbered_killharl_4)

    <span id="d-guthbered_workingforbwm_2"></span>**`guthbered_workingforbwm_2`** Guthbered: “My sources from inside the Blackwater mountain settlement tell me you are working for them.”

    - Next → [guthbered_workingforbwm_3](#d-guthbered_workingforbwm_3)

    <span id="d-guthbered_killharl_1"></span>**`guthbered_killharl_1`** Guthbered: “Hello again. Did you manage to remove that bastard battle master Harlenn from the Blackwater mountain settlement?”

    - “Can you tell me again what I was supposed to do?” → [guthbered_lookforsigns_6](#d-guthbered_lookforsigns_6)
    - “Not yet. I am still working on it.” → [guthbered_lookforsigns_9](#d-guthbered_lookforsigns_9)
    - “Yes, he is dead.” *(if hand over 1× [Harlenn's ring](../items/harlenn_id.md))* → [guthbered_killharl_2](#d-guthbered_killharl_2)
    - “Yes, he is gone.” *(if reached stage 91 of [Clouded intent](../quests/prim_hunt.md#stage-91))* → [guthbered_killharl_3](#d-guthbered_killharl_3)

    <span id="d-guthbered_lookforsigns_1"></span>**`guthbered_lookforsigns_1`** Guthbered: “Hello again. Did you find anything up in the Blackwater mountain settlement?”

    - “No, I am still looking.” → [guthbered_talkedto_harl_13](#d-guthbered_talkedto_harl_13)
    - “What was I supposed to do again?” → [guthbered_talkedto_harl_9](#d-guthbered_talkedto_harl_9)
    - “Yes, I found some papers with a plan to attack Prim.” *(if reached stage 60 of [Clouded intent](../quests/prim_hunt.md#stage-60))* → [guthbered_lookforsigns_2](#d-guthbered_lookforsigns_2)

    <span id="d-guthbered_return_1_1"></span>**`guthbered_return_1_1`** Guthbered: “Welcome back, traveller. Did you talk to Harlenn up in the Blackwater mountain settlement?”

    - “Can you tell me the story about the monsters again?” → [guthbered_13](#d-guthbered_13)
    - “What was I supposed to do again?” → [guthbered_29](#d-guthbered_29)
    - “Can you tell me the story about Prim again?” → [guthbered_2](#d-guthbered_2)
    - “Yes, but Harlenn denies that they have anything to do with the attacks.” *(if reached stage 30 of [Clouded intent](../quests/prim_hunt.md#stage-30))* → [guthbered_talkedto_harl_1](#d-guthbered_talkedto_harl_1)
    - “Actually, I am here to give you a message from the Blackwater mountain settlement.” *(if reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70))* → [guthbered_attacks](#d-guthbered_attacks)

    <span id="d-guthbered_1"></span>**`guthbered_1`** Guthbered: “Welcome to Prim, traveller.”

    - “What can you tell me about Prim?” → [guthbered_2](#d-guthbered_2)
    - “Who are you?” → [guthbered_who_1](#d-guthbered_who_1)
    - “I was told to see you about helping against the monster attacks.” *(if reached stage 11 of [Clouded intent](../quests/prim_hunt.md#stage-11))* → [guthbered_20](#d-guthbered_20)
    - “Actually, I am here to give you a message from the Blackwater mountain settlement.” *(if reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70))* → [guthbered_attacks](#d-guthbered_attacks)

    <span id="d-guthbered_sentbybwm_3"></span>**`guthbered_sentbybwm_3`** Guthbered: “How interesting... Please continue.”

    - “It's obvious that this conflict will only end in more bloodshed. That should stop here.” → [guthbered_sentbybwm_4](#d-guthbered_sentbybwm_4)

    <span id="d-guthbered_attacks"></span>**`guthbered_attacks`** Guthbered: “What message?”

    - “Harlenn in the Blackwater mountain settlement wants you to stop your attacks on their settlement.” → [guthbered_attacks_1](#d-guthbered_attacks_1)

    <span id="d-guthbered_completed_1"></span>**`guthbered_completed_1`** Guthbered: “I am sure everyone here in Prim will want to talk to you now.” — **effects:** sets stage 240 of [Clouded intent](../quests/prim_hunt.md#stage-240)

    - Next → [guthbered_completed_2](#d-guthbered_completed_2)

    <span id="d-guthbered_killharl_4"></span>**`guthbered_killharl_4`** Guthbered: “This will hopefully mean that their attacks on our village will cease.”

    - Next → [guthbered_killharl_5](#d-guthbered_killharl_5)

    <span id="d-guthbered_workingforbwm_3"></span>**`guthbered_workingforbwm_3`** Guthbered: “It is, of course, your choice. But if you are working for them, you are not welcome here in Prim. You should leave quickly, while you still can.” — **effects:** sets stage 251 of [Clouded intent](../quests/prim_hunt.md#stage-251)


    <span id="d-guthbered_lookforsigns_6"></span>**`guthbered_lookforsigns_6`** Guthbered: “I had hoped it would not come to this. But we are left with no choice. We must remove their main driving force behind the raids. We must remove their battle master, Harlenn.”

    - Next → [guthbered_lookforsigns_7](#d-guthbered_lookforsigns_7)

    <span id="d-guthbered_lookforsigns_9"></span>**`guthbered_lookforsigns_9`** Guthbered: “Excellent. Return to me once you are done.” — **effects:** sets stage 80 of [Clouded intent](../quests/prim_hunt.md#stage-80)


    <span id="d-guthbered_killharl_3"></span>**`guthbered_killharl_3`** Guthbered: “Really? This is great news indeed.”

    - Next → [guthbered_killharl_4](#d-guthbered_killharl_4)

    <span id="d-guthbered_talkedto_harl_13"></span>**`guthbered_talkedto_harl_13`** Guthbered: “Thank you, friend. Report back to me with your findings.” — **effects:** sets stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50)


    <span id="d-guthbered_talkedto_harl_9"></span>**`guthbered_talkedto_harl_9`** Guthbered: “I want you to go up there into their settlement and find any clues as to what they are planning.”

    - Next → [guthbered_talkedto_harl_10](#d-guthbered_talkedto_harl_10)

    <span id="d-guthbered_lookforsigns_2"></span>**`guthbered_lookforsigns_2`** Guthbered: “Then it is as we suspected. This is terrible news indeed.”

    - Next → [guthbered_lookforsigns_3](#d-guthbered_lookforsigns_3)

    <span id="d-guthbered_13"></span>**`guthbered_13`** Guthbered: “A while ago, we started seeing the first of the monsters. At first, they were no problem for us to handle. Our guards could cut them down easily.”

    - Next → [guthbered_14](#d-guthbered_14)

    <span id="d-guthbered_29"></span>**`guthbered_29`** Guthbered: “As I said, we believe those bastards up at the Blackwater mountain settlement are behind the monster attacks somehow.”

    - Next → [guthbered_30](#d-guthbered_30)

    <span id="d-guthbered_2"></span>**`guthbered_2`** Guthbered: “Prim began as a simple camp for the miners that worked in the mines around here. Later it grew to a settlement, and a few years back we even got a tavern and an inn here.”

    - Next → [guthbered_3](#d-guthbered_3)

    <span id="d-guthbered_talkedto_harl_1"></span>**`guthbered_talkedto_harl_1`** Guthbered: “What did I expect? Of course he would say that. He probably even denies it to himself. Meanwhile, we here in Prim suffer from their savage raids.”

    - Next → [guthbered_talkedto_harl_2](#d-guthbered_talkedto_harl_2)

    <span id="d-guthbered_who_1"></span>**`guthbered_who_1`** Guthbered: “I am Guthbered, protector of this village.”

    - “What can you tell me about Prim?” → [guthbered_2](#d-guthbered_2)
    - “I was told to see you about helping against the monster attacks.” *(if reached stage 11 of [Clouded intent](../quests/prim_hunt.md#stage-11))* → [guthbered_20](#d-guthbered_20)

    <span id="d-guthbered_20"></span>**`guthbered_20`** Guthbered: “Oh good. Did you talk to Tonis? Yes, I'm sure you met him on your way into town.”

    - Next → [guthbered_21](#d-guthbered_21)

    <span id="d-guthbered_sentbybwm_4"></span>**`guthbered_sentbybwm_4`** Guthbered: “What are you proposing?”

    - “My proposal is that you leave this village and find a new home somewhere else.” → [guthbered_sentbybwm_5](#d-guthbered_sentbybwm_5)

    <span id="d-guthbered_attacks_1"></span>**`guthbered_attacks_1`** Guthbered: “That's completely insane. We!? Stop OUR attacks?! You tell him that we have nothing to do with what happens up there. They have brought their own misfortune upon themselves.” — **effects:** sets stage 80 of [The agent and the beast](../quests/bwm_agent.md#stage-80)


    <span id="d-guthbered_completed_2"></span>**`guthbered_completed_2`** Guthbered: “Thank you again for your help.” — **effects:** sets stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250)


    <span id="d-guthbered_killharl_5"></span>**`guthbered_killharl_5`** Guthbered: “I do not know how to thank you enough my friend.”

    - Next → [guthbered_killharl_6](#d-guthbered_killharl_6)

    <span id="d-guthbered_lookforsigns_7"></span>**`guthbered_lookforsigns_7`** Guthbered: “This would be an excellent task for you my friend. Since you have access to their facilities, you can sneak in and kill that bastard Harlenn.”

    - Next → [guthbered_lookforsigns_8](#d-guthbered_lookforsigns_8)

    <span id="d-guthbered_talkedto_harl_10"></span>**`guthbered_talkedto_harl_10`** Guthbered: “We believe they are training their fighters to launch a larger raid on us soon.”

    - Next → [guthbered_talkedto_harl_11](#d-guthbered_talkedto_harl_11)

    <span id="d-guthbered_lookforsigns_3"></span>**`guthbered_lookforsigns_3`** Guthbered: “Now you know what I was talking about. They are always looking to cause trouble.”

    - Next → [guthbered_lookforsigns_4](#d-guthbered_lookforsigns_4)

    <span id="d-guthbered_14"></span>**`guthbered_14`** Guthbered: “But after a while, some of our guards got hurt, and the monsters started increasing in numbers.”

    - Next → [guthbered_15](#d-guthbered_15)

    <span id="d-guthbered_30"></span>**`guthbered_30`** Guthbered: “I want you to go up there to their settlement and ask their battle master, Harlenn, why they are doing this to us.” — **effects:** sets stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25)

    - “OK, I will go ask Harlenn in the Blackwater mountain settlement why they are attacking your village.” → [guthbered_31](#d-guthbered_31)

    <span id="d-guthbered_3"></span>**`guthbered_3`** Guthbered: “This place used to be full of life when the miners worked here.”

    - Next → [guthbered_4](#d-guthbered_4)

    <span id="d-guthbered_talkedto_harl_2"></span>**`guthbered_talkedto_harl_2`** Guthbered: “I am sure they are behind these attacks. However, I do not have sufficient evidence to back up my statements in order to do anything about it.”

    - Next → [guthbered_talkedto_harl_3](#d-guthbered_talkedto_harl_3)

    <span id="d-guthbered_21"></span>**`guthbered_21`** Guthbered: “Good. Let me tell you the back-story about Prim first.”

    - “Sure.” → [guthbered_2](#d-guthbered_2)
    - “I'd rather skip to the end directly.” → [guthbered_13](#d-guthbered_13)

    <span id="d-guthbered_sentbybwm_5"></span>**`guthbered_sentbybwm_5`** Guthbered: “Now why would I want to do that?”

    - “These two towns will always fight each other. By you leaving, they will think they have won, and stop their attacks.” → [guthbered_sentbybwm_6](#d-guthbered_sentbybwm_6)

    <span id="d-guthbered_killharl_6"></span>**`guthbered_killharl_6`** Guthbered: “Here, please accept these few items as some form of compensation for your help. Also, take this piece of paper that we have acquired.” — **effects:** sets stage 100 of [Clouded intent](../quests/prim_hunt.md#stage-100), gives [Blackwater dagger](../items/bwm_dagger.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md), [Forged papers for Blackwater](../items/bwm_permit.md)

    - Next → [guthbered_killharl_7](#d-guthbered_killharl_7)

    <span id="d-guthbered_lookforsigns_8"></span>**`guthbered_lookforsigns_8`** Guthbered: “By killing him, we can be sure that their attacks will ... shall we say ... lose their teeth. He he.”

    - “No problem, he is as good as dead.” → [guthbered_lookforsigns_9](#d-guthbered_lookforsigns_9)
    - “Are you sure more violence will really solve this conflict?” → [guthbered_lookforsigns_10](#d-guthbered_lookforsigns_10)

    <span id="d-guthbered_talkedto_harl_11"></span>**`guthbered_talkedto_harl_11`** Guthbered: “Go look for any plans that you might find. But make sure that they do not see you while you're looking around.”

    - Next → [guthbered_talkedto_harl_12](#d-guthbered_talkedto_harl_12)

    <span id="d-guthbered_lookforsigns_4"></span>**`guthbered_lookforsigns_4`** Guthbered: “Thank you for finding this information for us.” — **effects:** sets stage 70 of [Clouded intent](../quests/prim_hunt.md#stage-70)

    - Next → [guthbered_lookforsigns_5](#d-guthbered_lookforsigns_5)

    <span id="d-guthbered_15"></span>**`guthbered_15`** Guthbered: “Also, the monsters almost seemed like they were getting smarter. Their attacks were getting more and more coordinated.”

    - Next → [guthbered_16](#d-guthbered_16)

    <span id="d-guthbered_31"></span>**`guthbered_31`** Guthbered: “Thank you friend.” — **effects:** sets stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25)


    <span id="d-guthbered_4"></span>**`guthbered_4`** Guthbered: “The miners also attracted a lot of traders that used to come through here.”

    - “'used to'?” → [guthbered_5](#d-guthbered_5)
    - “What happened then?” → [guthbered_5](#d-guthbered_5)

    <span id="d-guthbered_talkedto_harl_3"></span>**`guthbered_talkedto_harl_3`** Guthbered: “But I am sure they are! As false as they are, they must be. Always lying and deceiving. Causing destruction and turmoil.” — **effects:** sets stage 40 of [Clouded intent](../quests/prim_hunt.md#stage-40)

    - Next → [guthbered_talkedto_harl_4](#d-guthbered_talkedto_harl_4)

    <span id="d-guthbered_sentbybwm_6"></span>**`guthbered_sentbybwm_6`** Guthbered: “Hmm, you might have a point there.”

    - Next → [guthbered_sentbybwm_7](#d-guthbered_sentbybwm_7)

    <span id="d-guthbered_killharl_7"></span>**`guthbered_killharl_7`** Guthbered: “This is a permit that we have ... produced, which according to our sources, will allow you to enter their inner chamber in the Blackwater mountain settlement.”

    - Next → [guthbered_killharl_8](#d-guthbered_killharl_8)

    <span id="d-guthbered_lookforsigns_10"></span>**`guthbered_lookforsigns_10`** Guthbered: “No, not really. But for now, it looks like the only option we have.”

    - “I will remove him, but I will try to find a peaceful solution to this.” → [guthbered_lookforsigns_9](#d-guthbered_lookforsigns_9)
    - “Very well. He is as good as dead.” → [guthbered_lookforsigns_9](#d-guthbered_lookforsigns_9)

    <span id="d-guthbered_talkedto_harl_12"></span>**`guthbered_talkedto_harl_12`** Guthbered: “You should probably start your search around where their battle master, Harlenn, stays.”

    - “OK. I will look for clues in their settlement.” → [guthbered_talkedto_harl_13](#d-guthbered_talkedto_harl_13)

    <span id="d-guthbered_lookforsigns_5"></span>**`guthbered_lookforsigns_5`** Guthbered: “Very well. We will have to deal with this.”

    - Next → [guthbered_lookforsigns_6](#d-guthbered_lookforsigns_6)

    <span id="d-guthbered_16"></span>**`guthbered_16`** Guthbered: “Now, we can hardly hold them back. They mostly come at night.”

    - Next → [guthbered_17](#d-guthbered_17)

    <span id="d-guthbered_5"></span>**`guthbered_5`** Guthbered: “Just until recently, we could at least get some contact with the outside villages. Nowadays, that hope is lost.”

    - Next → [guthbered_6](#d-guthbered_6)

    <span id="d-guthbered_talkedto_harl_4"></span>**`guthbered_talkedto_harl_4`** Guthbered: “Just listen to the name they have chosen for themselves: 'Blackwater'. The tone of it sounds like trouble.”

    - Next → [guthbered_talkedto_harl_5](#d-guthbered_talkedto_harl_5)

    <span id="d-guthbered_sentbybwm_7"></span>**`guthbered_sentbybwm_7`** Guthbered: “OK, you have convinced me. I will leave Prim for another town. The survival of my people here is more important than me.”

    - Next → [guthbered_sentbybwm_leave](#d-guthbered_sentbybwm_leave)

    <span id="d-guthbered_killharl_8"></span>**`guthbered_killharl_8`** Guthbered: “Now, the permit is not ... shall we say ... completely genuine. But we are certain that the guards won't notice any difference.”

    - Next → [guthbered_killharl_9](#d-guthbered_killharl_9)

    <span id="d-guthbered_17"></span>**`guthbered_17`** Guthbered: “According to lore, the monsters are called the 'gornauds'.”

    - “Any ideas where they might be coming from?” → [guthbered_18](#d-guthbered_18)

    <span id="d-guthbered_6"></span>**`guthbered_6`** Guthbered: “You see, the mine tunnel to the south is collapsed, and no one can get in or out of Prim.”

    - “I know, I just came from there.” → [guthbered_7](#d-guthbered_7)
    - “Tough luck.” → [guthbered_10](#d-guthbered_10)
    - “What made it collapse?” → [guthbered_11](#d-guthbered_11)

    <span id="d-guthbered_talkedto_harl_5"></span>**`guthbered_talkedto_harl_5`** Guthbered: “Anyway. I would like to get some further evidence on what they are up to. Maybe something you can help us with.”

    - Next → [guthbered_talkedto_harl_6](#d-guthbered_talkedto_harl_6)

    <span id="d-guthbered_killharl_9"></span>**`guthbered_killharl_9`** Guthbered: “Anyway, you have my greatest thanks for the assistance that you have provided for us.”

    - Next → [guthbered_completed_1](#d-guthbered_completed_1)

    <span id="d-guthbered_18"></span>**`guthbered_18`** Guthbered: “Oh yes, we are almost certain.”

    - Next → [guthbered_19](#d-guthbered_19)

    <span id="d-guthbered_7"></span>**`guthbered_7`** Guthbered: “You did? Oh. Well, yes of course you must have since you are not from Prim. So there's a way through it after all huh?”

    - “Yes, but I had to go through the old pitch-black mine.” → [guthbered_8](#d-guthbered_8)
    - “Yes, the passage in the mine below is safe.” → [guthbered_8](#d-guthbered_8)
    - “No, just kidding. I scaled over the mountain ridge to get here.” → [guthbered_8](#d-guthbered_8)

    <span id="d-guthbered_10"></span>**`guthbered_10`** Guthbered: “The collapsed mine tunnel makes it hard for any traders to reach Prim. Our resources are really starting to dwindle.”

    - Next → [guthbered_12](#d-guthbered_12)

    <span id="d-guthbered_11"></span>**`guthbered_11`** Guthbered: “We are not sure. But we have our suspicions.”

    - Next → [guthbered_10](#d-guthbered_10)

    <span id="d-guthbered_talkedto_harl_6"></span>**`guthbered_talkedto_harl_6`** Guthbered: “But I need to be sure that I can trust you. If you are working for them, you had better tell me now before things get ... messy.”

    - “Sure, you can trust me. I will help the people of Prim.” → [guthbered_talkedto_harl_8](#d-guthbered_talkedto_harl_8)
    - “Hmm, maybe I should help the people up in Blackwater mountain instead.” → [guthbered_workingforbwm_1](#d-guthbered_workingforbwm_1)
    - “[Lie] You can trust me.” *(if reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70))* → [guthbered_talkedto_harl_7](#d-guthbered_talkedto_harl_7)

    <span id="d-guthbered_19"></span>**`guthbered_19`** Guthbered: “Those evil bastards up in the Blackwater mountain settlement probably summoned them to attack us. They would rather see us perish.” — **effects:** sets stage 20 of [Clouded intent](../quests/prim_hunt.md#stage-20)

    - Next → [guthbered_22](#d-guthbered_22)

    <span id="d-guthbered_8"></span>**`guthbered_8`** Guthbered: “OK. We will have to investigate that later.”

    - Next → [guthbered_9](#d-guthbered_9)

    <span id="d-guthbered_12"></span>**`guthbered_12`** Guthbered: “On top of that, there are the attacks from the monsters that we have to deal with.” — **effects:** sets stage 11 of [Clouded intent](../quests/prim_hunt.md#stage-11)

    - “Yes, I noticed some monsters outside the village.” → [guthbered_13](#d-guthbered_13)
    - “What monsters?” → [guthbered_13](#d-guthbered_13)

    <span id="d-guthbered_talkedto_harl_8"></span>**`guthbered_talkedto_harl_8`** Guthbered: “Good. I'm glad you want to help us.”

    - Next → [guthbered_talkedto_harl_9](#d-guthbered_talkedto_harl_9)

    <span id="d-guthbered_workingforbwm_1"></span>**`guthbered_workingforbwm_1`** Guthbered: “Fine. You should leave now while you still can, traitor.” — **effects:** sets stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250)


    <span id="d-guthbered_talkedto_harl_7"></span>**`guthbered_talkedto_harl_7`** Guthbered: “Yet somehow I do not trust you.”

    - “I was working for them, but I have decided to help you instead.” → [guthbered_talkedto_harl_8](#d-guthbered_talkedto_harl_8)
    - “Why would I ever want to work for your filthy village? The people in the Blackwater mountain settlement deserve my…” → [guthbered_workingforbwm_1](#d-guthbered_workingforbwm_1)

    <span id="d-guthbered_22"></span>**`guthbered_22`** Guthbered: “We used to trade with them up there, but that all changed once they got greedy.” — **effects:** sets stage 25 of [The agent and the beast](../quests/bwm_agent.md#stage-25)

    - “I met a man outside the collapsed mine saying he was from the Blackwater mountain settlement.” → [guthbered_26](#d-guthbered_26)
    - “Do you need any help in dealing with those monsters?” → [guthbered_23](#d-guthbered_23)
    - “I would be glad to help you with the monsters.” → [guthbered_24](#d-guthbered_24)

    <span id="d-guthbered_9"></span>**`guthbered_9`** Guthbered: “Anyway, as I was saying...”

    - Next → [guthbered_10](#d-guthbered_10)

    <span id="d-guthbered_26"></span>**`guthbered_26`** Guthbered: “A man, from the Blackwater mountain settlement, you say?”

    - Next → [guthbered_27](#d-guthbered_27)

    <span id="d-guthbered_23"></span>**`guthbered_23`** Guthbered: “Oh boy, do we? Yes please, you are welcome to help.”

    - “I would be glad to help you with the monsters.” → [guthbered_24](#d-guthbered_24)

    <span id="d-guthbered_24"></span>**`guthbered_24`** Guthbered: “Do you really think you have what it takes to help us?”

    - “I have left a bloody trail of monsters behind me.” → [guthbered_25](#d-guthbered_25)
    - “Sure, I can handle it.” → [guthbered_25](#d-guthbered_25)
    - “If the monsters are anything like those around where I entered the mine, it will be a tough fight. But I can manage it.” → [guthbered_25](#d-guthbered_25)

    <span id="d-guthbered_27"></span>**`guthbered_27`** Guthbered: “Did he say anything about us here in Prim?”

    - “No. But he insisted that I go straight east when exiting the mine, thus not reaching Prim.” → [guthbered_28](#d-guthbered_28)

    <span id="d-guthbered_25"></span>**`guthbered_25`** Guthbered: “Great. I think we should go straight to the source with the problem.”

    - Next → [guthbered_29](#d-guthbered_29)

    <span id="d-guthbered_28"></span>**`guthbered_28`** Guthbered: “That figures. They send out their spies even now.”

    - “Do you need any help in dealing with those monsters?” → [guthbered_23](#d-guthbered_23)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | faction added (fct_prim)<br>Dialogue: 28 lines changed<br>· text: “This is a permit that we have .. produced .. , that according to our …” → “This is a permit that we have ... produced, which according to our so…”<br>· text: “Now, the permit is not .. shall we say .. completely genuine. But we …” → “Now, the permit is not ... shall we say ... completely genuine. But w…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guthbered` |
    | Spawn group | `guthbered` |
    | Loot table | `guthbered` |
    | Conversation | `guthbered_start` |
    | Faction | `fct_prim` |
    | Movement | – |
    | Icon | `monsters_rltiles1:92` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "guthbered",
     "name": "Guthbered",
     "iconID": "monsters_rltiles1:92",
     "maxHP": 80,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 4,
      "max": 9
     },
     "spawnGroup": "guthbered",
     "faction": "fct_prim",
     "phraseID": "guthbered_start",
     "droplistID": "guthbered",
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guthbered.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guthbered.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guthbered.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guthbered.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
