---
description: "Umar is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Starts A lost potion, Another ruthless Crackshot, Immaculate kidnapping, The ruthless Crackshot +2."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Umar

**Where to find Umar:** Fallhaven: [fallhaven_derelict2](../maps/fallhaven_derelict2.md#pin-npc-umar), Fallhaven: [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md#pin-npc-umar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [A lost potion](../quests/lodar.md), [Another ruthless Crackshot](../quests/Thieves04.md), [Immaculate kidnapping](../quests/Thieves02.md), [The ruthless Crackshot](../quests/Thieves03.md) +2 |
| **Found in** | Fallhaven |
| **Entry ID** | `umar` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fallhaven_derelict2](../maps/fallhaven_derelict2.md) | Fallhaven | 1 | – |
| [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) | Fallhaven | 1 | – |

## Quests

- [A lost potion](../quests/lodar.md): stages 10, 15
- [Another ruthless Crackshot](../quests/Thieves04.md): stages 10, 30, 40, 60, 70, 80
- [Immaculate kidnapping](../quests/Thieves02.md): stages 2, 4, 6, 30, 35, 40, 75, 76
- [Search for Andor](../quests/andor.md): stages 51, 55
- [The ruthless Crackshot](../quests/Thieves03.md): stages 1, 4, 5, 10, 45, 50
- [Thief apprentice](../quests/Thieves01.md): stages 5, 10
- [Troubling times](../quests/troubling_times.md): stages 10, 20, 30, 120
- [misc_nondisplay (hidden flag)](../quests/misc_nondisplay.md): stage 20
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stage 28

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Umar. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/umar_select_1.json" data-npc="Umar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (150 lines+)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-umar_select_1"></span>**`umar_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Wanted men](../quests/wanted_men.md#stage-70))* → [nanath_10](#d-nanath_10)
    - branch 2 *(if reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80))* → [nanath_12](#d-nanath_12)
    - branch 3 *(if reached stage 115 of [Troubling times](../quests/troubling_times.md#stage-115); NOT reached stage 120 of [Troubling times](../quests/troubling_times.md#stage-120))* → [umar_tt_100](#d-umar_tt_100)
    - branch 4 *(if reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); NOT reached stage 70 of [Wanted men](../quests/wanted_men.md#stage-70))* → [umar_tt](#d-umar_tt)
    - branch 5 *(if reached stage 51 of [Search for Andor](../quests/andor.md#stage-51))* → [umar_return_1](#d-umar_return_1)
    - branch 6 → [umar_novisit_1](#d-umar_novisit_1)

    <span id="d-nanath_10"></span>**`nanath_10`** Umar: “You? How dare you show your face?” — **effects:** sets stage 10 of [Troubling times](../quests/troubling_times.md#stage-10), sets stage 20 of [Troubling times](../quests/troubling_times.md#stage-20)

    - “Why?” → [nanath_18](#d-nanath_18)

    <span id="d-nanath_12"></span>**`nanath_12`** Umar: “You? How dare you show your face?” — **effects:** sets stage 10 of [Troubling times](../quests/troubling_times.md#stage-10), sets stage 30 of [Troubling times](../quests/troubling_times.md#stage-30)

    - “Why?” → [nanath_18](#d-nanath_18)

    <span id="d-umar_tt_100"></span>**`umar_tt_100`** Umar: “$playername, didn't I make it clear that I didn't want to be disturbed?”

    - “Yes, I'm sorry too. But we need your help.” → [umar_tt_102](#d-umar_tt_102)

    <span id="d-umar_tt"></span>**`umar_tt`** Umar: “Hello $playername, good that you are here. Please talk to Nanath, I am really busy right now.”

    - “Wait ...” → [umar_return_1](#d-umar_return_1)
    - “OK, I'll go find Nanath.” → *conversation ends*

    <span id="d-umar_return_1"></span>**`umar_return_1`** Umar: “Hello again, my friend.”

    - “Do you have any tasks for me?” *(if faction “ThievesGuild” ≥ 40)* → [umar_guild05_0](#d-umar_guild05_0)
    - “I have given them our promised share.” *(if NOT reached stage 80 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-80); reached stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30))* → [umar_guild04_29](#d-umar_guild04_29)
    - “What are we gonna do about Sullengard?” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70) is 70; NOT reached stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30))* → [umar_guild04_26](#d-umar_guild04_26)
    - “What are your plans for the new traitors?” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-60) is 60)* → [umar_guild04_21](#d-umar_guild04_21)
    - “Matpat told me that Defy and his men left Sullengard.” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-50) is 50)* → [umar_guild04_19](#d-umar_guild04_19)
    - “Defy and his men have left Sullengard.” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-35) is 35)* → [umar_guild04_17](#d-umar_guild04_17)
    - “Defy told me that the time to share will be delayed for no stated reason.” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-20) is 20)* → [umar_guild04_15](#d-umar_guild04_15)
    - “What am I supposed to do in Sullengard again?” *(if latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10)* → [umar_guild04_12](#d-umar_guild04_12)
    - “Do you have any tasks for me?” *(if faction “ThievesGuild” ≥ 30; NOT reached stage 10 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10))* → [umar_guild04_0](#d-umar_guild04_0)
    - “Are you going to tell me about the key?” *(if reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); NOT reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50))* → [umar_guild03_27c](#d-umar_guild03_27c)
    - “Crackshot is dead.” *(if reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40); NOT reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45))* → [umar_guild03_25](#d-umar_guild03_25)
    - “What am I supposed to do again?” *(if reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40))* → [umar_guild03_20](#d-umar_guild03_20)
    - “What are your plans for the traitors?” *(if reached stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5); NOT reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10))* → [umar_guild03_14](#d-umar_guild03_14)
    - “Can you continue with what you were telling me about the traitors?” *(if reached stage 4 of [The ruthless Crackshot](../quests/Thieves03.md#stage-4); NOT reached stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5))* → [umar_guild03_10c](#d-umar_guild03_10c)
    - “We are supposed to talk about something.” *(if reached stage 3 of [The ruthless Crackshot](../quests/Thieves03.md#stage-3); NOT reached stage 4 of [The ruthless Crackshot](../quests/Thieves03.md#stage-4))* → [umar_guild03_1](#d-umar_guild03_1)
    - “We were supposed to talk about something, right?” *(if reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76); NOT reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75); NOT reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1))* → [umar_guild02_26](#d-umar_guild02_26)
    - “We were supposed to talk about something, right?” *(if reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75); NOT reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1))* → [umar_guild02_26](#d-umar_guild02_26)
    - “I've finally finished the job.” *(if NOT latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-75) is 75; reached stage 70 of [Immaculate kidnapping](../quests/Thieves02.md#stage-70))* → [umar_guild02_22](#d-umar_guild02_22)
    - “What am I suppossed to do again?” *(if reached stage 40 of [Immaculate kidnapping](../quests/Thieves02.md#stage-40); NOT reached stage 45 of [Immaculate kidnapping](../quests/Thieves02.md#stage-45))* → [umar_guild02_21](#d-umar_guild02_21)
    - “What am I supposed to do with the noblewoman?” *(if reached stage 35 of [Immaculate kidnapping](../quests/Thieves02.md#stage-35); NOT reached stage 40 of [Immaculate kidnapping](../quests/Thieves02.md#stage-40))* → [umar_guild02_20](#d-umar_guild02_20)
    - “What am I supposed to do with the noblewoman?” *(if reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 35 of [Immaculate kidnapping](../quests/Thieves02.md#stage-35))* → [umar_guild02_19](#d-umar_guild02_19)
    - “I have to talk to you about the noblewoman.” *(if reached stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24); reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21); NOT reached stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20); NOT reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76))* → [umar_guild02_28](#d-umar_guild02_28)
    - “I have brought the hostage.” *(if reached stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20); NOT reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21); NOT reached stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24))* → [umar_guild02_16](#d-umar_guild02_16)
    - “Anything more about my new task?” *(if reached stage 6 of [Immaculate kidnapping](../quests/Thieves02.md#stage-6); NOT reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15))* → [umar_guild02_15](#d-umar_guild02_15)
    - “Anything more about my new task?” *(if latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2; NOT reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4))* → [umar_guild02_10](#d-umar_guild02_10)
    - “Anything more about my new task?” *(if latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-4) is 4; NOT reached stage 6 of [Immaculate kidnapping](../quests/Thieves02.md#stage-6); NOT reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15))* → [umar_guild02_13](#d-umar_guild02_13)
    - “Troublemaker sent me. I have finished the job.” *(if latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; NOT reached stage 2 of [Immaculate kidnapping](../quests/Thieves02.md#stage-2))* → [umar_guild02_1](#d-umar_guild02_1)
    - “Hello.” → [umar_return_2](#d-umar_return_2)
    - “Nice to meet you. Goodbye.” → *conversation ends*

    <span id="d-umar_novisit_1"></span>**`umar_novisit_1`** Umar: “Hello. How did your search go?”

    - “What search?” → [umar_2](#d-umar_2)

    <span id="d-nanath_18"></span>**`nanath_18`** Umar: “You betrayed the Guild over the task with Defy. Get out!”


    <span id="d-umar_tt_102"></span>**`umar_tt_102`** Umar: “[Muttering to himself] Tu quoque, mi fili? Sigh.”

    - “To break the spell, we need King Luthor's ring. Sly is the only one who knows where it is. But she refuses to cooperate.” → [umar_tt_110](#d-umar_tt_110)

    <span id="d-umar_guild05_0"></span>**`umar_guild05_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100); reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50))* → [umar_guild05_1a](#d-umar_guild05_1a)
    - branch 2 → [umar_guild05_1b](#d-umar_guild05_1b)

    <span id="d-umar_guild04_29"></span>**`umar_guild04_29`** Umar: “Good job, kid! I knew I could count on you. Here, take this blade. It used to be your brother's.” — **effects:** sets stage 80 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-80), faction “ThievesGuild” +10, gives 1× [Blade of the protector](../items/blade_protector.md)

    - “Thank you, sir. You can count me in as well to kill Defy.” → [umar_guild04_30](#d-umar_guild04_30)
    - “Thank you sir, but what about Defy and his men?” → [umar_guild04_30](#d-umar_guild04_30)

    <span id="d-umar_guild04_26"></span>**`umar_guild04_26`** Umar: “Sullengard is our friend. Find a way to earn gold.”

    - “How can we earn that large amount of gold?” → [umar_guild04_27](#d-umar_guild04_27)
    - “This requires so much gold, how can we earn it?” → [umar_guild04_27](#d-umar_guild04_27)

    <span id="d-umar_guild04_21"></span>**`umar_guild04_21`** Umar: “Fortunately, one of my men found one of his drunk men and had a short talk with him before he bled to death.”

    - “What did he say?” → [umar_guild04_22](#d-umar_guild04_22)
    - “Sweet justice with small information?” → [umar_guild04_22](#d-umar_guild04_22)

    <span id="d-umar_guild04_19"></span>**`umar_guild04_19`** Umar: “This is madness! He betrayed us just like Crackshot did.” — **effects:** sets stage 60 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-60)

    - “We better find and kill him and his men and retrieve the share to help the people of Sullengard.” → [umar_guild04_20](#d-umar_guild04_20)

    <span id="d-umar_guild04_17"></span>**`umar_guild04_17`** Umar: “He can't be gone without our share from the bootleg brewers.” — **effects:** sets stage 40 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-40)

    - “I thought he would come back here.” → [umar_guild04_18](#d-umar_guild04_18)
    - “You're right.” → [umar_guild04_18](#d-umar_guild04_18)

    <span id="d-umar_guild04_15"></span>**`umar_guild04_15`** Umar: “Not again. What's on his mind?”

    - “I don't know.” → [umar_guild04_16](#d-umar_guild04_16)
    - “I'll ask him again once his head is cool.” → [umar_guild04_16](#d-umar_guild04_16)

    <span id="d-umar_guild04_12"></span>**`umar_guild04_12`** Umar: “I want you to go to Sullengard and find one of my appointed veterans named Defy.”

    - Next → [umar_guild04_13](#d-umar_guild04_13)

    <span id="d-umar_guild04_0"></span>**`umar_guild04_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [umar_guild04_1](#d-umar_guild04_1)

    <span id="d-umar_guild03_27c"></span>**`umar_guild03_27c`** Umar: “I've told you to have patience, my friend. Any thief is dead without patience.”

    - “What do you mean?” → [umar_guild03_28b](#d-umar_guild03_28b)
    - “Understood ....” → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_25"></span>**`umar_guild03_25`** Umar: “Excellent. Did he have the key with him?”

    - “Yes ... [give key]. Why is this key so important to us?” *(if hand over 1× [Key of Luthor](../items/g03_luthor.md))* → [umar_guild03_26a](#d-umar_guild03_26a)
    - “Sure, here, take it. And maybe it's time to give me some more information.” *(if hand over 1× [Key of Luthor](../items/g03_luthor.md))* → [umar_guild03_26b](#d-umar_guild03_26b)
    - “(Lie) No, I didn't find it.” → [umar_guild03_25_1](#d-umar_guild03_25_1)
    - “He had the key, but I don't have it with me.” *(if NOT carry 1× [Key of Luthor](../items/g03_luthor.md))* → [umar_guild03_25_2](#d-umar_guild03_25_2)

    <span id="d-umar_guild03_20"></span>**`umar_guild03_20`** Umar: “Remember, this is an important mission! Don't forget it again!”

    - Next → [umar_guild03_21](#d-umar_guild03_21)

    <span id="d-umar_guild03_14"></span>**`umar_guild03_14`** Umar: “Hmm ... I think we have no choice. We'll have to deal with him and his henchmen ... forever.”

    - “OK, leave this to me. That's finally the kind of work I was searching for.” → [umar_guild03_15a](#d-umar_guild03_15a)
    - “I ... I prefer to not get involved into this. Sorry.” → [umar_guild03_15b](#d-umar_guild03_15b)

    <span id="d-umar_guild03_10c"></span>**`umar_guild03_10c`** Umar: “Sure, I can do that.”

    - Next → [umar_guild03_11b](#d-umar_guild03_11b)

    <span id="d-umar_guild03_1"></span>**`umar_guild03_1`** Umar: “I see you are better than yesterday.”

    - “Indeed I am!” → [umar_guild03_2](#d-umar_guild03_2)
    - “Yes ...” → [umar_guild03_2](#d-umar_guild03_2)

    <span id="d-umar_guild02_26"></span>**`umar_guild02_26`** Umar: “(Umar looks a little worried) This is really not your line of work huh? I suggest you rest for a while before doing more. You look tired.”

    - “I'm not tired at all.” → [umar_guild02_27a](#d-umar_guild02_27a)
    - “Tired? I don't know what that means!” → [umar_guild02_27b](#d-umar_guild02_27b)
    - “Good idea.” → [umar_guild02_27c](#d-umar_guild02_27c)

    <span id="d-umar_guild02_22"></span>**`umar_guild02_22`** Umar: “Fine .... Although you look odd. What's the matter?”

    - “It's OK ... it's just that is not my kind of work.” → [umar_guild02_23a](#d-umar_guild02_23a)
    - “Urgh ... I just need better tasks! Do you still think I'm not yet ready?” → [umar_guild02_23b](#d-umar_guild02_23b)

    <span id="d-umar_guild02_21"></span>**`umar_guild02_21`** Umar: “Simple. Talk with Troublemaker about this job. He probably knows of some safe place to keep her. Then return to me.”

    - “OK, thanks.” → *conversation ends*
    - “Understood.” → *conversation ends*

    <span id="d-umar_guild02_20"></span>**`umar_guild02_20`** [Umar](../monsters/umar.md): “Hmm, I believe Troublemaker knows the actual state of that place. Ask him, and if it's possible leave our guest there.” — **effects:** sets stage 40 of [Immaculate kidnapping](../quests/Thieves02.md#stage-40)

    - “OK, I will. (You lift Ambelie up and carry her on your shoulders)” → *conversation ends*
    - “Hmpf ... Bye (You lift Ambelie up and carry her on your shoulders)” → *conversation ends*

    <span id="d-umar_guild02_19"></span>**`umar_guild02_19`** Umar: “We are supposed to have one room for receiving "visitors". However, I don't know if It's finished.” — **effects:** sets stage 35 of [Immaculate kidnapping](../quests/Thieves02.md#stage-35)

    - “Great, more boring "moving" tasks, right?” → [umar_guild02_20](#d-umar_guild02_20)
    - “And so?” → [umar_guild02_20](#d-umar_guild02_20)

    <span id="d-umar_guild02_28"></span>**`umar_guild02_28`** Umar: “I see guilt in your eyes, my young friend.”

    - “I couldn't accomplish the objective, I'm sorry.” → [umar_guild02_29a](#d-umar_guild02_29a)
    - “I felt sorry for that woman, and I decided to extort her and get the gold directly.” → [umar_guild02_29b](#d-umar_guild02_29b)

    <span id="d-umar_guild02_16"></span>**`umar_guild02_16`** Umar: “(You put Ambelie, who is still unconscious, in a chair next to you) Oh! How did you get here so fast? I've heard reports of a barricade blocking the way from the Duleian road to Fallhaven.” — **effects:** sets stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30)

    - “Barricades, guards ... no big thing for me.” → [umar_guild02_17](#d-umar_guild02_17)
    - “I found a shortcut.” → [umar_guild02_17](#d-umar_guild02_17)

    <span id="d-umar_guild02_15"></span>**`umar_guild02_15`** Umar: “No, I've told you all you need to know. Now leave me please, I've work to do.”


    <span id="d-umar_guild02_10"></span>**`umar_guild02_10`** Umar: “I want you to bring the noble woman here, so that we can ask for a substantial ransom from her generous father.” — **effects:** sets stage 2 of [Immaculate kidnapping](../quests/Thieves02.md#stage-2)

    - “Consider it done.” → [umar_guild02_11a](#d-umar_guild02_11a)
    - “Where can I find this woman?” → [umar_guild02_11b](#d-umar_guild02_11b)

    <span id="d-umar_guild02_13"></span>**`umar_guild02_13`** Umar: “Use your tongue, young man. Sometimes it is more important than your sword skills.” — **effects:** sets stage 6 of [Immaculate kidnapping](../quests/Thieves02.md#stage-6)

    - “Hah! I don't think so. But anyway, thank you for the advice.” → [umar_guild02_14](#d-umar_guild02_14)
    - “I'll do that, thanks for the advice.” → [umar_guild02_14](#d-umar_guild02_14)

    <span id="d-umar_guild02_1"></span>**`umar_guild02_1`** Umar: “Excellent, young friend. Consider yourself a member of our Guild.”

    - “Meh, that was nothing special. Bye.” → *conversation ends*
    - “OK, nice to see you again.” → *conversation ends*
    - “Hah, what an honor! It has been so, so difficult ....” → [umar_guild02_2](#d-umar_guild02_2)

    <span id="d-umar_return_2"></span>**`umar_return_2`** Umar: “Anything else I can help you with?”

    - “Can you repeat what you said about Andor?” → [umar_5](#d-umar_5)
    - “Nice to meet you. Goodbye.” → *conversation ends*
    - “Yes, I want to know more about the Thieves' Guild.” *(if reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); NOT reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5))* → [umar_guild_1](#d-umar_guild_1)
    - “I've been thinking about joining the guild.” *(if reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5); NOT reached stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10); NOT latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60)* → [umar_guild_4b](#d-umar_guild_4b)

    <span id="d-umar_2"></span>**`umar_2`** Umar: “Last time we talked, you asked for the way to Lodar's Hideaway. Did you find it?”

    - “We have never met.” → [umar_3](#d-umar_3)
    - “You must have me confused with my brother Andor. We look very much alike.” → [umar_4](#d-umar_4)

    <span id="d-umar_tt_110"></span>**`umar_tt_110`** Umar: “She must. Tell her this password [whispering something]. It means you have direct order from me, Umar. Let no one else hear it.” — **effects:** sets stage 120 of [Troubling times](../quests/troubling_times.md#stage-120)

    - “OK. She will listen to you.” → [umar_tt_120](#d-umar_tt_120)

    <span id="d-umar_guild05_1a"></span>**`umar_guild05_1a`** Umar: “You are really very hardworking. I can't find new work for you fast enough. You're free for now.”


    <span id="d-umar_guild05_1b"></span>**`umar_guild05_1b`** Umar: “No jobs today my young friend. Maybe some other day.”

    - “I see. Bye.” → *conversation ends*
    - “That's a shame. Find more time for my skills then.” → *conversation ends*

    <span id="d-umar_guild04_30"></span>**`umar_guild04_30`** Umar: “Like I said, we are still looking for him. You should rest for now from your long haul.”

    - “You're right. My legs are so tired from having to walk back and forth from here to Sullengard so many times.” → *conversation ends*
    - “Yes, I should rest from my long travel.” → *conversation ends*

    <span id="d-umar_guild04_27"></span>**`umar_guild04_27`** Umar: “I trust that you will find a way. In the meantime, go back to Sullengard and give them the share we promised them so they can go on with their lives.” — **effects:** sets stage 70 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70)

    - “What? How?” *(if NOT reached stage 28 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-28))* → [umar_guild04_28b](#d-umar_guild04_28b)
    - “Yes. I'm on it.” → [umar_guild04_28a](#d-umar_guild04_28a)

    <span id="d-umar_guild04_22"></span>**`umar_guild04_22`** Umar: “He said that they will no longer be a part of the Thieves' Guild. They are now referring to themselves as 'Aidem'.”

    - “What a weird name. For what reason?” → [umar_guild04_23](#d-umar_guild04_23)
    - “But why?” → [umar_guild04_23](#d-umar_guild04_23)

    <span id="d-umar_guild04_20"></span>**`umar_guild04_20`** Umar: “Yes. We must find and kill them and retrieve the share for the sake of Sullengard's living.”

    - Next → [umar_guild04_21](#d-umar_guild04_21)

    <span id="d-umar_guild04_18"></span>**`umar_guild04_18`** Umar: “Go back to Sullengard and ask the townspeople if they know of his whereabouts.”

    - “I'm on my way back to Sullengard now. Bye.” → *conversation ends*

    <span id="d-umar_guild04_16"></span>**`umar_guild04_16`** Umar: “Sigh. He may be stubborn sometimes but he is a great supervisor. You should ask him once he is calm.” — **effects:** sets stage 30 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-30), removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement

    - “I'm going to visit him again. Bye.” → *conversation ends*
    - “That's what I just said.” → *conversation ends*

    <span id="d-umar_guild04_13"></span>**`umar_guild04_13`** Umar: “Tell him that it is time to give the bootleg brewers their share to aid in their livelihoods. Especially in paying their taxes.”

    - “You can count on me.” → [umar_guild04_14](#d-umar_guild04_14)
    - “But I need an invitation letter first.” → [umar_guild04_14](#d-umar_guild04_14)
    - “I'll just wait for my brother to do that because it's very far.” → *conversation ends*

    <span id="d-umar_guild04_1"></span>**`umar_guild04_1`** Umar: “Yes, I do have a new task for you. So, listen to me carefully.”

    - “I'm listening.” → [umar_guild04_2](#d-umar_guild04_2)

    <span id="d-umar_guild03_28b"></span>**`umar_guild03_28b`** Umar: “I mean this is not the time to tell you what you want to know, sorry.”

    - “Tsch, whatever.” → [umar_guild03_27a](#d-umar_guild03_27a)
    - “Yes, understood.” → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_27a"></span>**`umar_guild03_27a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-90))* → [umar_guild03_27a_2](#d-umar_guild03_27a_2)
    - branch 2 *(if reached stage 32 of [The ruthless Crackshot](../quests/Thieves03.md#stage-32))* → [umar_guild03_27a_1](#d-umar_guild03_27a_1)
    - branch 3 → [umar_guild03_29](#d-umar_guild03_29)

    <span id="d-umar_guild03_26a"></span>**`umar_guild03_26a`** Umar: “I'm sorry, but for now I can't say more.” — **effects:** sets stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45)

    - “I see ....” → [umar_guild03_27a](#d-umar_guild03_27a)
    - “Tsch, OK.” → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_26b"></span>**`umar_guild03_26b`** Umar: “Be patient, my friend. Everything will come in due time.” — **effects:** sets stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45)

    - “I expect my patience will be rewarded.” → [umar_guild03_27b](#d-umar_guild03_27b)
    - “If you say so ...” → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_25_1"></span>**`umar_guild03_25_1`** Umar: “Don't try to fool me. I am Umar. I know you have it.”

    - “Oh. Yes, I remember now that I found the key. Here, take it.” *(if hand over 1× [Key of Luthor](../items/g03_luthor.md))* → [umar_guild03_25_3](#d-umar_guild03_25_3)
    - “Even if I have the key, I won't give it to you.” → [umar_guild03_25_1a](#d-umar_guild03_25_1a)

    <span id="d-umar_guild03_25_2"></span>**`umar_guild03_25_2`** Umar: “Then what you are waiting for? Go and get it!”


    <span id="d-umar_guild03_21"></span>**`umar_guild03_21`** Umar: “First, you must find Crackshot's hideout.”

    - Next → [umar_guild03_22](#d-umar_guild03_22)

    <span id="d-umar_guild03_15a"></span>**`umar_guild03_15a`** Umar: “Are you completely sure? You will be alone against trained thieves and other criminals whose sole objective is to earn more and more gold.”

    - “I can deal with them with my bare hands!” → [umar_guild03_16](#d-umar_guild03_16)
    - “Don't worry, I'll be careful.” → [umar_guild03_16](#d-umar_guild03_16)

    <span id="d-umar_guild03_15b"></span>**`umar_guild03_15b`** Umar: “Maybe it's not the best time. We must bring him down. Think about it. There are probably many lives at risk ...”

    - “I will, I promise. Bye.” → *conversation ends*

    <span id="d-umar_guild03_11b"></span>**`umar_guild03_11b`** Umar: “Apparently they decided the Guild wasn't the best option, so they turned greedy and betrayed us. That's more common than I would like to admit.”

    - “What filthy and disloyal people.” → [umar_guild03_12](#d-umar_guild03_12)
    - “They have signed their own death sentence.” → [umar_guild03_12](#d-umar_guild03_12)

    <span id="d-umar_guild03_2"></span>**`umar_guild03_2`** Umar: “Fine. Listen to me carefully.”

    - “Sure, tell me what you have to say.” → [umar_guild03_3](#d-umar_guild03_3)
    - “I'm all ears.” → [umar_guild03_3](#d-umar_guild03_3)

    <span id="d-umar_guild02_27a"></span>**`umar_guild02_27a`** Umar: “I prefer that you are completely rested before talking about work.”

    - “Ugh ... OK.” → [umar_guild02_27c](#d-umar_guild02_27c)
    - “I'm always rested!” → [umar_guild02_27b](#d-umar_guild02_27b)

    <span id="d-umar_guild02_27b"></span>**`umar_guild02_27b`** Umar: “Don't be overconfident. Take my advice and rest. We'll talk tomorrow.”

    - “Tsch. All right, sir.” → [umar_guild02_27c](#d-umar_guild02_27c)

    <span id="d-umar_guild02_27c"></span>**`umar_guild02_27c`** Umar: “Come back to me when you're prepared. Bear in mind that your next task isn't going to be as easy as the ones you already did. We'll talk about that tomorrow.” — **effects:** sets stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1), changes map fallhaven_tavern, changes map fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from guildbrig2

    - “I expected that. See you tomorrow then.” → [umar_guild02_27d](#d-umar_guild02_27d)
    - “Easy? Argh, they've been so difficult! Good night.” → [umar_guild02_27d](#d-umar_guild02_27d)

    <span id="d-umar_guild02_23a"></span>**`umar_guild02_23a`** Umar: “Sometimes people must do things that they don't like. Maybe you're still too young to understand that?”

    - “Not at all.” → [umar_guild02_24a](#d-umar_guild02_24a)
    - “Yes.” → [umar_guild02_24b](#d-umar_guild02_24b)

    <span id="d-umar_guild02_23b"></span>**`umar_guild02_23b`** Umar: “No, nothing of the kind! I was .... Well, let's talk.”

    - Next → [umar_guild02_25](#d-umar_guild02_25)

    <span id="d-umar_guild02_29a"></span>**`umar_guild02_29a`** Umar: “You don't need to tell me things I can see with my own eyes, it is a waste of time.”

    - Next → [umar_guild02_30](#d-umar_guild02_30)

    <span id="d-umar_guild02_29b"></span>**`umar_guild02_29b`** Umar: “Being a good liar is a very valuable ability for the guild, but useless against me.”

    - Next → [umar_guild02_30](#d-umar_guild02_30)

    <span id="d-umar_guild02_17"></span>**`umar_guild02_17`** Umar: “OK, well done. Now we will have to find a better place for our guest. Keeping this lady here could be dangerous for us.”

    - “I'm sure that's the case, but that's not my problem anymore. Right?” → [umar_guild02_18a](#d-umar_guild02_18a)
    - “Do you have any ideas?” → [umar_guild02_18b](#d-umar_guild02_18b)

    <span id="d-umar_guild02_11a"></span>**`umar_guild02_11a`** Umar: “Great ... Before you go, I should tell you where she is.”

    - Next → [umar_guild02_11b](#d-umar_guild02_11b)

    <span id="d-umar_guild02_11b"></span>**`umar_guild02_11b`** Umar: “Scouts have seen the lady in the Foaming flask tavern. We do not want to be discovered, so act quietly. Guards are a problem though. It's up to you how you choose to solve the guards problem.” — **effects:** sets stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4)

    - “Yes. I understand.” → [umar_guild02_12](#d-umar_guild02_12)
    - “Seems difficult, but whatever. I'll do it.” → [umar_guild02_12](#d-umar_guild02_12)

    <span id="d-umar_guild02_14"></span>**`umar_guild02_14`** Umar: “Remember that if you are discovered, you are no one. No one knows you. And of course, no one has seen you. You are now a member of the guild, so don't fail.”

    - “You still think I'm a novice, right? You're going to see that you're wrong!” → *conversation ends*
    - “Understood. Bye.” → *conversation ends*

    <span id="d-umar_guild02_2"></span>**`umar_guild02_2`** Umar: “I detect a certain sarcasm in your words.”

    - “No, no .... Never mind, see you later.” → *conversation ends*
    - “That's maybe because I am trying to be sarcastic ...” → [umar_guild02_3](#d-umar_guild02_3)

    <span id="d-umar_5"></span>**`umar_5`** Umar: “He came here a while ago, asking a lot of questions about what relation the Thieves' Guild has to the Shadow and to the royal guard in Feygard.”

    - Next → [umar_6](#d-umar_6)

    <span id="d-umar_guild_1"></span>**`umar_guild_1`** Umar: “I see .... So you want to get involved in our Guild?”

    - “Yes, you seem like reasonable people.” → [umar_guild_2a](#d-umar_guild_2a)
    - “Whatever. It's just curiosity.” → [umar_guild_2a](#d-umar_guild_2a)
    - “No, not really. I'm not interested in being a smug thief.” → [umar_guild_2b](#d-umar_guild_2b)

    <span id="d-umar_guild_4b"></span>**`umar_guild_4b`** Umar: “What have you decided?”

    - “I will take your opportunity!” → [umar_guild_5a](#d-umar_guild_5a)
    - “I'm still confused, sorry.” → [umar_guild_5b](#d-umar_guild_5b)

    <span id="d-umar_3"></span>**`umar_3`** Umar: “Oh. I must have you confused with someone else.”

    - “My brother Andor and I look very much alike.” → [umar_4](#d-umar_4)

    <span id="d-umar_4"></span>**`umar_4`** Umar: “Really? Never mind I said anything then.” — **effects:** sets stage 51 of [Search for Andor](../quests/andor.md#stage-51)

    - “I guess that means that Andor was here. What was he doing?” → [umar_5](#d-umar_5)

    <span id="d-umar_tt_120"></span>**`umar_tt_120`** Umar: “My head is so full. I can hardly concentrate on the important things.”

    - “I won't bother you any further.” → *conversation ends*
    - “The spell will be broken.” → *conversation ends*
    - “Thoroughness is the key to success.” → [umar_tt_130](#d-umar_tt_130)

    <span id="d-umar_guild04_28b"></span>**`umar_guild04_28b`** Umar: “Here's 1,000 gold coins as my financial contribution.” — **effects:** sets stage 28 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-28), gives 1000× [Gold coins](../items/gold.md)

    - “Oh. Thank you.” → [umar_guild04_28a](#d-umar_guild04_28a)
    - “Wow! It motivated me. Thanks.” → [umar_guild04_28a](#d-umar_guild04_28a)

    <span id="d-umar_guild04_28a"></span>**`umar_guild04_28a`** Umar: “Immediately report back to me once you are done.”

    - “I better start looking for gold now.” → *conversation ends*
    - “It will be done.” → *conversation ends*

    <span id="d-umar_guild04_23"></span>**`umar_guild04_23`** Umar: “They prefer riches over honor.”

    - Next → [umar_guild04_24](#d-umar_guild04_24)

    <span id="d-umar_guild04_14"></span>**`umar_guild04_14`** Umar: “Hurry now. There's no time to waste.” — **effects:** sets stage 10 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10)

    - “Fine.” → *conversation ends*
    - “I'm going now.” → *conversation ends*

    <span id="d-umar_guild04_2"></span>**`umar_guild04_2`** Umar: “Here in the guild, as you know, income sources come in different classes from poor to wealthy. The lower-middle class and poor class are usually associated with us.”

    - Next → [umar_guild04_3](#d-umar_guild04_3)

    <span id="d-umar_guild03_27a_2"></span>**`umar_guild03_27a_2`** Umar: “Anyway, you've done your work. My spies reported to me you had saved someone's life.”

    - “If your spies help me, tasks would be easier.” → [umar_guild03_28a](#d-umar_guild03_28a)
    - “I tried to, unfortunately he didn't survive. But it was nobody important.” → [umar_guild03_28c](#d-umar_guild03_28c)
    - “No, he died at last. He was a Feygard officer ... a sergeant I think.” → [umar_guild03_28c](#d-umar_guild03_28c)

    <span id="d-umar_guild03_27a_1"></span>**`umar_guild03_27a_1`** Umar: “Anyway, you've done your work. My spies reported to me that you saved someone's life.”

    - “If your spies help me, tasks would be easier.” → [umar_guild03_28a](#d-umar_guild03_28a)
    - “It is true .... Nobody important.” → [umar_guild03_28c](#d-umar_guild03_28c)
    - “Yeah. He was a Feygard officer ... a sergeant I think.” → [umar_guild03_28c](#d-umar_guild03_28c)

    <span id="d-umar_guild03_29"></span>**`umar_guild03_29`** Umar: “Hmm! And now to business. Here's your reward for the good work.”

    - Next → [umar_guild03_30](#d-umar_guild03_30)

    <span id="d-umar_guild03_27b"></span>**`umar_guild03_27b`** Umar: “Trust me, it will.”

    - Next → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_25_3"></span>**`umar_guild03_25_3`** Umar: “Why did it take so long? And do not look at me that way. I can not tell you anything about the key for now.” — **effects:** sets stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45)

    - Next → [umar_guild03_27a](#d-umar_guild03_27a)

    <span id="d-umar_guild03_25_1a"></span>**`umar_guild03_25_1a`** Umar: “Come back when you are sane again.”


    <span id="d-umar_guild03_22"></span>**`umar_guild03_22`** Umar: “Then you will have to deal with him and his henchmen, and finally bring back the Key of Luthor to us.”

    - Next → [umar_guild03_23](#d-umar_guild03_23)

    <span id="d-umar_guild03_16"></span>**`umar_guild03_16`** Umar: “Whatever, I do believe you are capable. Regardless, be cautious with Crackshot. He's powerful, and his attacks can severely wound or kill you. Clear?”

    - “Bah, words are worth nothing now. It's going to be a nice fight.” → [umar_guild03_17a](#d-umar_guild03_17a)
    - “Yes, understood!” → [umar_guild03_17b](#d-umar_guild03_17b)

    <span id="d-umar_guild03_12"></span>**`umar_guild03_12`** Umar: “There's more. Two days ago the southern route from here to the Duleian road was closed, because there was a murder. Soldiers are trying to prevent the murderer from escaping to the west.”

    - “And you think the traitors are involved in that?” → [umar_guild03_13](#d-umar_guild03_13)

    <span id="d-umar_guild03_3"></span>**`umar_guild03_3`** Umar: “Here in the guild, as you know, members range from apprentices to veterans. The veterans are usually specialized in specific jobs.”

    - Next → [umar_guild03_4](#d-umar_guild03_4)

    <span id="d-umar_guild02_27d"></span>**`umar_guild02_27d`** Umar: “I'm afraid all the beds at the guild are taken for the night. We have arrangements at the inn in town though. If you tell them Umar sent you then you will not have to pay for a bed.” — **effects:** sets stage 20 of [misc_nondisplay (hidden flag)](../quests/misc_nondisplay.md#stage-20)

    - “OK. Thanks.” → *conversation ends*
    - “I'll do that.” → *conversation ends*

    <span id="d-umar_guild02_24a"></span>**`umar_guild02_24a`** Umar: “Well .... Anyway, I promise we won't give you those kind of jobs for a while.”

    - “Fine.” → [umar_guild02_24b](#d-umar_guild02_24b)
    - “That is good news for me.” → [umar_guild02_24b](#d-umar_guild02_24b)

    <span id="d-umar_guild02_24b"></span>**`umar_guild02_24b`** Umar: “Great, so let's talk then.”

    - Next → [umar_guild02_25](#d-umar_guild02_25)

    <span id="d-umar_guild02_25"></span>**`umar_guild02_25`** Umar: “First of all, take this gold for a job well done. We have already sent people to ask for the ransom.” — **effects:** sets stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75), faction “ThievesGuild” +10, gives 2500× [Gold coins](../items/gold.md)

    - Next → [umar_guild02_26](#d-umar_guild02_26)

    <span id="d-umar_guild02_30"></span>**`umar_guild02_30`** Umar: “I expect more of you. That was your first mission inside the guild and you failed it!”

    - “I brought a valuable necklace from the noblewoman.” *(if hand over 1× [Sapphire Necklace](../items/g02_ambelie.md))* → [umar_guild02_31](#d-umar_guild02_31)

    <span id="d-umar_guild02_18a"></span>**`umar_guild02_18a`** Umar: “Yes it is.”

    - “Well, I have no choice. What should I do?” → [umar_guild02_19](#d-umar_guild02_19)

    <span id="d-umar_guild02_18b"></span>**`umar_guild02_18b`** Umar: “Hmm, let me think about it ....”

    - Next → [umar_guild02_19](#d-umar_guild02_19)

    <span id="d-umar_guild02_12"></span>**`umar_guild02_12`** Umar: “Good luck. Return to me when you're done.”

    - “Wait, wait! How am I supposed to ...” → [umar_guild02_13](#d-umar_guild02_13)
    - “I will bring her, even if I have to eliminate Feygard's entire army!” → [umar_guild02_13](#d-umar_guild02_13)

    <span id="d-umar_guild02_3"></span>**`umar_guild02_3`** Umar: “What do you mean?”

    - “Just give me a high-risk job, please.” → [umar_guild02_4](#d-umar_guild02_4)
    - “I mean my last job was a piece of cake. I need something more exciting!” → [umar_guild02_4](#d-umar_guild02_4)

    <span id="d-umar_6"></span>**`umar_6`** Umar: “We in the Thieves' Guild really don't care much for the Shadow. Nor do we care for the royal guard.”

    - Next → [umar_7](#d-umar_7)

    <span id="d-umar_guild_2a"></span>**`umar_guild_2a`** Umar: “Well, you've shown us you are trustworthy by bringing that key. However, doing just one task does not prove to us that you are eligible to be a member of our guild.”

    - “But I really want to join your guild!” → [umar_guild_3](#d-umar_guild_3)
    - “Really? I didn't see any of your members bringing you "that" key.” → [umar_guild_3](#d-umar_guild_3)
    - “Never mind, bye.” → *conversation ends*

    <span id="d-umar_guild_2b"></span>**`umar_guild_2b`** Umar: “I'm sorry to hear that. Good luck.”

    - “Bye.” → *conversation ends*

    <span id="d-umar_guild_5a"></span>**`umar_guild_5a`** Umar: “Very well. Let's see if you're good enough to join our guild. Talk with Troublemaker. He will tell you what you have to do.” — **effects:** sets stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10)

    - “All right! I'll go see him.” → [umar_guild_6a](#d-umar_guild_6a)
    - “Anything else?” → [umar_guild_6b](#d-umar_guild_6b)

    <span id="d-umar_guild_5b"></span>**`umar_guild_5b`** Umar: “I understand your doubts. Come back when you're prepared.”

    - “Bye.” → *conversation ends*

    <span id="d-umar_tt_130"></span>**`umar_tt_130`** Umar: “Key? To success? Don't talk nonsense.”

    - Next → [umar_tt_132](#d-umar_tt_132)

    <span id="d-umar_guild04_24"></span>**`umar_guild04_24`** Umar: “Such a dishonorable act for they stole 50,000 gold coins including the treasures of Sullengard.”

    - “Their dishonorable act will be their undoing.” → [umar_guild04_25](#d-umar_guild04_25)
    - “Justice shall serve!” → [umar_guild04_25](#d-umar_guild04_25)

    <span id="d-umar_guild04_3"></span>**`umar_guild04_3`** Umar: “Wealthy class is our highest target. This is why I didn't doubt to give you the first mission to kidnap Ambelie for ransom.”

    - “My bad.” *(if reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76))* → [umar_guild04_4](#d-umar_guild04_4)
    - “That is not my kind of work though.” *(if reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75))* → [umar_guild04_4](#d-umar_guild04_4)

    <span id="d-umar_guild03_28a"></span>**`umar_guild03_28a`** Umar: “Each of you have your own specific task. Spies must hide their identities, even to their allies.”

    - “That makes sense.” → [umar_guild03_29](#d-umar_guild03_29)

    <span id="d-umar_guild03_28c"></span>**`umar_guild03_28c`** Umar: “I see ....”

    - Next → [umar_guild03_29](#d-umar_guild03_29)

    <span id="d-umar_guild03_30"></span>**`umar_guild03_30`** Umar: “Take 4,000 gold coins, and some bottles of my favorite mead. Now you deserve a good rest, my friend. You have earned the trust of the Thieves' Guild.” — **effects:** sets stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50), gives 4000× [Gold coins](../items/gold.md), gives 10× [Mead](../items/mead.md), faction “ThievesGuild” +20

    - “I'll be back soon.” → [umar_guild03_31a](#d-umar_guild03_31a)
    - “Count me in for the next job.” → [umar_guild03_31b](#d-umar_guild03_31b)
    - “OK, bye.” → *conversation ends*

    <span id="d-umar_guild03_23"></span>**`umar_guild03_23`** Umar: “Understood?”

    - “Yes!” → [umar_guild03_24a](#d-umar_guild03_24a)
    - “Understood ...” → [umar_guild03_24a](#d-umar_guild03_24a)
    - “Can you explain it to me again?” → [umar_guild03_24b](#d-umar_guild03_24b)

    <span id="d-umar_guild03_17a"></span>**`umar_guild03_17a`** Umar: “If you say so. Your self-confidence is a good aspect of your personality.”

    - “Thank you!” → [umar_guild03_17b](#d-umar_guild03_17b)

    <span id="d-umar_guild03_17b"></span>**`umar_guild03_17b`** Umar: “However, there's still a problem. We're not completely sure about the location of Crackshot's new hideout.”

    - “What? How I will find him then?” → [umar_guild03_18a](#d-umar_guild03_18a)
    - “He will show up sooner or later ...” → [umar_guild03_18b](#d-umar_guild03_18b)

    <span id="d-umar_guild03_13"></span>**`umar_guild03_13`** Umar: “I'm pretty sure about it. The team leader is the one we call "Crackshot", as he is a master of murder, torture and the subjugation arts. He's really a dangerous man.” — **effects:** sets stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5)

    - “So, do you have a plan?” → [umar_guild03_14](#d-umar_guild03_14)
    - “What am I supposed to do?” → [umar_guild03_14](#d-umar_guild03_14)

    <span id="d-umar_guild03_4"></span>**`umar_guild03_4`** Umar: “Troublemaker is my right hand man. He's in charge of planning jobs that have some level of complexity.”

    - Next → [umar_guild03_5](#d-umar_guild03_5)

    <span id="d-umar_guild02_31"></span>**`umar_guild02_31`** Umar: “What we have here? (Umar's face gets a smile while he admires the necklace)”

    - Next → [umar_guild02_32](#d-umar_guild02_32)

    <span id="d-umar_guild02_4"></span>**`umar_guild02_4`** Umar: “If you want me to give you a more difficult task, then I am happy to do so.”

    - “Well, so?” → [umar_guild02_5](#d-umar_guild02_5)
    - “OK, in that case tell me what it is.” → [umar_guild02_5](#d-umar_guild02_5)

    <span id="d-umar_7"></span>**`umar_7`** Umar: “We try to be above their bickering and differences. They may fight as much as they want, but the Thieves' Guild will outlive them all.”

    - “What differences?” → [umar_conflict_1](#d-umar_conflict_1)
    - “Tell me more about what Andor asked for.” → [umar_andor_1](#d-umar_andor_1)

    <span id="d-umar_guild_3"></span>**`umar_guild_3`** Umar: “OK, OK. You will get a chance. But I warn you that from now on, you cannot go back on your choice.” — **effects:** sets stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5)

    - Next → [umar_guild_4a](#d-umar_guild_4a)

    <span id="d-umar_guild_6a"></span>**`umar_guild_6a`** Umar: “Fine. I will keep an eye on you.”


    <span id="d-umar_guild_6b"></span>**`umar_guild_6b`** Umar: “Not for now. Make sure nobody sees you doing suspicious things. Good luck.” — **effects:** sets stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10)

    - “I will be careful. Bye.” → *conversation ends*

    <span id="d-umar_tt_132"></span>**`umar_tt_132`** Umar: “There's something else I should think about. But it just doesn't occur to me right now.”

    - “I better leave you alone now.” → *conversation ends*
    - “I'm sure you'll remember it again.” → *conversation ends*
    - “OK. Bye.” → *conversation ends*

    <span id="d-umar_guild04_25"></span>**`umar_guild04_25`** Umar: “We still don't know where they are.”

    - Next → [umar_guild04_26](#d-umar_guild04_26)

    <span id="d-umar_guild04_4"></span>**`umar_guild04_4`** Umar: “Don't worry, we already made a promise.”

    - Next → [umar_guild04_5](#d-umar_guild04_5)

    <span id="d-umar_guild03_31a"></span>**`umar_guild03_31a`** Umar: “And last but not least, I have some useful information for you. The way from here to the southeast has finally been opened, once Crackshot's hideout was discovered.”

    - “Good, I'm not going to have to take that detour.” → [umar_guild03_32](#d-umar_guild03_32)
    - “Thank you for the information. Bye.” → *conversation ends*

    <span id="d-umar_guild03_31b"></span>**`umar_guild03_31b`** Umar: “I will, no doubt about it.”

    - Next → [umar_guild03_31a](#d-umar_guild03_31a)

    <span id="d-umar_guild03_24a"></span>**`umar_guild03_24a`** Umar: “Excellent. Good luck.”

    - “Thank you.” → *conversation ends*

    <span id="d-umar_guild03_24b"></span>**`umar_guild03_24b`** Umar: “Are you serious? Bah, I'll repeat it for you ...”

    - Next → [umar_guild03_21](#d-umar_guild03_21)

    <span id="d-umar_guild03_18a"></span>**`umar_guild03_18a`** Umar: “Probably people near the Duleian road guard tower know more. See if you can ask them for tips.” — **effects:** sets stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10)

    - “Whatever. I'll find him.” → [umar_guild03_19c](#d-umar_guild03_19c)
    - “OK.” → [umar_guild03_19c](#d-umar_guild03_19c)

    <span id="d-umar_guild03_18b"></span>**`umar_guild03_18b`** Umar: “Maybe, but it will be faster if you question people near the Duleian road guard tower. The Duleian road is the place where we think he was last seen.” — **effects:** sets stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10)

    - “OK, I will ask there.” → [umar_guild03_19c](#d-umar_guild03_19c)
    - “Argh, the Duleian road is big!” → [umar_guild03_19b](#d-umar_guild03_19b)

    <span id="d-umar_guild03_5"></span>**`umar_guild03_5`** Umar: “Pickpocket has developed his stealth skills to such an extreme that he's able to take your equipment, and you'll barely even feel it.”

    - “Woah, how is that possible?” → [umar_guild03_6a](#d-umar_guild03_6a)
    - “I don't believe you.” → [umar_guild03_6b](#d-umar_guild03_6b)

    <span id="d-umar_guild02_32"></span>**`umar_guild02_32`** Umar: “Well. I will take it as compensation for your mistakes.” — **effects:** sets stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76), faction “ThievesGuild” +10

    - “Again, I'm sorry.” → [umar_guild02_26](#d-umar_guild02_26)
    - “Thank you.” → [umar_guild02_26](#d-umar_guild02_26)

    <span id="d-umar_guild02_5"></span>**`umar_guild02_5`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-80))* → [umar_guild02_5a](#d-umar_guild02_5a)
    - branch 2 → [umar_guild02_5z](#d-umar_guild02_5z)

    <span id="d-umar_conflict_1"></span>**`umar_conflict_1`** Umar: “Where have you been the last couple of years? Don't you know of the brewing conflict?”

    - Next → [umar_conflict_2](#d-umar_conflict_2)

    <span id="d-umar_andor_1"></span>**`umar_andor_1`** Umar: “He asked me for my support, and asked about how to find Lodar.”

    - “Who is Lodar?” → [umar_andor_2](#d-umar_andor_2)

    <span id="d-umar_guild_4a"></span>**`umar_guild_4a`** Umar: “So what is your decision?”

    - “Haven't you understood? Just tell me what I have to do.” → [umar_guild_5a](#d-umar_guild_5a)
    - “I will take the opportunity.” → [umar_guild_5a](#d-umar_guild_5a)
    - “I need some time to think about it.” → [umar_guild_5b](#d-umar_guild_5b)

    <span id="d-umar_guild04_5"></span>**`umar_guild04_5`** Umar: “Anyway, the rest of the class are either with us or against us.”

    - Next → [umar_guild04_6](#d-umar_guild04_6)

    <span id="d-umar_guild03_32"></span>**`umar_guild03_32`** Umar: “However, the Feygard presence is still significant. Be cautious with what you do.”

    - “I will, thank you for the advice.” → *conversation ends*
    - “All is under control. Bye.” → *conversation ends*

    <span id="d-umar_guild03_19c"></span>**`umar_guild03_19c`** Umar: “Make sure you don't talk about the Guild and his relationship with us. Don't trust anyone.”

    - “Understood!” → [umar_guild03_19d](#d-umar_guild03_19d)
    - “I won't even trust my shadow.” → [umar_guild03_19d](#d-umar_guild03_19d)

    <span id="d-umar_guild03_19b"></span>**`umar_guild03_19b`** Umar: “That's why you have to ask.”

    - Next → [umar_guild03_19c](#d-umar_guild03_19c)

    <span id="d-umar_guild03_6a"></span>**`umar_guild03_6a`** Umar: “Each person has their own way to reach the top.”

    - Next → `umar_guild03_7`

    <span id="d-umar_guild03_6b"></span>**`umar_guild03_6b`** Umar: “Believe me, I'm not lying.”

    - Next → `umar_guild03_7`

    <span id="d-umar_guild02_5a"></span>**`umar_guild02_5a`** Umar: “But first I have to clarify something. You need to be more careful not to give information to outsiders about the Thieves' Guild.”

    - “Did I?” → `umar_guild02_5b`
    - “You're right. It will not happen again.” → [umar_guild02_5z](#d-umar_guild02_5z)

    <span id="d-umar_guild02_5z"></span>**`umar_guild02_5z`** Umar: “Well, before I can give you a very demanding job, I need you to do another ... retrieval task.”

    - “Anything for the glory o... Oops, I mean OK” → `umar_guild02_6a`
    - “Sigh. If you insist ...” → `umar_guild02_6a`
    - “Hmm, sounds boring. I decline.” → `umar_guild02_6b`

    <span id="d-umar_conflict_2"></span>**`umar_conflict_2`** Umar: “The royal guard, led by Lord Geomyr in Feygard, are trying to ward off the recent increase in illegal activities, and are therefore imposing more restrictions on what is or is not allowed.”

    - Next → `umar_conflict_3`

    <span id="d-umar_andor_2"></span>**`umar_andor_2`** Umar: “Lodar? He is one of the famous potion makers from the old days. The Thieves' Guild has requested his services many times before. He can make all sorts of strong sleeping potions, healing potions and cures.”

    - Next → `umar_andor_3`

    <span id="d-umar_guild04_6"></span>**`umar_guild04_6`** Umar: “Most of the time we made deals and negotiations with them in exchange of peace or protection.”

    - Next → `umar_guild04_7`

    <span id="d-umar_guild03_19d"></span>**`umar_guild03_19d`** Umar: “Fine.”

    - “Anything more?” → `umar_guild03_19a`

    *Dialogue continues beyond this point (truncated).*


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “Oh. I must have you mixed up with someone else.” → “Oh. I must have you confused with someone else.”<br>· text: “Ok, I'll tell you how to get to Lodar's Hideaway. But you have to pro…” → “OK, I'll tell you how to get to Lodar's Hideaway. But you have to pro…” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 112 lines added, 7 lines changed<br>· text: “The royal guard, led by Lord Geomyr in Feygard, are trying to ward of…” → “The royal guard, led by Lord Geomyr in Feygard, are trying to ward of…”<br>· text: “The priests of the Shadow, mostly seated in Nor City, are opponents t…” → “The priests of the Shadow, mostly seated in Nor City, are opposed to …” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 4 lines changed<br>· text: “Appearently they decided the Guild wasn't the best option, so they tu…” → “Apparently they decided the Guild wasn't the best option, so they tur…”<br>· text: “What we have here? (Umar's face gets a smile while he admires the nec…” → “What we have here? (Umar's face gets a smile while he admires the nec…” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 3 lines changed<br>· text: “And last but not least, I have some useful information for you. The w…” → “And last but not least, I have some useful information for you. The w…”<br>· text: “However, the Feygard presence is still significant. Be cautious with …” → “However, the Feygard presence is still significant. Be cautious with …” |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 1 line changed |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “Take 4000 gold coins, and some bottles of my favourite mead. Now you …” → “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 35 lines added, 2 lines changed |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed |
| [v0.8.6](../versions/0.8.6.md) | Dialogue: 1 line changed<br>· text: “Fortunately, one of my men found one of his drunk men and had a short…” → “Fortunately, one of my men found one of his drunk men and had a short…” |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “[Here, the story continues]” → “You are really very hardworking. I can't find new work for you fast e…” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 10 lines added, 4 lines changed<br>· text: “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” → “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…”<br>· text: “But first I have to clarify something. You need to be more careful no…” → “But first I have to clarify something. You need to be more careful no…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines changed<br>· text: “Such a dishonorable act for they stole 50000 gold coins including the…” → “Such a dishonorable act for they stole {50000} gold coins including t…”<br>· text: “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” → “Take {4000} gold coins, and some bottles of my favorite mead. Now you…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `umar` |
    | Spawn group | `umar` |
    | Loot table | – |
    | Conversation | `umar_select_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "umar",
     "name": "Umar",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "umar",
     "phraseID": "umar_select_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=umar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=umar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=umar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=umar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
