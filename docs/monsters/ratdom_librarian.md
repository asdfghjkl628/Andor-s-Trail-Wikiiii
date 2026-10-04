# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Librarian

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 60 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 5 |
| Damage | 10 to 30 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Ratcave Torch](../items/ratdom_torch.md) | 50% | 1 |
| [Gold coins](../items/gold.md) | 50% | 30 to 80 |
| [Nasty looking book](../items/ratdom_book.md) | 100% | 1 |

## Found on

- [ratdom_maze_611](../maps/ratdom_maze_611.md)

## Quests

- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 93, 95

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_librarian"></span>**`ratdom_librarian`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-95))* → [ratdom_librarian_42](#d-ratdom_librarian_42)
    - Next → [ratdom_librarian_2](#d-ratdom_librarian_2)

    <span id="d-ratdom_librarian_42"></span>**`ratdom_librarian_42`** [Dummy NPC](../monsters/none.md): “The librarian is completely absorbed in his new book.”


    <span id="d-ratdom_librarian_2"></span>**`ratdom_librarian_2`** Librarian: “Andor! Good that you are back at last!”

    - “I am $playername. You have confused me with my brother.” → [ratdom_librarian_10](#d-ratdom_librarian_10)
    - “Indeed. Any news?” → [ratdom_librarian_20](#d-ratdom_librarian_20)
    - “Here I have a new book for your library.” *(if hand over 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_40](#d-ratdom_librarian_40)

    <span id="d-ratdom_librarian_10"></span>**`ratdom_librarian_10`** Librarian: “Yes. I see it now. Please leave. My master is not present today.”

    - “Andor - master? What ... Where is my brother?” → [ratdom_librarian_12](#d-ratdom_librarian_12)

    <span id="d-ratdom_librarian_20"></span>**`ratdom_librarian_20`** Librarian: “I am not sure. Today I hear footsteps of strangers in the corridors.”

    - “[muttering] Probably mine.” → [ratdom_librarian_22](#d-ratdom_librarian_22)
    - “Then what are you waiting for? Go and look who is wandering through our passages!” → [ratdom_librarian_30](#d-ratdom_librarian_30)
    - “Nonsense. Strangers would never find this secret library.” → [ratdom_librarian_24](#d-ratdom_librarian_24)

    <span id="d-ratdom_librarian_40"></span>**`ratdom_librarian_40`** Librarian: “Oh! What a wonder! I always wanted to have a copy of that wonderful book! Here, take this special bone as a token of my everlasting thanks. [gives leg bone of a rat]” — **effects:** gives 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), sets stage 95 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-95)

    - “A lousy bone for this valuable book?!” → [ratdom_librarian_42](#d-ratdom_librarian_42)

    <span id="d-ratdom_librarian_12"></span>**`ratdom_librarian_12`** Librarian: “That does not concern you. Mind your own business and leave now!”

    - “Bye.” → *conversation ends*
    - “Tell me about Andor, or ...” → [ratdom_librarian_14](#d-ratdom_librarian_14)

    <span id="d-ratdom_librarian_22"></span>**`ratdom_librarian_22`** Librarian: “What? You are the stranger! You are not allowed to be here!”

    - “It's fine, I'm going already.” → *conversation ends*
    - “Andor is my brother. I'm going to look for a clue to his whereabouts now. You won't stop me from doing that.” → *fight starts*

    <span id="d-ratdom_librarian_30"></span>**`ratdom_librarian_30`** Librarian: “As you command me - I'll be right back.”

    - “Take your time, better to be be thorough!” → [ratdom_librarian_32](#d-ratdom_librarian_32)

    <span id="d-ratdom_librarian_24"></span>**`ratdom_librarian_24`** Librarian: “You're right, I'm sure I only see pipe dreams.”

    - Next *(if carry 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_26](#d-ratdom_librarian_26)

    <span id="d-ratdom_librarian_14"></span>**`ratdom_librarian_14`** Librarian: “Or what? Attack? Hahaha!”

    - “You'll soon stop laughing.” → *fight starts*
    - “Just you wait when I come back.” → *conversation ends*

    <span id="d-ratdom_librarian_32"></span>**`ratdom_librarian_32`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 93 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-93)

    - Next → *NPC leaves*

    <span id="d-ratdom_librarian_26"></span>**`ratdom_librarian_26`** Librarian: “If only I had something to read. Something new, that I haven't read twenty times already.”

    - “Here I have a new book for your library.” *(if hand over 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_40](#d-ratdom_librarian_40)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_librarian` · Data from v0.8.18</small>
