---
description: "Lodar is a non-player character (NPC) in Andor's Trail, found in Prim. Shopkeeper; starts A creeping fear, Lodar's potions, Searching for madness, The way out is through."
---

# ![](../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite } Lodar

**Where to find Lodar:** Prim: [lodarhouse1](../maps/lodarhouse1.md#pin-npc-lodar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper; starts [A creeping fear](../quests/xulviir.md), [Lodar's potions](../quests/lodar_pots.md), [Searching for madness](../quests/lodar2.md), [The way out is through](../quests/shortcut_lodar.md) |
| **Found in** | Prim |
| **Entry ID** | `lodar` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Lodar's perilous concoction](../items/pot_rnd.md) | 100% | 2 to 6 |
| [Tears of the Shadow](../items/pot_shadowtear.md) | 100% | 1 to 2 |
| [Potion of haste](../items/pot_haste.md) | 100% | 3 |
| [Potion of minor regeneration](../items/pot_regen1.md) | 100% | 5 to 12 |
| [Lodar's potion of health](../items/pot_healthlodar.md) | 100% | 5 to 12 |
| [Lodar's bonemeal potion](../items/pot_bm_lodar.md) | 100% | 15 to 70 |
| [Potion of heightened senses](../items/pot_senses.md) | 100% | 5 to 12 |
| [Potion of vulnerabilities](../items/pot_aware.md) | 100% | 5 to 12 |
| [Liquid courage](../items/pot_courage.md) | 100% | 5 to 12 |

## Quests

- [A creeping fear](../quests/xulviir.md): stage 10
- [A lost potion](../quests/lodar.md): stage 110
- [Lodar's potions](../quests/lodar_pots.md): stages 10, 30, 40, 41, 42, 43
- [Search for Andor](../quests/andor.md): stages 70, 71, 72, 80
- [Searching for madness](../quests/lodar2.md): stages 10, 15, 20, 30, 50, 51, 60
- [The way out is through](../quests/shortcut_lodar.md): stages 10, 30

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Lodar. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lodar.json" data-npc="Lodar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (142 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lodar"></span>**`lodar`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60))* → [lodar_d0](#d-lodar_d0)
    - branch 2 *(if reached stage 51 of [Searching for madness](../quests/lodar2.md#stage-51))* → [lodar_find5](#d-lodar_find5)
    - branch 3 *(if reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50))* → [lodar_find2](#d-lodar_find2)
    - branch 4 *(if reached stage 20 of [Searching for madness](../quests/lodar2.md#stage-20))* → [lodar_find0](#d-lodar_find0)
    - branch 5 *(if reached stage 110 of [A lost potion](../quests/lodar.md#stage-110))* → [lodar_r0](#d-lodar_r0)
    - branch 6 → [lodar_0](#d-lodar_0)

    <span id="d-lodar_d0"></span>**`lodar_d0`** Lodar: “Hello again.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_find5"></span>**`lodar_find5`** Lodar: “Thank you my friend for saving not only me but all of us.”

    - Next → [lodar_find6](#d-lodar_find6)

    <span id="d-lodar_find2"></span>**`lodar_find2`** Lodar: “Did you really defeat the Hira'zinn? It is a formidable foe. I guess you must have, since you gave me its heart.”

    - Next → [lodar_find3](#d-lodar_find3)

    <span id="d-lodar_find0"></span>**`lodar_find0`** Lodar: “Oh, it's you again. Were you successful in what I asked of you?”

    - “What was I supposed to do again?” → [lodar_14](#d-lodar_14)
    - “I have defeated the Hira'zinn in the tomb below. Here is its heart.” *(if hand over 1× [Heart of the Hira'zinn](../items/hirazinn.md))* → [lodar_find1](#d-lodar_find1)

    <span id="d-lodar_r0"></span>**`lodar_r0`** Lodar: “Oh, it's you again. Now, who were you again?”

    - “I'm $playername.” → [lodar_2](#d-lodar_2)

    <span id="d-lodar_0"></span>**`lodar_0`** Lodar: “Maybe under here? No.”

    - Next → [lodar_1](#d-lodar_1)

    <span id="d-lodar_d1"></span>**`lodar_d1`** Lodar: “Again, thank you for your help.” — **effects:** sets stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)

    - “I'd like to talk about your potions.” → [lodar_pots0](#d-lodar_pots0)
    - “What are you doing all by yourself out here in the forest?” → [lodar_forest0](#d-lodar_forest0)
    - “On the body of the Hira'zinn, I found this peculiar sword. Do you know anything about it?” *(if carry 1× [Broken sword](../items/xulviir0.md))* → [lodar_xul0](#d-lodar_xul0)
    - “What was that Hira'zinn beast?” → [lodar_hira0](#d-lodar_hira0)
    - “I have come to find you. I am looking for my brother Andor.” → [lodar_andor0](#d-lodar_andor0)
    - “The way to come here is a real maze and the path is tricky to find. I think I've lost my way a hundred times. Do you…” *(if NOT reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10); NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30))* → [lodar_shortcut_0](#d-lodar_shortcut_0)
    - “I found the cave you mentioned but unfortunately the path doesn't go anywhere. I noticed a weird torch burning with a…” *(if reached stage 26 of [The way out is through](../quests/shortcut_lodar.md#stage-26); reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10); NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30))* → [shortcut_lodar_1](#d-shortcut_lodar_1)
    - “I found a cave beneath the Hira'zinn tomb but unfortunately the path doesn't go anywhere. I noticed a weird torch…” *(if reached stage 26 of [The way out is through](../quests/shortcut_lodar.md#stage-26); NOT reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10); NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30))* → [shortcut_lodar_1](#d-shortcut_lodar_1)
    - “It worked and I didn't get injured at all! There's now a path from the Duleian road to here that lets me avoid the maze.” *(if reached stage 40 of [The way out is through](../quests/shortcut_lodar.md#stage-40); NOT reached stage 50 of [The way out is through](../quests/shortcut_lodar.md#stage-50))* → [shortcut_lodar_2](#d-shortcut_lodar_2)
    - “Can I rest here?” → [lodar_rest](#d-lodar_rest)

    <span id="d-lodar_find6"></span>**`lodar_find6`** Lodar: “The Hira'zinn would have slowly but surely found a way to creep up on us all.”

    - Next → [lodar_find7](#d-lodar_find7)

    <span id="d-lodar_find3"></span>**`lodar_find3`** Lodar: “What was I doing? I was searching for something. I seem to recall you being here before, is that right?”

    - “Yes, we spoke before, but you seemed to be obsessed with the Hira'zinn and did not make much sense.” → [lodar_find4](#d-lodar_find4)
    - “Yes, but you were acting all crazy. I nearly put my sword through your throat.” → [lodar_find4](#d-lodar_find4)

    <span id="d-lodar_14"></span>**`lodar_14`** Lodar: “I thought I make it very clear before. With the stone in your possession, you will be able to enter the tomb. Go below. Return once you're done.”

    - “Fine. I still don't understand, but I'll try to do as you ask.” → [lodar_13](#d-lodar_13)
    - “Oh, that makes it much clearer! I'll be right back.” → [lodar_13](#d-lodar_13)
    - “OK. I'll be back once I'm done with your task.” → [lodar_13](#d-lodar_13)

    <span id="d-lodar_find1"></span>**`lodar_find1`** Lodar: “Give me that. Oh, yes ... yes!” — **effects:** sets stage 50 of [Searching for madness](../quests/lodar2.md#stage-50)

    - Next → [lodar_find2](#d-lodar_find2)

    <span id="d-lodar_2"></span>**`lodar_2`** Lodar: “Well, it doesn't matter who you are anyway. I am Lodar, maker of potions.” — **effects:** sets stage 110 of [A lost potion](../quests/lodar.md#stage-110)

    - “I was sent to find you, I'm looking for my brother, Andor - have you seen him?” → [lodar_2a](#d-lodar_2a)

    <span id="d-lodar_1"></span>**`lodar_1`** Lodar: “Maybe over there... Yikes! Who are you!?”

    - “I'm $playername.” → [lodar_2](#d-lodar_2)

    <span id="d-lodar_pots0"></span>**`lodar_pots0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Lodar's potions](../quests/lodar_pots.md#stage-40))* → [lodar_spo0](#d-lodar_spo0)
    - branch 2 *(if reached stage 30 of [Lodar's potions](../quests/lodar_pots.md#stage-30))* → [lodar_pots6](#d-lodar_pots6)
    - branch 3 *(if reached stage 10 of [Lodar's potions](../quests/lodar_pots.md#stage-10))* → [lodar_pots4](#d-lodar_pots4)
    - branch 4 → [lodar_pots1](#d-lodar_pots1)

    <span id="d-lodar_forest0"></span>**`lodar_forest0`** Lodar: “I try to keep to myself. Not many people find their way to my cabin here.”

    - Next → [lodar_forest1](#d-lodar_forest1)

    <span id="d-lodar_xul0"></span>**`lodar_xul0`** Lodar: “No! Get that thing away from me, I want nothing to do with it. I can almost hear the cries of the many lives that that thing has taken.”

    - Next → [lodar_xul1](#d-lodar_xul1)

    <span id="d-lodar_hira0"></span>**`lodar_hira0`** Lodar: “Ah yes, the Hira'zinn. It nearly had me fully in its grasp as well.”

    - “You seemed quite obsessed before.” → [lodar_hira1](#d-lodar_hira1)
    - “You seem a bit crazy to me.” → [lodar_hira1](#d-lodar_hira1)

    <span id="d-lodar_andor0"></span>**`lodar_andor0`** Lodar: “Oh, you must be referring to that older boy that was here recently.”

    - “You've seen him? Andor has been here?” → [lodar_andor1](#d-lodar_andor1)

    <span id="d-lodar_shortcut_0"></span>**`lodar_shortcut_0`** Lodar: “Hmm, I remember seeing a cave under the former cave of the Hira'zinn. I don't know where it leads to but maybe you could give it a try and search for a shortcut through this cave?” — **effects:** sets stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10)

    - “Thanks for your advice! I'll check it out!” → *conversation ends*

    <span id="d-shortcut_lodar_1"></span>**`shortcut_lodar_1`** Lodar: “Hmm, this is interesting. I have heard of such artifacts being teleporters but have never seen one myself. Here, take this vial and pour it over the torch. We will see what happens. I should tell you that this may be very dangerous. The…” — **effects:** gives 1× [Lodar's activation vial](../items/vial_activation.md), sets stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30)

    - “Thanks, I'll try it. Danger is my specialty.” → *conversation ends*
    - “I hope it will be OK.” → *conversation ends*

    <span id="d-shortcut_lodar_2"></span>**`shortcut_lodar_2`** Lodar: “Well, that's great to hear. But don't tell this to anybody else because I don't want to have some Feygard soldiers in front of my house one day.”

    - “Sure, this will be a secret between us.” → [lodar_d1](#d-lodar_d1)
    - “[Lie] Sure, this will be a secret between us.” → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_rest"></span>**`lodar_rest`** Lodar: “Sure feel free to use any bed in the main hall you like.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_find7"></span>**`lodar_find7`** Lodar: “So, thank you. I am in your debt. Now, how could I repay you?”

    - Next → [lodar_find8](#d-lodar_find8)

    <span id="d-lodar_find4"></span>**`lodar_find4`** Lodar: “Well, I feel much better now.” — **effects:** sets stage 51 of [Searching for madness](../quests/lodar2.md#stage-51)

    - Next → [lodar_find5](#d-lodar_find5)

    <span id="d-lodar_13"></span>**`lodar_13`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [A lost potion](../quests/lodar.md#stage-100))* → [lodar_13a](#d-lodar_13a)
    - branch 2 → [lodar_13b](#d-lodar_13b)

    <span id="d-lodar_2a"></span>**`lodar_2a`** Lodar: “Don't know. What difference does it make? I must get all this done before the Hira'zinn moves.”

    - “The Hira'zinn?” → [lodar_3](#d-lodar_3)

    <span id="d-lodar_spo0"></span>**`lodar_spo0`** Lodar: “With the Spotted Hornbeam fungus that you brought, I can either do a mixture that makes you think you're stronger than you actually are, or a mixture that makes you resist attacks more. There's also the skin-hardening potion, of course.”

    - “I'd like to see what regular potions you have available.” → *shop opens*
    - “Never mind that, let's go back to the other things we were discussing.” → [lodar_d1](#d-lodar_d1)
    - “What about the strength potion?” → [lodar_spo1_0](#d-lodar_spo1_0)
    - “What about the resistance potion?” → [lodar_spo2_0](#d-lodar_spo2_0)
    - “What about the hardening potion?” → [lodar_spo3_0](#d-lodar_spo3_0)

    <span id="d-lodar_pots6"></span>**`lodar_pots6`** Lodar: “The Spotted Hornbeam fungus is an excellent reagent for creating potent mixtures.”

    - Next → [lodar_pots7](#d-lodar_pots7)

    <span id="d-lodar_pots4"></span>**`lodar_pots4`** Lodar: “Yes, were you able to get some of that Spotted Hornbeam fungus from the potion-maker in Fallhaven?”

    - “No, not yet. I'd like to see what potions you have available right now.” → *shop opens*
    - “Yes, here it is.” *(if hand over 1× [Spotted Hornbeam fungus](../items/hornbeam.md))* → [lodar_pots5](#d-lodar_pots5)

    <span id="d-lodar_pots1"></span>**`lodar_pots1`** Lodar: “Oh yes. These are the ones I have available right now. If you want, I can also create some other special potions for you.”

    - “Let me see the ones you have.” → *shop opens*
    - “Special potions?” → [lodar_pots2](#d-lodar_pots2)

    <span id="d-lodar_forest1"></span>**`lodar_forest1`** Lodar: “I like that. That way, I am not bothered, like I used to be.”

    - “Like you used to be?” → [lodar_forest2](#d-lodar_forest2)

    <span id="d-lodar_xul1"></span>**`lodar_xul1`** Lodar: “I tell you - that thing should be destroyed.”

    - “How can I do that?” → [lodar_xul2](#d-lodar_xul2)
    - “I think I'll hold on to it a bit longer.” → [lodar_xul2](#d-lodar_xul2)

    <span id="d-lodar_hira1"></span>**`lodar_hira1`** Lodar: “That's the effect of the Hira'zinn. Its desire is to consume the minds of all it finds.”

    - Next → [lodar_hira2](#d-lodar_hira2)

    <span id="d-lodar_andor1"></span>**`lodar_andor1`** Lodar: “He did not tell me his name, but he had some similarities to how you look. Yes, then he probably was the person you are looking for.”

    - Next → [lodar_andor2](#d-lodar_andor2)

    <span id="d-lodar_find8"></span>**`lodar_find8`** Lodar: “Maybe you would be interested in purchasing some of my brews, mixtures or herbal salts? I am afraid that is the only thing of any worth that I possess. I will of course offer you a discount.”

    - “That will do nicely. Thank you.” → [lodar_find10a](#d-lodar_find10a)
    - “I killed that foul thing and saved us all, and all I get in return is a few lousy potions?” → [lodar_find10b](#d-lodar_find10b)

    <span id="d-lodar_13a"></span>**`lodar_13a`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 30 of [Searching for madness](../quests/lodar2.md#stage-30)

    - branch 1 → [lodar_13b](#d-lodar_13b)

    <span id="d-lodar_13b"></span>**`lodar_13b`** Lodar: “Good. Now, hurry, before the Hira'zinn moves again!”


    <span id="d-lodar_3"></span>**`lodar_3`** Lodar: “Yes yes, the Hira'zinn. As I said, I must find the correct mixture before it moves again.” — **effects:** sets stage 10 of [Searching for madness](../quests/lodar2.md#stage-10)

    - Next → [lodar_4](#d-lodar_4)

    <span id="d-lodar_spo1_0"></span>**`lodar_spo1_0`** Lodar: “Have you ever noticed how insects are able to lift things that are much larger than themselves? As it turns out, I have discovered that if you mix some ground up insect wings together with the dried body of a spider, you can experience…” — **effects:** sets stage 42 of [Lodar's potions](../quests/lodar_pots.md#stage-42)

    - “I'll go find some of that. Let's talk about the other potions.” → [lodar_spo0](#d-lodar_spo0)
    - “I have those things on me, here.” *(if hand over 1× [Dead spider](../items/spider.md); hand over 1× [Insect wing](../items/insectwing.md))* → [lodar_spo1_5](#d-lodar_spo1_5)
    - “I have enough of those things on me for five potions, here.” *(if hand over 5× [Dead spider](../items/spider.md); hand over 5× [Insect wing](../items/insectwing.md))* → [lodar_spo1_5x5](#d-lodar_spo1_5x5)
    - “I have enough of those things on me for ten potions, here.” *(if hand over 10× [Dead spider](../items/spider.md); hand over 10× [Insect wing](../items/insectwing.md))* → [lodar_spo1_5x10](#d-lodar_spo1_5x10)

    <span id="d-lodar_spo2_0"></span>**`lodar_spo2_0`** Lodar: “I have discovered that if you mix some ground up claws from a beast called the white wyrm, together with a slight sprinkle of the center of a ruby gem, it can have a most interesting effect on you. Two of those claws and one gem would do.” — **effects:** sets stage 41 of [Lodar's potions](../quests/lodar_pots.md#stage-41)

    - “I'll go find some of that. Let's talk about the other potions.” → [lodar_spo0](#d-lodar_spo0)
    - “I have those things on me, here.” *(if hand over 2× [White wyrm claw](../items/bwm_claws.md); hand over 1× [Ruby gem](../items/gem2.md))* → [lodar_spo2_5](#d-lodar_spo2_5)
    - “I have enough of those things on me for five potions, here.” *(if hand over 10× [White wyrm claw](../items/bwm_claws.md); hand over 5× [Ruby gem](../items/gem2.md))* → [lodar_spo2_5x5](#d-lodar_spo2_5x5)
    - “I have enough of those things on me for ten potions, here.” *(if hand over 20× [White wyrm claw](../items/bwm_claws.md); hand over 10× [Ruby gem](../items/gem2.md))* → [lodar_spo2_5x10](#d-lodar_spo2_5x10)

    <span id="d-lodar_spo3_0"></span>**`lodar_spo3_0`** Lodar: “Up in the north, I have heard tales of beast called the arulir. Their skin is thick as bark due to the interesting oily substance that they produce. I have learned that if you extract some of that thick oily substance, and mix it with an…” — **effects:** sets stage 43 of [Lodar's potions](../quests/lodar_pots.md#stage-43)

    - “I'll go find some of that. Let's talk about the other potions.” → [lodar_spo0](#d-lodar_spo0)
    - “I have those things on me, here.” *(if hand over 2× [Arulir skin](../items/arulir_skin.md); hand over 1× [Claws](../items/claws.md))* → [lodar_spo3_5](#d-lodar_spo3_5)
    - “I have enough of those things on me for five potions, here.” *(if hand over 10× [Arulir skin](../items/arulir_skin.md); hand over 5× [Claws](../items/claws.md))* → [lodar_spo3_5x5](#d-lodar_spo3_5x5)
    - “I have enough of those things on me for ten potions, here.” *(if hand over 20× [Arulir skin](../items/arulir_skin.md); hand over 10× [Claws](../items/claws.md))* → [lodar_spo3_5x10](#d-lodar_spo3_5x10)

    <span id="d-lodar_pots7"></span>**`lodar_pots7`** Lodar: “With your help, I can now create additional potions from the remains of certain animals if you would like.” — **effects:** sets stage 40 of [Lodar's potions](../quests/lodar_pots.md#stage-40)

    - Next → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_pots5"></span>**`lodar_pots5`** Lodar: “Oh yes, this will do nicely. Good, good. Thank you, my friend.” — **effects:** sets stage 30 of [Lodar's potions](../quests/lodar_pots.md#stage-30)

    - Next → [lodar_pots6](#d-lodar_pots6)

    <span id="d-lodar_pots2"></span>**`lodar_pots2`** Lodar: “Yes, yes. I have some even more interesting recipes that I might be able to mix for you. However, I am all out of some of the most important ingredients for them.”

    - Next → [lodar_pots3](#d-lodar_pots3)

    <span id="d-lodar_forest2"></span>**`lodar_forest2`** Lodar: “Oh yes, I too grew up in the city. But that life is behind me.”

    - Next → [lodar_forest3](#d-lodar_forest3)

    <span id="d-lodar_xul2"></span>**`lodar_xul2`** Lodar: “You should go see the smith in Vile ... haven? Vile ... fall? Argh, I'm not very good at names.”

    - “Vilegard?” → [lodar_xul3](#d-lodar_xul3)

    <span id="d-lodar_hira2"></span>**`lodar_hira2`** Lodar: “I have only heard of it through tales in books. It has been many generations ago since it last showed itself.”

    - Next → [lodar_hira3](#d-lodar_hira3)

    <span id="d-lodar_andor2"></span>**`lodar_andor2`** Lodar: “You say his name is Andor? That's an odd name, don't you think?”

    - Next → [lodar_andor3](#d-lodar_andor3)

    <span id="d-lodar_find10a"></span>**`lodar_find10a`** Lodar: “Good.”

    - Next → [lodar_find11](#d-lodar_find11)

    <span id="d-lodar_find10b"></span>**`lodar_find10b`** Lodar: “Do not forget that you also saved yourself from the Hira'zinn by defeating it. Had you not done that, it would have crept up on you as well, sooner or later.”

    - Next → [lodar_find11](#d-lodar_find11)

    <span id="d-lodar_4"></span>**`lodar_4`** Lodar: “Now, where were they? Over here perhaps?”

    - Next → [lodar_5](#d-lodar_5)

    <span id="d-lodar_spo1_5"></span>**`lodar_spo1_5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo1_6](#d-lodar_spo1_6)

    <span id="d-lodar_spo1_5x5"></span>**`lodar_spo1_5x5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo1_6x5](#d-lodar_spo1_6x5)

    <span id="d-lodar_spo1_5x10"></span>**`lodar_spo1_5x10`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo1_6x10](#d-lodar_spo1_6x10)

    <span id="d-lodar_spo2_5"></span>**`lodar_spo2_5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo2_6](#d-lodar_spo2_6)

    <span id="d-lodar_spo2_5x5"></span>**`lodar_spo2_5x5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo2_6x5](#d-lodar_spo2_6x5)

    <span id="d-lodar_spo2_5x10"></span>**`lodar_spo2_5x10`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo2_6x10](#d-lodar_spo2_6x10)

    <span id="d-lodar_spo3_5"></span>**`lodar_spo3_5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo3_6](#d-lodar_spo3_6)

    <span id="d-lodar_spo3_5x5"></span>**`lodar_spo3_5x5`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo3_6x5](#d-lodar_spo3_6x5)

    <span id="d-lodar_spo3_5x10"></span>**`lodar_spo3_5x10`** Lodar: “Excellent. These will do nicely. Now, we only need to mix these with some of this ... and some of...”

    - Next → [lodar_spo3_6x10](#d-lodar_spo3_6x10)

    <span id="d-lodar_pots3"></span>**`lodar_pots3`** Lodar: “If you want me to mix them for you, you'll have to help me get those ingredients.”

    - Next → [lodar_pq1](#d-lodar_pq1)

    <span id="d-lodar_forest3"></span>**`lodar_forest3`** Lodar: “Right now, this suits me well. I hope there won't be any more ... disturbances, like the one you helped with.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_xul3"></span>**`lodar_xul3`** Lodar: “Vilegard - yes, that's the place. You should go see the smith there. He might be able to guide you further.” — **effects:** sets stage 10 of [A creeping fear](../quests/xulviir.md#stage-10)

    - Next → [lodar_xul4](#d-lodar_xul4)

    <span id="d-lodar_hira3"></span>**`lodar_hira3`** Lodar: “Last time it crept up on the world, it got its grip on whole villages, I've read. People were fighting their own brethren, after having been consumed by the Hira'zinn.”

    - Next → [lodar_hira4](#d-lodar_hira4)

    <span id="d-lodar_andor3"></span>**`lodar_andor3`** Lodar: “Anyway, enough of that. What would you like to know?”

    - “What was he doing here?” → [lodar_andor4](#d-lodar_andor4)

    <span id="d-lodar_find11"></span>**`lodar_find11`** Lodar: “I can assure you that my mixtures are ... well ... shall we say ... not for the faint of heart. They can have quite a profound effect on you.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_5"></span>**`lodar_5`** Lodar: “No, maybe I should add some of the...”

    - “Is there anything I can do to help?” → [lodar_6a](#d-lodar_6a)
    - “What's going on here, why are you in such a hurry?” → [lodar_6b](#d-lodar_6b)

    <span id="d-lodar_spo1_6"></span>**`lodar_spo1_6`** Lodar: “There. One mixture for you.” — **effects:** gives [Minor potion of strength](../items/pot_str.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo1_6x5"></span>**`lodar_spo1_6x5`** Lodar: “There. Five mixtures for you.” — **effects:** gives [Minor potion of strength](../items/pot_str.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo1_6x10"></span>**`lodar_spo1_6x10`** Lodar: “There. Ten mixtures for you.” — **effects:** gives [Minor potion of strength](../items/pot_str.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo2_6"></span>**`lodar_spo2_6`** Lodar: “There. One mixture for you.” — **effects:** gives [Potion of improved defense](../items/pot_def.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo2_6x5"></span>**`lodar_spo2_6x5`** Lodar: “There. Five mixtures for you.” — **effects:** gives [Potion of improved defense](../items/pot_def.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo2_6x10"></span>**`lodar_spo2_6x10`** Lodar: “There. Ten mixtures for you.” — **effects:** gives [Potion of improved defense](../items/pot_def.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo3_6"></span>**`lodar_spo3_6`** Lodar: “There. One mixture for you.” — **effects:** gives [Potion of bark skin](../items/pot_barkskin.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo3_6x5"></span>**`lodar_spo3_6x5`** Lodar: “There. Five mixtures for you.” — **effects:** gives [Potion of bark skin](../items/pot_barkskin.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_spo3_6x10"></span>**`lodar_spo3_6x10`** Lodar: “There. Ten mixtures for you.” — **effects:** gives [Potion of bark skin](../items/pot_barkskin.md)

    - “Thank you. About those other potions...” → [lodar_spo0](#d-lodar_spo0)

    <span id="d-lodar_pq1"></span>**`lodar_pq1`** Lodar: “Actually, the most important ingredient is the one that I am out of. Most of the potent mixtures that I know of require the spores from the Spotted Hornbeam fungus.”

    - Next → [lodar_pq2](#d-lodar_pq2)

    <span id="d-lodar_xul4"></span>**`lodar_xul4`** Lodar: “Anyway, It's good that you defeated the Hira'zinn. I can't imagine what could have happened if the Hira'zinn would have given that thing into the wrong hands.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_hira4"></span>**`lodar_hira4`** Lodar: “Imagine, sisters and brothers fighting, husbands and wives going at each others throats, all because the Hira'zinn had twisted their minds.”

    - “Let's go back to the other questions.” → [lodar_d1](#d-lodar_d1)
    - “What caused it to appear the last time?” → [lodar_hira5](#d-lodar_hira5)
    - “Hah, those people seem like weaklings. That thing was no match for me, I could have defeated it while blindfolded even.” → [lodar_hira4b](#d-lodar_hira4b)

    <span id="d-lodar_andor4"></span>**`lodar_andor4`** Lodar: “Well, even from the first time I saw him, I knew something odd was going on.”

    - Next → [lodar_andor5](#d-lodar_andor5)

    <span id="d-lodar_6a"></span>**`lodar_6a`** Lodar: “Oh yes. Can you please move a bit, you are in the way. Can't you see I'm busy with finding a way to stop the spread of the Hira'zinn here?”

    - “You are still not making any sense to me. What is this Hira'zinn that you keep mentioning?” → [lodar_7](#d-lodar_7)
    - “Very well, I'll leave you to it. Good luck.” → *conversation ends*

    <span id="d-lodar_6b"></span>**`lodar_6b`** Lodar: “Didn't I tell you? I must find the correct mixture before the Hira'zinn spreads further.”

    - “You are still not making any sense to me. What is this Hira'zinn that you keep mentioning?” → [lodar_7](#d-lodar_7)
    - “OK then. I'll leave you to it. Good luck.” → *conversation ends*

    <span id="d-lodar_pq2"></span>**`lodar_pq2`** Lodar: “And that, my friend, is not easy to come by here in the forest. Believe me, I have scoured the nearby forest in search for it, and I have even tried to cultivate some of it myself, to no avail.”

    - Next → [lodar_pq3](#d-lodar_pq3)

    <span id="d-lodar_hira5"></span>**`lodar_hira5`** Lodar: “I do not know. The tales I have read do not tell how or why it all started - only that there was some kind of conflict going on at that time.”

    - Next → [lodar_hira6](#d-lodar_hira6)

    <span id="d-lodar_hira4b"></span>**`lodar_hira4b`** Lodar: “Now, don't be so quick to underestimate the Hira'zinn. It has many tricks up its sleeve.”

    - “Let's go back to the other questions.” → [lodar_d1](#d-lodar_d1)
    - “What caused it to appear the last time?” → [lodar_hira5](#d-lodar_hira5)

    <span id="d-lodar_andor5"></span>**`lodar_andor5`** Lodar: “He seemed overly friendly to me, almost like he seemed to know me already.”

    - Next → [lodar_andor6](#d-lodar_andor6)

    <span id="d-lodar_7"></span>**`lodar_7`** Lodar: “Everything was fine up until a few days ago. That's when everything started to happen.”

    - Next → [lodar_8](#d-lodar_8)

    <span id="d-lodar_pq3"></span>**`lodar_pq3`** Lodar: “However, I can imagine that the merchants in the larger settlements might have some.”

    - “Do you want me to find you some of that fungus?” → [lodar_pq4](#d-lodar_pq4)
    - “I'll help.” → [lodar_pq4](#d-lodar_pq4)

    <span id="d-lodar_hira6"></span>**`lodar_hira6`** Lodar: “The wise men during those days also spoke of having seen some sort of signs before things got worse.”

    - “What sort of signs?” → [lodar_hira7](#d-lodar_hira7)

    <span id="d-lodar_andor6"></span>**`lodar_andor6`** Lodar: “You should know that most people that stumble into my cabin here have either been lost in the maze some time, or are just happy to see another living being.”

    - Next → [lodar_andor7](#d-lodar_andor7)

    <span id="d-lodar_8"></span>**`lodar_8`** Lodar: “It never used to be like this, or did it? I can't remember.” — **effects:** sets stage 15 of [Searching for madness](../quests/lodar2.md#stage-15)

    - Next → [lodar_9](#d-lodar_9)

    <span id="d-lodar_pq4"></span>**`lodar_pq4`** Lodar: “Yes please. Maybe the potion-maker in that Fall-something town has some? Fall ... brim? Fall ... port?”

    - “Fallhaven? The potion maker in Fallhaven?” → [lodar_pq5](#d-lodar_pq5)

    <span id="d-lodar_hira7"></span>**`lodar_hira7`** Lodar: “I don't know. Something about some rocks turning to life. Sounds like crazy-talk to me.”

    - “Yes, maybe they too were affected by the Hira'zinn?” → [lodar_hira7a](#d-lodar_hira7a)
    - “I saw some odd looking rock formations on my way here through the forest. Some of them even seemed to have some inner…” → [lodar_hira9](#d-lodar_hira9)

    <span id="d-lodar_andor7"></span>**`lodar_andor7`** Lodar: “He showed no such signs. Almost like he knew who I was and that he expected me to be here.”

    - Next → [lodar_andor8](#d-lodar_andor8)

    <span id="d-lodar_9"></span>**`lodar_9`** Lodar: “Doesn't matter. I must make it stop anyway.”

    - Next → [lodar_10](#d-lodar_10)

    <span id="d-lodar_pq5"></span>**`lodar_pq5`** Lodar: “Yes, that's what I was looking for. Fallhaven. Go visit him and ask him if he has some. I am sure he has some, if you know enough to ask.” — **effects:** sets stage 10 of [Lodar's potions](../quests/lodar_pots.md#stage-10)

    - “I'll do that. Goodbye.” → *conversation ends*

    <span id="d-lodar_hira7a"></span>**`lodar_hira7a`** Lodar: “Yes, they might have been.”

    - Next → [lodar_hira8](#d-lodar_hira8)

    <span id="d-lodar_hira9"></span>**`lodar_hira9`** Lodar: “Formations of rocks you say? Hmm. I don't recall seeing any of that the last time I ventured out.”

    - Next → [lodar_hira10](#d-lodar_hira10)

    <span id="d-lodar_andor8"></span>**`lodar_andor8`** Lodar: “He very kindly asked for some Narwood extract.”

    - “Narwood extract, what's that?” → [lodar_andor9](#d-lodar_andor9)
    - “I recognize that name 'Narwood extract' from somewhere.” *(if reached stage 54 of [Flows through the veins](../quests/loneford.md#stage-54))* → [lodar_andor9](#d-lodar_andor9)

    <span id="d-lodar_10"></span>**`lodar_10`** Lodar: “Maybe it was in here...”

    - Next → [lodar_11](#d-lodar_11)

    <span id="d-lodar_hira8"></span>**`lodar_hira8`** Lodar: “Anyway, it's good that you defeated that thing.”

    - Next → [lodar_d1](#d-lodar_d1)

    <span id="d-lodar_hira10"></span>**`lodar_hira10`** Lodar: “Could that be how the Hira'zinn extends its reach?”

    - Next → [lodar_hira11](#d-lodar_hira11)

    <span id="d-lodar_andor9"></span>**`lodar_andor9`** Lodar: “It can be used to make quite a nasty poison.”

    - “Please continue.” → [lodar_andor10](#d-lodar_andor10)
    - “Oh right. I've visited a village whose town well had been poisoned with that.” *(if reached stage 54 of [Flows through the veins](../quests/loneford.md#stage-54))* → [lodar_andor9a](#d-lodar_andor9a)

    <span id="d-lodar_11"></span>**`lodar_11`** Lodar: “No ... hmm, wait. You! Maybe you can be of use here, if you are willing to help?”

    - “I'm up for it! What do you need help with?” → [lodar_12](#d-lodar_12)
    - “I'm not so sure about this. What do you need done?” → [lodar_12](#d-lodar_12)
    - “No way. You solve your own problems, old man.” → *conversation ends*

    <span id="d-lodar_hira11"></span>**`lodar_hira11`** Lodar: “Yes, that would explain a great deal. The tales speak of it slowly creeping up on the world.”

    - Next → [lodar_hira12](#d-lodar_hira12)

    <span id="d-lodar_andor10"></span>**`lodar_andor10`** Lodar: “So, he asked for a sample of Narwood extract. Normally, I wouldn't give that out to just anyone.”

    - Next → [lodar_andor11](#d-lodar_andor11)

    <span id="d-lodar_andor9a"></span>**`lodar_andor9a`** Lodar: “Those poor poor people. They have my sympathies. I hope it's not my things that brought this misery upon them.”

    - “Please continue your story about Andor.” → [lodar_andor10](#d-lodar_andor10)

    <span id="d-lodar_12"></span>**`lodar_12`** Lodar: “[Lodar hands you an odd looking stone that seems to be glowing from within] Good. Take this stone, it will allow you to enter the tomb. Go below. Return once you're done.” — **effects:** sets stage 20 of [Searching for madness](../quests/lodar2.md#stage-20), gives [Gatekeeper stone](../items/lodarstone.md)

    - “You're not very good at giving directions, old man. I'll try to do what you ask.” → [lodar_13](#d-lodar_13)
    - “No problem. I'll return soon.” → [lodar_13](#d-lodar_13)
    - “Below? Below what? Which tomb? What are you even talking about?” → [lodar_14](#d-lodar_14)

    <span id="d-lodar_hira12"></span>**`lodar_hira12`** Lodar: “It could be that those formations are the way it gets closer to the people and things that it wants to consume.”

    - Next → [lodar_hira13](#d-lodar_hira13)

    <span id="d-lodar_andor11"></span>**`lodar_andor11`** Lodar: “However, as I said, there was something odd about this whole meeting. I actually felt a bit threatened, even though he was so polite and friendly.”

    - Next → [lodar_andor12](#d-lodar_andor12)

    <span id="d-lodar_hira13"></span>**`lodar_hira13`** Lodar: “It could be that the Hira'zinn has some way of affecting the life of the forest itself, causing these formations to appear.”

    - Next → [lodar_hira14](#d-lodar_hira14)

    <span id="d-lodar_andor12"></span>**`lodar_andor12`** Lodar: “Fearing something would happen to me if I rejected his request, I reluctantly gave him a small sample of the Narwood extract.”

    - Next → [lodar_andor13](#d-lodar_andor13)

    <span id="d-lodar_hira14"></span>**`lodar_hira14`** Lodar: “That's what I think, at least.”

    - “You still sound a bit crazy to me.” → [lodar_hira8](#d-lodar_hira8)
    - “Thanks for the explanation.” → [lodar_hira8](#d-lodar_hira8)

    <span id="d-lodar_andor13"></span>**`lodar_andor13`** Lodar: “He gladly accepted the sample, and left shortly after. That's when it started to get even more odd.”

    - “What happened?” → [lodar_andor14](#d-lodar_andor14)

    <span id="d-lodar_andor14"></span>**`lodar_andor14`** Lodar: “As he left, I happened to glance out the window. There, in the forest I saw the bright flash of the light from the sun hitting a blade.”

    - Next → [lodar_andor15](#d-lodar_andor15)

    <span id="d-lodar_andor15"></span>**`lodar_andor15`** Lodar: “If I hadn't seen that light coming off the blade, I would not have spotted the person there at all. He seemed to be hiding in the forest.”

    - “Someone was hiding in the forest?” → [lodar_andor16](#d-lodar_andor16)

    <span id="d-lodar_andor16"></span>**`lodar_andor16`** Lodar: “Yes, so it would seem. It was quite obvious that he did not want me to spot him. After your brother left, I saw them both speak some words to each other, before they both left together.” — **effects:** sets stage 70 of [Search for Andor](../quests/andor.md#stage-70)

    - “So, Andor was here, wanted some Narwood extract, and he was travelling with someone that did not want you to spot him?” → [lodar_andor17](#d-lodar_andor17)

    <span id="d-lodar_andor17"></span>**`lodar_andor17`** Lodar: “Yes, that's basically it. But that's not all.”

    - Next → [lodar_andor18](#d-lodar_andor18)

    <span id="d-lodar_andor18"></span>**`lodar_andor18`** Lodar: “Shortly after they left, strange things started happening in the forest.”

    - Next → [lodar_andor19](#d-lodar_andor19)

    <span id="d-lodar_andor19"></span>**`lodar_andor19`** Lodar: “I saw a pack of wolves that were fighting each other. Tearing up each others sides, and eating the remains.”

    - Next → [lodar_andor20](#d-lodar_andor20)

    <span id="d-lodar_andor20"></span>**`lodar_andor20`** Lodar: “I saw birds flying over my cabin, totally covered in red blood. Blood covered birds - now that's something that I have not even heard about.”

    - Next → [lodar_andor21](#d-lodar_andor21)

    <span id="d-lodar_andor21"></span>**`lodar_andor21`** Lodar: “I tell you, something affected the forest. Myself, I felt my stomach turning even more often than it usually does.”

    - Next → [lodar_andor22](#d-lodar_andor22)

    <span id="d-lodar_andor22"></span>**`lodar_andor22`** Lodar: “I had this strong urge to eat more than usual. I even found myself having lapses of time where I could not remember what I had done for the past couple of hours.”

    - “What could have been causing that?” → [lodar_andor23](#d-lodar_andor23)

    <span id="d-lodar_andor23"></span>**`lodar_andor23`** Lodar: “In hindsight, I think it's pretty clear what started to happen. The Hira'zinn awoke. To make matters worse, at least for me, it awoke in the tomb beneath my cabin here.”

    - Next → [lodar_andor24](#d-lodar_andor24)

    <span id="d-lodar_andor24"></span>**`lodar_andor24`** Lodar: “What I find disturbing is that this all started to happen right after your brother and that other person were here.”

    - Next → [lodar_andor25](#d-lodar_andor25)

    <span id="d-lodar_andor25"></span>**`lodar_andor25`** Lodar: “Maybe they visited that tomb. Now, I'm not pointing any fingers here, but it certainly seems like they had something to do with this, considering that the tomb has been quiet for ages.” — **effects:** sets stage 71 of [Search for Andor](../quests/andor.md#stage-71)

    - “Are you implying that Andor awoke the Hira'zinn?” → [lodar_andor25a](#d-lodar_andor25a)
    - “Interesting. Please go on.” → [lodar_andor26](#d-lodar_andor26)
    - “I don't think I like where you're going with this. Andor is my brother, and he would never do such a thing.” → [lodar_andor25a](#d-lodar_andor25a)

    <span id="d-lodar_andor25a"></span>**`lodar_andor25a`** Lodar: “I don't know the details of course, and I have no proof. I only know that asking for Narwood extract is an odd request, and that the Hira'zinn started to creep up on me shortly after that.”

    - Next → [lodar_andor26](#d-lodar_andor26)

    <span id="d-lodar_andor26"></span>**`lodar_andor26`** Lodar: “Now, I am no expert in these things. I have only read bits and pieces from old books. I mostly focus my thoughts on herbs, mixtures and potions.”

    - Next → [lodar_andor27](#d-lodar_andor27)

    <span id="d-lodar_andor27"></span>**`lodar_andor27`** Lodar: “But I do know other people that might be able to provide you with further guidance.”

    - Next → [lodar_andor28](#d-lodar_andor28)

    <span id="d-lodar_andor28"></span>**`lodar_andor28`** Lodar: “Since you defeated the Hira'zinn, I think those people would be more than happy to speak to you. I would be happy to help you in any way I can too, of course.”

    - “Who do you have in mind?” → [lodar_andor29](#d-lodar_andor29)

    <span id="d-lodar_andor29"></span>**`lodar_andor29`** Lodar: “Seek out Lady Lydalon in the Valanyr temple of the Shadow in Nor City. She is one of the wisest people I know, and an excellent mentor.”

    - Next → [lodar_andor30s](#d-lodar_andor30s)

    <span id="d-lodar_andor30s"></span>**`lodar_andor30s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72))* → [lodar_andor31](#d-lodar_andor31)
    - branch 2 → [lodar_andor30](#d-lodar_andor30)

    <span id="d-lodar_andor31"></span>**`lodar_andor31`** Lodar: “Present the letter to the guards at the temple, and they will grant you an audience with Lady Lydalon.”

    - Next → [lodar_andor32](#d-lodar_andor32)

    <span id="d-lodar_andor30"></span>**`lodar_andor30`** Lodar: “Here, take this letter.” — **effects:** gives [Lodar's letter](../items/lodar_letter.md), sets stage 72 of [Search for Andor](../quests/andor.md#stage-72)

    - Next → [lodar_andor31](#d-lodar_andor31)

    <span id="d-lodar_andor32"></span>**`lodar_andor32`** Lodar: “Also, while you're there, please give her my warmest regards. It has been too long since I last visited her.”

    - “I will go to Nor City and visit Lady Lydalon in the Valanyr temple of the Shadow.” → [lodar_andor33](#d-lodar_andor33)
    - “He he, a temple. That must mean a lot of riches in there.” → [lodar_andor32a](#d-lodar_andor32a)

    <span id="d-lodar_andor33"></span>**`lodar_andor33`** Lodar: “Just one more thing.”

    - Next → [lodar_andor34](#d-lodar_andor34)

    <span id="d-lodar_andor32a"></span>**`lodar_andor32a`** Lodar: “Show some respect will you?”

    - Next → [lodar_andor33](#d-lodar_andor33)

    <span id="d-lodar_andor34"></span>**`lodar_andor34`** Lodar: “The person that was hiding among the trees here, that your brother was travelling with - I happened to get a quick view of his cloak.”

    - Next → [lodar_andor35](#d-lodar_andor35)

    <span id="d-lodar_andor35"></span>**`lodar_andor35`** Lodar: “I've seen cloaks like that before. The fabric is similar to a fabric commonly used in Nor City.”

    - Next → [lodar_andor36](#d-lodar_andor36)

    <span id="d-lodar_andor36"></span>**`lodar_andor36`** Lodar: “It could mean that whatever group of people he belongs to - there might be more of them in Nor City. Either you might want to stay away from them, or seek them out. You decide.” — **effects:** sets stage 80 of [Search for Andor](../quests/andor.md#stage-80)

    - “Thank you for all the information. I will travel to Nor City.” → [lodar_andor37](#d-lodar_andor37)
    - “I can handle myself.” → [lodar_andor37](#d-lodar_andor37)
    - “Will you ever stop talking?” → [lodar_andor37](#d-lodar_andor37)

    <span id="d-lodar_andor37"></span>**`lodar_andor37`** Lodar: “You have done a great deed here. Goodbye. Take care, my friend.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Dialogue: 1 line changed<br>· text: “Up in the north, I have heard tales of beast called the Arulir. Their…” → “Up in the north, I have heard tales of beast called the Arulir. Their…” |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines added, 40 lines changed<br>· text: “Give me that. Oh, yes.. Yes!” → “Give me that. Oh, yes ... yes!”<br>· text: “Excellent. These will do nicely. Now, we only need to mix these with …” → “Excellent. These will do nicely. Now, we only need to mix these with …” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines changed<br>· text: “I tell you, something affected the forest. Myself, I felt my stomach …” → “I tell you, something affected the forest. Myself, I felt my stomach …”<br>· text: “That's the effects of the Hira'zinn. Its desires is to consume the mi…” → “That's the effect of the Hira'zinn. Its desire is to consume the mind…” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Oh, you must be referring to that other boy that was here recently.” → “Oh, you must be referring to that older boy that was here recently.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lodar` |
    | Spawn group | `lodar` |
    | Loot table | `shop_lodar` |
    | Conversation | `lodar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:77` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "lodar",
     "name": "Lodar",
     "iconID": "monsters_rltiles1:77",
     "phraseID": "lodar",
     "droplistID": "shop_lodar"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
