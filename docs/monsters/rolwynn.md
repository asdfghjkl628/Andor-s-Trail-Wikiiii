# ![](../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite } Rolwynn

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

- [fields0](../maps/fields0.md)

## Quests

- [Flows through the veins](../quests/loneford.md): stages 10, 11, 22, 25

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Rolwynn. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/rolwynn.json" data-npc="Rolwynn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-rolwynn"></span>**`rolwynn`** Rolwynn: “What have we done to deserve this? Please, will you help us?”

    - “What do you think is the cause of the illness?” *(if reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11))* → [rolwynn_1](#d-rolwynn_1)
    - “What's wrong?” → [loneford_farmer0_1](#d-loneford_farmer0_1)

    <span id="d-rolwynn_1"></span>**`rolwynn_1`** Rolwynn: “My guess is that this must be something done by those arrogant people from Feygard.”

    - Next → [rolwynn_2](#d-rolwynn_2)

    <span id="d-loneford_farmer0_1"></span>**`loneford_farmer0_1`** Rolwynn: “Didn't you hear about the illness?”

    - “What illness?” → [loneford_farmer_il_1](#d-loneford_farmer_il_1)

    <span id="d-rolwynn_2"></span>**`rolwynn_2`** Rolwynn: “They are always looking for ways to make our lives a little bit harder.”

    - Next → [rolwynn_3](#d-rolwynn_3)

    <span id="d-loneford_farmer_il_1"></span>**`loneford_farmer_il_1`** Rolwynn: “It all started a few days ago. Selgan found Hesor passed out on his old crop field, completely white faced and shivering.”

    - Next → [loneford_farmer_il_2](#d-loneford_farmer_il_2)

    <span id="d-rolwynn_3"></span>**`rolwynn_3`** Rolwynn: “We try to farm our lands to feed ourselves, but they demand that they get a share of whatever we bring in.”

    - Next → [rolwynn_4](#d-rolwynn_4)

    <span id="d-loneford_farmer_il_2"></span>**`loneford_farmer_il_2`** Rolwynn: “A few days later, Selgan started showing the same symptoms as Hesor, with stomach aches. I also started feeling the pains and got the shivers.”

    - Next → [loneford_farmer_il_3](#d-loneford_farmer_il_3)

    <span id="d-rolwynn_4"></span>**`rolwynn_4`** Rolwynn: “Lately, the crops haven't been as good as they used to be, and the guards apparently think we are withholding some part of their share.”

    - Next → [rolwynn_5](#d-rolwynn_5)

    <span id="d-loneford_farmer_il_3"></span>**`loneford_farmer_il_3`** Rolwynn: “Then, all people showed the symptoms in one way or another.”

    - Next → [loneford_farmer_il_4](#d-loneford_farmer_il_4)

    <span id="d-rolwynn_5"></span>**`rolwynn_5`** Rolwynn: “I am sure that they did something to us as punishment for not following their *rules*. They are always talking about how the laws and rules are so precious to them.” — **effects:** sets stage 22 of [Flows through the veins](../quests/loneford.md#stage-22)

    - Next → [loneford_ill_c_1](#d-loneford_ill_c_1)

    <span id="d-loneford_farmer_il_4"></span>**`loneford_farmer_il_4`** Rolwynn: “Poor old Selgan and Hesor apparently got the worst of it, and both died the day before yesterday.”

    - Next → [loneford_farmer_il_5](#d-loneford_farmer_il_5)

    <span id="d-loneford_ill_c_1"></span>**`loneford_ill_c_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [loneford_ill_c_2](#d-loneford_ill_c_2)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_5"></span>**`loneford_farmer_il_5`** Rolwynn: “Cursed illness, why did it have to be Selgan and Hesor? I wonder who is next.”

    - Next → [loneford_farmer_il_6](#d-loneford_farmer_il_6)

    <span id="d-loneford_ill_c_2"></span>**`loneford_ill_c_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → [loneford_ill_c_3](#d-loneford_ill_c_3)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_n"></span>**`loneford_ill_c_n`** Rolwynn: “That's what I think anyway.”


    <span id="d-loneford_farmer_il_6"></span>**`loneford_farmer_il_6`** Rolwynn: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our suspicions.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [loneford_farmer_il_7](#d-loneford_farmer_il_7)

    <span id="d-loneford_ill_c_3"></span>**`loneford_ill_c_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23))* → [loneford_ill_c_4](#d-loneford_ill_c_4)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_7"></span>**`loneford_farmer_il_7`** Rolwynn: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and we fear who will be taken by the illness next.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)


    <span id="d-loneford_ill_c_4"></span>**`loneford_ill_c_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24))* → [loneford_ill_c_5](#d-loneford_ill_c_5)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_5"></span>**`loneford_ill_c_5`** Rolwynn: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but didn't dare tell me what it was.” — **effects:** sets stage 25 of [Flows through the veins](../quests/loneford.md#stage-25)

    - “Thank you, I will go talk to him.” → *conversation ends*
    - “Great, another drunk that I have to talk to.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `rolwynn` · Data from v0.8.18</small>
