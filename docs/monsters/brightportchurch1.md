---
description: "Praying woman is a non-player character (NPC) in Andor's Trail, found in Brightport, Stoutford."
---

# ![](../assets/icons/monsters/monsters_men_6.png){ .sprite } Praying woman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport, Stoutford |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Praying woman. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`brightportchurch1`](#v-brightportchurch1) | NPC | Brightport: [brightport_temple](../maps/brightport_temple.md#pin-npc-brightportchurch1) | – |
| [`stoutford_worshiper`](#v-stoutford_worshiper) | NPC | Stoutford: [stoutford_church](../maps/stoutford_church.md#pin-npc-stoutford_worshiper) | – |

## Brightport, Brightport temple (brightportchurch1) { #v-brightportchurch1 }

**Entry ID:** `brightportchurch1` · **Type:** NPC

**Location:** Brightport: [brightport_temple](../maps/brightport_temple.md#pin-npc-brightportchurch1)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Praying woman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_church1.json" data-npc="Praying woman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightportchurch1-brightport_church1"></span>**`brightport_church1`** [Praying woman](../monsters/brightportchurch1.md): “Shadow embrace me!”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportchurch1)"

    | | |
    |---|---|
    | Entry ID | `brightportchurch1` |
    | Spawn group | `brightportchurch1` |
    | Loot table | – |
    | Conversation | `brightport_church1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:6` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportchurch1",
     "name": "Praying woman",
     "iconID": "monsters_men:6",
     "phraseID": "brightport_church1"
    }
    ```


## Stoutford, Stoutford church (stoutford_worshiper) { #v-stoutford_worshiper }

**Entry ID:** `stoutford_worshiper` · **Type:** NPC

**Location:** Stoutford: [stoutford_church](../maps/stoutford_church.md#pin-npc-stoutford_worshiper)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Praying woman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/chapelgoer.json" data-npc="Praying woman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_worshiper-chapelgoer"></span>**`chapelgoer`** Praying woman: “Shadow, embrace me.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stoutford_worshiper)"

    | | |
    |---|---|
    | Entry ID | `stoutford_worshiper` |
    | Spawn group | `stoutford_worshiper` |
    | Loot table | – |
    | Conversation | `chapelgoer` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:6` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_worshiper",
     "name": "Praying woman",
     "iconID": "monsters_men:6",
     "phraseID": "chapelgoer"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportchurch1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportchurch1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportchurch1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportchurch1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
