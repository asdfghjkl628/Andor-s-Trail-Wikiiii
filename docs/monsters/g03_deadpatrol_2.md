# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Dying Patrol

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

- [crackshot_hideout2](../maps/crackshot_hideout2.md)

## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stages 26, 27
- [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dying Patrol. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guild03_deadpatrol_2_1.json" data-npc="Dying Patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guild03_deadpatrol_2_1"></span>**`guild03_deadpatrol_2_1`** Dying Patrol: “Sar...gent. *gasps*.”

    - Next → [guild03_deadpatrol_2_2](#d-guild03_deadpatrol_2_2)

    <span id="d-guild03_deadpatrol_2_2"></span>**`guild03_deadpatrol_2_2`** Dying Patrol: “Y..you kid ... Argh! *spits up blood*. That guy is not ... Argh.”

    - “What guy?” *(if reached stage 40 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-40))* → [guild03_deadpatrol_2_was_second](#d-guild03_deadpatrol_2_was_second)
    - “What guy?” *(if NOT reached stage 40 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-40))* → [guild03_deadpatrol_2_was_first](#d-guild03_deadpatrol_2_was_first)

    <span id="d-guild03_deadpatrol_2_was_second"></span>**`guild03_deadpatrol_2_was_second`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 26 of [The ruthless Crackshot](../quests/Thieves03.md#stage-26)

    - branch 1 → [guild03_deadpatrol_2_3](#d-guild03_deadpatrol_2_3)

    <span id="d-guild03_deadpatrol_2_was_first"></span>**`guild03_deadpatrol_2_was_first`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 27 of [The ruthless Crackshot](../quests/Thieves03.md#stage-27)

    - branch 1 → [guild03_deadpatrol_2_3](#d-guild03_deadpatrol_2_3)

    <span id="d-guild03_deadpatrol_2_3"></span>**`guild03_deadpatrol_2_3`** Dying Patrol: “No ... he's not .... Agggh! [He has stopped breathing. I cannot do anything for him. Better to move on.]” — **effects:** removes monsters from crackshot_hideout2, sets stage 50 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-50)

    - “Shadow, embrace him ....” → *NPC leaves*
    - “I'll save your sergeant!” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `g03_deadpatrol_2` · Data from v0.8.18</small>
