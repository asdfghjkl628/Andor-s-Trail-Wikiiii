---
description: "Scylla is an enemy in Andor's Trail (animal) with 180 HP, worth 1442 XP, found in Mountainlake 32."
---

# ![](../assets/icons/monsters/monsters_ld2_18.png){ .sprite } Scylla

**Where to find Scylla:** [Mountainlake 32](#v-scylla_1), [Mountainlake 32](#v-scylla_2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_18.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mountainlake 32 |
| **Class** | Animal |
| **HP** | 180 |
| **XP when defeated** | 1,442 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Mountainlake 32 { #v-scylla_1 }

**Where:** [Mountainlake 32](../maps/mountainlake32.md)

### Combat

| | |
|---|---|
| Class | Animal |
| HP | 180 |
| XP when defeated | 1,442 |
| Damage | 1 |
| AC | 250 |
| BC | 500 |
| DR | 100 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 180; On target: [Scylla's bite](../conditions/scylla.md) (magnitude 1, 1 round)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mountainlake 32](../maps/mountainlake32.md) | – | 6 | – |

### Quests that count defeats

- A conversation with stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Mountainlake 32 (2) { #v-scylla_2 }

**Where:** [Mountainlake 32](../maps/mountainlake32.md)

### Combat

| | |
|---|---|
| Class | Animal |
| HP | 180 |
| XP when defeated | 1,442 |
| Damage | 1 |
| AC | 250 |
| BC | 500 |
| DR | 100 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 180; On target: [Scylla's bite](../conditions/scylla.md) (magnitude 1, 1 round)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mountainlake 32](../maps/mountainlake32.md) | – | 6 | – |

### Quests that count defeats

- A conversation with stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Scylla. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: appearance.

| Entry | Type | Section |
|---|---|---|
| `scylla_1` | Enemy | [Mountainlake 32](#v-scylla_1) |
| `scylla_2` | Enemy | [Mountainlake 32](#v-scylla_2) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: scylla_1"

    | | |
    |---|---|
    | Entry ID | `scylla_1` |
    | Type (wiki) | Enemy |
    | Spawn group | `scylla` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:18` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "scylla_1",
     "name": "Scylla",
     "iconID": "monsters_ld2:18",
     "maxHP": 180,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "scylla",
     "attackCost": 10,
     "attackChance": 250,
     "blockChance": 500,
     "damageResistance": 100,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 180,
       "max": 180
      },
      "conditionsTarget": [
       {
        "condition": "scylla",
        "magnitude": 1,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```

??? info "Technical information: scylla_2"

    | | |
    |---|---|
    | Entry ID | `scylla_2` |
    | Type (wiki) | Enemy |
    | Spawn group | `scylla` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:19` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "scylla_2",
     "name": "Scylla",
     "iconID": "monsters_ld2:19",
     "maxHP": 180,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 1
     },
     "spawnGroup": "scylla",
     "attackCost": 10,
     "attackChance": 250,
     "blockChance": 500,
     "damageResistance": 100,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 180,
       "max": 180
      },
      "conditionsTarget": [
       {
        "condition": "scylla",
        "magnitude": 1,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scylla_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
