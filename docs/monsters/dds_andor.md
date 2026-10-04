# ![](../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite } Andor

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

- [road5_house](../maps/road5_house.md)
- [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md)

## Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 300, 310
- [Shadows](../quests/shadows.md): stages 280, 290

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_andor"></span>**`dds_andor`** Andor: “Hey, who's that running over?”

    - “Hey, Andor!” *(if reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280))* → [dds_andor_2](#d-dds_andor_2)
    - “Hey, Andor!” *(if reached stage 260 of [Shadows](../quests/shadows.md#stage-260))* → [dds_andor_4](#d-dds_andor_4)

    <span id="d-dds_andor_2"></span>**`dds_andor_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 300 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-300)

    - branch 1 → [dds_andor_10](#d-dds_andor_10)

    <span id="d-dds_andor_4"></span>**`dds_andor_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 280 of [Shadows](../quests/shadows.md#stage-280)

    - branch 1 → [dds_andor_10](#d-dds_andor_10)

    <span id="d-dds_andor_10"></span>**`dds_andor_10`** Andor: “Hello, $playername, is it really you? You have grown.”

    - “I've finally found you!” → [dds_andor_20](#d-dds_andor_20)

    <span id="d-dds_andor_20"></span>**`dds_andor_20`** Andor: “Why? Did you miss me so much? Or do you not want to have to do Mikhail's work all by yourself?”

    - “Don't talk nonsense. I'm glad to see you. Come home with me.” → [dds_andor_30](#d-dds_andor_30)

    <span id="d-dds_andor_30"></span>**`dds_andor_30`** Andor: “I can't. At least not yet.”

    - “But why? Does someone want to do something bad to you? I won't allow that.” → [dds_andor_40](#d-dds_andor_40)

    <span id="d-dds_andor_40"></span>**`dds_andor_40`** Andor: “[Andor laughs dryly] Let it go, it's the big brother's job to keep an eye on things.”

    - “But ...” → [dds_andor_50](#d-dds_andor_50)

    <span id="d-dds_andor_50"></span>**`dds_andor_50`** Andor: “No. It's not possible. You'll understand that one day.”

    - “Are you just going to disappear again? Please don't!” *(if reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280))* → [dds_andor_52](#d-dds_andor_52)
    - “Are you just going to disappear again? Please don't!” *(if reached stage 260 of [Shadows](../quests/shadows.md#stage-260))* → [dds_andor_54](#d-dds_andor_54)

    <span id="d-dds_andor_52"></span>**`dds_andor_52`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 310 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-310), sets stage 145 of [andor (hidden flag)](../quests/andor.md#stage-145)

    - branch 1 → [dds_andor_60](#d-dds_andor_60)

    <span id="d-dds_andor_54"></span>**`dds_andor_54`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 290 of [Shadows](../quests/shadows.md#stage-290), sets stage 147 of [andor (hidden flag)](../quests/andor.md#stage-147)

    - branch 1 → [dds_andor_60](#d-dds_andor_60)

    <span id="d-dds_andor_60"></span>**`dds_andor_60`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 999 of [andor (hidden flag)](../quests/andor.md#stage-999)

    - branch 1 → [dds_andor_62](#d-dds_andor_62)

    <span id="d-dds_andor_62"></span>**`dds_andor_62`** Andor: “Don't worry - we'll see each other again, in happier days.” — **effects:** removes monsters from wayto_feygard_duleian_2, removes monsters from road5_house, sets stage 999 of [andor (hidden flag)](../quests/andor.md#stage-999)

    - “Wait!” → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `dds_andor` · Data from v0.8.18</small>
