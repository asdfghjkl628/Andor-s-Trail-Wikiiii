---
description: "Irdegh spawn is an enemy in Andor's Trail (reptile) with 57–68 HP, worth 153–166 XP, found in Brightport. Drops: Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_rltiles2_26.png){ .sprite } Irdegh spawn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_26.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport |
| **Class** | Reptile |
| **HP** | 57–68 |
| **XP when defeated** | 153–166 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Irdegh spawn. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: combat statistics. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`irdegh_sp_1`](#v-irdegh_sp_1) | Enemy | Brightport: [Waytobrightport 22](../maps/waytobrightport22.md), Brightport: [Waytobrightport 23](../maps/waytobrightport23.md) (+5 more) | – | 57 |
| [`irdegh_sp_2`](#v-irdegh_sp_2) | Enemy | Brightport: [Waytobrightport 22](../maps/waytobrightport22.md), Brightport: [Waytobrightport 23](../maps/waytobrightport23.md) (+5 more) | – | 68 |

## Brightport, Waytobrightport 22 and 6 more (irdegh_sp_1) { #v-irdegh_sp_1 }

**Entry ID:** `irdegh_sp_1` · **Type:** Enemy

**Location:** Brightport: [Waytobrightport 22](../maps/waytobrightport22.md), Brightport: [Waytobrightport 23](../maps/waytobrightport23.md), [Waterway 11 east](../maps/waterway11_east.md), [Waterway forest 3](../maps/waterway_forest3.md), [Waytomountaincave 0](../maps/waytomountaincave0.md), [Waytomountaincave 1](../maps/waytomountaincave1.md) (+1 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 57 |
| XP when defeated | 153 |
| Damage | 0 to 6 |
| Attack chance | 120 |
| Block chance | 80 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Irdegh poison](../conditions/poison_irdegh.md) (magnitude 2, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 1% | 1 |
| [Poison gland](../items/gland.md) | 1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 11 east](../maps/waterway11_east.md) | – | 7 | – |
| [Waterway forest 3](../maps/waterway_forest3.md) | – | 12 | – |
| [Waytobrightport 22](../maps/waytobrightport22.md) | Brightport | 2 | – |
| [Waytobrightport 23](../maps/waytobrightport23.md) | Brightport | 1 | – |
| [Waytomountaincave 0](../maps/waytomountaincave0.md) | – | 8 | – |
| [Waytomountaincave 1](../maps/waytomountaincave1.md) | – | 8 | – |
| [Waytomountaincave 2](../maps/waytomountaincave2.md) | – | 8 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Irdegh poison](../conditions/poison_irdegh.md) (magnitude 2, 3 rounds, 10% chance) → (magnitude 2, 3 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (irdegh_sp_1)"

    | | |
    |---|---|
    | Entry ID | `irdegh_sp_1` |
    | Spawn group | `irdegh_spawn` |
    | Loot table | `irdegh_spawn` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:26` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "irdegh_sp_1",
     "name": "Irdegh spawn",
     "iconID": "monsters_rltiles2:26",
     "maxHP": 57,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 0,
      "max": 6
     },
     "spawnGroup": "irdegh_spawn",
     "droplistID": "irdegh_spawn",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 80,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_irdegh",
        "magnitude": 2,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


## Brightport, Waytobrightport 22 and 6 more (irdegh_sp_2) { #v-irdegh_sp_2 }

**Entry ID:** `irdegh_sp_2` · **Type:** Enemy

**Location:** Brightport: [Waytobrightport 22](../maps/waytobrightport22.md), Brightport: [Waytobrightport 23](../maps/waytobrightport23.md), [Waterway 11 east](../maps/waterway11_east.md), [Waterway forest 3](../maps/waterway_forest3.md), [Waytomountaincave 0](../maps/waytomountaincave0.md), [Waytomountaincave 1](../maps/waytomountaincave1.md) (+1 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 68 |
| XP when defeated | 166 |
| Damage | 0 to 6 |
| Attack chance | 120 |
| Block chance | 80 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Irdegh poison](../conditions/poison_irdegh.md) (magnitude 2, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 1% | 1 |
| [Poison gland](../items/gland.md) | 1% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 11 east](../maps/waterway11_east.md) | – | 7 | – |
| [Waterway forest 3](../maps/waterway_forest3.md) | – | 12 | – |
| [Waytobrightport 22](../maps/waytobrightport22.md) | Brightport | 2 | – |
| [Waytobrightport 23](../maps/waytobrightport23.md) | Brightport | 1 | – |
| [Waytomountaincave 0](../maps/waytomountaincave0.md) | – | 8 | – |
| [Waytomountaincave 1](../maps/waytomountaincave1.md) | – | 8 | – |
| [Waytomountaincave 2](../maps/waytomountaincave2.md) | – | 8 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Irdegh poison](../conditions/poison_irdegh.md) (magnitude 2, 3 rounds, 10% chance) → (magnitude 2, 3 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (irdegh_sp_2)"

    | | |
    |---|---|
    | Entry ID | `irdegh_sp_2` |
    | Spawn group | `irdegh_spawn` |
    | Loot table | `irdegh_spawn` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:26` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "irdegh_sp_2",
     "name": "Irdegh spawn",
     "iconID": "monsters_rltiles2:26",
     "maxHP": 68,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 0,
      "max": 6
     },
     "spawnGroup": "irdegh_spawn",
     "droplistID": "irdegh_spawn",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 80,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_irdegh",
        "magnitude": 2,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irdegh_sp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irdegh_sp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irdegh_sp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irdegh_sp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
