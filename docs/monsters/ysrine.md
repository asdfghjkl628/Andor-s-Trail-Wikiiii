---
description: "Ysrine is a non-player character (NPC) in Andor's Trail, found in Undertell 1 1. Starts Dominion."
---

# ![](../assets/icons/monsters/monsters_newb_1_124.png){ .sprite } Ysrine

**Where to find Ysrine:** [Undertell 1 1](../maps/undertell_1_1.md#pin-npc-ysrine)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_124.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Dominion](../quests/dominion.md) |
| **Found in** | Undertell 1 1 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! note "A fight can start here"
    Answering “You followers of Kazaul - you want everything for yourself! Give…” starts a fight with [Saki](../monsters/saki.md).

## Quests

- [Dominion](../quests/dominion.md): stages 10, 20, 30, 50, 60, 70, 90
- [Undertell: What was not written](../quests/undertell_book.md): stage 30

## Dialogue simulator

Talk to Ysrine as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ysrine_selector.json" data-npc="Ysrine" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (58 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ysrine_selector"></span>**`ysrine_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 7 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-7))* → [ysrine_warn_of_master_lies_10](#d-ysrine_warn_of_master_lies_10)
    - branch 2 *(if reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10))* → [ysrine_start_devotion_10](#d-ysrine_start_devotion_10)
    - branch 3 *(if reached stage 480 of [Devotion](../quests/devotion.md#stage-480); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10))* → [ysrine_start_devotion_10](#d-ysrine_start_devotion_10)
    - branch 4 *(if reached stage 30 of [Dominion](../quests/dominion.md#stage-30); NOT reached stage 50 of [Dominion](../quests/dominion.md#stage-50))* → [ysrine_dominion_saki_fleed_10](#d-ysrine_dominion_saki_fleed_10)
    - branch 5 *(if reached stage 50 of [Dominion](../quests/dominion.md#stage-50); NOT reached stage 60 of [Dominion](../quests/dominion.md#stage-60))* → [ysrine_dominion_saki_fleed_60](#d-ysrine_dominion_saki_fleed_60)
    - branch 6 *(if reached stage 60 of [Dominion](../quests/dominion.md#stage-60); NOT killed 1× [Saki](../monsters/saki.md))* → [ysrine_saki_not_killed](#d-ysrine_saki_not_killed)
    - branch 7 *(if killed 1× [Saki](../monsters/saki.md); NOT reached stage 90 of [Dominion](../quests/dominion.md#stage-90))* → [ysrine_saki_killed_10](#d-ysrine_saki_killed_10)
    - branch 8 → [ysrine_default_10](#d-ysrine_default_10)

    <span id="d-ysrine_warn_of_master_lies_10"></span>**`ysrine_warn_of_master_lies_10`** Ysrine: “You have spoken with one of them, haven't you? Their words cling to you. Be careful what promises you keep down here.”

    - “They spoke of balance. I am not sure what they meant.” → [ysrine_warn_of_master_lies_20](#d-ysrine_warn_of_master_lies_20)
    - “I did. Do you know what they want?” → [ysrine_warn_of_master_lies_30](#d-ysrine_warn_of_master_lies_30)
    - “I wanted to talk about something else. The Kha'zaan to be specific.” *(if reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10))* → [ysrine_start_devotion_10](#d-ysrine_start_devotion_10)
    - “I wanted to talk about something else. The Kha'zaan to be specific.” *(if reached stage 480 of [Devotion](../quests/devotion.md#stage-480); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10))* → [ysrine_start_devotion_10](#d-ysrine_start_devotion_10)
    - “I found a book about Undertell. Do you know it?” *(if carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md); NOT reached stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90))* → [ysrine_undertell_book_intro](#d-ysrine_undertell_book_intro)
    - “Actually, I want to talk about Saki.” *(if reached stage 30 of [Dominion](../quests/dominion.md#stage-30); NOT reached stage 50 of [Dominion](../quests/dominion.md#stage-50))* → [ysrine_dominion_saki_fleed_20](#d-ysrine_dominion_saki_fleed_20)
    - “Where is Saki now?” *(if reached stage 50 of [Dominion](../quests/dominion.md#stage-50); NOT reached stage 60 of [Dominion](../quests/dominion.md#stage-60))* → [ysrine_dominion_saki_fleed_60](#d-ysrine_dominion_saki_fleed_60)
    - “I destroyed Saki.” *(if NOT reached stage 90 of [Dominion](../quests/dominion.md#stage-90); killed 1× [Saki](../monsters/saki.md))* → [ysrine_saki_killed_10](#d-ysrine_saki_killed_10)

    <span id="d-ysrine_start_devotion_10"></span>**`ysrine_start_devotion_10`** Ysrine: “Thank you! It's because of you that we are rid of the remnants of the Kha'zaan. On that note, there's someone here to meet you.”

    - Next → [ysrine_start_devotion_15](#d-ysrine_start_devotion_15)

    <span id="d-ysrine_dominion_saki_fleed_10"></span>**`ysrine_dominion_saki_fleed_10`** Ysrine: “Oh no. Just as I feared.”

    - “What just happened?” → [ysrine_dominion_saki_fleed_20](#d-ysrine_dominion_saki_fleed_20)

    <span id="d-ysrine_dominion_saki_fleed_60"></span>**`ysrine_dominion_saki_fleed_60`** Ysrine: “Saki is trying to flee Undertell. Find him, defeat him, and recover the soul pearls and anything else he carries. Bring them back here.” — **effects:** sets stage 60 of [Dominion](../quests/dominion.md#stage-60), spawns monsters on undertell_exit

    - “Looks like no one can be trusted.” → [ysrine_dominion_saki_fleed_70](#d-ysrine_dominion_saki_fleed_70)

    <span id="d-ysrine_saki_not_killed"></span>**`ysrine_saki_not_killed`** Ysrine: “This is no time to be fooling around. Please get those pearls back.”


    <span id="d-ysrine_saki_killed_10"></span>**`ysrine_saki_killed_10`** Ysrine: “Good - you're back...”

    - Next → [ysrine_saki_killed_selector](#d-ysrine_saki_killed_selector)

    <span id="d-ysrine_default_10"></span>**`ysrine_default_10`** Ysrine: “Oh, a human child, here? How did that come about?”

    - “Shannal let me through. Can I ask you, why do you look different than the others here?” → [ysrine_looks_10](#d-ysrine_looks_10)

    <span id="d-ysrine_warn_of_master_lies_20"></span>**`ysrine_warn_of_master_lies_20`** Ysrine: “Balance can mean many things. For them, it once meant chains and silence. Listen closely, but never forget they speak for themselves, not for you.”

    - “I will keep that in mind.” → *conversation ends*

    <span id="d-ysrine_warn_of_master_lies_30"></span>**`ysrine_warn_of_master_lies_30`** Ysrine: “No one truly knows what the Masters want anymore. Even they may have forgotten. Just remember this: "truth and deceit sound much the same when spoken by the dead".”

    - “You sound like you don't trust them.” → [ysrine_warn_of_master_lies_40](#d-ysrine_warn_of_master_lies_40)

    <span id="d-ysrine_undertell_book_intro"></span>**`ysrine_undertell_book_intro`** Ysrine: “Written histories come easily to stone and steel. They are less kind to breath, fear, and hunger.”

    - “It feels like something is missing.” *(if NOT reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40))* → [ysrine_undertell_book_missing](#d-ysrine_undertell_book_missing)
    - “A book collector from Fallhaven asked me to listen to the ghosts of Undertell.” *(if reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40))* → [ysrine_undertell_after_arcir](#d-ysrine_undertell_after_arcir)
    - “I will think on that.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_dominion_saki_fleed_20"></span>**`ysrine_dominion_saki_fleed_20`** Ysrine: “Like I feared. He was up to no good.”

    - “Well... what happened?” → [ysrine_dominion_saki_fleed_30](#d-ysrine_dominion_saki_fleed_30)

    <span id="d-ysrine_start_devotion_15"></span>**`ysrine_start_devotion_15`** Ysrine: “Here, on my left.” — **effects:** spawns monsters on undertell_1_1, sets stage 10 of [Dominion](../quests/dominion.md#stage-10)

    - Next → [saki_selector](#d-saki_selector)

    <span id="d-ysrine_dominion_saki_fleed_70"></span>**`ysrine_dominion_saki_fleed_70`** Ysrine: “In the end, trust is still required. Without it, we would already be lost.”


    <span id="d-ysrine_saki_killed_selector"></span>**`ysrine_saki_killed_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT carry 5× [Soul pearl](../items/soul_pearl.md))* → [ysrine_saki_killed_12](#d-ysrine_saki_killed_12)
    - Next *(if carry 5× [Soul pearl](../items/soul_pearl.md))* → [ysrine_saki_killed_13](#d-ysrine_saki_killed_13)

    <span id="d-ysrine_looks_10"></span>**`ysrine_looks_10`** Ysrine: “This is what happened when he died [point to the man at the table]. That is what happened when they died [pointing east]. It's all very personal.”

    - “[puzzled] Oh, I see.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_warn_of_master_lies_40"></span>**`ysrine_warn_of_master_lies_40`** Ysrine: “Trust is for the living. Down here, it's better to doubt everything, even me.”

    - “I will remember that.” → *conversation ends*

    <span id="d-ysrine_undertell_book_missing"></span>**`ysrine_undertell_book_missing`** Ysrine: “What is measured can be counted. What is endured must be remembered. Undertell has little love for the latter.”

    - “You think the book leaves things out?” → [ysrine_undertell_omission](#d-ysrine_undertell_omission)
    - “Thank you.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_undertell_after_arcir"></span>**`ysrine_undertell_after_arcir`** Ysrine: “Then you walk a quieter road than most.”

    - “What do you mean?” → [ysrine_undertell_quiet_road](#d-ysrine_undertell_quiet_road)
    - “Thank you.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_questions_10"></span>**`ysrine_questions_10`** Ysrine: “You carry questions like coins. Ask them, child.”

    - “What is this heartstone everyone speaks of?” → [ysrine_heartstone_10](#d-ysrine_heartstone_10)
    - “I found a book about Undertell. Do you know it?” *(if carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md); NOT reached stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90))* → [ysrine_undertell_book_intro](#d-ysrine_undertell_book_intro)
    - “I found these coins [showing Ysrine the rare coins] here in Undertell. Are you familiar with them?” *(if carry 1× [Rare coins](../items/rare_coins.md))* → [ysrine_question_coins_10](#d-ysrine_question_coins_10)

    <span id="d-ysrine_dominion_saki_fleed_30"></span>**`ysrine_dominion_saki_fleed_30`** Ysrine: “Saki seemed kind, even gentle. But there were inconsistencies in his stories. I assumed they came from the loss of memory that follows death. I was wrong.”

    - “Wrong how?” → [ysrine_dominion_saki_fleed_40](#d-ysrine_dominion_saki_fleed_40)

    <span id="d-saki_selector"></span>**`saki_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Dominion](../quests/dominion.md#stage-10) is 10)* → [saki_meet_10](#d-saki_meet_10)
    - branch 2 *(if reached stage 20 of [Dominion](../quests/dominion.md#stage-20); NOT reached stage 30 of [Dominion](../quests/dominion.md#stage-30))* → [saki_pearls_10](#d-saki_pearls_10)
    - branch 3 *(if reached stage 60 of [Dominion](../quests/dominion.md#stage-60))* → [saki_trapped_10](#d-saki_trapped_10)

    <span id="d-ysrine_saki_killed_12"></span>**`ysrine_saki_killed_12`** Ysrine: “but unfortunately you've come empty handed. How did you manage to drop them on the way back?”

    - “Don't be so judgemental. They are really heavy, so I didn't want to carry them around with me.” → [ysrine_saki_killed_14](#d-ysrine_saki_killed_14)

    <span id="d-ysrine_saki_killed_13"></span>**`ysrine_saki_killed_13`** Ysrine: “and you have brought the Soul pearls.”

    - “What do I do with the Soul pearls?” → [ysrine_saki_killed_20](#d-ysrine_saki_killed_20)

    <span id="d-ysrine_undertell_omission"></span>**`ysrine_undertell_omission`** Ysrine: “Those who suffered here were tools, not witnesses. Tools are used. Witnesses are avoided.”

    - “I should keep that in mind.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_undertell_quiet_road"></span>**`ysrine_undertell_quiet_road`** Ysrine: “The dead are accustomed to being spoken for. Few think to listen instead. Undertell remembers those who do.” — **effects:** sets stage 30 of [Undertell: What was not written](../quests/undertell_book.md#stage-30)

    - “I will listen.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_heartstone_10"></span>**`ysrine_heartstone_10`** Ysrine: “It is not ordinary ore. Heartstone drinks the breath of the Rift and holds it. They wanted it.”

    - “Who wanted it?” → [ysrine_heartstone_20](#d-ysrine_heartstone_20)

    <span id="d-ysrine_question_coins_10"></span>**`ysrine_question_coins_10`** Ysrine: “Oh, sorry, child. I am not knowledgeable about such things.”

    - “Oh, that's disappointing.” → [ysrine_questions_10](#d-ysrine_questions_10)

    <span id="d-ysrine_dominion_saki_fleed_40"></span>**`ysrine_dominion_saki_fleed_40`** Ysrine: “Saki was no follower of Elythara. He sought to absorb the spirits of the Elytharan mages and draw power from them. I fear he serves the Kazaul, and he must be stopped.” — **effects:** sets stage 50 of [Dominion](../quests/dominion.md#stage-50)

    - “By we, do you mean me?” → [ysrine_dominion_saki_fleed_50](#d-ysrine_dominion_saki_fleed_50)

    <span id="d-saki_meet_10"></span>**`saki_meet_10`** Ysrine: “Hello, $playername.”

    - “[freaking out] Who are you? Where did you come from?” → [saki_meet_20](#d-saki_meet_20)

    <span id="d-saki_pearls_10"></span>**`saki_pearls_10`** Ysrine: “Are you returning because you were successful in retrieving the pearls?”

    - “Yeah, here they are.” *(if hand over 5× [Soul pearl](../items/soul_pearl.md))* → [saki_pearls_20](#d-saki_pearls_20)
    - “[lie] Yes. Here you go, all five of them.” *(if NOT carry 5× [Soul pearl](../items/soul_pearl.md))* → [saki_not_5_pearls](#d-saki_not_5_pearls)

    <span id="d-saki_trapped_10"></span>**`saki_trapped_10`** Ysrine: “I'm not able to get out!”

    - Next → [saki_trapped_20](#d-saki_trapped_20)

    <span id="d-ysrine_saki_killed_14"></span>**`ysrine_saki_killed_14`** Ysrine: “Go get them and bring them back here!”


    <span id="d-ysrine_saki_killed_20"></span>**`ysrine_saki_killed_20`** Ysrine: “Besides keeping them away from those Kazaul Masters? I do not know yet. Powerful they are - they could perhaps bring Elythara back, help her re-establish her Dominion on Dhayavar. Those Pearls might be the key to bring Elythara back, and…” — **effects:** sets stage 90 of [Dominion](../quests/dominion.md#stage-90)


    <span id="d-ysrine_heartstone_20"></span>**`ysrine_heartstone_20`** Ysrine: “Long ago, the first King of Nor City, Garthan of House Houdart, sent men into Galmore to pry at the mountain. They prized what they pulled from the mountain, though few ever speak plainly of why.”

    - “What did they want it for?” → [ysrine_heartstone_30](#d-ysrine_heartstone_30)
    - “Thank you. That is enough for now.” → *conversation ends*

    <span id="d-ysrine_dominion_saki_fleed_50"></span>**`ysrine_dominion_saki_fleed_50`** Ysrine: “Unfortunately, yes.”

    - “Then what do I do?” → [ysrine_dominion_saki_fleed_60](#d-ysrine_dominion_saki_fleed_60)

    <span id="d-saki_meet_20"></span>**`saki_meet_20`** Ysrine: “Saki, my name is. Haunt this area is all I do.”

    - “Pleased to meet you...I think.” → [saki_devotion_selector](#d-saki_devotion_selector)

    <span id="d-saki_pearls_20"></span>**`saki_pearls_20`** Ysrine: “Thank you for these powerful artifacts!” — **effects:** sets stage 30 of [Dominion](../quests/dominion.md#stage-30), removes monsters from undertell_1_1


    <span id="d-saki_not_5_pearls"></span>**`saki_not_5_pearls`** Ysrine: “You still have to find all of them. Now go.”

    - “Right, I need to find five of them.” → *conversation ends*

    <span id="d-saki_trapped_20"></span>**`saki_trapped_20`** [Voice of Shannal](../monsters/voice_shannal.md): “My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername, get this guy!” — **effects:** sets stage 70 of [Dominion](../quests/dominion.md#stage-70)

    - Next → [saki_fight](#d-saki_fight)

    <span id="d-ysrine_heartstone_30"></span>**`ysrine_heartstone_30`** Ysrine: “Power and profit are plain reasons. Old families in Nor City desired advantage. That is what men call progress and what others call cost. Remember this when you carry the stone.”

    - “I will.” → *conversation ends*

    <span id="d-saki_devotion_selector"></span>**`saki_devotion_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 450 of [Devotion](../quests/devotion.md#stage-450))* → [saki_devotion_450_10](#d-saki_devotion_450_10)
    - branch 2 *(if reached stage 480 of [Devotion](../quests/devotion.md#stage-480))* → [saki_devotion_480_10](#d-saki_devotion_480_10)

    <span id="d-saki_fight"></span>**`saki_fight`** [Saki](../monsters/saki.md): “The kid can try!”

    - “It'll be my pleasure!” → [saki_fight_20](#d-saki_fight_20)

    <span id="d-saki_devotion_450_10"></span>**`saki_devotion_450_10`** Ysrine: “Kha'zaan are no more, thanks to you. Their spirits lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_devotion_480_10"></span>**`saki_devotion_480_10`** Ysrine: “Kha'zaan are no more. However, in the future, be wary, and learn not to get bamboozled. Hope you have learned your lesson.”

    - Next → [saki_devotion_480_ysrine_10](#d-saki_devotion_480_ysrine_10)

    <span id="d-saki_fight_20"></span>**`saki_fight_20`** Ysrine: “You can't have what is mine! I shall use this power to cleanse a corner of Dhayavar and make it my Dominion!”

    - “You followers of Kazaul - you want everything for yourself! Give them up!” → *fight starts*

    <span id="d-saki_dominion_10"></span>**`saki_dominion_10`** Ysrine: “Well, now you need to find more spirits in this place. Ours.”

    - “And you want me to liberate them. Why?” → [saki_dominion_20](#d-saki_dominion_20)

    <span id="d-saki_devotion_480_ysrine_10"></span>**`saki_devotion_480_ysrine_10`** [Ysrine](../monsters/ysrine.md): “Aye, little one. What were you thinking?”

    - Next → [saki_devotion_480_20](#d-saki_devotion_480_20)

    <span id="d-saki_dominion_20"></span>**`saki_dominion_20`** Ysrine: “Because while the light of Elythara may not be extinguished, it has dimmed here in Dhayavar.”

    - “Why would your colleagues be spirits? You won the war.” → [saki_dominion_30](#d-saki_dominion_30)

    <span id="d-saki_devotion_480_20"></span>**`saki_devotion_480_20`** [Saki](../monsters/saki.md): “Anyways, it was their spirits that lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_dominion_30"></span>**`saki_dominion_30`** Ysrine: “Did we win? Perhaps. Narrowly. And not decisively. The Shadow remains, and monsters from the other realm still roam freely.”

    - “They lost their bodies during the war?” → [saki_dominion_40](#d-saki_dominion_40)

    <span id="d-saki_dominion_40"></span>**`saki_dominion_40`** Ysrine: “Yes. Five of my closest colleagues lost their corporeal forms here. The magic was heavy, and Elythara's blessing caused their spirits to linger.”

    - “Like the Kha'zaan shades.” → [saki_dominion_50](#d-saki_dominion_50)

    <span id="d-saki_dominion_50"></span>**`saki_dominion_50`** Ysrine: “Er...yes. Similar. And now that the Kha'zaan are gone, they remain. Will you help them?”

    - “They will not attack me?” → [saki_dominion_60](#d-saki_dominion_60)

    <span id="d-saki_dominion_60"></span>**`saki_dominion_60`** [Lethgar miner ghost](../monsters/lethgar_miner_ghost.md): “They helped defend Dhayavar. They are not likely to harm any of us now.”

    - “Very well. What needs to be done?” → [saki_dominion_70](#d-saki_dominion_70)

    <span id="d-saki_dominion_70"></span>**`saki_dominion_70`** [Saki](../monsters/saki.md): “You are right to be wary. But I swear on Elythara, no harm will come from us.”

    - “Tell me what I must do.” → [saki_dominion_80](#d-saki_dominion_80)

    <span id="d-saki_dominion_80"></span>**`saki_dominion_80`** Ysrine: “When they fell, their souls condensed into pearls. Five in total.”

    - “Pearls?” → [saki_dominion_90](#d-saki_dominion_90)

    <span id="d-saki_dominion_90"></span>**`saki_dominion_90`** Ysrine: “Yes. Shimmering soul pearls. Liches gathered them, unaware of what they carried.”

    - “So I must destroy the liches and recover the pearls.” → [saki_dominion_100](#d-saki_dominion_100)

    <span id="d-saki_dominion_100"></span>**`saki_dominion_100`** Ysrine: “They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.” — **effects:** sets stage 20 of [Dominion](../quests/dominion.md#stage-20), spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5

    - “I will return with the soul pearls.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 58 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ysrine` |
    | Type (wiki) | NPC |
    | Spawn group | `ysrine` |
    | Loot table | – |
    | Conversation | `ysrine_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:124` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "ysrine",
     "name": "Ysrine",
     "iconID": "monsters_newb_1:124",
     "phraseID": "ysrine_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ysrine.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ysrine.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ysrine.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ysrine.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
