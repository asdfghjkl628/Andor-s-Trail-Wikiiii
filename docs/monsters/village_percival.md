---
description: "Percival is a non-player character (NPC) in Andor's Trail, found in Wexlow Village, Gamjee well 4 1, Gamjee well jail cells."
---

# ![](../assets/icons/monsters/monsters_ld1_140.png){ .sprite } Percival

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_140.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Wexlow Village, Gamjee well 4 1, Gamjee well jail cells |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Percival. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`village_percival`](#v-village_percival) | NPC | Wexlow Village: [Wexlow village south-east house](../maps/wexlow_village_se_house.md#pin-npc-village_percival) | – |
| [`troll_hollow_percival`](#v-troll_hollow_percival) | NPC | [Gamjee well 4 1](../maps/gamjee_well_4_1.md#pin-npc-troll_hollow_percival), [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md#pin-npc-troll_hollow_percival) | – |

## Wexlow Village, Wexlow village south-east house (village_percival) { #v-village_percival }

**Entry ID:** `village_percival` · **Type:** NPC

**Location:** Wexlow Village: [Wexlow village south-east house](../maps/wexlow_village_se_house.md#pin-npc-village_percival)

### Dialogue simulator

Set your quest stages and items, then talk to Percival. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/village_percival_start.json" data-npc="Percival" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-village_percival-village_percival_start"></span>**`village_percival_start`** Percival: “Thank you for rescuing us earlier! I would have done it myself but...”

    - “You are pathetic?” → [village_percival_rude](#d-village_percival-village_percival_rude)
    - “You did not have The Shadow with you.” → [village_percival_shadow](#d-village_percival-village_percival_shadow)
    - “What about the state of your house? It's a mess now.” → [village_percival_cleanup](#d-village_percival-village_percival_cleanup)

    <span id="d-village_percival-village_percival_rude"></span>**`village_percival_rude`** Percival: “Now watch it, kid!”


    <span id="d-village_percival-village_percival_shadow"></span>**`village_percival_shadow`** Percival: “The Shadow? You don't believe in that nonsense, do you?”

    - “Shadow be with you.” → *conversation ends*
    - “Me? No way! I was just kidding. Glory be to Feygard.” → [glory_be_to_feygard](#d-village_percival-glory_be_to_feygard)

    <span id="d-village_percival-village_percival_cleanup"></span>**`village_percival_cleanup`** Percival: “Can you believe it? It'll take weeks to clear out all the cobwebs. It's like the spiders moved in the moment we disappeared. And the food... oh, the smell of it all rotting away. It's a mess.”

    - “Good luck with all that.” → *conversation ends*

    <span id="d-village_percival-glory_be_to_feygard"></span>**`glory_be_to_feygard`** Percival: “Glory be to Feygard.”




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (village_percival)"

    | | |
    |---|---|
    | Entry ID | `village_percival` |
    | Spawn group | `village_percival` |
    | Loot table | – |
    | Conversation | `village_percival_start` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:140` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_percival",
     "name": "Percival",
     "iconID": "monsters_ld1:140",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "village_percival_start"
    }
    ```


## Gamjee well 4 1 and 1 more (troll_hollow_percival) { #v-troll_hollow_percival }

**Entry ID:** `troll_hollow_percival` · **Type:** NPC

**Location:** [Gamjee well 4 1](../maps/gamjee_well_4_1.md#pin-npc-troll_hollow_percival), [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md#pin-npc-troll_hollow_percival)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Gamjee well 4 1](../maps/gamjee_well_4_1.md) | – | 1 | Appears later, during a quest |
| [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md) | – | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Percival. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/perciva_int_phrasel.json" data-npc="Percival" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-troll_hollow_percival-perciva_int_phrasel"></span>**`perciva_int_phrasel`** Percival: “What are you doing? Help us!”




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (troll_hollow_percival)"

    | | |
    |---|---|
    | Entry ID | `troll_hollow_percival` |
    | Spawn group | `troll_hollow_percival` |
    | Loot table | – |
    | Conversation | `perciva_int_phrasel` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:140` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "troll_hollow_percival",
     "name": "Percival",
     "iconID": "monsters_ld1:140",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "perciva_int_phrasel"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_percival.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_percival.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_percival.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_percival.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
