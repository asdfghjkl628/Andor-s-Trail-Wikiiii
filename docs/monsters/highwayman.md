# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Highwayman

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 54 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 2 to 4 |
| Attack chance | 90 |
| Block chance | 30 |
| Damage resistance | 2 |
| Critical skill | 50 |
| Critical multiplier | 2.0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 41 |

## Found on

- [wild9](../maps/wild9.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Highwayman. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bandit1.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bandit1"></span>**`bandit1`** Highwayman: “What have we here? A lost wanderer?” — **effects:** faction “fct_bandit1” set to -10

    - Next → [bandit1_2](#d-bandit1_2)

    <span id="d-bandit1_2"></span>**`bandit1_2`** Highwayman: “How much is your life worth to you? Give me 100 gold and I'll let you go.”

    - “OK OK. Here is the gold. Please don't hurt me!” *(if pay 100 gold)* → [bandit1_3](#d-bandit1_3)
    - “How about we fight over it?” → [bandit1_4](#d-bandit1_4)
    - “How much is your life worth?” → [bandit1_4](#d-bandit1_4)

    <span id="d-bandit1_3"></span>**`bandit1_3`** Highwayman: “About damn time. You are free to go.” — **effects:** faction “fct_bandit1” set to 11

    - Next → *NPC leaves*

    <span id="d-bandit1_4"></span>**`bandit1_4`** Highwayman: “OK then, your life it is. Let's fight. I have been looking forward to a good fight!”

    - “Let's fight!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | faction added (fct_bandit1); movementAggressionType added (protectSpawn)<br>Dialogue: 4 lines changed<br>· text: “Ok then, your life it is. Let's fight. I have been looking forward to…” → “OK then, your life it is. Let's fight. I have been looking forward to…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `highwayman` · Data from v0.8.18</small>
