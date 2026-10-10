---
description: "Pixie Cort is an enemy in Andor's Trail (construct) with 160 HP, worth 620 XP, found in Sullengard west ravine, Sullengard woods 1, Sullengard woods 13. Drops: Gold coins, Small tree branch, Small rock."
---

# ![](../assets/icons/monsters/monsters_rltiles1_154.png){ .sprite } Pixie Cort

**Found in:** [Sullengard west ravine](../maps/sullengard_west_ravine.md), [Sullengard woods 1](../maps/sullengard_woods1.md), [Sullengard woods 13](../maps/sullengard_woods13.md), [Sullengard woods 14](../maps/sullengard_woods14.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_154.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard west ravine, Sullengard woods 1, Sullengard woods 13 |
| **Class** | Construct |
| **HP** | 160 |
| **XP when defeated** | 620 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 160 |
| XP when defeated | 620 |
| Damage | 12 to 15 |
| AC | 155 |
| BC | 250 |
| DR | 11 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 15% (×4.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 566.667% | 1 to 10 |
| [Small tree branch](../items/small_tree_branch.md) | 160% | 1 to 2 |
| [Small rock](../items/rock.md) | 185.714% | 2 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Sullengard west ravine](../maps/sullengard_west_ravine.md) | – | 6 | – |
| [Sullengard woods 1](../maps/sullengard_woods1.md) | – | 3 | – |
| [Sullengard woods 13](../maps/sullengard_woods13.md) | – | 5 | – |
| [Sullengard woods 14](../maps/sullengard_woods14.md) | – | 5 | – |
| [Sullengard woods 2](../maps/sullengard_woods2.md) | – | 4 | – |
| [Sullengard woods 3](../maps/sullengard_woods3.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

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
    | Entry ID | `sull_forest_tree_fungus` |
    | Type (wiki) | Enemy |
    | Spawn group | `sull_forest_tree_fungus` |
    | Loot table | `sull_forest_tree_fungus_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles1:154` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sull_forest_tree_fungus",
     "name": "Pixie Cort",
     "iconID": "monsters_rltiles1:154",
     "maxHP": 160,
     "moveCost": 6,
     "monsterClass": "construct",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 15
     },
     "spawnGroup": "sull_forest_tree_fungus",
     "droplistID": "sull_forest_tree_fungus_dl",
     "attackCost": 4,
     "attackChance": 155,
     "criticalSkill": 20,
     "criticalMultiplier": 4.0,
     "blockChance": 250,
     "damageResistance": 11
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_forest_tree_fungus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_forest_tree_fungus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_forest_tree_fungus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_forest_tree_fungus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
