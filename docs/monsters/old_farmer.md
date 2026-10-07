---
description: "Old farmer is a non-player character (NPC) in Andor's Trail, found in Remgard, Stoutford."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Old farmer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Remgard, Stoutford |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Old farmer. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`old_farmer`](#v-old_farmer) | NPC | Remgard: [remgard4](../maps/remgard4.md#pin-npc-old_farmer) | – |
| [`stoutford_farmer3`](#v-stoutford_farmer3) | NPC | Stoutford: [stoutford_se](../maps/stoutford_se.md#pin-npc-stoutford_farmer3) | – |

## Remgard, Remgard4 (old_farmer) { #v-old_farmer }

**Entry ID:** `old_farmer` · **Type:** NPC

**Location:** Remgard: [remgard4](../maps/remgard4.md#pin-npc-old_farmer)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Old farmer. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_farmer2.json" data-npc="Old farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-old_farmer-fallhaven_farmer2"></span>**`fallhaven_farmer2`** Old farmer: “Hello. Could you please move out of the way? I am trying to work here.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | name: Old Farmer → Old farmer |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (old_farmer)"

    | | |
    |---|---|
    | Entry ID | `old_farmer` |
    | Spawn group | `fallhaven_farmer2` |
    | Loot table | – |
    | Conversation | `fallhaven_farmer2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "old_farmer",
     "name": "Old farmer",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_farmer2",
     "phraseID": "fallhaven_farmer2"
    }
    ```


## Stoutford, Stoutford south-east (stoutford_farmer3) { #v-stoutford_farmer3 }

**Entry ID:** `stoutford_farmer3` · **Type:** NPC

**Location:** Stoutford: [stoutford_se](../maps/stoutford_se.md#pin-npc-stoutford_farmer3)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Old farmer. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_farmer3.json" data-npc="Old farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_farmer3-stoutford_farmer3"></span>**`stoutford_farmer3`** Old farmer: “Hello. Could you please move out of the way? I am trying to work here.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stoutford_farmer3)"

    | | |
    |---|---|
    | Entry ID | `stoutford_farmer3` |
    | Spawn group | `stoutford_farmer3` |
    | Loot table | – |
    | Conversation | `stoutford_farmer3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_farmer3",
     "name": "Old farmer",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_farmer3",
     "phraseID": "stoutford_farmer3"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=old_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
