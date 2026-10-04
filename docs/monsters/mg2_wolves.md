# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Galmore wolf

| Stat | Value |
|---|---|
| Class | animal |
| HP | 251 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 3 |
| Damage | 15 to 20 |
| Attack chance | 177 |
| Block chance | 153 |
| Damage resistance | 0 |
| Critical skill | 10 |
| Critical multiplier | 2.0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 to 3 |
| [Gold coins](../items/gold.md) | 10% | 1 to 21 |

## Found on

- [galmore_54](../maps/galmore_54.md)
- [galmore_55](../maps/galmore_55.md)
- [galmore_64](../maps/galmore_64.md)

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stages 200
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 70

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mg2_wolves"></span>**`mg2_wolves`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Wolfpack's animal hide](../items/packhide.md))* → [mg2_wolves_1](#d-mg2_wolves_1)
    - branch 2 → [mg2_wolves_2](#d-mg2_wolves_2)

    <span id="d-mg2_wolves_1"></span>**`mg2_wolves_1`** Galmore wolf: “Grrr. You look like a grrreat wolf, but smell two-leggish.”

    - “Grrr, grrr” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “I am the big bad wolf from the stories. Fear me!” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “Move out of my way!” → *NPC leaves*

    <span id="d-mg2_wolves_2"></span>**`mg2_wolves_2`** Galmore wolf: “Grrroarrrr! It's a two-leg!” — **effects:** faction “mg2_wolves_faction” set to -666

    - “Attack!” → *fight starts*

    <span id="d-mg2_wolves_10"></span>**`mg2_wolves_10`** Galmore wolf: “You may go thrrrough herrre. No tarrrrying.” — **effects:** sets stage 200 of [Unusual experiences and achievements](../quests/achievements.md#stage-200)

    - “Agrrreed.” → *conversation ends*
    - “I am hungrrry.” *(if NOT reached stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_20](#d-mg2_wolves_20)
    - “I am hungrrry.” *(if reached stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_30](#d-mg2_wolves_30)

    <span id="d-mg2_wolves_20"></span>**`mg2_wolves_20`** Galmore wolf: “We can prrrovide you with good rrraw meat.”

    - “Do.” → [mg2_wolves_22](#d-mg2_wolves_22)
    - “No, thank you.” → *conversation ends*

    <span id="d-mg2_wolves_30"></span>**`mg2_wolves_30`** Galmore wolf: “We've alrrready given you. Now go.”

    - “Grrr.” → *conversation ends*
    - “That was looong ago. Long forrrgotten.” *(if 100 rounds passed since timer “mg2_wolves”)* → [mg2_wolves_40](#d-mg2_wolves_40)

    <span id="d-mg2_wolves_22"></span>**`mg2_wolves_22`** Galmore wolf: “Much grrreat meat. Twenty fourrr bites.” — **effects:** sets stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70), gives 24× [Meat](../items/meat.md), starts timer “mg2_wolves”

    - “Tha... I mean grrr.” → *conversation ends*

    <span id="d-mg2_wolves_40"></span>**`mg2_wolves_40`** Galmore wolf: “Parrrasite.”

    - “What?” → [mg2_wolves_42](#d-mg2_wolves_42)

    <span id="d-mg2_wolves_42"></span>**`mg2_wolves_42`** Galmore wolf: “Nothing. OK, look herrre.”

    - Next → [mg2_wolves_22](#d-mg2_wolves_22)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `mg2_wolves` · Data from v0.8.18</small>
