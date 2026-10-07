---
description: "Pixie Cort is an enemy in Andor's Trail (construct) with 160 HP, worth 620 XP, found in sullengard_west_ravine, sullengard_woods1, sullengard_woods13. Drops: Gold coins, Small tree branch, Small rock."
---

# ![](../assets/icons/monsters/monsters_rltiles1_154.png){ .sprite } Pixie Cort

**Found in:** [sullengard_west_ravine](../maps/sullengard_west_ravine.md), [sullengard_woods1](../maps/sullengard_woods1.md), [sullengard_woods13](../maps/sullengard_woods13.md), [sullengard_woods14](../maps/sullengard_woods14.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_154.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | sullengard_west_ravine, sullengard_woods1, sullengard_woods13 |
| **Class** | Construct |
| **HP** | 160 |
| **XP when defeated** | 620 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `sull_forest_tree_fungus` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 160 |
| XP when defeated | 620 |
| Damage | 12 to 15 |
| Attack chance | 155 |
| Block chance | 250 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 6 AP |
| Critical skill | 20 |
| Critical multiplier | 4.0 |
| Critical hit chance | 15% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 566.667% | 1 to 10 |
| [Small tree branch](../items/small_tree_branch.md) | 160% | 1 to 2 |
| [Small rock](../items/rock.md) | 185.714% | 2 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [sullengard_west_ravine](../maps/sullengard_west_ravine.md) | – | 6 | – |
| [sullengard_woods1](../maps/sullengard_woods1.md) | – | 3 | – |
| [sullengard_woods13](../maps/sullengard_woods13.md) | – | 5 | – |
| [sullengard_woods14](../maps/sullengard_woods14.md) | – | 5 | – |
| [sullengard_woods2](../maps/sullengard_woods2.md) | – | 4 | – |
| [sullengard_woods3](../maps/sullengard_woods3.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sull_forest_tree_fungus` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
