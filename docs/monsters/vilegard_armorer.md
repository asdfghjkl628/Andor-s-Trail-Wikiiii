---
description: "Vilegard armorer is a non-player character (NPC) in Andor's Trail, found in Vilegard. Shopkeeper; starts Trusting an outsider."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Vilegard armorer

**Where to find Vilegard armorer:** Vilegard: [Vilegard armorer](../maps/vilegard_armorer.md#pin-npc-vilegard_armorer)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper; starts [Trusting an outsider](../quests/vilegard.md) |
| **Found in** | Vilegard |
| **Entry ID** | `vilegard_armorer` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Wooden buckler](../items/shield1.md) | 100% | 1 |
| [Crude wooden shield](../items/shield4.md) | 100% | 1 |
| [Heavy iron gloves](../items/hglv_irn.md) | 100% | 1 |
| [Chainmail mittens](../items/hglv_chml.md) | 100% | 1 |
| [Wooden shield](../items/shield_wooden.md) | 100% | 1 |
| [Crude leather cap](../items/hat3.md) | 100% | 1 |
| [Leather cap](../items/hat4.md) | 100% | 1 |
| [Ordinary leather cap](../items/hat_leather1.md) | 100% | 1 |
| [Hardened leather cap](../items/hat_hard_leather.md) | 100% | 1 |
| [Reinforced boots](../items/boots5.md) | 100% | 1 |
| [Worn iron boots](../items/hboot_wirn.md) | 100% | 1 |
| [Heavy iron boots](../items/hboot_irn.md) | 100% | 1 |
| [Rusty chain mail](../items/armor_chain1.md) | 100% | 1 |
| [Ordinary chain mail](../items/armor_chain2.md) | 100% | 1 |
| [Rigid chain mail](../items/armour_rigid_chain.md) | 100% | 1 |
| [Worn chainmail](../items/chmail2.md) | 100% | 1 |
| [Rusty heavy cuirass](../items/hvbdy_rust.md) | 100% | 1 |

## Quests

- [Trusting an outsider](../quests/vilegard.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Vilegard armorer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/vilegard_armorer_select.json" data-npc="Vilegard armorer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-vilegard_armorer_select"></span>**`vilegard_armorer_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [vilegard_armorer_1](#d-vilegard_armorer_1)
    - branch 2 → [vilegard_shop_notrust](#d-vilegard_shop_notrust)

    <span id="d-vilegard_armorer_1"></span>**`vilegard_armorer_1`** Vilegard armorer: “Hello there. Please browse my selection of fine armors and protection.”

    - “Let me see your list of wares.” → *shop opens*

    <span id="d-vilegard_shop_notrust"></span>**`vilegard_shop_notrust`** Vilegard armorer: “You are an outsider. We don't like outsiders here in Vilegard. Please leave.”

    - “Why is everyone in Vilegard so suspicious of outsiders?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)
    - “Can I see what items you have for sale?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)

    <span id="d-vilegard_shop_notrust_2"></span>**`vilegard_shop_notrust_2`** Vilegard armorer: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.” — **effects:** sets stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `vilegard_armorer` |
    | Spawn group | `vg_armorer` |
    | Loot table | `shop_vg_armorer` |
    | Conversation | `vilegard_armorer_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "vilegard_armorer",
     "name": "Vilegard armorer",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "vg_armorer",
     "phraseID": "vilegard_armorer_select",
     "droplistID": "shop_vg_armorer"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
