# ![](../assets/icons/monsters/monsters_ld1_145.png){ .sprite } Arensia

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

- [fallhaven_sw](../maps/fallhaven_sw.md)

## Quests

- [It's knot funny](../quests/fallhaven_lytwings.md): stages 1, 91, 100, 101, 102, 103
- [You're the postman](../quests/postman.md): stages 20

??? quote "Dialogue (45 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-arensia"></span>**`arensia`** Arensia: “Hello, dear.”

    - “I have a letter for you.” *(if carry 1× [Gorwath's letter](../items/gorwath_letter.md))* → [arensia_letter](#d-arensia_letter)
    - “Hello. I am wondering if you could help me?” *(if latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-10) is 10)* → [arensia_witch_10](#d-arensia_witch_10)
    - “You seem tired. Is everything alright?” *(if NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1))* → [arensia_lytwing_select](#d-arensia_lytwing_select)
    - “About the lytwings ...” *(if reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); NOT reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102); NOT reached stage 103 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-103))* → [arensia_lytwing_select](#d-arensia_lytwing_select)
    - “Have the lytwings honored their word?” *(if reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); wearing [Arensia's Ring of Promise](../items/ring_of_promise.md))* → [arensia_lytwing_34](#d-arensia_lytwing_34)
    - “Hello.” → [arensia_done](#d-arensia_done)

    <span id="d-arensia_letter"></span>**`arensia_letter`** Arensia: “A letter? From whom?”

    - “It is from Gorwath, of Crossgl...” → [arensia_letter_10](#d-arensia_letter_10)

    <span id="d-arensia_witch_10"></span>**`arensia_witch_10`** Arensia: “Of course, my dear.”

    - “Did you see a witch around here or hear about a witch kidnapping a girl?” → [no_witch_info](#d-no_witch_info)

    <span id="d-arensia_lytwing_select"></span>**`arensia_lytwing_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1))* → [arensia_lytwing_1](#d-arensia_lytwing_1)
    - branch 2 *(if reached stage 101 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-101))* → [arensia_lytwing_22](#d-arensia_lytwing_22)
    - branch 3 *(if NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12))* → [arensia_lytwing_5](#d-arensia_lytwing_5)
    - branch 4 *(if NOT reached stage 99 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-99))* → [arensia_lytwing_6](#d-arensia_lytwing_6)
    - branch 5 *(if reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); NOT reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102))* → [arensia_lytwing_24](#d-arensia_lytwing_24)
    - branch 6 *(if reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); NOT reached stage 103 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-103))* → [arensia_lytwing_24](#d-arensia_lytwing_24)
    - branch 7 → [arensia_lytwing_23](#d-arensia_lytwing_23)

    <span id="d-arensia_lytwing_34"></span>**`arensia_lytwing_34`** Arensia: “They have, I no longer wake up with fairy-locks.”

    - “I am happy to hear that.” *(if reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102))* → [arensia_lytwing_35](#d-arensia_lytwing_35)
    - “I am happy to hear that.” *(if reached stage 103 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-103))* → [arensia_lytwing_36](#d-arensia_lytwing_36)

    <span id="d-arensia_done"></span>**`arensia_done`** Arensia: “What a beautiful day, isn't it?”


    <span id="d-arensia_letter_10"></span>**`arensia_letter_10`** Arensia: “Oh really? Give it to me - quickly!”

    - “Here it is.” *(if hand over 1× [Gorwath's letter](../items/gorwath_letter.md))* → [arensia_letter_20](#d-arensia_letter_20)

    <span id="d-no_witch_info"></span>**`no_witch_info`** Arensia: “No, I'm sorry, I didn't.”

    - “Oh, thanks anyway.” → *conversation ends*

    <span id="d-arensia_lytwing_1"></span>**`arensia_lytwing_1`** Arensia: “My sleep has been very restless lately.”

    - “Oh no, why are you not sleeping well?” → [arensia_lytwing_2](#d-arensia_lytwing_2)

    <span id="d-arensia_lytwing_22"></span>**`arensia_lytwing_22`** Arensia: “There is nothing else to be done, and I will have to live with the lytwings tormenting me until my last day.”


    <span id="d-arensia_lytwing_5"></span>**`arensia_lytwing_5`** Arensia: “Have you found them yet?”

    - “Not yet. I still need to go talk with Rigmor to find out more.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1)* → [arensia_lytwing_33](#d-arensia_lytwing_33)
    - “Not yet. I am still looking for their mushroom patch. You wouldn't know where it is, perhaps?” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-10) is 10)* → [arensia_lytwing_27](#d-arensia_lytwing_27)
    - “I did, they asked that I bring them a gift of apples and strawberries.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-11) is 11)* → [arensia_lytwing_11](#d-arensia_lytwing_11)

    <span id="d-arensia_lytwing_6"></span>**`arensia_lytwing_6`** Arensia: “Please tell me you have good news?”

    - “They accepted the gift and will allow me to talk to them.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12) is 12)* → [arensia_lytwing_8](#d-arensia_lytwing_8)
    - “The lytwings are upset that you took their mushrooms. I pleaded with them, and am now waiting on their decision.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-13) is 13)* → [arensia_lytwing_10](#d-arensia_lytwing_10)
    - “I have, and they agreed to stop pestering you if I help cut down a tree for them.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20) is 20)* → [arensia_lytwing_7](#d-arensia_lytwing_7)
    - “The lytwings changed their minds, and are now thinking of something else they want instead.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-21) is 21)* → [arensia_lytwing_13](#d-arensia_lytwing_13)
    - “They now want four bottles of mead. They sure are giving me the run around today!” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30) is 30)* → [arensia_lytwing_14](#d-arensia_lytwing_14)
    - “They took the mead, but said they need something else.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-31) is 31)* → [arensia_lytwing_28](#d-arensia_lytwing_28)
    - “They want a dozen wild flowers.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40)* → [arensia_lytwing_30](#d-arensia_lytwing_30)
    - “They took the wild flowers ...” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-41) is 41)* → [arensia_lytwing_18](#d-arensia_lytwing_18)
    - “The lytwings ask that you make a promise to never pick mushrooms from their fairy ring again.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90)* → [arensia_lytwing_19](#d-arensia_lytwing_19)
    - “I will take your ring to them at once!” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-91) is 91)* → [arensia_lytwing_32](#d-arensia_lytwing_32)
    - “I gave them your ring, they are busy discussing it now.” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-92) is 92)* → [arensia_lytwing_32](#d-arensia_lytwing_32)

    <span id="d-arensia_lytwing_24"></span>**`arensia_lytwing_24`** Arensia: “I cannot thank you enough, $playername. You have saved my sanity!” — **effects:** sets stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100)

    - “Unfortunately they kept your mother's ring (Lie).” → [arensia_lytwing_25](#d-arensia_lytwing_25)
    - “They used their magic on your ring, and asked that I give it back to you.” → [arensia_lytwing_26](#d-arensia_lytwing_26)

    <span id="d-arensia_lytwing_23"></span>**`arensia_lytwing_23`** Arensia: “So ... what did they say?”

    - “The lytwings finally agreed to leave you in peace.” → [arensia_lytwing_24](#d-arensia_lytwing_24)

    <span id="d-arensia_lytwing_35"></span>**`arensia_lytwing_35`** Arensia: “But I see you have the ring I gave them. You told me they kept it, which can only mean that you lied to me. You are just a common thief. Shame on you.”

    - “But, I ... um ....” → *conversation ends*

    <span id="d-arensia_lytwing_36"></span>**`arensia_lytwing_36`** Arensia: “I see you have my magical ring. I hope it serves you well, you deserve it.”

    - “I keep it safe, and it keeps me safe in return.” → *conversation ends*

    <span id="d-arensia_letter_20"></span>**`arensia_letter_20`** Arensia: “[Reading] Oh that's cute. Tell Gorwath I love him too.” — **effects:** sets stage 20 of [You're the postman](../quests/postman.md#stage-20)

    - “I'll be happy to tell him that.” → *conversation ends*

    <span id="d-arensia_lytwing_2"></span>**`arensia_lytwing_2`** Arensia: “I am being taunted by naughty lytwings at night. At least that is what Rigmor tells me. They play with my hair while I sleep, and tangle it into fairy-lock knots. Every morning I wake up tired, and I spend an hour brushing out the knots.…”

    - “I am sorry to hear that, but I cannot help you right now.” → [arensia_lytwing_3](#d-arensia_lytwing_3)
    - “That sounds awful, can I help in any way?” → [arensia_lytwing_4](#d-arensia_lytwing_4)

    <span id="d-arensia_lytwing_33"></span>**`arensia_lytwing_33`** Arensia: “You should talk to Rigmor, as she knows more about the lytwings than I do. She lives here in Fallhaven, just go north past the tavern.” — **effects:** sets stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1)

    - “Okay.” → *conversation ends*

    <span id="d-arensia_lytwing_27"></span>**`arensia_lytwing_27`** Arensia: “I can't say that I have noticed it. A few days ago I was picking mushrooms to the west of here.”


    <span id="d-arensia_lytwing_11"></span>**`arensia_lytwing_11`** Arensia: “Oh wonderful! An odd request nonetheless.”

    - “I better go and find those fruit.” → *conversation ends*
    - “Where can I find apples and strawberries?” → [arensia_lytwing_12](#d-arensia_lytwing_12)

    <span id="d-arensia_lytwing_8"></span>**`arensia_lytwing_8`** Arensia: “Please keep me updated.”

    - “I will.” → *conversation ends*

    <span id="d-arensia_lytwing_10"></span>**`arensia_lytwing_10`** Arensia: “Okay thanks for letting me know. Don't let them wait too long.”

    - Next → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_7"></span>**`arensia_lytwing_7`** Arensia: “Oh that is great news! If you need an axe, check with Jakrar, my father, over there.”

    - Next → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_13"></span>**`arensia_lytwing_13`** Arensia: “Oh no, they sound very difficult to deal with. I hope it gets better.”

    - “Thank you.” → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_14"></span>**`arensia_lytwing_14`** Arensia: “I am so sorry.”

    - Next → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_28"></span>**`arensia_lytwing_28`** Arensia: “They sure are a greedy bunch!”

    - Next → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_30"></span>**`arensia_lytwing_30`** Arensia: “How can I help?”

    - “Where can I find wild flowers?” *(if NOT carry 1× [Wild Flower](../items/wild_flower.md))* → [arensia_lytwing_31](#d-arensia_lytwing_31)
    - “I found some wild flowers, I just need a few more.” *(if carry 1× [Wild Flower](../items/wild_flower.md); NOT carry 12× [Wild Flower](../items/wild_flower.md))* → [arensia_lytwing_37](#d-arensia_lytwing_37)
    - “I have found a dozen wild flowers. I will take them to the lytwings.” *(if carry 12× [Wild Flower](../items/wild_flower.md))* → [arensia_lytwing_37](#d-arensia_lytwing_37)
    - “Will this ever end?” → [arensia_lytwing_15](#d-arensia_lytwing_15)

    <span id="d-arensia_lytwing_18"></span>**`arensia_lytwing_18`** Arensia: “Oh please tell me that is the end of it?”

    - “I'm afraid not, they still want more.” → [arensia_lytwing_15](#d-arensia_lytwing_15)

    <span id="d-arensia_lytwing_19"></span>**`arensia_lytwing_19`** Arensia: “Of course! anything!”

    - “You have to make this promise to a piece of jewellery, which I will take back to them.” → [arensia_lytwing_20](#d-arensia_lytwing_20)

    <span id="d-arensia_lytwing_32"></span>**`arensia_lytwing_32`** Arensia: “Oh I hope they accept it, and I hope they are done with their silly errands.”

    - “Me too.” → *conversation ends*

    <span id="d-arensia_lytwing_25"></span>**`arensia_lytwing_25`** Arensia: “That is okay. I did not expect to get it back.” — **effects:** sets stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102)

    - Next → [arensia_lytwing_9](#d-arensia_lytwing_9)

    <span id="d-arensia_lytwing_26"></span>**`arensia_lytwing_26`** Arensia: “After everything you have done for me ... I want you to keep it. Please, I insist!” — **effects:** sets stage 103 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-103)

    - “That is very generous, I won't forget it.” → [arensia_lytwing_9](#d-arensia_lytwing_9)

    <span id="d-arensia_lytwing_3"></span>**`arensia_lytwing_3`** Arensia: “I understand. I guess I will just have to live with their mischief, and hope that I don't lose my hair, or my sanity!”

    - “Good luck.” → *conversation ends*

    <span id="d-arensia_lytwing_4"></span>**`arensia_lytwing_4`** Arensia: “You would be willing to help me? I would be so grateful if you could make them leave me alone.”

    - Next → [arensia_lytwing_33](#d-arensia_lytwing_33)

    <span id="d-arensia_lytwing_12"></span>**`arensia_lytwing_12`** Arensia: “You can buy apples at the Fallhaven tavern. Not sure about strawberries though.”

    - “OK, thanks anyway.” → *conversation ends*

    <span id="d-arensia_lytwing_31"></span>**`arensia_lytwing_31`** Arensia: “Look to the south, and southeast from here. You will see the wild flowers growing next to the trees.”

    - Next → [arensia_lytwing_30](#d-arensia_lytwing_30)

    <span id="d-arensia_lytwing_37"></span>**`arensia_lytwing_37`** Arensia: “Those flowers look perfect.”


    <span id="d-arensia_lytwing_15"></span>**`arensia_lytwing_15`** Arensia: “You have done so much for me already. I will understand if you want to quit, I won't blame you.”

    - “I want to see this through.” → [arensia_lytwing_16](#d-arensia_lytwing_16)
    - “The lytwings are driving me insane. I thought about this, and I can't help you any more. I am sorry.” → [arensia_lytwing_29](#d-arensia_lytwing_29)

    <span id="d-arensia_lytwing_20"></span>**`arensia_lytwing_20`** Arensia: “I know, I will promise on this ring I'm wearing. It belonged to my mother, and it's dear to me, but I will do anything to stop the lytwings!”

    - “I hope this works.” → [arensia_lytwing_21](#d-arensia_lytwing_21)

    <span id="d-arensia_lytwing_9"></span>**`arensia_lytwing_9`** Arensia: “Thank you so much for helping me with the lytwings!”

    - “You are welcome!” → *conversation ends*

    <span id="d-arensia_lytwing_16"></span>**`arensia_lytwing_16`** Arensia: “You are too kind!”

    - Next → [arensia_lytwing_8](#d-arensia_lytwing_8)

    <span id="d-arensia_lytwing_29"></span>**`arensia_lytwing_29`** Arensia: “Are you sure that you want to quit?”

    - “Yes, I want to quit.” → [arensia_lytwing_17](#d-arensia_lytwing_17)
    - “On second thought, I want to see this through.” → [arensia_lytwing_16](#d-arensia_lytwing_16)

    <span id="d-arensia_lytwing_21"></span>**`arensia_lytwing_21`** Arensia: “I made a promise to the ring, here take it to the lytwings!” — **effects:** gives 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md), sets stage 91 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-91)

    - “I will, right away!” → *conversation ends*

    <span id="d-arensia_lytwing_17"></span>**`arensia_lytwing_17`** Arensia: “I appreciate your help either way.” — **effects:** sets stage 101 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-101)

    - “Goodbye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 2 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 38 lines added, 1 line changed<br>· text: “null” → “Hello, dear.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arensia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arensia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arensia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arensia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `arensia` · Data from v0.8.18</small>
