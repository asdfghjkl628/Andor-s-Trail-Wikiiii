# ![](../assets/icons/monsters/monsters_ld1_180.png){ .sprite } Rosmara

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Strawberry](../items/strawberry.md) | 100% | 2 to 4 |
| [Radish](../items/radish.md) | 100% | 3 to 8 |
| [Carrots](../items/carrots.md) | 100% | 3 to 5 |
| [Pear](../items/pear.md) | 100% | 3 to 10 |
| [Fig](../items/fig_fruit.md) | 100% | 5 to 9 |
| [Green apple](../items/apple_green.md) | 100% | 5 to 9 |
| [Red apple](../items/apple_red.md) | 100% | 7 to 9 |
| [Broccoli](../items/broccoli.md) | 100% | 10 to 12 |
| [Durian fruit](../items/durian.md) | 85% | 1 to 2 |
| [Corn](../items/corn.md) | 100% | 1 to 3 |

## Found on

- [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md)

## Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 8

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-rosmara_initial_phrase"></span>**`rosmara_initial_phrase`** Rosmara: “How can I help you today?”

    - “What is going on with that cat?” → [rosmara_cat_1](#d-rosmara_cat_1)
    - “What is this place?” → [rosmara_explain](#d-rosmara_explain)
    - “Do you know why the village of Wexlow is void of people?” *(if reached stage 11 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-11); NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10))* → [rosmara_wexlow](#d-rosmara_wexlow)
    - “I would like to make a purchase, please.” *(if reached stage 8 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-8))* → *shop opens*

    <span id="d-rosmara_cat_1"></span>**`rosmara_cat_1`** Rosmara: “Well, you see, he's my guard cat.”

    - “Your guard cat?” → [rosmara_cat_2](#d-rosmara_cat_2)

    <span id="d-rosmara_explain"></span>**`rosmara_explain`** Rosmara: “This is my place of business. Right here on the side of Duleian Road.”

    - “Why here? There's nothing else here besides you.” → [rosmara_explain_2](#d-rosmara_explain_2)
    - “What do you sell?” → [rosmara_explain_3](#d-rosmara_explain_3)

    <span id="d-rosmara_wexlow"></span>**`rosmara_wexlow`** Rosmara: “What?! There's nobody in the village?”

    - “Nope. Not a single person, and it looks like there hasn't been for a while.” → [rosmara_wexlow2](#d-rosmara_wexlow2)

    <span id="d-rosmara_cat_2"></span>**`rosmara_cat_2`** Rosmara: “Yes. If you attempt to rob me, he'll attack you. Hence he is my guard cat.”

    - “I see.” → *conversation ends*
    - “Seriously?” → [rosmara_cat_3](#d-rosmara_cat_3)

    <span id="d-rosmara_explain_2"></span>**`rosmara_explain_2`** Rosmara: “Oh, you silly child. This is a very well traveled road. All the people coming and going from and to Feygard. It's a long road and they get hungry.”

    - “I'm not a child anymore!” *(if wearing [#heartsteel_filter](../items/#heartsteel_filter.md))* → [rosmara_heartsteel_10](#d-rosmara_heartsteel_10)
    - “I am not a child!” *(if NOT carry 1× [#heartsteel_filter](../items/#heartsteel_filter.md))* → *conversation ends*
    - “OK, you sell food. What kind of food?” → [rosmara_explain_3](#d-rosmara_explain_3)
    - “And the fog? No one could take the path anymore.” → [rosmara_explain_10](#d-rosmara_explain_10)

    <span id="d-rosmara_explain_3"></span>**`rosmara_explain_3`** Rosmara: “I sell things that a child such as yourself is most likely not interested in.”

    - “I am not a child anymore!!” → *conversation ends*
    - “What is it?” → [rosmara_explain_4](#d-rosmara_explain_4)

    <span id="d-rosmara_wexlow2"></span>**`rosmara_wexlow2`** Rosmara: “Hmm, I hope they are all right.”

    - “Me too.” → *conversation ends*

    <span id="d-rosmara_cat_3"></span>**`rosmara_cat_3`** Rosmara: “No, not seroiusly. He guards my fruits and vegetables.”

    - “Guards them from what?” → [rosmara_cat_4](#d-rosmara_cat_4)

    <span id="d-rosmara_heartsteel_10"></span>**`rosmara_heartsteel_10`** Rosmara: “Yes, yes you are and a foolhardy one at that.”

    - “Why the insult?” → [rosmara_heartsteel_20](#d-rosmara_heartsteel_20)

    <span id="d-rosmara_explain_10"></span>**`rosmara_explain_10`** Rosmara: “What kind of fog are you talking about?”

    - “The fog that the witch had created in the swamp, of course.” *(if reached stage 30 of [Fog in the woods](../quests/fogmonster.md#stage-30))* → [rosmara_explain_11](#d-rosmara_explain_11)
    - “The fog further down the road behind the kobolds, of course.” *(if NOT reached stage 30 of [Fog in the woods](../quests/fogmonster.md#stage-30))* → [rosmara_explain_11a](#d-rosmara_explain_11a)

    <span id="d-rosmara_explain_4"></span>**`rosmara_explain_4`** Rosmara: “I sell fruits and vegetables.” — **effects:** sets stage 8 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-8)

    - “As an adult, I am interested in seeing what you have.” → *shop opens*
    - “Where do you get these fruits and vegetables?” → [rosmara_explain_5](#d-rosmara_explain_5)

    <span id="d-rosmara_cat_4"></span>**`rosmara_cat_4`** Rosmara: “I have a business agreement with him. He guards my food from the rats in exchange for a place to sleep.”

    - “Oh, why didn't you just say so?” → [rosmara_cat_5](#d-rosmara_cat_5)
    - “Well, he's not holding up his end of the deal, because there's a rat behind your tent right now.” → [rosmara_cat_rat](#d-rosmara_cat_rat)

    <span id="d-rosmara_heartsteel_20"></span>**`rosmara_heartsteel_20`** Rosmara: “Carrying the very same weapon Geomyr banned?”

    - “Oh! Oops!” → *conversation ends*

    <span id="d-rosmara_explain_11"></span>**`rosmara_explain_11`** Rosmara: “Are you still afraid of witches or fog, child?”

    - “I am not a child anymore!!” → *conversation ends*
    - “I was with the witch! Without me the fog would still be there!” → [rosmara_explain_12](#d-rosmara_explain_12)

    <span id="d-rosmara_explain_11a"></span>**`rosmara_explain_11a`** Rosmara: “Are you still afraid of kobolds or fog, child?”

    - “I am not a child anymore!!” → *conversation ends*
    - “I have mastered the fog and survived the kobolds!!” → [rosmara_explain_12](#d-rosmara_explain_12)

    <span id="d-rosmara_explain_5"></span>**`rosmara_explain_5`** Rosmara: “From all over Dhayavar, but mostly from the great farmers in Loneford.”

    - “Oh, yeah. I've seen all of their great farms.” *(if reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → *conversation ends*
    - “Loneford, where's that?” *(if NOT reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → *conversation ends*

    <span id="d-rosmara_cat_5"></span>**`rosmara_cat_5`** Rosmara: “I wanted to waste your time just as you are doing to my time. Walking up to my business counter asking about my cat! Get lost, kid.”


    <span id="d-rosmara_cat_rat"></span>**`rosmara_cat_rat`** Rosmara: “Oh, my!”


    <span id="d-rosmara_explain_12"></span>**`rosmara_explain_12`** Rosmara: “Yes, of course. Calm down, child.”

    - Next → [rosmara_initial_phrase](#d-rosmara_initial_phrase)



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 18 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rosmara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rosmara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rosmara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rosmara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `rosmara` · Data from v0.8.18</small>
