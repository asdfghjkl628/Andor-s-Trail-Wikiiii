# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Lediofa

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

- [fallhaven_potions](../maps/fallhaven_potions.md)

## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 220

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lediofa. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/fungi_rescued2.json" data-npc="Lediofa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fungi_rescued2"></span>**`fungi_rescued2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220))* → [fungi_rescued2_1](#d-fungi_rescued2_1)
    - branch 2 *(if reached stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220))* → [fungi_rescued2_30](#d-fungi_rescued2_30)

    <span id="d-fungi_rescued2_1"></span>**`fungi_rescued2_1`** Lediofa: “Outrageous! I told you already, I don't have 150 gold!”

    - Next → [fungi_rescued2_10](#d-fungi_rescued2_10)

    <span id="d-fungi_rescued2_30"></span>**`fungi_rescued2_30`** Lediofa: “You've saved me again, $playername. You truly are a hero. If you ever find yourself in Nor City, I'm sure my family would love to meet you. Thank you!” — **effects:** sets stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220)

    - “Take care!” → *NPC leaves*

    <span id="d-fungi_rescued2_10"></span>**`fungi_rescued2_10`** [Potion merchant](../monsters/potion_merchant.md): “I'm sorry that you're ill, girl, but I can't work for free. The price is 150 gold, no less.”

    - Next → [fungi_rescued2_20](#d-fungi_rescued2_20)

    <span id="d-fungi_rescued2_20"></span>**`fungi_rescued2_20`** [Lediofa](../monsters/fungi_rescued2.md): “You greedy swine...Oh! It's $playername! I came here to cure the mushroom poison, but that lousy merchant won't help me until he receives payment. And I have no gold...”

    - “That's no trouble. I can spare 150 gold to help.” *(if pay 150 gold)* → [fungi_rescued2_30](#d-fungi_rescued2_30)
    - “I'm sorry to hear that, but I can't spare the gold to help you right now.” → *conversation ends*
    - “The potioner is right, you know. Nobody works for free.” → [fungi_rescued2_20_2](#d-fungi_rescued2_20_2)

    <span id="d-fungi_rescued2_20_2"></span>**`fungi_rescued2_20_2`** Lediofa: “But what can I do? I don't feel well...”




## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `fungi_rescued2` · Data from v0.8.18</small>
