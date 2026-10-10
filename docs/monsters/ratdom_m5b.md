---
description: "Poisenous snail is an enemy in Andor's Trail (reptile) with 30 HP, worth 117 XP, found in Pub, Bloskelt + Roskelt, Gold hunter. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_rltiles2_120.png){ .sprite } Poisenous snail

**Found in:** Bloskelt + Roskelt: [Ratdom maze 414](../maps/ratdom_maze_414.md), Gold hunter: [Ratdom maze 423](../maps/ratdom_maze_423.md), Gold hunter: [Ratdom maze 434](../maps/ratdom_maze_434.md), Pub: [Ratdom maze 412](../maps/ratdom_maze_412.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_120.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Pub, Bloskelt + Roskelt, Gold hunter |
| **Class** | Reptile |
| **HP** | 30 |
| **XP when defeated** | 117 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 30 |
| XP when defeated | 117 |
| Damage | 5 |
| AC | 110 |
| BC | 20 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 23% (×2.0) |

**Its hits:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 3 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 412](../maps/ratdom_maze_412.md) | Pub | 4 | – |
| [Ratdom maze 413](../maps/ratdom_maze_413.md) | Pub | 1 | – |
| [Ratdom maze 414](../maps/ratdom_maze_414.md) | Bloskelt + Roskelt | 2 | – |
| [Ratdom maze 421](../maps/ratdom_maze_421.md) | Pub | 2 | – |
| [Ratdom maze 422](../maps/ratdom_maze_422.md) | Pub | 3 | – |
| [Ratdom maze 423](../maps/ratdom_maze_423.md) | Gold hunter | 2 | – |
| [Ratdom maze 432](../maps/ratdom_maze_432.md) | Pub | 2 | – |
| [Ratdom maze 434](../maps/ratdom_maze_434.md) | Gold hunter | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_m5b` |
    | Type (wiki) | Enemy |
    | Spawn group | `ratdom_m5` |
    | Loot table | `snake` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:120` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_m5b",
     "name": "Poisenous snail",
     "iconID": "monsters_rltiles2:120",
     "maxHP": 30,
     "maxAP": 10,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 5,
      "max": 5
     },
     "spawnGroup": "ratdom_m5",
     "droplistID": "snake",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 20,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m5b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m5b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m5b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_m5b.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
