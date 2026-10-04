# ![](../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite } Agitated ghost

| Stat | Value |
|---|---|
| Class | undead |
| HP | 159 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 10 to 15 |
| Attack chance | 80 |
| Block chance | 90 |
| Damage resistance | 3 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [brightport_grave](../maps/brightport_grave.md)

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 238, 239, 241

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_ghost"></span>**`brightport_ghost`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 241 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-241)

    - Next *(if reached stage 239 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-239))* → [brightport_ghost8](#d-brightport_ghost8)
    - Next *(if NOT reached stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost1](#d-brightport_ghost1)
    - Next *(if reached stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost6](#d-brightport_ghost6)

    <span id="d-brightport_ghost8"></span>**`brightport_ghost8`** Agitated ghost: “Vengeance, vengeance!” — **effects:** sets stage 239 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-239)

    - “I promise I will find a way to put you to rest properly.” → *conversation ends*
    - “You make no sense cursed creature, I will put you to rest now.” → *fight starts*

    <span id="d-brightport_ghost1"></span>**`brightport_ghost1`** [Agitated ghost](../monsters/brightport_ghost.md): “You scoundrel dogs of Feygard, how dare you disturb the rest of a knight of Nor City!”

    - Next → [brightport_ghost2](#d-brightport_ghost2)

    <span id="d-brightport_ghost6"></span>**`brightport_ghost6`** [Agitated ghost](../monsters/brightport_ghost.md): “The blood we shed for the Kingdom was in vain.”

    - Next → [brightport_ghost7](#d-brightport_ghost7)

    <span id="d-brightport_ghost2"></span>**`brightport_ghost2`** [Drendolas](../monsters/brightport_studentghost1.md): “Well actually I'm from Remgard and my friend over there is from...”

    - Next → [brightport_ghost3](#d-brightport_ghost3)

    <span id="d-brightport_ghost7"></span>**`brightport_ghost7`** [Agitated ghost](../monsters/brightport_ghost.md): “It was stolen to birth this curse, and now we cannot rest!”

    - Next → [brightport_ghost8](#d-brightport_ghost8)

    <span id="d-brightport_ghost3"></span>**`brightport_ghost3`** [Agitated ghost](../monsters/brightport_ghost.md): “Silence! No more of your lies... You used me!”

    - “It's time I put you to rest. [Fight.]” → [brightport_ghost4](#d-brightport_ghost4)
    - “What are you talking about?” → [brightport_ghost5](#d-brightport_ghost5)

    <span id="d-brightport_ghost4"></span>**`brightport_ghost4`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8, sets stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238)

    - branch 1 → *fight starts*

    <span id="d-brightport_ghost5"></span>**`brightport_ghost5`** [Dummy NPC](../monsters/none.md): “The two kids sneak past the ghost and leave in a hurry.” — **effects:** sets stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238), removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8

    - Next → [brightport_ghost6](#d-brightport_ghost6)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightport_ghost` · Data from v0.8.18</small>
