# ![](../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite } Roundling

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 200 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 10 to 30 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [ratdom_maze_448](../maps/ratdom_maze_448.md)

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 960
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 13

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_roundling2"></span>**`ratdom_roundling2`** Roundling: “A thief who thinks to get through with our treasure, is due to give his life upon a strife, and all his stolen goods too.”

    - “Eh, let us think a minute.” → *conversation ends*
    - “Well, OK. We have no chance against so many roundlings.” → [ratdom_roundling2_10](#d-ratdom_roundling2_10)
    - “Never - attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)

    <span id="d-ratdom_roundling2_10"></span>**`ratdom_roundling2_10`** [Clevred](../monsters/ratdom_rat.md): “Coward! You didn't even try.”

    - “Never call me coward! Attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)
    - “They are too many for us, we would be killed. Let's give up the artifact.” → [ratdom_roundling2_12](#d-ratdom_roundling2_12)

    <span id="d-ratdom_roundling2_90"></span>**`ratdom_roundling2_90`** *(silent check: the first matching branch below is taken)* — **effects:** faction “fct_ratdom_roundling2” set to -10

    - branch 1 → *fight starts*

    <span id="d-ratdom_roundling2_12"></span>**`ratdom_roundling2_12`** Roundling: “Never! I'd rather die!”

    - “If you think so, then let's attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)
    - “Die you will, if you can't let go of it. I will leave it behind.” → [ratdom_roundling2_20](#d-ratdom_roundling2_20)

    <span id="d-ratdom_roundling2_20"></span>**`ratdom_roundling2_20`** Roundling: “I see. I thought you were braver. Go then, I don't want to see you again!” — **effects:** sets stage 960 of [Yellow is it](../quests/ratdom_quest.md#stage-960), clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_roundling2` · Data from v0.8.18</small>
