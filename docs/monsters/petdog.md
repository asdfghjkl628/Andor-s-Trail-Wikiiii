---
description: "Dog is a non-player character (NPC) in Andor's Trail, found in Remgard, Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_dogs_0.png){ .sprite } Dog

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Remgard, Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Dog. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`petdog`](#v-petdog) | NPC | Remgard: [Remgard villager 4](../maps/remgard_villager4.md#pin-npc-petdog) | – |
| [`guynmart_dog10`](#v-guynmart_dog10) | NPC | Guynmart Castle: [Guynmart wood 10](../maps/guynmart_wood_10.md#pin-npc-guynmart_dog10), Guynmart Castle: [Guynmart wood 11](../maps/guynmart_wood_11.md#pin-npc-guynmart_dog10) | – |

## Remgard, Remgard villager 4 (petdog) { #v-petdog }

**Entry ID:** `petdog` · **Type:** NPC

**Location:** Remgard: [Remgard villager 4](../maps/remgard_villager4.md#pin-npc-petdog)

### Dialogue simulator

Set your quest stages and items, then talk to Dog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/petdog.json" data-npc="Dog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-petdog-petdog"></span>**`petdog`** Dog: “Woof! *pant* *pant*”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (petdog)"

    | | |
    |---|---|
    | Entry ID | `petdog` |
    | Spawn group | `petdog` |
    | Loot table | – |
    | Conversation | `petdog` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:0` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "petdog",
     "name": "Dog",
     "iconID": "monsters_dogs:0",
     "monsterClass": "animal",
     "spawnGroup": "petdog",
     "phraseID": "petdog"
    }
    ```


## Guynmart Castle, Guynmart wood 10 and 1 more (guynmart_dog10) { #v-guynmart_dog10 }

**Entry ID:** `guynmart_dog10` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart wood 10](../maps/guynmart_wood_10.md#pin-npc-guynmart_dog10), Guynmart Castle: [Guynmart wood 11](../maps/guynmart_wood_11.md#pin-npc-guynmart_dog10)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart wood 10](../maps/guynmart_wood_10.md) | Guynmart Castle | 6 | – |
| [Guynmart wood 11](../maps/guynmart_wood_11.md) | Guynmart Castle | 6 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Dog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_dog10_10.json" data-npc="Dog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_dog10-guynmart_dog10_10"></span>**`guynmart_dog10_10`** [Dog](../monsters/petdog.md#v-guynmart_dog10): “Grrrrrr”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_dog10)"

    | | |
    |---|---|
    | Entry ID | `guynmart_dog10` |
    | Spawn group | `guynmart_dog10` |
    | Loot table | – |
    | Conversation | `guynmart_dog10_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_dog10",
     "name": "Dog",
     "iconID": "monsters_dogs:4",
     "monsterClass": "animal",
     "phraseID": "guynmart_dog10_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=petdog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=petdog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=petdog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=petdog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
