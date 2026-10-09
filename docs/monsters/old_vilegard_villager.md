---
description: "Old Vilegard villager is a non-player character (NPC) in Andor's Trail, found in Vilegard."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Old Vilegard villager

**Where to find Old Vilegard villager:** Vilegard: [Vilegard north](../maps/vilegard_n.md#pin-npc-old_vilegard_villager)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Vilegard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Old Vilegard villager. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/vilegard_villager_1.json" data-npc="Old Vilegard villager" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-vilegard_villager_1"></span>**`vilegard_villager_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [vilegard_villager_friend](#d-vilegard_villager_friend)
    - branch 2 → [vilegard_villager_1_0](#d-vilegard_villager_1_0)

    <span id="d-vilegard_villager_friend"></span>**`vilegard_villager_friend`** Old Vilegard villager: “Hello there. I heard you helped us common folk here in Vilegard. Please stay for as long as you like friend.”

    - “Thank you. Have you seen my brother Andor around here?” → [vilegard_villager_friend_1](#d-vilegard_villager_friend_1)
    - “Thank you. See you.” → *conversation ends*

    <span id="d-vilegard_villager_1_0"></span>**`vilegard_villager_1_0`** Old Vilegard villager: “Hello. Who are you? You are not welcome here in Vilegard.”

    - “Have you seen my brother, Andor, around here?” → [vilegard_villager_1_2](#d-vilegard_villager_1_2)

    <span id="d-vilegard_villager_friend_1"></span>**`vilegard_villager_friend_1`** Old Vilegard villager: “Your brother? No, I haven't seen anyone that looks like you. But then again, I never take much notice to outsiders.”

    - “Thanks, bye.” → *conversation ends*

    <span id="d-vilegard_villager_1_2"></span>**`vilegard_villager_1_2`** Old Vilegard villager: “No, I have certainly not. Even if I had, why would I tell you?”




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
    | Entry ID | `old_vilegard_villager` |
    | Type (wiki) | NPC |
    | Spawn group | `vilegard_villager_1` |
    | Loot table | – |
    | Conversation | `vilegard_villager_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "old_vilegard_villager",
     "name": "Old Vilegard villager",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "vilegard_villager_1",
     "phraseID": "vilegard_villager_1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_vilegard_villager.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_vilegard_villager.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_vilegard_villager.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_vilegard_villager.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
