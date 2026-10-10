---
description: "Lesser wight is an enemy in Andor's Trail (undead) with 130 HP, worth 174 XP, found in Laerothprison 6, Laerothprison 5. Drops: Gold coins, Small rock, Bone."
---

# ![](../assets/icons/monsters/monsters_tometik7_13.png){ .sprite } Lesser wight

**Where to find Lesser wight:** [Laerothprison 6](#v-wight_lesser), [Laerothprison 5](#v-wight_lesser5), [Laerothprison 5](#v-wight_lesser5b)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_13.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Laerothprison 6, Laerothprison 5 |
| **Class** | Undead |
| **HP** | 130 |
| **XP when defeated** | 174 |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Laerothprison 6 { #v-wight_lesser }

**Where:** [Laerothprison 6](../maps/laerothprison6.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| AC | 65 |
| BC | 70 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 0

**When you hit it:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 6](../maps/laerothprison6.md) | – | 3 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Laerothprison 5 { #v-wight_lesser5 }

**Where:** [Laerothprison 5](../maps/laerothprison5.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| AC | 65 |
| BC | 70 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 0

**When you hit it:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 5](../maps/laerothprison5.md) | – | 17 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Laerothprison 5 (2) { #v-wight_lesser5b }

**Where:** [Laerothprison 5](../maps/laerothprison5.md)

### Combat

| | |
|---|---|
| Class | Undead |
| HP | 130 |
| XP when defeated | 174 |
| Damage | 1 to 13 |
| AC | 65 |
| BC | 70 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 0

**When you hit it:** Heal HP: 1; increaseAttackerCurrentHP: -1


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 10 |
| [Small rock](../items/rock.md) | 40% | 1 to 2 |
| [Bone](../items/bone.md) | 30% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Laerothprison 5](../maps/laerothprison5.md) | – | 5 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Lesser wight. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location.

| Entry | Type | Section |
|---|---|---|
| `wight_lesser` | Enemy | [Laerothprison 6](#v-wight_lesser) |
| `wight_lesser5` | Enemy | [Laerothprison 5](#v-wight_lesser5) |
| `wight_lesser5b` | Enemy | [Laerothprison 5](#v-wight_lesser5b) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: wight_lesser"

    | | |
    |---|---|
    | Entry ID | `wight_lesser` |
    | Type (wiki) | Enemy |
    | Spawn group | `wight` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```

??? info "Technical information: wight_lesser5"

    | | |
    |---|---|
    | Entry ID | `wight_lesser5` |
    | Type (wiki) | Enemy |
    | Spawn group | `wight_lesser5` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser5",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight_lesser5",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```

??? info "Technical information: wight_lesser5b"

    | | |
    |---|---|
    | Entry ID | `wight_lesser5b` |
    | Type (wiki) | Enemy |
    | Spawn group | `wight_lesser5b` |
    | Loot table | `wight1` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik7:13` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "wight_lesser5b",
     "name": "Lesser wight",
     "iconID": "monsters_tometik7:13",
     "maxHP": 130,
     "moveCost": 5,
     "monsterClass": "undead",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 1,
      "max": 13
     },
     "spawnGroup": "wight_lesser5b",
     "droplistID": "wight1",
     "attackCost": 4,
     "attackChance": 65,
     "blockChance": 70,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 0
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "increaseAttackerCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wight_lesser.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
