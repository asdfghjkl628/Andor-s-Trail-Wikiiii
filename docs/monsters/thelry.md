---
description: "Thelry is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_133.png){ .sprite } Thelry

**Where to find Thelry:** Brimhaven: [Brimhaven armor 1](../maps/brimhaven_armor1.md#pin-npc-thelry)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_133.png){ .sprite }</p>

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
| [Brimhaven steel helmet](../items/brimhaven_steel_helmet.md) | 100% | 1 |
| [Brimhaven plate mail](../items/brimhaven_plate_mail1.md) | 100% | 1 |
| [Brimhaven rigid plate mail](../items/brimhaven_plate_mail2.md) | 100% | 1 |
| [Reinforced wooden buckler](../items/shield3.md) | 100% | 1 |
| [Ordinary chain mail](../items/armor_chain2.md) | 100% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 100% | 1 to 2 |
| [Leather boots](../items/boots1.md) | 100% | 1 |
| [Ordinary leather cap](../items/hat_leather1.md) | 100% | 1 to 2 |

## Dialogue simulator

Set your quest stages and items, then talk to Thelry. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/thelry_0.json" data-npc="Thelry" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-thelry_0"></span>**`thelry_0`** Thelry: “Hi kid. I'm Thelry, the local armorer. You are too young to need armor though. If you need armor, then you are doing something which could get you hurt. Kids should stay at home, where it's safe.”

    - “I can handle myself. I'm from Crossglen, and I made it here OK. Please show me your wares.” → *shop opens*
    - “My father sent me out to look for by brother, Andor. He looks a bit like me. Have you seen him?” → [thelry_1](#d-thelry_1)
    - “If that's what you think then I won't buy anything from you.” → *conversation ends*

    <span id="d-thelry_1"></span>**`thelry_1`** Thelry: “No, sorry, I haven't seen anyone like that.”

    - “OK. Thanks. What do you have to sell?” → *shop opens*



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “No, sorry, I haven't seen onyone like that.” → “No, sorry, I haven't seen anyone like that.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `thelry` |
    | Type (wiki) | NPC |
    | Spawn group | `thelry` |
    | Loot table | `thelry` |
    | Conversation | `thelry_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:133` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "thelry",
     "name": "Thelry",
     "iconID": "monsters_ld1:133",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "thelry",
     "phraseID": "thelry_0",
     "droplistID": "thelry"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thelry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thelry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thelry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thelry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
