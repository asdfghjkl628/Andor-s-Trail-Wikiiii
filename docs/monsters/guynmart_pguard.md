---
description: "Guynmart elite guard is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_1.png){ .sprite } Guynmart elite guard

**Where to find Guynmart elite guard:** [Guynmart Castle, Guynmart and 1 more](#v-guynmart_pguard), [Guynmart Castle, Guynmart wood 4](#v-guynmart_pguard2), [Guynmart Castle, Guynmart wood 4](#v-guynmart_pguard3)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Guynmart Castle, Guynmart and 1 more { #v-guynmart_pguard }

**Where:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_pguard), Guynmart Castle: [Guynmart wood 4](../maps/guynmart_wood_4.md#pin-npc-guynmart_pguard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 4 | Appears later, during a quest |
| [Guynmart wood 4](../maps/guynmart_wood_4.md) | Guynmart Castle | 3 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Guynmart elite guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_guard_10.json" data-npc="Guynmart elite guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_pguard-guynmart_guard_10"></span>**`guynmart_guard_10`** Guynmart elite guard: “Go away, kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart wood 4 { #v-guynmart_pguard2 }

**Where:** Guynmart Castle: [Guynmart wood 4](../maps/guynmart_wood_4.md#pin-npc-guynmart_pguard2)

### Dialogue simulator

Set your quest stages and items, then talk to Guynmart elite guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_pguard2_10.json" data-npc="Guynmart elite guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_pguard2-guynmart_pguard2_10"></span>**`guynmart_pguard2_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 81 of [Roses](../quests/guynmart.md#stage-81))* → [guynmart_pguard2_20](#d-guynmart_pguard2-guynmart_pguard2_20)
    - branch 2 → [guynmart_pguard2_30](#d-guynmart_pguard2-guynmart_pguard2_30)

    <span id="d-guynmart_pguard2-guynmart_pguard2_20"></span>**`guynmart_pguard2_20`** [Guynmart elite guard](../monsters/guynmart_pguard.md#v-guynmart_pguard2): “Halt! Talk to Norgothla before you walk around here!”


    <span id="d-guynmart_pguard2-guynmart_pguard2_30"></span>**`guynmart_pguard2_30`** Guynmart elite guard: “Go away, kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart wood 4 (2) { #v-guynmart_pguard3 }

**Where:** Guynmart Castle: [Guynmart wood 4](../maps/guynmart_wood_4.md#pin-npc-guynmart_pguard3)

### Dialogue simulator

Set your quest stages and items, then talk to Guynmart elite guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_pguard3_10.json" data-npc="Guynmart elite guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_pguard3-guynmart_pguard3_10"></span>**`guynmart_pguard3_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 170 of [Roses](../quests/guynmart.md#stage-170))* → [guynmart_pguard3_20](#d-guynmart_pguard3-guynmart_pguard3_20)
    - branch 2 → [guynmart_pguard2_30](#d-guynmart_pguard2-guynmart_pguard2_30) (listed above)

    <span id="d-guynmart_pguard3-guynmart_pguard3_20"></span>**`guynmart_pguard3_20`** Guynmart elite guard: “Go away, kid. I am depressed.”

    - Next → [guynmart_pguard3_22](#d-guynmart_pguard3-guynmart_pguard3_22)

    <span id="d-guynmart_pguard3-guynmart_pguard3_22"></span>**`guynmart_pguard3_22`** Guynmart elite guard: “They have all gone, and forgotten me here. *Sigh*”

    - “Oh my.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Guynmart elite guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `guynmart_pguard` | NPC | [Guynmart Castle, Guynmart and 1 more](#v-guynmart_pguard) |
| `guynmart_pguard2` | NPC | [Guynmart Castle, Guynmart wood 4](#v-guynmart_pguard2) |
| `guynmart_pguard3` | NPC | [Guynmart Castle, Guynmart wood 4](#v-guynmart_pguard3) |

??? info "Technical information: guynmart_pguard"

    | | |
    |---|---|
    | Entry ID | `guynmart_pguard` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_pguard` |
    | Loot table | – |
    | Conversation | `guynmart_guard_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:1` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_pguard",
     "name": "Guynmart elite guard",
     "iconID": "monsters_ld1:1",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_guard_10"
    }
    ```

??? info "Technical information: guynmart_pguard2"

    | | |
    |---|---|
    | Entry ID | `guynmart_pguard2` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_pguard2` |
    | Loot table | – |
    | Conversation | `guynmart_pguard2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:1` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_pguard2",
     "name": "Guynmart elite guard",
     "iconID": "monsters_ld1:1",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_pguard2_10"
    }
    ```

??? info "Technical information: guynmart_pguard3"

    | | |
    |---|---|
    | Entry ID | `guynmart_pguard3` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_pguard3` |
    | Loot table | – |
    | Conversation | `guynmart_pguard3_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:1` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_pguard3",
     "name": "Guynmart elite guard",
     "iconID": "monsters_ld1:1",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_pguard3_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_pguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_pguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_pguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_pguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
