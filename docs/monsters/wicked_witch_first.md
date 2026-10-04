# ![](../assets/icons/monsters/monsters_phoenix01_8.png){ .sprite } Bonicksa

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 229 |
| Max AP | 12 |
| Attack cost | 4 |
| Move cost | 3 |
| Damage | 13 to 15 |
| Attack chance | 187 |
| Block chance | 152 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## On hit

- **On target:** Rootsnare (magnitude 1, 3 rounds, 25% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Music box](../items/music_box.md) | 100% | 1 |

## Found on

- [witch_house](../maps/witch_house.md)

## Quests

- [A Wicked witch](../quests/wicked_witch.md): stages 50

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-wicked_witch_first_selector"></span>**`wicked_witch_first_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-40) is 40)* → [wicked_witch_first_10](#d-wicked_witch_first_10)
    - Next *(if latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-50) is 50)* → [wicked_witch_first_30](#d-wicked_witch_first_30)
    - Next *(if latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-55) is 55)* → [wicked_witch_first_45](#d-wicked_witch_first_45)

    <span id="d-wicked_witch_first_10"></span>**`wicked_witch_first_10`** Bonicksa: “Oh my, what have we here? Another brave soul seeking to challenge me?”

    - “[While backing up] Me? No ma'am. I just wandered into the wrong house. Please don't hurt me.” → *conversation ends*
    - “Halt, foul witch! Your reign of darkness ends here!” → [wicked_witch_first_20](#d-wicked_witch_first_20)

    <span id="d-wicked_witch_first_30"></span>**`wicked_witch_first_30`** Bonicksa: “Oh, the "confident child". Please leave me to my business.”


    <span id="d-wicked_witch_first_45"></span>**`wicked_witch_first_45`** Bonicksa: “Oh, this fight will be fun ... for me that is.”

    - “I won't hesitate! Take this!” → *fight starts*

    <span id="d-wicked_witch_first_20"></span>**`wicked_witch_first_20`** Bonicksa: “And with such polite manners too. Come. Come. Take a seat.”

    - “Your tricks won't work on me. Prepare to meet your end!” → [wicked_witch_first_40](#d-wicked_witch_first_40)
    - “Witches don't bother me. I'll leave you be.” → [wicked_witch_first_25](#d-wicked_witch_first_25)

    <span id="d-wicked_witch_first_40"></span>**`wicked_witch_first_40`** Bonicksa: “[laughs] How amusing. You're not the first to try, and you won't be the last. But do go ahead, if you must.”

    - “I won't hesitate! Take this!” → *fight starts*

    <span id="d-wicked_witch_first_25"></span>**`wicked_witch_first_25`** Bonicksa: “How intriguing. Such confidence in your path. We shall see, won't we?” — **effects:** sets stage 50 of [A Wicked witch](../quests/wicked_witch.md#stage-50), starts timer “wicked_witch_despawn_timer”




## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wicked_witch_first.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wicked_witch_first.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wicked_witch_first.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wicked_witch_first.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `wicked_witch_first` · Data from v0.8.18</small>
