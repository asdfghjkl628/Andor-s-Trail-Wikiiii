# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Jan

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

??? quote "Dialogue (20 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-jan_start_select"></span>**`jan_start_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [jan (hidden flag)](../quests/jan.md#stage-100))* → [jan_complete2](#d-jan_complete2)
    - branch 2 *(if reached stage 10 of [jan (hidden flag)](../quests/jan.md#stage-10))* → [jan_return](#d-jan_return)
    - branch 3 → [jan_default](#d-jan_default)

    <span id="d-jan_complete2"></span>**`jan_complete2`** Jan: “Thanks for dealing with Irogotu earlier! I am forever in debt to you.”

    - “Bye.” → *conversation ends*

    <span id="d-jan_return"></span>**`jan_return`** Jan: “Hello again kid. Did you find Irogotu down in the cave?”

    - “No, not yet.” → [jan_default14](#d-jan_default14)
    - “Can you tell me your story again?” → [jan_background](#d-jan_background)
    - “Yes, I have killed Irogotu.” *(if hand over 1× [Gandir's ring](../items/ring_gandir.md))* → [jan_complete](#d-jan_complete)

    <span id="d-jan_default"></span>**`jan_default`** Jan: “Hello kid. Please leave me to my mourning.”

    - “What is the problem?” → [jan_default2](#d-jan_default2)
    - “Do you want to talk about it?” → [jan_default2](#d-jan_default2)
    - “OK, bye.” → *conversation ends*

    <span id="d-jan_default14"></span>**`jan_default14`** Jan: “Return to me when you are done. Bring me Gandir's ring from Irogotu down in the cave.”

    - “OK, bye.” → *conversation ends*

    <span id="d-jan_background"></span>**`jan_background`** Jan: “Didn't you listen the first time I told you the story? Do I really have to tell you the story one more time?”

    - “Yes, please tell me the story again.” → [jan_default3](#d-jan_default3)
    - “I wasn't listening that much the first time you told it. What was that about a treasure?” → [jan_default4](#d-jan_default4)
    - “No, never mind. I remember it now.” → [jan_default14](#d-jan_default14)

    <span id="d-jan_complete"></span>**`jan_complete`** Jan: “Wait, what? You actually went down there and returned alive? How did you manage that? Wow, I almost died going into that cave. Oh thank you so much for bringing me back Gandir's ring! Now I can have something to remember him by.” — **effects:** sets stage 100 of [jan (hidden flag)](../quests/jan.md#stage-100)

    - “Glad that I could help. Goodbye.” → *conversation ends*
    - “Shadow be with you. Goodbye.” → *conversation ends*
    - “Whatever. I only did it for the loot.” → *conversation ends*

    <span id="d-jan_default2"></span>**`jan_default2`** Jan: “Oh, it's so sad. I really don't want to talk about it.”

    - “Please do.” → [jan_default3](#d-jan_default3)
    - “OK, bye.” → *conversation ends*

    <span id="d-jan_default3"></span>**`jan_default3`** Jan: “Well, I guess it's OK to tell you. You seem to be a nice enough kid.”

    - Next → [jan_default4](#d-jan_default4)

    <span id="d-jan_default4"></span>**`jan_default4`** Jan: “My friend Gandir, his friend Irogotu, and I were down here digging this hole. We had heard there was a hidden treasure down here.”

    - Next → [jan_default5](#d-jan_default5)

    <span id="d-jan_default5"></span>**`jan_default5`** Jan: “We started digging and finally broke through to the cave system below. That's when we discovered them. The critters and bugs.”

    - Next → [jan_default6](#d-jan_default6)

    <span id="d-jan_default6"></span>**`jan_default6`** Jan: “Oh those critters. Damn bastards. Nearly killed me they did. Gandir and I told Irogotu that we should stop the digging and leave while we still could.”

    - Next → [jan_default7](#d-jan_default7)

    <span id="d-jan_default7"></span>**`jan_default7`** Jan: “But Irogotu wanted to continue deeper into the dungeon. He and Gandir got into an argument and started fighting.”

    - Next → [jan_default8](#d-jan_default8)

    <span id="d-jan_default8"></span>**`jan_default8`** Jan: “That's when it happened. *sob* Oh what have we done?”

    - “Please go on.” → [jan_default9](#d-jan_default9)

    <span id="d-jan_default9"></span>**`jan_default9`** Jan: “Irogotu killed Gandir with his bare hands. You could see the fire in his eyes. He almost seemed to enjoy it.”

    - Next → [jan_default10](#d-jan_default10)

    <span id="d-jan_default10"></span>**`jan_default10`** Jan: “I fled and haven't dared go back down there because of the critters and Irogotu himself.”

    - Next → [jan_default11](#d-jan_default11)

    <span id="d-jan_default11"></span>**`jan_default11`** Jan: “Oh that damn Irogotu. If only I could get to him. I'd show him one thing and another.”

    - “Do you think I could help?” → [jan_default11_1](#d-jan_default11_1)

    <span id="d-jan_default11_1"></span>**`jan_default11_1`** Jan: “Do you think you could help me?”

    - “Sure, there may be some treasure in this for me.” → [jan_default12](#d-jan_default12)
    - “Sure. Irogotu should pay for what he did.” → [jan_default12](#d-jan_default12)
    - “No thanks, I would rather not be involved in this. It sounds dangerous.” → *conversation ends*

    <span id="d-jan_default12"></span>**`jan_default12`** Jan: “Really? You think you could help? Hmm, maybe you could. Beware of those bugs though, they're really tough bastards.” — **effects:** sets stage 10 of [jan (hidden flag)](../quests/jan.md#stage-10)

    - Next → [jan_default13](#d-jan_default13)

    <span id="d-jan_default13"></span>**`jan_default13`** Jan: “If you really want to help, go find Irogotu down in the cave, and get me back Gandir's ring.”

    - “Sure, I'll help.” → [jan_default14](#d-jan_default14)
    - “Can you tell me the story again?” → [jan_background](#d-jan_background)
    - “Never mind, goodbye.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `jan` · Data from v0.8.18</small>
