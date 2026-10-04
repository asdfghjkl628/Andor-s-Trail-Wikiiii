# ![](../assets/icons/monsters/monsters_karvis2_0.png){ .sprite } Aryfora

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [stoutford_gate](../maps/stoutford_gate.md)

## Quests

- [The roots of love](../quests/roots_love.md): stages 10, 30, 40, 45
- [The thorns of vengeance](../quests/thorns_vengeance.md): stages 10, 20, 30, 32, 40, 50, 76, 90

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Aryfora. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_widow_select_0.json" data-npc="Aryfora" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (67 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_widow_select_0"></span>**`stoutford_widow_select_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-80))* → [stoutford_widow_thorns80_0](#d-stoutford_widow_thorns80_0)
    - branch 2 *(if reached stage 76 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-76))* → [stoutford_widow_thorns74_1](#d-stoutford_widow_thorns74_1)
    - branch 3 *(if reached stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75))* → [stoutford_widow_thorns72_70](#d-stoutford_widow_thorns72_70)
    - branch 4 *(if reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74))* → [stoutford_widow_thorns74_0](#d-stoutford_widow_thorns74_0)
    - branch 5 *(if reached stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72))* → [stoutford_widow_thorns72_0](#d-stoutford_widow_thorns72_0)
    - branch 6 *(if reached stage 70 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-70))* → [stoutford_widow_thorns70_0](#d-stoutford_widow_thorns70_0)
    - branch 7 *(if reached stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50))* → [stoutford_widow_thorns50_0](#d-stoutford_widow_thorns50_0)
    - branch 8 *(if reached stage 40 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-40))* → [stoutford_widow_thorns40_0](#d-stoutford_widow_thorns40_0)
    - branch 9 *(if reached stage 32 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-32))* → [stoutford_widow_thorns20_5](#d-stoutford_widow_thorns20_5)
    - branch 10 *(if reached stage 30 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-30))* → [stoutford_widow_thorns30_0](#d-stoutford_widow_thorns30_0)
    - branch 11 *(if reached stage 20 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-20))* → [stoutford_widow_thorns20_0](#d-stoutford_widow_thorns20_0)
    - branch 12 *(if reached stage 10 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-10))* → [stoutford_widow_thorns10_0](#d-stoutford_widow_thorns10_0)
    - Next *(if reached stage 45 of [The roots of love](../quests/roots_love.md#stage-45))* → [stoutford_widow_roots4045_0](#d-stoutford_widow_roots4045_0)
    - Next *(if reached stage 40 of [The roots of love](../quests/roots_love.md#stage-40))* → [stoutford_widow_roots4045_0](#d-stoutford_widow_roots4045_0)
    - Next *(if reached stage 30 of [The roots of love](../quests/roots_love.md#stage-30))* → [stoutford_widow_roots30_0](#d-stoutford_widow_roots30_0)
    - Next *(if reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10))* → [stoutford_widow_roots10_0](#d-stoutford_widow_roots10_0)
    - Next → [stoutford_widow_0](#d-stoutford_widow_0)

    <span id="d-stoutford_widow_thorns80_0"></span>**`stoutford_widow_thorns80_0`** Aryfora: “You look like you are in a good mood. What did you accomplish?”

    - “Blornvale is gone! Tahalendor came to hear him give a detailed confession to the murder. Then he took him away.” → [stoutford_widow_thorns80_1](#d-stoutford_widow_thorns80_1)

    <span id="d-stoutford_widow_thorns74_1"></span>**`stoutford_widow_thorns74_1`** Aryfora: “Oh no! Now I will never get justice!” — **effects:** sets stage 76 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-76)

    - “I did my best.” → *conversation ends*

    <span id="d-stoutford_widow_thorns72_70"></span>**`stoutford_widow_thorns72_70`** Aryfora: “Any news about the murderer?”

    - “Yes, but it's not good news. Tahalendor won't believe me.” → [stoutford_widow_thorns74_1](#d-stoutford_widow_thorns74_1)

    <span id="d-stoutford_widow_thorns74_0"></span>**`stoutford_widow_thorns74_0`** Aryfora: “Any news about the murderer?”

    - “Yes, but it's not good news. He guessed that I tried to entrap him, and is cautious now.” → [stoutford_widow_thorns74_1](#d-stoutford_widow_thorns74_1)

    <span id="d-stoutford_widow_thorns72_0"></span>**`stoutford_widow_thorns72_0`** Aryfora: “Any news about the murderer?”

    - “Yes, he confessed to poisoning your father.” → *conversation ends*

    <span id="d-stoutford_widow_thorns70_0"></span>**`stoutford_widow_thorns70_0`** Aryfora: “Did Blornvale drink the potion of truth?”

    - “Yes. I just have to make him confess to the murder.” → *conversation ends*

    <span id="d-stoutford_widow_thorns50_0"></span>**`stoutford_widow_thorns50_0`** Aryfora: “Did Blornvale drink the potion of truth?”

    - “Eh, almost.” → *conversation ends*

    <span id="d-stoutford_widow_thorns40_0"></span>**`stoutford_widow_thorns40_0`** Aryfora: “With the potion of truth you will make Blornvale confess that he poisoned his brother.”

    - “But who would believe me, a stranger?” → [stoutford_widow_thorns40_1](#d-stoutford_widow_thorns40_1)

    <span id="d-stoutford_widow_thorns20_5"></span>**`stoutford_widow_thorns20_5`** [Dummy NPC](../monsters/none.md): “Aryfora just glares at you. Her eyes are icy cold.”


    <span id="d-stoutford_widow_thorns30_0"></span>**`stoutford_widow_thorns30_0`** Aryfora: “Now I take three potions of the brave *chanting* ... add my prepared ingredients *chanting* ... shake it *chanting* ... shake it - ready. Here, be careful with it. Potions of truth are rare.” — **effects:** sets stage 40 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-40), gives 1× [Potion of truth](../items/potion_truth.md)

    - “Thank you. What do you have in mind now?” → [stoutford_widow_thorns30_1](#d-stoutford_widow_thorns30_1)

    <span id="d-stoutford_widow_thorns20_0"></span>**`stoutford_widow_thorns20_0`** Aryfora: “Did you get the three potions of the brave from Blornvale?”

    - “No, not yet.” → *conversation ends*
    - “Yes, here they are.” *(if hand over 3× [Potion of the brave](../items/potion_brave.md))* → [stoutford_widow_thorns20_1](#d-stoutford_widow_thorns20_1)
    - “Yes, I have them. But I won't give them to you.” *(if carry 3× [Potion of the brave](../items/potion_brave.md))* → [stoutford_widow_thorns20_2](#d-stoutford_widow_thorns20_2)

    <span id="d-stoutford_widow_thorns10_0"></span>**`stoutford_widow_thorns10_0`** Aryfora: “To begin, you'll have to buy some potions of the brave from him. I need these as the base for a potion I want to create. Don't forget: three potions of the brave.”

    - “What will you do with them?” → [stoutford_widow_thorns10_1](#d-stoutford_widow_thorns10_1)

    <span id="d-stoutford_widow_roots4045_0"></span>**`stoutford_widow_roots4045_0`** Aryfora: “Thank you very much for the flowers. Is there anything I can do for you?”

    - “Your potion was great! Can I have some more?” *(if used 1× [Potion of deftness](../items/potion_deftness.md))* → [stoutford_widow_roots4045_1](#d-stoutford_widow_roots4045_1)
    - “That potion you made smells really interesting. Can I buy another?” *(if carry 1× [Potion of deftness](../items/potion_deftness.md))* → [stoutford_widow_roots4045_1](#d-stoutford_widow_roots4045_1)
    - “See you later.” → *conversation ends*

    <span id="d-stoutford_widow_roots30_0"></span>**`stoutford_widow_roots30_0`** Aryfora: “How did you find these flowers?”

    - “Caeda, Noraed's sister, gave them to me. She sends you her condolences.” → [stoutford_widow_roots30_3](#d-stoutford_widow_roots30_3)
    - “I found them in the wild around Remgard.” → [stoutford_widow_roots30_1](#d-stoutford_widow_roots30_1)

    <span id="d-stoutford_widow_roots10_0"></span>**`stoutford_widow_roots10_0`** Aryfora: “You're back! Have you found some damerilias yet?”

    - “Yes. Here they are, three of the most beautiful damerilias.” *(if hand over 3× [Damerilias](../items/damerilias.md))* → [stoutford_widow_roots10_2](#d-stoutford_widow_roots10_2)
    - “Yes. Here they are, two of the most beautiful damerilias.” *(if NOT carry 3× [Damerilias](../items/damerilias.md); carry 2× [Damerilias](../items/damerilias.md))* → [stoutford_widow_roots10_1a](#d-stoutford_widow_roots10_1a)
    - “Yes. Here it is, the most beautiful one.” *(if NOT carry 2× [Damerilias](../items/damerilias.md); carry 1× [Damerilias](../items/damerilias.md))* → [stoutford_widow_roots10_1a](#d-stoutford_widow_roots10_1a)
    - “No, not yet.” *(if NOT carry 1× [Damerilias](../items/damerilias.md))* → [stoutford_widow_roots10_1](#d-stoutford_widow_roots10_1)

    <span id="d-stoutford_widow_0"></span>**`stoutford_widow_0`** Aryfora: “Please. Leave me alone. I'm mourning.”

    - “Sorry for your loss.” → *conversation ends*
    - “Whatever.” → *conversation ends*
    - “Is there anything I can do to ease your pain?” → [stoutford_widow_1](#d-stoutford_widow_1)

    <span id="d-stoutford_widow_thorns80_1"></span>**`stoutford_widow_thorns80_1`** Aryfora: “At last! How can I thank you?”

    - “Oh, that was just a trifle.” → [stoutford_widow_thorns80_2](#d-stoutford_widow_thorns80_2)
    - “No problem. I can handle myself.” → [stoutford_widow_thorns80_2](#d-stoutford_widow_thorns80_2)

    <span id="d-stoutford_widow_thorns40_1"></span>**`stoutford_widow_thorns40_1`** Aryfora: “You are right. We need a credible witness...”

    - Next → [stoutford_widow_thorns40_2](#d-stoutford_widow_thorns40_2)

    <span id="d-stoutford_widow_thorns30_1"></span>**`stoutford_widow_thorns30_1`** Aryfora: “Isn't it obvious?”

    - Next → [stoutford_widow_thorns40_0](#d-stoutford_widow_thorns40_0)

    <span id="d-stoutford_widow_thorns20_1"></span>**`stoutford_widow_thorns20_1`** Aryfora: “Great! This will finally break him.” — **effects:** sets stage 30 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-30)

    - “I hope so. He is a most unfriendly guy.” → [stoutford_widow_thorns30_0](#d-stoutford_widow_thorns30_0)

    <span id="d-stoutford_widow_thorns20_2"></span>**`stoutford_widow_thorns20_2`** Aryfora: “What? Do you betray me? We must get rid of Blornvale!”

    - “I don't quit think so. He is an honest person.” → [stoutford_widow_thorns20_4](#d-stoutford_widow_thorns20_4)
    - “I'm just kidding. Here, take the three potions.” *(if hand over 3× [Potion of the brave](../items/potion_brave.md))* → [stoutford_widow_thorns20_1](#d-stoutford_widow_thorns20_1)

    <span id="d-stoutford_widow_thorns10_1"></span>**`stoutford_widow_thorns10_1`** Aryfora: “The potion of the brave can be enhanced to the much more useful potion of truth. These additions are easy, but for the potion of the brave I would need a laboratory.”

    - Next → [stoutford_widow_thorns10_2](#d-stoutford_widow_thorns10_2)

    <span id="d-stoutford_widow_roots4045_1"></span>**`stoutford_widow_roots4045_1`** Aryfora: “No, sorry.”

    - “Too bad.” → *conversation ends*
    - “Oh. Why is that?” → [stoutford_widow_roots4045_2](#d-stoutford_widow_roots4045_2)

    <span id="d-stoutford_widow_roots30_3"></span>**`stoutford_widow_roots30_3`** Aryfora: “Noraed had a sister? He never talked about his family. He said he had a happy childhood, but that's it. I think he didn't want me to ask to go there with him. I'd love to meet her someday.” — **effects:** sets stage 40 of [The roots of love](../quests/roots_love.md#stage-40)

    - “I'm sure she feels the same.” → [stoutford_widow_roots30_2](#d-stoutford_widow_roots30_2)
    - “Who knows...” → [stoutford_widow_roots30_2](#d-stoutford_widow_roots30_2)
    - “That seems unlikely.” → [stoutford_widow_roots30_2](#d-stoutford_widow_roots30_2)

    <span id="d-stoutford_widow_roots30_1"></span>**`stoutford_widow_roots30_1`** Aryfora: “Is that so? Remgard must be a beautiful place to have such nice flowers growing in the wild.” — **effects:** sets stage 45 of [The roots of love](../quests/roots_love.md#stage-45)

    - “Beautiful, but deadly to get there!” → [stoutford_widow_roots30_2](#d-stoutford_widow_roots30_2)
    - “Yeah, maybe...” → [stoutford_widow_roots30_2](#d-stoutford_widow_roots30_2)

    <span id="d-stoutford_widow_roots10_2"></span>**`stoutford_widow_roots10_2`** Aryfora: “Oh. They're beautiful! Thank you! Here, take this potion as your reward.” — **effects:** sets stage 30 of [The roots of love](../quests/roots_love.md#stage-30), gives 1× [Potion of deftness](../items/potion_deftness.md)

    - Next → [stoutford_widow_roots30_0](#d-stoutford_widow_roots30_0)

    <span id="d-stoutford_widow_roots10_1a"></span>**`stoutford_widow_roots10_1a`** Aryfora: “Oh. But that is not enough - what would that look like! There must be at least 3 damerilias for the grave. Please...”

    - “Alright. I'll go there again.” → [stoutford_widow_12](#d-stoutford_widow_12)

    <span id="d-stoutford_widow_roots10_1"></span>**`stoutford_widow_roots10_1`** Aryfora: “Oh. Come back to me if you find some, will you?”


    <span id="d-stoutford_widow_1"></span>**`stoutford_widow_1`** Aryfora: “Oh. No one asked before you. I didn't even think about it.”

    - Next → [stoutford_widow_2](#d-stoutford_widow_2)

    <span id="d-stoutford_widow_thorns80_2"></span>**`stoutford_widow_thorns80_2`** Aryfora: “Now I can move back into my father's house and create potions again. I will leave at once. Please come and visit me at any time.” — **effects:** sets stage 90 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-90), removes monsters from stoutford_gate, spawns monsters on stoutford_potion

    - “Bye.” → *NPC leaves*
    - “I will.” → *NPC leaves*

    <span id="d-stoutford_widow_thorns40_2"></span>**`stoutford_widow_thorns40_2`** Aryfora: “Best would be Tahalendor himself. Yes, you must persuade the priest to be present when Blornvale tells the whole story.” — **effects:** sets stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50)

    - “Tahalendor? How can I do that?” → [stoutford_widow_thorns40_3](#d-stoutford_widow_thorns40_3)

    <span id="d-stoutford_widow_thorns20_4"></span>**`stoutford_widow_thorns20_4`** Aryfora: “I would not have expected that from you!” — **effects:** sets stage 32 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-32)


    <span id="d-stoutford_widow_thorns10_2"></span>**`stoutford_widow_thorns10_2`** Aryfora: “That is why you must get the potions of the brave from Blornvale. Oh how I hate that name! Be quick.” — **effects:** sets stage 20 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-20), spawns monsters on stoutford_sw

    - “I will be right back.” → *conversation ends*
    - “By chance, I have three potions of the brave with me. Here, take them.” *(if hand over 3× [Potion of the brave](../items/potion_brave.md))* → [stoutford_widow_thorns20_1](#d-stoutford_widow_thorns20_1)

    <span id="d-stoutford_widow_roots4045_2"></span>**`stoutford_widow_roots4045_2`** Aryfora: “I gave you my last one, and I can't brew potions anymore.”

    - Next → [stoutford_widow_roots4045_3](#d-stoutford_widow_roots4045_3)

    <span id="d-stoutford_widow_roots30_2"></span>**`stoutford_widow_roots30_2`** Aryfora: “Anyway. Thank you very much.”

    - “You're welcome.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*
    - “That wasn't worth the trouble.” → *conversation ends*

    <span id="d-stoutford_widow_12"></span>**`stoutford_widow_12`** Aryfora: “Thank you for listening to me anyway. I wish you the best.”

    - “Goodbye.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-stoutford_widow_2"></span>**`stoutford_widow_2`** Aryfora: “Are you willing to hear my story?”

    - “Oh no. Not a long story.” → *conversation ends*
    - “If it can be of any comfort ... go ahead.” → [stoutford_widow_3](#d-stoutford_widow_3)

    <span id="d-stoutford_widow_thorns40_3"></span>**`stoutford_widow_thorns40_3`** Aryfora: “I have full confidence in you. You will come up with something.”


    <span id="d-stoutford_widow_roots4045_3"></span>**`stoutford_widow_roots4045_3`** Aryfora: “It is something I gave up long ago.”

    - “Why did you stop?” → [stoutford_widow_roots4045_4](#d-stoutford_widow_roots4045_4)
    - “I understand.” → *conversation ends*

    <span id="d-stoutford_widow_3"></span>**`stoutford_widow_3`** Aryfora: “Thank you. My name is Aryfora. I met my husband here in Stoutford, during the fair. He offered me a beautiful flower, one that I had never seen before.”

    - Next → [stoutford_widow_4](#d-stoutford_widow_4)

    <span id="d-stoutford_widow_roots4045_4"></span>**`stoutford_widow_roots4045_4`** Aryfora: “It's a long story.”

    - “Never mind. Now I understand why Noraed traveled so far every year.” → *conversation ends*
    - “Go on, please.” → [stoutford_widow_roots4045_5](#d-stoutford_widow_roots4045_5)

    <span id="d-stoutford_widow_4"></span>**`stoutford_widow_4`** Aryfora: “He was smart and handsome and we quickly fell in love. He was from a town called Remgard. His name was Noraed.”

    - Next → [stoutford_widow_5](#d-stoutford_widow_5)

    <span id="d-stoutford_widow_roots4045_5"></span>**`stoutford_widow_roots4045_5`** Aryfora: “My father was the alchemist of this town. He was very talented, and inspired. He experimented with all sorts of ingredients from all over Dhayavar. Whatever he could get from the travellers stopping at Stoutford.”

    - Next → [stoutford_widow_roots4045_6](#d-stoutford_widow_roots4045_6)

    <span id="d-stoutford_widow_5"></span>**`stoutford_widow_5`** Aryfora: “He told me that it is very far from here, to the northeast, beyond the river and the mountains.”

    - Next → [stoutford_widow_6](#d-stoutford_widow_6)

    <span id="d-stoutford_widow_roots4045_6"></span>**`stoutford_widow_roots4045_6`** Aryfora: “He created unique potions, and no other alchemist that I have heard of managed to reproduce his recipes.”

    - Next → [stoutford_widow_roots4045_7](#d-stoutford_widow_roots4045_7)

    <span id="d-stoutford_widow_6"></span>**`stoutford_widow_6`** Aryfora: “I've never been there, as he always said how dangerous that road was, but every year, for our anniversary, he went back to bring me a damerilia, the same flower he offered me on the day we met.”

    - “How romantic!” → [stoutford_widow_7](#d-stoutford_widow_7)

    <span id="d-stoutford_widow_roots4045_7"></span>**`stoutford_widow_roots4045_7`** Aryfora: “When he deemed me old and responsible enough, he started teaching me his art.”

    - Next → [stoutford_widow_roots4045_8](#d-stoutford_widow_roots4045_8)

    <span id="d-stoutford_widow_7"></span>**`stoutford_widow_7`** Aryfora: “During one of the recent attacks on Stoutford, my husband sacrificed his life to save mine. Now, I can't do anything but mourn next to his grave.”

    - “He must have loved you very much.” → [stoutford_widow_8](#d-stoutford_widow_8)

    <span id="d-stoutford_widow_roots4045_8"></span>**`stoutford_widow_roots4045_8`** Aryfora: “He passed away a few years later. They said he poisoned himself during a new experiment, but I never believed it.”

    - “Sorry, I have to go now.” → *conversation ends*
    - “Who are "they"?” → [stoutford_widow_roots4045_9](#d-stoutford_widow_roots4045_9)

    <span id="d-stoutford_widow_8"></span>**`stoutford_widow_8`** Aryfora: “I'd really love to place damerilias on his grave, as a symbol of our love.”

    - “What a nice idea!” → [stoutford_widow_9](#d-stoutford_widow_9)
    - “Uh oh, I suspect I am going to be asked for something...” → [stoutford_widow_9](#d-stoutford_widow_9)

    <span id="d-stoutford_widow_roots4045_9"></span>**`stoutford_widow_roots4045_9`** Aryfora: “Our priest, Tahalendor, was convinced by my uncle, Blornvale, my father's own brother.”

    - Next → [stoutford_widow_roots4045_10](#d-stoutford_widow_roots4045_10)

    <span id="d-stoutford_widow_9"></span>**`stoutford_widow_9`** Aryfora: “But it would be reckless of me to ask such a young kid as you to go so far to the northeast.”

    - “I've had enough - bye.” → *conversation ends*
    - “Don't worry about me. I can handle myself.” → [stoutford_widow_10](#d-stoutford_widow_10)
    - “I'm an adventurer. I'm afraid of nothing.” → [stoutford_widow_10](#d-stoutford_widow_10)
    - “Remgard. *sigh*. OK, I'll do it.” *(if reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170))* → [stoutford_widow_10](#d-stoutford_widow_10)

    <span id="d-stoutford_widow_roots4045_10"></span>**`stoutford_widow_roots4045_10`** Aryfora: “My uncle also convinced the whole village that I was too young to be their alchemist, and that they needed him to take over the shop.”

    - Next → [stoutford_widow_roots4045_11](#d-stoutford_widow_roots4045_11)

    <span id="d-stoutford_widow_10"></span>**`stoutford_widow_10`** Aryfora: “Really? If you manage to do it, I'll make sure to reward you with something only I can do, and that I haven't done in a long time.” — **effects:** sets stage 10 of [The roots of love](../quests/roots_love.md#stage-10)

    - “And what would that be?” → [stoutford_widow_11](#d-stoutford_widow_11)
    - “Great!” → [stoutford_widow_12](#d-stoutford_widow_12)
    - “I guess I have work to do now.” → [stoutford_widow_12](#d-stoutford_widow_12)

    <span id="d-stoutford_widow_roots4045_11"></span>**`stoutford_widow_roots4045_11`** Aryfora: “They all agreed, even though my uncle is a lousy alchemist. I was sent to work on a farm, while my uncle took my father's house and opened the shop again.”

    - “Outrageous!” → [stoutford_widow_roots4045_12](#d-stoutford_widow_roots4045_12)

    <span id="d-stoutford_widow_11"></span>**`stoutford_widow_11`** Aryfora: “That's a secret. I can't tell you, but you'll know when you'll see it.”

    - Next → [stoutford_widow_12](#d-stoutford_widow_12)

    <span id="d-stoutford_widow_roots4045_12"></span>**`stoutford_widow_roots4045_12`** Aryfora: “Everyone suffered from the nasty side effects of my uncle's ... I can't say potions ... poisonous imitations of my father's recipes.”

    - Next → [stoutford_widow_roots4045_13](#d-stoutford_widow_roots4045_13)

    <span id="d-stoutford_widow_roots4045_13"></span>**`stoutford_widow_roots4045_13`** Aryfora: “People complained at first, but nobody ever looked for a real solution.”

    - Next → [stoutford_widow_roots4045_14](#d-stoutford_widow_roots4045_14)

    <span id="d-stoutford_widow_roots4045_14"></span>**`stoutford_widow_roots4045_14`** Aryfora: “Seeing how things turned out, I came to suspect that my uncle is responsible for my father's death.”

    - “Do you have any evidence?” → [stoutford_widow_roots4045_15](#d-stoutford_widow_roots4045_15)
    - “And would you brew more potions if you had your father's shop back?” → [stoutford_widow_roots4045_16](#d-stoutford_widow_roots4045_16)

    <span id="d-stoutford_widow_roots4045_15"></span>**`stoutford_widow_roots4045_15`** Aryfora: “No. Every time I talk to him, he denies everything, and calls me crazy. I can tell he's lying though.”

    - “And would you brew more potions if you had your father's shop back?” → [stoutford_widow_roots4045_16](#d-stoutford_widow_roots4045_16)

    <span id="d-stoutford_widow_roots4045_16"></span>**`stoutford_widow_roots4045_16`** Aryfora: “Maybe. If the villagers asked me to, and if they recognize the guilt of my uncle.”

    - “Can I help you with this?” → [stoutford_widow_roots4045_16a](#d-stoutford_widow_roots4045_16a)

    <span id="d-stoutford_widow_roots4045_16a"></span>**`stoutford_widow_roots4045_16a`** Aryfora: “You have already done so much for me. I cannot accept that.”

    - “Oh, that's alright.” → [stoutford_widow_roots4045_17](#d-stoutford_widow_roots4045_17)

    <span id="d-stoutford_widow_roots4045_17"></span>**`stoutford_widow_roots4045_17`** Aryfora: “Really? Then I think I have a plan.”

    - Next → [stoutford_widow_roots4045_18](#d-stoutford_widow_roots4045_18)

    <span id="d-stoutford_widow_roots4045_18"></span>**`stoutford_widow_roots4045_18`** Aryfora: “My uncle is very cautious with me, but with an unknown kid, there's a chance we can make him confess.”

    - “Sounds reasonable.” → [stoutford_widow_roots4045_19](#d-stoutford_widow_roots4045_19)

    <span id="d-stoutford_widow_roots4045_19"></span>**`stoutford_widow_roots4045_19`** Aryfora: “He's a dangerous man though. Are you sure you wish to confront him?”

    - “I can do it!” → [stoutford_widow_roots4045_20](#d-stoutford_widow_roots4045_20)
    - “Eh, I'd better leave now. It's none of my business.” → *conversation ends*

    <span id="d-stoutford_widow_roots4045_20"></span>**`stoutford_widow_roots4045_20`** Aryfora: “Then it's settled.” — **effects:** sets stage 10 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-10)

    - Next → [stoutford_widow_thorns10_0](#d-stoutford_widow_thorns10_0)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 67 lines added |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_widow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stoutford_widow` · Data from v0.8.18</small>
