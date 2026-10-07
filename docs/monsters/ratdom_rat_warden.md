# ![](../assets/icons/monsters/monsters_rltiles3_10.png){ .sprite } Wart

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_10.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ratdom_rat_warden` |
| **Type** | Shopkeeper |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Museum |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Orange rat necklace](../items/ratdom_compass_tour.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_624](../maps/ratdom_maze_624.md) | Museum | 1 | appears later in a quest |


## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 310, 320, 321, 322, 323, 324, 325, 390
- [Ratdom_maze (hidden flag)](../quests/ratdom_maze.md): stages 132
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 192

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Wart. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_rat_warden.json" data-npc="Wart" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (72 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_rat_warden"></span>**`ratdom_rat_warden`** Wart: “Yes please?”

    - “I have found some bones. May I enter now?” *(if reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390))* → [ratdom_rat_warden_50](#d-ratdom_rat_warden_50)
    - “Who are you?” → [ratdom_rat_warden_10](#d-ratdom_rat_warden_10)
    - “What are you doing here?” → [ratdom_rat_warden_10](#d-ratdom_rat_warden_10)
    - “Could you tell me something about this place?” → [ratdom_rat_warden_30](#d-ratdom_rat_warden_30)
    - “Oh, it's nothing. I just tried the bell.” → [ratdom_rat_warden_20](#d-ratdom_rat_warden_20)
    - “Please give me back my cheese.” *(if faction “ratdom_rat_cheese1” ≥ 1)* → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)
    - “Please give me back my cheese.” *(if NOT faction “ratdom_rat_cheese1” ≥ 1; faction “ratdom_rat_cheese2” ≥ 1)* → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)
    - “Please give me back my cheese.” *(if NOT faction “ratdom_rat_cheese1” ≥ 1; NOT faction “ratdom_rat_cheese2” ≥ 1; faction “ratdom_rat_cheese3” ≥ 1)* → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)
    - “Please give me back my cheese.” *(if NOT faction “ratdom_rat_cheese1” ≥ 1; NOT faction “ratdom_rat_cheese2” ≥ 1; NOT faction “ratdom_rat_cheese3” ≥ 1; faction “ratdom_rat_cheese4” ≥ 1)* → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)

    <span id="d-ratdom_rat_warden_50"></span>**`ratdom_rat_warden_50`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); hand over 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); hand over 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); hand over 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); hand over 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_52](#d-ratdom_rat_warden_52)
    - branch 2 *(if carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md))* → [ratdom_rat_warden_60](#d-ratdom_rat_warden_60)
    - branch 3 *(if carry 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md))* → [ratdom_rat_warden_61](#d-ratdom_rat_warden_61)
    - branch 4 *(if carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md))* → [ratdom_rat_warden_65](#d-ratdom_rat_warden_65)
    - branch 5 *(if carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md))* → [ratdom_rat_warden_66](#d-ratdom_rat_warden_66)
    - branch 6 *(if carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_67](#d-ratdom_rat_warden_67)
    - branch 7 → [ratdom_rat_warden_69](#d-ratdom_rat_warden_69)

    <span id="d-ratdom_rat_warden_10"></span>**`ratdom_rat_warden_10`** Wart: “I am the warden of our Memorial Hall. I keep the exhibits in order and answer questions from visitors. Call me Wart.”

    - “Could you tell me anything about this place?” → [ratdom_rat_warden_30](#d-ratdom_rat_warden_30)
    - “Wart - really? [giggle]” → [ratdom_rat_warden_20](#d-ratdom_rat_warden_20)
    - “OK, bye.” → *conversation ends*

    <span id="d-ratdom_rat_warden_30"></span>**`ratdom_rat_warden_30`** Wart: “This used to be a happy place of memories. Many objects and statues from the past invite you to linger and think. Every rat loved this place.”

    - Next → [ratdom_rat_warden_31](#d-ratdom_rat_warden_31)

    <span id="d-ratdom_rat_warden_20"></span>**`ratdom_rat_warden_20`** Wart: “[Incomprehensible muttering]”

    - “OK, just leave me then.” → *NPC leaves*

    <span id="d-ratdom_rat_warden_cheese"></span>**`ratdom_rat_warden_cheese`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “ratdom_rat_cheese1” ≥ 1)* → [ratdom_rat_warden_cheese_1](#d-ratdom_rat_warden_cheese_1)
    - branch 2 *(if faction “ratdom_rat_cheese2” ≥ 1)* → [ratdom_rat_warden_cheese_2](#d-ratdom_rat_warden_cheese_2)
    - branch 3 *(if faction “ratdom_rat_cheese3” ≥ 1)* → [ratdom_rat_warden_cheese_3](#d-ratdom_rat_warden_cheese_3)
    - branch 4 *(if faction “ratdom_rat_cheese4” ≥ 1)* → [ratdom_rat_warden_cheese_4](#d-ratdom_rat_warden_cheese_4)
    - branch 5 → [ratdom_rat_warden_cheese_50](#d-ratdom_rat_warden_cheese_50)

    <span id="d-ratdom_rat_warden_52"></span>**`ratdom_rat_warden_52`** Wart: “Let's have a look. Oh, what are my old eyes seeing? King Rah is back, completely! I am overwhelmed with joy! You may pass now of course.” — **effects:** sets stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390)

    - “I hope you can puzzle your king back together.” → [ratdom_rat_warden_54](#d-ratdom_rat_warden_54)

    <span id="d-ratdom_rat_warden_60"></span>**`ratdom_rat_warden_60`** Wart: “Wonderful! You've already recovered King Rah's head!”

    - Next → [ratdom_rat_warden_70](#d-ratdom_rat_warden_70)

    <span id="d-ratdom_rat_warden_61"></span>**`ratdom_rat_warden_61`** Wart: “You've already recovered some of King Rah's legs.”

    - Next → [ratdom_rat_warden_70](#d-ratdom_rat_warden_70)

    <span id="d-ratdom_rat_warden_65"></span>**`ratdom_rat_warden_65`** Wart: “Ah, you've already recovered King Rah's tail!”

    - Next → [ratdom_rat_warden_70](#d-ratdom_rat_warden_70)

    <span id="d-ratdom_rat_warden_66"></span>**`ratdom_rat_warden_66`** Wart: “Good, you've already recovered King Rah's back bone.”

    - Next → [ratdom_rat_warden_70](#d-ratdom_rat_warden_70)

    <span id="d-ratdom_rat_warden_67"></span>**`ratdom_rat_warden_67`** Wart: “Great! These bones look like King Rah's ribs!”

    - Next → [ratdom_rat_warden_70](#d-ratdom_rat_warden_70)

    <span id="d-ratdom_rat_warden_69"></span>**`ratdom_rat_warden_69`** Wart: “Please go and find all of King Rah's bones.”

    - Next → [ratdom_rat_warden_80](#d-ratdom_rat_warden_80)

    <span id="d-ratdom_rat_warden_31"></span>**`ratdom_rat_warden_31`** Wart: “Well, almost every rat.”

    - Next → [ratdom_rat_warden_32](#d-ratdom_rat_warden_32)

    <span id="d-ratdom_rat_warden_cheese_1"></span>**`ratdom_rat_warden_cheese_1`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_rat_cheese1” -1, gives 1× [Cheese](../items/cheese.md)

    - branch 1 *(if faction “ratdom_rat_cheese1” ≥ 1)* → [ratdom_rat_warden_cheese_1](#d-ratdom_rat_warden_cheese_1)
    - branch 2 → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)

    <span id="d-ratdom_rat_warden_cheese_2"></span>**`ratdom_rat_warden_cheese_2`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_rat_cheese2” -1, gives 1× [Charwood cheddar](../items/charwood_cheddar.md)

    - branch 1 *(if faction “ratdom_rat_cheese2” ≥ 1)* → [ratdom_rat_warden_cheese_2](#d-ratdom_rat_warden_cheese_2)
    - branch 2 → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)

    <span id="d-ratdom_rat_warden_cheese_3"></span>**`ratdom_rat_warden_cheese_3`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_rat_cheese3” -1, gives 1× [Blue cheese](../items/cheese_blue.md)

    - branch 1 *(if faction “ratdom_rat_cheese3” ≥ 1)* → [ratdom_rat_warden_cheese_3](#d-ratdom_rat_warden_cheese_3)
    - branch 2 → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)

    <span id="d-ratdom_rat_warden_cheese_4"></span>**`ratdom_rat_warden_cheese_4`** *(silent check: the first matching branch below is taken)* — **effects:** faction “ratdom_rat_cheese4” -1, gives 1× [Goat cheese](../items/cheese_goat.md)

    - branch 1 *(if faction “ratdom_rat_cheese4” ≥ 1)* → [ratdom_rat_warden_cheese_4](#d-ratdom_rat_warden_cheese_4)
    - branch 2 → [ratdom_rat_warden_cheese](#d-ratdom_rat_warden_cheese)

    <span id="d-ratdom_rat_warden_cheese_50"></span>**`ratdom_rat_warden_cheese_50`** Wart: “Sure, here you are.”

    - “Thank you. Here, have some coins.” *(if pay 2 gold)* → [ratdom_rat_warden_cheese_52](#d-ratdom_rat_warden_cheese_52)
    - “Wasn't there one or two more pieces of cheese?” → [ratdom_rat_warden_cheese_54](#d-ratdom_rat_warden_cheese_54)

    <span id="d-ratdom_rat_warden_54"></span>**`ratdom_rat_warden_54`** *(silent check: the first matching branch below is taken)*

    - Next *(if random chance (25%))* → [ratdom_rat_warden_54d](#d-ratdom_rat_warden_54d)
    - Next *(if random chance (33%))* → [ratdom_rat_warden_54c](#d-ratdom_rat_warden_54c)
    - Next *(if random chance (50%))* → [ratdom_rat_warden_54b](#d-ratdom_rat_warden_54b)
    - Next → [ratdom_rat_warden_54a](#d-ratdom_rat_warden_54a)

    <span id="d-ratdom_rat_warden_70"></span>**`ratdom_rat_warden_70`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_70a](#d-ratdom_rat_warden_70a)
    - branch 2 *(if carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_71a](#d-ratdom_rat_warden_71a)
    - branch 3 *(if carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_75a](#d-ratdom_rat_warden_75a)
    - branch 4 *(if carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md))* → [ratdom_rat_warden_76a](#d-ratdom_rat_warden_76a)
    - branch 5 *(if carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md))* → [ratdom_rat_warden_77a](#d-ratdom_rat_warden_77a)
    - branch 6 → [ratdom_rat_warden_79](#d-ratdom_rat_warden_79)

    <span id="d-ratdom_rat_warden_80"></span>**`ratdom_rat_warden_80`** [Wart](../monsters/ratdom_rat_warden.md): “I can't let you enter our Memorial Hall. We have to get back our skeleton statue of King Rah first.” — **effects:** sets stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310)

    - “OK. I will find the bones for you.” → [ratdom_rat_warden_90](#d-ratdom_rat_warden_90)
    - “This maze is terrible. Do you have any idea how I could find my way out again?” → [ratdom_rat_warden_82](#d-ratdom_rat_warden_82)
    - “Do you have any idea where I should go looking for your bones?” → [ratdom_rat_warden_90](#d-ratdom_rat_warden_90)

    <span id="d-ratdom_rat_warden_32"></span>**`ratdom_rat_warden_32`** Wart: “But Fraedro was filled with jealousy and consumed with envy.”

    - “Yes, it is always the same thing.” → [ratdom_rat_warden_33](#d-ratdom_rat_warden_33)
    - “Sigh. I know that story already. Get to the point.” *(if reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310))* → [ratdom_rat_warden_44b](#d-ratdom_rat_warden_44b)

    <span id="d-ratdom_rat_warden_cheese_52"></span>**`ratdom_rat_warden_cheese_52`** Wart: “2 gold coins - how very generous.”

    - Next → [ratdom_rat_warden_cheese_53](#d-ratdom_rat_warden_cheese_53)

    <span id="d-ratdom_rat_warden_cheese_54"></span>**`ratdom_rat_warden_cheese_54`** Wart: “Insolence. I'll pretend that I didn't hear it.”


    <span id="d-ratdom_rat_warden_54d"></span>**`ratdom_rat_warden_54d`** Wart: “I am so grateful.”

    - Next → [ratdom_rat_warden_54](#d-ratdom_rat_warden_54)

    <span id="d-ratdom_rat_warden_54c"></span>**`ratdom_rat_warden_54c`** Wart: “Thanks!”

    - Next → [ratdom_rat_warden_54](#d-ratdom_rat_warden_54)

    <span id="d-ratdom_rat_warden_54b"></span>**`ratdom_rat_warden_54b`** Wart: “Thank you a thousand times!”

    - Next → [ratdom_rat_warden_54](#d-ratdom_rat_warden_54)

    <span id="d-ratdom_rat_warden_54a"></span>**`ratdom_rat_warden_54a`** Wart: “Thank you!”

    - Next → [ratdom_rat_warden_54](#d-ratdom_rat_warden_54)

    <span id="d-ratdom_rat_warden_70a"></span>**`ratdom_rat_warden_70a`** Wart: “Let's have a look ... Great! Only King Rah's head is missing. You will find it too, I am sure.” — **effects:** sets stage 321 of [Yellow is it](../quests/ratdom_quest.md#stage-321)

    - “Of course.” → *conversation ends*
    - “I hope it is worth the hard work.” → *conversation ends*

    <span id="d-ratdom_rat_warden_71a"></span>**`ratdom_rat_warden_71a`** Wart: “Let's have a look ... Great! Now we only need the fourth leg. You will find it too, I am sure.” — **effects:** sets stage 325 of [Yellow is it](../quests/ratdom_quest.md#stage-325)

    - “Of course.” → *conversation ends*
    - “I hope it is worth the hard work.” → *conversation ends*

    <span id="d-ratdom_rat_warden_75a"></span>**`ratdom_rat_warden_75a`** Wart: “Let's have a look ... Great! Only King Rah's tail is missing. You will find it too, I am sure.” — **effects:** sets stage 324 of [Yellow is it](../quests/ratdom_quest.md#stage-324)

    - “Of course.” → *conversation ends*
    - “I hope it is worth the hard work.” → *conversation ends*

    <span id="d-ratdom_rat_warden_76a"></span>**`ratdom_rat_warden_76a`** Wart: “Let's have a look ... Great! Only King Rah's back bone is missing. You will find it too, I am sure.” — **effects:** sets stage 322 of [Yellow is it](../quests/ratdom_quest.md#stage-322)

    - “Of course.” → *conversation ends*
    - “I hope it is worth the hard work.” → *conversation ends*

    <span id="d-ratdom_rat_warden_77a"></span>**`ratdom_rat_warden_77a`** Wart: “Let's have a look ... Great! Only King Rah's rib bones are missing. You will find them too, I am sure.” — **effects:** sets stage 323 of [Yellow is it](../quests/ratdom_quest.md#stage-323)

    - “Of course.” → *conversation ends*
    - “I hope it is worth the hard work.” → *conversation ends*

    <span id="d-ratdom_rat_warden_79"></span>**`ratdom_rat_warden_79`** Wart: “Let's have a look ... In total we need the head, the ribs and the back bone, 4 legs and the tail of course.” — **effects:** sets stage 320 of [Yellow is it](../quests/ratdom_quest.md#stage-320)

    - “OK, I'll be back.” → *conversation ends*

    <span id="d-ratdom_rat_warden_90"></span>**`ratdom_rat_warden_90`** [Wart](../monsters/ratdom_rat_warden.md): “The cave system is huge and really very confusing. It already surprised me how you found your way to me here.”

    - Next → [ratdom_rat_warden_91](#d-ratdom_rat_warden_91)

    <span id="d-ratdom_rat_warden_82"></span>**`ratdom_rat_warden_82`** Wart: “That is easy. Just choose the exit where you see rats in front of it. Rats always know their way out.”

    - Next → [ratdom_rat_warden_84](#d-ratdom_rat_warden_84)

    <span id="d-ratdom_rat_warden_33"></span>**`ratdom_rat_warden_33`** Wart: “How he hated it when visitors crowded these halls around the valuable exhibits and admired the statues.”

    - Next → [ratdom_rat_warden_34](#d-ratdom_rat_warden_34)

    <span id="d-ratdom_rat_warden_44b"></span>**`ratdom_rat_warden_44b`** Wart: “For security reasons, we don't let anyone in or out until King Rah is back in his accustomed place.”

    - “Even 100 pieces of gold wouldn't change your mind?” → [ratdom_rat_warden_46a](#d-ratdom_rat_warden_46a)
    - “If the skeleton is back, may I pass?” *(if NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390))* → [ratdom_rat_warden_48](#d-ratdom_rat_warden_48)
    - “I want to talk with Fraedro.” *(if NOT reached stage 395 of [Yellow is it](../quests/ratdom_quest.md#stage-395))* → [ratdom_rat_warden_46b](#d-ratdom_rat_warden_46b)
    - “What lies behind this blocked passage?” → [ratdom_rat_warden_46c](#d-ratdom_rat_warden_46c)
    - “May I enter?” *(if reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390))* → [ratdom_rat_warden_50](#d-ratdom_rat_warden_50)

    <span id="d-ratdom_rat_warden_cheese_53"></span>**`ratdom_rat_warden_cheese_53`** Wart: “[low voice] Scrooge.”


    <span id="d-ratdom_rat_warden_91"></span>**`ratdom_rat_warden_91`** Wart: “Maybe you'll find wisdom in my compass?”

    - “What compass?” → [ratdom_rat_warden_92](#d-ratdom_rat_warden_92)

    <span id="d-ratdom_rat_warden_84"></span>**`ratdom_rat_warden_84`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [ratdom_rat_warden_86](#d-ratdom_rat_warden_86)
    - Next → [ratdom_rat_warden_80](#d-ratdom_rat_warden_80)

    <span id="d-ratdom_rat_warden_34"></span>**`ratdom_rat_warden_34`** Wart: “He wanted to be the center of attention. A larger-than-life statue of himself should dominate the room, he thought.”

    - “Such a braggart.” → [ratdom_rat_warden_35](#d-ratdom_rat_warden_35)

    <span id="d-ratdom_rat_warden_46a"></span>**`ratdom_rat_warden_46a`** Wart: “Of course not! This door will remain closed until King Rah returns.”

    - “Sorry.” → [ratdom_rat_warden_44b](#d-ratdom_rat_warden_44b)

    <span id="d-ratdom_rat_warden_48"></span>**`ratdom_rat_warden_48`** Wart: “If King Rah is with us again, that would be great! Of course you can then go to our memory hall. You would be our guest of honor.” — **effects:** sets stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310)

    - Next → [ratdom_rat_warden_48a](#d-ratdom_rat_warden_48a)

    <span id="d-ratdom_rat_warden_46b"></span>**`ratdom_rat_warden_46b`** Wart: “Impossible! No way.”

    - Next → [ratdom_rat_warden_44b](#d-ratdom_rat_warden_44b)

    <span id="d-ratdom_rat_warden_46c"></span>**`ratdom_rat_warden_46c`** Wart: “The memory hall of course.”

    - Next → [ratdom_rat_warden_44d](#d-ratdom_rat_warden_44d)

    <span id="d-ratdom_rat_warden_92"></span>**`ratdom_rat_warden_92`** Wart: “Start at the entrance where you entered the lower part of these caves.”

    - Next → [ratdom_rat_warden_94](#d-ratdom_rat_warden_94)

    <span id="d-ratdom_rat_warden_86"></span>**`ratdom_rat_warden_86`** [Clevred](../monsters/ratdom_rat.md): “Didn't I tell you?”

    - “You talk all the time and too much anyway. I can't always listen to that.” → [ratdom_rat_warden_80](#d-ratdom_rat_warden_80)

    <span id="d-ratdom_rat_warden_35"></span>**`ratdom_rat_warden_35`** Wart: “He hated especially the fully preserved skeleton of King Rah, the powerful founder of this empire. It was particularly brilliant: King Rah, standing upright, his dreaded sword in his bony right hand.”

    - Next → [ratdom_rat_warden_36](#d-ratdom_rat_warden_36)

    <span id="d-ratdom_rat_warden_48a"></span>**`ratdom_rat_warden_48a`** Wart: “But we are not there yet.”

    - Next → [ratdom_rat_warden_80](#d-ratdom_rat_warden_80)

    <span id="d-ratdom_rat_warden_44d"></span>**`ratdom_rat_warden_44d`** Wart: “And another tunnel, but only a short distance and a dead end.”

    - Next → [ratdom_rat_warden_44e](#d-ratdom_rat_warden_44e)

    <span id="d-ratdom_rat_warden_94"></span>**`ratdom_rat_warden_94`** Wart: “There you put on the necklace with my compass. With this compass you may perceive otherwise invisible signs on the walls. Follow these.”

    - “What signs?” → [ratdom_rat_warden_95](#d-ratdom_rat_warden_95)

    <span id="d-ratdom_rat_warden_36"></span>**`ratdom_rat_warden_36`** Wart: “Yes, King Rah was a great leader. Many battles were fought against the monsters that came out of the rift. But when the superiority became too great, Rah led his people into the caves under the Blackwater Mountains and founded a new…”

    - Next → [ratdom_rat_warden_37](#d-ratdom_rat_warden_37)

    <span id="d-ratdom_rat_warden_44e"></span>**`ratdom_rat_warden_44e`** Wart: “We never go there, there are scary noises coming from there.”

    - “Finally light at the end of the tunnel.” → [ratdom_rat_warden_44b](#d-ratdom_rat_warden_44b)

    <span id="d-ratdom_rat_warden_95"></span>**`ratdom_rat_warden_95`** Wart: “Shields in orange and yellow color. Orange for the main route and yellow for short side tunnels.”

    - “What?” → [ratdom_rat_warden_95_10](#d-ratdom_rat_warden_95_10)
    - “OK.” → [ratdom_rat_warden_96](#d-ratdom_rat_warden_96)

    <span id="d-ratdom_rat_warden_37"></span>**`ratdom_rat_warden_37`** Wart: “The wise King Rah had the existing caves further expanded as protection.”

    - “That's why the passages are laid out so confusingly?” → [ratdom_rat_warden_38](#d-ratdom_rat_warden_38)

    <span id="d-ratdom_rat_warden_95_10"></span>**`ratdom_rat_warden_95_10`** Wart: “Should there be a branch, there will be an additional flag. The side trip is marked with a yellow shield.”

    - “What?” → [ratdom_rat_warden_95_20](#d-ratdom_rat_warden_95_20)

    <span id="d-ratdom_rat_warden_96"></span>**`ratdom_rat_warden_96`** [Wart](../monsters/ratdom_rat_warden.md): “It will be a far journey. But you will meet everything that you need to meet. And even more.”

    - “This is finally good news.” → [ratdom_rat_warden_98](#d-ratdom_rat_warden_98)

    <span id="d-ratdom_rat_warden_38"></span>**`ratdom_rat_warden_38`** Wart: “Right. This should be additional protection from enemies.”

    - “Interesting. But why is the passage here closed now?” → [ratdom_rat_warden_40](#d-ratdom_rat_warden_40)

    <span id="d-ratdom_rat_warden_95_20"></span>**`ratdom_rat_warden_95_20`** Wart: “Sigh. If you see an orange shield together with a flag, then first look for another passage marked with a yellow shield.”

    - “And then?” → [ratdom_rat_warden_95_30](#d-ratdom_rat_warden_95_30)

    <span id="d-ratdom_rat_warden_98"></span>**`ratdom_rat_warden_98`** Wart: “Beware! It slows you down, because your mind is clouded and partly in another dimension.”

    - “No problem. Show me this wonderful item.” → *shop opens*
    - “However, I am as poor as a church rat.” *(if NOT have 5,555 gold; NOT reached stage 192 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-192))* → [ratdom_rat_warden_99](#d-ratdom_rat_warden_99)

    <span id="d-ratdom_rat_warden_40"></span>**`ratdom_rat_warden_40`** Wart: “One bad day I found this place ransacked! Only an empty pedestal remained where the richly decorated skeleton of King Rah had been.”

    - “No.” → [ratdom_rat_warden_41](#d-ratdom_rat_warden_41)
    - “How did that happen?” → [ratdom_rat_warden_42](#d-ratdom_rat_warden_42)

    <span id="d-ratdom_rat_warden_95_30"></span>**`ratdom_rat_warden_95_30`** Wart: “Follow this passage to the end. You might find something important there. Then go back to the crossing and follow the orange shield again.” — **effects:** sets stage 132 of [Ratdom_maze (hidden flag)](../quests/ratdom_maze.md#stage-132), starts timer “ratdom_compass_tour”

    - “Eh, OK. Got it.” *(if reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [ratdom_rat_warden_95_40](#d-ratdom_rat_warden_95_40)
    - “Eh, OK. Got it.” *(if NOT reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [ratdom_rat_warden_95_41](#d-ratdom_rat_warden_95_41)

    <span id="d-ratdom_rat_warden_99"></span>**`ratdom_rat_warden_99`** Wart: “Well, I have too good a heart. Here, take the amulet for 100 gold pieces.”

    - “Oh thank you! Here is the gold.” *(if pay 100 gold)* → [ratdom_rat_warden_99a](#d-ratdom_rat_warden_99a)
    - “I will think about it.” → *conversation ends*

    <span id="d-ratdom_rat_warden_41"></span>**`ratdom_rat_warden_41`** Wart: “Yes.”

    - “Ooh.” → [ratdom_rat_warden_42](#d-ratdom_rat_warden_42)

    <span id="d-ratdom_rat_warden_42"></span>**`ratdom_rat_warden_42`** Wart: “This was probably Fraedro's most terrifying act. We found him and confronted him.”

    - “Such a miserable villain!” → [ratdom_rat_warden_44](#d-ratdom_rat_warden_44)
    - “Did he admit it?” → [ratdom_rat_warden_44](#d-ratdom_rat_warden_44)

    <span id="d-ratdom_rat_warden_95_40"></span>**`ratdom_rat_warden_95_40`** [Clevred](../monsters/ratdom_rat.md): “[muttering] I want to hope so, but I don't really believe it yet.”

    - Next → [ratdom_rat_warden_96](#d-ratdom_rat_warden_96)

    <span id="d-ratdom_rat_warden_95_41"></span>**`ratdom_rat_warden_95_41`** Wart: “[muttering] I want to hope so, but I don't really believe it yet.”

    - Next → [ratdom_rat_warden_96](#d-ratdom_rat_warden_96)

    <span id="d-ratdom_rat_warden_99a"></span>**`ratdom_rat_warden_99a`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Orange rat necklace](../items/ratdom_compass_tour.md), sets stage 192 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-192)


    <span id="d-ratdom_rat_warden_44"></span>**`ratdom_rat_warden_44`** Wart: “Of course he denied everything, that hypocrite! But who else could have done it?”

    - Next → [ratdom_rat_warden_44a](#d-ratdom_rat_warden_44a)

    <span id="d-ratdom_rat_warden_44a"></span>**`ratdom_rat_warden_44a`** Wart: “He deserved immediate death for this terrible act. However, we only locked him up until he would reveal where he stashed our beloved royal skeleton.”

    - Next → [ratdom_rat_warden_44b](#d-ratdom_rat_warden_44b)



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 72 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ratdom_rat_warden` |
    | Spawn group | `ratdom_rat_warden` |
    | Loot table | `ratdom_rat_warden` |
    | Conversation | `ratdom_rat_warden` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles3:10` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_rat_warden",
     "name": "Wart",
     "iconID": "monsters_rltiles3:10",
     "movementAggressionType": "wholeMap",
     "phraseID": "ratdom_rat_warden",
     "droplistID": "ratdom_rat_warden"
    }
    ```


<small>Data from v0.8.18</small>
