# ![](../assets/icons/monsters/monsters_rltiles1_42.png){ .sprite } Kazaul guardian

| Stat | Value |
|---|---|
| Class | demon |
| HP | 95 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 5 |
| Damage | 3 to 8 |
| Attack chance | 70 |
| Block chance | 90 |
| Damage resistance | 3 |
| Critical skill | 40 |
| Critical multiplier | 2.0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 52 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 2 |
| [Shadow of the slayer](../items/shadow_slayer.md) | 100% | 1 |

## Found on

- [blackwater_mountain42](../maps/blackwater_mountain42.md)

## Quests

- [Lights in the dark](../quests/kazaul.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Kazaul guardian. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/kazaul_guardian.json" data-npc="Kazaul guardian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kazaul_guardian"></span>**`kazaul_guardian`** Kazaul guardian: “Kazaul...”

    - “What?” → [kazaul_guardian_1](#d-kazaul_guardian_1)
    - “Kazaul, destroyer of bright dreams.” *(if reached stage 40 of [Lights in the dark](../quests/kazaul.md#stage-40))* → [kazaul_guardian_2](#d-kazaul_guardian_2)

    <span id="d-kazaul_guardian_1"></span>**`kazaul_guardian_1`** Kazaul guardian: “[The guardian looks completely unaware of your presence]”


    <span id="d-kazaul_guardian_2"></span>**`kazaul_guardian_2`** Kazaul guardian: “[The guardian looks down upon you with its burning eyes]”

    - “Kazaul, defiler of the Elytharan Temple.” → [kazaul_guardian_3](#d-kazaul_guardian_3)

    <span id="d-kazaul_guardian_3"></span>**`kazaul_guardian_3`** Kazaul guardian: “[You see the burning eyes of the guardian instantly turn into a dark red haze]” — **effects:** sets stage 50 of [Lights in the dark](../quests/kazaul.md#stage-50)

    - “A fight, I have been waiting for this!” → *fight starts*
    - “Please don't kill me!” → *fight starts*
    - “For the Shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change<br>Dialogue: 4 lines changed<br>· text: “(The guardian looks down upon you with its burning eyes)” → “[The guardian looks down upon you with its burning eyes]”<br>· text: “(You see the burning eyes of the guardian instantly turn into a dark …” → “[You see the burning eyes of the guardian instantly turn into a dark …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `kazaul_guardian` · Data from v0.8.18</small>
