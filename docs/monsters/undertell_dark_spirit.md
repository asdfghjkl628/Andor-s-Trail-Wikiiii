# ![](../assets/icons/monsters/monsters_newb_1_686.png){ .sprite } Dark spirit

| Stat | Value |
|---|---|
| Class | demon |
| HP | 509 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 3 |
| Damage | 9 to 10 |
| Attack chance | 155 |
| Block chance | 142 |
| Damage resistance | 6 |
| Critical skill | 3 |
| Critical multiplier | 2.0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **Heal HP:** 2 to 4

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 75 to 110 |
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 4 to 8 |
| [Elytharan gloves](../items/elytharan_gloves.md) | 100% | 1 |

## Found on

- [galmore_32](../maps/galmore_32.md)

## Quests

- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stages 4

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dark spirit. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/galmore_dark_spirit_selector.json" data-npc="Dark spirit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-galmore_dark_spirit_selector"></span>**`galmore_dark_spirit_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 4 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-4))* → *fight starts*
    - branch 2 → [galmore_dark_spirit_10](#d-galmore_dark_spirit_10)

    <span id="d-galmore_dark_spirit_10"></span>**`galmore_dark_spirit_10`** Dark spirit: “Destroy me? Foolish mortal! I am older than your bloodline, stronger than your resolve. You will break, just like the others. Their despair feeds me, and yours will be no different!”

    - Next → [galmore_dark_spirit_11](#d-galmore_dark_spirit_11)

    <span id="d-galmore_dark_spirit_11"></span>**`galmore_dark_spirit_11`** [Dummy NPC](../monsters/none.md): “The spirit swirls with dark energy, causing the ground to tremble as it prepares to attack.”

    - Next → [galmore_dark_spirit_20](#d-galmore_dark_spirit_20)

    <span id="d-galmore_dark_spirit_20"></span>**`galmore_dark_spirit_20`** [Dark spirit](../monsters/undertell_dark_spirit.md): “Let me show you what true suffering feels like. You will know despair, and your name will be forgotten in the darkness of my power!” — **effects:** spawns monsters on galmore_32, sets stage 4 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-4)

    - “Let me show you the darkness of my power!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undertell_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `undertell_dark_spirit` · Data from v0.8.18</small>
