---
description: "Rambling Feygard guard is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Rambling Feygard guard

**Where to find Rambling Feygard guard:** Loneford: [Lodar 2](../maps/lodar2.md#pin-npc-lodar_fg2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Loneford |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [A lost potion](../quests/lodar.md): stage 71

## Dialogue simulator

Set your quest stages and items, then talk to Rambling Feygard guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/lodar_fg2.json" data-npc="Rambling Feygard guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lodar_fg2"></span>**`lodar_fg2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50))* → [lodar_fg2_a](#d-lodar_fg2_a)
    - branch 2 → [lodar_fg2_0](#d-lodar_fg2_0)

    <span id="d-lodar_fg2_a"></span>**`lodar_fg2_a`** Rambling Feygard guard: “Ouch, my head. It hurts so much.”


    <span id="d-lodar_fg2_0"></span>**`lodar_fg2_0`** Rambling Feygard guard: “What? Who are you?”

    - “I'm $playername.” → [lodar_fg2_1](#d-lodar_fg2_1)
    - “Why would I tell you?” → [lodar_fg2_1](#d-lodar_fg2_1)

    <span id="d-lodar_fg2_1"></span>**`lodar_fg2_1`** Rambling Feygard guard: “No no. You are too small. You can't be him.”

    - Next → [lodar_fg2_2](#d-lodar_fg2_2)

    <span id="d-lodar_fg2_2"></span>**`lodar_fg2_2`** Rambling Feygard guard: “Crazy old fool, that's what they said he'd be.”

    - “Who?” → [lodar_fg2_3](#d-lodar_fg2_3)

    <span id="d-lodar_fg2_3"></span>**`lodar_fg2_3`** Rambling Feygard guard: “Ha ha. Crazy!”

    - Next → [lodar_fg2_4](#d-lodar_fg2_4)

    <span id="d-lodar_fg2_4"></span>**`lodar_fg2_4`** Rambling Feygard guard: “[The guard mumbles something that you can't understand]”

    - Next → [lodar_fg2_5](#d-lodar_fg2_5)

    <span id="d-lodar_fg2_5"></span>**`lodar_fg2_5`** Rambling Feygard guard: “Must get away! Soon we all will be able to see it.”

    - “See what?” → [lodar_fg2_6](#d-lodar_fg2_6)

    <span id="d-lodar_fg2_6"></span>**`lodar_fg2_6`** Rambling Feygard guard: “[The guard continues with his mumbling]” — **effects:** sets stage 71 of [A lost potion](../quests/lodar.md#stage-71)

    - “Hello?” → [lodar_fg2_1](#d-lodar_fg2_1)
    - “Are you even listening to me?” → [lodar_fg2_1](#d-lodar_fg2_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “(the guard mumbles something that you can't understand)” → “[The guard mumbles something that you can't understand]”<br>· text: “(the guard continues with his mumbling)” → “[The guard continues with his mumbling]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lodar_fg2` |
    | Type (wiki) | NPC |
    | Spawn group | `lodar_fg2` |
    | Loot table | – |
    | Conversation | `lodar_fg2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v070_lodarnpcs.json` |

    Raw data:

    ```json
    {
     "id": "lodar_fg2",
     "name": "Rambling Feygard guard",
     "iconID": "monsters_rltiles3:14",
     "spawnGroup": "lodar_fg2",
     "phraseID": "lodar_fg2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
