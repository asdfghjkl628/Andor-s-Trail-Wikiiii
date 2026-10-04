# ![](../assets/icons/monsters/monsters_bosses_2x2_4.png){ .sprite } Rock eater

| Stat | Value |
|---|---|
| Class | construct |
| HP | 500 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 5 |
| Damage | 12 to 14 |
| Attack chance | 254 |
| Block chance | 180 |
| Damage resistance | 20 |
| Critical skill | 23 |
| Critical multiplier | 2.2 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 2500 |

## Found on

- [undertell_exit](../maps/undertell_exit.md)

## Quests

- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 60

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Rock eater. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/rock_eater_selector.json" data-npc="Rock eater" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-rock_eater_selector"></span>**`rock_eater_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-60))* → [rock_eater_move_along](#d-rock_eater_move_along)
    - branch 2 *(if reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2))* → [rock_eater_pc_rewarded_with_nixite_10](#d-rock_eater_pc_rewarded_with_nixite_10)
    - branch 3 → [rock_eater_fight](#d-rock_eater_fight)

    <span id="d-rock_eater_move_along"></span>**`rock_eater_move_along`** Rock eater: “Move along. I'm busy!”


    <span id="d-rock_eater_pc_rewarded_with_nixite_10"></span>**`rock_eater_pc_rewarded_with_nixite_10`** Rock eater: “You! You stole my Nixite crystal and I want it back now or your life ends here, right now.”

    - “I had it, yes, but I no longer have it. I think I may have it stored away somewhere, maybe.” *(if NOT carry 1× [Nixite crystal](../items/nixite_crystal.md))* → [rock_eater_fetch_crystal](#d-rock_eater_fetch_crystal)
    - “I sold it.” *(if NOT carry 1× [Nixite crystal](../items/nixite_crystal.md))* → [rock_eater_then_die](#d-rock_eater_then_die)
    - “Here, I have it. Take it.” *(if hand over 1× [Nixite crystal](../items/nixite_crystal.md))* → [rock_eater_pc_give_nixite_10](#d-rock_eater_pc_give_nixite_10)

    <span id="d-rock_eater_fight"></span>**`rock_eater_fight`** *(silent check: the first matching branch below is taken)*

    - branch 1 → *fight starts*

    <span id="d-rock_eater_fetch_crystal"></span>**`rock_eater_fetch_crystal`** Rock eater: “Then bring it to me and you shall pass.”


    <span id="d-rock_eater_then_die"></span>**`rock_eater_then_die`** Rock eater: “Then you die!”

    - Next → [rock_eater_fight](#d-rock_eater_fight)

    <span id="d-rock_eater_pc_give_nixite_10"></span>**`rock_eater_pc_give_nixite_10`** Rock eater: “Wonderful! Now move along before I change my mind.” — **effects:** sets stage 60 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-60), removes monsters from undertell_exit, spawns monsters on undertell_exit




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rock_eater.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `rock_eater` · Data from v0.8.18</small>
