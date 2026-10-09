---
description: "Watchdog is a non-player character (NPC) in Andor's Trail, found in Brightport, Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_94.png){ .sprite } Watchdog

**Where to find Watchdog:** [Brightport, Brightport jail and 1 more](#v-brightportthieves4), [Brimhaven, Brimhaven brother 1](#v-brv_brother1_watchdog)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport, Brimhaven |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Brightport, Brightport jail and 1 more { #v-brightportthieves4 }

**Where:** Brightport: [Brightport jail](../maps/brightport_jail.md#pin-npc-brightportthieves4), Brightport: [Brightport thieves](../maps/brightport_thieves.md#pin-npc-brightportthieves4)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport jail](../maps/brightport_jail.md) | Brightport | 1 | – |
| [Brightport thieves](../maps/brightport_thieves.md) | Brightport | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Watchdog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brighport_watchdog.json" data-npc="Watchdog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportthieves4-brighport_watchdog"></span>**`brighport_watchdog`** [Watchdog](../monsters/brightportthieves4.md): “Sigh. It's almost time for my shift again, but I can't complain. The Guild pays good money.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven brother 1 { #v-brv_brother1_watchdog }

**Where:** Brimhaven: [Brimhaven brother 1](../maps/brimhaven_brother1.md#pin-npc-brv_brother1_watchdog)

### Dialogue simulator

Set your quest stages and items, then talk to Watchdog. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_brother1_watchdog.json" data-npc="Watchdog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_brother1_watchdog-brv_brother1_watchdog"></span>**`brv_brother1_watchdog`** Watchdog: “Grrr.... Woof.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Watchdog. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `brightportthieves4` | NPC | [Brightport, Brightport jail and 1 more](#v-brightportthieves4) |
| `brv_brother1_watchdog` | NPC | [Brimhaven, Brimhaven brother 1](#v-brv_brother1_watchdog) |

??? info "Technical information: brightportthieves4"

    | | |
    |---|---|
    | Entry ID | `brightportthieves4` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportthieves4` |
    | Loot table | – |
    | Conversation | `brighport_watchdog` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportthieves4",
     "name": "Watchdog",
     "iconID": "monsters_ld1:94",
     "phraseID": "brighport_watchdog"
    }
    ```

??? info "Technical information: brv_brother1_watchdog"

    | | |
    |---|---|
    | Entry ID | `brv_brother1_watchdog` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_brother1_watchdog` |
    | Loot table | – |
    | Conversation | `brv_brother1_watchdog` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:108` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_brother1_watchdog",
     "name": "Watchdog",
     "iconID": "monsters_rltiles2:108",
     "phraseID": "brv_brother1_watchdog"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportthieves4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
