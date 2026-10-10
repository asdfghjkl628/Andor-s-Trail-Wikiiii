---
description: "Luthor's skeleton guard is an enemy in Andor's Trail (construct) with 52 HP, worth 63 XP, found in Crackshot hideout 4. Drops: Gold coins, Ruby gem, Regular potion of health, Bone."
---

# ![](../assets/icons/monsters/monsters_skeleton1_0.png){ .sprite } Luthor's skeleton guard

**Where to find Luthor's skeleton guard:** [Crackshot hideout 4](#v-tt_monster1), [Crackshot hideout 4](#v-tt_monster2), [Crackshot hideout 4](#v-tt_monster3)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_skeleton1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crackshot hideout 4 |
| **Class** | Construct |
| **HP** | 52 |
| **XP when defeated** | 63 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

## Crackshot hideout 4 { #v-tt_monster1 }

**Where:** [Crackshot hideout 4](../maps/crackshot_hideout4.md)

### Combat

| | |
|---|---|
| Class | Construct |
| HP | 52 |
| XP when defeated | 63 |
| Damage | 1 to 3 |
| AC | 60 |
| BC | 40 |
| DR | 1 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 16 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crackshot hideout 4](../maps/crackshot_hideout4.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crackshot hideout 4 (2) { #v-tt_monster2 }

**Where:** [Crackshot hideout 4](../maps/crackshot_hideout4.md)

### Combat

| | |
|---|---|
| Class | Construct |
| HP | 52 |
| XP when defeated | 63 |
| Damage | 1 to 3 |
| AC | 60 |
| BC | 40 |
| DR | 1 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 16 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crackshot hideout 4](../maps/crackshot_hideout4.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Crackshot hideout 4 (3) { #v-tt_monster3 }

**Where:** [Crackshot hideout 4](../maps/crackshot_hideout4.md)

### Combat

| | |
|---|---|
| Class | Construct |
| HP | 52 |
| XP when defeated | 63 |
| Damage | 1 to 3 |
| AC | 60 |
| BC | 40 |
| DR | 1 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 16 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crackshot hideout 4](../maps/crackshot_hideout4.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Luthor's skeleton guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: appearance.

| Entry | Type | Section |
|---|---|---|
| `tt_monster1` | Enemy | [Crackshot hideout 4](#v-tt_monster1) |
| `tt_monster2` | Enemy | [Crackshot hideout 4](#v-tt_monster2) |
| `tt_monster3` | Enemy | [Crackshot hideout 4](#v-tt_monster3) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: tt_monster1"

    | | |
    |---|---|
    | Entry ID | `tt_monster1` |
    | Type (wiki) | Enemy |
    | Spawn group | `tt_monster1` |
    | Loot table | `skeleton` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_skeleton1:0` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_monster1",
     "name": "Luthor's skeleton guard",
     "iconID": "monsters_skeleton1:0",
     "maxHP": 52,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 1,
      "max": 3
     },
     "spawnGroup": "tt_monster1",
     "droplistID": "skeleton",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 40,
     "damageResistance": 1
    }
    ```

??? info "Technical information: tt_monster2"

    | | |
    |---|---|
    | Entry ID | `tt_monster2` |
    | Type (wiki) | Enemy |
    | Spawn group | `tt_monster2` |
    | Loot table | `skeleton` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_skeleton2:0` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_monster2",
     "name": "Luthor's skeleton guard",
     "iconID": "monsters_skeleton2:0",
     "maxHP": 52,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 1,
      "max": 3
     },
     "spawnGroup": "tt_monster2",
     "droplistID": "skeleton",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 40,
     "damageResistance": 1
    }
    ```

??? info "Technical information: tt_monster3"

    | | |
    |---|---|
    | Entry ID | `tt_monster3` |
    | Type (wiki) | Enemy |
    | Spawn group | `tt_monster3` |
    | Loot table | `skeleton` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_skeleton1:0` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_monster3",
     "name": "Luthor's skeleton guard",
     "iconID": "monsters_skeleton1:0",
     "maxHP": 52,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 1,
      "max": 3
     },
     "spawnGroup": "tt_monster3",
     "droplistID": "skeleton",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 40,
     "damageResistance": 1
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_monster1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_monster1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_monster1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_monster1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
