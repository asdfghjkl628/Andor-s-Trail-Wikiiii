---
description: "Poisonous river frog is an enemy in Andor's Trail (reptile) with 21 HP, worth 117 XP, found in Guynmart Castle. Drops: Gold coins, Poison gland."
---

# ![](../assets/icons/monsters/monsters_rltiles1_130.png){ .sprite } Poisonous river frog

**Found in:** Guynmart Castle: [Fields 5](../maps/fields5.md), [Fields 12](../maps/fields12.md), [Waterway 0](../maps/waterway0.md), [Waterway 1](../maps/waterway1.md) (+9 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_130.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Guynmart Castle |
| **Class** | Reptile |
| **HP** | 21 |
| **XP when defeated** | 117 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 21 |
| XP when defeated | 117 |
| Damage | 0 to 5 |
| AC | 165 |
| BC | 55 |
| DR | 0 |
| Attacks per turn | 5 (2 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 2, 5 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 3 |
| [Poison gland](../items/gland.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Fields 12](../maps/fields12.md) | – | 1 | – |
| [Fields 5](../maps/fields5.md) | Guynmart Castle | 2 | – |
| [Waterway 0](../maps/waterway0.md) | – | 3 | – |
| [Waterway 1](../maps/waterway1.md) | – | 2 | – |
| [Waterway 14](../maps/waterway14.md) | – | 3 | – |
| [Waterway 15](../maps/waterway15.md) | – | 4 | – |
| [Waterway 2](../maps/waterway2.md) | – | 4 | – |
| [Waterway 3](../maps/waterway3.md) | – | 4 | – |
| [Waterway 4](../maps/waterway4.md) | – | 8 | – |
| [Waterway 5](../maps/waterway5.md) | – | 4 | – |
| [Waterwaya 1](../maps/waterwaya1.md) | – | 2 | – |
| [Waterwaya 2](../maps/waterwaya2.md) | – | 3 | – |
| [Waterwayextention](../maps/waterwayextention.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Weak Poison](../conditions/poison_weak.md) (magnitude 2, 5 rounds, 30% chance) → (magnitude 2, 5 rounds, 30% chance) |

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
    | Entry ID | `frog_3` |
    | Type (wiki) | Enemy |
    | Spawn group | `frog_3` |
    | Loot table | `frog_3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:130` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "frog_3",
     "name": "Poisonous river frog",
     "iconID": "monsters_rltiles1:130",
     "maxHP": 21,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 0,
      "max": 5
     },
     "spawnGroup": "frog_3",
     "droplistID": "frog_3",
     "attackCost": 2,
     "attackChance": 165,
     "blockChance": 55,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 2,
        "duration": 5,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=frog_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=frog_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=frog_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=frog_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
