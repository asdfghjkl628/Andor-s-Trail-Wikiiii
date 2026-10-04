# ![](../assets/icons/monsters/monsters_ld1_144.png){ .sprite } Godelieve

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

- [wexlow_village_nw_house](../maps/wexlow_village_nw_house.md)

## Quests

- [Echoes of enchantment](../quests/echoes_of_enchantment.md): stages 14
- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 9

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Godelieve. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/village_godelieve_selector.json" data-npc="Godelieve" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-village_godelieve_selector"></span>**`village_godelieve_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 14 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-14))* → [village_godelieve_1](#d-village_godelieve_1)
    - Next → [village_godelieve_generic](#d-village_godelieve_generic)

    <span id="d-village_godelieve_1"></span>**`village_godelieve_1`** Godelieve: “Oh, our hero returns to us.”

    - “I'm just happy to see you guys safe.” → [village_godelieve_2](#d-village_godelieve_2)

    <span id="d-village_godelieve_generic"></span>**`village_godelieve_generic`** Godelieve: “It's very nice to see you again.”

    - “Would it be OK with you if I slept here? I'm pretty tired.” *(if reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [village_godelieve_bed](#d-village_godelieve_bed)

    <span id="d-village_godelieve_2"></span>**`village_godelieve_2`** Godelieve: “I'm just happy to curl up with Godwin in our own bed tonight.” — **effects:** sets stage 14 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-14)


    <span id="d-village_godelieve_bed"></span>**`village_godelieve_bed`** Godelieve: “Of course. Just use the mat over there in the corner.” — **effects:** sets stage 9 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-9)




## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `village_godelieve` · Data from v0.8.18</small>
