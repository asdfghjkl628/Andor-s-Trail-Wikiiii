# ![](../assets/icons/monsters/monsters_karvis2_5.png){ .sprite } Taevinn

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

- [loneford7](../maps/loneford7.md)

## Quests

- [Flows through the veins](../quests/loneford.md): stages 10, 11, 24, 25

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-taevinn"></span>**`taevinn`** Taevinn: “Please, you must help us!”

    - “Do you know anything about the illness?” *(if reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11))* → [taevinn_1](#d-taevinn_1)
    - “What's wrong?” → [loneford_farmer0_1](#d-loneford_farmer0_1)

    <span id="d-taevinn_1"></span>**`taevinn_1`** Taevinn: “I'll tell you what I know. We try to follow the law around here. Without rules and laws, how would we be any different from the savages that roam the southern lands?”

    - Next → [taevinn_2](#d-taevinn_2)

    <span id="d-loneford_farmer0_1"></span>**`loneford_farmer0_1`** Taevinn: “Didn't you hear about the illness?”

    - “What illness?” → [loneford_farmer_il_1](#d-loneford_farmer_il_1)

    <span id="d-taevinn_2"></span>**`taevinn_2`** Taevinn: “But even if we here in Loneford keep as peaceful as possible, there's always someone that has a desire to cause mischief.”

    - Next → [taevinn_3](#d-taevinn_3)

    <span id="d-loneford_farmer_il_1"></span>**`loneford_farmer_il_1`** Taevinn: “It all started a few days ago. Selgan found Hesor passed out on his old crop field, completely white faced and shivering.”

    - Next → [loneford_farmer_il_2](#d-loneford_farmer_il_2)

    <span id="d-taevinn_3"></span>**`taevinn_3`** Taevinn: “Have you seen him? That fool Sienn. Him and his 'pet' are always trying to cause some trouble. We can't have that around here in our friendly village. Especially not in times like these when we are trying to show our good side to those…”

    - Next → [taevinn_4](#d-taevinn_4)

    <span id="d-loneford_farmer_il_2"></span>**`loneford_farmer_il_2`** Taevinn: “A few days later, Selgan started showing the same symptoms as Hesor, with stomach aches. I also started feeling the pains and got the shivers.”

    - Next → [loneford_farmer_il_3](#d-loneford_farmer_il_3)

    <span id="d-taevinn_4"></span>**`taevinn_4`** Taevinn: “Did you know I tried to talk to him on several occasions about his so called 'pet'? I couldn't really make out what he was trying to tell me, but that thing of his nearly tried to kill me, it did!”

    - Next → [taevinn_5](#d-taevinn_5)

    <span id="d-loneford_farmer_il_3"></span>**`loneford_farmer_il_3`** Taevinn: “Then, all people showed the symptoms in one way or another.”

    - Next → [loneford_farmer_il_4](#d-loneford_farmer_il_4)

    <span id="d-taevinn_5"></span>**`taevinn_5`** Taevinn: “I tell you, there's mischief all around him and that thing he keeps around. I am sure they are up to something. They probably caused this illness somehow. Maybe we caught something contagious from that thing of his that he keeps around?” — **effects:** sets stage 24 of [Flows through the veins](../quests/loneford.md#stage-24)

    - Next → [loneford_ill_c_1](#d-loneford_ill_c_1)

    <span id="d-loneford_farmer_il_4"></span>**`loneford_farmer_il_4`** Taevinn: “Poor old Selgan and Hesor apparently got the worst of it, and both died the day before yesterday.”

    - Next → [loneford_farmer_il_5](#d-loneford_farmer_il_5)

    <span id="d-loneford_ill_c_1"></span>**`loneford_ill_c_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [loneford_ill_c_2](#d-loneford_ill_c_2)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_5"></span>**`loneford_farmer_il_5`** Taevinn: “Cursed illness, why did it have to be Selgan and Hesor? I wonder who is next.”

    - Next → [loneford_farmer_il_6](#d-loneford_farmer_il_6)

    <span id="d-loneford_ill_c_2"></span>**`loneford_ill_c_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → [loneford_ill_c_3](#d-loneford_ill_c_3)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_n"></span>**`loneford_ill_c_n`** Taevinn: “That's what I think anyway.”


    <span id="d-loneford_farmer_il_6"></span>**`loneford_farmer_il_6`** Taevinn: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our suspicions.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [loneford_farmer_il_7](#d-loneford_farmer_il_7)

    <span id="d-loneford_ill_c_3"></span>**`loneford_ill_c_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23))* → [loneford_ill_c_4](#d-loneford_ill_c_4)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_7"></span>**`loneford_farmer_il_7`** Taevinn: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and we fear who will be taken by the illness next.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)


    <span id="d-loneford_ill_c_4"></span>**`loneford_ill_c_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24))* → [loneford_ill_c_5](#d-loneford_ill_c_5)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_5"></span>**`loneford_ill_c_5`** Taevinn: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but didn't dare tell me what it was.” — **effects:** sets stage 25 of [Flows through the veins](../quests/loneford.md#stage-25)

    - “Thank you, I will go talk to him.” → *conversation ends*
    - “Great, another drunk that I have to talk to.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taevinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taevinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taevinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taevinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `taevinn` · Data from v0.8.18</small>
