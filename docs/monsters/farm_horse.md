---
description: "Farm horse is scenery in Andor's Trail: a decoration or dialogue prop, found in Deebo's Orchard."
---

# ![](../assets/icons/monsters/monsters_ld2_67.png){ .sprite } Farm horse

**Where to find Farm horse:** [Deebo's Orchard, Sullengard apple farm east](#v-farm_horse), [Deebo's Orchard, Sullengard apple farm east](#v-farm_horse_right)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_67.png" alt=""></p>

| | |
|---|---|
| **Type** | Scenery (decoration or dialogue prop) |
| **Found in** | Deebo's Orchard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

Part of the scenery: no conversation, no fight ~~and no, you can't take it home~~.

## Deebo's Orchard, Sullengard apple farm east { #v-farm_horse }

**Where:** Deebo's Orchard: [Sullengard apple farm east](../maps/sullengard_apple_farm_east.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Deebo's Orchard, Sullengard apple farm east (2) { #v-farm_horse_right }

**Where:** Deebo's Orchard: [Sullengard apple farm east](../maps/sullengard_apple_farm_east.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Farm horse. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `farm_horse` | Scenery | [Deebo's Orchard, Sullengard apple farm east](#v-farm_horse) |
| `farm_horse_right` | Scenery | [Deebo's Orchard, Sullengard apple farm east](#v-farm_horse_right) |

- `farm_horse` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.
- `farm_horse_right` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.

??? info "Technical information: farm_horse"

    | | |
    |---|---|
    | Entry ID | `farm_horse` |
    | Type (wiki) | Scenery |
    | Spawn group | `farm_horse_left` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld2:67` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "farm_horse",
     "name": "Farm horse",
     "iconID": "monsters_ld2:67",
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "spawnGroup": "farm_horse_left"
    }
    ```

??? info "Technical information: farm_horse_right"

    | | |
    |---|---|
    | Entry ID | `farm_horse_right` |
    | Type (wiki) | Scenery |
    | Spawn group | `farm_horse_right` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:64` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "farm_horse_right",
     "name": "Farm horse",
     "iconID": "monsters_ld2:64",
     "monsterClass": "animal",
     "spawnGroup": "farm_horse_right"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farm_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farm_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farm_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farm_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
