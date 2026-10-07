---
description: "Brightport commoner is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Brightport commoner

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Brightport commoner. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`brightportcitizen`](#v-brightportcitizen) | NPC | Brightport: [brightport1](../maps/brightport1.md#pin-npc-brightportcitizen), Brightport: [brightport3](../maps/brightport3.md#pin-npc-brightportcitizen) | – |
| [`brightportcitizen1`](#v-brightportcitizen1) | NPC | Brightport: [brightport5](../maps/brightport5.md#pin-npc-brightportcitizen1) | – |

## Brightport, Brightport1 and 1 more (brightportcitizen) { #v-brightportcitizen }

**Entry ID:** `brightportcitizen` · **Type:** NPC

**Location:** Brightport: [brightport1](../maps/brightport1.md#pin-npc-brightportcitizen), Brightport: [brightport3](../maps/brightport3.md#pin-npc-brightportcitizen)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport1](../maps/brightport1.md) | Brightport | 1 | – |
| [brightport3](../maps/brightport3.md) | Brightport | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Brightport commoner. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_citizen0.json" data-npc="Brightport commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightportcitizen-brightport_citizen0"></span>**`brightport_citizen0`** [Brightport commoner](../monsters/brightportcitizen.md): “Excuse me, I have no time for discussion.”

    - “Neither do I.” → *conversation ends*
    - “How boorish.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportcitizen)"

    | | |
    |---|---|
    | Entry ID | `brightportcitizen` |
    | Spawn group | `brightportcitizen` |
    | Loot table | – |
    | Conversation | `brightport_citizen0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportcitizen",
     "name": "Brightport commoner",
     "iconID": "monsters_man1:0",
     "unique": 1,
     "phraseID": "brightport_citizen0"
    }
    ```


## Brightport, Brightport5 (brightportcitizen1) { #v-brightportcitizen1 }

**Entry ID:** `brightportcitizen1` · **Type:** NPC

**Location:** Brightport: [brightport5](../maps/brightport5.md#pin-npc-brightportcitizen1)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Brightport commoner. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_citizen.json" data-npc="Brightport commoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightportcitizen1-brightport_citizen"></span>**`brightport_citizen`** [Brightport commoner](../monsters/brightportcitizen.md#v-brightportcitizen1): “Sigh. Nowadays, the streets are always bustling with clamor, and everyone seems to be in a hurry. I miss the days when I could quietly sit and gaze at the lake.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportcitizen1)"

    | | |
    |---|---|
    | Entry ID | `brightportcitizen1` |
    | Spawn group | `brightportcitizen1` |
    | Loot table | – |
    | Conversation | `brightport_citizen` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:12` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportcitizen1",
     "name": "Brightport commoner",
     "iconID": "monsters_ld1:12",
     "unique": 1,
     "phraseID": "brightport_citizen"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportcitizen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
