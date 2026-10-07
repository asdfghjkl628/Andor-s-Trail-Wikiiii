---
description: "Acolyte is a non-player character (NPC) in Andor's Trail, found in Fallhaven, Vilegard."
---

# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Acolyte

**Where to find Acolyte:** Fallhaven: [Fallhaven north-east](../maps/fallhaven_ne.md#pin-npc-acolyte), Fallhaven: [Fallhaven north-west](../maps/fallhaven_nw.md#pin-npc-acolyte), Vilegard: [Vilegard south](../maps/vilegard_s.md#pin-npc-acolyte)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Fallhaven, Vilegard |
| **Entry ID** | `acolyte` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Fallhaven north-east](../maps/fallhaven_ne.md) | Fallhaven | 1 | – |
| [Fallhaven north-west](../maps/fallhaven_nw.md) | Fallhaven | 1 | – |
| [Vilegard south](../maps/vilegard_s.md) | Vilegard | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Acolyte. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_priest.json" data-npc="Acolyte" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_priest"></span>**`fallhaven_priest`** Acolyte: “Shadow be with you.”

    - “Can you tell me more about the Shadow?” → [priest_shadow_1](#d-priest_shadow_1)

    <span id="d-priest_shadow_1"></span>**`priest_shadow_1`** Acolyte: “The Shadow protects us. It keeps us safe and comforts us when we sleep.”

    - Next → [priest_shadow_2](#d-priest_shadow_2)

    <span id="d-priest_shadow_2"></span>**`priest_shadow_2`** Acolyte: “It follows us wherever we go. Go with the Shadow my child.”

    - “Shadow be with you.” → *conversation ends*
    - “Whatever, bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `acolyte` |
    | Spawn group | `fallhaven_priest` |
    | Loot table | – |
    | Conversation | `fallhaven_priest` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "acolyte",
     "name": "Acolyte",
     "iconID": "monsters_men:4",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_priest",
     "phraseID": "fallhaven_priest"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
