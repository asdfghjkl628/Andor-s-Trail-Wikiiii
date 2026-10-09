---
description: "Terrified teenager is a non-player character (NPC) in Andor's Trail, found in Undertell 3 12."
---

# ![](../assets/icons/monsters/monsters_gisons_14.png){ .sprite } Terrified teenager

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Undertell 3 12 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "3 entries in the game data"
    The game data defines 3 separate characters named Terrified teenager. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, movement. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`about_a_girl1`](#v-about_a_girl1) | NPC | [Undertell 3 12](../maps/undertell_3_12.md#pin-npc-about_a_girl1) | – |
| [`about_a_girl_flee`](#v-about_a_girl_flee) | Scenery | [Undertell 3 12](../maps/undertell_3_12.md) | – |
| [`about_a_girl_hidden`](#v-about_a_girl_hidden) | Scenery | [Undertell 3 12](../maps/undertell_3_12.md) | – |

## Undertell 3 12 (about_a_girl1) { #v-about_a_girl1 }

**Entry ID:** `about_a_girl1` · **Type:** NPC

**Location:** [Undertell 3 12](../maps/undertell_3_12.md#pin-npc-about_a_girl1)

### Quests

- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 90

### Dialogue simulator

Set your quest stages and items, then talk to Terrified teenager. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/about_girl_scream_10.json" data-npc="Terrified teenager" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-about_a_girl1-about_girl_scream_10"></span>**`about_girl_scream_10`** [Terrified teenager](../monsters/about_a_girl1.md#v-about_a_girl_hidden): “HELP! SOMEBODY HELP ME!”

    - “What is wrong?” → [about_girl_scream_20](#d-about_a_girl1-about_girl_scream_20)

    <span id="d-about_a_girl1-about_girl_scream_20"></span>**`about_girl_scream_20`** Terrified teenager: “STAY AWAY FROM ME!” — **effects:** removes monsters from undertell_3_12, spawns monsters on undertell_3_12, sets stage 90 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-90)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl1)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl1` |
    | Spawn group | `about_a_girl1` |
    | Loot table | – |
    | Conversation | `about_girl_scream_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl1",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 50,
     "phraseID": "about_girl_scream_10"
    }
    ```


## Undertell 3 12 (about_a_girl_flee) { #v-about_a_girl_flee }

**Entry ID:** `about_a_girl_flee` · **Type:** Scenery

**Location:** [Undertell 3 12](../maps/undertell_3_12.md)

!!! note "Scenery"
    No conversation and no combat statistics: a decoration, an animal or a figure in a scripted scene that also speaks lines in someone else's dialogue.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl_flee)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_flee` |
    | Spawn group | `about_a_girl_flee` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | flee |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_flee",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "movementAggressionType": "flee",
     "horizontalFlipChance": 50
    }
    ```


## Undertell 3 12 (about_a_girl_hidden) { #v-about_a_girl_hidden }

**Entry ID:** `about_a_girl_hidden` · **Type:** Scenery

**Location:** [Undertell 3 12](../maps/undertell_3_12.md)

!!! note "Scenery"
    No conversation and no combat statistics: a decoration, an animal or a figure in a scripted scene that also speaks lines in someone else's dialogue.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (about_a_girl_hidden)"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_hidden` |
    | Spawn group | `about_a_girl_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_hidden",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 0
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
