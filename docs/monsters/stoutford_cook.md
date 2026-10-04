# ![](../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite } Cadoren

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stoutford_cook` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Smoked sausage](../items/smoked-sausage.md) | 100% | 4 to 5 |
| [Fermented garlic](../items/ferm-garlic.md) | 100% | 3 to 5 |
| [Goat milk](../items/milk_goat.md) | 100% | 5 |
| [Pickled cabbage](../items/pickled-cabbage.md) | 100% | 3 to 6 |
| [Blue cheese](../items/cheese_blue.md) | 100% | 5 to 7 |
| [Bread](../items/bread.md) | 100% | 4 to 7 |
| [Eggs](../items/eggs.md) | 100% | 2 to 4 |
| [Goat cheese](../items/cheese_goat.md) | 100% | 1 to 6 |
| [Dried goat meat](../items/goat_meat_dried.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_tavern](../maps/stoutford_tavern.md) | Stoutford | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Cadoren. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/cadoren_0.json" data-npc="Cadoren" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-cadoren_0"></span>**`cadoren_0`** Cadoren: “Welcome to our wonderful Inn. How can we help you?”

    - “Who are you?” → [cadoren_1](#d-cadoren_1)

    <span id="d-cadoren_1"></span>**`cadoren_1`** Cadoren: “My name is Cadoren. I'm the best cook in town.”

    - Next → [cadoren_2](#d-cadoren_2)

    <span id="d-cadoren_2"></span>**`cadoren_2`** Cadoren: “Unlike most, lesser, cooks in local towns, I'm a specialist.”

    - “A specialist? In what?” → [cadoren_3](#d-cadoren_3)
    - “Enough of the bragging. Show me what you have to trade.” → *shop opens*

    <span id="d-cadoren_3"></span>**`cadoren_3`** Cadoren: “Food that lasts a long time. *cough*. Or in some cases food that has already lasted a long time.”

    - “That sounds disgusting. No thanks.” → *conversation ends*
    - “That sounds interesting. Show me what you have.” → *shop opens*
    - “Why do you need food that lasts a long time?” → [cadoren_4](#d-cadoren_4)

    <span id="d-cadoren_4"></span>**`cadoren_4`** Cadoren: “The path to Blackwater mountain has been cut off. There are also increasing attacks by monsters. These things have driven down trade, making supplies hard to get.”

    - “So all the food you sell is old?” → [cadoren_5](#d-cadoren_5)
    - “Where is Blackwater mountain?” → [cadoran_4b](#d-cadoran_4b)
    - “Why are monster attacks increasing?” → [cadoren_4a](#d-cadoren_4a)
    - “Thanks for the information. I have to leave now.” → *conversation ends*

    <span id="d-cadoren_5"></span>**`cadoren_5`** Cadoren: “Of course not. We have some fields where we grow crops. And we have a number of goats.”

    - “Goats?” → [cadoren_6](#d-cadoren_6)

    <span id="d-cadoran_4b"></span>**`cadoran_4b`** Cadoren: “Head out of town to the north. There are two settlements there, Prim and Blackwater mountain Settlement. There has been a rockfall though, making it very difficult to get to them.”

    - “Thanks for the information. What was it you said about the monsters?” → [cadoren_4](#d-cadoren_4)

    <span id="d-cadoren_4a"></span>**`cadoren_4a`** Cadoren: “We think they came from Mount Galmore, and they recently started attacking the town. We can fight them off, but they deter travelers from coming here.”

    - “OK. Could you repeat what you said about that other mountain.” → [cadoren_4](#d-cadoren_4)

    <span id="d-cadoren_6"></span>**`cadoren_6`** Cadoren: “Goats are very versatile. They eat almost anything, provide both milk and meat, and their hides make excellent clothing.”

    - Next → [cadoren_7](#d-cadoren_7)

    <span id="d-cadoren_7"></span>**`cadoren_7`** Cadoren: “With supplies from other towns being so limited, getting the goats was an excellent idea. My idea, of course.”

    - “*Sigh*. The whole town would obviously starve if it were not for you. Thanks for the information though.” → *conversation ends*
    - “How about you quit with the bragging, and show me what you have to trade.” → *shop opens*
    - “Whatever. Why don't we go back to what you said about the monsters and that mountain.” → [cadoren_4](#d-cadoren_4)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “Follow the path to the west. There are two settlements there, Prim an…” → “Head out of town to the north. There are two settlements there, Prim …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_cook.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stoutford_cook` |
    | Spawn group | `stoutford_cook` |
    | Loot table | `shop_cadoren` |
    | Conversation | `cadoren_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:81` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_cook",
     "name": "Cadoren",
     "iconID": "monsters_rltiles2:81",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_cook",
     "phraseID": "cadoren_0",
     "droplistID": "shop_cadoren"
    }
    ```


<small>Data from v0.8.18</small>
