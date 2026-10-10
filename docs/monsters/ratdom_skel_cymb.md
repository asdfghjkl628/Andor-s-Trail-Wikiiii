---
description: "Cymbalist is a non-player character (NPC) in Andor's Trail, found in Skeleton dance, Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_fatboy73_47.png){ .sprite } Cymbalist

**Where to find Cymbalist:** [Skeleton dance, Ratdom maze 543d](#v-ratdom_skel_cymb), [Flagstone Prison, Stoutford castle shed](#v-erwyn_skel_cymbal), [Appears during a quest or event](#v-ratdom_skel_cymb1), [Appears during a quest or event](#v-ratdom_skel_cymb2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_fatboy73_47.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Skeleton dance, Flagstone Prison |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Skeleton dance, Ratdom maze 543d { #v-ratdom_skel_cymb }

**Where:** Skeleton dance: [Ratdom maze 543d](../maps/ratdom_maze_543d.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Stoutford castle shed { #v-erwyn_skel_cymbal }

**Where:** Flagstone Prison: [Stoutford castle shed](../maps/stoutford_castle_shed.md#pin-npc-erwyn_skel_cymbal)

### Dialogue simulator

Talk to Cymbalist as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/erwyn_skel_band.json" data-npc="Cymbalist" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erwyn_skel_cymbal-erwyn_skel_band"></span>**`erwyn_skel_band`** Cymbalist: “Please don't disturb. We have to practice.”




### Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Appears during a quest or event { #v-ratdom_skel_cymb1 }

**Where:** appears during a quest or scripted event.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Appears during a quest or event (2) { #v-ratdom_skel_cymb2 }

**Where:** appears during a quest or scripted event.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**4 entries.** The game data defines 4 separate characters named Cymbalist. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, appearance.

| Entry | Type | Section |
|---|---|---|
| `ratdom_skel_cymb` | Scenery | [Skeleton dance, Ratdom maze 543d](#v-ratdom_skel_cymb) |
| `erwyn_skel_cymbal` | NPC | [Flagstone Prison, Stoutford castle shed](#v-erwyn_skel_cymbal) |
| `ratdom_skel_cymb1` | Scenery | [Appears during a quest or event](#v-ratdom_skel_cymb1) |
| `ratdom_skel_cymb2` | Scenery | [Appears during a quest or event](#v-ratdom_skel_cymb2) |

- `ratdom_skel_cymb` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on Skeleton dance: [Ratdom maze 543d](../maps/ratdom_maze_543d.md).
- `ratdom_skel_cymb1` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.
- `ratdom_skel_cymb2` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.

??? info "Technical information: ratdom_skel_cymb"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_cymb` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_cymb` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:47` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_cymb",
     "name": "Cymbalist",
     "iconID": "monsters_fatboy73:47",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_cymb"
    }
    ```

??? info "Technical information: erwyn_skel_cymbal"

    | | |
    |---|---|
    | Entry ID | `erwyn_skel_cymbal` |
    | Type (wiki) | NPC |
    | Spawn group | `erwyn_skel_cymbal` |
    | Loot table | – |
    | Conversation | `erwyn_skel_band` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:47` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_skel_cymbal",
     "name": "Cymbalist",
     "iconID": "monsters_fatboy73:47",
     "monsterClass": "undead",
     "spawnGroup": "erwyn_skel_cymbal",
     "phraseID": "erwyn_skel_band"
    }
    ```

??? info "Technical information: ratdom_skel_cymb1"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_cymb1` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_cymb1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:47` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_cymb1",
     "name": "Cymbalist",
     "iconID": "monsters_fatboy73:47",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_cymb1"
    }
    ```

??? info "Technical information: ratdom_skel_cymb2"

    | | |
    |---|---|
    | Entry ID | `ratdom_skel_cymb2` |
    | Type (wiki) | Scenery |
    | Spawn group | `ratdom_skel_cymb2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_fatboy73:46` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_skel_cymb2",
     "name": "Cymbalist",
     "iconID": "monsters_fatboy73:46",
     "monsterClass": "undead",
     "spawnGroup": "ratdom_skel_cymb2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_cymb.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_cymb.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_cymb.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skel_cymb.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
