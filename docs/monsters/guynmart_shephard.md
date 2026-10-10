---
description: "Shepherd is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_karvis2_7.png){ .sprite } Shepherd

**Where to find Shepherd:** [Guynmart Castle, Guynmart wood 9](#v-guynmart_shephard), [Guynmart Castle, Guynmart main 1](#v-guynmart_shephard2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_karvis2_7.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Guynmart Castle, Guynmart wood 9 { #v-guynmart_shephard }

**Where:** Guynmart Castle: [Guynmart wood 9](../maps/guynmart_wood_9.md#pin-npc-guynmart_shephard)

### Dialogue simulator

Talk to Shepherd as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_shephard_10.json" data-npc="Shepherd" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_shephard-guynmart_shephard_10"></span>**`guynmart_shephard_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_shephard_20](#d-guynmart_shephard-guynmart_shephard_20)
    - branch 2 *(if killed 20× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_shephard_30](#d-guynmart_shephard-guynmart_shephard_30)
    - branch 3 → [guynmart_shephard_12](#d-guynmart_shephard-guynmart_shephard_12)

    <span id="d-guynmart_shephard-guynmart_shephard_20"></span>**`guynmart_shephard_20`** Shepherd: “Grrumble ... grrrrumble...”

    - “Maybe he does not like his sheep being killed?” → *conversation ends*

    <span id="d-guynmart_shephard-guynmart_shephard_30"></span>**`guynmart_shephard_30`** Shepherd: “GRRRUMMBLE!!!”

    - “Obviously he does not like his sheep being killed.” → *conversation ends*

    <span id="d-guynmart_shephard-guynmart_shephard_12"></span>**`guynmart_shephard_12`** Shepherd: “Grumble ... grumble...”

    - “He seems to speak mostly to his dogs.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart main 1 { #v-guynmart_shephard2 }

**Where:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_shephard2)

### Dialogue simulator

Talk to Shepherd as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_shephard_10.json" data-npc="Shepherd" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_shephard_10](#d-guynmart_shephard-guynmart_shephard_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Shepherd. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location.

| Entry | Type | Section |
|---|---|---|
| `guynmart_shephard` | NPC | [Guynmart Castle, Guynmart wood 9](#v-guynmart_shephard) |
| `guynmart_shephard2` | NPC | [Guynmart Castle, Guynmart main 1](#v-guynmart_shephard2) |

??? info "Technical information: guynmart_shephard"

    | | |
    |---|---|
    | Entry ID | `guynmart_shephard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_shephard` |
    | Loot table | – |
    | Conversation | `guynmart_shephard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:7` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_shephard",
     "name": "Shepherd",
     "iconID": "monsters_karvis2:7",
     "monsterClass": "humanoid",
     "phraseID": "guynmart_shephard_10"
    }
    ```

??? info "Technical information: guynmart_shephard2"

    | | |
    |---|---|
    | Entry ID | `guynmart_shephard2` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_shephard2` |
    | Loot table | – |
    | Conversation | `guynmart_shephard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:7` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_shephard2",
     "name": "Shepherd",
     "iconID": "monsters_karvis2:7",
     "monsterClass": "humanoid",
     "phraseID": "guynmart_shephard_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_shephard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
