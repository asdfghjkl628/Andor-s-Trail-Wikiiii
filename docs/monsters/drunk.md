# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Drunk

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

- [crossglen_hall](../maps/crossglen_hall.md)
- [fallhaven_tavern](../maps/fallhaven_tavern.md)
- [loneford3](../maps/loneford3.md)
- [loneford6](../maps/loneford6.md)

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-drunk1"></span>**`drunk1`** Drunk: “Drink drink drink, drink some more. Drink drink drink 'til you're on the floor. Hey kid, wanna join us in our drinking game?”

    - “No thanks.” → [drunk1a](#d-drunk1a)
    - “Maybe some other time.” → *conversation ends*

    <span id="d-drunk1a"></span>**`drunk1a`** Drunk: “Heeeey - come on. Don't be such a spoilsport.”

    - “Maybe some other time.” → *conversation ends*
    - “Well, if you really want to. But I have a new and definitive game for you. Here, drink this. [Give a bottle of weak…” *(if hand over 1× [Weak poison](../items/pot_poison_weak.md))* → [drunk1b](#d-drunk1b)

    <span id="d-drunk1b"></span>**`drunk1b`** Drunk: “Ohh ... [glug glug]”

    - Next → [drunk1c](#d-drunk1c)

    <span id="d-drunk1c"></span>**`drunk1c`** Drunk: “What an interesting ... [glug]”

    - Next → [drunk1d](#d-drunk1d)

    <span id="d-drunk1d"></span>**`drunk1d`** Drunk: “... taste [falls over]”

    - “Yes, really. A unique taste. And final - bye.” → [drunk1e](#d-drunk1e)

    <span id="d-drunk1e"></span>**`drunk1e`** *(silent check: the first matching branch below is taken)* — **effects:** faction “drunk1” +1

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 5 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `drunk` · Data from v0.8.18</small>
