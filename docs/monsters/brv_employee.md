# ![](../assets/icons/monsters/monsters_ld1_34.png){ .sprite } Stebbarik

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 5 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [brimhaven_employee](../maps/brimhaven_employee.md)

## Quests

- [Work for debts](../quests/brv_employee.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Stebbarik. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_employee.json" data-npc="Stebbarik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_employee"></span>**`brv_employee`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90))* → [brv_employee_90](#d-brv_employee_90)
    - branch 2 *(if reached stage 40 of [Work for debts](../quests/brv_employee.md#stage-40))* → [brv_employee_40](#d-brv_employee_40)
    - branch 3 *(if reached stage 30 of [Work for debts](../quests/brv_employee.md#stage-30))* → [brv_employee_30](#d-brv_employee_30)
    - branch 4 *(if reached stage 10 of [Work for debts](../quests/brv_employee.md#stage-10))* → [brv_employee_10](#d-brv_employee_10)
    - branch 5 → [brv_employee_01](#d-brv_employee_01)

    <span id="d-brv_employee_90"></span>**`brv_employee_90`** Stebbarik: “Thank you for your help!”

    - “Was a pleasure.” → *conversation ends*

    <span id="d-brv_employee_40"></span>**`brv_employee_40`** Stebbarik: “Did you start working already?”

    - “Yes. It is hard work, really.” → *conversation ends*

    <span id="d-brv_employee_30"></span>**`brv_employee_30`** Stebbarik: “Did you talk to Gnossath?”

    - “Yes. He wants me to carry heavy boulders.” → *conversation ends*

    <span id="d-brv_employee_10"></span>**`brv_employee_10`** Stebbarik: “Did you talk to Gnossath?”

    - “Not yet.” → *conversation ends*

    <span id="d-brv_employee_01"></span>**`brv_employee_01`** Stebbarik: “Ooh. Oooooh!”

    - “Hey, what's the matter with you?” → [brv_employee_02](#d-brv_employee_02)

    <span id="d-brv_employee_02"></span>**`brv_employee_02`** Stebbarik: “I feel so bad.”

    - “Looks like a bit of a fever. Just stay in bed for a few days.” → [brv_employee_03](#d-brv_employee_03)

    <span id="d-brv_employee_03"></span>**`brv_employee_03`** Stebbarik: “But I can't! I mustn't! Gnossath would kill me.”

    - “Gnossath would kill you? Why?” → [brv_employee_04](#d-brv_employee_04)

    <span id="d-brv_employee_04"></span>**`brv_employee_04`** Stebbarik: “I am working for him.”

    - Next → [brv_employee_05](#d-brv_employee_05)

    <span id="d-brv_employee_05"></span>**`brv_employee_05`** Stebbarik: “He lent me money, so that I could afford this house. But no work - no money. I fear that if I can't pay my debts, Gnossath will take my house.”

    - “Maybe I could help you? I could do your work.” → [brv_employee_06](#d-brv_employee_06)
    - “That's the way it goes, man. Have a nice day.” → *conversation ends*

    <span id="d-brv_employee_06"></span>**`brv_employee_06`** Stebbarik: “You would do that? Oh, thank you! Thank you!” — **effects:** sets stage 10 of [Work for debts](../quests/brv_employee.md#stage-10)

    - “And you - get healthy again!” → *conversation ends*
    - “I have too good a heart.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_employee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_employee` · Data from v0.8.18</small>
