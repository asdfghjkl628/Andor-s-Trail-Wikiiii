---
description: "Sullengard forest snake is an enemy in Andor's Trail (reptile) with 148 HP, worth 631 XP, found in Sullengard. Drops: Poison gland, Snake meat, Venomscale scales."
---

# ![](../assets/icons/monsters/monsters_tometik4_24.png){ .sprite } Sullengard forest snake

**Found in:** Sullengard: [sullengard5](../maps/sullengard5.md), Sullengard: [sullengard6](../maps/sullengard6.md), Sullengard: [sullengard_pond](../maps/sullengard_pond.md), [aidem_camp](../maps/aidem_camp.md) (+24 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_24.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard |
| **Class** | Reptile |
| **HP** | 148 |
| **XP when defeated** | 631 |
| **Entry ID** | `sullengard_venom_snake` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 148 |
| XP when defeated | 631 |
| Damage | 15 to 22 |
| Attack chance | 220 |
| Block chance | 108 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 3.0 |
| Critical hit chance | 9% |

**On hit:** On target: Nausea (magnitude 3, 5 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Poison gland](../items/gland.md) | 30% | 1 |
| [Snake meat](../items/snake_meat.md) | 15% | 1 to 3 |
| [Venomscale scales](../items/venomscale.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_camp](../maps/aidem_camp.md) | – | 2 | – |
| [sullengard5](../maps/sullengard5.md) | Sullengard | 1 | – |
| [sullengard6](../maps/sullengard6.md) | Sullengard | 5 | – |
| [sullengard9](../maps/sullengard9.md) | – | 3 | – |
| [sullengard_pond](../maps/sullengard_pond.md) | Sullengard | 1 | – |
| [sullengard_woods10](../maps/sullengard_woods10.md) | – | 3 | – |
| [sullengard_woods11](../maps/sullengard_woods11.md) | – | 4 | – |
| [sullengard_woods12](../maps/sullengard_woods12.md) | – | 11 | – |
| [sullengard_woods13](../maps/sullengard_woods13.md) | – | 1 | – |
| [sullengard_woods14](../maps/sullengard_woods14.md) | – | 2 | – |
| [sullengard_woods2](../maps/sullengard_woods2.md) | – | 4 | – |
| [sullengard_woods3](../maps/sullengard_woods3.md) | – | 8 | – |
| [sullengard_woods4](../maps/sullengard_woods4.md) | – | 6 | – |
| [sullengard_woods5](../maps/sullengard_woods5.md) | – | 8 | – |
| [sullengard_woods6](../maps/sullengard_woods6.md) | – | 8 | – |
| [sullengard_woods7](../maps/sullengard_woods7.md) | – | 6 | – |
| [sullengard_woods8](../maps/sullengard_woods8.md) | – | 1 | – |
| [sullengard_woods9](../maps/sullengard_woods9.md) | – | 8 | – |
| [way_to_aidem_camp_1](../maps/way_to_aidem_camp_1.md) | – | 5 | – |
| [way_to_sullengard_east10](../maps/way_to_sullengard_east10.md) | – | 6 | – |
| [way_to_sullengard_east11](../maps/way_to_sullengard_east11.md) | – | 1 | – |
| [way_to_sullengard_east4](../maps/way_to_sullengard_east4.md) | – | 3 | – |
| [way_to_sullengard_east8](../maps/way_to_sullengard_east8.md) | – | 6 | – |
| [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md) | – | 1 | – |
| [way_to_sullengard_east9a](../maps/way_to_sullengard_east9a.md) | – | 2 | – |
| [way_to_sullengard_east_ravine_cabin](../maps/way_to_sullengard_east_ravine_cabin.md) | – | 2 | – |
| [way_to_sullengard_east_ravine_north](../maps/way_to_sullengard_east_ravine_north.md) | – | 2 | – |
| [way_to_sullengard_pond_road](../maps/way_to_sullengard_pond_road.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_venom_snake` |
    | Spawn group | `sullengard_venom_snake` |
    | Loot table | `forest_snake_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik4:24` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_venom_snake",
     "name": "Sullengard forest snake",
     "iconID": "monsters_tometik4:24",
     "maxHP": 148,
     "moveCost": 5,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 15,
      "max": 22
     },
     "spawnGroup": "sullengard_venom_snake",
     "droplistID": "forest_snake_dl",
     "attackCost": 3,
     "attackChance": 220,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 108,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
