# ![](../assets/icons/monsters/items_japozero_483.png){ .sprite } Ice berries

| Stat | Value |
|---|---|
| Class | animal |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 999 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [blackwater_mountain32](../maps/blackwater_mountain32.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Ice berries. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/chk_wild_berry2.json" data-npc="Ice berries" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-chk_wild_berry2"></span>**`chk_wild_berry2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT wearing [Gardener's gloves](../items/gardener_gloves.md); reached stage 110 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-110))* → [chk_wild_berry_50](#d-chk_wild_berry_50)
    - branch 2 *(if random chance (5%))* → [chk_wild_berry2_20](#d-chk_wild_berry2_20)
    - branch 3 → [chk_wild_berry2_10](#d-chk_wild_berry2_10)

    <span id="d-chk_wild_berry_50"></span>**`chk_wild_berry_50`** Ice berries: “I should wear my gloves again.”


    <span id="d-chk_wild_berry2_20"></span>**`chk_wild_berry2_20`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Especially sweet ice berries](../items/wild_berry2a.md)

    - branch 1 → *NPC leaves*

    <span id="d-chk_wild_berry2_10"></span>**`chk_wild_berry2_10`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Ice berries](../items/wild_berry2.md)

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line changed<br>· text: “I should better wear my gloves again.” → “I should wear my gloves again.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_berry2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `wild_berry2` · Data from v0.8.18</small>
