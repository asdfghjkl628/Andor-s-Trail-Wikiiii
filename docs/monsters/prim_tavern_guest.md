---
description: "Prim tavern guest is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_106.png){ .sprite } Prim tavern guest

**Where to find Prim tavern guest:** Prim: [Blackwater mountain 22](../maps/blackwater_mountain22.md#pin-npc-prim_tavern_guest)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_106.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Prim |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Prim tavern guest. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_tavern_guest1.json" data-npc="Prim tavern guest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_tavern_guest1"></span>**`prim_tavern_guest1`** Prim tavern guest: “Oh, a new one around here.”

    - Next → [prim_tavern_guest1_1](#d-prim_tavern_guest1_1)

    <span id="d-prim_tavern_guest1_1"></span>**`prim_tavern_guest1_1`** Prim tavern guest: “Welcome kid. Are you here to drench your sorrows like the rest of us?”

    - “Not really. What is there to do around here?” → [prim_tavern_guest1_3](#d-prim_tavern_guest1_3)
    - “Yeah, give me some of what you're having.” → [prim_tavern_guest1_4](#d-prim_tavern_guest1_4)
    - “Stop bumping into me when I'm trying to walk.” → [prim_tavern_guest1_2](#d-prim_tavern_guest1_2)

    <span id="d-prim_tavern_guest1_3"></span>**`prim_tavern_guest1_3`** Prim tavern guest: “Drink, of course!”

    - “I should have seen that one coming. Goodbye.” → *conversation ends*

    <span id="d-prim_tavern_guest1_4"></span>**`prim_tavern_guest1_4`** Prim tavern guest: “Hey, this one is mine. Buy your own mead from Birgil over there.”

    - “Sure, whatever.” → *conversation ends*
    - “OK.” → *conversation ends*

    <span id="d-prim_tavern_guest1_2"></span>**`prim_tavern_guest1_2`** Prim tavern guest: “My my, a feisty one. Very well, I will get out of your way.”




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
    | Entry ID | `prim_tavern_guest` |
    | Type (wiki) | NPC |
    | Spawn group | `prim_tavern_guest1` |
    | Loot table | – |
    | Conversation | `prim_tavern_guest1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:106` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_tavern_guest",
     "name": "Prim tavern guest",
     "iconID": "monsters_rltiles1:106",
     "monsterClass": "humanoid",
     "spawnGroup": "prim_tavern_guest1",
     "phraseID": "prim_tavern_guest1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_tavern_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
