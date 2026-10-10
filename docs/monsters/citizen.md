---
description: "Citizen is a non-player character (NPC) in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Citizen

**Where to find Citizen:** Fallhaven: [Fallhaven north-east](../maps/fallhaven_ne.md#pin-npc-citizen), Fallhaven: [Fallhaven south-west](../maps/fallhaven_sw.md#pin-npc-citizen)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Fallhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Fallhaven north-east](../maps/fallhaven_ne.md) | Fallhaven | 1 | – |
| [Fallhaven south-west](../maps/fallhaven_sw.md) | Fallhaven | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Citizen. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_citizen3.json" data-npc="Citizen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_citizen3"></span>**`fallhaven_citizen3`** Citizen: “Hi. Can I help you?”

    - “Have you seen my brother Andor? He looks a bit like me.” → [fallhaven_andor_3](#d-fallhaven_andor_3)

    <span id="d-fallhaven_andor_3"></span>**`fallhaven_andor_3`** Citizen: “Hmm, I might have seen someone that looks a bit like you a few days ago. Can't remember where though.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Hm, I might have seen someone matching that description a few days ag…” → “Hmm, I might have seen someone matching that description a few days a…” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 2 lines changed<br>· text: “Hmm, I might have seen someone matching that description a few days a…” → “Hmm, I might have seen someone that looks a bit like you a few days a…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `citizen` |
    | Type (wiki) | NPC |
    | Spawn group | `fallhaven_citizen3` |
    | Loot table | – |
    | Conversation | `fallhaven_citizen3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "citizen",
     "name": "Citizen",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_citizen3",
     "phraseID": "fallhaven_citizen3"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
