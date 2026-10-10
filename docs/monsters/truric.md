---
description: "Truric is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_86.png){ .sprite } Truric

**Where to find Truric:** Brimhaven: [Brimhaven weapon 1](../maps/brimhaven_weapon1.md#pin-npc-truric)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_86.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Trident dagger](../items/dagger_trident.md) | 100% | 1 |
| [Fencing blade](../items/sword_fencing.md) | 100% | 1 |
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |
| [Massive two-handed sword](../items/clmr_msv.md) | 100% | 1 |
| [Maul](../items/maul.md) | 100% | 1 |
| [Bronze warhammer](../items/hmr_bronze.md) | 100% | 1 |
| [Steel claymore](../items/claymore_steel.md) | 100% | 1 |
| [Steel fauchard](../items/fauchard_steel.md) | 100% | 1 |

## Dialogue simulator

Talk to Truric as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/truric_0.json" data-npc="Truric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-truric_0"></span>**`truric_0`** Truric: “Hello. I am Truric. Welcome to my store.”

    - “Thanks, but I need to go. This isn't what I was looking for.” → *conversation ends*
    - “What do you sell?” → [truric_1_0](#d-truric_1_0)
    - “I am looking for my brother, Andor. He looks a bit like me. Have you seen anyone like that recently?” → [truric_2_0](#d-truric_2_0)

    <span id="d-truric_1_0"></span>**`truric_1_0`** Truric: “I am a weaponsmith. I have a good selection at the moment. Would you like to take a look?”

    - “Yes, please show me what you have.” → *shop opens*
    - “No thanks. I need to move on.” → *conversation ends*
    - “Not now. I wanted to ask you about something else. I am looking for my brother Andor. He looks a bit like me. Have you…” → [truric_2_0](#d-truric_2_0)

    <span id="d-truric_2_0"></span>**`truric_2_0`** Truric: “No, sorry, but I haven't. I spend most of my time indoors working on my trade though. He could have passed though town without me noticing.”

    - “Do you get many travelers here?” → [truric_2_1](#d-truric_2_1)

    <span id="d-truric_2_1"></span>**`truric_2_1`** Truric: “We get quite a few, yes. We are not on the main road, but many paths pass through Brimhaven.”

    - Next → [truric_2_2](#d-truric_2_2)

    <span id="d-truric_2_2"></span>**`truric_2_2`** Truric: “Few stay here though. We only have a few beds available at the inn on the east side of town.”

    - “OK. Thanks for the information. I need to go.” → *conversation ends*
    - “OK. Thanks for the information. What do you sell?” → [truric_1_0](#d-truric_1_0)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `truric` |
    | Type (wiki) | NPC |
    | Spawn group | `truric` |
    | Loot table | `truric` |
    | Conversation | `truric_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:86` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "truric",
     "name": "Truric",
     "iconID": "monsters_ld1:86",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "truric",
     "phraseID": "truric_0",
     "droplistID": "truric"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=truric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=truric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=truric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=truric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
