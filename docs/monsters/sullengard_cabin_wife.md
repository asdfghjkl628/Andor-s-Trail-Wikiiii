# ![](../assets/icons/monsters/monsters_ld1_221.png){ .sprite } Hadena

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

- [sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)

## Quests

- [Getting home on time](../quests/deebo_orchard_ght.md): stages 10, 20, 60
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 16

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_hadena_selector_0"></span>**`sullengard_hadena_selector_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10))* → [sullengard_hadena_0](#d-sullengard_hadena_0)
    - branch 2 *(if NOT reached stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60))* → [sullengard_hadena_6](#d-sullengard_hadena_6)
    - branch 3 *(if reached stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60))* → [sullengard_hadena_completed](#d-sullengard_hadena_completed)

    <span id="d-sullengard_hadena_0"></span>**`sullengard_hadena_0`** Hadena: “Andor, good timing! Your arrival is much appreciated because I need your help to get my husband home on time today.” — **effects:** sets stage 16 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-16)

    - “So, my brother Andor was here as well? I'm $playername and you are?” → [sullengard_hadena_1](#d-sullengard_hadena_1)
    - “You must be mistaken. I'm $playername and Andor is my brother, and you are?” → [sullengard_hadena_1](#d-sullengard_hadena_1)
    - “I'm sorry because I was only half listening to you earlier, so I am a little fuzzy on the details. But can you explain…” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10)* → [sullengard_hadena_2](#d-sullengard_hadena_2)

    <span id="d-sullengard_hadena_6"></span>**`sullengard_hadena_6`** Hadena: “I'm waiting for my husband's arrival. Please, I want him home on time today.”

    - “What do yo want me to do again with your husband?” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10)* → [sullengard_hadena_2](#d-sullengard_hadena_2)
    - “I'm not done yet.” *(if NOT reached stage 50 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50))* → *conversation ends*
    - “It is done. Ainsley will be home on time today.” *(if latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50) is 50)* → [sullengard_hadena_7](#d-sullengard_hadena_7)

    <span id="d-sullengard_hadena_completed"></span>**`sullengard_hadena_completed`** Hadena: “Thank you for helping Ainsley and I.”


    <span id="d-sullengard_hadena_1"></span>**`sullengard_hadena_1`** Hadena: “Oh, I'm sorry. My name is Hadena. Andor used to visit here but I don't know why he doesn't anymore. Anyways, I really need your help...please.” — **effects:** sets stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10)

    - “How may I help you?” → [sullengard_hadena_2](#d-sullengard_hadena_2)
    - “I'm sorry I can't help you right now. I'm busy.” → *conversation ends*

    <span id="d-sullengard_hadena_2"></span>**`sullengard_hadena_2`** Hadena: “As I already said, I need your help to get my husband Ainsley home on time today.”

    - Next → [sullengard_hadena_4](#d-sullengard_hadena_4)

    <span id="d-sullengard_hadena_7"></span>**`sullengard_hadena_7`** Hadena: “Thank you so much for helping us. You are just like your brother.” — **effects:** sets stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60)

    - “Of course. He is my brother.” → *conversation ends*
    - “You're welcome.” → *conversation ends*

    <span id="d-sullengard_hadena_4"></span>**`sullengard_hadena_4`** Hadena: “He is working at Deebo's Orchard located southwest of here. Please go there and help him.” — **effects:** sets stage 20 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-20)

    - “I'll go now to help get him home on time.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_cabin_wife.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sullengard_cabin_wife` · Data from v0.8.18</small>
