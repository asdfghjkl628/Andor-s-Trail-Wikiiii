# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Watchman

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

- [fallhaven_ne](../maps/fallhaven_ne.md)

## Quests

- [A path to the Duleian Road](../quests/pathway_fallhaven.md): stages 10, 60

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guard_pathway"></span>**`guard_pathway`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50))* → [guard_pathway_5](#d-guard_pathway_5)
    - branch 2 *(if reached stage 10 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10))* → [guard_pathway_6](#d-guard_pathway_6)
    - branch 3 → [guard_pathway_0](#d-guard_pathway_0)

    <span id="d-guard_pathway_5"></span>**`guard_pathway_5`** Watchman: “Hello again. It seems like you have sorted things out. Now the passage isn't blocked anymore. You have my gratitude for doing that.” — **effects:** sets stage 60 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-60)

    - “You're welcome. I'm glad the way is opened again!” → *conversation ends*

    <span id="d-guard_pathway_6"></span>**`guard_pathway_6`** Watchman: “Hello kid. Did you make any progress on your task?”

    - “Unfortunately not.” → *conversation ends*
    - “I wasn't able to convince the warden but I'm going to talk to the woodcutter now.” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-20) is 20; NOT latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-30) is 30)* → [guard_pathway_7](#d-guard_pathway_7)
    - “The woodcutter is going to help me if I retrieve his axe!” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-30) is 30)* → [guard_pathway_8](#d-guard_pathway_8)

    <span id="d-guard_pathway_0"></span>**`guard_pathway_0`** Watchman: “Halt! No one is allowed down the pathway to the Duleian Road!”

    - “Why not?” → [guard_pathway_1](#d-guard_pathway_1)
    - “Never mind. Shadow be with you.” → *conversation ends*
    - “Never mind. Goodbye.” → *conversation ends*

    <span id="d-guard_pathway_7"></span>**`guard_pathway_7`** Watchman: “Well good luck with that. Maybe you can convince him.”

    - “I hope so.” → *conversation ends*

    <span id="d-guard_pathway_8"></span>**`guard_pathway_8`** Watchman: “That sounds great! Good luck!”

    - “Goodbye.” → *conversation ends*

    <span id="d-guard_pathway_1"></span>**`guard_pathway_1`** Watchman: “Because a storm recently knocked over some trees that now block the passage. A villager even got hurt. And now the woodcutter that should be responsible doesn't want to cut the fallen trees away.”

    - “Why doesn't he want to do this work?” → [guard_pathway_2](#d-guard_pathway_2)

    <span id="d-guard_pathway_2"></span>**`guard_pathway_2`** Watchman: “You're really curious kid... Well our superior, the guard captain, only wants to pay the woodcutter when he has done his work.”

    - “Maybe I could help?” → [guard_pathway_3](#d-guard_pathway_3)
    - “Well, this is your problem. Goodbye.” → *conversation ends*

    <span id="d-guard_pathway_3"></span>**`guard_pathway_3`** Watchman: “You? You're just a kid!”

    - “You're right, but I'd really love to be able to take this path.” → [guard_pathway_4](#d-guard_pathway_4)
    - “So what. I can help!” → [guard_pathway_4](#d-guard_pathway_4)

    <span id="d-guard_pathway_4"></span>**`guard_pathway_4`** Watchman: “OK, maybe you can be of use. Talk to the guard captain. Maybe you can convince him to pay the woodcutter first. But I have to warn you, he is a stubborn beast.” — **effects:** sets stage 10 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10)

    - “OK, thanks for your advice. I'm going to do that!” → *conversation ends*
    - “Pff, easy. I'll do it.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_pathway.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_pathway.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_pathway.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_pathway.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guard_pathway` · Data from v0.8.18</small>
