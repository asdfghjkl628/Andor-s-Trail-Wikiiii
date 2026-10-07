---
description: "Playing child is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_21.png){ .sprite } Playing child

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_21.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "3 entries in the game data"
    The game data defines 3 separate characters named Playing child. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: appearance. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`brv_playing_child2`](#v-brv_playing_child2) | NPC | Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child2) | – |
| [`brv_playing_child3`](#v-brv_playing_child3) | NPC | Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child3) | – |
| [`brv_playing_child4`](#v-brv_playing_child4) | NPC | Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child4) | – |

## Brimhaven, Brimhaven 3 (brv_playing_child2) { #v-brv_playing_child2 }

**Entry ID:** `brv_playing_child2` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child2)

### Dialogue simulator

Set your quest stages and items, then talk to Playing child. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_playing_children.json" data-npc="Playing child" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_playing_child2-brv_playing_children"></span>**`brv_playing_children`** [Playing children](../monsters/brv_playing_child1.md): “Don't disturb our game. Go away!”

    - “I am sorry.” → *conversation ends*
    - “What are you playing?” → [brv_playing_children_10](#d-brv_playing_child2-brv_playing_children_10)

    <span id="d-brv_playing_child2-brv_playing_children_10"></span>**`brv_playing_children_10`** Playing child: “We are practicing 'Ba game'. Once a year the west and the east parts of the town play against each other. It can be very competitive.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_playing_child2)"

    | | |
    |---|---|
    | Entry ID | `brv_playing_child2` |
    | Spawn group | `brv_playing_child2` |
    | Loot table | – |
    | Conversation | `brv_playing_children` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:21` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_playing_child2",
     "name": "Playing child",
     "iconID": "monsters_ld1:21",
     "phraseID": "brv_playing_children"
    }
    ```


## Brimhaven, Brimhaven 3 (brv_playing_child3) { #v-brv_playing_child3 }

**Entry ID:** `brv_playing_child3` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child3)

### Dialogue simulator

Set your quest stages and items, then talk to Playing child. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_playing_children.json" data-npc="Playing child" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_playing_children](#d-brv_playing_child2-brv_playing_children).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_playing_child3)"

    | | |
    |---|---|
    | Entry ID | `brv_playing_child3` |
    | Spawn group | `brv_playing_child3` |
    | Loot table | – |
    | Conversation | `brv_playing_children` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:36` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_playing_child3",
     "name": "Playing child",
     "iconID": "monsters_ld1:36",
     "phraseID": "brv_playing_children"
    }
    ```


## Brimhaven, Brimhaven 3 (brv_playing_child4) { #v-brv_playing_child4 }

**Entry ID:** `brv_playing_child4` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven 3](../maps/brimhaven3.md#pin-npc-brv_playing_child4)

### Dialogue simulator

Set your quest stages and items, then talk to Playing child. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_playing_children.json" data-npc="Playing child" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_playing_children](#d-brv_playing_child2-brv_playing_children).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_playing_child4)"

    | | |
    |---|---|
    | Entry ID | `brv_playing_child4` |
    | Spawn group | `brv_playing_child4` |
    | Loot table | – |
    | Conversation | `brv_playing_children` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:37` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_playing_child4",
     "name": "Playing child",
     "iconID": "monsters_ld1:37",
     "phraseID": "brv_playing_children"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_playing_child2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_playing_child2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_playing_child2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_playing_child2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
