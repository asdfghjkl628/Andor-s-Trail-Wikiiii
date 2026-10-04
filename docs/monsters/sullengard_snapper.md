# ![](../assets/icons/monsters/monsters_tometik3_69.png){ .sprite } Sullengard snapper

| Stat | Value |
|---|---|
| Class | reptile |
| HP | 100 |
| Max AP | 10 |
| Attack cost | 7 |
| Move cost | 10 |
| Damage | 11 to 15 |
| Attack chance | 130 |
| Block chance | 200 |
| Damage resistance | 10 |
| Critical skill | 20 |
| Critical multiplier | 2.5 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 5% | 1 to 3 |
| [Gold coins](../items/gold.md) | 100% | 0 to 10 |

## Found on

- [sullengard5](../maps/sullengard5.md)
- [sullengard_pond](../maps/sullengard_pond.md)
- [sullengard_pond_east](../maps/sullengard_pond_east.md)
- [way_to_sullengard_east10](../maps/way_to_sullengard_east10.md)
- [way_to_sullengard_pond_road](../maps/way_to_sullengard_pond_road.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Sullengard snapper. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_snapper_00.json" data-npc="Sullengard snapper" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_snapper_00"></span>**`sullengard_snapper_00`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-20) is 20)* → *fight starts*
    - Next → [sullengard_snapper_0](#d-sullengard_snapper_0)

    <span id="d-sullengard_snapper_0"></span>**`sullengard_snapper_0`** Sullengard snapper: “[You see the mouth open widely.]”

    - “Do you want a hug?” → [sullengard_snapper_1](#d-sullengard_snapper_1)
    - “Do you want some food?” → [sullengard_snapper_1](#d-sullengard_snapper_1)
    - “I better stay away.” → *conversation ends*

    <span id="d-sullengard_snapper_1"></span>**`sullengard_snapper_1`** Sullengard snapper: “[Snap].” — **effects:** applies condition bleeding_wound

    - “Ouch! Why did you bite me? Bad turtle!” → [sullengard_snapper_0](#d-sullengard_snapper_0)
    - “Ouch. Why are you mad at me? Angry turtle!” → [sullengard_snapper_0](#d-sullengard_snapper_0)



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_snapper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sullengard_snapper` · Data from v0.8.18</small>
