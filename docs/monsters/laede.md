---
description: "Laede is a non-player character (NPC) in Andor's Trail, found in Blackwater mountain 44."
---

# ![](../assets/icons/monsters/monsters_rltiles1_81.png){ .sprite } Laede

**Where to find Laede:** [Blackwater mountain 44](../maps/blackwater_mountain44.md#pin-npc-laede)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_81.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Blackwater mountain 44 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [General story flags (hidden flag)](../quests/nondisplay.md): stage 16

## Dialogue simulator

Set your quest stages and items, then talk to Laede. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/laede.json" data-npc="Laede" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-laede"></span>**`laede`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [laede_1](#d-laede_1)
    - branch 2 → [laede_3](#d-laede_3)

    <span id="d-laede_1"></span>**`laede_1`** Laede: “You are welcome to rest here if you want. Pick any bed you wish.” — **effects:** sets stage 16 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-16)

    - Next → [laede_2](#d-laede_2)

    <span id="d-laede_3"></span>**`laede_3`** Laede: “Welcome traveller. These beds are only for residents of Blackwater mountain.”


    <span id="d-laede_2"></span>**`laede_2`** Laede: “I should warn you though that the one in the corner over there has a rotten stench to it. Someone must have spilled something onto it.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “Welcome traveller. These beds are only for residents of Blackwater Mo…” → “Welcome traveller. These beds are only for residents of Blackwater mo…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `laede` |
    | Type (wiki) | NPC |
    | Spawn group | `blackwater_sleephall` |
    | Loot table | – |
    | Conversation | `laede` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:81` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "laede",
     "name": "Laede",
     "iconID": "monsters_rltiles1:81",
     "monsterClass": "humanoid",
     "spawnGroup": "blackwater_sleephall",
     "phraseID": "laede"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laede.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laede.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laede.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laede.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
