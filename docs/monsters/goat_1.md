---
description: "Goat is a non-player character (NPC) in Andor's Trail, found in Mt. Galmore, Stoutford, Way to sullengard east 11."
---

# ![](../assets/icons/monsters/monsters_ld2_0.png){ .sprite } Goat

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Mt. Galmore, Stoutford, Way to sullengard east 11 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Goat. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`goat_1`](#v-goat_1) | NPC | Mt. Galmore: [Galmore 24](../maps/galmore_24.md#pin-npc-goat_1), Stoutford: [Stoutford south-west](../maps/stoutford_sw.md#pin-npc-goat_1) | – |
| [`sullengard_goat_standing`](#v-sullengard_goat_standing) | NPC | [Way to sullengard east 11](../maps/way_to_sullengard_east11.md#pin-npc-sullengard_goat_standing) | – |

## Mt. Galmore, Galmore 24 and 1 more (goat_1) { #v-goat_1 }

**Entry ID:** `goat_1` · **Type:** NPC

**Location:** Mt. Galmore: [Galmore 24](../maps/galmore_24.md#pin-npc-goat_1), Stoutford: [Stoutford south-west](../maps/stoutford_sw.md#pin-npc-goat_1)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 24](../maps/galmore_24.md) | Mt. Galmore | 1 | – |
| [Stoutford south-west](../maps/stoutford_sw.md) | Stoutford | 6 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Goat. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/goat_0.json" data-npc="Goat" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-goat_1-goat_0"></span>**`goat_0`** Goat: “Baaaaaa!”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (goat_1)"

    | | |
    |---|---|
    | Entry ID | `goat_1` |
    | Spawn group | `goat_1` |
    | Loot table | – |
    | Conversation | `goat_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:0` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "goat_1",
     "name": "Goat",
     "iconID": "monsters_ld2:0",
     "phraseID": "goat_0"
    }
    ```


## Way to sullengard east 11 (sullengard_goat_standing) { #v-sullengard_goat_standing }

**Entry ID:** `sullengard_goat_standing` · **Type:** NPC

**Location:** [Way to sullengard east 11](../maps/way_to_sullengard_east11.md#pin-npc-sullengard_goat_standing)

### Dialogue simulator

Set your quest stages and items, then talk to Goat. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_goat_0.json" data-npc="Goat" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_goat_standing-sullengard_goat_0"></span>**`sullengard_goat_0`** Goat: “Baa.”




### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (sullengard_goat_standing)"

    | | |
    |---|---|
    | Entry ID | `sullengard_goat_standing` |
    | Spawn group | `sullengard_goat_standing` |
    | Loot table | – |
    | Conversation | `sullengard_goat_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:0` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_goat_standing",
     "name": "Goat",
     "iconID": "monsters_ld2:0",
     "monsterClass": "animal",
     "spawnGroup": "sullengard_goat_standing",
     "phraseID": "sullengard_goat_0"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=goat_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=goat_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=goat_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=goat_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
