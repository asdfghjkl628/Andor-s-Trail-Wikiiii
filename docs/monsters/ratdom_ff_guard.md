# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard patrol watch

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 80 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 12 to 17 |
| Attack chance | 170 |
| Block chance | 180 |
| Damage resistance | 3 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 2 to 9 |

## Found on

- [ratdom_maze_412](../maps/ratdom_maze_412.md)

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_ff_guard"></span>**`ratdom_ff_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20))* → [ratdom_ff_guard_20](#d-ratdom_ff_guard_20)
    - branch 2 → [ratdom_ff_guard_10](#d-ratdom_ff_guard_10)

    <span id="d-ratdom_ff_guard_20"></span>**`ratdom_ff_guard_20`** Feygard patrol watch: “Hey, you!”

    - “Who, me?” → [ratdom_ff_guard_30](#d-ratdom_ff_guard_30)
    - “Hey, you!” → [ratdom_ff_guard_30](#d-ratdom_ff_guard_30)

    <span id="d-ratdom_ff_guard_10"></span>**`ratdom_ff_guard_10`** Feygard patrol watch: “Go away!”


    <span id="d-ratdom_ff_guard_30"></span>**`ratdom_ff_guard_30`** Feygard patrol watch: “I know your face!”

    - Next → [ratdom_ff_guard_40](#d-ratdom_ff_guard_40)

    <span id="d-ratdom_ff_guard_40"></span>**`ratdom_ff_guard_40`** Feygard patrol watch: “You had made me leave my post in front of the Foaming Flask!” — **effects:** removes monsters from road1

    - “Oh. It's you ...” → [ratdom_ff_guard_42](#d-ratdom_ff_guard_42)

    <span id="d-ratdom_ff_guard_42"></span>**`ratdom_ff_guard_42`** Feygard patrol watch: “Surprised? I'm sure you didn't think we'd see each other again.”

    - Next → [ratdom_ff_guard_50](#d-ratdom_ff_guard_50)

    <span id="d-ratdom_ff_guard_50"></span>**`ratdom_ff_guard_50`** Feygard patrol watch: “I have lost everything because of this! Above all, my honor!”

    - “What honor?” → [ratdom_ff_guard_60](#d-ratdom_ff_guard_60)
    - “Sorry.” → [ratdom_ff_guard_60](#d-ratdom_ff_guard_60)

    <span id="d-ratdom_ff_guard_60"></span>**`ratdom_ff_guard_60`** Feygard patrol watch: “I took refuge in this filthy cave to be safe from the guards of Feygard.”

    - Next → [ratdom_ff_guard_70](#d-ratdom_ff_guard_70)

    <span id="d-ratdom_ff_guard_70"></span>**`ratdom_ff_guard_70`** Feygard patrol watch: “You will pay for it now!”

    - “But you were so stupid ...” → *fight starts*
    - “Attack!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_ff_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_ff_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_ff_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_ff_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_ff_guard` · Data from v0.8.18</small>
