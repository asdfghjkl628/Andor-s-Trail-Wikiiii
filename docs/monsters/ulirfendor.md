---
description: "Ulirfendor is an NPC who can also be fought in Andor's Trail, found in Waytobrimhavencave 4. Teaches Dark blessing of the Shadow; starts An involuntary carrier."
---

# ![](../assets/icons/monsters/monsters_rltiles1_84.png){ .sprite } Ulirfendor

**Where to find Ulirfendor:** [Waytobrimhavencave 4](../maps/waytobrimhavencave4.md#pin-npc-ulirfendor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_84.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Teaches [Dark blessing of the Shadow](../skills/shadowBless.md); starts [An involuntary carrier](../quests/toszylae.md) |
| **Found in** | Waytobrimhavencave 4 |
| **Class** | Humanoid |
| **HP** | 288 |
| **XP when defeated** | 421 |
| **Entry ID** | `ulirfendor` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 288 |
| XP when defeated | 421 |
| Damage | 1 to 16 |
| Attack chance | 70 |
| Block chance | 60 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 2.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 50 |
| [Iron club](../items/club3.md) | 100% | 1 |
| [Minor vial of health](../items/health_minor.md) | 100% | 1 to 2 |
| [Empty vial](../items/vial_empty2.md) | 100% | 3 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytobrimhavencave 4](../maps/waytobrimhavencave4.md) | – | 1 | – |

## Quests

- [An involuntary carrier](../quests/toszylae.md): stages 10, 11, 15, 30, 32, 60, 70
- [I have it in me](../quests/maggots.md): stages 20, 21
- [The dark protector](../quests/darkprotector.md): stages 15, 26, 30, 31, 35, 40, 41, 50, 51

## Dialogue simulator

Set your quest stages and items, then talk to Ulirfendor. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ulirfendor.json" data-npc="Ulirfendor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (114 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ulirfendor"></span>**`ulirfendor`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [The dark protector](../quests/darkprotector.md#stage-40))* → [ulirfendor_dp_bless_6](#d-ulirfendor_dp_bless_6)
    - branch 2 *(if reached stage 41 of [The dark protector](../quests/darkprotector.md#stage-41))* → [ulirfendor_dp_bless_6](#d-ulirfendor_dp_bless_6)
    - branch 3 *(if reached stage 51 of [The dark protector](../quests/darkprotector.md#stage-51))* → [ulirfendor_helmet_keep3](#d-ulirfendor_helmet_keep3)
    - branch 4 *(if reached stage 50 of [The dark protector](../quests/darkprotector.md#stage-50))* → [ulirfendor_helmet_keep2](#d-ulirfendor_helmet_keep2)
    - branch 5 *(if reached stage 35 of [The dark protector](../quests/darkprotector.md#stage-35))* → [ulirfendor_dp_proc_16](#d-ulirfendor_dp_proc_16)
    - branch 6 *(if reached stage 31 of [The dark protector](../quests/darkprotector.md#stage-31))* → [ulirfendor_dp_proc_3](#d-ulirfendor_dp_proc_3)
    - branch 7 *(if reached stage 15 of [The dark protector](../quests/darkprotector.md#stage-15))* → [ulirfendor_dp_return1](#d-ulirfendor_dp_return1)
    - branch 8 *(if reached stage 50 of [I have it in me](../quests/maggots.md#stage-50))* → [ulirfendor_cured_1](#d-ulirfendor_cured_1)
    - branch 9 *(if reached stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60))* → [ulirfendor_infected_8](#d-ulirfendor_infected_8)
    - branch 10 *(if reached stage 50 of [An involuntary carrier](../quests/toszylae.md#stage-50))* → [ulirfendor_infected_1](#d-ulirfendor_infected_1)
    - branch 11 *(if reached stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32))* → [ulirfendor_findparts_10](#d-ulirfendor_findparts_10)
    - branch 12 *(if reached stage 30 of [An involuntary carrier](../quests/toszylae.md#stage-30))* → [ulirfendor_findparts_6](#d-ulirfendor_findparts_6)
    - branch 13 *(if reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15))* → [ulirfendor_findparts_1](#d-ulirfendor_findparts_1)
    - branch 14 *(if reached stage 10 of [An involuntary carrier](../quests/toszylae.md#stage-10))* → [ulirfendor_4](#d-ulirfendor_4)
    - branch 15 → [ulirfendor_1](#d-ulirfendor_1)

    <span id="d-ulirfendor_dp_bless_6"></span>**`ulirfendor_dp_bless_6`** Ulirfendor: “Thank you yet again for all you have done here.”


    <span id="d-ulirfendor_helmet_keep3"></span>**`ulirfendor_helmet_keep3`** Ulirfendor: “By the Shadow, I will stop you. Whatever it takes. You will not live to see the next day!” — **effects:** sets stage 51 of [The dark protector](../quests/darkprotector.md#stage-51)

    - “Attack!” → *fight starts*

    <span id="d-ulirfendor_helmet_keep2"></span>**`ulirfendor_helmet_keep2`** Ulirfendor: “What is this!? I knew there was something wrong about you the first time I saw you.” — **effects:** sets stage 50 of [The dark protector](../quests/darkprotector.md#stage-50)

    - Next → [ulirfendor_helmet_keep3](#d-ulirfendor_helmet_keep3)

    <span id="d-ulirfendor_dp_proc_16"></span>**`ulirfendor_dp_proc_16`** Ulirfendor: “You, my friend, have done a great deed here today. This thing would have brought great misery if it would have fallen into the wrong hands.”

    - Next → [ulirfendor_dp_proc_17](#d-ulirfendor_dp_proc_17)

    <span id="d-ulirfendor_dp_proc_3"></span>**`ulirfendor_dp_proc_3`** Ulirfendor: “[Ulirfendor places the helmet and the lich's heart on the ground before him, and opens his backpack of items]”

    - Next → [ulirfendor_dp_proc_4](#d-ulirfendor_dp_proc_4)

    <span id="d-ulirfendor_dp_return1"></span>**`ulirfendor_dp_return1`** Ulirfendor: “Hello again. Have you made up your mind about what we talked about before?”

    - “What was that about destroying the helmet?” → [ulirfendor_helmet_8](#d-ulirfendor_helmet_8)
    - “Can you tell me again what you think about this helmet?” → [ulirfendor_helmet_2](#d-ulirfendor_helmet_2)

    <span id="d-ulirfendor_cured_1"></span>**`ulirfendor_cured_1`** Ulirfendor: “I am glad to see that you are looking better than before. I assume you got the help you needed from Talion in Loneford?”

    - “Yes, Talion cured me of that thing.” → [ulirfendor_cured_2](#d-ulirfendor_cured_2)

    <span id="d-ulirfendor_infected_8"></span>**`ulirfendor_infected_8`** Ulirfendor: “Oh, what have I done? I made you say it, and now you are touched by its vile essence.” — **effects:** sets stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60)

    - “It's not that bad. I have had worse.” → [ulirfendor_infected_9](#d-ulirfendor_infected_9)
    - “What can I do to get rid of this affliction?” → [ulirfendor_infected_9](#d-ulirfendor_infected_9)
    - “You better have a plan for how you should repay me for this trickery!” → [ulirfendor_infected_9](#d-ulirfendor_infected_9)
    - “I at least defeated the lich that infected me with this thing.” *(if reached stage 10 of [The dark protector](../quests/darkprotector.md#stage-10))* → [ulirfendor_demon_s](#d-ulirfendor_demon_s)
    - “I found a strange looking helmet among the remains of the lich that I defeated. Do you know anything about it?” *(if reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70))* → [ulirfendor_helmet_s](#d-ulirfendor_helmet_s)

    <span id="d-ulirfendor_infected_1"></span>**`ulirfendor_infected_1`** Ulirfendor: “[Ulirfendor gives you a terrified look]”

    - Next → [ulirfendor_infected_2](#d-ulirfendor_infected_2)

    <span id="d-ulirfendor_findparts_10"></span>**`ulirfendor_findparts_10`** Ulirfendor: “Hello again. Did you speak those words to the creature you encountered?”

    - “What was I supposed to do again?” → [ulirfendor_findparts_6](#d-ulirfendor_findparts_6)
    - “Can you repeat the words I was supposed to speak to the guardian?” → [ulirfendor_findparts_11](#d-ulirfendor_findparts_11)
    - “No, not yet. But I am working on it.” → [ulirfendor_findparts_9](#d-ulirfendor_findparts_9)
    - “Yes, it is done.” *(if reached stage 42 of [An involuntary carrier](../quests/toszylae.md#stage-42))* → [ulirfendor_findparts_12](#d-ulirfendor_findparts_12)

    <span id="d-ulirfendor_findparts_6"></span>**`ulirfendor_findparts_6`** Ulirfendor: “I wonder what this whole piece means. 'Kulauil hamar urum Kazaul'te. Kazaul hamat urul' - that's the part you heard the creature speak.”

    - Next → [ulirfendor_findparts_7](#d-ulirfendor_findparts_7)

    <span id="d-ulirfendor_findparts_1"></span>**`ulirfendor_findparts_1`** Ulirfendor: “Hello again. Did you find any clues about what the missing parts are?”

    - “No, I have not found any clues yet.” → [ulirfendor_findparts_2](#d-ulirfendor_findparts_2)
    - “Can you tell me again what you have translated from the shrine?” → [ulirfendor_5_1](#d-ulirfendor_5_1)
    - “Yes, I encountered a creature to the east that spoke the words you told me.” *(if reached stage 20 of [An involuntary carrier](../quests/toszylae.md#stage-20))* → [ulirfendor_findparts_3](#d-ulirfendor_findparts_3)

    <span id="d-ulirfendor_4"></span>**`ulirfendor_4`** Ulirfendor: “Oh, how long have I been down here? I can't remember.”

    - Next → [ulirfendor_5](#d-ulirfendor_5)

    <span id="d-ulirfendor_1"></span>**`ulirfendor_1`** Ulirfendor: “No! Stay away! You shall not defeat me!”

    - Next → [ulirfendor_2](#d-ulirfendor_2)

    <span id="d-ulirfendor_dp_proc_17"></span>**`ulirfendor_dp_proc_17`** Ulirfendor: “The people of the surrounding towns are now safe from whatever misery that helmet would have brought. All thanks to you!”

    - Next → [ulirfendor_dp_proc_18](#d-ulirfendor_dp_proc_18)

    <span id="d-ulirfendor_dp_proc_4"></span>**`ulirfendor_dp_proc_4`** Ulirfendor: “[He pulls out a leathery potion case from his backpack, and takes out a vial of clear but almost shining liquid]”

    - Next → [ulirfendor_dp_proc_5](#d-ulirfendor_dp_proc_5)

    <span id="d-ulirfendor_helmet_8"></span>**`ulirfendor_helmet_8`** Ulirfendor: “I say, we must destroy that item immediately to make sure that the Kazaul taint is forever cleansed from this place and to make sure it does not fall into the wrong hands.” — **effects:** sets stage 15 of [The dark protector](../quests/darkprotector.md#stage-15)

    - “He he, a powerful item you say? How much would you think it is worth?” → [ulirfendor_helmet_worth](#d-ulirfendor_helmet_worth)
    - “What should we do in order to destroy it?” → [ulirfendor_helmet_n2](#d-ulirfendor_helmet_n2)
    - “Absolutely. I will do anything to protect the people from this thing.” → [ulirfendor_helmet_n1](#d-ulirfendor_helmet_n1)
    - “Interesting. How powerful could someone become by wearing this thing?” → [ulirfendor_helmet_power](#d-ulirfendor_helmet_power)

    <span id="d-ulirfendor_helmet_2"></span>**`ulirfendor_helmet_2`** Ulirfendor: “Those markings on it are most peculiar. It was found by the lich that you spoke of?”

    - Next → [ulirfendor_helmet_3](#d-ulirfendor_helmet_3)

    <span id="d-ulirfendor_cured_2"></span>**`ulirfendor_cured_2`** Ulirfendor: “That's good to hear. I hope that ... thing ... didn't have any permanent side-effects on you.”

    - “I defeated the lich in the depths of the eastern cave.” *(if reached stage 10 of [The dark protector](../quests/darkprotector.md#stage-10))* → [ulirfendor_demon_s](#d-ulirfendor_demon_s)
    - “I found a strange looking helmet among the remains of that lich. Do you know anything about it?” *(if reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70))* → [ulirfendor_helmet_s](#d-ulirfendor_helmet_s)

    <span id="d-ulirfendor_infected_9"></span>**`ulirfendor_infected_9`** Ulirfendor: “Let me have a look at you.”

    - Next → [ulirfendor_infected_10](#d-ulirfendor_infected_10)

    <span id="d-ulirfendor_demon_s"></span>**`ulirfendor_demon_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70))* → [ulirfendor_demon_1](#d-ulirfendor_demon_1)
    - branch 2 → [ulirfendor_demon_d1](#d-ulirfendor_demon_d1)

    <span id="d-ulirfendor_helmet_s"></span>**`ulirfendor_helmet_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [I have it in me](../quests/maggots.md#stage-50))* → [ulirfendor_helmet_1](#d-ulirfendor_helmet_1)
    - branch 2 → [ulirfendor_helmet_d1](#d-ulirfendor_helmet_d1)

    <span id="d-ulirfendor_infected_2"></span>**`ulirfendor_infected_2`** Ulirfendor: “You are back! Please tell me you are well! Please tell me nothing happened to you!”

    - Next → [ulirfendor_infected_3](#d-ulirfendor_infected_3)

    <span id="d-ulirfendor_findparts_11"></span>**`ulirfendor_findparts_11`** Ulirfendor: “Sure. It's 'Klatam ur turum Kazaul'te'.”


    <span id="d-ulirfendor_findparts_9"></span>**`ulirfendor_findparts_9`** Ulirfendor: “Good. Please return as soon as possible.” — **effects:** sets stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32)


    <span id="d-ulirfendor_findparts_12"></span>**`ulirfendor_findparts_12`** Ulirfendor: “So, did anything happen?”

    - “The creature started attacking me.” → [ulirfendor_findparts_13](#d-ulirfendor_findparts_13)
    - “No, nothing happened.” → [ulirfendor_findparts_13](#d-ulirfendor_findparts_13)

    <span id="d-ulirfendor_findparts_7"></span>**`ulirfendor_findparts_7`** Ulirfendor: “The next part is 'Klatam ur turum Kazaul'te', and I am not sure what that means. Something about handing over some item?”

    - Next → [ulirfendor_findparts_8](#d-ulirfendor_findparts_8)

    <span id="d-ulirfendor_findparts_2"></span>**`ulirfendor_findparts_2`** Ulirfendor: “If you really want to help, then please go look for any other clues you might find.”

    - Next → [ulirfendor_21](#d-ulirfendor_21)

    <span id="d-ulirfendor_5_1"></span>**`ulirfendor_5_1`** Ulirfendor: “If my understanding is correct, this shrine is a remnant of Kazaul.”

    - Next → [ulirfendor_6](#d-ulirfendor_6)

    <span id="d-ulirfendor_findparts_3"></span>**`ulirfendor_findparts_3`** Ulirfendor: “Oh good, tell me, did you find any more clues?”

    - “Yes, the creature also spoke the words 'Kazaul hamat urul', maybe that is part of the missing piece?” → [ulirfendor_findparts_4](#d-ulirfendor_findparts_4)

    <span id="d-ulirfendor_5"></span>**`ulirfendor_5`** Ulirfendor: “No matter. I must finish my work here. You see this shrine here?”

    - Next → [ulirfendor_5_1](#d-ulirfendor_5_1)

    <span id="d-ulirfendor_2"></span>**`ulirfendor_2`** Ulirfendor: “Oh wait, you are not one of them. You ... you are not one of those spawns.”

    - “Relax, I am not here to hurt you.” → [ulirfendor_4](#d-ulirfendor_4)
    - “What's going on here?” → [ulirfendor_4](#d-ulirfendor_4)
    - “Who are you?” → [ulirfendor_4](#d-ulirfendor_4)

    <span id="d-ulirfendor_dp_proc_18"></span>**`ulirfendor_dp_proc_18`** Ulirfendor: “As a token of my appreciation, I am willing to grant upon you a blessing of the Shadow.”

    - “What would the blessing do?” → [ulirfendor_dp_bless_2](#d-ulirfendor_dp_bless_2)
    - “Thank you, but that will not be necessary. I am just happy to help.” → [ulirfendor_dp_bless_1](#d-ulirfendor_dp_bless_1)
    - “Thank you, please go ahead.” → [ulirfendor_dp_bless_3](#d-ulirfendor_dp_bless_3)

    <span id="d-ulirfendor_dp_proc_5"></span>**`ulirfendor_dp_proc_5`** Ulirfendor: “[Ulirfendor pours the contents of the vial on the helmet and the heart in circling motions, taking good care to not spill any on the ground]”

    - Next → [ulirfendor_dp_proc_6](#d-ulirfendor_dp_proc_6)

    <span id="d-ulirfendor_helmet_worth"></span>**`ulirfendor_helmet_worth`** Ulirfendor: “Worth!? What difference would that make? We need to destroy it immediately!”

    - “How powerful could someone become by wearing this thing?” → [ulirfendor_helmet_power](#d-ulirfendor_helmet_power)
    - “What should we do in order to destroy it?” → [ulirfendor_helmet_n2](#d-ulirfendor_helmet_n2)
    - “No. I will keep this item for myself instead.” → [ulirfendor_helmet_keep1](#d-ulirfendor_helmet_keep1)

    <span id="d-ulirfendor_helmet_n2"></span>**`ulirfendor_helmet_n2`** Ulirfendor: “To destroy it, I think it will suffice to use what we normally use when removing the taint of Kazaul - a vial of purifying spirit.”

    - Next → [ulirfendor_helmet_n3](#d-ulirfendor_helmet_n3)

    <span id="d-ulirfendor_helmet_n1"></span>**`ulirfendor_helmet_n1`** Ulirfendor: “I'm glad to hear that.”

    - Next → [ulirfendor_helmet_n2](#d-ulirfendor_helmet_n2)

    <span id="d-ulirfendor_helmet_power"></span>**`ulirfendor_helmet_power`** Ulirfendor: “I don't even want to think about that. It would surely bring misery to the surroundings of whoever wears it. We must destroy it immediately!”

    - “He he, sounds powerful. How much would you think it is worth?” → [ulirfendor_helmet_worth](#d-ulirfendor_helmet_worth)
    - “What should we do in order to destroy it?” → [ulirfendor_helmet_n2](#d-ulirfendor_helmet_n2)
    - “No. I will keep this item for myself instead.” → [ulirfendor_helmet_keep1](#d-ulirfendor_helmet_keep1)

    <span id="d-ulirfendor_helmet_3"></span>**`ulirfendor_helmet_3`** Ulirfendor: “Hmm. You know what, this could actually be connected to what the shrine speaks of - The Dark Protector.”

    - Next → [ulirfendor_helmet_4](#d-ulirfendor_helmet_4)

    <span id="d-ulirfendor_infected_10"></span>**`ulirfendor_infected_10`** Ulirfendor: “No ... can it be? Are they actually real?”

    - “What is?” → [ulirfendor_infected_11](#d-ulirfendor_infected_11)

    <span id="d-ulirfendor_demon_1"></span>**`ulirfendor_demon_1`** Ulirfendor: “Yes, you told me that you killed the lich. Excellent work.”

    - Next → [ulirfendor_demon_2](#d-ulirfendor_demon_2)

    <span id="d-ulirfendor_demon_d1"></span>**`ulirfendor_demon_d1`** Ulirfendor: “Oh, that is good news indeed. A lich you say? With your help, the people of the surrounding towns should be safe from whatever mischief the lich could have caused now.” — **effects:** sets stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70)

    - Next → [ulirfendor_demon_d2](#d-ulirfendor_demon_d2)

    <span id="d-ulirfendor_helmet_1"></span>**`ulirfendor_helmet_1`** Ulirfendor: “Could it be? Hmm. Let me look at that thing.”

    - Next → [ulirfendor_helmet_2](#d-ulirfendor_helmet_2)

    <span id="d-ulirfendor_helmet_d1"></span>**`ulirfendor_helmet_d1`** Ulirfendor: “That is most interesting, but you seem to have more pressing matters to attend to.”

    - Next → [ulirfendor_infected_17](#d-ulirfendor_infected_17)

    <span id="d-ulirfendor_infected_3"></span>**`ulirfendor_infected_3`** Ulirfendor: “I managed to translate the piece that we spoke about. Oh, what have I done. Please, tell me you are well!”

    - “No, I am not well. My stomach is turning and I feel weaker than usual. I encountered a lich down there that did…” → [ulirfendor_infected_4](#d-ulirfendor_infected_4)

    <span id="d-ulirfendor_findparts_13"></span>**`ulirfendor_findparts_13`** Ulirfendor: “Well, you should probably investigate that area some more. I am sure there are more clues in there about what this shrine speaks of.”


    <span id="d-ulirfendor_findparts_8"></span>**`ulirfendor_findparts_8`** Ulirfendor: “Maybe the creature you encountered responds to that phrase if you speak to it? If you want to help, you could go and try speaking that phrase to it.”

    - “Sure, I will go speak those words to the creature.” → [ulirfendor_findparts_9](#d-ulirfendor_findparts_9)
    - “Whatever, I'll do it, but I hope this is the last time that I have to run back and forth!” → [ulirfendor_findparts_9](#d-ulirfendor_findparts_9)
    - “No way, I have helped you enough now.” → [ulirfendor_decline](#d-ulirfendor_decline)
    - “I had better not get involved in this.” → [ulirfendor_decline](#d-ulirfendor_decline)

    <span id="d-ulirfendor_21"></span>**`ulirfendor_21`** Ulirfendor: “I have looked thoroughly for any clues in the western part of this cave, but have not found any. I have not entered the eastern parts of the cave however.”

    - Next → [ulirfendor_22](#d-ulirfendor_22)

    <span id="d-ulirfendor_6"></span>**`ulirfendor_6`** Ulirfendor: “The writings on it have almost vanished, but I have managed to read parts of it. It speaks in an ancient Kazaul tongue, so all parts are not clear to me.”

    - Next → [ulirfendor_7](#d-ulirfendor_7)

    <span id="d-ulirfendor_findparts_4"></span>**`ulirfendor_findparts_4`** Ulirfendor: “Hmm ... 'hamat urul' ... yes of course! That's what it says on the eroded parts of the shrine!”

    - Next → [ulirfendor_findparts_5](#d-ulirfendor_findparts_5)

    <span id="d-ulirfendor_dp_bless_2"></span>**`ulirfendor_dp_bless_2`** Ulirfendor: “The blessing will grant you the aid of the Shadow while in combat, protecting you from harmful effects that your opponent might inflict upon you.”

    - “Thank you, but that will not be necessary. I am just happy to help.” → [ulirfendor_dp_bless_1](#d-ulirfendor_dp_bless_1)
    - “Thank you, please go ahead.” → [ulirfendor_dp_bless_3](#d-ulirfendor_dp_bless_3)

    <span id="d-ulirfendor_dp_bless_1"></span>**`ulirfendor_dp_bless_1`** Ulirfendor: “You truly have a large heart.” — **effects:** sets stage 41 of [The dark protector](../quests/darkprotector.md#stage-41)

    - Next → [ulirfendor_dp_bless_6](#d-ulirfendor_dp_bless_6)

    <span id="d-ulirfendor_dp_bless_3"></span>**`ulirfendor_dp_bless_3`** Ulirfendor: “Very well, I will give you the dark blessing of the Shadow.”

    - Next → [ulirfendor_dp_bless_4](#d-ulirfendor_dp_bless_4)

    <span id="d-ulirfendor_dp_proc_6"></span>**`ulirfendor_dp_proc_6`** Ulirfendor: “It should be as simple as that really. Powerful stuff this.”

    - Next → [ulirfendor_dp_proc_7](#d-ulirfendor_dp_proc_7)

    <span id="d-ulirfendor_helmet_keep1"></span>**`ulirfendor_helmet_keep1`** Ulirfendor: “What!? Keep it!? Have you gone mad? We need to destroy it to protect the people!”

    - “Who knows what power I could gain from it? I will keep this for myself.” → [ulirfendor_helmet_keep2](#d-ulirfendor_helmet_keep2)
    - “It could be worth a lot. I will keep this for myself.” → [ulirfendor_helmet_keep2](#d-ulirfendor_helmet_keep2)
    - “I think I should give this a second thought before we begin.” → [ulirfendor_helmet_n8](#d-ulirfendor_helmet_n8)

    <span id="d-ulirfendor_helmet_n3"></span>**`ulirfendor_helmet_n3`** Ulirfendor: “Fortunately, I always carry some on me, so that won't be a problem.”

    - Next → [ulirfendor_helmet_n4](#d-ulirfendor_helmet_n4)

    <span id="d-ulirfendor_helmet_4"></span>**`ulirfendor_helmet_4`** Ulirfendor: “I am not certain of what the term 'The Dark Protector' refers to. At first I thought it might be some creature protecting something, but this helmet seems to better fit what the shrine speaks of.”

    - Next → [ulirfendor_helmet_5](#d-ulirfendor_helmet_5)

    <span id="d-ulirfendor_infected_11"></span>**`ulirfendor_infected_11`** Ulirfendor: “You show all the signs. If this is true, then you are in great danger.”

    - Next → [ulirfendor_infected_12](#d-ulirfendor_infected_12)

    <span id="d-ulirfendor_demon_2"></span>**`ulirfendor_demon_2`** Ulirfendor: “The people of the surrounding towns will have you to thank.”

    - “No problem. Goodbye.” → *conversation ends*
    - “I found a strange looking helmet among the remains of that lich. Do you know anything about it?” *(if reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70))* → [ulirfendor_helmet_s](#d-ulirfendor_helmet_s)

    <span id="d-ulirfendor_demon_d2"></span>**`ulirfendor_demon_d2`** Ulirfendor: “Thank you so much for your help!”

    - Next → [ulirfendor_demon_2](#d-ulirfendor_demon_2)

    <span id="d-ulirfendor_infected_17"></span>**`ulirfendor_infected_17`** Ulirfendor: “You should hurry and seek help from one of the priests of the Shadow as quickly as possible. My dear friend Talion in the temple of Loneford should be able to help you.” — **effects:** sets stage 21 of [I have it in me](../quests/maggots.md#stage-21)

    - Next → [ulirfendor_infected_18_s](#d-ulirfendor_infected_18_s)

    <span id="d-ulirfendor_infected_4"></span>**`ulirfendor_infected_4`** Ulirfendor: “Nooo! What have I done?”

    - Next → [ulirfendor_infected_5](#d-ulirfendor_infected_5)

    <span id="d-ulirfendor_decline"></span>**`ulirfendor_decline`** Ulirfendor: “No matter, I will find out myself then. Thank you for your help so far. Goodbye.”


    <span id="d-ulirfendor_22"></span>**`ulirfendor_22`** Ulirfendor: “Also, I should warn you that I believe the shrine talks of a powerful creature somewhere in this cave. Maybe if you find that creature, it will provide some clue as to what the missing parts are? You need to be careful though.” — **effects:** sets stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15)

    - “I will go look in the eastern parts of the cave then.” → [ulirfendor_bye](#d-ulirfendor_bye)

    <span id="d-ulirfendor_7"></span>**`ulirfendor_7`** Ulirfendor: “I am sure that this shrine is part of the cause for these ... these ... things ... that lurk in this cave. I will do anything in my power to defeat whatever mischief that comes from it.”

    - “What are these creatures?” → [ulirfendor_8](#d-ulirfendor_8)
    - “How come these creatures do not attack you?” → [ulirfendor_10](#d-ulirfendor_10)
    - “What have you translated so far?” → [ulirfendor_12](#d-ulirfendor_12)

    <span id="d-ulirfendor_findparts_5"></span>**`ulirfendor_findparts_5`** Ulirfendor: “Excellent work my friend! Now I just need to translate it.” — **effects:** sets stage 30 of [An involuntary carrier](../quests/toszylae.md#stage-30)

    - Next → [ulirfendor_findparts_6](#d-ulirfendor_findparts_6)

    <span id="d-ulirfendor_dp_bless_4"></span>**`ulirfendor_dp_bless_4`** Ulirfendor: “[Ulirfendor starts chanting in a tongue that you do not recognize]”

    - Next → [ulirfendor_dp_bless_5](#d-ulirfendor_dp_bless_5)

    <span id="d-ulirfendor_dp_proc_7"></span>**`ulirfendor_dp_proc_7`** Ulirfendor: “[The surface of the helmet seems to freeze, almost like it had a layer of ice on it]”

    - Next → [ulirfendor_dp_proc_8](#d-ulirfendor_dp_proc_8)

    <span id="d-ulirfendor_helmet_n8"></span>**`ulirfendor_helmet_n8`** Ulirfendor: “Think all you want, but please hurry. We need to destroy this thing as soon as possible!”


    <span id="d-ulirfendor_helmet_n4"></span>**`ulirfendor_helmet_n4`** Ulirfendor: “What could be a problem however, is the other thing we will need. This artifact is most likely connected to that lich you encountered.”

    - Next → [ulirfendor_helmet_n5](#d-ulirfendor_helmet_n5)

    <span id="d-ulirfendor_helmet_5"></span>**`ulirfendor_helmet_5`** Ulirfendor: “It could either be the helmet itself, or that the helmet has some effect on whoever wears it, meaning that the wearer will become the Dark Protector.”

    - Next → [ulirfendor_helmet_6](#d-ulirfendor_helmet_6)

    <span id="d-ulirfendor_infected_12"></span>**`ulirfendor_infected_12`** Ulirfendor: “Long ago, I read a book on Kazaul rituals. The first part of one particular ritual I read about talks about 'the carrier', that supposedly is infected with Kazaul rotworms.”

    - Next → [ulirfendor_infected_13](#d-ulirfendor_infected_13)

    <span id="d-ulirfendor_infected_18_s"></span>**`ulirfendor_infected_18_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70))* → [ulirfendor_infected_18](#d-ulirfendor_infected_18)
    - branch 2 → [ulirfendor_infected_19](#d-ulirfendor_infected_19)

    <span id="d-ulirfendor_infected_5"></span>**`ulirfendor_infected_5`** Ulirfendor: “You see, while you were away, I managed to translate the words that we spoke about before.”

    - Next → [ulirfendor_infected_6](#d-ulirfendor_infected_6)

    <span id="d-ulirfendor_bye"></span>**`ulirfendor_bye`** Ulirfendor: “Thank you. Goodbye.”


    <span id="d-ulirfendor_8"></span>**`ulirfendor_8`** Ulirfendor: “Ah, the allaceph. I had not seen one for many years until I entered this cave. They are a remnant of the guardians of Kazaul.”

    - Next → [ulirfendor_9](#d-ulirfendor_9)

    <span id="d-ulirfendor_10"></span>**`ulirfendor_10`** Ulirfendor: “I have placed a blessing of the Shadow upon this small island here, so that I may work uninterrupted. Strangely enough, it seems to be very effective on them.”

    - Next → [ulirfendor_11](#d-ulirfendor_11)

    <span id="d-ulirfendor_12"></span>**`ulirfendor_12`** Ulirfendor: “It speaks of Kazaul and of the misery that comes to anyone that opposes the will of Kazaul.”

    - Next → [ulirfendor_13](#d-ulirfendor_13)

    <span id="d-ulirfendor_dp_bless_5"></span>**`ulirfendor_dp_bless_5`** Ulirfendor: “There. You now have the dark blessing of the Shadow upon you.” — **effects:** sets stage 40 of [The dark protector](../quests/darkprotector.md#stage-40), +1 [Dark blessing of the Shadow](../skills/shadowBless.md)

    - Next → [ulirfendor_dp_bless_6](#d-ulirfendor_dp_bless_6)

    <span id="d-ulirfendor_dp_proc_8"></span>**`ulirfendor_dp_proc_8`** Ulirfendor: “[After a while, small cracks appear on the surface, making tiny sounds as they appear]”

    - Next → [ulirfendor_dp_proc_9](#d-ulirfendor_dp_proc_9)

    <span id="d-ulirfendor_helmet_n5"></span>**`ulirfendor_helmet_n5`** Ulirfendor: “We would need to use the vial of purifying spirit on something powerful from that lich as well.”

    - “I managed to get the heart of the lich, would that do?” → [ulirfendor_helmet_n6](#d-ulirfendor_helmet_n6)

    <span id="d-ulirfendor_helmet_6"></span>**`ulirfendor_helmet_6`** Ulirfendor: “Nevertheless, I am almost certain that this artifact is connected to what this shrine speaks of, and that the artifact is rich with Kazaul influence.”

    - Next → [ulirfendor_helmet_7](#d-ulirfendor_helmet_7)

    <span id="d-ulirfendor_infected_13"></span>**`ulirfendor_infected_13`** Ulirfendor: “The Kazaul rotworms need a living being to feed upon, before their eggs can hatch. Their eggs can slowly kill a person from the inside, and the worms themselves cause the carrier to become weak during the whole process.”

    - Next → [ulirfendor_infected_14](#d-ulirfendor_infected_14)

    <span id="d-ulirfendor_infected_18"></span>**`ulirfendor_infected_18`** Ulirfendor: “Seek him out immediately. Hurry! You might not have much time.”

    - “OK, I will go to Talion in the Loneford temple at once. Goodbye.” → *conversation ends*

    <span id="d-ulirfendor_infected_19"></span>**`ulirfendor_infected_19`** Ulirfendor: “I should also tell you that it is of great importance that you first destroy whatever creature that infected you with this.”

    - “OK, I will defeat the lich first. Goodbye.” → *conversation ends*
    - “I defeated the lich in the depths of the eastern cave.” *(if reached stage 10 of [The dark protector](../quests/darkprotector.md#stage-10))* → [ulirfendor_demon_s](#d-ulirfendor_demon_s)

    <span id="d-ulirfendor_infected_6"></span>**`ulirfendor_infected_6`** Ulirfendor: “The part that the creature spoke basically means 'No offering is worthy for Kazaul'.”

    - Next → [ulirfendor_infected_7](#d-ulirfendor_infected_7)

    <span id="d-ulirfendor_9"></span>**`ulirfendor_9`** Ulirfendor: “Have you noticed how they seem to feed upon whoever tries to fight them? Cursed things, almost got a hold of me, they did.”

    - “How come these creatures do not attack you?” → [ulirfendor_10](#d-ulirfendor_10)
    - “What have you translated from the shrine so far?” → [ulirfendor_12](#d-ulirfendor_12)

    <span id="d-ulirfendor_11"></span>**`ulirfendor_11`** Ulirfendor: “They seem to be very cautious about it. So far, not even one has dared to approach me. Even those pesky lizards are keeping their distance.”

    - “What are these creatures?” → [ulirfendor_8](#d-ulirfendor_8)
    - “What have you translated from the shrine so far?” → [ulirfendor_12](#d-ulirfendor_12)

    <span id="d-ulirfendor_13"></span>**`ulirfendor_13`** Ulirfendor: “Something about 're-birth from within the followers'. Not sure I have translated that part correctly, but I think that is what it says. Definitely something about re-birth or birth.”

    - Next → [ulirfendor_14](#d-ulirfendor_14)

    <span id="d-ulirfendor_dp_proc_9"></span>**`ulirfendor_dp_proc_9`** Ulirfendor: “[The cracks start to get larger and more dense along the surface, until the helmet is completely covered by them]”

    - Next → [ulirfendor_dp_proc_10](#d-ulirfendor_dp_proc_10)

    <span id="d-ulirfendor_helmet_n6"></span>**`ulirfendor_helmet_n6`** Ulirfendor: “The heart? Oh yes, that would surely do.” — **effects:** sets stage 26 of [The dark protector](../quests/darkprotector.md#stage-26)

    - Next → [ulirfendor_helmet_n7](#d-ulirfendor_helmet_n7)

    <span id="d-ulirfendor_helmet_7"></span>**`ulirfendor_helmet_7`** Ulirfendor: “As such, it would most certainly bring misery to the surroundings of whoever carries it. Directly or indirectly, I do not know.”

    - Next → [ulirfendor_helmet_8](#d-ulirfendor_helmet_8)

    <span id="d-ulirfendor_infected_14"></span>**`ulirfendor_infected_14`** Ulirfendor: “The ritual proceeds with the carrier being eaten from the inside by the rotworms and their eggs, in effect, giving birth to the creatures within. Also, the process can have ... shall we say ... unusual effects on the carrier before that.”

    - Next → [ulirfendor_infected_15](#d-ulirfendor_infected_15)

    <span id="d-ulirfendor_infected_7"></span>**`ulirfendor_infected_7`** Ulirfendor: “Furthermore, the last part, that I made you speak to the creature, 'Klatam ur turum Kazaul'te', means 'My body for Kazaul'.”

    - Next → [ulirfendor_infected_8](#d-ulirfendor_infected_8)

    <span id="d-ulirfendor_14"></span>**`ulirfendor_14`** Ulirfendor: “It also speaks of someone or some ... thing called the 'Dark protector'. Most parts of the text for that is missing from the shrine however.”

    - Next → [ulirfendor_15](#d-ulirfendor_15)

    <span id="d-ulirfendor_dp_proc_10"></span>**`ulirfendor_dp_proc_10`** Ulirfendor: “Now, watch this. I love this part.”

    - Next → [ulirfendor_dp_proc_11](#d-ulirfendor_dp_proc_11)

    <span id="d-ulirfendor_helmet_n7"></span>**`ulirfendor_helmet_n7`** Ulirfendor: “Quickly now, give me the helmet and the heart of the lich, and I will begin the procedure.”

    - “Here is the helmet and the heart.” *(if hand over 1× [Strange looking helmet](../items/helm_protector0.md); hand over 1× [Demon heart](../items/toszylae_heart.md))* → [ulirfendor_dp_proc_2](#d-ulirfendor_dp_proc_2)
    - “I think I should give this a second thought before we begin.” → [ulirfendor_helmet_n8](#d-ulirfendor_helmet_n8)
    - “No. I will keep this item for myself instead.” → [ulirfendor_helmet_keep1](#d-ulirfendor_helmet_keep1)

    <span id="d-ulirfendor_infected_15"></span>**`ulirfendor_infected_15`** Ulirfendor: “Needless to say, you are in great danger, and you should seek help immediately.” — **effects:** sets stage 20 of [I have it in me](../quests/maggots.md#stage-20)

    - Next → [ulirfendor_infected_17](#d-ulirfendor_infected_17)

    <span id="d-ulirfendor_15"></span>**`ulirfendor_15`** Ulirfendor: “Whatever it means, it seems important. It is also obvious that the 'Dark protector' brings power to Kazaul, and misery to any opposition.”

    - Next → [ulirfendor_16](#d-ulirfendor_16)

    <span id="d-ulirfendor_dp_proc_11"></span>**`ulirfendor_dp_proc_11`** Ulirfendor: “[Ulirfendor takes aim with his foot and stomps the helmet with the heel of his boot in a powerful motion]”

    - Next → [ulirfendor_dp_proc_12](#d-ulirfendor_dp_proc_12)

    <span id="d-ulirfendor_dp_proc_2"></span>**`ulirfendor_dp_proc_2`** Ulirfendor: “Excellent. I will begin the procedure immediately.” — **effects:** sets stage 30 of [The dark protector](../quests/darkprotector.md#stage-30), sets stage 31 of [The dark protector](../quests/darkprotector.md#stage-31)

    - Next → [ulirfendor_dp_proc_3](#d-ulirfendor_dp_proc_3)

    <span id="d-ulirfendor_16"></span>**`ulirfendor_16`** Ulirfendor: “Regardless, it must be stopped, whatever it means. Maybe it refers to something deeper down this cave? I have not ventured further into the cave to the east since I could not get past those ... things.” — **effects:** sets stage 10 of [An involuntary carrier](../quests/toszylae.md#stage-10)

    - Next → [ulirfendor_16_1](#d-ulirfendor_16_1)

    <span id="d-ulirfendor_dp_proc_12"></span>**`ulirfendor_dp_proc_12`** Ulirfendor: “[The helmet completely shatters, leaving nothing but a fine dust]” — **effects:** sets stage 35 of [The dark protector](../quests/darkprotector.md#stage-35)

    - Next → [ulirfendor_dp_proc_13](#d-ulirfendor_dp_proc_13)

    <span id="d-ulirfendor_16_1"></span>**`ulirfendor_16_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15))* → [ulirfendor_19](#d-ulirfendor_19)
    - branch 2 → [ulirfendor_17](#d-ulirfendor_17)

    <span id="d-ulirfendor_dp_proc_13"></span>**`ulirfendor_dp_proc_13`** Ulirfendor: “Ha ha! Look at that!”

    - Next → [ulirfendor_dp_proc_14](#d-ulirfendor_dp_proc_14)

    <span id="d-ulirfendor_19"></span>**`ulirfendor_19`** Ulirfendor: “The last part of this piece has been eroded from the rock. It begins with 'Kulauil hamar urum Kazaul'te'. But what is the rest of that?” — **effects:** sets stage 11 of [An involuntary carrier](../quests/toszylae.md#stage-11)

    - Next → [ulirfendor_19_1](#d-ulirfendor_19_1)

    <span id="d-ulirfendor_17"></span>**`ulirfendor_17`** Ulirfendor: “Forgive me, I must continue translating the few readable parts left on this shrine.”

    - “Would you like any help with that?” → [ulirfendor_18](#d-ulirfendor_18)
    - “Well, good luck with that.” → [ulirfendor_bye](#d-ulirfendor_bye)

    <span id="d-ulirfendor_dp_proc_14"></span>**`ulirfendor_dp_proc_14`** Ulirfendor: “[He does the same with the heart that also seems to have completely frozen and gotten covered with cracks]”

    - Next → [ulirfendor_dp_proc_15](#d-ulirfendor_dp_proc_15)

    <span id="d-ulirfendor_19_1"></span>**`ulirfendor_19_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15))* → [ulirfendor_21](#d-ulirfendor_21)
    - branch 2 → [ulirfendor_19_2](#d-ulirfendor_19_2)

    <span id="d-ulirfendor_18"></span>**`ulirfendor_18`** Ulirfendor: “Hmm, maybe. I need to figure out what this last part should be. Hmm...”

    - Next → [ulirfendor_19](#d-ulirfendor_19)

    <span id="d-ulirfendor_dp_proc_15"></span>**`ulirfendor_dp_proc_15`** Ulirfendor: “Ah, that sure felt good.”

    - Next → [ulirfendor_dp_proc_16](#d-ulirfendor_dp_proc_16)

    <span id="d-ulirfendor_19_2"></span>**`ulirfendor_19_2`** Ulirfendor: “Argh, if this cave wasn't so damp, I bet the rest of the text would still be there.”

    - “I could go look for other clues about the missing parts if you want?” → [ulirfendor_20](#d-ulirfendor_20)
    - “Good luck with that, goodbye.” → [ulirfendor_bye](#d-ulirfendor_bye)

    <span id="d-ulirfendor_20"></span>**`ulirfendor_20`** Ulirfendor: “Sure, you do that.”

    - Next → [ulirfendor_21](#d-ulirfendor_21)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 34 lines changed<br>· text: “Oh wait, you are not one of them. You.. you are not one of those spaw…” → “Oh wait, you are not one of them. You ... you are not one of those sp…”<br>· text: “(Ulirfendor pours the contents of the vial on the helmet and the hear…” → “[Ulirfendor pours the contents of the vial on the helmet and the hear…” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines changed<br>· text: “The blessing will grant you the aid of the Shadow while in combat, pr…” → “The blessing will grant you the aid of the Shadow while in combat, pr…”<br>· text: “I am not certain of what the term 'The Dark Protector' refers to. At …” → “I am not certain of what the term 'The Dark Protector' refers to. At …” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “Hmm. You know what, this could actually be connected to what the shri…” → “Hmm. You know what, this could actually be connected to what the shri…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ulirfendor` |
    | Spawn group | `ulirfendor` |
    | Loot table | `ulirfendor` |
    | Conversation | `ulirfendor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:84` |
    | Defined in | `res/raw/monsterlist_v0611_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "ulirfendor",
     "name": "Ulirfendor",
     "iconID": "monsters_rltiles1:84",
     "maxHP": 288,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 16
     },
     "spawnGroup": "ulirfendor",
     "phraseID": "ulirfendor",
     "droplistID": "ulirfendor",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 30,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "damageResistance": 6
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ulirfendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ulirfendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ulirfendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ulirfendor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
