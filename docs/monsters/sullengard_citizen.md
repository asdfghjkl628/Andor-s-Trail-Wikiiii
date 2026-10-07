---
description: "Local citizen is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_112.png){ .sprite } Local citizen

**Where to find Local citizen:** Sullengard: [sullengard1](../maps/sullengard1.md#pin-npc-sullengard_citizen)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_112.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Sullengard |
| **Entry ID** | `sullengard_citizen` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Local citizen. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_citizen_0.json" data-npc="Local citizen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_citizen_0"></span>**`sullengard_citizen_0`** Local citizen: “Are you here for the beer festival?”

    - “Yes.” → [sullengard_citizen_festival](#d-sullengard_citizen_festival)
    - “Actually, I'm here looking for someone...my brother.” → [sullengard_citizen_andor](#d-sullengard_citizen_andor)
    - “I was hoping that you knew where I can find Celdar? I was told that this is her hometown.” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-123) is 123)* → [sullengard_citizen_celdar](#d-sullengard_citizen_celdar)

    <span id="d-sullengard_citizen_festival"></span>**`sullengard_citizen_festival`** Local citizen: “Well in that case, you are a couple of weeks early.”


    <span id="d-sullengard_citizen_andor"></span>**`sullengard_citizen_andor`** Local citizen: “Your brother you say? Maybe I can help. Tell me about him.”

    - “Well there's not much to say really except his name is Andor and he looks sort of like me.” → [sullengard_citizen_andor_10](#d-sullengard_citizen_andor_10)

    <span id="d-sullengard_citizen_celdar"></span>**`sullengard_citizen_celdar`** Local citizen: “I thought you were looking for your brother? What's the matter, you couldn't find Andor, so you gave up and are now looking for someone new?”

    - “Very funny.” → *conversation ends*

    <span id="d-sullengard_citizen_andor_10"></span>**`sullengard_citizen_andor_10`** Local citizen: “"Andor" you say? Why do I know that name...hmm...”

    - “You've heard of him?!” → [sullengard_citizen_andor_20](#d-sullengard_citizen_andor_20)

    <span id="d-sullengard_citizen_andor_20"></span>**`sullengard_citizen_andor_20`** Local citizen: “Maybe, but I'm not really sure. I think you should ask Mayor Ale.”

    - “Thank you so much.” → *conversation ends*
    - “Well you were nothing but a tease. Thanks a lot!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 5 lines added |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_citizen` |
    | Spawn group | `sullengard_citizen` |
    | Loot table | – |
    | Conversation | `sullengard_citizen_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:112` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_citizen",
     "name": "Local citizen",
     "iconID": "monsters_ld1:112",
     "spawnGroup": "sullengard_citizen",
     "phraseID": "sullengard_citizen_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_citizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
