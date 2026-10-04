# ![](../assets/icons/monsters/monsters_ld1_11.png){ .sprite } Unkorh

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

## Found on

- [guynmart_main_2](../maps/guynmart_main_2.md)

## Quests

- [Roses](../quests/guynmart.md): stages 40

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_steward_10"></span>**`guynmart_steward_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [guynmart_steward_20](#d-guynmart_steward_20)

    <span id="d-guynmart_steward_20"></span>**`guynmart_steward_20`** Unkorh: “Hello - I am Unkorh, Steward of Guynmart Castle. I have never seen you here before. Are you looking for something?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)
    - “Eh ... I...” → [guynmart_steward_22](#d-guynmart_steward_22)

    <span id="d-guynmart_steward_30"></span>**`guynmart_steward_30`** Unkorh: “The cook shall give you some bread. And he can provide you with further provisions, if you can pay for them.” — **effects:** sets stage 40 of [Roses](../quests/guynmart.md#stage-40)

    - Next → [guynmart_steward_32](#d-guynmart_steward_32)

    <span id="d-guynmart_steward_40"></span>**`guynmart_steward_40`** Unkorh: “You have a message for our Lord?”

    - “Yes.” → [guynmart_steward_42](#d-guynmart_steward_42)

    <span id="d-guynmart_steward_50"></span>**`guynmart_steward_50`** Unkorh: “Lady Hannah is not in the mood to receive people. Something else?”

    - “Eh ... I...” → [guynmart_steward_22](#d-guynmart_steward_22)
    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “No, thank you, I will leave now.” → *conversation ends*

    <span id="d-guynmart_steward_22"></span>**`guynmart_steward_22`** Unkorh: “Stop stuttering, kid. What do you want?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)

    <span id="d-guynmart_steward_32"></span>**`guynmart_steward_32`** Unkorh: “Take the left stairway and ask for Hofala, our cook.”

    - “Thank you. I will go upstairs.” → *conversation ends*

    <span id="d-guynmart_steward_42"></span>**`guynmart_steward_42`** Unkorh: “Lord Guynmart is uproad tending to urgent affairs. I expect him back tomorrow.”

    - Next → [guynmart_steward_44](#d-guynmart_steward_44)

    <span id="d-guynmart_steward_44"></span>**`guynmart_steward_44`** Unkorh: “Deliver your message to me. I will pass it to Lord Guynmart when he returns.”

    - “Eh, Guynmart shall ... he...” → [guynmart_steward_45](#d-guynmart_steward_45)
    - “I have orders to give it directly to Lord Guynmart.” → [guynmart_steward_46](#d-guynmart_steward_46)

    <span id="d-guynmart_steward_45"></span>**`guynmart_steward_45`** Unkorh: “I don't believe a single word you say. Don't waste my time. I have important things to do.”


    <span id="d-guynmart_steward_46"></span>**`guynmart_steward_46`** Unkorh: “You have? Then you must wait. Leave now and come back tomorrow.”

    - “Wait!” → [guynmart_steward_48](#d-guynmart_steward_48)

    <span id="d-guynmart_steward_48"></span>**`guynmart_steward_48`** Unkorh: “Yes?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guynmart_steward2` · Data from v0.8.18</small>
