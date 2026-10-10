---
description: "Terrified teenager is a non-player character (NPC) in Andor's Trail, found in Undertell 3 12."
---

# ![](../assets/icons/monsters/monsters_gisons_14.png){ .sprite } Terrified teenager

**Where to find Terrified teenager:** [Undertell 3 12](#v-about_a_girl1), [Undertell 3 12](#v-about_a_girl_flee), [Undertell 3 12](#v-about_a_girl_hidden)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_gisons_14.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Undertell 3 12 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Undertell 3 12 { #v-about_a_girl1 }

**Where:** [Undertell 3 12](../maps/undertell_3_12.md#pin-npc-about_a_girl1)

### Quests

- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 90

### Dialogue simulator

Talk to Terrified teenager as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/about_girl_scream_10.json" data-npc="Terrified teenager" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-about_a_girl1-about_girl_scream_10"></span>**`about_girl_scream_10`** [Terrified teenager](../monsters/about_a_girl1.md#v-about_a_girl_hidden): “HELP! SOMEBODY HELP ME!”

    - “What is wrong?” → [about_girl_scream_20](#d-about_a_girl1-about_girl_scream_20)

    <span id="d-about_a_girl1-about_girl_scream_20"></span>**`about_girl_scream_20`** Terrified teenager: “STAY AWAY FROM ME!” — **effects:** removes monsters from undertell_3_12, spawns monsters on undertell_3_12, sets stage 90 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-90)




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 12 (2) { #v-about_a_girl_flee }

**Where:** [Undertell 3 12](../maps/undertell_3_12.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Undertell 3 12 (3) { #v-about_a_girl_hidden }

**Where:** [Undertell 3 12](../maps/undertell_3_12.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Terrified teenager. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, movement.

| Entry | Type | Section |
|---|---|---|
| `about_a_girl1` | NPC | [Undertell 3 12](#v-about_a_girl1) |
| `about_a_girl_flee` | Scenery | [Undertell 3 12](#v-about_a_girl_flee) |
| `about_a_girl_hidden` | Scenery | [Undertell 3 12](#v-about_a_girl_hidden) |

- `about_a_girl_flee` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on [Undertell 3 12](../maps/undertell_3_12.md).
- `about_a_girl_hidden` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on [Undertell 3 12](../maps/undertell_3_12.md).

??? info "Technical information: about_a_girl1"

    | | |
    |---|---|
    | Entry ID | `about_a_girl1` |
    | Type (wiki) | NPC |
    | Spawn group | `about_a_girl1` |
    | Loot table | – |
    | Conversation | `about_girl_scream_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl1",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 50,
     "phraseID": "about_girl_scream_10"
    }
    ```

??? info "Technical information: about_a_girl_flee"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_flee` |
    | Type (wiki) | Scenery |
    | Spawn group | `about_a_girl_flee` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | flee |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_flee",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "movementAggressionType": "flee",
     "horizontalFlipChance": 50
    }
    ```

??? info "Technical information: about_a_girl_hidden"

    | | |
    |---|---|
    | Entry ID | `about_a_girl_hidden` |
    | Type (wiki) | Scenery |
    | Spawn group | `about_a_girl_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:14` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "about_a_girl_hidden",
     "name": "Terrified teenager",
     "iconID": "monsters_gisons:14",
     "monsterClass": "ghost",
     "horizontalFlipChance": 0
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=about_a_girl1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
