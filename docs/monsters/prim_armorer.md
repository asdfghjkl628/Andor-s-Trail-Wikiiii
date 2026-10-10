---
description: "Prim armorer is a non-player character (NPC) in Andor's Trail, found in Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_88.png){ .sprite } Prim armorer

**Where to find Prim armorer:** Prim: [Blackwater mountain 23](../maps/blackwater_mountain23.md#pin-npc-prim_armorer)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_88.png){ .sprite }</p>

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
| [Rusted iron sword](../items/rusted_iron_sword.md) | 100% | 1 |
| [Iron sword](../items/ironsword1.md) | 100% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 100% | 1 |
| [Blood-stained gloves](../items/used_gloves.md) | 100% | 1 to 2 |

## Dialogue simulator

Set your quest stages and items, then talk to Prim armorer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_armorer.json" data-npc="Prim armorer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_armorer"></span>**`prim_armorer`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [Clouded intent](../quests/prim_hunt.md#stage-240))* → [prim_armorer_1](#d-prim_armorer_1)
    - branch 2 → [prim_armorer_2](#d-prim_armorer_2)

    <span id="d-prim_armorer_1"></span>**`prim_armorer_1`** Prim armorer: “Welcome friend! Would you like to see what equipment I have available?”

    - “Sure. Show me what you have.” → [prim_armorer_3](#d-prim_armorer_3)

    <span id="d-prim_armorer_2"></span>**`prim_armorer_2`** Prim armorer: “Welcome traveller. Have you come to ask for help from me and the equipment I sell?”

    - Next → [prim_notrust](#d-prim_notrust)

    <span id="d-prim_armorer_3"></span>**`prim_armorer_3`** Prim armorer: “I must tell you that my supply is not what it used to be, now that the southern mine entrance has collapsed. Far fewer traders come here to Prim now.”

    - “OK, let me see your wares.” → *shop opens*

    <span id="d-prim_notrust"></span>**`prim_notrust`** Prim armorer: “Regardless, I cannot help you. My services are only for residents of Prim, and I don't trust you enough yet. You might be a spy from the Blackwater mountain settlement.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Regardless, I cannot help you. My services are only for residents of …” → “Regardless, I cannot help you. My services are only for residents of …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_armorer` |
    | Type (wiki) | NPC |
    | Spawn group | `prim_armorer` |
    | Loot table | `shop_prim_armorer` |
    | Conversation | `prim_armorer` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:88` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_armorer",
     "name": "Prim armorer",
     "iconID": "monsters_rltiles1:88",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_armorer",
     "phraseID": "prim_armorer",
     "droplistID": "shop_prim_armorer"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
