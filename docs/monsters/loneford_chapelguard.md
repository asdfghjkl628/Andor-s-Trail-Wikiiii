---
description: "Chapel guard is a non-player character (NPC) in Andor's Trail, found in Loneford, Sullengard."
---

# ![](../assets/icons/monsters/monsters_rltiles1_78.png){ .sprite } Chapel guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_78.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Loneford, Sullengard |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Chapel guard. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`loneford_chapelguard`](#v-loneford_chapelguard) | NPC | Loneford: [loneford4](../maps/loneford4.md#pin-npc-loneford_chapelguard) | – |
| [`sullengard_church_guard`](#v-sullengard_church_guard) | NPC | Sullengard: [sullengard_church](../maps/sullengard_church.md#pin-npc-sullengard_church_guard) | – |

## Loneford, Loneford4 (loneford_chapelguard) { #v-loneford_chapelguard }

**Entry ID:** `loneford_chapelguard` · **Type:** NPC

**Location:** Loneford: [loneford4](../maps/loneford4.md#pin-npc-loneford_chapelguard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Chapel guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_chapelguard.json" data-npc="Chapel guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-loneford_chapelguard-loneford_chapelguard"></span>**`loneford_chapelguard`** Chapel guard: “Walk with the Shadow, child.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (loneford_chapelguard)"

    | | |
    |---|---|
    | Entry ID | `loneford_chapelguard` |
    | Spawn group | `loneford_chapelguard` |
    | Loot table | – |
    | Conversation | `loneford_chapelguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:78` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "loneford_chapelguard",
     "name": "Chapel guard",
     "iconID": "monsters_rltiles1:78",
     "monsterClass": "humanoid",
     "spawnGroup": "loneford_chapelguard",
     "phraseID": "loneford_chapelguard"
    }
    ```


## Sullengard, Sullengard church (sullengard_church_guard) { #v-sullengard_church_guard }

**Entry ID:** `sullengard_church_guard` · **Type:** NPC

**Location:** Sullengard: [sullengard_church](../maps/sullengard_church.md#pin-npc-sullengard_church_guard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Chapel guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_church_guard.json" data-npc="Chapel guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_church_guard-sullengard_church_guard"></span>**`sullengard_church_guard`** Chapel guard: “Walk with the Shadow, child”

    - “Yes, I am walking with the Shadow and I'm loving it.” → *conversation ends*
    - “The Shadow? What's it ever done for me?” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (sullengard_church_guard)"

    | | |
    |---|---|
    | Entry ID | `sullengard_church_guard` |
    | Spawn group | `sullengard_church_guard` |
    | Loot table | – |
    | Conversation | `sullengard_church_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:39` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_church_guard",
     "name": "Chapel guard",
     "iconID": "monsters_tometik6:39",
     "phraseID": "sullengard_church_guard"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_chapelguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_chapelguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_chapelguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=loneford_chapelguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
