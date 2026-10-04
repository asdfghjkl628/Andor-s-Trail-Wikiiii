# ![](../assets/icons/monsters/monsters_rltiles1_69.png){ .sprite } Gandoren

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

## Quests

- [Feygard errands](../quests/feygard_shipment.md): stages 10, 20, 21, 22, 25, 26, 80, 81
- [Flows through the veins](../quests/loneford.md): stages 10, 11, 21
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 18

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gandoren. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/gandoren.json" data-npc="Gandoren" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (53 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gandoren"></span>**`gandoren`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 81 of [Feygard errands](../quests/feygard_shipment.md#stage-81))* → [gandoren_completed_1](#d-gandoren_completed_1)
    - branch 2 *(if reached stage 80 of [Feygard errands](../quests/feygard_shipment.md#stage-80))* → [gandoren_completed_1](#d-gandoren_completed_1)
    - branch 3 *(if reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25))* → [gandoren_deliver_1](#d-gandoren_deliver_1)
    - branch 4 *(if reached stage 22 of [Feygard errands](../quests/feygard_shipment.md#stage-22))* → [gandoren_20](#d-gandoren_20)
    - branch 5 *(if reached stage 21 of [Feygard errands](../quests/feygard_shipment.md#stage-21))* → [gandoren_20](#d-gandoren_20)
    - branch 6 *(if reached stage 20 of [Feygard errands](../quests/feygard_shipment.md#stage-20))* → [gandoren_wantshelp_1](#d-gandoren_wantshelp_1)
    - branch 7 *(if reached stage 10 of [Feygard errands](../quests/feygard_shipment.md#stage-10))* → [gandoren_noguards_1](#d-gandoren_noguards_1)
    - branch 8 → [gandoren_1](#d-gandoren_1)

    <span id="d-gandoren_completed_1"></span>**`gandoren_completed_1`** Gandoren: “You return. Thank you for helping with the shipment earlier.”

    - Next → [gandoren_completed_2](#d-gandoren_completed_2)

    <span id="d-gandoren_deliver_1"></span>**`gandoren_deliver_1`** Gandoren: “You return. Good news about the shipment I hope?”

    - “You guards seem to have a lot of equipment here, anything to trade?” → [gandoren_tr_2](#d-gandoren_tr_2)
    - “I am still working on transporting that shipment.” → [gandoren_22](#d-gandoren_22)
    - “What was I supposed to do again?” → [gandoren_21](#d-gandoren_21)
    - “Yes. I have delivered them as you ordered.” *(if reached stage 50 of [Feygard errands](../quests/feygard_shipment.md#stage-50))* → [gandoren_deliver_y_1](#d-gandoren_deliver_y_1)
    - “Yes. I have delivered them.” *(if reached stage 60 of [Feygard errands](../quests/feygard_shipment.md#stage-60))* → [gandoren_deliver_n_1](#d-gandoren_deliver_n_1)
    - “I'd rather talk about the troubles in Loneford that you had mentioned.” *(if NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [cr_loneford_st_1](#d-cr_loneford_st_1)

    <span id="d-gandoren_20"></span>**`gandoren_20`** Gandoren: “Here is the shipment that I want you to transport.” — **effects:** sets stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25), gives [Feygard iron sword](../items/fg_ironsword.md)

    - Next → [gandoren_21](#d-gandoren_21)

    <span id="d-gandoren_wantshelp_1"></span>**`gandoren_wantshelp_1`** Gandoren: “Hello again. Welcome to the Crossroads guardhouse. How may I help you?”

    - “What was that you told me before about a shipment?” → [gandoren_6](#d-gandoren_6)

    <span id="d-gandoren_noguards_1"></span>**`gandoren_noguards_1`** Gandoren: “Hello again. Welcome to the Crossroads guardhouse. How may I help you?”

    - “Can you tell me again what you told me before about recent events?” → [gandoren_3](#d-gandoren_3)

    <span id="d-gandoren_1"></span>**`gandoren_1`** Gandoren: “Hello there. Welcome to the Crossroads guardhouse. How may I help you?”

    - “You guards seem to have a lot of equipment here, anything to trade?” → [gandoren_tr_1](#d-gandoren_tr_1)
    - “What do you do here?” → [gandoren_2](#d-gandoren_2)

    <span id="d-gandoren_completed_2"></span>**`gandoren_completed_2`** Gandoren: “Is there anything I can do for you?”

    - “Do you have anything to trade?” → [gandoren_tr_3](#d-gandoren_tr_3)
    - “No thanks. Goodbye.” → *conversation ends*

    <span id="d-gandoren_tr_2"></span>**`gandoren_tr_2`** Gandoren: “I'm sorry, we only trade with allies of Feygard. Help me with the task I gave you and we might be able to work something out.”


    <span id="d-gandoren_22"></span>**`gandoren_22`** Gandoren: “Return to me once you are done.”

    - Next → [gandoren_23](#d-gandoren_23)

    <span id="d-gandoren_21"></span>**`gandoren_21`** Gandoren: “As I said, you should deliver those 10 iron swords to the guard captain stationed in a tavern called 'The Foaming Flask', near a village called Vilegard.”

    - Next → [gandoren_22](#d-gandoren_22)

    <span id="d-gandoren_deliver_y_1"></span>**`gandoren_deliver_y_1`** Gandoren: “Splendid! Feygard is in debt to you.” — **effects:** sets stage 80 of [Feygard errands](../quests/feygard_shipment.md#stage-80)

    - Next → [gandoren_delivered_1](#d-gandoren_delivered_1)

    <span id="d-gandoren_deliver_n_1"></span>**`gandoren_deliver_n_1`** Gandoren: “Splendid! Feygard is in debt to you.” — **effects:** sets stage 81 of [Feygard errands](../quests/feygard_shipment.md#stage-81)

    - Next → [gandoren_delivered_1](#d-gandoren_delivered_1)

    <span id="d-cr_loneford_st_1"></span>**`cr_loneford_st_1`** Gandoren: “Didn't you hear? They have all gotten ill.”

    - Next → [cr_loneford_st_2](#d-cr_loneford_st_2)

    <span id="d-gandoren_6"></span>**`gandoren_6`** Gandoren: “Well, we usually do not employ just any civilian. Our tasks are important for Feygard - and by extension, important for the people. Our tasks are usually not suited for commoners like you.”

    - Next → [gandoren_7](#d-gandoren_7)

    <span id="d-gandoren_3"></span>**`gandoren_3`** Gandoren: “Oh sure. Recently, we have had to focus our attention to the troubles up in Loneford.”

    - Next → [gandoren_4](#d-gandoren_4)

    <span id="d-gandoren_tr_1"></span>**`gandoren_tr_1`** Gandoren: “I'm sorry, we only trade with allies of Feygard.”


    <span id="d-gandoren_2"></span>**`gandoren_2`** Gandoren: “This guardhouse is a safe haven for merchants travelling the Duleian road. We keep law and order around here, for Feygard.”

    - “Any recent events happening?” → [gandoren_3](#d-gandoren_3)
    - “The Duleian road?” → [gandoren_dr_1](#d-gandoren_dr_1)

    <span id="d-gandoren_tr_3"></span>**`gandoren_tr_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The path is clear to me](../quests/rogorn.md#stage-60))* → [gandoren_tr_4](#d-gandoren_tr_4)
    - branch 2 → [gandoren_tr_6](#d-gandoren_tr_6)

    <span id="d-gandoren_23"></span>**`gandoren_23`** Gandoren: “I feel that I should warn you about something also. See that fellow over there in the corner? Ailshara. She seems very interested in our dealings for some reason.”

    - Next → [gandoren_24](#d-gandoren_24)

    <span id="d-gandoren_delivered_1"></span>**`gandoren_delivered_1`** Gandoren: “I hope you managed to stay away from the savages of Nor City as much as possible while being over there.”

    - Next → [gandoren_delivered_2](#d-gandoren_delivered_2)

    <span id="d-cr_loneford_st_2"></span>**`cr_loneford_st_2`** Gandoren: “It all started a few days ago. As the story goes, someone found one of the farmers passed out in one of the fields, completely white faced and shivering.”

    - Next → [cr_loneford_st_3](#d-cr_loneford_st_3)

    <span id="d-gandoren_7"></span>**`gandoren_7`** Gandoren: “But I guess the recent situation really leaves us no choice. We need to keep the guards in Loneford, and we also need to deliver this shipment. At the moment, we cannot do both.”

    - Next → [gandoren_8](#d-gandoren_8)

    <span id="d-gandoren_4"></span>**`gandoren_4`** Gandoren: “That situation has forced us to be more alert than usual, and we have had to send some guards up there to help them.”

    - Next → [gandoren_5](#d-gandoren_5)

    <span id="d-gandoren_dr_1"></span>**`gandoren_dr_1`** Gandoren: “Noticed the large road outside? That's the Duleian road. It goes all the way from the glorious city of Feygard up in the northwest down to the wretched Nor City in the southeast.”

    - “Any recent events happening?” → [gandoren_3](#d-gandoren_3)

    <span id="d-gandoren_tr_4"></span>**`gandoren_tr_4`** Gandoren: “Absolutely, as thanks for the help you provided earlier to both Minarra and me, we could agree to trade with you.”

    - Next → [gandoren_tr_5](#d-gandoren_tr_5)

    <span id="d-gandoren_tr_6"></span>**`gandoren_tr_6`** Gandoren: “I hear that Minarra up in the lookout tower over there wants help with something. Why don't you go up to her and ask her about it, and we might be able to work something out after that.”


    <span id="d-gandoren_24"></span>**`gandoren_24`** Gandoren: “I would urge you to stay away from her at all costs. Whatever you do, do not speak to her about your mission with the shipment.” — **effects:** sets stage 26 of [Feygard errands](../quests/feygard_shipment.md#stage-26)


    <span id="d-gandoren_delivered_2"></span>**`gandoren_delivered_2`** Gandoren: “From what I hear, things are rough down south.”

    - Next → [gandoren_delivered_3](#d-gandoren_delivered_3)

    <span id="d-cr_loneford_st_3"></span>**`cr_loneford_st_3`** Gandoren: “A few days later, the same symptoms started to show on a lot more people.”

    - Next → [cr_loneford_st_4](#d-cr_loneford_st_4)

    <span id="d-gandoren_8"></span>**`gandoren_8`** Gandoren: “Tell you what, you might be able to help us after all if you are willing to work.”

    - “What is the task?” → [gandoren_11](#d-gandoren_11)
    - “Anything for the glory of Feygard.” → [gandoren_9](#d-gandoren_9)
    - “If the pay is sufficient, I guess I can help.” → [gandoren_10](#d-gandoren_10)
    - “I had better not get involved in your Feygard business.” → [gandoren_rej_1](#d-gandoren_rej_1)

    <span id="d-gandoren_5"></span>**`gandoren_5`** Gandoren: “This also means that we cannot focus as much on our usual tasks as we normally do, but instead need help with doing basic tasks just to hold our grounds.” — **effects:** sets stage 10 of [Feygard errands](../quests/feygard_shipment.md#stage-10)

    - “What troubles in Loneford are you referring to?” → [cr_loneford_st_1](#d-cr_loneford_st_1)
    - “Anything I can do to help?” → [gandoren_6](#d-gandoren_6)

    <span id="d-gandoren_tr_5"></span>**`gandoren_tr_5`** Gandoren: “Go up in the lookout tower over there and talk to Minarra about equipment. She has our supply.” — **effects:** sets stage 18 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-18)


    <span id="d-gandoren_delivered_3"></span>**`gandoren_delivered_3`** Gandoren: “As for you, you have both my and the rest of the Feygard patrol's gratitude for helping us with this.”

    - Next → [gandoren_completed_2](#d-gandoren_completed_2)

    <span id="d-cr_loneford_st_4"></span>**`cr_loneford_st_4`** Gandoren: “Then, all people showed the symptoms in one way or another.”

    - Next → [cr_loneford_st_5](#d-cr_loneford_st_5)

    <span id="d-gandoren_11"></span>**`gandoren_11`** Gandoren: “I need you to take a shipment of equipment to another one of our outposts further south on the Duleian road.”

    - Next → [gandoren_12](#d-gandoren_12)

    <span id="d-gandoren_9"></span>**`gandoren_9`** Gandoren: “I'm glad to hear that.”

    - Next → [gandoren_11](#d-gandoren_11)

    <span id="d-gandoren_10"></span>**`gandoren_10`** Gandoren: “Pay? Oh, I guess we could pay you.”

    - Next → [gandoren_11](#d-gandoren_11)

    <span id="d-gandoren_rej_1"></span>**`gandoren_rej_1`** Gandoren: “I'm sorry to hear that. Good day to you.”


    <span id="d-cr_loneford_st_5"></span>**`cr_loneford_st_5`** Gandoren: “Some old people even died.”

    - Next → [cr_loneford_st_6](#d-cr_loneford_st_6)

    <span id="d-gandoren_12"></span>**`gandoren_12`** Gandoren: “Those outposts further down south are in greater need of equipment than us, them being closer to that wretched Nor City and all.”

    - Next → [gandoren_13](#d-gandoren_13)

    <span id="d-cr_loneford_st_6"></span>**`cr_loneford_st_6`** Gandoren: “Everyone started investigating what could be the cause. Currently, the cause is still unknown.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [cr_loneford_st_7](#d-cr_loneford_st_7)

    <span id="d-gandoren_13"></span>**`gandoren_13`** Gandoren: “Take this shipment of 10 iron swords to the guard captain stationed in a tavern called 'The Foaming Flask', near a village called Vilegard.” — **effects:** sets stage 20 of [Feygard errands](../quests/feygard_shipment.md#stage-20)

    - “No problem. Anything for the glory of Feygard.” → [gandoren_17](#d-gandoren_17)
    - “You did not mention any amount that I would be paid.” → [gandoren_18](#d-gandoren_18)
    - “Why should I help you people? I have only heard bad things about Feygard.” → [gandoren_14](#d-gandoren_14)
    - “I had better not get involved in your Feygard business.” → [gandoren_rej_1](#d-gandoren_rej_1)

    <span id="d-cr_loneford_st_7"></span>**`cr_loneford_st_7`** Gandoren: “Luckily, now Feygard has sent patrols up there to help guard the village at least. The people are still suffering though.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)

    - Next → [cr_loneford_st_8](#d-cr_loneford_st_8)

    <span id="d-gandoren_17"></span>**`gandoren_17`** Gandoren: “Excellent.” — **effects:** sets stage 21 of [Feygard errands](../quests/feygard_shipment.md#stage-21)

    - Next → [gandoren_20](#d-gandoren_20)

    <span id="d-gandoren_18"></span>**`gandoren_18`** Gandoren: “I cannot promise you any amount on a reward.”

    - Next → [gandoren_16](#d-gandoren_16)

    <span id="d-gandoren_14"></span>**`gandoren_14`** Gandoren: “Bad things? Who have you been talking to then? I would urge you to make up your own opinion of Feygard by travelling there yourself.”

    - Next → [gandoren_15](#d-gandoren_15)

    <span id="d-cr_loneford_st_8"></span>**`cr_loneford_st_8`** Gandoren: “Me, I am certain that this is the work of those savages from Nor City somehow. They probably sabotaged something up there.”

    - Next → [cr_loneford_st_9](#d-cr_loneford_st_9)

    <span id="d-gandoren_16"></span>**`gandoren_16`** Gandoren: “As to why you would help us, I can only say that Feygard would be grateful for your services if you help us.”

    - “Fine, whatever. I will carry your stupid swords. I still hope there will be some reward for this.” → [gandoren_19](#d-gandoren_19)
    - “Sounds good to me. Anything for the glory of Feygard.” → [gandoren_17](#d-gandoren_17)
    - “I had better not get involved in your Feygard business.” → [gandoren_rej_1](#d-gandoren_rej_1)

    <span id="d-gandoren_15"></span>**`gandoren_15`** Gandoren: “Personally, I cannot think of a greater place to be than in Feygard. Order is kept and people are friendly.”

    - Next → [gandoren_16](#d-gandoren_16)

    <span id="d-cr_loneford_st_9"></span>**`cr_loneford_st_9`** Gandoren: “What do they call it, the 'Shadow'? They are willing to do almost anything to upset the law and order around here.”

    - Next → [cr_loneford_st_10](#d-cr_loneford_st_10)

    <span id="d-gandoren_19"></span>**`gandoren_19`** Gandoren: “OK then.” — **effects:** sets stage 22 of [Feygard errands](../quests/feygard_shipment.md#stage-22)

    - Next → [gandoren_20](#d-gandoren_20)

    <span id="d-cr_loneford_st_10"></span>**`cr_loneford_st_10`** Gandoren: “I tell you. Savages - that's what they are. No respect for the laws or authority.” — **effects:** sets stage 21 of [Flows through the veins](../quests/loneford.md#stage-21)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “Ok then.” → “OK then.” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gandoren.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gandoren.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gandoren.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gandoren.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `gandoren` · Data from v0.8.18</small>
