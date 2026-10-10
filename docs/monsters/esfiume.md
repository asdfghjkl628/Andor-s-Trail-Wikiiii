---
description: "Esfiume is a non-player character (NPC) in Andor's Trail, found in Foaming Flask Tavern."
---

# ![](../assets/icons/monsters/monsters_ld1_125.png){ .sprite } Esfiume

**Where to find Esfiume:** Foaming Flask Tavern: [Waytominingtown 1a](../maps/waytominingtown1a.md#pin-npc-esfiume)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_125.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Foaming Flask Tavern |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Esfiume. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/esfiume0.json" data-npc="Esfiume" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-esfiume0"></span>**`esfiume0`** Esfiume: “Hey! Whatever you saw us doing here, we're completely innocent.”

    - Next → [esfiume1](#d-esfiume1)

    <span id="d-esfiume1"></span>**`esfiume1`** Esfiume: “These aren't even our things. We are only ... uh ... standing around here.”

    - “I didn't see anything.” → [esfiume2](#d-esfiume2)
    - “What do you do around here?” → [esfiume3](#d-esfiume3)

    <span id="d-esfiume2"></span>**`esfiume2`** Esfiume: “That's right you didn't.”

    - “What do you do around here?” → [esfiume3](#d-esfiume3)

    <span id="d-esfiume3"></span>**`esfiume3`** Esfiume: “Oh, we ... um ... stay here. Completely legit. Not at all doing anything that's not allowed.”

    - “What's in those crates back there?” → [esfiume4](#d-esfiume4)

    <span id="d-esfiume4"></span>**`esfiume4`** Esfiume: “Oh nothing. They're ... uh ... empty. Yes, that's it, empty.”

    - “Right. I had better leave.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Oh nothing. They're .. uh .. empty. Yes, that's it, empty.” → “Oh nothing. They're ... uh ... empty. Yes, that's it, empty.”<br>· text: “Oh, we .. um .. stay here. Completely legit. Not at all doing anythin…” → “Oh, we ... um ... stay here. Completely legit. Not at all doing anyth…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `esfiume` |
    | Type (wiki) | NPC |
    | Spawn group | `esfiume` |
    | Loot table | – |
    | Conversation | `esfiume0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:125` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "esfiume",
     "name": "Esfiume",
     "iconID": "monsters_ld1:125",
     "phraseID": "esfiume0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=esfiume.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=esfiume.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=esfiume.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=esfiume.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
