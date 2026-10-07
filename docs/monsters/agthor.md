---
description: "Agthor is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men2_4.png){ .sprite } Agthor

**Where to find Agthor:** Fallhaven: [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md#pin-npc-agthor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Fallhaven |
| **Entry ID** | `agthor` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Spiked club of bleeding](../items/club_bld.md) | 100% | 1 |
| [Dull two-handed sword](../items/clmr_dl.md) | 100% | 1 |
| [Massive greataxe](../items/graxe_massive.md) | 100% | 1 |
| [Greataxe of fury](../items/graxe_fury.md) | 100% | 1 |
| [Iron war hammer](../items/hmr_iron.md) | 100% | 1 |
| [Iron mace](../items/mace_iron.md) | 100% | 1 |
| [Two-handed steel sword](../items/clmr_stl.md) | 100% | 1 |
| [Heavy steel skullcap](../items/hvhead_stl.md) | 100% | 1 |
| [Heavy iron skullcap](../items/hvhead_irn.md) | 100% | 1 |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Agthor. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/agthor.json" data-npc="Agthor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-agthor"></span>**`agthor`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [Feygard errands](../quests/feygard_shipment.md#stage-80))* → [agthor_y1](#d-agthor_y1)
    - branch 2 → [agthor0](#d-agthor0)

    <span id="d-agthor_y1"></span>**`agthor_y1`** Agthor: “Hey, you're that kid! That kid that we've been hearing about. It's great to finally get a face on the stories we've heard.”

    - Next → [agthor_y2](#d-agthor_y2)

    <span id="d-agthor0"></span>**`agthor0`** Agthor: “Hello there. Please move along. These things are property of Feygard, and you have no business here.”


    <span id="d-agthor_y2"></span>**`agthor_y2`** Agthor: “Please, anything I can help you with?”

    - “Care to trade some items?” → [agthor_y4](#d-agthor_y4)
    - “I'm looking for my brother.” → [agthor_y3](#d-agthor_y3)

    <span id="d-agthor_y4"></span>**`agthor_y4`** Agthor: “Sure thing. Here's what I've got.”

    - “Trade” → *shop opens*

    <span id="d-agthor_y3"></span>**`agthor_y3`** Agthor: “Sorry, can't help you there. You're the only kid I've seen running along here in a long time.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `agthor` |
    | Spawn group | `agthor` |
    | Loot table | `shop_agthor` |
    | Conversation | `agthor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:4` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agthor",
     "name": "Agthor",
     "iconID": "monsters_men2:4",
     "phraseID": "agthor",
     "droplistID": "shop_agthor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
