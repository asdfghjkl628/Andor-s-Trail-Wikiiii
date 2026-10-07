---
description: "Shepherd is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_karvis2_7.png){ .sprite } Shepherd

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_7.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Shepherd. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_shephard`](#v-guynmart_shephard) | NPC | Guynmart Castle: [Guynmart wood 9](../maps/guynmart_wood_9.md#pin-npc-guynmart_shephard) | – |
| [`guynmart_shephard2`](#v-guynmart_shephard2) | NPC | Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_shephard2) | – |

## Guynmart Castle, Guynmart wood 9 (guynmart_shephard) { #v-guynmart_shephard }

**Entry ID:** `guynmart_shephard` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart wood 9](../maps/guynmart_wood_9.md#pin-npc-guynmart_shephard)

### Dialogue simulator

Set your quest stages and items, then talk to Shepherd. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_shephard_10.json" data-npc="Shepherd" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_shephard-guynmart_shephard_10"></span>**`guynmart_shephard_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_shephard_20](#d-guynmart_shephard-guynmart_shephard_20)
    - branch 2 *(if killed 20× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_shephard_30](#d-guynmart_shephard-guynmart_shephard_30)
    - branch 3 → [guynmart_shephard_12](#d-guynmart_shephard-guynmart_shephard_12)

    <span id="d-guynmart_shephard-guynmart_shephard_20"></span>**`guynmart_shephard_20`** Shepherd: “Grrumble ... grrrrumble...”

    - “Maybe he does not like his sheep being killed?” → *conversation ends*

    <span id="d-guynmart_shephard-guynmart_shephard_30"></span>**`guynmart_shephard_30`** Shepherd: “GRRRUMMBLE!!!”

    - “Obviously he does not like his sheep being killed.” → *conversation ends*

    <span id="d-guynmart_shephard-guynmart_shephard_12"></span>**`guynmart_shephard_12`** Shepherd: “Grumble ... grumble...”

    - “He seems to speak mostly to his dogs.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_shephard)"

    | | |
    |---|---|
    | Entry ID | `guynmart_shephard` |
    | Spawn group | `guynmart_shephard` |
    | Loot table | – |
    | Conversation | `guynmart_shephard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:7` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_shephard",
     "name": "Shepherd",
     "iconID": "monsters_karvis2:7",
     "monsterClass": "humanoid",
     "phraseID": "guynmart_shephard_10"
    }
    ```


## Guynmart Castle, Guynmart main 1 (guynmart_shephard2) { #v-guynmart_shephard2 }

**Entry ID:** `guynmart_shephard2` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_shephard2)

### Dialogue simulator

Set your quest stages and items, then talk to Shepherd. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_shephard_10.json" data-npc="Shepherd" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_shephard_10](#d-guynmart_shephard-guynmart_shephard_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_shephard2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_shephard2` |
    | Spawn group | `guynmart_shephard2` |
    | Loot table | – |
    | Conversation | `guynmart_shephard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:7` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_shephard2",
     "name": "Shepherd",
     "iconID": "monsters_karvis2:7",
     "monsterClass": "humanoid",
     "phraseID": "guynmart_shephard_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
