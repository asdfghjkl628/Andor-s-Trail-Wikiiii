# ![](../assets/icons/monsters/monsters_rltiles1_68.png){ .sprite } Algangror

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 241 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 5 |
| Damage | 3 to 9 |
| Attack chance | 80 |
| Block chance | 120 |
| Damage resistance | 4 |
| Critical skill | 200 |
| Critical multiplier | 2.0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Algangror's ring](../items/algangror_ring.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 0 to 20 |
| [Regular potion of health](../items/health.md) | 100% | 1 to 2 |
| [Sharpened gem](../items/gem4.md) | 100% | 1 |
| [Empty vial](../items/vial_empty2.md) | 100% | 3 to 5 |

## Found on

- [lonelyhouse0](../maps/lonelyhouse0.md)

## Quests

- [Of mice and men](../quests/algangror.md): stages 10, 11, 15, 20, 21, 100, 101
- [The five idols](../quests/fiveidols.md): stages 10, 20, 30, 31, 32, 33, 34, 35, 37, 51, 60, 61, 70, 100
- [What is that stench?](../quests/remgard2.md): stages 30, 35

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Algangror. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/algangror.json" data-npc="Algangror" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (108 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-algangror"></span>**`algangror`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 35 of [What is that stench?](../quests/remgard2.md#stage-35))* → [algangror_fight_6](#d-algangror_fight_6)
    - branch 2 *(if reached stage 30 of [What is that stench?](../quests/remgard2.md#stage-30))* → [algangror_fight_3](#d-algangror_fight_3)
    - branch 3 *(if reached stage 100 of [The five idols](../quests/fiveidols.md#stage-100))* → [algangror_return_d1](#d-algangror_return_d1)
    - branch 4 *(if reached stage 70 of [The five idols](../quests/fiveidols.md#stage-70))* → [algangror_cmp5](#d-algangror_cmp5)
    - branch 5 *(if reached stage 61 of [The five idols](../quests/fiveidols.md#stage-61))* → [algangror_cmp1](#d-algangror_cmp1)
    - branch 6 *(if reached stage 51 of [The five idols](../quests/fiveidols.md#stage-51))* → [algangror_story1](#d-algangror_story1)
    - branch 7 *(if reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37))* → [algangror_task2_ret1](#d-algangror_task2_ret1)
    - branch 8 *(if reached stage 20 of [The five idols](../quests/fiveidols.md#stage-20))* → [algangror_task2_7](#d-algangror_task2_7)
    - branch 9 *(if reached stage 101 of [Of mice and men](../quests/algangror.md#stage-101))* → [algangror_return_d1](#d-algangror_return_d1)
    - branch 10 *(if reached stage 100 of [Of mice and men](../quests/algangror.md#stage-100))* → [algangror_return_d1](#d-algangror_return_d1)
    - branch 11 *(if reached stage 21 of [Of mice and men](../quests/algangror.md#stage-21))* → [algangror_return_c1](#d-algangror_return_c1)
    - branch 12 *(if reached stage 20 of [Of mice and men](../quests/algangror.md#stage-20))* → [algangror_return_3](#d-algangror_return_3)
    - branch 13 *(if reached stage 15 of [Of mice and men](../quests/algangror.md#stage-15))* → [algangror_return_1](#d-algangror_return_1)
    - branch 14 → [algangror_1](#d-algangror_1)

    <span id="d-algangror_fight_6"></span>**`algangror_fight_6`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 35 of [What is that stench?](../quests/remgard2.md#stage-35)

    - branch 1 → *fight starts*

    <span id="d-algangror_fight_3"></span>**`algangror_fight_3`** Algangror: “Jhaeld, the fool. He hides behind his guards and his stone walls. Such a pitiful man he is. Yes, I made those people disappear, but they were all worth it. I will have my revenge!” — **effects:** sets stage 30 of [What is that stench?](../quests/remgard2.md#stage-30)

    - Next → [algangror_fight_4](#d-algangror_fight_4)

    <span id="d-algangror_return_d1"></span>**`algangror_return_d1`** Algangror: “Oh, it's you again.”

    - Next → [algangror_return_d2](#d-algangror_return_d2)

    <span id="d-algangror_cmp5"></span>**`algangror_cmp5`** Algangror: “Again, thank you for helping me. You will always be welcome here, friend.”


    <span id="d-algangror_cmp1"></span>**`algangror_cmp1`** Algangror: “So, for helping me with the idols, I believe I promised you my enchanted necklace, 'Marrowtaint'.”

    - Next → [algangror_cmp2](#d-algangror_cmp2)

    <span id="d-algangror_story1"></span>**`algangror_story1`** Algangror: “You see, I used to live in the city of Remgard. The times were good, and the city prospered.”

    - Next → [algangror_story2](#d-algangror_story2)

    <span id="d-algangror_task2_ret1"></span>**`algangror_task2_ret1`** Algangror: “Tell me, how goes the task of placing the idols?”

    - “Can you repeat what you wanted me to do?” → [algangror_task2_8](#d-algangror_task2_8)
    - “I am still trying to find everyone.” → [algangror_task2_ret2](#d-algangror_task2_ret2)
    - “It is done.” *(if reached stage 50 of [The five idols](../quests/fiveidols.md#stage-50))* → [algangror_task2_done1](#d-algangror_task2_done1)
    - “I won't do your stupid task.” → [algangror_task2_n](#d-algangror_task2_n)
    - “I will not help you with your task.” → [algangror_task2_n](#d-algangror_task2_n)

    <span id="d-algangror_task2_7"></span>**`algangror_task2_7`** Algangror: “You will tell no one of this task that I am about to give you, and you must be as discreet as possible.”

    - Next → [algangror_task2_8](#d-algangror_task2_8)

    <span id="d-algangror_return_c1"></span>**`algangror_return_c1`** Algangror: “You return. Thank you for helping me with my ... ahem ... rodent problem earlier.”

    - Next → [algangror_return_c2](#d-algangror_return_c2)

    <span id="d-algangror_return_3"></span>**`algangror_return_3`** Algangror: “Those rodents have really been bothering me. Good thing I managed to catch some of them. He he.”

    - Next → [algangror_return_4](#d-algangror_return_4)

    <span id="d-algangror_return_1"></span>**`algangror_return_1`** Algangror: “You return. Did you handle all those ... ahem ... rodents in my basement?”

    - “Yes, they are all dead.” *(if hand over 6× [Strange looking rat tail](../items/algangror_rat.md))* → [algangror_return_2](#d-algangror_return_2)
    - “I am still working on it. Goodbye.” → *conversation ends*
    - “I won't do your stupid task, count me out.” → [algangror_decline_1](#d-algangror_decline_1)
    - “I have decided not to help you with your rodents.” → [algangror_decline_1](#d-algangror_decline_1)
    - “I am sent by Jhaeld to end whatever it is you do to the people of Remgard.” *(if reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21))* → [algangror_fight_1](#d-algangror_fight_1)

    <span id="d-algangror_1"></span>**`algangror_1`** Algangror: “Oh my, a child. He he, how nice. Tell me, what brings you here?” — **effects:** sets stage 10 of [Of mice and men](../quests/algangror.md#stage-10)

    - “I am looking for my brother.” → [algangror_2a](#d-algangror_2a)
    - “I just entered to see if there's any loot to be found here.” → [algangror_2b](#d-algangror_2b)
    - “I'm an adventurer, looking to help anyone in need of help.” → [algangror_2c](#d-algangror_2c)
    - “I'd rather not tell.” → [algangror_2d](#d-algangror_2d)
    - “I am sent by Jhaeld to end whatever it is you do to the people of Remgard.” *(if reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21))* → [algangror_fight_1](#d-algangror_fight_1)

    <span id="d-algangror_fight_4"></span>**`algangror_fight_4`** Algangror: “And you, what are you trying to accomplish by running his errands? How fortunate that you entered my house. He he.”

    - Next → [algangror_fight_5](#d-algangror_fight_5)

    <span id="d-algangror_return_d2"></span>**`algangror_return_d2`** Algangror: “You should probably leave before you tip something over that might ... ahem ... break. He he.”

    - “I was sent by Jhaeld to end whatever it is you are doing to the people of Remgard.” *(if reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21))* → [algangror_fight_1](#d-algangror_fight_1)
    - “Watch your tongue, witch.” → *conversation ends*
    - “You are right, I had better leave.” → *conversation ends*

    <span id="d-algangror_cmp2"></span>**`algangror_cmp2`** Algangror: “Wear it well, my friend. Do not let others get hold of the power that Marrowtaint provides.”

    - Next → [algangror_cmp3](#d-algangror_cmp3)

    <span id="d-algangror_story2"></span>**`algangror_story2`** Algangror: “Our crops grew well, and some people had very fortunate trading agreements with other cities, making the life for most of us living in Remgard very easy.”

    - Next → [algangror_story3](#d-algangror_story3)

    <span id="d-algangror_task2_8"></span>**`algangror_task2_8`** Algangror: “I have in my possession five idols. Five idols with very unique ... qualities. What I want you to do is ... deliver these idols to various people in the town of Remgard.”

    - Next → [algangror_task2_9](#d-algangror_task2_9)

    <span id="d-algangror_task2_ret2"></span>**`algangror_task2_ret2`** Algangror: “Please hurry, we might not have much time.”


    <span id="d-algangror_task2_done1"></span>**`algangror_task2_done1`** Algangror: “Excellent. Maybe, now I can rest easily. Thank you so much for helping me.”

    - Next → [algangror_task2_done2](#d-algangror_task2_done2)

    <span id="d-algangror_task2_n"></span>**`algangror_task2_n`** Algangror: “Ah yes. After all, you are just a child and I can understand that all of this must be too much for you. Hee hee.” — **effects:** sets stage 100 of [The five idols](../quests/fiveidols.md#stage-100)

    - Next → [algangror_task2_n2](#d-algangror_task2_n2)

    <span id="d-algangror_return_c2"></span>**`algangror_return_c2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [What is that stench?](../quests/remgard2.md#stage-10))* → [algangror_told_1](#d-algangror_told_1)
    - branch 2 *(if reached stage 75 of [Everything in order](../quests/remgard.md#stage-75))* → [algangror_return_c4](#d-algangror_return_c4)
    - branch 3 → [algangror_return_c3](#d-algangror_return_c3)

    <span id="d-algangror_return_4"></span>**`algangror_return_4`** Algangror: “Now, there was something else I wanted to talk to you about. Have you been to the city of Remgard in your travels?”

    - “Yes, I have been there.” → [algangror_remgard_2](#d-algangror_remgard_2)
    - “No, where is that?” → [algangror_remgard_1](#d-algangror_remgard_1)

    <span id="d-algangror_return_2"></span>**`algangror_return_2`** Algangror: “He he. I bet you sure showed them. Excellent. Thank you for ... ahem ... helping me.” — **effects:** sets stage 20 of [Of mice and men](../quests/algangror.md#stage-20)

    - Next → [algangror_return_3](#d-algangror_return_3)

    <span id="d-algangror_decline_1"></span>**`algangror_decline_1`** Algangror: “Ah yes. After all, you are just a child and I can understand such a task would be too much for you. He he.” — **effects:** sets stage 100 of [Of mice and men](../quests/algangror.md#stage-100)


    <span id="d-algangror_fight_1"></span>**`algangror_fight_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Of mice and men](../quests/algangror.md#stage-100))* → [algangror_fight_2](#d-algangror_fight_2)
    - branch 2 *(if reached stage 101 of [Of mice and men](../quests/algangror.md#stage-101))* → [algangror_fight_2](#d-algangror_fight_2)
    - branch 3 *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [algangror_fight_1a](#d-algangror_fight_1a)
    - branch 4 → [algangror_fight_2](#d-algangror_fight_2)

    <span id="d-algangror_2a"></span>**`algangror_2a`** Algangror: “Run away, has he? He he.”

    - Next → [algangror_3](#d-algangror_3)

    <span id="d-algangror_2b"></span>**`algangror_2b`** Algangror: “Oh sure, you think you can just pick up anything and claim it as yours?”

    - Next → [algangror_3](#d-algangror_3)

    <span id="d-algangror_2c"></span>**`algangror_2c`** Algangror: “How noble. Maybe you can be of use to me.”

    - Next → [algangror_3](#d-algangror_3)

    <span id="d-algangror_2d"></span>**`algangror_2d`** Algangror: “Clever. I like that.”

    - Next → [algangror_3](#d-algangror_3)

    <span id="d-algangror_fight_5"></span>**`algangror_fight_5`** Algangror: “Do you really think you can defeat *me*? Ha ha, this will be fun!”

    - “Fight!” → [algangror_fight_6](#d-algangror_fight_6)

    <span id="d-algangror_cmp3"></span>**`algangror_cmp3`** Algangror: “Here you go.” — **effects:** sets stage 70 of [The five idols](../quests/fiveidols.md#stage-70), gives [Marrowtaint](../items/marrowtaint.md)

    - “Thank you.” → [algangror_cmp5](#d-algangror_cmp5)
    - “That's all? One lousy necklace for all this trouble I went through?” → [algangror_cmp4](#d-algangror_cmp4)

    <span id="d-algangror_story3"></span>**`algangror_story3`** Algangror: “I even sold some of the baskets that I used to make to a wealthy merchant that visited us from Nor City.”

    - Next → [algangror_story4](#d-algangror_story4)

    <span id="d-algangror_task2_9"></span>**`algangror_task2_9`** Algangror: “You will place them by the beds of five particular persons, and you must hide it well so that the person does not find the idol itself.”

    - Next → [algangror_task2_10](#d-algangror_task2_10)

    <span id="d-algangror_task2_done2"></span>**`algangror_task2_done2`** Algangror: “Did anyone see you or where you placed the idols?”

    - “No, I hid the idols as you instructed.” → [algangror_task2_done3](#d-algangror_task2_done3)

    <span id="d-algangror_task2_n2"></span>**`algangror_task2_n2`** Algangror: “Can I at least urge you not to disclose my location to the people of Remgard?”

    - “I will keep your location secret. Goodbye.” → *conversation ends*
    - “We'll see. Goodbye.” → *conversation ends*
    - “Don't tell me what to do! Goodbye.” → *conversation ends*

    <span id="d-algangror_told_1"></span>**`algangror_told_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [algangror_told_1a](#d-algangror_told_1a)
    - branch 2 → [algangror_told_2](#d-algangror_told_2)

    <span id="d-algangror_return_c4"></span>**`algangror_return_c4`** Algangror: “Say, you seem like a resourceful person. Would you be interested in helping me with yet another ... task?”

    - “Depends on the task.” → [algangror_task2_1](#d-algangror_task2_1)
    - “Sure.” → [algangror_task2_1](#d-algangror_task2_1)
    - “Not right now.” → [algangror_task2_d](#d-algangror_task2_d)

    <span id="d-algangror_return_c3"></span>**`algangror_return_c3`** Algangror: “I hope that will teach those *other* rats.”


    <span id="d-algangror_remgard_2"></span>**`algangror_remgard_2`** Algangror: “You see, I used to live there. To make a long story short, there were some ... ahem ... misunderstandings.”

    - Next → [algangror_remgard_3](#d-algangror_remgard_3)

    <span id="d-algangror_remgard_1"></span>**`algangror_remgard_1`** Algangror: “Oh, it's not far from here. Doesn't matter really.”

    - Next → [algangror_remgard_2](#d-algangror_remgard_2)

    <span id="d-algangror_fight_2"></span>**`algangror_fight_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [The five idols](../quests/fiveidols.md#stage-10))* → [algangror_fight_2a](#d-algangror_fight_2a)
    - branch 2 → [algangror_fight_3](#d-algangror_fight_3)

    <span id="d-algangror_fight_1a"></span>**`algangror_fight_1a`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 101 of [Of mice and men](../quests/algangror.md#stage-101)

    - branch 1 → [algangror_fight_2](#d-algangror_fight_2)

    <span id="d-algangror_3"></span>**`algangror_3`** Algangror: “Tell me, now that you have entered this house, would you be willing to help me with a small ... problem?”

    - “Sure, what's the problem?” → [algangror_4](#d-algangror_4)
    - “Maybe, it depends on what the problem is.” → [algangror_4](#d-algangror_4)
    - “Maybe, it depends on what type of reward we are talking about.” → [algangror_3c](#d-algangror_3c)
    - “No way. You are acting way too creepy for me.” → [algangror_decline_1](#d-algangror_decline_1)

    <span id="d-algangror_cmp4"></span>**`algangror_cmp4`** Algangror: “Do not underestimate it, my friend.”

    - Next → [algangror_cmp5](#d-algangror_cmp5)

    <span id="d-algangror_story4"></span>**`algangror_story4`** Algangror: “However, even the easy life gets boring after a while. I believe it is in our nature to strive for new and better things, to free us from the boredom of day-to-day life.”

    - Next → [algangror_story5](#d-algangror_story5)

    <span id="d-algangror_task2_10"></span>**`algangror_task2_10`** Algangror: “Remember, it is of utmost importance that you be as discreet as possible about this. The idols must not be found once you have placed them, and no one must notice that you place the idols.” — **effects:** sets stage 30 of [The five idols](../quests/fiveidols.md#stage-30)

    - “Go on.” → [algangror_task2_11](#d-algangror_task2_11)

    <span id="d-algangror_task2_done3"></span>**`algangror_task2_done3`** Algangror: “Good. Thank you again for helping me.” — **effects:** sets stage 51 of [The five idols](../quests/fiveidols.md#stage-51)

    - Next → [algangror_story](#d-algangror_story)

    <span id="d-algangror_told_1a"></span>**`algangror_told_1a`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 101 of [Of mice and men](../quests/algangror.md#stage-101)

    - branch 1 → [algangror_told_2](#d-algangror_told_2)

    <span id="d-algangror_told_2"></span>**`algangror_told_2`** Algangror: “Say, despite my previous urging to you to keep my location a secret to the people of Remgard, I have this feeling that this trust has been broken. Please tell me it isn't so.”

    - “Yes, I have told Jhaeld where you are.” → [algangror_told_3](#d-algangror_told_3)
    - “[Lie] No, I have not told anyone.” → [algangror_told_3](#d-algangror_told_3)

    <span id="d-algangror_task2_1"></span>**`algangror_task2_1`** Algangror: “Now, I can't tell you what task I have in mind before I am confident that you will actually help me. Granted, you have already shown some level of respect for my need of discretion.”

    - Next → [algangror_task2_2](#d-algangror_task2_2)

    <span id="d-algangror_task2_d"></span>**`algangror_task2_d`** Algangror: “Very well, return to me once you are ready.”


    <span id="d-algangror_remgard_3"></span>**`algangror_remgard_3`** Algangror: “These days, I think they are looking for me, for some reason. Can't think of any reason why really. But I believe they are.”

    - Next → [algangror_remgard_4](#d-algangror_remgard_4)

    <span id="d-algangror_fight_2a"></span>**`algangror_fight_2a`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 100 of [The five idols](../quests/fiveidols.md#stage-100)

    - branch 1 → [algangror_fight_3](#d-algangror_fight_3)

    <span id="d-algangror_4"></span>**`algangror_4`** Algangror: “You see, I have this slight problem with ... ahem ... vermin.”

    - Next → [algangror_5](#d-algangror_5)

    <span id="d-algangror_3c"></span>**`algangror_3c`** Algangror: “Reward? No, no, I don't have anything to give you, unfortunately.”

    - “I guess you won't get any help either then.” → *conversation ends*
    - “Fine, what's the problem you want help with?” → [algangror_4](#d-algangror_4)
    - “Something feels wrong here. I better not get involved in this.” → [algangror_decline_1](#d-algangror_decline_1)

    <span id="d-algangror_story5"></span>**`algangror_story5`** Algangror: “I wanted to learn more of things that I knew nothing about, and wanted to explore things I had only read of in books before.”

    - Next → [algangror_story6](#d-algangror_story6)

    <span id="d-algangror_task2_11"></span>**`algangror_task2_11`** Algangror: “So, the first person that I want you to visit is Jhaeld. I hear that he spends most of his time in the Remgard tavern these days.” — **effects:** sets stage 31 of [The five idols](../quests/fiveidols.md#stage-31)

    - Next → [algangror_task2_12](#d-algangror_task2_12)

    <span id="d-algangror_story"></span>**`algangror_story`** Algangror: “Let me tell you my story.”

    - “Please do.” → [algangror_story1](#d-algangror_story1)
    - “Can we just skip to the end?” → [algangror_cmp1](#d-algangror_cmp1)

    <span id="d-algangror_told_3"></span>**`algangror_told_3`** Algangror: “I can feel it in me.”

    - Next → [algangror_return_d2](#d-algangror_return_d2)

    <span id="d-algangror_task2_2"></span>**`algangror_task2_2`** Algangror: “Nor can I describe my reasoning behind this task before you are done with it.”

    - Next → [algangror_task2_3](#d-algangror_task2_3)

    <span id="d-algangror_remgard_4"></span>**`algangror_remgard_4`** Algangror: “Because of our previous ... misunderstanding, I think it's best they don't find out that I'm here.”

    - Next → [algangror_remgard_5](#d-algangror_remgard_5)

    <span id="d-algangror_5"></span>**`algangror_5`** Algangror: “Always sneaking around, always trying to cause mischief.”

    - Next → [algangror_6](#d-algangror_6)

    <span id="d-algangror_story6"></span>**`algangror_story6`** Algangror: “So I went to Nor City myself, and visited many ... interesting people and ... dark corners.”

    - Next → [algangror_story7](#d-algangror_story7)

    <span id="d-algangror_task2_12"></span>**`algangror_task2_12`** Algangror: “Secondly, I want you to visit one of the farmers named Larni. He lives with his wife Caeda here in Remgard in one of the northern cabins.” — **effects:** sets stage 32 of [The five idols](../quests/fiveidols.md#stage-32)

    - Next → [algangror_task2_13](#d-algangror_task2_13)

    <span id="d-algangror_task2_3"></span>**`algangror_task2_3`** Algangror: “Rest assured, you will be sufficiently rewarded by helping me. In fact, you see this necklace here? It has some peculiar powers that many people seek.”

    - Next → [algangror_task2_4](#d-algangror_task2_4)

    <span id="d-algangror_remgard_5"></span>**`algangror_remgard_5`** Algangror: “Therefore, I ask of you not to reveal my whereabouts to them.”

    - “OK.” → [algangror_remgard_6](#d-algangror_remgard_6)
    - “[Lie] OK.” → [algangror_remgard_6](#d-algangror_remgard_6)

    <span id="d-algangror_6"></span>**`algangror_6`** Algangror: “Fortunately, I managed to capture some of them, and locked them in my basement.”

    - Next → [algangror_7](#d-algangror_7)

    <span id="d-algangror_story7"></span>**`algangror_story7`** Algangror: “Naturally, I was thrilled of the knowledge I gained from the experience, and from what I learned while there.”

    - “What then?” → [algangror_story8](#d-algangror_story8)

    <span id="d-algangror_task2_13"></span>**`algangror_task2_13`** Algangror: “The third person is Arnal the weapon-smith, that lives in the northwest of Remgard.” — **effects:** sets stage 33 of [The five idols](../quests/fiveidols.md#stage-33)

    - Next → [algangror_task2_14](#d-algangror_task2_14)

    <span id="d-algangror_task2_4"></span>**`algangror_task2_4`** Algangror: “The world around you seems to move a bit slower when you wear it.” — **effects:** sets stage 10 of [The five idols](../quests/fiveidols.md#stage-10)

    - “OK. I will help you with your task.” → [algangror_task2_6](#d-algangror_task2_6)
    - “OK, I'll help. I'm always interested in new items.” → [algangror_task2_6](#d-algangror_task2_6)
    - “It all depends on what you want me to do.” → [algangror_task2_5](#d-algangror_task2_5)
    - “Something feels wrong here. I don't think I should help you.” → [algangror_task2_n](#d-algangror_task2_n)

    <span id="d-algangror_remgard_6"></span>**`algangror_remgard_6`** Algangror: “Thank you. Under no circumstances should you tell them where I am. They will most likely try to persuade you into revealing my location.”

    - “OK.” → [algangror_remgard_7](#d-algangror_remgard_7)

    <span id="d-algangror_7"></span>**`algangror_7`** Algangror: “Now, I can't handle them myself because of certain ... issues.”

    - Next → [algangror_8](#d-algangror_8)

    <span id="d-algangror_story8"></span>**`algangror_story8`** Algangror: “As I got back home, I wanted to continue practicing what I had observed and learned while in Nor City.”

    - Next → [algangror_story9](#d-algangror_story9)

    <span id="d-algangror_task2_14"></span>**`algangror_task2_14`** Algangror: “Fourth is Emerei, that can probably be found in his house to the southeast of Remgard.” — **effects:** sets stage 34 of [The five idols](../quests/fiveidols.md#stage-34)

    - Next → [algangror_task2_15](#d-algangror_task2_15)

    <span id="d-algangror_task2_6"></span>**`algangror_task2_6`** Algangror: “Good, good.” — **effects:** sets stage 20 of [The five idols](../quests/fiveidols.md#stage-20)

    - Next → [algangror_task2_7](#d-algangror_task2_7)

    <span id="d-algangror_task2_5"></span>**`algangror_task2_5`** Algangror: “As I said, I cannot tell you what task I have in mind, or my reasoning behind it until you are done. I would need your total ... cooperation with this.”

    - “OK. I will agree to help you with your task.” → [algangror_task2_6](#d-algangror_task2_6)
    - “OK, I'll help. I'm always interested in new items.” → [algangror_task2_6](#d-algangror_task2_6)
    - “No. I will not help you unless you tell me what you want me to do.” → [algangror_task2_n](#d-algangror_task2_n)
    - “No, I would never help someone like you.” → [algangror_task2_n](#d-algangror_task2_n)

    <span id="d-algangror_remgard_7"></span>**`algangror_remgard_7`** Algangror: “Under no circumstances.” — **effects:** sets stage 21 of [Of mice and men](../quests/algangror.md#stage-21)


    <span id="d-algangror_8"></span>**`algangror_8`** Algangror: “That's where you come in. Would you be willing to ... ahem ... handle those rodents for me?” — **effects:** sets stage 11 of [Of mice and men](../quests/algangror.md#stage-11)

    - “Sure, some rodents, I can handle that.” → [algangror_9](#d-algangror_9)
    - “No problem, I'll be right back once I have killed them.” → [algangror_9](#d-algangror_9)
    - “Something feels wrong here. I better not get involved in this.” → [algangror_decline_1](#d-algangror_decline_1)

    <span id="d-algangror_story9"></span>**`algangror_story9`** Algangror: “You could say I got obsessed with learning more. I guess the others living in Remgard did not ... share my enthusiasm. Some of them even questioned the fact that I wanted to learn more.”

    - Next → [algangror_story10](#d-algangror_story10)

    <span id="d-algangror_task2_15"></span>**`algangror_task2_15`** Algangror: “The fifth person is the farmer Carthe. Carthe lives on the eastern shore of Remgard, near the tavern.” — **effects:** sets stage 35 of [The five idols](../quests/fiveidols.md#stage-35)

    - Next → [algangror_task2_16](#d-algangror_task2_16)

    <span id="d-algangror_9"></span>**`algangror_9`** Algangror: “Splendid. Return to me with some proof that they have been dealt with.” — **effects:** sets stage 15 of [Of mice and men](../quests/algangror.md#stage-15)


    <span id="d-algangror_story10"></span>**`algangror_story10`** Algangror: “So I told myself that others would not hinder me in my curiosity to better myself.”

    - Next → [algangror_story11](#d-algangror_story11)

    <span id="d-algangror_task2_16"></span>**`algangror_task2_16`** Algangror: “Once you have placed these five idols by the beds of these five people, return to me as soon as possible.”

    - Next → [algangror_task2_17](#d-algangror_task2_17)

    <span id="d-algangror_story11"></span>**`algangror_story11`** Algangror: “Those books that I bought from the Blackmarrow residence in Nor City - I must have read them all perhaps five times over. This was something completely new to me, and at the same time very exciting.”

    - “What then?” → [algangror_story12](#d-algangror_story12)

    <span id="d-algangror_task2_17"></span>**`algangror_task2_17`** Algangror: “Again, I cannot stress this enough - you must not tell anyone about these idols, and you must not be seen while placing them.”

    - “I understand.” → [algangror_task2_18s](#d-algangror_task2_18s)

    <span id="d-algangror_story12"></span>**`algangror_story12`** Algangror: “For some reason, the others in Remgard started giving me strange looks, and I could hear the whispers behind my back.”

    - Next → [algangror_story13](#d-algangror_story13)

    <span id="d-algangror_task2_18s"></span>**`algangror_task2_18s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37))* → [algangror_task2_19](#d-algangror_task2_19)
    - branch 2 → [algangror_task2_18](#d-algangror_task2_18)

    <span id="d-algangror_story13"></span>**`algangror_story13`** Algangror: “I was even barred from the tavern. 'People come here for a good time, and we don't want people like you here ruining that' they said. What fools they are.”

    - Next → [algangror_story14](#d-algangror_story14)

    <span id="d-algangror_task2_19"></span>**`algangror_task2_19`** Algangror: “Now go, and please hurry, we might not have much time.”


    <span id="d-algangror_task2_18"></span>**`algangror_task2_18`** Algangror: “Here are the idols.” — **effects:** gives [Small idol](../items/algangror_idol.md), sets stage 37 of [The five idols](../quests/fiveidols.md#stage-37)

    - “I will be back shortly.” → [algangror_task2_19](#d-algangror_task2_19)
    - “This should be easy.” → [algangror_task2_19](#d-algangror_task2_19)

    <span id="d-algangror_story14"></span>**`algangror_story14`** Algangror: “I heard one woman whispering to her boy, 'Don't look at her, she'll turn you to stone!'. Others just turned the other way when they met me.”

    - Next → [algangror_story15](#d-algangror_story15)

    <span id="d-algangror_story15"></span>**`algangror_story15`** Algangror: “What fools they are.”

    - “So what happened?” → [algangror_story16](#d-algangror_story16)

    <span id="d-algangror_story16"></span>**`algangror_story16`** Algangror: “One day, Jhaeld showed up at my doorstep with a group of guards.”

    - Next → [algangror_story17](#d-algangror_story17)

    <span id="d-algangror_story17"></span>**`algangror_story17`** Algangror: “The people of Remgard had decided that I could not stay there anymore, he said. The things I did were causing other people harm, he said.”

    - Next → [algangror_story18](#d-algangror_story18)

    <span id="d-algangror_story18"></span>**`algangror_story18`** Algangror: “What had I done, I asked myself? I had never hurt anyone, much less affected anyone with my ... experiments. Am I not allowed to do what I wish?”

    - Next → [algangror_story19](#d-algangror_story19)

    <span id="d-algangror_story19"></span>**`algangror_story19`** Algangror: “I had little chance to argue, however. The guards led me out of the city. They did not even let me gather my things. All my books, all my notes and all my findings - gone. I lost everything.” — **effects:** sets stage 60 of [The five idols](../quests/fiveidols.md#stage-60)

    - “What now?” → [algangror_story20](#d-algangror_story20)

    <span id="d-algangror_story20"></span>**`algangror_story20`** Algangror: “All this happened several seasons ago. I knew I had to get revenge for what they did to me.”

    - Next → [algangror_story21](#d-algangror_story21)

    <span id="d-algangror_story21"></span>**`algangror_story21`** Algangror: “Oh, how I despise them all. The people that gave me those looks, the people that whispered behind my back, and most of all that fool Jhaeld.”

    - Next → [algangror_story22](#d-algangror_story22)

    <span id="d-algangror_story22"></span>**`algangror_story22`** Algangror: “So, I decided to extend my ... experiments ... to larger things. To people, to living things. This is the perfect opportunity to learn even more than what is in the books.”

    - Next → [algangror_story23](#d-algangror_story23)

    <span id="d-algangror_story23"></span>**`algangror_story23`** Algangror: “To think that I could do it while at the same time get revenge on those despicable people - it's an excellent plan, if I may say so myself. He he.”

    - “So, what happened to all those people that have gone missing?” → [algangror_story24](#d-algangror_story24)

    <span id="d-algangror_story24"></span>**`algangror_story24`** Algangror: “I lured them here. Once I managed to trap them, I placed a curse on them that, in theory, should have only made them unable to speak.”

    - Next → [algangror_story25](#d-algangror_story25)

    <span id="d-algangror_story25"></span>**`algangror_story25`** Algangror: “Maybe I haven't understood everything correctly from the books that I have read, since instead of making them unable to speak, they were all turned into rats instead.”

    - Next → [algangror_story26](#d-algangror_story26)

    <span id="d-algangror_story26"></span>**`algangror_story26`** Algangror: “Practice makes perfect, I suppose. Ha ha.”

    - “Wait, does this mean that those rats I killed for you were...” → [algangror_story27](#d-algangror_story27)

    <span id="d-algangror_story27"></span>**`algangror_story27`** Algangror: “Oh yes. With your help, they are now one less problem to deal with, so to speak. He he.”

    - Next → [algangror_story28](#d-algangror_story28)

    <span id="d-algangror_story28"></span>**`algangror_story28`** Algangror: “So, that's my story. Thank you for listening to it.” — **effects:** sets stage 61 of [The five idols](../quests/fiveidols.md#stage-61)

    - “I understand, and I agree with your actions.” → [algangror_story29a](#d-algangror_story29a)
    - “I do not fully agree with your actions.” → [algangror_story29b](#d-algangror_story29b)
    - “What you did could never be justified!” → [algangror_story29b](#d-algangror_story29b)

    <span id="d-algangror_story29a"></span>**`algangror_story29a`** Algangror: “Thank you. It is good to know there are more people interested in learning more.”

    - Next → [algangror_cmp1](#d-algangror_cmp1)

    <span id="d-algangror_story29b"></span>**`algangror_story29b`** Algangror: “I never expected you to understand it. No one else seems to understand me either. Oh well, your loss, I guess.”

    - Next → [algangror_cmp1](#d-algangror_cmp1)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change<br>Dialogue: 30 lines changed<br>· text: “He he. I bet you sure showed them. Excellent. Thank you for .. ahem .…” → “He he. I bet you sure showed them. Excellent. Thank you for ... ahem …”<br>· text: “Tell me, now that you have entered this house, would you be willing t…” → “Tell me, now that you have entered this house, would you be willing t…” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed<br>· text: “Ah yes. After all, you are just a child and I can understand that all…” → “Ah yes. After all, you are just a child and I can understand that all…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algangror.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algangror.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algangror.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algangror.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `algangror` · Data from v0.8.18</small>
