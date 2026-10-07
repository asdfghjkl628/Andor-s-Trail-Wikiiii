---
description: "Siola is a non-player character (NPC) in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_90.png){ .sprite } Siola

**Where to find Siola:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_90.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Entry ID** | `siola` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Fine iron broadsword](../items/broadsword_fine_iron.md) | 100% | 1 |
| [Steel broadsword](../items/broadsword2.md) | 100% | 1 |
| [Fine steel broadsword](../items/broadsword_fine_steel.md) | 100% | 1 |
| [Heavy iron club](../items/club_wood1.md) | 100% | 1 |
| [Heavy club](../items/heavy_club.md) | 100% | 1 |
| [Brutal club](../items/club_brutal.md) | 100% | 1 |
| [Balanced heavy iron club](../items/club_wood2.md) | 100% | 1 |
| [Defender's claymore](../items/clmr_def1.md) | 100% | 1 |
| [Runed scepter](../items/scptr_runed.md) | 100% | 1 |
| [Wooden tower shield](../items/shield6.md) | 100% | 1 |
| [Strong wooden tower shield](../items/shield7.md) | 100% | 1 |
| [Crude iron helmet](../items/helm_crude_iron.md) | 100% | 1 |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Siola. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/siola.json" data-npc="Siola" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-siola"></span>**`siola`** Siola: “Hello there. Have you come to browse my selection of items?”

    - “Yes, let's trade.” → *shop opens*
    - “What's the deal with Sienn over there with his pet?” → [siola_sienn_1](#d-siola_sienn_1)

    <span id="d-siola_sienn_1"></span>**`siola_sienn_1`** Siola: “I don't know where he got it from. Anyway, they don't harm anyone, so I'm fine with them being in here. I figured someone should help them have some place to stay, and no one else wanted to help them, so I let them stay here.”

    - Next → [siola_sienn_2](#d-siola_sienn_2)

    <span id="d-siola_sienn_2"></span>**`siola_sienn_2`** Siola: “Sienn may be a bit thick, but he sure can be funny when you get to know him and he trusts you. He can do a lot of those hilarious facial expressions.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `siola` |
    | Spawn group | `siola` |
    | Loot table | `shop_siola` |
    | Conversation | `siola` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:90` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "siola",
     "name": "Siola",
     "iconID": "monsters_rltiles1:90",
     "monsterClass": "humanoid",
     "spawnGroup": "siola",
     "phraseID": "siola",
     "droplistID": "shop_siola"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=siola.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=siola.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=siola.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=siola.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
