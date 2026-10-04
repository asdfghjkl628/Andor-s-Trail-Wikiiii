# ![](../assets/icons/monsters/monsters_rltiles2_89.png){ .sprite } Wise of the wells

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

- [ratdom_maze_768](../maps/ratdom_maze_768.md)

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 30
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 50

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_well_wise3"></span>**`ratdom_well_wise3`** Wise of the wells: “Omm...”

    - “Hi! I am $playername.” *(if NOT reached stage 50 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-50))* → [ratdom_well_wise3_10](#d-ratdom_well_wise3_10)
    - “Omm.” → [ratdom_well_wise3_20](#d-ratdom_well_wise3_20)

    <span id="d-ratdom_well_wise3_10"></span>**`ratdom_well_wise3_10`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 50 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-50)

    - branch 1 → [ratdom_well_wise3](#d-ratdom_well_wise3)

    <span id="d-ratdom_well_wise3_20"></span>**`ratdom_well_wise3_20`** Wise of the wells: “Ommmmm...”

    - “I am $playername. Who are you?” *(if NOT reached stage 50 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-50))* → [ratdom_well_wise3_10](#d-ratdom_well_wise3_10)
    - “Omm.” → [ratdom_well_wise3_10](#d-ratdom_well_wise3_10)
    - “Ommmmm...” → [ratdom_well_wise3_30](#d-ratdom_well_wise3_30)

    <span id="d-ratdom_well_wise3_30"></span>**`ratdom_well_wise3_30`** Wise of the wells: “Omm... ommm... ommmmm...”

    - “Omm... omm... omm...” → [ratdom_well_wise3_10](#d-ratdom_well_wise3_10)
    - “Omm... ommm... ommmmm...” → [ratdom_well_wise3_50](#d-ratdom_well_wise3_50)
    - “Omm... ommm... ommmmmm...” → [ratdom_well_wise3_10](#d-ratdom_well_wise3_10)

    <span id="d-ratdom_well_wise3_50"></span>**`ratdom_well_wise3_50`** Wise of the wells: “Very good. Finally a learned being in this rat hole.”

    - Next *(if NOT reached stage 30 of [Yellow is it](../quests/ratdom_quest.md#stage-30))* → [ratdom_well_wise3_52](#d-ratdom_well_wise3_52)

    <span id="d-ratdom_well_wise3_52"></span>**`ratdom_well_wise3_52`** Wise of the wells: “In gratitude for the great joy I give you this rat skull.” — **effects:** sets stage 30 of [Yellow is it](../quests/ratdom_quest.md#stage-30), gives 1× [Rat skull](../items/ratdom_rat_skelett_skull.md)

    - “Eh - nice, thank you.” → [ratdom_well_wise3_90](#d-ratdom_well_wise3_90)

    <span id="d-ratdom_well_wise3_90"></span>**`ratdom_well_wise3_90`** Wise of the wells: “Come again whenever you want. It is a nice diversion to talk with someone with a bit of brain at least.”




## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_well_wise3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_well_wise3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_well_wise3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_well_wise3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_well_wise3` · Data from v0.8.18</small>
