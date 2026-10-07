---
description: "Shy Cora is a non-player character (NPC) in Andor's Trail, found in undertell_01, undertell_1_1. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_gisons_12.png){ .sprite } Shy Cora

**Where to find Shy Cora:** [undertell_01](../maps/undertell_01.md#pin-npc-shy_cora), [undertell_1_1](../maps/undertell_1_1.md#pin-npc-shy_cora)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_12.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | undertell_01, undertell_1_1 |
| **Entry ID** | `shy_cora` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Undertell pickaxe](../items/undertell_pickaxe.md) | 50% | 1 |
| [Emerald](../items/undertell_emerald.md) | 100% | 1 to 2 |
| [Arschleder](../items/arschleder.md) | 100% | 1 |
| [Miner's tunic](../items/miner_tunic.md) | 100% | 1 |
| [Undertell shovel](../items/undertell_shovel.md) | 100% | 1 |
| [Miner's hooded tunic](../items/miner_hood.md) | 100% | 1 |
| [Shredded tunic](../items/shredded_tunic.md) | 100% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [undertell_01](../maps/undertell_01.md) | – | 1 | Appears later, during a quest |
| [undertell_1_1](../maps/undertell_1_1.md) | – | 1 | Appears later, during a quest |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Shy Cora. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/cora_vendor_intro.json" data-npc="Shy Cora" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-cora_vendor_intro"></span>**`cora_vendor_intro`** Shy Cora: “You don't shout.”

    - “I won't.” → [cora_vendor_ack](#d-cora_vendor_ack)
    - “I understand.” → [cora_vendor_ack](#d-cora_vendor_ack)

    <span id="d-cora_vendor_ack"></span>**`cora_vendor_ack`** Shy Cora: “Then we can speak briefly.”

    - “May I look at what's here?” → [cora_vendor_open](#d-cora_vendor_open)
    - “That's enough.” → *conversation ends*

    <span id="d-cora_vendor_open"></span>**`cora_vendor_open`** Shy Cora: “These were stored. Not claimed.”

    - “Let me see.” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `shy_cora` |
    | Spawn group | `shy_cora` |
    | Loot table | `cora_dl` |
    | Conversation | `cora_vendor_intro` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:12` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "shy_cora",
     "name": "Shy Cora",
     "iconID": "monsters_gisons:12",
     "monsterClass": "ghost",
     "horizontalFlipChance": 75,
     "phraseID": "cora_vendor_intro",
     "droplistID": "cora_dl"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shy_cora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shy_cora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shy_cora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shy_cora.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
