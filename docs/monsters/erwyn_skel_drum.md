---
description: "Drummer is a non-player character (NPC) in Andor's Trail, found in Flagstone Prison, Skeleton dance."
---

# ![](../assets/icons/monsters/monsters_fatboy73_45.png){ .sprite } Drummer

**Where to find Drummer:** [Flagstone Prison, Stoutford castle shed](#v-erwyn_skel_drum), [Skeleton dance, Ratdom maze 543d](#v-ratdom_skel_drum), [Appears during a quest or event](#v-ratdom_skel_drum1), [Appears during a quest or event](#v-ratdom_skel_drum2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_fatboy73_45.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Flagstone Prison, Skeleton dance |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Flagstone Prison, Stoutford castle shed { #v-erwyn_skel_drum }

**Where:** Flagstone Prison: [Stoutford castle shed](../maps/stoutford_castle_shed.md#pin-npc-erwyn_skel_drum)

### Dialogue simulator

Talk to Drummer as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/erwyn_skel_band.json" data-npc="Drummer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erwyn_skel_drum-erwyn_skel_band"></span>**`erwyn_skel_band`** Drummer: “Please don't disturb. We have to practice.”




### Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Skeleton dance, Ratdom maze 543d { #v-ratdom_skel_drum }

**Where:** Skeleton dance: [Ratdom maze 543d](../maps/ratdom_maze_543d.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Appears during a quest or event { #v-ratdom_skel_drum1 }

**Where:** appears during a quest or scripted event.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Appears during a quest or event (2) { #v-ratdom_skel_drum2 }

**Where:** appears during a quest or scripted event.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**4 entries.** The game data defines 4 separate characters named Drummer. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `erwyn_skel_drum` | NPC | [Flagstone Prison, Stoutford castle shed](#v-erwyn_skel_drum) |
| `ratdom_skel_drum` | Scenery | [Skeleton dance, Ratdom maze 543d](#v-ratdom_skel_drum) |
| `ratdom_skel_drum1` | Scenery | [Appears during a quest or event](#v-ratdom_skel_drum1) |
| `ratdom_skel_drum2` | Scenery | [Appears during a quest or event](#v-ratdom_skel_drum2) |

- `ratdom_skel_drum` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on Skeleton dance: [Ratdom maze 543d](../maps/ratdom_maze_543d.md).
- `ratdom_skel_drum1` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.
- `ratdom_skel_drum2` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.

??? info "Technical information: erwyn_skel_drum"

    | | |
    |---|---|
    | Entry ID | `erwyn_skel_drum` |
    | Type (wiki) | NPC |
    | Spawn group | `erwyn_skel_drum` |
    | Loot table | – |
    | Conversation | `erwyn_skel_band` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:45` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_skel_drum",
     "name": "Drummer",
     "iconID": "monsters_fatboy73:45",
     "monsterClass": "undead",
     "spawnGroup": "erwyn_skel_drum",
     "phraseID": "erwyn_skel_band"
    }
    ```

??? info "Technical information: ratdom_skel_drum"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_drum` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_drum` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:45` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_drum",
     "name": "Drummer",
     "iconID": "monsters_fatboy73:45",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_drum"
    }
    ```

??? info "Technical information: ratdom_skel_drum1"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_drum1` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_drum1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:45` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_drum1",
     "name": "Drummer",
     "iconID": "monsters_fatboy73:45",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_drum1"
    }
    ```

??? info "Technical information: ratdom_skel_drum2"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_drum2` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_drum2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:44` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_drum2",
     "name": "Drummer",
     "iconID": "monsters_fatboy73:44",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_drum2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_skel_drum.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_skel_drum.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_skel_drum.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_skel_drum.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
