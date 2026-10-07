---
description: "Spectator is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Spectator

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Spectator. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_spectator2`](#v-guynmart_spectator2) | NPC | Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator2) | – |
| [`guynmart_spectator1a`](#v-guynmart_spectator1a) | NPC | Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator1a) | – |
| [`guynmart_spectator1b`](#v-guynmart_spectator1b) | NPC | Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator1b) | – |

## Guynmart Castle, Guynmart wood 8 (guynmart_spectator2) { #v-guynmart_spectator2 }

**Entry ID:** `guynmart_spectator2` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator2)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Spectator. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_spectator2_10.json" data-npc="Spectator" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_spectator2-guynmart_spectator2_10"></span>**`guynmart_spectator2_10`** Spectator: “Hey, come and join our beetle battle.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_spectator2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_spectator2` |
    | Spawn group | `guynmart_spectator2` |
    | Loot table | – |
    | Conversation | `guynmart_spectator2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_spectator2",
     "name": "Spectator",
     "iconID": "monsters_ld1:20",
     "moveCost": 10,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_spectator2_10"
    }
    ```


## Guynmart Castle, Guynmart wood 8 (guynmart_spectator1a) { #v-guynmart_spectator1a }

**Entry ID:** `guynmart_spectator1a` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator1a)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Spectator. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_spectator1_10.json" data-npc="Spectator" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_spectator1a-guynmart_spectator1_10"></span>**`guynmart_spectator1_10`** Spectator: “The left beetle will win.” — **effects:** faction “beetle_watching” +1

    - Next → [guynmart_spectator1_20](#d-guynmart_spectator1a-guynmart_spectator1_20)

    <span id="d-guynmart_spectator1a-guynmart_spectator1_20"></span>**`guynmart_spectator1_20`** [Spectator](../monsters/guynmart_spectator2.md#v-guynmart_spectator1b): “No, the right beetle will win.” — **effects:** faction “beetle_watching” +1

    - Next → [guynmart_spectator1_30](#d-guynmart_spectator1a-guynmart_spectator1_30)

    <span id="d-guynmart_spectator1a-guynmart_spectator1_30"></span>**`guynmart_spectator1_30`** [Spectator](../monsters/guynmart_spectator2.md#v-guynmart_spectator1a): “Nonsense, the left beetle will win.” — **effects:** faction “beetle_watching” +1

    - Next → [guynmart_spectator1_20](#d-guynmart_spectator1a-guynmart_spectator1_20)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_spectator1a)"

    | | |
    |---|---|
    | Entry ID | `guynmart_spectator1a` |
    | Spawn group | `guynmart_spectator1a` |
    | Loot table | – |
    | Conversation | `guynmart_spectator1_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:9` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_spectator1a",
     "name": "Spectator",
     "iconID": "monsters_ld1:9",
     "moveCost": 10,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_spectator1_10"
    }
    ```


## Guynmart Castle, Guynmart wood 8 (guynmart_spectator1b) { #v-guynmart_spectator1b }

**Entry ID:** `guynmart_spectator1b` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_8](../maps/guynmart_wood_8.md#pin-npc-guynmart_spectator1b)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Spectator. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_spectator1b_10.json" data-npc="Spectator" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_spectator1b-guynmart_spectator1b_10"></span>**`guynmart_spectator1b_10`** Spectator: “The right beetle will win.” — **effects:** faction “beetle_watching” +1

    - Next → [guynmart_spectator1_30](#d-guynmart_spectator1a-guynmart_spectator1_30) (listed above)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_spectator1b)"

    | | |
    |---|---|
    | Entry ID | `guynmart_spectator1b` |
    | Spawn group | `guynmart_spectator1b` |
    | Loot table | – |
    | Conversation | `guynmart_spectator1b_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:18` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_spectator1b",
     "name": "Spectator",
     "iconID": "monsters_ld1:18",
     "moveCost": 10,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_spectator1b_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_spectator2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_spectator2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_spectator2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_spectator2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
