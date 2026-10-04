# ![](../assets/icons/monsters/monsters_men_6.png){ .sprite } Wrye

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

- [vilegard_wrye](../maps/vilegard_wrye.md)

## Quests

- [Uncertain cause](../quests/wrye.md): stages 20, 30, 40, 41, 90
- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stages 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Wrye. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/wrye_select_1.json" data-npc="Wrye" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (40 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-wrye_select_1"></span>**`wrye_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Uncertain cause](../quests/wrye.md#stage-90))* → [wrye_return_2](#d-wrye_return_2)
    - branch 2 *(if reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40))* → [wrye_return_1](#d-wrye_return_1)
    - branch 3 → [wrye_mourn_1](#d-wrye_mourn_1)

    <span id="d-wrye_return_2"></span>**`wrye_return_2`** Wrye: “Welcome back. Thank you for your help in finding out what happened to my son.”

    - “Shadow be with you.” → [wrye_story_15](#d-wrye_story_15)
    - “You are welcome.” → [wrye_story_15](#d-wrye_story_15)
    - “Yes, I came back to deliver your order of a 'Lyre'. You must be good at playing it?” *(if hand over 1× [Lyre](../items/brv_wh_item_02.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90))* → [brv_wh_delivery_wyre](#d-brv_wh_delivery_wyre)

    <span id="d-wrye_return_1"></span>**`wrye_return_1`** Wrye: “Welcome back. Have you found out anything about my son, Rincel?”

    - “Can you tell me the story about what happened again?” → [wrye_mourn_5](#d-wrye_mourn_5)
    - “No, I have not found anything yet.” → [wrye_story_14](#d-wrye_story_14)
    - “Yes, I have found out the story about what happened to him.” *(if reached stage 80 of [Uncertain cause](../quests/wrye.md#stage-80))* → [wrye_resolved_1](#d-wrye_resolved_1)
    - “Not yet, but your order has finally arrived.” *(if carry 1× [Lyre](../items/brv_wh_item_02.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90))* → [brv_wh_delivery_wyre_negative](#d-brv_wh_delivery_wyre_negative)

    <span id="d-wrye_mourn_1"></span>**`wrye_mourn_1`** Wrye: “Shadow help me.”

    - “What is the matter?” → [wrye_mourn_2](#d-wrye_mourn_2)
    - “Excuse me, I'm here to deliver your order for a 'Lyre'.” *(if carry 1× [Lyre](../items/brv_wh_item_02.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90))* → [wrye_mourn_3](#d-wrye_mourn_3)

    <span id="d-wrye_story_15"></span>**`wrye_story_15`** Wrye: “Walk with the Shadow.”


    <span id="d-brv_wh_delivery_wyre"></span>**`brv_wh_delivery_wyre`** Wrye: “Yes, I'm longing for it just like how I'm longing for my son. But now I can mourn as I play his favorite song until I die.” — **effects:** clears stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90), sets stage 80 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-80)

    - “My sincere condolence for the loss of your beloved son.” → *conversation ends*

    <span id="d-wrye_mourn_5"></span>**`wrye_mourn_5`** Wrye: “My son is dead, I know it! And it's those damn guards fault. Those guards with their snobby Feygard attitude.”

    - Next → [wrye_mourn_6](#d-wrye_mourn_6)

    <span id="d-wrye_story_14"></span>**`wrye_story_14`** Wrye: “Please return here as soon as you have found out anything.”

    - Next → [wrye_story_15](#d-wrye_story_15)

    <span id="d-wrye_resolved_1"></span>**`wrye_resolved_1`** Wrye: “Please tell me what happened to him!”

    - “He left Vilegard by his own will because he wanted to see the great city of Feygard.” → [wrye_resolved_2](#d-wrye_resolved_2)

    <span id="d-brv_wh_delivery_wyre_negative"></span>**`brv_wh_delivery_wyre_negative`** Wrye: “That's not what I'm waiting for! Go out and find out what happened to my son, please!”


    <span id="d-wrye_mourn_2"></span>**`wrye_mourn_2`** Wrye: “My son! My son is gone.”

    - “Jolnor said I should see you about your son.” *(if reached stage 10 of [Uncertain cause](../quests/wrye.md#stage-10))* → [wrye_mourn_5](#d-wrye_mourn_5)
    - “What about him?” → [wrye_mourn_3](#d-wrye_mourn_3)
    - “Maybe your order here will comfort you?” *(if carry 1× [Lyre](../items/brv_wh_item_02.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90))* → [wrye_mourn_3](#d-wrye_mourn_3)

    <span id="d-wrye_mourn_3"></span>**`wrye_mourn_3`** Wrye: “I don't want to talk about it. Not with an outsider like you.”

    - “Outsider?” → [wrye_mourn_4](#d-wrye_mourn_4)
    - “Jolnor said I should see you about your son.” *(if reached stage 10 of [Uncertain cause](../quests/wrye.md#stage-10))* → [wrye_mourn_5](#d-wrye_mourn_5)

    <span id="d-wrye_mourn_6"></span>**`wrye_mourn_6`** Wrye: “At first they come with promises of protection and power. But then you really start to see them for what they are.”

    - Next → [wrye_mourn_7](#d-wrye_mourn_7)

    <span id="d-wrye_resolved_2"></span>**`wrye_resolved_2`** Wrye: “I don't believe it.”

    - “He had secretly longed to go to Feygard, but didn't dare tell you.” → [wrye_resolved_3](#d-wrye_resolved_3)

    <span id="d-wrye_mourn_4"></span>**`wrye_mourn_4`** Wrye: “Please leave me. Oh Shadow, watch over me.”


    <span id="d-wrye_mourn_7"></span>**`wrye_mourn_7`** Wrye: “I can feel it in me. The Shadow speaks to me. He is dead.” — **effects:** sets stage 20 of [Uncertain cause](../quests/wrye.md#stage-20)

    - “Can you tell me what happened?” → [wrye_story_1](#d-wrye_story_1)
    - “What are you talking about?” → [wrye_story_1](#d-wrye_story_1)
    - “Shadow be with you.” → [wrye_mourn_8](#d-wrye_mourn_8)

    <span id="d-wrye_resolved_3"></span>**`wrye_resolved_3`** Wrye: “Really?”

    - “But he never got far. He was attacked while camping one night.” → [wrye_resolved_4](#d-wrye_resolved_4)

    <span id="d-wrye_story_1"></span>**`wrye_story_1`** Wrye: “It all started with those Feygard royal guards coming here.”

    - Next → [wrye_story_2](#d-wrye_story_2)

    <span id="d-wrye_mourn_8"></span>**`wrye_mourn_8`** Wrye: “Thank you. Shadow watch over me.”

    - Next → [wrye_story_1](#d-wrye_story_1)

    <span id="d-wrye_resolved_4"></span>**`wrye_resolved_4`** Wrye: “Attacked?”

    - “Yes, he could not stand up to the monsters, and was critically wounded.” → [wrye_resolved_5](#d-wrye_resolved_5)

    <span id="d-wrye_story_2"></span>**`wrye_story_2`** Wrye: “They tried to pressure everyone in Vilegard into recruiting more soldiers.”

    - Next → [wrye_story_3](#d-wrye_story_3)

    <span id="d-wrye_resolved_5"></span>**`wrye_resolved_5`** Wrye: “My dear boy.”

    - “I talked to a man that found him bleeding to death.” → [wrye_resolved_6](#d-wrye_resolved_6)

    <span id="d-wrye_story_3"></span>**`wrye_story_3`** Wrye: “The guards would say they needed more support to help squelch the supposed uprising and sabotage.”

    - “How did this relate to your son?” → [wrye_story_4](#d-wrye_story_4)
    - “Are you going to get to the point soon?” → [wrye_story_4](#d-wrye_story_4)

    <span id="d-wrye_resolved_6"></span>**`wrye_resolved_6`** Wrye: “He was still alive?”

    - “Yes, but not for long. He did not survive the wounds. He is now buried to the northwest of Vilegard.” → [wrye_resolved_7](#d-wrye_resolved_7)

    <span id="d-wrye_story_4"></span>**`wrye_story_4`** Wrye: “My son, Rincel, did not seem to care much for the stories they told.”

    - Next → [wrye_story_5](#d-wrye_story_5)

    <span id="d-wrye_resolved_7"></span>**`wrye_resolved_7`** Wrye: “Oh my poor boy. What have I done?” — **effects:** sets stage 90 of [Uncertain cause](../quests/wrye.md#stage-90)

    - Next → [wrye_resolved_8](#d-wrye_resolved_8)

    <span id="d-wrye_story_5"></span>**`wrye_story_5`** Wrye: “I also told Rincel of how bad an idea I thought it was to recruit more people to the Royal Guard.”

    - Next → [wrye_story_6](#d-wrye_story_6)

    <span id="d-wrye_resolved_8"></span>**`wrye_resolved_8`** Wrye: “I always thought he shared my view of those Feygard snobs.”

    - Next → [wrye_resolved_9](#d-wrye_resolved_9)

    <span id="d-wrye_story_6"></span>**`wrye_story_6`** Wrye: “The guards stayed a couple of days to talk to everyone here in Vilegard. Then they left. They went to the next town I guess.”

    - Next → [wrye_story_7](#d-wrye_story_7)

    <span id="d-wrye_resolved_9"></span>**`wrye_resolved_9`** Wrye: “And now he is not with us anymore.”

    - Next → [wrye_resolved_10](#d-wrye_resolved_10)

    <span id="d-wrye_story_7"></span>**`wrye_story_7`** Wrye: “A few days passed, and then suddenly my boy Rincel was gone one day. I am sure those guards managed to somehow persuade him to join them.”

    - Next → [wrye_story_8](#d-wrye_story_8)

    <span id="d-wrye_resolved_10"></span>**`wrye_resolved_10`** Wrye: “Thank you, friend, for finding out what happened to him and telling me the truth.”

    - Next → [wrye_resolved_11](#d-wrye_resolved_11)

    <span id="d-wrye_story_8"></span>**`wrye_story_8`** Wrye: “Oh how I despise those evil and snobby Feygard bastards.”

    - “What now?” → [wrye_story_9](#d-wrye_story_9)

    <span id="d-wrye_resolved_11"></span>**`wrye_resolved_11`** Wrye: “Oh my poor boy.”

    - Next → [wrye_mourn_4](#d-wrye_mourn_4)

    <span id="d-wrye_story_9"></span>**`wrye_story_9`** Wrye: “This was several weeks ago. Now I feel an emptiness inside. I know in me that something has happened to my son Rincel.”

    - Next → [wrye_story_10](#d-wrye_story_10)

    <span id="d-wrye_story_10"></span>**`wrye_story_10`** Wrye: “I fear he has died or got hurt somehow. Those bastards probably drove him into his own death.” — **effects:** sets stage 30 of [Uncertain cause](../quests/wrye.md#stage-30)

    - Next → [wrye_story_11](#d-wrye_story_11)

    <span id="d-wrye_story_11"></span>**`wrye_story_11`** Wrye: “*sob* Shadow help me.”

    - “What can I do to help?” → [wrye_story_13](#d-wrye_story_13)
    - “That sounds awful. I am sure you are just imagining things.” → [wrye_story_13](#d-wrye_story_13)
    - “Do you have proof that the people from Feygard are involved?” → [wrye_story_12](#d-wrye_story_12)

    <span id="d-wrye_story_13"></span>**`wrye_story_13`** Wrye: “If you want to help me, please find out what happened to my son, Rincel.” — **effects:** sets stage 40 of [Uncertain cause](../quests/wrye.md#stage-40)

    - “Any idea where I should look?” → [wrye_story_16](#d-wrye_story_16)
    - “OK. I will go look for your son. I sure hope there will be some reward for this.” → [wrye_story_14](#d-wrye_story_14)
    - “By the Shadow, your son will be avenged.” → [wrye_story_14](#d-wrye_story_14)

    <span id="d-wrye_story_12"></span>**`wrye_story_12`** Wrye: “No, but I know it in me that they are. The Shadow speaks to me.”

    - “OK. Is there anything I can do to help?” → [wrye_story_13](#d-wrye_story_13)
    - “You sound a bit too occupied with the Shadow. I want no part of this.” → [wrye_mourn_4](#d-wrye_mourn_4)
    - “I probably shouldn't get involved in this if it means that I could upset the royal guard.” → [wrye_mourn_4](#d-wrye_mourn_4)

    <span id="d-wrye_story_16"></span>**`wrye_story_16`** Wrye: “I guess you could ask in the tavern here in Vilegard, or the Foaming Flask tavern just north of here.” — **effects:** sets stage 41 of [Uncertain cause](../quests/wrye.md#stage-41)

    - “By the Shadow, your son will be avenged.” → [wrye_story_14](#d-wrye_story_14)
    - “OK. I will go look for your son. I sure hope there will be some reward for this.” → [wrye_story_14](#d-wrye_story_14)
    - “OK. I will go look for your son so that you may know what happened to him.” → [wrye_story_14](#d-wrye_story_14)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 2 lines added, 4 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wrye.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wrye.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wrye.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wrye.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `wrye` · Data from v0.8.18</small>
