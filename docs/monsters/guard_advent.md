# ![](../assets/icons/monsters/monsters_ld1_41.png){ .sprite } Guard

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

- [brimhaven3](../maps/brimhaven3.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guard_advent.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (19 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guard_advent"></span>**`guard_advent`** Guard: “I used to be an adventurer like you,”

    - Next → [guard_advent_2](#d-guard_advent_2)

    <span id="d-guard_advent_2"></span>**`guard_advent_2`** Guard: “Then I took an arrow in the knee.”

    - “Sorry for you.” → *conversation ends*
    - “That reminds me of a song.” *(if random chance (20%))* → [guard_advent_4](#d-guard_advent_4)
    - “I'm wondering, do you know anything about Lawellyn's death?” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [guard_advent_asd_10](#d-guard_advent_asd_10)

    <span id="d-guard_advent_4"></span>**`guard_advent_4`** Guard: “I think I know which song you are thinking of.”

    - “Shall we sing it together?” → [guard_advent_10](#d-guard_advent_10)

    <span id="d-guard_advent_asd_10"></span>**`guard_advent_asd_10`** Guard: “Death? The last I knew was that Arlish reported him missing.”


    <span id="d-guard_advent_10"></span>**`guard_advent_10`** Guard: “Mahna.”

    - “Mahna mahna?” → [guard_advent_12](#d-guard_advent_12)

    <span id="d-guard_advent_12"></span>**`guard_advent_12`** Guard: “I took an arrow ...”

    - “You took an arrow” → [guard_advent_14](#d-guard_advent_14)

    <span id="d-guard_advent_14"></span>**`guard_advent_14`** Guard: “... right in the knee.”

    - “right in your knee” → [guard_advent_16](#d-guard_advent_16)

    <span id="d-guard_advent_16"></span>**`guard_advent_16`** Guard: “I took an arrow.”

    - “You took an arrow, an arrow, an arrow, an evil dirty arrow in your knee.” → [guard_advent_20](#d-guard_advent_20)

    <span id="d-guard_advent_20"></span>**`guard_advent_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [guard_advent_22](#d-guard_advent_22)
    - branch 2 → [guard_advent_30](#d-guard_advent_30)

    <span id="d-guard_advent_22"></span>**`guard_advent_22`** Guard: “-”

    - “What?” → [guard_advent_30](#d-guard_advent_30)

    <span id="d-guard_advent_30"></span>**`guard_advent_30`** Guard: “I took an arrow ...”

    - “He took an arrow” → [guard_advent_32](#d-guard_advent_32)

    <span id="d-guard_advent_32"></span>**`guard_advent_32`** Guard: “... right in the knee.”

    - “right in his knee” → [guard_advent_34](#d-guard_advent_34)

    <span id="d-guard_advent_34"></span>**`guard_advent_34`** Guard: “I took an arrow.”

    - “He took an arrow, an arrow, an arrow, an evil dirty arrow in his knee.” → [guard_advent_40](#d-guard_advent_40)

    <span id="d-guard_advent_40"></span>**`guard_advent_40`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (25%))* → [guard_advent_12](#d-guard_advent_12)
    - branch 2 → [guard_advent_50](#d-guard_advent_50)

    <span id="d-guard_advent_50"></span>**`guard_advent_50`** Guard: “An adventurer like you,”

    - Next → [guard_advent_52](#d-guard_advent_52)

    <span id="d-guard_advent_52"></span>**`guard_advent_52`** Guard: “I took an arrow in the knee!”

    - Next → [guard_advent_54](#d-guard_advent_54)

    <span id="d-guard_advent_54"></span>**`guard_advent_54`** Guard: “adventunarrow, In the knee the arrow”

    - Next → [guard_advent_56](#d-guard_advent_56)

    <span id="d-guard_advent_56"></span>**`guard_advent_56`** Guard: “La be di bap bap ...”

    - Next → [guard_advent_58](#d-guard_advent_58)

    <span id="d-guard_advent_58"></span>**`guard_advent_58`** Guard: “Die be die be boo mbie La be di bap bap ...”

    - “What??” → [guard_advent_12](#d-guard_advent_12)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 18 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_advent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_advent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_advent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard_advent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `guard_advent` · Data from v0.8.18</small>
