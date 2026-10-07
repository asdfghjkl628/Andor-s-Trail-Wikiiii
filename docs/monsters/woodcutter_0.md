---
description: "Woodcutter is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse, Brimhaven."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Woodcutter

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Crossroads Guardhouse, Brimhaven |
| **Entries in game data** | 6 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "6 entries in the game data"
    The game data defines 6 separate characters named Woodcutter. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`woodcutter_0`](#v-woodcutter_0) | NPC | Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_0) | – |
| [`brv_woodcutter`](#v-brv_woodcutter) | NPC | Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_woodcutter) | – |
| [`woodcutter_2`](#v-woodcutter_2) | NPC | Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_2) | – |
| [`woodcutter_3`](#v-woodcutter_3) | NPC | Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_3) | – |
| [`woodcutter_4`](#v-woodcutter_4) | NPC | Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_4) | – |
| [`woodcutter_5`](#v-woodcutter_5) | NPC | Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_5) | – |

## Crossroads Guardhouse, Roadtocarntower 1 (woodcutter_0) { #v-woodcutter_0 }

**Entry ID:** `woodcutter_0` · **Type:** NPC

**Location:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_0)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/woodcutter_0.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-woodcutter_0-woodcutter_0"></span>**`woodcutter_0`** Woodcutter: “Stupid wasps...”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Stupid wasps..” → “Stupid wasps...” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (woodcutter_0)"

    | | |
    |---|---|
    | Entry ID | `woodcutter_0` |
    | Spawn group | `woodcutter_0` |
    | Loot table | – |
    | Conversation | `woodcutter_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "woodcutter_0",
     "name": "Woodcutter",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "woodcutter_0",
     "phraseID": "woodcutter_0"
    }
    ```


## Brimhaven, Brimhaven 2 (brv_woodcutter) { #v-brv_woodcutter }

**Entry ID:** `brv_woodcutter` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven 2](../maps/brimhaven2.md#pin-npc-brv_woodcutter)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_woodcutter_0.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_woodcutter-brv_woodcutter_0"></span>**`brv_woodcutter_0`** Woodcutter: “[Cutting wood]”

    - “Hello” → [brv_woodcutter_1](#d-brv_woodcutter-brv_woodcutter_1)

    <span id="d-brv_woodcutter-brv_woodcutter_1"></span>**`brv_woodcutter_1`** Woodcutter: “[Stops cutting wood] If you want to buy some wood cutting tools or wood products then just go inside. [Continues cutting wood]”

    - “Bye” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_woodcutter)"

    | | |
    |---|---|
    | Entry ID | `brv_woodcutter` |
    | Spawn group | `brv_woodcutter` |
    | Loot table | – |
    | Conversation | `brv_woodcutter_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:39` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_woodcutter",
     "name": "Woodcutter",
     "iconID": "monsters_tometik2:39",
     "phraseID": "brv_woodcutter_0"
    }
    ```


## Crossroads Guardhouse, Roadtocarntower 1 (woodcutter_2) { #v-woodcutter_2 }

**Entry ID:** `woodcutter_2` · **Type:** NPC

**Location:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_2)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/woodcutter_2.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-woodcutter_2-woodcutter_2"></span>**`woodcutter_2`** Woodcutter: “Stay away from the road to the west, for it leads to Carn Tower. You most certainly do not want to go there.”

    - Next → [woodcutter_1](#d-woodcutter_2-woodcutter_1)

    <span id="d-woodcutter_2-woodcutter_1"></span>**`woodcutter_1`** Woodcutter: “When travelling, keep to the roads. Veer off course and you might find yourself in danger.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (woodcutter_2)"

    | | |
    |---|---|
    | Entry ID | `woodcutter_2` |
    | Spawn group | `woodcutter_2` |
    | Loot table | – |
    | Conversation | `woodcutter_2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "woodcutter_2",
     "name": "Woodcutter",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "woodcutter_2",
     "phraseID": "woodcutter_2"
    }
    ```


## Crossroads Guardhouse, Roadtocarntower 1 (woodcutter_3) { #v-woodcutter_3 }

**Entry ID:** `woodcutter_3` · **Type:** NPC

**Location:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_3)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/woodcutter_3.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-woodcutter_3-woodcutter_3"></span>**`woodcutter_3`** Woodcutter: “Maybe we shouldn't have cut down all the trees over there. Those wasps really seem upset.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (woodcutter_3)"

    | | |
    |---|---|
    | Entry ID | `woodcutter_3` |
    | Spawn group | `woodcutter_3` |
    | Loot table | – |
    | Conversation | `woodcutter_3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:2` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "woodcutter_3",
     "name": "Woodcutter",
     "iconID": "monsters_men2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "woodcutter_3",
     "phraseID": "woodcutter_3"
    }
    ```


## Crossroads Guardhouse, Roadtocarntower 1 (woodcutter_4) { #v-woodcutter_4 }

**Entry ID:** `woodcutter_4` · **Type:** NPC

**Location:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_4)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/woodcutter_4.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-woodcutter_4-woodcutter_4"></span>**`woodcutter_4`** Woodcutter: “I can still feel the sting from those wasps in my legs. Good thing we are done with all the trees now.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (woodcutter_4)"

    | | |
    |---|---|
    | Entry ID | `woodcutter_4` |
    | Spawn group | `woodcutter_4` |
    | Loot table | – |
    | Conversation | `woodcutter_4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:93` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "woodcutter_4",
     "name": "Woodcutter",
     "iconID": "monsters_rltiles1:93",
     "monsterClass": "humanoid",
     "spawnGroup": "woodcutter_4",
     "phraseID": "woodcutter_4"
    }
    ```


## Crossroads Guardhouse, Roadtocarntower 1 (woodcutter_5) { #v-woodcutter_5 }

**Entry ID:** `woodcutter_5` · **Type:** NPC

**Location:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-woodcutter_5)

### Dialogue simulator

Set your quest stages and items, then talk to Woodcutter. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/woodcutter_5.json" data-npc="Woodcutter" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-woodcutter_5-woodcutter_5"></span>**`woodcutter_5`** Woodcutter: “Hello there, welcome to our encampment. You should talk to Hadracor over there.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (woodcutter_5)"

    | | |
    |---|---|
    | Entry ID | `woodcutter_5` |
    | Spawn group | `woodcutter_5` |
    | Loot table | – |
    | Conversation | `woodcutter_5` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:2` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "woodcutter_5",
     "name": "Woodcutter",
     "iconID": "monsters_men2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "woodcutter_5",
     "phraseID": "woodcutter_5"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=woodcutter_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=woodcutter_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=woodcutter_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=woodcutter_0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
