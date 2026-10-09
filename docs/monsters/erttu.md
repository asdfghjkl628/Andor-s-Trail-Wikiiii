---
description: "Erttu is a non-player character (NPC) in Andor's Trail, found in Vilegard."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Erttu

**Where to find Erttu:** Vilegard: [Vilegard erttu](../maps/vilegard_erttu.md#pin-npc-erttu)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Vilegard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Erttu. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/erttu_1.json" data-npc="Erttu" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erttu_1"></span>**`erttu_1`** Erttu: “Hello there outsider. In general, we dislike outsiders here in Vilegard, but there is something about you that I find familiar.”

    - Next → [erttu_default](#d-erttu_default)

    <span id="d-erttu_default"></span>**`erttu_default`** Erttu: “What do you want to talk about?”

    - “Why is everyone in Vilegard so suspicious of outsiders?” *(if reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10))* → [erttu_distrust_1](#d-erttu_distrust_1)
    - “What can you tell me about Vilegard?” → [erttu_vilegard_1](#d-erttu_vilegard_1)

    <span id="d-erttu_distrust_1"></span>**`erttu_distrust_1`** Erttu: “Most of us that live here in Vilegard have a history of trusting people too much. People that have hurt us in the end.”

    - Next → [erttu_distrust_2](#d-erttu_distrust_2)

    <span id="d-erttu_vilegard_1"></span>**`erttu_vilegard_1`** Erttu: “We have almost everything we need here in Vilegard. Our center of the village is the chapel.”

    - Next → [erttu_vilegard_2](#d-erttu_vilegard_2)

    <span id="d-erttu_distrust_2"></span>**`erttu_distrust_2`** Erttu: “Now we start by being suspicious, and ask that outsiders coming here gain our trust by helping us first.”

    - Next → [erttu_distrust_3](#d-erttu_distrust_3)

    <span id="d-erttu_vilegard_2"></span>**`erttu_vilegard_2`** Erttu: “The chapel serves as our place of worship for the Shadow, and also as our place to gather when discussing larger issues in our village.”

    - Next → [erttu_vilegard_3](#d-erttu_vilegard_3)

    <span id="d-erttu_distrust_3"></span>**`erttu_distrust_3`** Erttu: “Also, other people generally look down upon us here in Vilegard for some reason. Especially those snobs from Feygard and the northern cities.”

    - “What else can you tell me about Vilegard?” → [erttu_vilegard_1](#d-erttu_vilegard_1)

    <span id="d-erttu_vilegard_3"></span>**`erttu_vilegard_3`** Erttu: “Apart from the chapel, we have a tavern, a smith and an armorer.”

    - “Thanks for the information. There was something else I wanted to talk about.” → [erttu_default](#d-erttu_default)
    - “Thanks for the information. Goodbye.” → *conversation ends*
    - “Wow, nothing more? I wonder what I am doing in a puny village such as this one.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `erttu` |
    | Type (wiki) | NPC |
    | Spawn group | `erttu` |
    | Loot table | – |
    | Conversation | `erttu_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "erttu",
     "name": "Erttu",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "erttu",
     "phraseID": "erttu_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
