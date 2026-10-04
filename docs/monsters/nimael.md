# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Nimael

| Stat | Value |
|---|---|
| Class | ? |
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

- [mywild20_houseleft](../maps/mywild20_houseleft.md)

## Quests

- [Delicious soup](../quests/gison_soup.md): stages 70, 90, 110, 120
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 20, 21

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-nimael"></span>**`nimael`** Nimael: “Hello kid.”

    - Next → [nimael_evaluation](#d-nimael_evaluation)

    <span id="d-nimael_evaluation"></span>**`nimael_evaluation`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-10); NOT reached stage 60 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-60); NOT reached stage 62 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-62))* → [nimael_4](#d-nimael_4)
    - branch 2 *(if killed 1× [Zuul'khan](../monsters/zuul_khan9.md); reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 60 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-60); NOT reached stage 62 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-62))* → [nimael_1](#d-nimael_1)
    - branch 3 *(if killed 1× [Zuul'khan](../monsters/zuul_khan9.md); reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); NOT reached stage 60 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-60); NOT reached stage 62 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-62))* → [nimael_1](#d-nimael_1)
    - branch 4 *(if 1500 rounds passed since timer “del_soup”; NOT reached stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120))* → [nimael_b1](#d-nimael_b1)
    - branch 5 → [nimael_busy](#d-nimael_busy)

    <span id="d-nimael_4"></span>**`nimael_4`** Nimael: “Thanks for helping us!”

    - “With pleasure.” → *conversation ends*
    - “I only hope it'll be worth the trouble.” → *conversation ends*

    <span id="d-nimael_1"></span>**`nimael_1`** Nimael: “Please help us. We got raided.”

    - “What happened?” → [nimael_2](#d-nimael_2)

    <span id="d-nimael_b1"></span>**`nimael_b1`** Nimael: “It's nice to see you again. I have some exciting news to share.”

    - Next → [nimael_b2](#d-nimael_b2)

    <span id="d-nimael_busy"></span>**`nimael_busy`** Nimael: “I'm busy at the moment. Please talk to Gison. He's over there.”

    - “Alaun told me that you also make very good soup.” *(if reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110))* → [nimael_arg_10](#d-nimael_arg_10)
    - “OK. Bye.” → *conversation ends*
    - “While exploring the Sullengard forest, I stumbled across this giant mushroom and was wondering if you knew what it was.” *(if reached stage 5 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-5); carry 1× [Gloriosa mushroom](../items/gloriosa_mushroom.md); reached stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120))* → [nimael_pm_0](#d-nimael_pm_0)
    - “Is the Gloriosa soup ready?” *(if reached stage 20 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-20); NOT reached stage 21 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-21))* → [nimael_pm_40](#d-nimael_pm_40)

    <span id="d-nimael_2"></span>**`nimael_2`** Nimael: “I don't know exactly. Everything went so fast ... I'm too upset and my head hurts too much.”

    - Next → [nimael_3](#d-nimael_3)

    <span id="d-nimael_b2"></span>**`nimael_b2`** Nimael: “Thanks to your advice, we have been successful selling more soup to the townsfolk in Fallhaven. We have even cooperated to craft new recipes. We also give free samples of our latest soups to those that buy from us, so they know what is on…” — **effects:** sets stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120)

    - “I'm glad I could help. You sell more soup, and the people in Fallhaven get more choices. Everyone wins!” → *conversation ends*

    <span id="d-nimael_arg_10"></span>**`nimael_arg_10`** Nimael: “Yes. Vegetables with forest herbs. It is even better than my husband's mushroom soup.” — **effects:** sets stage 70 of [Delicious soup](../quests/gison_soup.md#stage-70)

    - “Your husband disagrees.” *(if reached stage 60 of [Delicious soup](../quests/gison_soup.md#stage-60))* → [nimael_arg_20](#d-nimael_arg_20)
    - “If you say so.” → *conversation ends*

    <span id="d-nimael_pm_0"></span>**`nimael_pm_0`** Nimael: “Sure, kid, let me take a look.”

    - “[Hand it over to Nimael]” *(if hand over 1× [Gloriosa mushroom](../items/gloriosa_mushroom.md))* → [nimael_pm_10](#d-nimael_pm_10)
    - “Never mind. I have to go now.” → *conversation ends*

    <span id="d-nimael_pm_40"></span>**`nimael_pm_40`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if 30 rounds passed since timer “gloriosa_soup_making”)* → [nimael_pm_50](#d-nimael_pm_50)
    - branch 2 → [nimael_pm_45](#d-nimael_pm_45)

    <span id="d-nimael_3"></span>**`nimael_3`** Nimael: “If you want to help us, please talk to Gison.”

    - “OK. Get well.” → *conversation ends*

    <span id="d-nimael_arg_20"></span>**`nimael_arg_20`** Nimael: “Well, here is a small taste of mine, and a small taste of his. I am sure you will agree with me.” — **effects:** sets stage 90 of [Delicious soup](../quests/gison_soup.md#stage-90)

    - “I think they are both good. One is not better than the other, just different. Different people have different tastes,…” → [nimael_arg_30](#d-nimael_arg_30)

    <span id="d-nimael_pm_10"></span>**`nimael_pm_10`** Nimael: “Ah, what you have here is called the Diervilla Cobaea, or more commonly known as the Gloriosa, it is an extremely rare, but highly poisonous fungus most commonly found in dark, shadowy places like forests. It's a defense mechanism as it…”

    - “So it is useless?” → [nimael_pm_20](#d-nimael_pm_20)

    <span id="d-nimael_pm_50"></span>**`nimael_pm_50`** Nimael: “Yes. Please enjoy while it's hot.” — **effects:** sets stage 21 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-21), gives 1× [Gloriosa mushroom soup](../items/gloriosa_mushroom_soup.md)


    <span id="d-nimael_pm_45"></span>**`nimael_pm_45`** Nimael: “No, not yet. You must have patience. Making the Gloriosa soup safe to eat takes time.”


    <span id="d-nimael_arg_30"></span>**`nimael_arg_30`** Nimael: “For a kid, that's a very insightful comment. I will talk to my husband about how we can better sell both soups to the townsfolk in Fallhaven. Here are a couple of bottles of my soup as thanks.” — **effects:** sets stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110), gives 2× [Nimael's vegetable soup](../items/nimael_soup.md), starts timer “del_soup”

    - “Glad I could help.” → *conversation ends*

    <span id="d-nimael_pm_20"></span>**`nimael_pm_20`** Nimael: “Actually, quite the opposite in fact. You see, Gison and I have perfected the process of removing the poison and using it in our soups. I can do this for you if you like.”

    - “No, thank you. I think I will hang onto it for a little bit and see if I can find a better use for it.” → [nimael_pm_25](#d-nimael_pm_25)
    - “Thanks. That would be great.” → [nimael_pm_30](#d-nimael_pm_30)

    <span id="d-nimael_pm_25"></span>**`nimael_pm_25`** Nimael: “Well, if you change your mind, you know where to find me.” — **effects:** gives 1× [Gloriosa mushroom](../items/gloriosa_mushroom.md)


    <span id="d-nimael_pm_30"></span>**`nimael_pm_30`** Nimael: “I just need a little bit of time. Please come back soon and I will have your soup ready.” — **effects:** starts timer “gloriosa_soup_making”, sets stage 20 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-20)




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nimael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nimael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nimael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nimael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `nimael` · Data from v0.8.18</small>
