---
description: "Sullengard red forest snake is an enemy in Andor's Trail (reptile) with 175 HP, worth 768 XP, found in sullengard_west_ravine, sullengard_woods1, sullengard_woods13. Drops: Poison gland, Snake meat, Venomscale scales."
---

# ![](../assets/icons/monsters/monsters_tometik4_27.png){ .sprite } Sullengard red forest snake

**Found in:** [sullengard_west_ravine](../maps/sullengard_west_ravine.md), [sullengard_woods1](../maps/sullengard_woods1.md), [sullengard_woods13](../maps/sullengard_woods13.md), [sullengard_woods14](../maps/sullengard_woods14.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_27.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | sullengard_west_ravine, sullengard_woods1, sullengard_woods13 |
| **Class** | Reptile |
| **HP** | 175 |
| **XP when defeated** | 768 |
| **Entry ID** | `sull_red_forest_snake` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 175 |
| XP when defeated | 768 |
| Damage | 18 to 25 |
| Attack chance | 245 |
| Block chance | 115 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 2.75 |
| Critical hit chance | 9% |

**On hit:** On target: Nausea (magnitude 3, 5 rounds, 50% chance)


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
| [sullengard_west_ravine](../maps/sullengard_west_ravine.md) | – | 10 | – |
| [sullengard_woods1](../maps/sullengard_woods1.md) | – | 5 | – |
| [sullengard_woods13](../maps/sullengard_woods13.md) | – | 3 | – |
| [sullengard_woods14](../maps/sullengard_woods14.md) | – | 7 | – |
| [sullengard_woods2](../maps/sullengard_woods2.md) | – | 1 | – |
| [sullengard_woods_gj1](../maps/sullengard_woods_gj1.md) | – | 13 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sull_red_forest_snake` |
    | Spawn group | `sull_red_forest_snake` |
    | Loot table | `forest_snake_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik4:27` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sull_red_forest_snake",
     "name": "Sullengard red forest snake",
     "iconID": "monsters_tometik4:27",
     "maxHP": 175,
     "moveCost": 4,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 18,
      "max": 25
     },
     "spawnGroup": "sull_red_forest_snake",
     "droplistID": "forest_snake_dl",
     "attackCost": 3,
     "attackChance": 245,
     "criticalSkill": 10,
     "criticalMultiplier": 2.75,
     "blockChance": 115,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_red_forest_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_red_forest_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_red_forest_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_red_forest_snake.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
