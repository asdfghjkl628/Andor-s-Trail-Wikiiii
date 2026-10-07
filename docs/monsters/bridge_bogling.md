---
description: "Bridge bogling is an enemy in Andor's Trail (humanoid) with 222 HP, worth 595 XP, found in Mt. Galmore. Drops: Bridgebreaker, Small tree branch, Gold coins, Duskbloom."
---

# ![](../assets/icons/monsters/monsters_misc_7.png){ .sprite } Bridge bogling

**Found in:** Mt. Galmore: [galmore_36](../maps/galmore_36.md), Mt. Galmore: [galmore_48](../maps/galmore_48.md), [galmore_15](../maps/galmore_15.md), [galmore_19](../maps/galmore_19.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_misc_7.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 222 |
| **XP when defeated** | 595 |
| **Entry ID** | `bridge_bogling` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 222 |
| XP when defeated | 595 |
| Damage | 5 to 25 |
| Attack chance | 165 |
| Block chance | 150 |
| Damage resistance | 8 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**When hit:** Heal HP: 6 to 12; Restore AP: 1 to 2; On target: Unsteady footing (magnitude 1, 5 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bridgebreaker](../items/bridgebreaker.md) | 0.01% | 1 |
| [Small tree branch](../items/small_tree_branch.md) | 25% | 1 |
| [Gold coins](../items/gold.md) | 25% | 8 to 9 |
| [Duskbloom](../items/duskbloom_flower.md) | 15% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_15](../maps/galmore_15.md) | – | 2 | – |
| [galmore_19](../maps/galmore_19.md) | – | 2 | – |
| [galmore_36](../maps/galmore_36.md) | Mt. Galmore | 1 | – |
| [galmore_38](../maps/galmore_38.md) | – | 2 | – |
| [galmore_39](../maps/galmore_39.md) | – | 1 | – |
| [galmore_48](../maps/galmore_48.md) | Mt. Galmore | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bridge_bogling` |
    | Spawn group | `bridge_bogling` |
    | Loot table | `bridge_bogling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_misc:7` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "bridge_bogling",
     "name": "Bridge bogling",
     "iconID": "monsters_misc:7",
     "maxHP": 222,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 5,
      "max": 25
     },
     "droplistID": "bridge_bogling_dl",
     "attackCost": 4,
     "attackChance": 165,
     "blockChance": 150,
     "damageResistance": 8,
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 6,
       "max": 12
      },
      "increaseCurrentAP": {
       "min": 1,
       "max": 2
      },
      "conditionsTarget": [
       {
        "condition": "unsteady_footing",
        "magnitude": 1,
        "duration": 5,
        "chance": "40"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
