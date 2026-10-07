---
description: "Embergeist is an enemy in Andor's Trail (construct) with 266 HP, worth 787 XP, found in Mt. Galmore. Drops: Small rock, Sharpened gem, Red Crystals, Garnet stone."
---

# ![](../assets/icons/monsters/monsters_newb_1_658.png){ .sprite } Embergeist

**Found in:** Mt. Galmore: [galmore_52](../maps/galmore_52.md), Mt. Galmore: [galmore_62](../maps/galmore_62.md), [galmore_71](../maps/galmore_71.md), [galmore_72](../maps/galmore_72.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_658.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Construct |
| **HP** | 266 |
| **XP when defeated** | 787 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `embergeist` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 266 |
| XP when defeated | 787 |
| Damage | 21 to 22 |
| Attack chance | 150 |
| Block chance | 219 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On target: Ablaze (magnitude 2, 5 rounds, 90% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 50% | 1 to 2 |
| [Sharpened gem](../items/gem4.md) | 100% | 1 to 2 |
| [Red Crystals](../items/crystal_red.md) | 10% | 1 |
| [Garnet stone](../items/garnet_stone.md) | 8% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_52](../maps/galmore_52.md) | Mt. Galmore | 1 | – |
| [galmore_62](../maps/galmore_62.md) | Mt. Galmore | 14 | – |
| [galmore_71](../maps/galmore_71.md) | – | 1 | – |
| [galmore_72](../maps/galmore_72.md) | – | 8 | – |
| [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | 1 | – |
| [undertell_3_lava_10](../maps/undertell_3_lava_10.md) | – | 1 | – |
| [undertell_4_00](../maps/undertell_4_00.md) | – | 3 | – |
| [undertell_4_01](../maps/undertell_4_01.md) | – | 8 | – |
| [undertell_4_10](../maps/undertell_4_10.md) | – | 5 | – |
| [undertell_4_11](../maps/undertell_4_11.md) | – | 4 | – |
| [undertell_7_00](../maps/undertell_7_00.md) | – | 2 | – |
| [undertell_7_01](../maps/undertell_7_01.md) | – | 3 | – |
| [undertell_7_10](../maps/undertell_7_10.md) | – | 8 | – |
| [undertell_7_11](../maps/undertell_7_11.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `embergeist` |
    | Spawn group | `embergeist` |
    | Loot table | `embergeist_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:658` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "embergeist",
     "name": "Embergeist",
     "iconID": "monsters_newb_1:658",
     "maxHP": 266,
     "moveCost": 4,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 21,
      "max": 22
     },
     "droplistID": "embergeist_dl",
     "attackCost": 5,
     "attackChance": 150,
     "blockChance": 219,
     "damageResistance": 9,
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 2,
        "duration": 5,
        "chance": "90"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=embergeist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=embergeist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=embergeist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=embergeist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
