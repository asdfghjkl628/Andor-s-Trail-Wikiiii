# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Rhodita

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

- [guynmart_wood_1](../maps/guynmart_wood_1.md)

## Quests

- [Roses](../quests/guynmart.md): stages 10

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_farmer_10"></span>**`guynmart_farmer_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 180 of [Roses](../quests/guynmart.md#stage-180))* → [guynmart_farmer_14](#d-guynmart_farmer_14)
    - branch 2 *(if reached stage 181 of [Roses](../quests/guynmart.md#stage-181))* → [guynmart_farmer_14](#d-guynmart_farmer_14)
    - branch 3 *(if reached stage 170 of [Roses](../quests/guynmart.md#stage-170))* → [guynmart_farmer_16](#d-guynmart_farmer_16)
    - branch 4 *(if reached stage 30 of [Roses](../quests/guynmart.md#stage-30))* → [guynmart_farmer_100](#d-guynmart_farmer_100)
    - branch 5 → [guynmart_farmer_20](#d-guynmart_farmer_20)

    <span id="d-guynmart_farmer_14"></span>**`guynmart_farmer_14`** Rhodita: “Welcome! Nice to see you again.”


    <span id="d-guynmart_farmer_16"></span>**`guynmart_farmer_16`** Rhodita: “Good morning! Did you hear the music last night? I think it came from the castle.”


    <span id="d-guynmart_farmer_100"></span>**`guynmart_farmer_100`** Rhodita: “Hi! Any news from Guynmart castle?”

    - “Oh yes, it is a long story. Maybe I could stay overnight and tell you all about it in detail?” *(if reached stage 164 of [Roses](../quests/guynmart.md#stage-164))* → [guynmart_farmer_110](#d-guynmart_farmer_110)
    - “Yes, but I want to learn more about what is going on before I am willing to discuss it.” *(if NOT reached stage 164 of [Roses](../quests/guynmart.md#stage-164))* → *conversation ends*

    <span id="d-guynmart_farmer_20"></span>**`guynmart_farmer_20`** Rhodita: “What is a kid like you doing all alone on the road?”

    - “I am looking for my brother Andor. Have you seen him by any chance?” → [guynmart_farmer_30](#d-guynmart_farmer_30)
    - “I am tired and hungry. Do you have a place to rest, please?” → [guynmart_farmer_90](#d-guynmart_farmer_90)
    - “None of your business.” → *conversation ends*

    <span id="d-guynmart_farmer_110"></span>**`guynmart_farmer_110`** Rhodita: “With pleasure. Just go inside and make yourself comfortable on the cushions in the corner behind the oven. We will talk when my work is done.”

    - “Great. Thank you.” → *conversation ends*

    <span id="d-guynmart_farmer_30"></span>**`guynmart_farmer_30`** Rhodita: “No, sorry. We seldom see strangers in the area. But you could ask at Guynmart Castle. Just follow the road to the north, you can't miss it.”

    - “Guynmart Castle? I have never heard of it. Please tell me more.” → [guynmart_farmer_40](#d-guynmart_farmer_40)

    <span id="d-guynmart_farmer_90"></span>**`guynmart_farmer_90`** Rhodita: “Yes of course. Go inside, there is some food left, and some cushions in the corner behind the oven. I will join you later.”

    - “Great. Thank you.” → *conversation ends*

    <span id="d-guynmart_farmer_40"></span>**`guynmart_farmer_40`** Rhodita: “Our land belongs to Guynmart Castle, but old Guynmart is a friendly and righteous man. He never takes too much from us.”

    - Next → [guynmart_farmer_50](#d-guynmart_farmer_50)

    <span id="d-guynmart_farmer_50"></span>**`guynmart_farmer_50`** Rhodita: “Young Lady Hannah of Guynmart Castle often comes to visit us. A lovely girl she is. But she has not been here for a week now. I wonder if everything is all right.”

    - Next → [guynmart_farmer_60](#d-guynmart_farmer_60)

    <span id="d-guynmart_farmer_60"></span>**`guynmart_farmer_60`** Rhodita: “I have too much work to do now. But maybe you could check if everything is OK with her?” — **effects:** sets stage 10 of [Roses](../quests/guynmart.md#stage-10)

    - “Yes, of course. I will come back and tell you what I find out.” → *conversation ends*
    - “No, sorry. I have to press on again. Bye.” → *conversation ends*
    - “I will go tomorrow. But now I am tired and hungry. Do you have a place to rest, please?” → [guynmart_farmer_90](#d-guynmart_farmer_90)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Our land belongs to Guynmart Castle, but old Guynmart is a friendly a…” → “Our land belongs to Guynmart Castle, but old Guynmart is a friendly a…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_farmer` · Data from v0.8.18</small>
