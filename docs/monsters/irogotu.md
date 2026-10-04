# ![](../assets/icons/monsters/monsters_liches_0.png){ .sprite } Irogotu

| Stat | Value |
|---|---|
| Class | undead |
| HP | 61 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 10 |
| Damage | 2 to 5 |
| Attack chance | 50 |
| Block chance | 70 |
| Damage resistance | 4 |
| Critical skill | 40 |
| Critical multiplier | 3.0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Irogotu's necklace](../items/neck_irogotu.md) | 100% | 1 |
| [Gandir's ring](../items/ring_gandir.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 1 |

## Found on

- [jan_pitcave3](../maps/jan_pitcave3.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Irogotu. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/irogotu.json" data-npc="Irogotu" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-irogotu"></span>**`irogotu`** Irogotu: “Well hello there. Another adventurer coming to steal my bounty. This is MY CAVE. The treasure will be MINE!”

    - “Did you kill Gandir?” *(if reached stage 10 of [Fallen friends](../quests/jan.md#stage-10))* → [irogotu1](#d-irogotu1)

    <span id="d-irogotu1"></span>**`irogotu1`** Irogotu: “That whelp Gandir? He was in my way. I merely used him as a tool to dig deeper into the cave.”

    - Next → [irogotu2](#d-irogotu2)

    <span id="d-irogotu2"></span>**`irogotu2`** Irogotu: “Besides, I never really liked him anyway.”

    - “I guess he deserved to die. Did he have a ring on him?” → [irogotu3](#d-irogotu3)
    - “Jan mentioned something about a ring?” → [irogotu3](#d-irogotu3)

    <span id="d-irogotu3"></span>**`irogotu3`** Irogotu: “NO! You cannot have it. It's mine! And who are you anyway kid, coming down here to disturb me?!”

    - “I'm not a kid anymore! Now give me that ring!” → [irogotu4](#d-irogotu4)
    - “Give me that ring and we might both come out of here alive.” → [irogotu4](#d-irogotu4)

    <span id="d-irogotu4"></span>**`irogotu4`** Irogotu: “No. If you want it you will have to take it from me by force, and I should tell you that my powers are great. Besides, you probably wouldn't dare fight me anyway.”

    - “Very well, let's see who dies here.” → *fight starts*
    - “By the Shadow, Gandir will be avenged.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `irogotu` · Data from v0.8.18</small>
