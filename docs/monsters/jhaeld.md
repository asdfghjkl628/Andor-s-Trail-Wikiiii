---
description: "Jhaeld is an NPC you can also fight in Andor's Trail, found in Remgard, Island 4 cave 1, Final cave 1, Final cave 2. Starts What is that stench?."
---

# ![](../assets/icons/monsters/monsters_mage_0.png){ .sprite } Jhaeld

**Where to find Jhaeld:** [Remgard, Remgard tavern 1](#v-jhaeld), [Island 4 cave 1](#v-lae_jhaeld1), [Final cave 1](#v-lae_jhaeld2), [Final cave 2](#v-lae_jhaeld3)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_mage_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Starts [What is that stench?](../quests/remgard2.md) |
| **Found in** | Remgard, Island 4 cave 1, Final cave 1, Final cave 2 |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when defeated** | 258 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Remgard, Remgard tavern 1 { #v-jhaeld }

**Where:** Remgard: [Remgard tavern 1](../maps/remgard_tavern1.md#pin-npc-jhaeld) · **Role:** Starts [What is that stench?](../quests/remgard2.md)

### Quests

- [Everything in order](../quests/remgard.md): stages 40, 50, 51, 52, 53, 54, 59, 75, 80, 110
- [What is that stench?](../quests/remgard2.md): stages 10, 20, 21, 40, 41, 45

### Dialogue simulator

Talk to Jhaeld as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/jhaeld.json" data-npc="Jhaeld" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (81 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-jhaeld-jhaeld"></span>**`jhaeld`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 41 of [The five idols](../quests/fiveidols.md#stage-41))* → [jhaeld_idol_1](#d-jhaeld-jhaeld_idol_1)
    - branch 2 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [jhaeld_completed](#d-jhaeld-jhaeld_completed)
    - branch 3 *(if reached stage 41 of [What is that stench?](../quests/remgard2.md#stage-41))* → [jhaeld_killalg_3](#d-jhaeld-jhaeld_killalg_3)
    - branch 4 *(if reached stage 40 of [What is that stench?](../quests/remgard2.md#stage-40))* → [jhaeld_killalg_2](#d-jhaeld-jhaeld_killalg_2)
    - branch 5 *(if reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21))* → [jhaeld_killalg](#d-jhaeld-jhaeld_killalg)
    - branch 6 *(if reached stage 10 of [What is that stench?](../quests/remgard2.md#stage-10))* → [jhaeld_alg_3](#d-jhaeld-jhaeld_alg_3)
    - branch 7 *(if reached stage 110 of [Everything in order](../quests/remgard.md#stage-110))* → [jhaeld_rejected](#d-jhaeld-jhaeld_rejected)
    - branch 8 *(if reached stage 80 of [Everything in order](../quests/remgard.md#stage-80))* → [jhaeld_return8](#d-jhaeld-jhaeld_return8)
    - branch 9 *(if reached stage 75 of [Everything in order](../quests/remgard.md#stage-75))* → [jhaeld_return6](#d-jhaeld-jhaeld_return6)
    - branch 10 *(if reached stage 50 of [Everything in order](../quests/remgard.md#stage-50))* → [jhaeld_return1](#d-jhaeld-jhaeld_return1)
    - branch 11 → [jhaeld_1](#d-jhaeld-jhaeld_1)

    <span id="d-jhaeld-jhaeld_idol_1"></span>**`jhaeld_idol_1`** Jhaeld: “Please leave me be, child. I just had a sudden attack of nausea. I should probably lie down.”


    <span id="d-jhaeld-jhaeld_completed"></span>**`jhaeld_completed`** Jhaeld: “Again, thank you for all your help.”


    <span id="d-jhaeld-jhaeld_killalg_3"></span>**`jhaeld_killalg_3`** Jhaeld: “This means that the people of Remgard are now safe from her, and it is all thanks to you! Who would have thought.” — **effects:** sets stage 41 of [What is that stench?](../quests/remgard2.md#stage-41)

    - Next → [jhaeld_killalg_4](#d-jhaeld-jhaeld_killalg_4)

    <span id="d-jhaeld-jhaeld_killalg_2"></span>**`jhaeld_killalg_2`** Jhaeld: “You actually defeated her? I am so relieved! Tell me, how crazy was she? No, don't tell me, I don't want to hear more of her filth.”

    - Next → [jhaeld_killalg_3](#d-jhaeld-jhaeld_killalg_3)

    <span id="d-jhaeld-jhaeld_killalg"></span>**`jhaeld_killalg`** Jhaeld: “Hello again. What news do you bring?”

    - “Can you tell me the story of Algangror again?” → [jhaeld_alg_5](#d-jhaeld-jhaeld_alg_5)
    - “I am still trying to find a way to make Algangror disappear.” → [jhaeld_alg_26](#d-jhaeld-jhaeld_alg_26)
    - “Algangror is dead.” *(if reached stage 35 of [What is that stench?](../quests/remgard2.md#stage-35))* → [jhaeld_killalg_1](#d-jhaeld-jhaeld_killalg_1)

    <span id="d-jhaeld-jhaeld_alg_3"></span>**`jhaeld_alg_3`** Jhaeld: “If Algangror is here, this is grim news indeed.” — **effects:** sets stage 10 of [What is that stench?](../quests/remgard2.md#stage-10)

    - Next → [jhaeld_alg_4](#d-jhaeld-jhaeld_alg_4)

    <span id="d-jhaeld-jhaeld_rejected"></span>**`jhaeld_rejected`** Jhaeld: “What now? Look, we don't want kids like you running around here, messing with our things.”

    - Next → [jhaeld_leave](#d-jhaeld-jhaeld_leave)

    <span id="d-jhaeld-jhaeld_return8"></span>**`jhaeld_return8`** Jhaeld: “I suggest you go look in other places if you really want to help us.” — **effects:** sets stage 80 of [Everything in order](../quests/remgard.md#stage-80)

    - Next → [jhaeld_return_s](#d-jhaeld-jhaeld_return_s)

    <span id="d-jhaeld-jhaeld_return6"></span>**`jhaeld_return6`** Jhaeld: “[Jhaeld mumbles] Stupid kids...” — **effects:** sets stage 75 of [Everything in order](../quests/remgard.md#stage-75)

    - Next → [jhaeld_return7](#d-jhaeld-jhaeld_return7)

    <span id="d-jhaeld-jhaeld_return1"></span>**`jhaeld_return1`** Jhaeld: “Did you talk to those people that I sent you to ask about the missing people?”

    - “Yes, I have talked to all of them.” *(if reached stage 70 of [Everything in order](../quests/remgard.md#stage-70))* → [jhaeld_return2](#d-jhaeld-jhaeld_return2)
    - “Can you repeat the names of those that you wanted me to ask?” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “I'm not too sure about this. Will there be a reward?” → [jhaeld_11](#d-jhaeld-jhaeld_11)
    - “I'm not too sure about this. Why would I want to help you people?” → [jhaeld_13](#d-jhaeld-jhaeld_13)
    - “Not yet, but I will.” → [jhaeld_19](#d-jhaeld-jhaeld_19)

    <span id="d-jhaeld-jhaeld_1"></span>**`jhaeld_1`** Jhaeld: “What, who are you? Don't bother me, child. We don't want kids running around in here.”

    - “Are you Jhaeld? I was sent here to help you investigate the missing people.” → [jhaeld_3](#d-jhaeld-jhaeld_3)
    - “Hey, watch that tone of yours. It would be a pity if more of your people would ... disappear.” → [jhaeld_2](#d-jhaeld-jhaeld_2)

    <span id="d-jhaeld-jhaeld_killalg_4"></span>**`jhaeld_killalg_4`** Jhaeld: “I ... I don't know what to say. Thank you, that's the least I can say.”

    - “You are most welcome.” → [jhaeld_killalg_5](#d-jhaeld-jhaeld_killalg_5)
    - “That was a tough fight. Now, let's talk reward.” → [jhaeld_killalg_5](#d-jhaeld-jhaeld_killalg_5)
    - “Just another body behind me.” → [jhaeld_killalg_5](#d-jhaeld-jhaeld_killalg_5)

    <span id="d-jhaeld-jhaeld_alg_5"></span>**`jhaeld_alg_5`** Jhaeld: “She used to live here in Remgard, during the days of prosperity. She even helped with the crops on some days.”

    - Next → [jhaeld_alg_6](#d-jhaeld-jhaeld_alg_6)

    <span id="d-jhaeld-jhaeld_alg_26"></span>**`jhaeld_alg_26`** Jhaeld: “Remember, please be careful! I would not want to be responsible for another person disappearing.” — **effects:** sets stage 21 of [What is that stench?](../quests/remgard2.md#stage-21)


    <span id="d-jhaeld-jhaeld_killalg_1"></span>**`jhaeld_killalg_1`** Jhaeld: “I find this very hard to believe. For you to have killed Algangror would have been a difficult task, given her power.”

    - “I have brought you her ring as proof that what I say is true.” *(if hand over 1× [Algangror's ring](../items/algangror_ring.md))* → [jhaeld_killalg_1b](#d-jhaeld-jhaeld_killalg_1b)
    - “No, never mind. I haven't actually defeated her yet.” → [jhaeld_alg_26](#d-jhaeld-jhaeld_alg_26)

    <span id="d-jhaeld-jhaeld_alg_4"></span>**`jhaeld_alg_4`** Jhaeld: “To be honest, I had heard about this before, but I dismissed all talk of it since I did not believe it. Now you tell me this also, and I am starting to think that it may be true. She may have returned.”

    - “Who is she?” → [jhaeld_alg_5](#d-jhaeld-jhaeld_alg_5)

    <span id="d-jhaeld-jhaeld_leave"></span>**`jhaeld_leave`** Jhaeld: “I think you had better leave, before anything bad might happen to you.”


    <span id="d-jhaeld-jhaeld_return_s"></span>**`jhaeld_return_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [The five idols](../quests/fiveidols.md#stage-20))* → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)
    - branch 2 *(if reached stage 59 of [Everything in order](../quests/remgard.md#stage-59))* → [jhaeld_task2_f](#d-jhaeld-jhaeld_task2_f)
    - branch 3 *(if reached stage 30 of [Everything in order](../quests/remgard.md#stage-30))* → [jhaeld_task2_y](#d-jhaeld-jhaeld_task2_y)
    - branch 4 → [jhaeld_task2](#d-jhaeld-jhaeld_task2)

    <span id="d-jhaeld-jhaeld_return7"></span>**`jhaeld_return7`** Jhaeld: “Fine then.”

    - Next → [jhaeld_return8](#d-jhaeld-jhaeld_return8)

    <span id="d-jhaeld-jhaeld_return2"></span>**`jhaeld_return2`** Jhaeld: “Well, what did you find out?”

    - “Nothing. None of them told me anything new about the missing people.” → [jhaeld_return3](#d-jhaeld-jhaeld_return3)

    <span id="d-jhaeld-jhaeld_14"></span>**`jhaeld_14`** Jhaeld: “There are four people here in Remgard that I believe have more to tell than what we have managed to get out of them. I want you to go ask them what they know of the disappearances.” — **effects:** sets stage 50 of [Everything in order](../quests/remgard.md#stage-50)

    - Next → [jhaeld_15](#d-jhaeld-jhaeld_15)

    <span id="d-jhaeld-jhaeld_11"></span>**`jhaeld_11`** Jhaeld: “What, you have the arrogance to ask for a reward for helping us find the people that are missing? If it's gold you seek, I suggest you look somewhere else.”

    - “Fine, I'll do it. Who do you want me to ask?” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “No reward, no help.” → [jhaeld_12](#d-jhaeld-jhaeld_12)

    <span id="d-jhaeld-jhaeld_13"></span>**`jhaeld_13`** Jhaeld: “Why!? It would be the right thing to do, of course. If you can't understand that, you had better go somewhere else.”

    - “Fine, I'll do it. Who do you want me to ask?” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “I won't do it. I fail to see why I should help you.” → [jhaeld_reject](#d-jhaeld-jhaeld_reject)

    <span id="d-jhaeld-jhaeld_19"></span>**`jhaeld_19`** Jhaeld: “Please be as swift as possible.”

    - “What about that Algangror woman that lives outside town?” *(if reached stage 30 of [Everything in order](../quests/remgard.md#stage-30))* → [jhaeld_21](#d-jhaeld-jhaeld_21)
    - “I'll go ask them.” → [jhaeld_20](#d-jhaeld-jhaeld_20)

    <span id="d-jhaeld-jhaeld_3"></span>**`jhaeld_3`** Jhaeld: “Yes, yes. The missing people. What could possibly a kid like you help with, hm?”

    - “I was thinking you could provide me with some tasks to help you with the investigation.” → [jhaeld_4](#d-jhaeld-jhaeld_4)
    - “The bridge guard told me to talk to you.” → [jhaeld_4](#d-jhaeld-jhaeld_4)

    <span id="d-jhaeld-jhaeld_2"></span>**`jhaeld_2`** Jhaeld: “Hrmpf. I don't take threats lightly. Especially not from snot-nosed kids like you.”

    - “I was sent here to help you investigate the missing people.” → [jhaeld_3](#d-jhaeld-jhaeld_3)
    - “You better get used to it with an attitude like that.” → [jhaeld_leave](#d-jhaeld-jhaeld_leave)

    <span id="d-jhaeld-jhaeld_killalg_5"></span>**`jhaeld_killalg_5`** Jhaeld: “I would think that the whole town is in your debt, but they may not know it.”

    - Next → [jhaeld_killalg_6](#d-jhaeld-jhaeld_killalg_6)

    <span id="d-jhaeld-jhaeld_alg_6"></span>**`jhaeld_alg_6`** Jhaeld: “Then something happened. She started getting ideas, and occasionally locked herself in her house for several days. No one really knew what she was doing in there, but we all knew that she was up to no good.”

    - Next → [jhaeld_alg_7](#d-jhaeld-jhaeld_alg_7)

    <span id="d-jhaeld-jhaeld_killalg_1b"></span>**`jhaeld_killalg_1b`** Jhaeld: “I can hardly believe it! Yes, this is indeed her ring.” — **effects:** sets stage 40 of [What is that stench?](../quests/remgard2.md#stage-40)

    - Next → [jhaeld_killalg_2](#d-jhaeld-jhaeld_killalg_2)

    <span id="d-jhaeld-jhaeld_task2_n"></span>**`jhaeld_task2_n`** Jhaeld: “I have nothing more to say to you.”


    <span id="d-jhaeld-jhaeld_task2_f"></span>**`jhaeld_task2_f`** Jhaeld: “Maybe someone else knows something that we haven't taken into account yet. Also, I seem to recall you saying something about Algangror before, is that right?”

    - “Yes. As I tried to tell you, Algangror is hiding in that abandoned house outside town.” → [jhaeld_alg_3](#d-jhaeld-jhaeld_alg_3)

    <span id="d-jhaeld-jhaeld_task2_y"></span>**`jhaeld_task2_y`** Jhaeld: “Maybe someone else knows something that we haven't taken into account yet.”

    - “The bridge guard sent me to scout an abandoned house outside town.” → [jhaeld_alg_1](#d-jhaeld-jhaeld_alg_1)
    - “Does the name 'Algangror' mean anything to you?” → [jhaeld_alg_2](#d-jhaeld-jhaeld_alg_2)

    <span id="d-jhaeld-jhaeld_task2"></span>**`jhaeld_task2`** Jhaeld: “Maybe someone else knows something that we haven't taken into account yet.”

    - “The bridge guard sent me to scout an abandoned house outside town.” → [jhaeld_alg_1](#d-jhaeld-jhaeld_alg_1)
    - “I might know something, but I have promised not to tell anyone.” *(if reached stage 31 of [Everything in order](../quests/remgard.md#stage-31))* → [jhaeld_task2_1](#d-jhaeld-jhaeld_task2_1)
    - “I don't know anything else.” → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)
    - “I'll go ask around.” → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)

    <span id="d-jhaeld-jhaeld_return3"></span>**`jhaeld_return3`** Jhaeld: “So ... let me get things straight. You went and asked them about the missing people, and they didn't tell you anything new?”

    - “No. None of them had anything new to say.” → [jhaeld_return4](#d-jhaeld-jhaeld_return4)
    - “You heard me the first time.” → [jhaeld_return4](#d-jhaeld-jhaeld_return4)
    - “Maybe you should have sent me to ask other people than these losers you sent me to.” → [jhaeld_return4](#d-jhaeld-jhaeld_return4)

    <span id="d-jhaeld-jhaeld_15"></span>**`jhaeld_15`** Jhaeld: “First, there's Norath and his wife Bethir that lives in the farmhouse on the southwestern shore. Bethir is nowhere to be found, and Norath might know more about where she is.” — **effects:** sets stage 51 of [Everything in order](../quests/remgard.md#stage-51)

    - Next → [jhaeld_16](#d-jhaeld-jhaeld_16)

    <span id="d-jhaeld-jhaeld_12"></span>**`jhaeld_12`** Jhaeld: “I knew you were just trouble. Sigh. Please leave me.”

    - “Fine, I'll do it. Who do you want me to ask?” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “Suit yourself.” → [jhaeld_reject](#d-jhaeld-jhaeld_reject)

    <span id="d-jhaeld-jhaeld_reject"></span>**`jhaeld_reject`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 110 of [Everything in order](../quests/remgard.md#stage-110)

    - branch 1 → [jhaeld_leave](#d-jhaeld-jhaeld_leave)

    <span id="d-jhaeld-jhaeld_21"></span>**`jhaeld_21`** Jhaeld: “What was that? Are you still here? I told you to be as quick as possible.” — **effects:** sets stage 59 of [Everything in order](../quests/remgard.md#stage-59)

    - “What about her? The bridge guard sent me to investigate that house, and seemed very upset when I mentioned that she's…” → [jhaeld_22](#d-jhaeld-jhaeld_22)
    - “I'll go ask those people you mentioned.” → [jhaeld_20](#d-jhaeld-jhaeld_20)

    <span id="d-jhaeld-jhaeld_20"></span>**`jhaeld_20`** Jhaeld: “As I said, please be as quick as possible.”


    <span id="d-jhaeld-jhaeld_4"></span>**`jhaeld_4`** Jhaeld: “Hmm, now that you are here you might as well make yourself useful instead of just standing there looking stupid. Even if you are a kid, you might be able to gather some information for me.”

    - “Sure, what do you need help with?” → [jhaeld_7](#d-jhaeld-jhaeld_7)
    - “Sigh. OK. I guess.” → [jhaeld_7](#d-jhaeld-jhaeld_7)
    - “I'd rather kill something.” → [jhaeld_6](#d-jhaeld-jhaeld_6)
    - “Hey, watch that tone of yours!” → [jhaeld_5](#d-jhaeld-jhaeld_5)

    <span id="d-jhaeld-jhaeld_killalg_6"></span>**`jhaeld_killalg_6`** Jhaeld: “Go talk to Rothses over at the west side of town. He should be able to help you improve some of your equipment.” — **effects:** sets stage 45 of [What is that stench?](../quests/remgard2.md#stage-45)

    - Next → [jhaeld_completed](#d-jhaeld-jhaeld_completed)

    <span id="d-jhaeld-jhaeld_alg_7"></span>**`jhaeld_alg_7`** Jhaeld: “I can still recall the stench that came from her house. Ugh. What could possibly smell that bad?”

    - Next → [jhaeld_alg_8](#d-jhaeld-jhaeld_alg_8)

    <span id="d-jhaeld-jhaeld_alg_1"></span>**`jhaeld_alg_1`** Jhaeld: “Hmm, yes, and what of it?”

    - “I met a woman named Algangror in that house.” → [jhaeld_alg_2](#d-jhaeld-jhaeld_alg_2)

    <span id="d-jhaeld-jhaeld_alg_2"></span>**`jhaeld_alg_2`** Jhaeld: “Algangror?! Now that's a name I have not heard in a long time.”

    - “Algangror is hiding in that abandoned house outside town.” → [jhaeld_alg_3](#d-jhaeld-jhaeld_alg_3)

    <span id="d-jhaeld-jhaeld_task2_1"></span>**`jhaeld_task2_1`** Jhaeld: “A secret, eh? You would do well to tell me what you know. Lives may be at stake here.”

    - “The bridge guard sent me to scout an abandoned house outside town.” → [jhaeld_alg_1](#d-jhaeld-jhaeld_alg_1)
    - “No, I will keep my word and not tell.” → [jhaeld_task2_2](#d-jhaeld-jhaeld_task2_2)
    - “Never mind, it was nothing.” → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)
    - “Never mind, I'll go ask around if anyone else knows anything.” → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)

    <span id="d-jhaeld-jhaeld_return4"></span>**`jhaeld_return4`** Jhaeld: “Oh, I knew you were nothing but trouble the moment I saw you.”

    - Next → [jhaeld_return5](#d-jhaeld-jhaeld_return5)

    <span id="d-jhaeld-jhaeld_16"></span>**`jhaeld_16`** Jhaeld: “Secondly, as you might have heard, we have been blessed by a visit from a delegation of the Knights of Elythom here in Remgard. Unfortunately, one of the knights has vanished, which is most embarrassing for us. They can be found here in…” — **effects:** sets stage 52 of [Everything in order](../quests/remgard.md#stage-52)

    - Next → [jhaeld_17](#d-jhaeld-jhaeld_17)

    <span id="d-jhaeld-jhaeld_22"></span>**`jhaeld_22`** Jhaeld: “Did you not hear me? I told you to be as quick as possible! That means you should go talk to those people instead of standing around here blabbing.”

    - “But the bridge guard seemed...” → [jhaeld_23](#d-jhaeld-jhaeld_23)
    - “But I thought that...” → [jhaeld_23](#d-jhaeld-jhaeld_23)
    - “What about the...” → [jhaeld_23](#d-jhaeld-jhaeld_23)
    - “I'll go ask those people you mentioned.” → [jhaeld_20](#d-jhaeld-jhaeld_20)

    <span id="d-jhaeld-jhaeld_7"></span>**`jhaeld_7`** Jhaeld: “*sigh* To even think that we need to get help from children to run errands now.”

    - Next → [jhaeld_8](#d-jhaeld-jhaeld_8)

    <span id="d-jhaeld-jhaeld_6"></span>**`jhaeld_6`** Jhaeld: “Ha ha. You? Killing something?! Now that's about the funniest thing I have heard all day. Just about.”

    - “Hey, watch that tone of yours!” → [jhaeld_5](#d-jhaeld-jhaeld_5)
    - “I can handle myself. What do you need help with?” → [jhaeld_7](#d-jhaeld-jhaeld_7)
    - “You just wait and see.” → [jhaeld_7](#d-jhaeld-jhaeld_7)

    <span id="d-jhaeld-jhaeld_5"></span>**`jhaeld_5`** Jhaeld: “No, you watch that attitude of yours! Remember where you are and who you are talking to. I am Jhaeld, and you are in Remgard - which could be called *my* city.”

    - “Fine. What do you need help with?” → [jhaeld_7](#d-jhaeld-jhaeld_7)
    - “You don't scare me, old man!” → [jhaeld_leave](#d-jhaeld-jhaeld_leave)

    <span id="d-jhaeld-jhaeld_alg_8"></span>**`jhaeld_alg_8`** Jhaeld: “Anyway, we started questioning her, and tried to persuade her to tell what she was up to. Stubborn and crazy as she is, she refused of course.”

    - Next → [jhaeld_alg_9](#d-jhaeld-jhaeld_alg_9)

    <span id="d-jhaeld-jhaeld_task2_2"></span>**`jhaeld_task2_2`** Jhaeld: “Ah, someone with honor. I respect that, and will not ask any more.”

    - Next → [jhaeld_task2_n](#d-jhaeld-jhaeld_task2_n)

    <span id="d-jhaeld-jhaeld_return5"></span>**`jhaeld_return5`** Jhaeld: “I sent you to do a simple task, and you return with ... nothing!”

    - Next → [jhaeld_return6](#d-jhaeld-jhaeld_return6)

    <span id="d-jhaeld-jhaeld_17"></span>**`jhaeld_17`** Jhaeld: “Third, the old woman Duaina usually has great wisdom to share, considering the experience she has with ... things out of the ordinary. You'll find her in her house to the south.” — **effects:** sets stage 53 of [Everything in order](../quests/remgard.md#stage-53)

    - Next → [jhaeld_18](#d-jhaeld-jhaeld_18)

    <span id="d-jhaeld-jhaeld_23"></span>**`jhaeld_23`** Jhaeld: “Are you still talking? I knew you were nothing but trouble the moment I saw you. Now, can you please hurry up and go talk to those people?”

    - “Fine. I'll go ask them.” → [jhaeld_20](#d-jhaeld-jhaeld_20)

    <span id="d-jhaeld-jhaeld_8"></span>**`jhaeld_8`** Jhaeld: “I guess you know the background to this situation already. We have had some people disappear on us for some time now. We have no idea what has happened to the people that have disappeared, or even if they are still alive.”

    - Next → [jhaeld_9](#d-jhaeld-jhaeld_9)

    <span id="d-jhaeld-jhaeld_alg_9"></span>**`jhaeld_alg_9`** Jhaeld: “Things started getting worse, and the stench spread like a deep fog over the whole town. All of us living here in Remgard knew we had to act before she did something that could hurt us all.”

    - Next → [jhaeld_alg_10](#d-jhaeld-jhaeld_alg_10)

    <span id="d-jhaeld-jhaeld_18"></span>**`jhaeld_18`** Jhaeld: “Lastly, you should go talk to Rothses, the armorer in town. He meets most people now and then, and might have picked up something that he won't dare tell us guards. His house is on the western side of town.” — **effects:** sets stage 54 of [Everything in order](../quests/remgard.md#stage-54)

    - Next → [jhaeld_19](#d-jhaeld-jhaeld_19)

    <span id="d-jhaeld-jhaeld_9"></span>**`jhaeld_9`** Jhaeld: “Considering how many there are that have disappeared without anyone knowing what happened, it doesn't seem like they are out travelling.” — **effects:** sets stage 40 of [Everything in order](../quests/remgard.md#stage-40)

    - Next → [jhaeld_10](#d-jhaeld-jhaeld_10)

    <span id="d-jhaeld-jhaeld_alg_10"></span>**`jhaeld_alg_10`** Jhaeld: “So we forced her to explain herself.”

    - “Did she tell?” → [jhaeld_alg_11](#d-jhaeld-jhaeld_alg_11)

    <span id="d-jhaeld-jhaeld_10"></span>**`jhaeld_10`** Jhaeld: “OK, so what I would like you to do for me is ask some people what they know of the missing people. The fact that you are not from around here might help you get information that neither me nor my guards would be able to acquire.”

    - “Sounds simple enough.” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “Sure, I'll do it. Who do you want me to ask?” → [jhaeld_14](#d-jhaeld-jhaeld_14)
    - “I'm not too sure about this. Will there be a reward?” → [jhaeld_11](#d-jhaeld-jhaeld_11)
    - “I'm not too sure about this. Why would I want to help you people?” → [jhaeld_13](#d-jhaeld-jhaeld_13)

    <span id="d-jhaeld-jhaeld_alg_11"></span>**`jhaeld_alg_11`** Jhaeld: “Would you believe it, she told us that what she believed in, and what she was doing was no concern of ours. She even had the stomach to tell us that she wanted to be left alone.”

    - “What did you do?” → [jhaeld_alg_12](#d-jhaeld-jhaeld_alg_12)

    <span id="d-jhaeld-jhaeld_alg_12"></span>**`jhaeld_alg_12`** Jhaeld: “Of course, we did what any sane man would do. We forced her to abandon her house and find somewhere else to live. Somewhere other than Remgard.”

    - Next → [jhaeld_alg_13](#d-jhaeld-jhaeld_alg_13)

    <span id="d-jhaeld-jhaeld_alg_13"></span>**`jhaeld_alg_13`** Jhaeld: “You should have seen her. Nails long as your finger, and her face full of unwashed hair. Clearly, she was crazy and could not be reasoned with.”

    - Next → [jhaeld_alg_14](#d-jhaeld-jhaeld_alg_14)

    <span id="d-jhaeld-jhaeld_alg_14"></span>**`jhaeld_alg_14`** Jhaeld: “When we marched her out of town, the children started crying out of fear of her.”

    - Next → [jhaeld_alg_15](#d-jhaeld-jhaeld_alg_15)

    <span id="d-jhaeld-jhaeld_alg_15"></span>**`jhaeld_alg_15`** Jhaeld: “The worst thing though, is that she said she would put a curse on all of us.”

    - Next → [jhaeld_alg_16](#d-jhaeld-jhaeld_alg_16)

    <span id="d-jhaeld-jhaeld_alg_16"></span>**`jhaeld_alg_16`** Jhaeld: “All of this was several seasons ago, and things have gone back to the usual business nowadays.”

    - “What now then, since she has returned?” → [jhaeld_alg_17](#d-jhaeld-jhaeld_alg_17)

    <span id="d-jhaeld-jhaeld_alg_17"></span>**`jhaeld_alg_17`** Jhaeld: “Yes. Her being back would explain the missing people. She must have done something to them. I fear for the worst.”

    - Next → [jhaeld_alg_18](#d-jhaeld-jhaeld_alg_18)

    <span id="d-jhaeld-jhaeld_alg_18"></span>**`jhaeld_alg_18`** Jhaeld: “Considering the people that have disappeared, I frankly don't know what to do. As you know, even one of the Knights of Elythom has disappeared.”

    - Next → [jhaeld_alg_19](#d-jhaeld-jhaeld_alg_19)

    <span id="d-jhaeld-jhaeld_alg_19"></span>**`jhaeld_alg_19`** Jhaeld: “Someone that can do that is dangerous indeed. I am not sure I would even risk sending the guards out there for her, in fear of what she might do.”

    - “So, what then?” → [jhaeld_alg_20](#d-jhaeld-jhaeld_alg_20)

    <span id="d-jhaeld-jhaeld_alg_20"></span>**`jhaeld_alg_20`** Jhaeld: “If I were to choose, I would rather not deal with it, and just seal the town bridge as safely as possible, to prevent any more people from disappearing.” — **effects:** sets stage 20 of [What is that stench?](../quests/remgard2.md#stage-20)

    - Next → [jhaeld_alg_21s](#d-jhaeld-jhaeld_alg_21s)

    <span id="d-jhaeld-jhaeld_alg_21s"></span>**`jhaeld_alg_21s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21))* → [jhaeld_alg_21n](#d-jhaeld-jhaeld_alg_21n)
    - branch 2 → [jhaeld_alg_21](#d-jhaeld-jhaeld_alg_21)

    <span id="d-jhaeld-jhaeld_alg_21n"></span>**`jhaeld_alg_21n`** Jhaeld: “I ... I don't know what to do.”


    <span id="d-jhaeld-jhaeld_alg_21"></span>**`jhaeld_alg_21`** Jhaeld: “I ... I don't know what to do.”

    - “I could help you if you want.” → [jhaeld_alg_24](#d-jhaeld-jhaeld_alg_24)
    - “You pathetic fool. You would rather sit here and do nothing instead of confronting her?” → [jhaeld_alg_22](#d-jhaeld-jhaeld_alg_22)
    - “Hah, sucks to be you!” → [jhaeld_alg_23](#d-jhaeld-jhaeld_alg_23)

    <span id="d-jhaeld-jhaeld_alg_24"></span>**`jhaeld_alg_24`** Jhaeld: “If you really want to help us, then please be careful. She can not be trusted.”

    - Next → [jhaeld_alg_25](#d-jhaeld-jhaeld_alg_25)

    <span id="d-jhaeld-jhaeld_alg_22"></span>**`jhaeld_alg_22`** Jhaeld: “I will not see more of my people get hurt, or whatever it is she has done to them. I will keep my people safe.”

    - “I could help you if you want.” → [jhaeld_alg_24](#d-jhaeld-jhaeld_alg_24)
    - “Hah, sucks to be you!” → [jhaeld_alg_23](#d-jhaeld-jhaeld_alg_23)

    <span id="d-jhaeld-jhaeld_alg_23"></span>**`jhaeld_alg_23`** Jhaeld: “Insults won't get you anywhere. The people that have disappeared are still missing, and may be hurt, while you run around handing out insults. I pity you.”

    - “I could help you if you want.” → [jhaeld_alg_24](#d-jhaeld-jhaeld_alg_24)
    - “You pathetic fool. You would rather sit here and do nothing instead of confronting her?” → [jhaeld_alg_22](#d-jhaeld-jhaeld_alg_22)

    <span id="d-jhaeld-jhaeld_alg_25"></span>**`jhaeld_alg_25`** Jhaeld: “However, if you were to find a way to make her disappear, we would of course be forever in your debt.”

    - “I'll see what I can do.” → [jhaeld_alg_26](#d-jhaeld-jhaeld_alg_26)
    - “I have dealt with stronger foes.” → [jhaeld_alg_27](#d-jhaeld-jhaeld_alg_27)

    <span id="d-jhaeld-jhaeld_alg_27"></span>**`jhaeld_alg_27`** Jhaeld: “I doubt it.”

    - Next → [jhaeld_alg_26](#d-jhaeld-jhaeld_alg_26)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 20 lines changed<br>· text: “(Sigh) To even think that we need to get help from children to run er…” → “*sigh* To even think that we need to get help from children to run er…”<br>· text: “I.. I don't know what to do.” → “I ... I don't know what to do.” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “I find this very hard to believe. For to have killed Algangror would …” → “I find this very hard to believe. For you to have killed Algangror wo…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Island 4 cave 1 { #v-lae_jhaeld1 }

**Where:** [Island 4 cave 1](../maps/island_4_cave1.md#pin-npc-lae_jhaeld1)

### Quests

- [Not Pony Island](../quests/lae_centaurs.md): stages 112, 120
- [Final cave (hidden flag)](../quests/final_cave.md): stage 12

### Dialogue simulator

Talk to Jhaeld as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_jhaeld1.json" data-npc="Jhaeld" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_jhaeld1-lae_jhaeld1"></span>**`lae_jhaeld1`** Jhaeld: “$playername - good that you are here! I need your help urgently.” — **effects:** sets stage 112 of [Not Pony Island](../quests/lae_centaurs.md#stage-112)

    - “Why? Don't coming around on your own anymore?” → [lae_algangror1_20](#d-lae_jhaeld1-lae_algangror1_20)

    <span id="d-lae_jhaeld1-lae_algangror1_20"></span>**`lae_algangror1_20`** Jhaeld: “A friend of mine is captured, here, deep in the cave.”

    - Next → [lae_algangror1_22](#d-lae_jhaeld1-lae_algangror1_22)

    <span id="d-lae_jhaeld1-lae_algangror1_22"></span>**`lae_algangror1_22`** Jhaeld: “You know him very well by the way. We have to help him!” — **effects:** sets stage 120 of [Not Pony Island](../quests/lae_centaurs.md#stage-120)

    - “Of course I'm happy to help.” → [lae_algangror1_30](#d-lae_jhaeld1-lae_algangror1_30)
    - “Who is this friend?” → [lae_algangror1_30](#d-lae_jhaeld1-lae_algangror1_30)

    <span id="d-lae_jhaeld1-lae_algangror1_30"></span>**`lae_algangror1_30`** Jhaeld: “To free him I would need to go for some items all over the isle. But these nasty centaurs wouldn't let me.” — **effects:** sets stage 12 of [Final cave (hidden flag)](../quests/final_cave.md#stage-12)

    - “Well, first I am going downstairs to talk to our friend and find out who he is.” → [lae_algangror1_40](#d-lae_jhaeld1-lae_algangror1_40)

    <span id="d-lae_jhaeld1-lae_algangror1_40"></span>**`lae_algangror1_40`** Jhaeld: “Do that. But hurry.”




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Final cave 1 { #v-lae_jhaeld2 }

**Where:** [Final cave 1](../maps/final_cave1.md#pin-npc-lae_jhaeld2)

### Quests

- [Not Pony Island](../quests/lae_centaurs.md): stage 170

### Dialogue simulator

Talk to Jhaeld as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_algangror2.json" data-npc="Jhaeld" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_jhaeld2-lae_algangror2"></span>**`lae_algangror2`** Jhaeld: “$playername, what have you done?”

    - Next → [lae_algangror2_10](#d-lae_jhaeld2-lae_algangror2_10)

    <span id="d-lae_jhaeld2-lae_algangror2_10"></span>**`lae_algangror2_10`** Jhaeld: “Now we are all locked in here! We will all starve to death!”

    - Next → [lae_algangror2_20](#d-lae_jhaeld2-lae_algangror2_20)

    <span id="d-lae_jhaeld2-lae_algangror2_20"></span>**`lae_algangror2_20`** Jhaeld: “It is all your fault!”

    - “Hey - I did nothing!” → [lae_algangror2_30](#d-lae_jhaeld2-lae_algangror2_30)

    <span id="d-lae_jhaeld2-lae_algangror2_30"></span>**`lae_algangror2_30`** Jhaeld: “Our only chance of survival lies in that stairway over there.”

    - “What is down there?” → [lae_algangror2_50](#d-lae_jhaeld2-lae_algangror2_50)
    - “You didn't try it yourself yet?” → [lae_algangror2_50](#d-lae_jhaeld2-lae_algangror2_50)
    - “Why did all that gold disappear for a few moments?” → [lae_algangror2_32](#d-lae_jhaeld2-lae_algangror2_32)

    <span id="d-lae_jhaeld2-lae_algangror2_50"></span>**`lae_algangror2_50`** Jhaeld: “We can't use those stairs. Some invisible force holds us back. But maybe you can do it?” — **effects:** sets stage 170 of [Not Pony Island](../quests/lae_centaurs.md#stage-170)

    - “OK you weaklings - I'll show you.” → *conversation ends*
    - “Well, I could at least try.” → *conversation ends*

    <span id="d-lae_jhaeld2-lae_algangror2_32"></span>**`lae_algangror2_32`** Jhaeld: “Did it? You must have dreamed that.”

    - “If you say so.” → [lae_algangror2_30](#d-lae_jhaeld2-lae_algangror2_30)
    - “Hmm ...” → [lae_algangror2_30](#d-lae_jhaeld2-lae_algangror2_30)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Final cave 2 { #v-lae_jhaeld3 }

**Where:** [Final cave 2](../maps/final_cave2.md#pin-npc-lae_jhaeld3)

!!! warning "You can fight Jhaeld"
    Answering “The same that I'll do to you now.” starts a fight with Jhaeld.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 258 |
| Damage | 10 to 22 |
| AC | 70 |
| BC | 50 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Scroll of fire](../items/final_cave_f.md) | 100% | 1 |

### Quests

- [Not Pony Island](../quests/lae_centaurs.md): stage 200

### Dialogue simulator

Talk to Jhaeld as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_algangror3.json" data-npc="Jhaeld" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (15 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_jhaeld3-lae_algangror3"></span>**`lae_algangror3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Dorhantarh](../monsters/lae_island_boss.md))* → [lae_algangror3_100](#d-lae_jhaeld3-lae_algangror3_100)
    - branch 2 *(if reached stage 200 of [Not Pony Island](../quests/lae_centaurs.md#stage-200))* → [lae_algangror3_40](#d-lae_jhaeld3-lae_algangror3_40)
    - branch 3 → [lae_algangror3_10](#d-lae_jhaeld3-lae_algangror3_10)

    <span id="d-lae_jhaeld3-lae_algangror3_100"></span>**`lae_algangror3_100`** Jhaeld: “NO! What have you done to our master?!”

    - “The same that I'll do to you now.” → *fight starts*

    <span id="d-lae_jhaeld3-lae_algangror3_40"></span>**`lae_algangror3_40`** Jhaeld: “Now go ahead, you'll be a tasty dinner for our master Dorhantarh tonight.” — **effects:** sets stage 200 of [Not Pony Island](../quests/lae_centaurs.md#stage-200)

    - Next → [lae_algangror3_42](#d-lae_jhaeld3-lae_algangror3_42)

    <span id="d-lae_jhaeld3-lae_algangror3_10"></span>**`lae_algangror3_10`** Jhaeld: “Surprised to see me here?”

    - Next → [lae_algangror3_12](#d-lae_jhaeld3-lae_algangror3_12)

    <span id="d-lae_jhaeld3-lae_algangror3_42"></span>**`lae_algangror3_42`** Jhaeld: “You're so speechless. Hahaha! Go now.”

    - “Well wait - attack!” → [lae_algangror3_50](#d-lae_jhaeld3-lae_algangror3_50)

    <span id="d-lae_jhaeld3-lae_algangror3_12"></span>**`lae_algangror3_12`** Jhaeld: “You should see your face! Hahaha!”

    - Next → [lae_algangror3_20](#d-lae_jhaeld3-lae_algangror3_20)

    <span id="d-lae_jhaeld3-lae_algangror3_50"></span>**`lae_algangror3_50`** Jhaeld: “No no no. It is not proper to draw a weapon in the presence of our Master.”


    <span id="d-lae_jhaeld3-lae_algangror3_20"></span>**`lae_algangror3_20`** Jhaeld: “Of course we are not what you think you see. Ever heard of posers? You were great, that was really fun.”

    - Next → [lae_algangror3_22](#d-lae_jhaeld3-lae_algangror3_22)

    <span id="d-lae_jhaeld3-lae_algangror3_22"></span>**`lae_algangror3_22`** Jhaeld: “Even the many gold is all fake. We had a lot of fun decorating this ugly room as a treasure trove.”

    - Next → [lae_algangror3_24](#d-lae_jhaeld3-lae_algangror3_24)

    <span id="d-lae_jhaeld3-lae_algangror3_24"></span>**`lae_algangror3_24`** Jhaeld: “Making rocks look like piles of gold and stuff like that.”

    - “And the walls? The element scrolls and the globes?” → [lae_algangror3_26](#d-lae_jhaeld3-lae_algangror3_26)

    <span id="d-lae_jhaeld3-lae_algangror3_26"></span>**`lae_algangror3_26`** Jhaeld: “The point of all this was just to lure you down here to our master Dorhantarh without you becoming suspicious.”

    - Next → [lae_algangror3_28](#d-lae_jhaeld3-lae_algangror3_28)

    <span id="d-lae_jhaeld3-lae_algangror3_28"></span>**`lae_algangror3_28`** Jhaeld: “So it couldn't be too easy for you. That's why I came up with the idea of the scrolls and glass balls.”

    - “Does that mean this complex mechanism doesn't work at all?” → [lae_algangror3_30](#d-lae_jhaeld3-lae_algangror3_30)

    <span id="d-lae_jhaeld3-lae_algangror3_30"></span>**`lae_algangror3_30`** Jhaeld: “Oh yes, of course it works. Why do you think the wall closed again?”

    - “Yes, why did it?” → [lae_algangror3_32](#d-lae_jhaeld3-lae_algangror3_32)

    <span id="d-lae_jhaeld3-lae_algangror3_32"></span>**`lae_algangror3_32`** Jhaeld: “Well, because I brought a scroll from the table here with me. That's why.”

    - “What?! You ...” → [lae_algangror3_34](#d-lae_jhaeld3-lae_algangror3_34)

    <span id="d-lae_jhaeld3-lae_algangror3_34"></span>**`lae_algangror3_34`** Jhaeld: “Hahaha!”

    - Next → [lae_algangror3_40](#d-lae_jhaeld3-lae_algangror3_40)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 15 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**4 entries.** The game data defines 4 separate characters named Jhaeld. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `jhaeld` | NPC | [Remgard, Remgard tavern 1](#v-jhaeld) |
| `lae_jhaeld1` | NPC | [Island 4 cave 1](#v-lae_jhaeld1) |
| `lae_jhaeld2` | NPC | [Final cave 1](#v-lae_jhaeld2) |
| `lae_jhaeld3` | NPC/Enemy | [Final cave 2](#v-lae_jhaeld3) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: jhaeld"

    | | |
    |---|---|
    | Entry ID | `jhaeld` |
    | Type (wiki) | NPC |
    | Spawn group | `jhaeld` |
    | Loot table | – |
    | Conversation | `jhaeld` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "jhaeld",
     "name": "Jhaeld",
     "iconID": "monsters_mage:0",
     "monsterClass": "humanoid",
     "spawnGroup": "jhaeld",
     "phraseID": "jhaeld"
    }
    ```

??? info "Technical information: lae_jhaeld1"

    | | |
    |---|---|
    | Entry ID | `lae_jhaeld1` |
    | Type (wiki) | NPC |
    | Spawn group | `lae_jhaeld1` |
    | Loot table | – |
    | Conversation | `lae_jhaeld1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_jhaeld1",
     "name": "Jhaeld",
     "iconID": "monsters_mage:0",
     "monsterClass": "humanoid",
     "spawnGroup": "lae_jhaeld1",
     "phraseID": "lae_jhaeld1"
    }
    ```

??? info "Technical information: lae_jhaeld2"

    | | |
    |---|---|
    | Entry ID | `lae_jhaeld2` |
    | Type (wiki) | NPC |
    | Spawn group | `lae_jhaeld2` |
    | Loot table | – |
    | Conversation | `lae_algangror2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_jhaeld2",
     "name": "Jhaeld",
     "iconID": "monsters_mage:0",
     "monsterClass": "humanoid",
     "spawnGroup": "lae_jhaeld2",
     "phraseID": "lae_algangror2"
    }
    ```

??? info "Technical information: lae_jhaeld3"

    | | |
    |---|---|
    | Entry ID | `lae_jhaeld3` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `lae_jhaeld3` |
    | Loot table | `lae_algangror3` |
    | Conversation | `lae_algangror3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage:0` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_jhaeld3",
     "name": "Jhaeld",
     "iconID": "monsters_mage:0",
     "maxHP": 200,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 22
     },
     "spawnGroup": "lae_jhaeld3",
     "phraseID": "lae_algangror3",
     "droplistID": "lae_algangror3",
     "attackCost": 4,
     "attackChance": 70,
     "blockChance": 50
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jhaeld.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jhaeld.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jhaeld.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jhaeld.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
