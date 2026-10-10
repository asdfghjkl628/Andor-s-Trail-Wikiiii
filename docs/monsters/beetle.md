---
description: "Beetle is an enemy in Andor's Trail (insect) with 4 HP, worth 8 XP, found in Crossglen, Guynmart Castle. Drops: Gold coins, Insect shell."
---

# ![](../assets/icons/monsters/monsters_insects_4.png){ .sprite } Beetle

**Where to find Beetle:** [Crossglen, Crossglen and 3 more](#v-beetle), [Guynmart Castle, Guynmart wood 8](#v-guynmart_fighter1), [Guynmart Castle, Guynmart wood 8](#v-guynmart_fighter2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_insects_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossglen, Guynmart Castle |
| **Class** | Insect |
| **HP** | 4 |
| **XP when defeated** | 8 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Crossglen, Crossglen and 3 more { #v-beetle }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md), Crossglen: [Crossglen farmhouse basement](../maps/crossglen_farmhouse_basement.md), [Guynmart wood 19](../maps/guynmart_wood_19.md), [Hauntedhouse 2](../maps/hauntedhouse2.md)

### Combat

| | |
|---|---|
| Class | Insect |
| HP | 4 |
| XP when defeated | 8 |
| Damage | 3 |
| AC | 70 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 2 to 4 |
| [Insect shell](../items/shell.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen](../maps/crossglen.md) | Crossglen | 1 | – |
| [Crossglen farmhouse basement](../maps/crossglen_farmhouse_basement.md) | Crossglen | 3 | – |
| [Guynmart wood 19](../maps/guynmart_wood_19.md) | – | 3 | – |
| [Hauntedhouse 2](../maps/hauntedhouse2.md) | – | 2 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |
| [v0.8.15](../versions/0.8.15.md) | Chance of appearing mirrored: added (25) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart wood 8 { #v-guynmart_fighter1 }

**Where:** Guynmart Castle: [Guynmart wood 8](../maps/guynmart_wood_8.md)


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart wood 8 (2) { #v-guynmart_fighter2 }

**Where:** Guynmart Castle: [Guynmart wood 8](../maps/guynmart_wood_8.md)


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Beetle. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics, loot or shop stock, appearance.

| Entry | Type | Section |
|---|---|---|
| `beetle` | Enemy | [Crossglen, Crossglen and 3 more](#v-beetle) |
| `guynmart_fighter1` | Scenery | [Guynmart Castle, Guynmart wood 8](#v-guynmart_fighter1) |
| `guynmart_fighter2` | Scenery | [Guynmart Castle, Guynmart wood 8](#v-guynmart_fighter2) |

- `guynmart_fighter1` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.
- `guynmart_fighter2` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: beetle"

    | | |
    |---|---|
    | Entry ID | `beetle` |
    | Type (wiki) | Enemy |
    | Spawn group | `crossglen_beetle` |
    | Loot table | `insect` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:4` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "beetle",
     "name": "Beetle",
     "iconID": "monsters_insects:4",
     "maxHP": 4,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 3,
      "max": 3
     },
     "spawnGroup": "crossglen_beetle",
     "droplistID": "insect",
     "attackCost": 9,
     "attackChance": 70,
     "horizontalFlipChance": 25
    }
    ```

??? info "Technical information: guynmart_fighter1"

    | | |
    |---|---|
    | Entry ID | `guynmart_fighter1` |
    | Type (wiki) | Scenery |
    | Spawn group | `guynmart_fighter1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_fighter1",
     "name": "Beetle",
     "iconID": "monsters_guynmart:0",
     "moveCost": 1,
     "monsterClass": "animal"
    }
    ```

??? info "Technical information: guynmart_fighter2"

    | | |
    |---|---|
    | Entry ID | `guynmart_fighter2` |
    | Type (wiki) | Scenery |
    | Spawn group | `guynmart_fighter2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:1` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_fighter2",
     "name": "Beetle",
     "iconID": "monsters_guynmart:1",
     "moveCost": 1,
     "monsterClass": "animal"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
