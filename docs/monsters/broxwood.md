---
description: "Broxwood is an enemy in Andor's Trail (construct) with 225 HP, worth 791 XP, found in Sullengard woods 10, Sullengard woods 11, Sullengard woods 12. Drops: Small tree branch, Gold coins, Rotten apple."
---

# ![](../assets/icons/monsters/monsters_newb_1_1083.png){ .sprite } Broxwood

**Found in:** [Sullengard woods 10](../maps/sullengard_woods10.md), [Sullengard woods 11](../maps/sullengard_woods11.md), [Sullengard woods 12](../maps/sullengard_woods12.md), [Sullengard woods 13](../maps/sullengard_woods13.md) (+8 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1083.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard woods 10, Sullengard woods 11, Sullengard woods 12 |
| **Class** | Construct |
| **HP** | 225 |
| **XP when defeated** | 791 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 225 |
| XP when defeated | 791 |
| Damage | 20 to 25 |
| AC | 170 |
| BC | 229 |
| DR | 10 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×3.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small tree branch](../items/small_tree_branch.md) | 65% | 1 |
| [Gold coins](../items/gold.md) | 166.667% | 5 to 7 |
| [Rotten apple](../items/rotten_apple.md) | 300% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Sullengard woods 10](../maps/sullengard_woods10.md) | – | 2 | – |
| [Sullengard woods 11](../maps/sullengard_woods11.md) | – | 3 | – |
| [Sullengard woods 12](../maps/sullengard_woods12.md) | – | 1 | – |
| [Sullengard woods 13](../maps/sullengard_woods13.md) | – | 2 | – |
| [Sullengard woods 14](../maps/sullengard_woods14.md) | – | 2 | – |
| [Sullengard woods 2](../maps/sullengard_woods2.md) | – | 4 | – |
| [Sullengard woods 3](../maps/sullengard_woods3.md) | – | 4 | – |
| [Sullengard woods 4](../maps/sullengard_woods4.md) | – | 4 | – |
| [Sullengard woods 5](../maps/sullengard_woods5.md) | – | 2 | – |
| [Sullengard woods 6](../maps/sullengard_woods6.md) | – | 1 | – |
| [Sullengard woods 7](../maps/sullengard_woods7.md) | – | 1 | – |
| [Sullengard woods 9](../maps/sullengard_woods9.md) | – | 1 | – |


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
    | Entry ID | `broxwood` |
    | Type (wiki) | Enemy |
    | Spawn group | `broxwood` |
    | Loot table | `forest_tree_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:1083` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "broxwood",
     "name": "Broxwood",
     "iconID": "monsters_newb_1:1083",
     "maxHP": 225,
     "moveCost": 7,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 20,
      "max": 25
     },
     "spawnGroup": "broxwood",
     "droplistID": "forest_tree_dl",
     "attackCost": 5,
     "attackChance": 170,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 229,
     "damageResistance": 10
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=broxwood.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=broxwood.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=broxwood.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=broxwood.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
