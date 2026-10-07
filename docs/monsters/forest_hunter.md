---
description: "Forest hunter is an enemy in Andor's Trail (insect) with 90 HP, worth 356 XP, found in haunted_forest1, haunted_forest13, haunted_forest14. Drops: Spider eggs, Dead spider."
---

# ![](../assets/icons/monsters/monsters_tometik10_50.png){ .sprite } Forest hunter

**Found in:** [haunted_forest1](../maps/haunted_forest1.md), [haunted_forest13](../maps/haunted_forest13.md), [haunted_forest14](../maps/haunted_forest14.md), [haunted_forest15](../maps/haunted_forest15.md) (+13 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_50.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | haunted_forest1, haunted_forest13, haunted_forest14 |
| **Class** | Insect |
| **HP** | 90 |
| **XP when defeated** | 356 |
| **Entry ID** | `forest_hunter` |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 90 |
| XP when defeated | 356 |
| Damage | 12 to 21 |
| Attack chance | 150 |
| Block chance | 160 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Insect contagion (magnitude 4, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spider eggs](../items/spider_eggs.md) | 25% | 1 to 2 |
| [Dead spider](../items/spider.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_forest1](../maps/haunted_forest1.md) | – | 4 | – |
| [haunted_forest13](../maps/haunted_forest13.md) | – | 1 | – |
| [haunted_forest14](../maps/haunted_forest14.md) | – | 3 | – |
| [haunted_forest15](../maps/haunted_forest15.md) | – | 2 | – |
| [haunted_forest16](../maps/haunted_forest16.md) | – | 1 | – |
| [haunted_forest19](../maps/haunted_forest19.md) | – | 1 | – |
| [haunted_forest2](../maps/haunted_forest2.md) | – | 3 | – |
| [haunted_forest25](../maps/haunted_forest25.md) | – | 2 | – |
| [haunted_forest3](../maps/haunted_forest3.md) | – | 2 | – |
| [haunted_forest4](../maps/haunted_forest4.md) | – | 2 | – |
| [haunted_forest5](../maps/haunted_forest5.md) | – | 2 | – |
| [haunted_forest6](../maps/haunted_forest6.md) | – | 2 | – |
| [haunted_forest8](../maps/haunted_forest8.md) | – | 1 | – |
| [haunted_forest9](../maps/haunted_forest9.md) | – | 1 | – |
| [haunted_forest_filler](../maps/haunted_forest_filler.md) | – | 2 | – |
| [haunted_forest_way_to_house4](../maps/haunted_forest_way_to_house4.md) | – | 1 | – |
| [vilegard_sullengard_filler1](../maps/vilegard_sullengard_filler1.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `forest_hunter` |
    | Spawn group | `forest_hunter` |
    | Loot table | `forest_hunter_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik10:50` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "forest_hunter",
     "name": "Forest hunter",
     "iconID": "monsters_tometik10:50",
     "maxHP": 90,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 12,
      "max": 21
     },
     "droplistID": "forest_hunter_dl",
     "attackCost": 4,
     "attackChance": 150,
     "blockChance": 160,
     "damageResistance": 6,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 4,
        "duration": 5,
        "chance": "50"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_hunter.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
