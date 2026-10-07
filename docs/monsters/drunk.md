---
description: "Drunk is a non-player character (NPC) in Andor's Trail, found in Crossglen, Fallhaven, Loneford."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Drunk

**Where to find Drunk:** Crossglen: [crossglen_hall](../maps/crossglen_hall.md#pin-npc-drunk), Fallhaven: [fallhaven_tavern](../maps/fallhaven_tavern.md#pin-npc-drunk), Loneford: [loneford3](../maps/loneford3.md#pin-npc-drunk), Loneford: [loneford6](../maps/loneford6.md#pin-npc-drunk)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Crossglen, Fallhaven, Loneford |
| **Entry ID** | `drunk` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossglen_hall](../maps/crossglen_hall.md) | Crossglen | 3 | – |
| [fallhaven_tavern](../maps/fallhaven_tavern.md) | Fallhaven | 2 | – |
| [loneford3](../maps/loneford3.md) | Loneford | 2 | – |
| [loneford6](../maps/loneford6.md) | Loneford | 2 | – |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Drunk. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/drunk1.json" data-npc="Drunk" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-drunk1"></span>**`drunk1`** Drunk: “Drink drink drink, drink some more. Drink drink drink 'til you're on the floor. Hey kid, wanna join us in our drinking game?”

    - “No thanks.” → [drunk1a](#d-drunk1a)
    - “Maybe some other time.” → *conversation ends*

    <span id="d-drunk1a"></span>**`drunk1a`** Drunk: “Heeeey - come on. Don't be such a spoilsport.”

    - “Maybe some other time.” → *conversation ends*
    - “Well, if you really want to. But I have a new and definitive game for you. Here, drink this. [Give a bottle of weak…” *(if hand over 1× [Weak poison](../items/pot_poison_weak.md))* → [drunk1b](#d-drunk1b)

    <span id="d-drunk1b"></span>**`drunk1b`** Drunk: “Ohh ... [glug glug]”

    - Next → [drunk1c](#d-drunk1c)

    <span id="d-drunk1c"></span>**`drunk1c`** Drunk: “What an interesting ... [glug]”

    - Next → [drunk1d](#d-drunk1d)

    <span id="d-drunk1d"></span>**`drunk1d`** Drunk: “... taste [falls over]”

    - “Yes, really. A unique taste. And final - bye.” → [drunk1e](#d-drunk1e)

    <span id="d-drunk1e"></span>**`drunk1e`** *(silent check: the first matching branch below is taken)* — **effects:** faction “drunk1” +1

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 5 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `drunk` |
    | Spawn group | `drunk` |
    | Loot table | – |
    | Conversation | `drunk1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "drunk",
     "name": "Drunk",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "drunk",
     "phraseID": "drunk1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
