---
description: "Pig is a non-player character (NPC) in Andor's Trail, found in Loneford, Sullengard, Deebo's Orchard, mountainlake_circe."
---

# ![](../assets/icons/monsters/monsters_rltiles2_106.png){ .sprite } Pig

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_106.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Loneford, Sullengard, Deebo's Orchard, mountainlake_circe |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Pig. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`pig`](#v-pig) | NPC | Deebo's Orchard: [sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md#pin-npc-pig), Fallhaven: [woodsettlement0](../maps/woodsettlement0.md#pin-npc-pig) (+3 more) | – |
| [`ll2_circe_pig`](#v-ll2_circe_pig) | NPC | [mountainlake_circe](../maps/mountainlake_circe.md#pin-npc-ll2_circe_pig) | – |

## Deebo's Orchard, Sullengard apple farm east and 4 more (pig) { #v-pig }

**Entry ID:** `pig` · **Type:** NPC

**Location:** Deebo's Orchard: [sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md#pin-npc-pig), Fallhaven: [woodsettlement0](../maps/woodsettlement0.md#pin-npc-pig), Loneford: [loneford2](../maps/loneford2.md#pin-npc-pig), Sullengard: [sullengard1](../maps/sullengard1.md#pin-npc-pig), [waterwayb4](../maps/waterwayb4.md#pin-npc-pig)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [loneford2](../maps/loneford2.md) | Loneford | 2 | – |
| [sullengard1](../maps/sullengard1.md) | Sullengard | 1 | – |
| [sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md) | Deebo's Orchard | 2 | – |
| [waterwayb4](../maps/waterwayb4.md) | – | 2 | – |
| [woodsettlement0](../maps/woodsettlement0.md) | Fallhaven | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Pig. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/pig.json" data-npc="Pig" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-pig-pig"></span>**`pig`** Pig: “[Grunt]”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “[grunt]” → “[Grunt]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (pig)"

    | | |
    |---|---|
    | Entry ID | `pig` |
    | Spawn group | `pig` |
    | Loot table | – |
    | Conversation | `pig` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:106` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "pig",
     "name": "Pig",
     "iconID": "monsters_rltiles2:106",
     "monsterClass": "animal",
     "spawnGroup": "pig",
     "phraseID": "pig"
    }
    ```


## Mountainlake circe (ll2_circe_pig) { #v-ll2_circe_pig }

**Entry ID:** `ll2_circe_pig` · **Type:** NPC

**Location:** [mountainlake_circe](../maps/mountainlake_circe.md#pin-npc-ll2_circe_pig)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Pig. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_circe_pig.json" data-npc="Pig" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_circe_pig-ll2_circe_pig"></span>**`ll2_circe_pig`** Pig: “Oink oink.”




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_circe_pig)"

    | | |
    |---|---|
    | Entry ID | `ll2_circe_pig` |
    | Spawn group | `ll2_circe_pig` |
    | Loot table | – |
    | Conversation | `ll2_circe_pig` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:106` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_circe_pig",
     "name": "Pig",
     "iconID": "monsters_rltiles2:106",
     "monsterClass": "animal",
     "spawnGroup": "ll2_circe_pig",
     "horizontalFlipChance": 100,
     "phraseID": "ll2_circe_pig"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pig.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
