---
description: "Tunlon is an NPC who can also be fought in Andor's Trail, found in Blackwater Mountain. Shopkeeper; starts It makes no fence."
---

# ![](../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite } Tunlon

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper; starts [It makes no fence](../quests/tunlon_fence.md) |
| **Found in** | Blackwater Mountain |
| **Class** | Humanoid |
| **HP** | 73 |
| **XP when defeated** | 292 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Tunlon. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`tunlon`](#v-tunlon) | NPC | Blackwater Mountain: [Bwmfill 3](../maps/bwmfill3.md#pin-npc-tunlon) | shopkeeper; starts [It makes no fence](../quests/tunlon_fence.md) | – |
| [`tunlon2`](#v-tunlon2) | Enemy | Blackwater Mountain: [Bwmfill 3](../maps/bwmfill3.md) | – | 73 |

## Blackwater Mountain, Bwmfill 3 (tunlon) { #v-tunlon }

**Entry ID:** `tunlon` · **Type:** NPC · **Role:** Shopkeeper; starts [It makes no fence](../quests/tunlon_fence.md)

**Location:** Blackwater Mountain: [Bwmfill 3](../maps/bwmfill3.md#pin-npc-tunlon)

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green Pepper](../items/green_pepper.md) | 70% | 1 to 5 |
| [Yellow Pepper](../items/yellow_pepper.md) | 60% | 1 to 5 |
| [Red Pepper](../items/red_pepper.md) | 50% | 1 to 5 |
| [Raw lamb meat](../items/lamb_meat_raw.md) | 100% | 5 to 10 |
| [Cooked lamb meat](../items/lamb_meat.md) | 100% | 2 to 5 |

### Quests

- [It makes no fence](../quests/tunlon_fence.md): stages 10, 12, 40, 200, 250
- [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md): stage 44

### Dialogue simulator

Set your quest stages and items, then talk to Tunlon. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tunlon_start.json" data-npc="Tunlon" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (50 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tunlon-tunlon_start"></span>**`tunlon_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → [bwmfill_killsheep](#d-tunlon-bwmfill_killsheep)
    - Next *(if reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250))* → [tunlon_start_1](#d-tunlon-tunlon_start_1)
    - Next *(if reached stage 200 of [It makes no fence](../quests/tunlon_fence.md#stage-200))* → [tunlon_prog_21](#d-tunlon-tunlon_prog_21)
    - Next *(if reached stage 40 of [It makes no fence](../quests/tunlon_fence.md#stage-40))* → [tunlon_prog_11](#d-tunlon-tunlon_prog_11)
    - Next *(if reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10))* → [tunlon_prog_1](#d-tunlon-tunlon_prog_1)
    - Next → [tunlon_start_1](#d-tunlon-tunlon_start_1)

    <span id="d-tunlon-bwmfill_killsheep"></span>**`bwmfill_killsheep`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → [bwmfill_killsheep_10](#d-tunlon-bwmfill_killsheep_10)

    <span id="d-tunlon-tunlon_start_1"></span>**`tunlon_start_1`** Tunlon: “Hello kid! How are you?”

    - “Fine, thank you. Who are you?” *(if NOT reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10))* → [tunlon_start_2](#d-tunlon-tunlon_start_2)
    - “Good. Do you have anything to trade?” → [tunlon_trade](#d-tunlon-tunlon_trade)
    - “Have you seen Andor, my brother? He looks a bit ...” *(if NOT reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20))* → [tunlon_andor](#d-tunlon-tunlon_andor)

    <span id="d-tunlon-tunlon_prog_21"></span>**`tunlon_prog_21`** Tunlon: “Ah, my litle friend.”

    - “Yes, I am back again.” → [tunlon_prog_21a](#d-tunlon-tunlon_prog_21a)

    <span id="d-tunlon-tunlon_prog_11"></span>**`tunlon_prog_11`** Tunlon: “So how is your journey going?”

    - “Tinlyn said there is a woodcutter in Loneford who can help.” *(if reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150))* → [tunlon_prog_12](#d-tunlon-tunlon_prog_12)
    - “Tinlyn said there is a woodcutter in Loneford who can help.” *(if reached stage 110 of [It makes no fence](../quests/tunlon_fence.md#stage-110); NOT reached stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150))* → [tunlon_prog_12](#d-tunlon-tunlon_prog_12)
    - “I still have to ask Tinlyn.” *(if NOT reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 110 of [It makes no fence](../quests/tunlon_fence.md#stage-110))* → [tunlon_noprog](#d-tunlon-tunlon_noprog)
    - “Here, I brought you fences.” *(if carry 10× [Sturdy fence](../items/tunlon_fence1.md))* → [tunlon_prog_15](#d-tunlon-tunlon_prog_15)
    - “I still have to look for the fences ...” *(if NOT carry 10× [Sturdy fence](../items/tunlon_fence1.md))* → [tunlon_noprog](#d-tunlon-tunlon_noprog)

    <span id="d-tunlon-tunlon_prog_1"></span>**`tunlon_prog_1`** Tunlon: “Hello - are you back yet? I wasn't expecting you yet.”

    - “Well ...” → [tunlon_prog_1b](#d-tunlon-tunlon_prog_1b)

    <span id="d-tunlon-bwmfill_killsheep_10"></span>**`bwmfill_killsheep_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 44 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44))* → [bwmfill_killsheep_20](#d-tunlon-bwmfill_killsheep_20)
    - branch 2 *(if reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250); NOT reached stage 12 of [It makes no fence](../quests/tunlon_fence.md#stage-12))* → [bwmfill_killsheep_12](#d-tunlon-bwmfill_killsheep_12)

    <span id="d-tunlon-tunlon_start_2"></span>**`tunlon_start_2`** Tunlon: “I am Tunlon of Crossglen. I look after my flock of sheep here.”

    - “I am from Crossglen too!” *(if NOT reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10))* → [tunlon_quest_1](#d-tunlon-tunlon_quest_1)
    - “Nice to have met you.” *(if reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10))* → *conversation ends*

    <span id="d-tunlon-tunlon_trade"></span>**`tunlon_trade`** Tunlon: “Yes, I have a few basic supplies that I could offer. Do you want to have a look?”

    - “Sure!” → *shop opens*

    <span id="d-tunlon-tunlon_andor"></span>**`tunlon_andor`** Tunlon: “I know Andor. Of course I do.”

    - Next → [tunlon_andor_2](#d-tunlon-tunlon_andor_2)

    <span id="d-tunlon-tunlon_prog_21a"></span>**`tunlon_prog_21a`** Tunlon: “Have you brought new fences?”

    - “Here, I hope these are better.” *(if hand over 10× [New fence](../items/tunlon_fence2.md))* → [tunlon_prog_22](#d-tunlon-tunlon_prog_22)
    - “No, I am still looking for them.” *(if NOT carry 10× [New fence](../items/tunlon_fence2.md))* → *conversation ends*

    <span id="d-tunlon-tunlon_prog_12"></span>**`tunlon_prog_12`** Tunlon: “Have you been there already?”

    - “No, not yet.” → [tunlon_noprog](#d-tunlon-tunlon_noprog)

    <span id="d-tunlon-tunlon_noprog"></span>**`tunlon_noprog`** Tunlon: “Keep on going!”


    <span id="d-tunlon-tunlon_prog_15"></span>**`tunlon_prog_15`** Tunlon: “Let me see!”

    - Next → [tunlon_prog_16](#d-tunlon-tunlon_prog_16)

    <span id="d-tunlon-tunlon_prog_1b"></span>**`tunlon_prog_1b`** Tunlon: “Have you found some wood already?”

    - “No, I am still searching.” *(if NOT reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20))* → *conversation ends*
    - “No, I asked Jakrar in Fallhaven, but he just sent me to other woodcutters.” *(if reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20))* → [tunlon_prog_2](#d-tunlon-tunlon_prog_2)

    <span id="d-tunlon-bwmfill_killsheep_20"></span>**`bwmfill_killsheep_20`** [Tunlon](../monsters/tunlon.md#v-tunlon2): “You filthy MURDERER!!” — **effects:** sets stage 44 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44), removes monsters from bwmfill3, spawns monsters on bwmfill3

    - Next → [bwmfill_killsheep_22](#d-tunlon-bwmfill_killsheep_22)

    <span id="d-tunlon-bwmfill_killsheep_12"></span>**`bwmfill_killsheep_12`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 12 of [It makes no fence](../quests/tunlon_fence.md#stage-12)


    <span id="d-tunlon-tunlon_quest_1"></span>**`tunlon_quest_1`** Tunlon: “That is great to hear. Could you by any chance get me something from Crossglen? Unfortunately I have to stay here to watch my sheep.”

    - “Oh yeah, no problem!” → [tunlon_quest_2](#d-tunlon-tunlon_quest_2)
    - “Sorry, I have other things to do right now.” → [tunlon_noquest](#d-tunlon-tunlon_noquest)

    <span id="d-tunlon-tunlon_andor_2"></span>**`tunlon_andor_2`** Tunlon: “Always good for mischief, that boy.”

    - “Yes, that's him. Do you know where he is?” → [tunlon_andor_3](#d-tunlon-tunlon_andor_3)

    <span id="d-tunlon-tunlon_prog_22"></span>**`tunlon_prog_22`** Tunlon: “Yeah, these posts are looking really good! Thank you, kid. Here, take this as a small reward.” — **effects:** sets stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250), gives [Gold coins](../items/gold.md), [Specially peppered lamb meat](../items/lamb_meat2.md), [Red Pepper](../items/red_pepper.md)

    - “No problem. See you!” → *conversation ends*
    - “I love running around and helping. See you!” → *conversation ends*
    - “Hmm, the lamb meat looks good. What is that exactly?” → [tunlon_prog_22a](#d-tunlon-tunlon_prog_22a)

    <span id="d-tunlon-tunlon_prog_16"></span>**`tunlon_prog_16`** Tunlon: “Hmm, no, these posts are too short. My sheep are probably able to jump over them.”

    - Next → [tunlon_prog_17](#d-tunlon-tunlon_prog_17)

    <span id="d-tunlon-tunlon_prog_2"></span>**`tunlon_prog_2`** Tunlon: “Have you been there yet?”

    - “No. I will go there next.” *(if NOT reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30))* → *conversation ends*
    - “Yes. They created a shortcut here into the forest.” *(if reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32))* → [tunlon_prog_2a](#d-tunlon-tunlon_prog_2a)
    - “Yes. However, they only have firewood available.” *(if reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30); NOT reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32))* → [tunlon_prog_2a](#d-tunlon-tunlon_prog_2a)

    <span id="d-tunlon-bwmfill_killsheep_22"></span>**`bwmfill_killsheep_22`** Tunlon: “My poor sheep! What have you done?!” — **effects:** sets stage 12 of [It makes no fence](../quests/tunlon_fence.md#stage-12)

    - Next → [bwmfill_killsheep_24](#d-tunlon-bwmfill_killsheep_24)

    <span id="d-tunlon-tunlon_quest_2"></span>**`tunlon_quest_2`** Tunlon: “Thank you, kid. What I need is some wood to repair my fence.”

    - “Where do I get that from?” → [tunlon_quest_3](#d-tunlon-tunlon_quest_3)

    <span id="d-tunlon-tunlon_noquest"></span>**`tunlon_noquest`** Tunlon: “No problem, kid. Just come back here whenever you have some time.”


    <span id="d-tunlon-tunlon_andor_3"></span>**`tunlon_andor_3`** Tunlon: “No. And I want to keep it that way.”

    - “Oh. What has he done to you?” → [tunlon_andor_4](#d-tunlon-tunlon_andor_4)

    <span id="d-tunlon-tunlon_prog_22a"></span>**`tunlon_prog_22a`** Tunlon: “This is lamb with a special seasoning mixture which of course I won't tell you. Here you have an additional one.” — **effects:** gives 1× [Specially peppered lamb meat](../items/lamb_meat2.md)

    - “Thank you. Bye.” → *conversation ends*

    <span id="d-tunlon-tunlon_prog_17"></span>**`tunlon_prog_17`** Tunlon: “Could you go and ask him for other fences?”

    - “Sure! No problem.” → [tunlon_prog_18](#d-tunlon-tunlon_prog_18)
    - “Maybe ...” → [tunlon_prog_18](#d-tunlon-tunlon_prog_18)
    - “What? All the way over again just because you didn't tell me how high your fences had to be?” → [tunlon_prog_17a](#d-tunlon-tunlon_prog_17a)

    <span id="d-tunlon-tunlon_prog_2a"></span>**`tunlon_prog_2a`** Tunlon: “That's good to hear.”

    - “Yes. However, they only have firewood available.” → [tunlon_prog_2b](#d-tunlon-tunlon_prog_2b)

    <span id="d-tunlon-bwmfill_killsheep_24"></span>**`bwmfill_killsheep_24`** Tunlon: “Just you wait - you will pay for it!!”


    <span id="d-tunlon-tunlon_quest_3"></span>**`tunlon_quest_3`** Tunlon: “Oh, isn't there a lumberjack in Crossglen anymore? I haven't been down there for a long time”

    - “Maybe this explains why the forest around Crossglen is too dense to get through...” → [tunlon_quest_3a](#d-tunlon-tunlon_quest_3a)
    - “At least not that I know.” → [tunlon_quest_4](#d-tunlon-tunlon_quest_4)

    <span id="d-tunlon-tunlon_andor_4"></span>**`tunlon_andor_4`** Tunlon: “He scared my sheep. They didn't dare to leave the stable for two weeks.”

    - Next → [tunlon_andor_5](#d-tunlon-tunlon_andor_5)

    <span id="d-tunlon-tunlon_prog_18"></span>**`tunlon_prog_18`** Tunlon: “Thank you. I knew I could trust you.” — **effects:** sets stage 200 of [It makes no fence](../quests/tunlon_fence.md#stage-200)


    <span id="d-tunlon-tunlon_prog_17a"></span>**`tunlon_prog_17a`** Tunlon: “But ...”

    - “Do you actually know how far the path is?” → [tunlon_prog_17b](#d-tunlon-tunlon_prog_17b)
    - “I also have something else to do. After all, I'm on Andor's trail.” → [tunlon_prog_17b](#d-tunlon-tunlon_prog_17b)

    <span id="d-tunlon-tunlon_prog_2b"></span>**`tunlon_prog_2b`** Tunlon: “But firewood isn't good for fences.”

    - “Exactly. Where else can you get suitable wood?” → [tunlon_prog_2c](#d-tunlon-tunlon_prog_2c)

    <span id="d-tunlon-tunlon_quest_3a"></span>**`tunlon_quest_3a`** Tunlon: “What do you mean? The climb into the mountains is just northeast of Crossglen?”

    - “Maybe it used to be like that.” → [tunlon_quest_3b](#d-tunlon-tunlon_quest_3b)
    - “If there was a path, it has long since become overgrown.” → [tunlon_quest_3b](#d-tunlon-tunlon_quest_3b)

    <span id="d-tunlon-tunlon_quest_4"></span>**`tunlon_quest_4`** Tunlon: “Well, then you would have to travel over to Fallhaven. Of course only, if that's not too much for you.”

    - “Not for me! I know the way perfectly well.” → [tunlon_quest_5](#d-tunlon-tunlon_quest_5)
    - “Hmm, now that I think about it ...” → [tunlon_quest_4a](#d-tunlon-tunlon_quest_4a)

    <span id="d-tunlon-tunlon_andor_5"></span>**`tunlon_andor_5`** Tunlon: “I then confronted him, even though I was a little scared myself.”

    - “And then?” → [tunlon_andor_6](#d-tunlon-tunlon_andor_6)

    <span id="d-tunlon-tunlon_prog_17b"></span>**`tunlon_prog_17b`** Tunlon: “Please ...”

    - “All right. I'll go again.” → [tunlon_prog_18](#d-tunlon-tunlon_prog_18)

    <span id="d-tunlon-tunlon_prog_2c"></span>**`tunlon_prog_2c`** Tunlon: “Maybe it would be better to buy the finished fences straight away.”

    - “Finished fences? Where do you get something like that from?” → [tunlon_prog_3](#d-tunlon-tunlon_prog_3)

    <span id="d-tunlon-tunlon_quest_3b"></span>**`tunlon_quest_3b`** Tunlon: “What do you mean?”

    - “I had to take a long detour past Stoutford and Prim and come from the other side.” → [tunlon_quest_3c](#d-tunlon-tunlon_quest_3c)

    <span id="d-tunlon-tunlon_quest_5"></span>**`tunlon_quest_5`** Tunlon: “Thank you so much! Here is a bit of gold so you can pay for it.” — **effects:** sets stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10), gives [Gold coins](../items/gold.md)

    - “I will go and get it now.” → *conversation ends*
    - “Hehe, thank you!” → *conversation ends*

    <span id="d-tunlon-tunlon_quest_4a"></span>**`tunlon_quest_4a`** Tunlon: “Please don't let me down. There are wolves and worse here threatening my sheep.”

    - “Sigh, I have too good a heart. It's okay, I'll do it.” → [tunlon_quest_5](#d-tunlon-tunlon_quest_5)
    - “No, forget it. I'm out.” → [tunlon_quest_4b](#d-tunlon-tunlon_quest_4b)

    <span id="d-tunlon-tunlon_andor_6"></span>**`tunlon_andor_6`** Tunlon: “And then? Nothing. With a look that made my blood run cold, he left.”

    - “Yes, my beloved brother. Who are you by the way?” *(if NOT reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10))* → [tunlon_start_2](#d-tunlon-tunlon_start_2)
    - “Then that's settled. Another question: Do you have anything to trade?” → [tunlon_trade](#d-tunlon-tunlon_trade)

    <span id="d-tunlon-tunlon_prog_3"></span>**`tunlon_prog_3`** Tunlon: “Hmm. Maybe my brother knows a place where to get fences.”

    - “Your brother?” *(if reached stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21))* → [tunlon_prog_4_1](#d-tunlon-tunlon_prog_4_1)
    - “Your brother?” *(if NOT reached stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21))* → [tunlon_prog_4_2](#d-tunlon-tunlon_prog_4_2)

    <span id="d-tunlon-tunlon_quest_3c"></span>**`tunlon_quest_3c`** Tunlon: “Then it's a good thing that I haven't tried to go down to Crossglen with my sheep in recent years.”

    - “In any case, there is no lumberjack in Crossglen.” → [tunlon_quest_4](#d-tunlon-tunlon_quest_4)

    <span id="d-tunlon-tunlon_quest_4b"></span>**`tunlon_quest_4b`** Tunlon: “A pity. Come back if you change your mind.”


    <span id="d-tunlon-tunlon_prog_4_1"></span>**`tunlon_prog_4_1`** Tunlon: “Tinlyn, my brother. Poor guy, lost all of his sheep. He lives north of Crossroads guardhouse.”

    - “Well ... yeah I know him.” → [tunlon_prog_5](#d-tunlon-tunlon_prog_5)

    <span id="d-tunlon-tunlon_prog_4_2"></span>**`tunlon_prog_4_2`** Tunlon: “Tinlyn, my brother. He lives north of Crossroads guardhouse.”

    - “Ah, I think I know him.” *(if reached stage 10 of [Lost sheep](../quests/tinlyn.md#stage-10))* → [tunlon_prog_5](#d-tunlon-tunlon_prog_5)
    - “I don't know this Tinlyn yet, but I will find him.” *(if NOT reached stage 10 of [Lost sheep](../quests/tinlyn.md#stage-10))* → [tunlon_prog_5](#d-tunlon-tunlon_prog_5)

    <span id="d-tunlon-tunlon_prog_5"></span>**`tunlon_prog_5`** Tunlon: “Please go and ask him, if he knows anyone who could help.” — **effects:** sets stage 40 of [It makes no fence](../quests/tunlon_fence.md#stage-40)

    - “I'm on my way!” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added<br>Dialogue: 50 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tunlon)"

    | | |
    |---|---|
    | Entry ID | `tunlon` |
    | Spawn group | `tunlon` |
    | Loot table | `tunlon` |
    | Conversation | `tunlon_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:83` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "tunlon",
     "name": "Tunlon",
     "iconID": "monsters_rltiles1:83",
     "monsterClass": "humanoid",
     "spawnGroup": "tunlon",
     "phraseID": "tunlon_start",
     "droplistID": "tunlon"
    }
    ```


## Blackwater Mountain, Bwmfill 3 (tunlon2) { #v-tunlon2 }

**Entry ID:** `tunlon2` · **Type:** Enemy

**Location:** Blackwater Mountain: [Bwmfill 3](../maps/bwmfill3.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 73 |
| XP when defeated | 292 |
| Damage | 9 to 17 |
| Attack chance | 200 |
| Block chance | 90 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1000 to 2000 |
| [Quarterstaff](../items/qtrstaff.md) | 100% | 1 |
| [Green Pepper](../items/green_pepper.md) | 70% | 1 to 2 |
| [Yellow Pepper](../items/yellow_pepper.md) | 60% | 1 to 2 |
| [Red Pepper](../items/red_pepper.md) | 50% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Bwmfill 3](../maps/bwmfill3.md) | Blackwater Mountain | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (tunlon2)"

    | | |
    |---|---|
    | Entry ID | `tunlon2` |
    | Spawn group | `tunlon2` |
    | Loot table | `tunlon2` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:83` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "tunlon2",
     "name": "Tunlon",
     "iconID": "monsters_rltiles1:83",
     "maxHP": 73,
     "maxAP": 10,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 9,
      "max": 17
     },
     "spawnGroup": "tunlon2",
     "droplistID": "tunlon2",
     "attackCost": 5,
     "attackChance": 200,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 10
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
