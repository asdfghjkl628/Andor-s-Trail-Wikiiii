---
description: "Arnal is a non-player character (NPC) in Andor's Trail, found in Remgard. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_28.png){ .sprite } Arnal

**Where to find Arnal:** Remgard: [remgard_weapon](../maps/remgard_weapon.md#pin-npc-arnal)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_28.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Remgard |
| **Entry ID** | `arnal` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Hardened iron sword](../items/sword_hard_iron.md) | 100% | 1 |
| [Fine iron axe](../items/axe_fine_iron.md) | 100% | 1 |
| [Hardened iron longsword](../items/longsword_hard_iron.md) | 100% | 1 |
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |
| [Combat gloves](../items/gloves_combat1.md) | 100% | 1 |
| [Remgard fighting gloves](../items/gloves_remgard1.md) | 100% | 1 |
| [Enchanted Remgard gloves](../items/gloves_remgard2.md) | 100% | 1 |
| [Remgard steel spear](../items/spear_steel_remgard.md) | 100% | 1 |
| [Superior quarterstaff](../items/qtrstaff_2.md) | 100% | 1 |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Arnal. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/arnal.json" data-npc="Arnal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-arnal"></span>**`arnal`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 43 of [The five idols](../quests/fiveidols.md#stage-43))* → [arnal_2](#d-arnal_2)
    - branch 2 → [arnal_1](#d-arnal_1)

    <span id="d-arnal_2"></span>**`arnal_2`** Arnal: “[Arnal clears his throat]”

    - Next → [arnal_3](#d-arnal_3)

    <span id="d-arnal_1"></span>**`arnal_1`** Arnal: “Welcome to my shop. Would you like to see what I have available?”

    - “Yes, please show me what you have.” → *shop opens*
    - “No thank you. Goodbye.” → *conversation ends*

    <span id="d-arnal_3"></span>**`arnal_3`** Arnal: “Welcome to ... *cough* ... my shop. Would you like ... *cough* ... to see what I have available?”

    - “Yes, please show me what you have.” → *shop opens*
    - “No thank you. Goodbye.” → *conversation ends*
    - “Are you all right?” → [arnal_4](#d-arnal_4)
    - “Get away from me, I don't want to catch whatever it is you are infected with!” → *conversation ends*

    <span id="d-arnal_4"></span>**`arnal_4`** Arnal: “I don't know what ... *cough* ... happened. I started getting dizzy and nauseous. Now this cough is really irritating. It must have been something I ate. *cough*”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “I don't know what .. *cough* .. happened. I started getting dizzy and…” → “I don't know what ... *cough* ... happened. I started getting dizzy a…”<br>· text: “Welcome to .. *cough* .. my shop. Would you like .. *cough* .. to see…” → “Welcome to ... *cough* ... my shop. Would you like ... *cough* ... to…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `arnal` |
    | Spawn group | `arnal` |
    | Loot table | `shop_arnal` |
    | Conversation | `arnal` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:28` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "arnal",
     "name": "Arnal",
     "iconID": "monsters_ld1:28",
     "monsterClass": "humanoid",
     "spawnGroup": "arnal",
     "phraseID": "arnal",
     "droplistID": "shop_arnal"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arnal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arnal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arnal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arnal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
