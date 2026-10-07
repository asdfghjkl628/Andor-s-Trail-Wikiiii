---
description: "Mountain bridge bogling is an enemy in Andor's Trail (humanoid) with 232 HP, worth 631 XP, found in Mt. Galmore. Drops: Major potion of health, Small tree branch, Gold coins."
---

# ![](../assets/icons/monsters/monsters_misc_6.png){ .sprite } Mountain bridge bogling

**Found in:** Mt. Galmore: [galmore_54](../maps/galmore_54.md), Mt. Galmore: [galmore_55](../maps/galmore_55.md), Mt. Galmore: [galmore_56](../maps/galmore_56.md), Mt. Galmore: [galmore_57](../maps/galmore_57.md) (+8 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_misc_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 232 |
| **XP when defeated** | 631 |
| **Entry ID** | `mt_bridge_bogling` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 232 |
| XP when defeated | 631 |
| Damage | 12 to 19 |
| Attack chance | 170 |
| Block chance | 155 |
| Damage resistance | 8 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**When hit:** Heal HP: 8 to 12; Restore AP: 1 to 2; On target: Unsteady footing (magnitude 1, 7 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Major potion of health](../items/health_major2.md) | 0% | 1 to 2 |
| [Small tree branch](../items/small_tree_branch.md) | 25% | 1 |
| [Gold coins](../items/gold.md) | 25% | 12 to 15 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_54](../maps/galmore_54.md) | Mt. Galmore | 3 | – |
| [galmore_55](../maps/galmore_55.md) | Mt. Galmore | 2 | – |
| [galmore_56](../maps/galmore_56.md) | Mt. Galmore | 2 | – |
| [galmore_57](../maps/galmore_57.md) | Mt. Galmore | 1 | – |
| [galmore_63](../maps/galmore_63.md) | Mt. Galmore | 2 | – |
| [galmore_64](../maps/galmore_64.md) | Mt. Galmore | 1 | – |
| [galmore_65](../maps/galmore_65.md) | Mt. Galmore | 3 | – |
| [galmore_66](../maps/galmore_66.md) | Mt. Galmore | 4 | – |
| [galmore_67](../maps/galmore_67.md) | Mt. Galmore | 1 | – |
| [galmore_73](../maps/galmore_73.md) | Mt. Galmore | 3 | – |
| [galmore_74](../maps/galmore_74.md) | Mt. Galmore | 2 | – |
| [galmore_76](../maps/galmore_76.md) | Mt. Galmore | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mt_bridge_bogling` |
    | Spawn group | `mt_bridge_bogling` |
    | Loot table | `mt_bridge_bogling_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_misc:6` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mt_bridge_bogling",
     "name": "Mountain bridge bogling",
     "iconID": "monsters_misc:6",
     "maxHP": 232,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 12,
      "max": 19
     },
     "droplistID": "mt_bridge_bogling_dl",
     "attackCost": 4,
     "attackChance": 170,
     "blockChance": 155,
     "damageResistance": 8,
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 8,
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
        "duration": 7,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mt_bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mt_bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mt_bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mt_bridge_bogling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
