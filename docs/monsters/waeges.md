---
description: "Waeges is a non-player character (NPC) in Andor's Trail, found in Blackwater mountain 43. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_88.png){ .sprite } Waeges

**Where to find Waeges:** [Blackwater mountain 43](../maps/blackwater_mountain43.md#pin-npc-waeges)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_88.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Blackwater mountain 43 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Blackwater dagger](../items/bwm_dagger.md) | 100% | 2 |
| [Blackwater poisoned dagger](../items/bwm_dagger_venom.md) | 100% | 2 |
| [Blackwater iron sword](../items/bwm_ironsword.md) | 100% | 2 |

## Dialogue simulator

Set your quest stages and items, then talk to Waeges. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/waeges.json" data-npc="Waeges" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-waeges"></span>**`waeges`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [waeges_1](#d-waeges_1)
    - branch 2 → [waeges_2](#d-waeges_2)

    <span id="d-waeges_1"></span>**`waeges_1`** Waeges: “Welcome friend. What can I do for you?”

    - “What weapons do you have for sale?” → *shop opens*

    <span id="d-waeges_2"></span>**`waeges_2`** Waeges: “Welcome traveller. I see you are looking at my fine selection of weapons.”

    - Next → [blackwater_notrust](#d-blackwater_notrust)

    <span id="d-blackwater_notrust"></span>**`blackwater_notrust`** Waeges: “Regardless, I cannot help you. My services are only for residents of Blackwater mountain, and I don't trust you enough yet.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “Regardless, I cannot help you. My services are only for residents of …” → “Regardless, I cannot help you. My services are only for residents of …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `waeges` |
    | Type (wiki) | NPC |
    | Spawn group | `waeges` |
    | Loot table | `shop_waeges` |
    | Conversation | `waeges` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:88` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "waeges",
     "name": "Waeges",
     "iconID": "monsters_rltiles1:88",
     "monsterClass": "humanoid",
     "spawnGroup": "waeges",
     "phraseID": "waeges",
     "droplistID": "shop_waeges"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waeges.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waeges.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waeges.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waeges.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
