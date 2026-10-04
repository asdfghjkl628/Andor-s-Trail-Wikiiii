# ![](../assets/icons/monsters/monsters_ld1_95.png){ .sprite } Brightport guard

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

- [brightport5](../maps/brightport5.md)

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 232

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightportguard_1_selector"></span>**`brightportguard_1_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144); NOT reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 232 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-232))* → [brightportguard_afterhide](#d-brightportguard_afterhide)
    - Next *(if reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 232 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-232))* → [brightportguard_2](#d-brightportguard_2)
    - Next → [brightportguard_1](#d-brightportguard_1)

    <span id="d-brightportguard_afterhide"></span>**`brightportguard_afterhide`** Brightport guard: “Hey, did you not meet with my comrades? They came back from a patrol just now.” — **effects:** sets stage 232 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Uhh no, bye.” → *conversation ends*

    <span id="d-brightportguard_2"></span>**`brightportguard_2`** Brightport guard: “Hmm? I think I saw my comrades carry you away from this direction before...” — **effects:** sets stage 232 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Oops, gotta go.” → *conversation ends*

    <span id="d-brightportguard_1"></span>**`brightportguard_1`** Brightport guard: “Halt! If you value your life, stay off this path.” — **effects:** clears stage 232 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Ha, I can handle myself. Don't worry about me.” → [brightportguard_1reply](#d-brightportguard_1reply)
    - “What's wrong with this road?” → [brightportguard_1reply1](#d-brightportguard_1reply1)
    - “[Slip past him.]” → *conversation ends*

    <span id="d-brightportguard_1reply"></span>**`brightportguard_1reply`** [Brightport guard](../monsters/brightportguard2.md): “Sure, kid. You do seem to be carrying some shiny equipment. Just don't blame me if you get eaten by a scary lizardman.”

    - “Lizardmen?” → [brightportguard_1reply2](#d-brightportguard_1reply2)

    <span id="d-brightportguard_1reply1"></span>**`brightportguard_1reply1`** [Brightport guard](../monsters/brightportguard2.md): “If you go that way, all you'll find is a shack, some trees, and the mountain. What's really scary are the nasty lizardmen who occasionally stumble up on the shore.”

    - “Lizardmen?” → [brightportguard_1reply2](#d-brightportguard_1reply2)
    - “Guess I'll turn around.” → [brightportguard_1reply3](#d-brightportguard_1reply3)

    <span id="d-brightportguard_1reply2"></span>**`brightportguard_1reply2`** [Brightport guard](../monsters/brightportguard.md): “Terrifying, humanoid creatures with blood-red scales instead of skin, and the head of a giant Erumen lizard.”

    - Next → [brightportguard_1_reply4](#d-brightportguard_1_reply4)

    <span id="d-brightportguard_1reply3"></span>**`brightportguard_1reply3`** [Brightport guard](../monsters/brightportguard2.md): “Take care, and don't slack off in school, or else you'll end up slaying sewer rats down in Nor City. [laughs]”


    <span id="d-brightportguard_1_reply4"></span>**`brightportguard_1_reply4`** [Brightport guard](../monsters/brightportguard.md): “Just the thought gives me shivers.”

    - “Guess I'll go back.” → [brightportguard_1reply3](#d-brightportguard_1reply3)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportguard2` · Data from v0.8.18</small>
