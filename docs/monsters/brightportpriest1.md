# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Stiyl

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 5 |
| [Regular potion of health](../items/health.md) | 100% | 5 |
| [Major potion of health](../items/health_major2.md) | 100% | 5 |

## Found on

- [brightport_temple1](../maps/brightport_temple1.md)

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 10

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_priest_1"></span>**`brightport_priest_1`** [Stiyl](../monsters/brightportpriest1.md): “Hello there, child. Are you perhaps interested in following the Shadow?”

    - “I'm searching for my brother, Andor. Have you seen him?” → [brightport_priest_1_reply1](#d-brightport_priest_1_reply1)
    - “How do I follow the Shadow?” → [brightport_priest_1_reply2](#d-brightport_priest_1_reply2)
    - “Could you provide me with supplies?” → *shop opens*
    - “I've visited the chapel, and for a town of this size, it's surprisingly small.” *(if reached stage 5 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-5); NOT reached stage 10 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-10))* → [brightport_priest_story](#d-brightport_priest_story)
    - “Can you tell me the story about the temple again?” *(if reached stage 10 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-10))* → [brightport_priest_story1](#d-brightport_priest_story1)
    - “I heard a rumor from one of the guards about a place called the Water Temple.” *(if reached stage 251 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-251); NOT reached stage 10 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-10))* → [brightport_priest_story1](#d-brightport_priest_story1)
    - “All this Shadow stuff. What a bunch of nonsense.” → [brightport_priest_1_reply](#d-brightport_priest_1_reply)

    <span id="d-brightport_priest_1_reply1"></span>**`brightport_priest_1_reply1`** [Stiyl](../monsters/brightportpriest1.md): “I'm sorry, there are many students from the academy playing, and their faces are not imprinted on my memory.”

    - “Can you tell me how to follow the Shadow?” → [brightport_priest_1_reply2](#d-brightport_priest_1_reply2)
    - “Thanks. I must go now.” → [brightportpriest_1_reply1goodbye](#d-brightportpriest_1_reply1goodbye)

    <span id="d-brightport_priest_1_reply2"></span>**`brightport_priest_1_reply2`** [Stiyl](../monsters/brightportpriest1.md): “The Shadow speaks to us. It watches over our thoughts, and guides us.”

    - Next → [brightport_priest_1_reply2_1](#d-brightport_priest_1_reply2_1)

    <span id="d-brightport_priest_story"></span>**`brightport_priest_story`** [Stiyl](../monsters/brightportpriest1.md): “Behind it, lies a story.”

    - Next → [brightport_priest_story1](#d-brightport_priest_story1)

    <span id="d-brightport_priest_story1"></span>**`brightport_priest_story1`** [Stiyl](../monsters/brightportpriest1.md): “In the past, the chapel was only a minor shrine. The people of Brightport used to worship the Shadow at the great Water Temple.” — **effects:** sets stage 10 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-10)

    - Next → [brightport_priest_story2](#d-brightport_priest_story2)

    <span id="d-brightport_priest_1_reply"></span>**`brightport_priest_1_reply`** [Stiyl](../monsters/brightportpriest1.md): “Even if you believe so, the Shadow most certainly watches over you.”


    <span id="d-brightportpriest_1_reply1goodbye"></span>**`brightportpriest_1_reply1goodbye`** [Stiyl](../monsters/brightportpriest1.md): “May the Shadow assist you on your journey.”


    <span id="d-brightport_priest_1_reply2_1"></span>**`brightport_priest_1_reply2_1`** [Stiyl](../monsters/brightportpriest1.md): “To follow the Shadow, one must listen to its voice and direct their gaze toward its wisdom.”

    - Next → [brightport_priest_1_reply2_2](#d-brightport_priest_1_reply2_2)

    <span id="d-brightport_priest_story2"></span>**`brightport_priest_story2`** [Stiyl](../monsters/brightportpriest1.md): “But many years ago, calamity struck. A race of lizardmen, uncannily similar to us in form but beastly in nature, engulfed the islands of the lake.”

    - Next → [brightport_priest_story3](#d-brightport_priest_story3)

    <span id="d-brightport_priest_1_reply2_2"></span>**`brightport_priest_1_reply2_2`** [Stiyl](../monsters/brightportpriest1.md): “Walk the path of one's destiny, and as the challenges upon your journey unfold, follow the guiding voice of the Shadow.”

    - “Thanks, may the Shadow be with you.” → *conversation ends*
    - “None of this makes any sense, but sure.” → *conversation ends*

    <span id="d-brightport_priest_story3"></span>**`brightport_priest_story3`** [Stiyl](../monsters/brightportpriest1.md): “The temple was ransacked, and not a single one of its acolytes or servants returned. The nobles now, as back then, are still preoccupied with trifling matters. I'm afraid we will never reclaim our holy place.”

    - “Could you tell me more about the lizardmen?” → [brightport_priest_story4](#d-brightport_priest_story4)
    - “Is there something I could do to help?” → [brightport_priest](#d-brightport_priest)
    - “Thank you for telling me this story.” → *conversation ends*

    <span id="d-brightport_priest_story4"></span>**`brightport_priest_story4`** [Stiyl](../monsters/brightportpriest1.md): “They carry crudely made weapons and have distinctive blood-red scales. They attack travelers along the shores of the bright lake.”

    - Next → [brightport_priest_story5](#d-brightport_priest_story5)

    <span id="d-brightport_priest"></span>**`brightport_priest`** Stiyl: “Unless you could travel to Feygard and speak with the Lord of Brightport. I'm afraid not my child.”

    - “Thanks for telling me this story. I'll go now.” → *conversation ends*

    <span id="d-brightport_priest_story5"></span>**`brightport_priest_story5`** [Stiyl](../monsters/brightportpriest1.md): “I have heard stories from adventurers of lizardmen of different colors that display more reason than the red-scaled ones. But stay safe, my child.”

    - “Thank you for telling me this story.” → *conversation ends*
    - “Thank you, Shadow be with you.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportpriest1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportpriest1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportpriest1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportpriest1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportpriest1` · Data from v0.8.18</small>
