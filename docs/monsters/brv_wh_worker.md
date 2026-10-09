---
description: "Warehouse worker is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_15.png){ .sprite } Warehouse worker

**Where to find Warehouse worker:** [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker), [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker2), [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker3)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_15.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Brimhaven, Brimhaven warehouse { #v-brv_wh_worker }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_worker)

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse worker. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_worker.json" data-npc="Warehouse worker" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_worker-brv_wh_worker"></span>**`brv_wh_worker`** Warehouse worker: “Do you have some work for me to do?”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (2) { #v-brv_wh_worker2 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_worker2)

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse worker. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_worker.json" data-npc="Warehouse worker" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_wh_worker](#d-brv_wh_worker-brv_wh_worker).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (3) { #v-brv_wh_worker3 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_worker3)

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse worker. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_worker.json" data-npc="Warehouse worker" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_wh_worker](#d-brv_wh_worker-brv_wh_worker).


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Warehouse worker. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: appearance.

| Entry | Type | Section |
|---|---|---|
| `brv_wh_worker` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker) |
| `brv_wh_worker2` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker2) |
| `brv_wh_worker3` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_worker3) |

??? info "Technical information: brv_wh_worker"

    | | |
    |---|---|
    | Entry ID | `brv_wh_worker` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_worker` |
    | Loot table | – |
    | Conversation | `brv_wh_worker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:15` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_worker",
     "name": "Warehouse worker",
     "iconID": "monsters_ld1:15",
     "moveCost": 6,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_worker",
     "phraseID": "brv_wh_worker"
    }
    ```

??? info "Technical information: brv_wh_worker2"

    | | |
    |---|---|
    | Entry ID | `brv_wh_worker2` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_worker2` |
    | Loot table | – |
    | Conversation | `brv_wh_worker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:19` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_worker2",
     "name": "Warehouse worker",
     "iconID": "monsters_ld1:19",
     "moveCost": 3,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_worker2",
     "phraseID": "brv_wh_worker"
    }
    ```

??? info "Technical information: brv_wh_worker3"

    | | |
    |---|---|
    | Entry ID | `brv_wh_worker3` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_worker3` |
    | Loot table | – |
    | Conversation | `brv_wh_worker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:100` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_worker3",
     "name": "Warehouse worker",
     "iconID": "monsters_ld1:100",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_worker3",
     "phraseID": "brv_wh_worker"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_worker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_worker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_worker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_worker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
