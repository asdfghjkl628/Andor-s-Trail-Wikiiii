---
description: "Huckleberreaper is an enemy in Andor's Trail (construct) with 265 HP, worth 962 XP, found in Sullengard west ravine, Sullengard woods 1, Sullengard woods 13. Drops: Small tree branch, Gold coins, Rotten apple."
---

# ![](../assets/icons/monsters/monsters_newb_1_1081.png){ .sprite } Huckleberreaper

**Found in:** [Sullengard west ravine](../maps/sullengard_west_ravine.md), [Sullengard woods 1](../maps/sullengard_woods1.md), [Sullengard woods 13](../maps/sullengard_woods13.md), [Sullengard woods 14](../maps/sullengard_woods14.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1081.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard west ravine, Sullengard woods 1, Sullengard woods 13 |
| **Class** | Construct |
| **HP** | 265 |
| **XP when defeated** | 962 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `huckleber_reaper` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 265 |
| XP when defeated | 962 |
| Damage | 30 |
| Attack chance | 190 |
| Block chance | 240 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 7 AP |
| Critical skill | 10 |
| Critical multiplier | 1.2 |
| Critical hit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small tree branch](../items/small_tree_branch.md) | 65% | 1 |
| [Gold coins](../items/gold.md) | 166.667% | 5 to 7 |
| [Rotten apple](../items/rotten_apple.md) | 300% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Sullengard west ravine](../maps/sullengard_west_ravine.md) | – | 3 | – |
| [Sullengard woods 1](../maps/sullengard_woods1.md) | – | 3 | – |
| [Sullengard woods 13](../maps/sullengard_woods13.md) | – | 1 | – |
| [Sullengard woods 14](../maps/sullengard_woods14.md) | – | 7 | – |
| [Sullengard woods gj 1](../maps/sullengard_woods_gj1.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `huckleber_reaper` |
    | Spawn group | `huckleber_reaper` |
    | Loot table | `forest_tree_dl` |
    | Conversation | – |
    | Faction | `huckleber_reaper` |
    | Movement | – |
    | Icon | `monsters_newb_1:1081` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "huckleber_reaper",
     "name": "Huckleberreaper",
     "iconID": "monsters_newb_1:1081",
     "maxHP": 265,
     "moveCost": 7,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 30,
      "max": 30
     },
     "spawnGroup": "huckleber_reaper",
     "faction": "huckleber_reaper",
     "droplistID": "forest_tree_dl",
     "attackCost": 5,
     "attackChance": 190,
     "criticalSkill": 10,
     "criticalMultiplier": 1.2,
     "blockChance": 240,
     "damageResistance": 10
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=huckleber_reaper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=huckleber_reaper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=huckleber_reaper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=huckleber_reaper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
