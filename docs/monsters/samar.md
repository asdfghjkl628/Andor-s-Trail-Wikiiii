---
description: "Samar is a non-player character (NPC) in Andor's Trail, found in Prim. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles2_93.png){ .sprite } Samar

**Where to find Samar:** Prim: [Blackwater mountain 25](../maps/blackwater_mountain25.md#pin-npc-samar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_93.png){ .sprite }</p>

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
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Weak poison antidote](../items/pot_poison_weak_antidote.md) | 100% | 10 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 100% | 10 |
| [Minor potion of speed](../items/pot_speed_1.md) | 100% | 10 |

## Dialogue simulator

Set your quest stages and items, then talk to Samar. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_priest.json" data-npc="Samar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_priest"></span>**`prim_priest`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [Clouded intent](../quests/prim_hunt.md#stage-240))* → [prim_priest_1](#d-prim_priest_1)
    - branch 2 → [prim_priest_2](#d-prim_priest_2)

    <span id="d-prim_priest_1"></span>**`prim_priest_1`** Samar: “Welcome friend! Would you like to browse my selection of fine potions and ointments?”

    - “Sure. Show me what you have.” → *shop opens*

    <span id="d-prim_priest_2"></span>**`prim_priest_2`** Samar: “Welcome traveller. Have you come to ask for help from me and my potions?”

    - Next → [prim_notrust](#d-prim_notrust)

    <span id="d-prim_notrust"></span>**`prim_notrust`** Samar: “Regardless, I cannot help you. My services are only for residents of Prim, and I don't trust you enough yet. You might be a spy from the Blackwater mountain settlement.”




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
    | Entry ID | `samar` |
    | Type (wiki) | NPC |
    | Spawn group | `prim_priest` |
    | Loot table | `shop_samar` |
    | Conversation | `prim_priest` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:93` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "samar",
     "name": "Samar",
     "iconID": "monsters_rltiles2:93",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_priest",
     "phraseID": "prim_priest",
     "droplistID": "shop_samar"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=samar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=samar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=samar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=samar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
