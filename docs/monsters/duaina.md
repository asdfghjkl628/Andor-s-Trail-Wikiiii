# ![](../assets/icons/monsters/monsters_ld1_154.png){ .sprite } Duaina

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

- [remgard3](../maps/remgard3.md)

## Quests

- [Everything in order](../quests/remgard.md): stages 63, 70

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-duaina"></span>**`duaina`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [duaina_0](#d-duaina_0)

    <span id="d-duaina_0"></span>**`duaina_0`** Duaina: “You! I have seen you.”

    - “Jhaeld sent me to ask you about the people that have gone missing.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [duaina_1](#d-duaina_1)
    - “I don't think so, I've never been here before.” → [duaina_stop](#d-duaina_stop)
    - “Yes, I was just here, remember?” *(if reached stage 63 of [Everything in order](../quests/remgard.md#stage-63))* → [duaina_1](#d-duaina_1)

    <span id="d-duaina_1"></span>**`duaina_1`** Duaina: “The dreams and the visions. It is you! The child that challenges the beast. [Duaina gives you a terrified look]”

    - “So you have seen me in your visions?” → [duaina_2](#d-duaina_2)

    <span id="d-duaina_stop"></span>**`duaina_stop`** Duaina: “[Duaina stares at you in silence]”


    <span id="d-duaina_2"></span>**`duaina_2`** Duaina: “The sleeping beast. No, no. The blinding light. Oh, why have you come here? Have you come for me?”

    - “What are you talking about?” → [duaina_3](#d-duaina_3)

    <span id="d-duaina_3"></span>**`duaina_3`** Duaina: “Nooo, please spare me!”

    - “I'm not here to get you, if that's what you are afraid of.” → [duaina_4](#d-duaina_4)

    <span id="d-duaina_4"></span>**`duaina_4`** Duaina: “I can see it in you. You have the gift. The gift that will destroy the beast. My visions were true.”

    - “Maybe you are confusing me with my brother Andor?” → [duaina_5](#d-duaina_5)

    <span id="d-duaina_5"></span>**`duaina_5`** Duaina: “A brother? Yes, that must be what I saw in my visions. It is all becoming clearer.”

    - Next → [duaina_6](#d-duaina_6)

    <span id="d-duaina_6"></span>**`duaina_6`** Duaina: “The black hand sweeps over the land. The beast that hunts. Nooo! Leave this place!”

    - “I'm not here to hurt you!” → [duaina_7](#d-duaina_7)

    <span id="d-duaina_7"></span>**`duaina_7`** Duaina: “The child and the brother. The unsuspecting people. The beast casts its shadow.”

    - Next → [duaina_s_0](#d-duaina_s_0)

    <span id="d-duaina_s_0"></span>**`duaina_s_0`** Duaina: “I have seen you in my visions.”

    - Next → [duaina_s_1](#d-duaina_s_1)

    <span id="d-duaina_s_1"></span>**`duaina_s_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [flagstone (hidden flag)](../quests/flagstone.md#stage-60))* → [duaina_s_1a](#d-duaina_s_1a)
    - branch 2 → [duaina_s_2](#d-duaina_s_2)

    <span id="d-duaina_s_1a"></span>**`duaina_s_1a`** Duaina: “Slaying the beast beneath the prison of Flagstone.”

    - Next → [duaina_s_2](#d-duaina_s_2)

    <span id="d-duaina_s_2"></span>**`duaina_s_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Night visit](../quests/farrik.md#stage-70))* → [duaina_s_2a](#d-duaina_s_2a)
    - branch 2 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [duaina_s_2b](#d-duaina_s_2b)
    - branch 3 → [duaina_s_3](#d-duaina_s_3)

    <span id="d-duaina_s_2a"></span>**`duaina_s_2a`** Duaina: “Cooperating with the thieves in Fallhaven.”

    - Next → [duaina_s_3](#d-duaina_s_3)

    <span id="d-duaina_s_2b"></span>**`duaina_s_2b`** Duaina: “Working against the thieves in Fallhaven.”

    - Next → [duaina_s_3](#d-duaina_s_3)

    <span id="d-duaina_s_3"></span>**`duaina_s_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-50))* → [duaina_s_3a](#d-duaina_s_3a)
    - branch 2 *(if reached stage 60 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-60))* → [duaina_s_3b](#d-duaina_s_3b)
    - branch 3 → [duaina_s_4](#d-duaina_s_4)

    <span id="d-duaina_s_3a"></span>**`duaina_s_3a`** Duaina: “Something about a dagger returned to an ancestor in a tomb.”

    - Next → [duaina_s_4](#d-duaina_s_4)

    <span id="d-duaina_s_3b"></span>**`duaina_s_3b`** Duaina: “Something about stealing a dagger in a dark tomb.”

    - Next → [duaina_s_4](#d-duaina_s_4)

    <span id="d-duaina_s_4"></span>**`duaina_s_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Cheap cuts](../quests/benbyr.md#stage-30))* → [duaina_s_4a](#d-duaina_s_4a)
    - branch 2 → [duaina_jhaeld_s_1](#d-duaina_jhaeld_s_1)

    <span id="d-duaina_s_4a"></span>**`duaina_s_4a`** Duaina: “Killing innocent sheep.”

    - Next → [duaina_jhaeld_s_1](#d-duaina_jhaeld_s_1)

    <span id="d-duaina_jhaeld_s_1"></span>**`duaina_jhaeld_s_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 63 of [Everything in order](../quests/remgard.md#stage-63)

    - branch 1 *(if reached stage 61 of [Everything in order](../quests/remgard.md#stage-61))* → [duaina_jhaeld_s_2](#d-duaina_jhaeld_s_2)
    - branch 2 → [duaina_8](#d-duaina_8)

    <span id="d-duaina_jhaeld_s_2"></span>**`duaina_jhaeld_s_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 62 of [Everything in order](../quests/remgard.md#stage-62))* → [duaina_jhaeld_s_3](#d-duaina_jhaeld_s_3)
    - branch 2 → [duaina_8](#d-duaina_8)

    <span id="d-duaina_8"></span>**`duaina_8`** Duaina: “[Duaina stares at you in silence while holding her hand over her mouth]”

    - “What else have you seen in your visions?” → [duaina_stop](#d-duaina_stop)
    - “I don't understand.” → [duaina_stop](#d-duaina_stop)

    <span id="d-duaina_jhaeld_s_3"></span>**`duaina_jhaeld_s_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 64 of [Everything in order](../quests/remgard.md#stage-64))* → [duaina_jhaeld_s_4](#d-duaina_jhaeld_s_4)
    - branch 2 → [duaina_8](#d-duaina_8)

    <span id="d-duaina_jhaeld_s_4"></span>**`duaina_jhaeld_s_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [Everything in order](../quests/remgard.md#stage-70)

    - branch 1 → [duaina_8](#d-duaina_8)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duaina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duaina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duaina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duaina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `duaina` · Data from v0.8.18</small>
