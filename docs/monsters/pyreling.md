---
description: "Pyreling is an enemy in Andor's Trail (construct) with 266 HP, worth 727 XP, found in Mt. Galmore. Drops: Small rock, Glass gem, Red Crystals, Garnet stone."
---

# ![](../assets/icons/monsters/monsters_newb_1_1200.png){ .sprite } Pyreling

**Found in:** Mt. Galmore: [galmore_42](../maps/galmore_42.md), Mt. Galmore: [galmore_52](../maps/galmore_52.md), Mt. Galmore: [galmore_53](../maps/galmore_53.md), Mt. Galmore: [galmore_62](../maps/galmore_62.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1200.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Construct |
| **HP** | 266 |
| **XP when defeated** | 727 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `pyreling` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 266 |
| XP when defeated | 727 |
| Damage | 20 to 28 |
| Attack chance | 150 |
| Block chance | 219 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 9 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 85% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 2 |
| [Red Crystals](../items/crystal_red.md) | 3% | 1 |
| [Garnet stone](../items/garnet_stone.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_32](../maps/galmore_32.md) | – | 4 | – |
| [galmore_41](../maps/galmore_41.md) | – | 8 | – |
| [galmore_42](../maps/galmore_42.md) | Mt. Galmore | 5 | – |
| [galmore_52](../maps/galmore_52.md) | Mt. Galmore | 8 | – |
| [galmore_53](../maps/galmore_53.md) | Mt. Galmore | 1 | – |
| [galmore_62](../maps/galmore_62.md) | Mt. Galmore | 7 | – |
| [galmore_72](../maps/galmore_72.md) | – | 1 | – |
| [undertell_3_lava_00](../maps/undertell_3_lava_00.md) | – | 1 | – |
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 2 | – |
| [undertell_3_lava_11](../maps/undertell_3_lava_11.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `pyreling` |
    | Spawn group | `pyreling` |
    | Loot table | `pyreling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:1200` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "pyreling",
     "name": "Pyreling",
     "iconID": "monsters_newb_1:1200",
     "maxHP": 266,
     "moveCost": 9,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 20,
      "max": 28
     },
     "droplistID": "pyreling_dl",
     "attackCost": 6,
     "attackChance": 150,
     "blockChance": 219,
     "damageResistance": 9
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pyreling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
