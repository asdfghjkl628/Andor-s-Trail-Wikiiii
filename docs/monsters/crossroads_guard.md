# ![](../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite } Guard

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

- [crossroads](../maps/crossroads.md)
- [houseatcrossroads2](../maps/houseatcrossroads2.md)
- [houseatcrossroads3](../maps/houseatcrossroads3.md)

## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stages 15

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_guard"></span>**`crossroads_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15))* → [crossroads_guild03_1](#d-crossroads_guild03_1)
    - branch 2 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [crossroads_guard_r_1](#d-crossroads_guard_r_1)
    - branch 3 → [crossroads_guard_1](#d-crossroads_guard_1)

    <span id="d-crossroads_guild03_1"></span>**`crossroads_guild03_1`** Guard: “Aren't you a bit young to be travelling around here all by yourself?”

    - “Sorry, have you heard anything about a murder?” → [crossroads_guild03_2](#d-crossroads_guild03_2)

    <span id="d-crossroads_guard_r_1"></span>**`crossroads_guard_r_1`** Guard: “Did you hear? Some thieves down in Fallhaven were planning an escape for one of the imprisoned thieves in the prison there.”

    - Next → [crossroads_guard_r_2](#d-crossroads_guard_r_2)

    <span id="d-crossroads_guard_1"></span>**`crossroads_guard_1`** Guard: “Aren't you a bit young to be traveling around here all by yourself?”

    - Next → [crossroads_guard_2](#d-crossroads_guard_2)

    <span id="d-crossroads_guild03_2"></span>**`crossroads_guild03_2`** Guard: “Yeah, Feygard authorities have sent more patrols to the south. Apparently there is a group of criminals hiding in the forest” — **effects:** sets stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15)

    - Next → [crossroads_guild03_3](#d-crossroads_guild03_3)

    <span id="d-crossroads_guard_r_2"></span>**`crossroads_guard_r_2`** Guard: “Luckily, someone got wind of it and told the guard captain.”

    - Next → [crossroads_guard_r_3](#d-crossroads_guard_r_3)

    <span id="d-crossroads_guard_2"></span>**`crossroads_guard_2`** Guard: “I sure hope you are not another one of those types trying to sell me your cheap junk.”

    - Next → [crossroads_guard_3](#d-crossroads_guard_3)

    <span id="d-crossroads_guild03_3"></span>**`crossroads_guild03_3`** Guard: “Now go away kid, I'm working!”


    <span id="d-crossroads_guard_r_3"></span>**`crossroads_guard_r_3`** Guard: “It's good to know that there are at least a few decent people still around.”


    <span id="d-crossroads_guard_3"></span>**`crossroads_guard_3`** Guard: “Go away, kid.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 3 lines added, 2 lines changed<br>· text: “Aren't you a bit young to be travelling around here all by yourself?” → “Aren't you a bit young to be traveling around here all by yourself?” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Yeah, Feygard authorities have sent more patrols to the south. Appear…” → “Yeah, Feygard authorities have sent more patrols to the south. Appare…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossroads_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `crossroads_guard` · Data from v0.8.18</small>
