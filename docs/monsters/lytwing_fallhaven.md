---
description: "Lytwing is a non-player character (NPC) in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_203.png){ .sprite } Lytwing

**Where to find Lytwing:** Fallhaven: [gapfiller2](../maps/gapfiller2.md#pin-npc-lytwing_fallhaven)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_203.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Fallhaven |
| **Entry ID** | `lytwing_fallhaven` |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Quests

- [It's knot funny](../quests/fallhaven_lytwings.md): stages 11, 12, 13, 20, 30, 31, 40, 41, 90, 92, 99

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Lytwing. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lytwing_fallhaven_select.json" data-npc="Lytwing" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (38 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lytwing_fallhaven_select"></span>**`lytwing_fallhaven_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-10) is 10)* → [lytwing_fallhaven_1](#d-lytwing_fallhaven_1)
    - branch 2 *(if NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12))* → [lytwing_fallhaven_3](#d-lytwing_fallhaven_3)
    - branch 3 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12) is 12)* → [lytwing_fallhaven_6](#d-lytwing_fallhaven_6)
    - branch 4 *(if NOT 2 rounds passed since timer “lytwing_fallhaven_timer”)* → [lytwing_fallhaven_10](#d-lytwing_fallhaven_10)
    - branch 5 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-13) is 13)* → [lytwing_fallhaven_11](#d-lytwing_fallhaven_11)
    - branch 6 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20) is 20)* → [lytwing_fallhaven_14](#d-lytwing_fallhaven_14)
    - branch 7 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-21) is 21)* → [lytwing_fallhaven_17](#d-lytwing_fallhaven_17)
    - branch 8 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30) is 30)* → [lytwing_fallhaven_18](#d-lytwing_fallhaven_18)
    - branch 9 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-31) is 31)* → [lytwing_fallhaven_22](#d-lytwing_fallhaven_22)
    - branch 10 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40)* → [lytwing_fallhaven_23](#d-lytwing_fallhaven_23)
    - branch 11 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-41) is 41)* → [lytwing_fallhaven_26](#d-lytwing_fallhaven_26)
    - branch 12 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90)* → [lytwing_fallhaven_31](#d-lytwing_fallhaven_31)
    - branch 13 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-91) is 91)* → [lytwing_fallhaven_31](#d-lytwing_fallhaven_31)
    - branch 14 *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-92) is 92)* → [lytwing_fallhaven_35](#d-lytwing_fallhaven_35)
    - branch 15 → [lytwing_fallhaven_38](#d-lytwing_fallhaven_38)

    <span id="d-lytwing_fallhaven_1"></span>**`lytwing_fallhaven_1`** Lytwing: “Hello there, stranger!”

    - “Oh, hi. My name is $playername. Who are you?” → [lytwing_fallhaven_2](#d-lytwing_fallhaven_2)

    <span id="d-lytwing_fallhaven_3"></span>**`lytwing_fallhaven_3`** Lytwing: “Did you bring us a gift?”

    - “Yes, here are two red apples and two strawberries.” *(if hand over 2× [Red apple](../items/apple_red.md); hand over 2× [Strawberry](../items/strawberry.md))* → [lytwing_fallhaven_5](#d-lytwing_fallhaven_5)
    - “I did not, sorry.” → [lytwing_fallhaven_4](#d-lytwing_fallhaven_4)

    <span id="d-lytwing_fallhaven_6"></span>**`lytwing_fallhaven_6`** Lytwing: “Hi $playername! Want to play with us?”

    - “I'm here on behalf of Arensia. She is very upset.” → [lytwing_fallhaven_7](#d-lytwing_fallhaven_7)

    <span id="d-lytwing_fallhaven_10"></span>**`lytwing_fallhaven_10`** Lytwing: “We are busy discussing the matter. Please wait a little bit longer.”


    <span id="d-lytwing_fallhaven_11"></span>**`lytwing_fallhaven_11`** Lytwing: “We have decided to entertain your request.”

    - “Thank you, Arensia will be happy to hear that!” → [lytwing_fallhaven_12](#d-lytwing_fallhaven_12)

    <span id="d-lytwing_fallhaven_14"></span>**`lytwing_fallhaven_14`** Lytwing: “Please chop down this gnarly old tree inside our fairy circle. Can you do that for us?” — **effects:** sets stage 20 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20)

    - “No, I am not willing to do that.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “OK, I will chop it down.” → [lytwing_fallhaven_39](#d-lytwing_fallhaven_39)

    <span id="d-lytwing_fallhaven_17"></span>**`lytwing_fallhaven_17`** Lytwing: “We are having a celebration, please get us four bottles of mead. [giggle]” — **effects:** sets stage 30 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30)

    - “I don't think so. Your demands are getting ridiculous.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Okay, fine. I will get you the mead. But you better not change your mind again.” → *conversation ends*

    <span id="d-lytwing_fallhaven_18"></span>**`lytwing_fallhaven_18`** Lytwing: “Do you have our mead?”

    - “No, sorry.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Yes, here is your mead.” *(if hand over 4× [Mead](../items/mead.md))* → [lytwing_fallhaven_19](#d-lytwing_fallhaven_19)

    <span id="d-lytwing_fallhaven_22"></span>**`lytwing_fallhaven_22`** Lytwing: “For our celebrations, we would like a dozen wild flowers.” — **effects:** sets stage 40 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40)

    - “This is getting silly. I don't want to collect flowers for you.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Okay fine. But this better be the last thing.” → *conversation ends*

    <span id="d-lytwing_fallhaven_23"></span>**`lytwing_fallhaven_23`** Lytwing: “Do you have our wild flowers?”

    - “No I don't.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Yes, here are your flowers.” *(if hand over 12× [Wild Flower](../items/wild_flower.md))* → [lytwing_fallhaven_24](#d-lytwing_fallhaven_24)
    - “Yes, here are your flowers.” *(if carry 1× [Wild Flower](../items/wild_flower.md); NOT carry 12× [Wild Flower](../items/wild_flower.md))* → [lytwing_fallhaven_23a](#d-lytwing_fallhaven_23a)

    <span id="d-lytwing_fallhaven_26"></span>**`lytwing_fallhaven_26`** Lytwing: “Okay so after carefully considering your request ...”

    - “Yes?” → [lytwing_fallhaven_27](#d-lytwing_fallhaven_27)

    <span id="d-lytwing_fallhaven_31"></span>**`lytwing_fallhaven_31`** Lytwing: “Did you bring us Arensia's promise?”

    - “No, I have not.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Yes, here is her promise ring.” *(if hand over 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md))* → [lytwing_fallhaven_32](#d-lytwing_fallhaven_32)

    <span id="d-lytwing_fallhaven_35"></span>**`lytwing_fallhaven_35`** Lytwing: “We have discussed this matter and made a final decision ...”

    - “OK, I hope this turns out well.” → [lytwing_fallhaven_36](#d-lytwing_fallhaven_36)

    <span id="d-lytwing_fallhaven_38"></span>**`lytwing_fallhaven_38`** Lytwing: “Hello $playername. We hope you are staying out of trouble.”


    <span id="d-lytwing_fallhaven_2"></span>**`lytwing_fallhaven_2`** Lytwing: “Well met, $playername. I won't tell you my name, it is forbidden for otherkinds to know our names.”

    - Next → [lytwing_fallhaven_3](#d-lytwing_fallhaven_3)

    <span id="d-lytwing_fallhaven_5"></span>**`lytwing_fallhaven_5`** Lytwing: “Wonderful! These strawberries are so sweet. You may stay!” — **effects:** sets stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12)


    <span id="d-lytwing_fallhaven_4"></span>**`lytwing_fallhaven_4`** Lytwing: “Bring us two red apples and two strawberries. Since you came without a gift, we cast on you a mystical Lytwing spell!” — **effects:** sets stage 11 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-11), applies condition fatigue_minor

    - “I feel so ... tired.” → *conversation ends*

    <span id="d-lytwing_fallhaven_7"></span>**`lytwing_fallhaven_7`** Lytwing: “She should be sorry! She stole our mushrooms.”

    - “I'm sure she did not mean to steal them. She was probably just gathering mushrooms for a stew.” → [lytwing_fallhaven_8](#d-lytwing_fallhaven_8)

    <span id="d-lytwing_fallhaven_12"></span>**`lytwing_fallhaven_12`** Lytwing: “But you have to do something for us first [giggle].”

    - “Oh please just let Arensia be, she meant no ill will.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Please just forgive her mistake. There is no need to prolong her suffering.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Yes of course. What do you need?” → [lytwing_fallhaven_14](#d-lytwing_fallhaven_14)

    <span id="d-lytwing_fallhaven_13"></span>**`lytwing_fallhaven_13`** Lytwing: “Suit yourself. If you won't help us, we won't help Arensia. Goodbye!” — **effects:** applies condition fatigue_minor


    <span id="d-lytwing_fallhaven_39"></span>**`lytwing_fallhaven_39`** Lytwing: “It is important that you use an iron axe. That tree is cursed, and only an iron axe will work.”

    - “OK, I understand.” → *conversation ends*

    <span id="d-lytwing_fallhaven_19"></span>**`lytwing_fallhaven_19`** Lytwing: “Wonderful!” — **effects:** sets stage 31 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-31)

    - “Will you leave Arensia alone now?” → [lytwing_fallhaven_20](#d-lytwing_fallhaven_20)

    <span id="d-lytwing_fallhaven_24"></span>**`lytwing_fallhaven_24`** Lytwing: “These are perfect. Thank you!” — **effects:** sets stage 41 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-41)

    - “Is that everything? Will you leave Arensia be?” → [lytwing_fallhaven_20](#d-lytwing_fallhaven_20)

    <span id="d-lytwing_fallhaven_23a"></span>**`lytwing_fallhaven_23a`** Lytwing: “No, you don't have enough flowers. A dozen means 12, not one less. Do you think lytwings can't count?”

    - “I have collected enough for you. Take it or leave it.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Sorry, I'm going to look for the missing wild flowers now.” → *conversation ends*

    <span id="d-lytwing_fallhaven_27"></span>**`lytwing_fallhaven_27`** Lytwing: “We have decided what would make this right ...”

    - “OK?” → [lytwing_fallhaven_28](#d-lytwing_fallhaven_28)

    <span id="d-lytwing_fallhaven_32"></span>**`lytwing_fallhaven_32`** Lytwing: “This will do just fine, thank you $playername.” — **effects:** sets stage 92 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-92)

    - “I hope this settles the matter?” → [lytwing_fallhaven_33](#d-lytwing_fallhaven_33)

    <span id="d-lytwing_fallhaven_36"></span>**`lytwing_fallhaven_36`** Lytwing: “Please tell Arensia that we have accepted her promise. We will no longer taunt her at night.”

    - “Oh how wonderful. Thank you forest lytwings!” → [lytwing_fallhaven_37](#d-lytwing_fallhaven_37)

    <span id="d-lytwing_fallhaven_8"></span>**`lytwing_fallhaven_8`** Lytwing: “A STEW? That is unacceptable. She must be punished.”

    - “Don't be mad, I am just trying to help. Is there anything I can do to make this right?” → [lytwing_fallhaven_9](#d-lytwing_fallhaven_9)

    <span id="d-lytwing_fallhaven_20"></span>**`lytwing_fallhaven_20`** Lytwing: “Yes, of course we will.”

    - “Arensia wil be very happy to hear this.” → [lytwing_fallhaven_21](#d-lytwing_fallhaven_21)

    <span id="d-lytwing_fallhaven_28"></span>**`lytwing_fallhaven_28`** Lytwing: “We want Arensia to promise not to pick our mushrooms again. And we want proof!” — **effects:** sets stage 90 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90)

    - “I can ask her, but how can I provide proof?” → [lytwing_fallhaven_29](#d-lytwing_fallhaven_29)

    <span id="d-lytwing_fallhaven_33"></span>**`lytwing_fallhaven_33`** Lytwing: “Well, I think you know what I will say next ...”

    - “Oh no, not again!” → [lytwing_fallhaven_21](#d-lytwing_fallhaven_21)

    <span id="d-lytwing_fallhaven_37"></span>**`lytwing_fallhaven_37`** Lytwing: “However, we have no need for a human ring. We embued it with our magical powers. Please take this ring back to Arensia.” — **effects:** gives 1× [Arensia's Ring of Promise](../items/ring_of_promise.md), sets stage 99 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-99)

    - “I will give Arensia her ring back. She will appreciate this gesture very much.” → *conversation ends*

    <span id="d-lytwing_fallhaven_9"></span>**`lytwing_fallhaven_9`** Lytwing: “Hmmm, let us discuss this amongst ourselves. Can you give us a minute alone?” — **effects:** sets stage 13 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-13), starts timer “lytwing_fallhaven_timer”

    - “OK, I will wait nearby.” → *conversation ends*

    <span id="d-lytwing_fallhaven_21"></span>**`lytwing_fallhaven_21`** Lytwing: “We just need you to do one more thing for us ...”

    - “More? No I don't think so. This is absurd.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “What do you want now?” → [lytwing_fallhaven_25](#d-lytwing_fallhaven_25)

    <span id="d-lytwing_fallhaven_29"></span>**`lytwing_fallhaven_29`** Lytwing: “She must give a piece of jewelry as proof of her promise. Her word would be bound to it.”

    - “This sounds very silly.” → [lytwing_fallhaven_13](#d-lytwing_fallhaven_13)
    - “Very well. I will go talk to Arensia.” → [lytwing_fallhaven_30](#d-lytwing_fallhaven_30)

    <span id="d-lytwing_fallhaven_25"></span>**`lytwing_fallhaven_25`** Lytwing: “Give us a minute to think about it.” — **effects:** starts timer “lytwing_fallhaven_timer”


    <span id="d-lytwing_fallhaven_30"></span>**`lytwing_fallhaven_30`** Lytwing: “Good. And remember, she has to make her promise to the jewelry.”




## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 38 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lytwing_fallhaven` |
    | Spawn group | `lytwing_fallhaven` |
    | Loot table | – |
    | Conversation | `lytwing_fallhaven_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:203` |
    | Defined in | `res/raw/monsterlist_lytwings.json` |

    Raw data:

    ```json
    {
     "id": "lytwing_fallhaven",
     "name": "Lytwing",
     "iconID": "monsters_ld1:203",
     "moveCost": 2,
     "monsterClass": "humanoid",
     "spawnGroup": "lytwing_fallhaven",
     "phraseID": "lytwing_fallhaven_select"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lytwing_fallhaven.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lytwing_fallhaven.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lytwing_fallhaven.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lytwing_fallhaven.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
