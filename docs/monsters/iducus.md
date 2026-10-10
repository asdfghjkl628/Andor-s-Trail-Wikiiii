---
description: "Iducus is a non-player character (NPC) in Andor's Trail, found in Blackwater mountain 44. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_87.png){ .sprite } Iducus

**Where to find Iducus:** [Blackwater mountain 44](../maps/blackwater_mountain44.md#pin-npc-iducus)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_87.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Blackwater mountain 44 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Blackwater leather armor](../items/bwm_leather_armour.md) | 100% | 2 |
| [Blackwater leather cap](../items/bwm_leather_cap.md) | 100% | 2 |
| [Blackwater ring of combat](../items/bwm_combat_ring.md) | 100% | 2 |

## Dialogue simulator

Set your quest stages and items, then talk to Iducus. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/iducus.json" data-npc="Iducus" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-iducus"></span>**`iducus`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [iducus_1](#d-iducus_1)
    - branch 2 → [iducus_2](#d-iducus_2)

    <span id="d-iducus_1"></span>**`iducus_1`** Iducus: “Welcome friend. What can I do for you?”

    - “What items do you have for sale?” → *shop opens*

    <span id="d-iducus_2"></span>**`iducus_2`** Iducus: “Welcome traveller. I see you are looking at my fine selection of wares.”

    - Next → [blackwater_notrust](#d-blackwater_notrust)

    <span id="d-blackwater_notrust"></span>**`blackwater_notrust`** Iducus: “Regardless, I cannot help you. My services are only for residents of Blackwater mountain, and I don't trust you enough yet.”




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
    | Entry ID | `iducus` |
    | Type (wiki) | NPC |
    | Spawn group | `iducus` |
    | Loot table | `shop_iducus` |
    | Conversation | `iducus` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:87` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "iducus",
     "name": "Iducus",
     "iconID": "monsters_rltiles1:87",
     "monsterClass": "humanoid",
     "spawnGroup": "iducus",
     "phraseID": "iducus",
     "droplistID": "shop_iducus"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iducus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iducus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iducus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iducus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
