---
description: "Cornith is a non-player character (NPC) in Andor's Trail, found in Stoutford. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_29.png){ .sprite } Cornith

**Where to find Cornith:** Stoutford: [Stoutford smith](../maps/stoutford_smith.md#pin-npc-stoutford_smith)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_29.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Stoutford |
| **Entry ID** | `stoutford_smith` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Steel shortsword](../items/shortsword2.md) | 100% | 1 |
| [Fine iron axe](../items/axe_fine_iron.md) | 100% | 1 |
| [Iron flail](../items/flail_iron.md) | 100% | 1 |
| [Bronze morningstar](../items/morn_bronze.md) | 100% | 1 |
| [Two-handed steel sword](../items/clmr_stl.md) | 100% | 1 |
| [Iron morningstar](../items/morn_iron.md) | 100% | 1 |
| [Leather whip](../items/whip_leather.md) | 100% | 1 |
| [Fine iron broadsword](../items/broadsword_fine_iron.md) | 100% | 1 |
| [Scythe](../items/scythe.md) | 100% | 1 |
| [Fine steel broadsword](../items/broadsword_fine_steel.md) | 100% | 1 |
| [Two-handed iron sword](../items/clmr_irn1.md) | 100% | 1 |
| [Rusty scythe](../items/scythe_rusty.md) | 100% | 1 |
| [Sharp steel rapier](../items/rapier_steel.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Cornith. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/cornith_0.json" data-npc="Cornith" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-cornith_0"></span>**`cornith_0`** Cornith: “Hello, welcome to my shop.”

    - “Please show me what you have to trade.” → *shop opens*
    - “What can you tell me about the town and local area?” → [cornith_1](#d-cornith_1)
    - “I'm looking for my brother, Andor. He looks a bit like me.” → [cornith_2](#d-cornith_2)

    <span id="d-cornith_1"></span>**`cornith_1`** Cornith: “Stoutford is not a big town, but it used to be important.”

    - “Important in what way?” → [cornith_1_1](#d-cornith_1_1)

    <span id="d-cornith_2"></span>**`cornith_2`** Cornith: “Sorry, I don't recall seeing anyone like that recently. Most visitors go to the inn though, so you might have more luck asking there.”

    - “OK. Thanks.” → *conversation ends*

    <span id="d-cornith_1_1"></span>**`cornith_1_1`** Cornith: “We are on the road to Blackwater mountain, so many traders used to pass through Stoutford and stay at the inn.”

    - Next → [cornith_1_2](#d-cornith_1_2)

    <span id="d-cornith_1_2"></span>**`cornith_1_2`** Cornith: “That's all changed though. The path to Blackwater mountain has been blocked by a rockfall. There is also the prison that's just east of here.”

    - “Prison?” → [cornith_1_3](#d-cornith_1_3)

    <span id="d-cornith_1_3"></span>**`cornith_1_3`** Cornith: “Flagstone prison. We never liked it being so close. Who would? But recently something happened, and it was overrun by monsters.”

    - Next → [cornith_1_4](#d-cornith_1_4)

    <span id="d-cornith_1_4"></span>**`cornith_1_4`** Cornith: “There's a guard that protects the path, but without a good reason to come this way most people choose not to risk it. And then of course, there are the monsters coming from the south.”

    - “Monsters from the south?” → [cornith_1_5](#d-cornith_1_5)
    - “I'm tired of hearing about your problems.” → *conversation ends*

    <span id="d-cornith_1_5"></span>**`cornith_1_5`** Cornith: “We think they come from Mount Galmore, and they keep attacking our town.”

    - “I'm sorry to hear about all the trouble, but there's something else I wanted to talk about.” → [cornith_0](#d-cornith_0)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `stoutford_smith` |
    | Spawn group | `stoutford_smith` |
    | Loot table | `shop_cornith` |
    | Conversation | `cornith_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:29` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_smith",
     "name": "Cornith",
     "iconID": "monsters_ld1:29",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_smith",
     "phraseID": "cornith_0",
     "droplistID": "shop_cornith"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
