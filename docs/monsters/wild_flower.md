---
description: "Wild flower is a non-player character (NPC) in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/items_japozero_547.png){ .sprite } Wild flower

**Where to find Wild flower:** Fallhaven: [Wild 10](../maps/wild10.md#pin-npc-wild_flower), Fallhaven: [Wild 11](../maps/wild11.md#pin-npc-wild_flower)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/items_japozero_547.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Fallhaven |
| **Entry ID** | `wild_flower` |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Wild 10](../maps/wild10.md) | Fallhaven | 3 | Appears later, during a quest |
| [Wild 11](../maps/wild11.md) | Fallhaven | 2 | Appears later, during a quest |

## Dialogue simulator

Set your quest stages and items, then talk to Wild flower. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/chk_wildflower.json" data-npc="Wild flower" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-chk_wildflower"></span>**`chk_wildflower`** *(silent check: the first matching branch below is taken)* — **effects:** gives 1× [Wild Flower](../items/wild_flower.md)

    - branch 1 → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wild_flower` |
    | Spawn group | `wild_flower` |
    | Loot table | – |
    | Conversation | `chk_wildflower` |
    | Faction | – |
    | Movement | – |
    | Icon | `items_japozero:547` |
    | Defined in | `res/raw/monsterlist_lytwings.json` |

    Raw data:

    ```json
    {
     "id": "wild_flower",
     "name": "Wild flower",
     "iconID": "items_japozero:547",
     "moveCost": 999,
     "monsterClass": "animal",
     "spawnGroup": "wild_flower",
     "phraseID": "chk_wildflower"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_flower.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_flower.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_flower.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild_flower.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
