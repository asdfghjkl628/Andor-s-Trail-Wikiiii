---
description: "Customer is a non-player character (NPC) in Andor's Trail, found in Brimhaven, Stoutford."
---

# ![](../assets/icons/monsters/monsters_ld1_119.png){ .sprite } Customer

**Where to find Customer:** [Brimhaven, Brimhaven tavern 1](#v-brv_tavern1_guest), [Stoutford, Stoutford tavern](#v-stoutford_drinker_1), [Stoutford, Stoutford tavern](#v-stoutford_drinker_2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_119.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven, Stoutford |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Brimhaven, Brimhaven tavern 1 { #v-brv_tavern1_guest }

**Where:** Brimhaven: [Brimhaven tavern 1](../maps/brimhaven_tavern1.md#pin-npc-brv_tavern1_guest)

### Dialogue simulator

Set your quest stages and items, then talk to Customer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_tavern1_guest.json" data-npc="Customer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_tavern1_guest-brv_tavern1_guest"></span>**`brv_tavern1_guest`** Customer: “I'm drinking because I hate myself...”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Stoutford, Stoutford tavern { #v-stoutford_drinker_1 }

**Where:** Stoutford: [Stoutford tavern](../maps/stoutford_tavern.md#pin-npc-stoutford_drinker_1)

### Dialogue simulator

Set your quest stages and items, then talk to Customer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_commoner_0.json" data-npc="Customer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_drinker_1-stoutford_commoner_0"></span>**`stoutford_commoner_0`** Customer: “Welcome to Stoutford kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Stoutford, Stoutford tavern (2) { #v-stoutford_drinker_2 }

**Where:** Stoutford: [Stoutford tavern](../maps/stoutford_tavern.md#pin-npc-stoutford_drinker_2)

### Dialogue simulator

Set your quest stages and items, then talk to Customer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_commoner_0.json" data-npc="Customer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [stoutford_commoner_0](#d-stoutford_drinker_1-stoutford_commoner_0).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Customer. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `brv_tavern1_guest` | NPC | [Brimhaven, Brimhaven tavern 1](#v-brv_tavern1_guest) |
| `stoutford_drinker_1` | NPC | [Stoutford, Stoutford tavern](#v-stoutford_drinker_1) |
| `stoutford_drinker_2` | NPC | [Stoutford, Stoutford tavern](#v-stoutford_drinker_2) |

??? info "Technical information: brv_tavern1_guest"

    | | |
    |---|---|
    | Entry ID | `brv_tavern1_guest` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_tavern1_guest` |
    | Loot table | – |
    | Conversation | `brv_tavern1_guest` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:119` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_tavern1_guest",
     "name": "Customer",
     "iconID": "monsters_ld1:119",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_tavern1_guest",
     "phraseID": "brv_tavern1_guest"
    }
    ```

??? info "Technical information: stoutford_drinker_1"

    | | |
    |---|---|
    | Entry ID | `stoutford_drinker_1` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_drinkers` |
    | Loot table | – |
    | Conversation | `stoutford_commoner_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:35` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_drinker_1",
     "name": "Customer",
     "iconID": "monsters_ld1:35",
     "spawnGroup": "stoutford_drinkers",
     "phraseID": "stoutford_commoner_0"
    }
    ```

??? info "Technical information: stoutford_drinker_2"

    | | |
    |---|---|
    | Entry ID | `stoutford_drinker_2` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_drinkers` |
    | Loot table | – |
    | Conversation | `stoutford_commoner_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:18` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_drinker_2",
     "name": "Customer",
     "iconID": "monsters_ld1:18",
     "spawnGroup": "stoutford_drinkers",
     "phraseID": "stoutford_commoner_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
