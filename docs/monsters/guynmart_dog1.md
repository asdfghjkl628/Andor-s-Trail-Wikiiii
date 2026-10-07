---
description: "Shepherd's dog is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Shepherd's dog

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Shepherd's dog. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. These entries are identical apart from their IDs. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_dog1`](#v-guynmart_dog1) | NPC | Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_dog1) | – |
| [`guynmart_dog2`](#v-guynmart_dog2) | NPC | Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_dog2) | – |

## Guynmart Castle, Guynmart wood 9 (guynmart_dog1) { #v-guynmart_dog1 }

**Entry ID:** `guynmart_dog1` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_dog1)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Shepherd's dog. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_dog10_10.json" data-npc="Shepherd&#x27;s dog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_dog1-guynmart_dog10_10"></span>**`guynmart_dog10_10`** [Dog](../monsters/petdog.md#v-guynmart_dog10): “Grrrrrr”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_dog1)"

    | | |
    |---|---|
    | Entry ID | `guynmart_dog1` |
    | Spawn group | `guynmart_dog1` |
    | Loot table | – |
    | Conversation | `guynmart_dog10_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_dog1",
     "name": "Shepherd's dog",
     "iconID": "monsters_dogs:4",
     "monsterClass": "animal",
     "phraseID": "guynmart_dog10_10"
    }
    ```


## Guynmart Castle, Guynmart wood 9 (guynmart_dog2) { #v-guynmart_dog2 }

**Entry ID:** `guynmart_dog2` · **Type:** NPC

**Location:** Guynmart Castle: [guynmart_wood_9](../maps/guynmart_wood_9.md#pin-npc-guynmart_dog2)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Shepherd's dog. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_dog10_10.json" data-npc="Shepherd&#x27;s dog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_dog10_10](#d-guynmart_dog1-guynmart_dog10_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_dog2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_dog2` |
    | Spawn group | `guynmart_dog2` |
    | Loot table | – |
    | Conversation | `guynmart_dog10_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_dog2",
     "name": "Shepherd's dog",
     "iconID": "monsters_dogs:4",
     "monsterClass": "animal",
     "phraseID": "guynmart_dog10_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_dog1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_dog1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_dog1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_dog1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
