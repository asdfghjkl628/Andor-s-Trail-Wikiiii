# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Arghes

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Bar brawler's ring](../items/ring_barbrawler.md) | 100% | 1 |
| [Bar brawler's boots](../items/boots_brawler.md) | 100% | 1 |
| [Cap of red eyes](../items/helm_redeye1.md) | 100% | 1 |
| [Cap of bloody eyes](../items/helm_redeye2.md) | 100% | 1 |
| [Troublemaker's ring](../items/ring_troublemaker.md) | 100% | 1 |

## Found on

- [remgard_tavern0](../maps/remgard_tavern0.md)

## Quests

- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stages 70

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Arghes. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/arghes.json" data-npc="Arghes" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-arghes"></span>**`arghes`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 51 of [Search for Andor](../quests/andor.md#stage-51))* → [arghes_2](#d-arghes_2)
    - branch 2 → [arghes_1](#d-arghes_1)

    <span id="d-arghes_2"></span>**`arghes_2`** Arghes: “How interesting. The child from Fallhaven, here in Remgard?”

    - “I'm not from Fallhaven, I'm from Crossglen, west of Fallhaven.” → [arghes_3a](#d-arghes_3a)
    - “Who are you?” → [arghes_3b](#d-arghes_3b)
    - “How do you know where I am from?” → [arghes_3c](#d-arghes_3c)
    - “And how interesting that you ordered a pair of 'Yellow boots'. Did you really order this?” *(if hand over 1× [Yellow boot](../items/brv_wh_item_03.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80))* → [brv_wh_delivery_arghes](#d-brv_wh_delivery_arghes)

    <span id="d-arghes_1"></span>**`arghes_1`** Arghes: “You will find no business here, child.”


    <span id="d-arghes_3a"></span>**`arghes_3a`** Arghes: “Is that so? Hmm, most interesting. It does not change anything, however.”

    - Next → [arghes_4](#d-arghes_4)

    <span id="d-arghes_3b"></span>**`arghes_3b`** Arghes: “Who I am is of no importance in this situation. You on the other hand, are most important.”

    - Next → [arghes_4](#d-arghes_4)

    <span id="d-arghes_3c"></span>**`arghes_3c`** Arghes: “I know ... a great deal of things.”

    - Next → [arghes_4](#d-arghes_4)

    <span id="d-brv_wh_delivery_arghes"></span>**`brv_wh_delivery_arghes`** Arghes: “Yes kid, thank you. Here, take this gold for them.” — **effects:** clears stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80), sets stage 70 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-70), gives 50× [Gold coins](../items/gold.md)

    - “You're welcome.” → *conversation ends*
    - “Bye.” → *conversation ends*

    <span id="d-arghes_4"></span>**`arghes_4`** Arghes: “$playername - yes, that is what they call you.”

    - “How do you know my name? Who are you?” → [arghes_5](#d-arghes_5)

    <span id="d-arghes_5"></span>**`arghes_5`** Arghes: “Let's just say that I am a ... friend. You would do well to keep your ... friends close.”

    - Next → [arghes_6](#d-arghes_6)

    <span id="d-arghes_6"></span>**`arghes_6`** Arghes: “Now, how may I help you? Equipment? Information?”

    - “Let me see what you have to trade.” → [arghes_shop](#d-arghes_shop)
    - “What information do you have?” → [arghes_7](#d-arghes_7)

    <span id="d-arghes_shop"></span>**`arghes_shop`** Arghes: “Certainly.”

    - Next → *shop opens*

    <span id="d-arghes_7"></span>**`arghes_7`** Arghes: “Hmm, let me see.”

    - Next → [arghes_8](#d-arghes_8)

    <span id="d-arghes_8"></span>**`arghes_8`** Arghes: “No, I cannot tell you anything at this time. You are welcome to return once your path has become ... clearer.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Let's just say that I am a .. friend. You would do well to keep your …” → “Let's just say that I am a ... friend. You would do well to keep your…”<br>· text: “Hm, let me see.” → “Hmm, let me see.” |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghes.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghes.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghes.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghes.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `arghes` · Data from v0.8.18</small>
