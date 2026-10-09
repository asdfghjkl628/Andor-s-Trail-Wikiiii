---
description: "Birgil is a non-player character (NPC) in Andor's Trail, found in Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite } Birgil

**Where to find Birgil:** Prim: [Blackwater mountain 22](../maps/blackwater_mountain22.md#pin-npc-birgil)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Prim |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Mead](../items/mead.md) | 100% | 10 |
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Radish](../items/radish.md) | 100% | 5 |

## Dialogue simulator

Set your quest stages and items, then talk to Birgil. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/birgil_1.json" data-npc="Birgil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-birgil_1"></span>**`birgil_1`** Birgil: “Welcome to my tavern. Please have a seat anywhere.”

    - “What can I get to drink around here?” → [birgil_2](#d-birgil_2)

    <span id="d-birgil_2"></span>**`birgil_2`** Birgil: “Well, unfortunately, with the mine tunnel collapsed, we cannot trade much with the outside villages.”

    - Next → [birgil_3](#d-birgil_3)

    <span id="d-birgil_3"></span>**`birgil_3`** Birgil: “However, I do have a huge supply of mead that I stocked up on before the mine shaft collapsed.”

    - “Mead? Yuck. Too sweet for my taste.” → [birgil_4](#d-birgil_4)
    - “Alright! Just my kind of taste. Let's see what you have to trade.” → *shop opens*
    - “Very well, it will have to do. I guess it has some healing potential. Let's trade.” → *shop opens*

    <span id="d-birgil_4"></span>**`birgil_4`** Birgil: “Suit yourself. That's what I've got anyway.”

    - “OK, let's trade anyway.” → *shop opens*
    - “Never mind, goodbye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `birgil` |
    | Type (wiki) | NPC |
    | Spawn group | `birgil` |
    | Loot table | `shop_birgil` |
    | Conversation | `birgil_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:81` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "birgil",
     "name": "Birgil",
     "iconID": "monsters_rltiles2:81",
     "monsterClass": "humanoid",
     "spawnGroup": "birgil",
     "phraseID": "birgil_1",
     "droplistID": "shop_birgil"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=birgil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=birgil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=birgil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=birgil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
