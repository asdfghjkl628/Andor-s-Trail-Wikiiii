# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Highwayman

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 154 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 2 to 7 |
| Attack chance | 160 |
| Block chance | 70 |
| Damage resistance | 4 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 20 |
| [Torn shirt](../items/shirt_torn.md) | 100% | 1 |
| [Mead](../items/mead.md) | 100% | 1 |

## Found on

- [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Highwayman. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/highwayman1.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-highwayman1"></span>**`highwayman1`** Highwayman: “Hold up. What have we here? A lone traveller on the Duleian road.” — **effects:** faction “fct_highwayman1” set to -10

    - Next → [highwayman1_2](#d-highwayman1_2)

    <span id="d-highwayman1_2"></span>**`highwayman1_2`** Highwayman: “Haven't you heard, travelling this road can be dangerous.”

    - Next → [highwayman1_3](#d-highwayman1_3)

    <span id="d-highwayman1_3"></span>**`highwayman1_3`** Highwayman: “There have been reports of people being robbed of all their possessions whilst travelling down this road.”

    - Next → [highwayman1_4](#d-highwayman1_4)

    <span id="d-highwayman1_4"></span>**`highwayman1_4`** Highwayman: “Tell you what, if you give me ... shall we say ... 500 gold, I can almost guarantee that you won't be robbed on this road.”

    - “Sounds good. Here is 500 gold.” *(if pay 500 gold)* → [highwayman1_5](#d-highwayman1_5)
    - “Hey, that sounds like robbery to me!” → [highwayman1_7](#d-highwayman1_7)
    - “How about I just kill you instead?” → [highwayman1_6](#d-highwayman1_6)

    <span id="d-highwayman1_5"></span>**`highwayman1_5`** Highwayman: “Thank you. Have a pleasant day. Watch out for those robbers!” — **effects:** faction “fct_highwayman1” set to 11

    - Next → *NPC leaves*

    <span id="d-highwayman1_7"></span>**`highwayman1_7`** Highwayman: “Oh no no, are you accusing me of robbing you? That's not the case at all. I'm just asking for 500 gold so that you won't be robbed of all your possessions while travelling down this road.”

    - “OK. Here is 500 gold.” *(if pay 500 gold)* → [highwayman1_5](#d-highwayman1_5)
    - “How about I just kill you instead?” → [highwayman1_6](#d-highwayman1_6)

    <span id="d-highwayman1_6"></span>**`highwayman1_6`** Highwayman: “Oh, I see. You are trying to rob ME instead? Well then, I will not be so easily defeated. Prepare yourself.”

    - “Fight!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | faction added (fct_highwayman1); unique removed<br>Dialogue: 4 lines changed<br>· text: “Tell you what, if you give me .. shall we say .. 500 gold, I can almo…” → “Tell you what, if you give me ... shall we say ... 500 gold, I can al…” |
| [v0.8.7](../versions/0.8.7.md) | monsterClass added (humanoid) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `highwayman1` · Data from v0.8.18</small>
