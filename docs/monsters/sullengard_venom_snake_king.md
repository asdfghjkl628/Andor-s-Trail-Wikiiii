---
description: "King Sullengard forest snake is an enemy in Andor's Trail (reptile) with 207 HP, worth 880 XP, found in way_to_sullengard_east8. Drops: Gold coins, Snake meat, Venomscale scales."
---

# ![](../assets/icons/monsters/monsters_ld2_18.png){ .sprite } King Sullengard forest snake

**Found in:** [way_to_sullengard_east8](../maps/way_to_sullengard_east8.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | way_to_sullengard_east8 |
| **Class** | Reptile |
| **HP** | 207 |
| **XP when defeated** | 880 |
| **Entry ID** | `sullengard_venom_snake_king` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 207 |
| XP when defeated | 880 |
| Damage | 20 to 25 |
| Attack chance | 247 |
| Block chance | 128 |
| Damage resistance | 7 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 3.0 |
| Critical hit chance | 9% |

**On hit:** On target: Nausea (magnitude 3, 5 rounds, 43% chance)

**When hit:** On target: Trapped (magnitude 1, 2 rounds, 100% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1003 to 1300 |
| [Snake meat](../items/snake_meat.md) | 15% | 3 to 6 |
| [Venomscale scales](../items/venomscale.md) | 10% | 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [way_to_sullengard_east8](../maps/way_to_sullengard_east8.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_venom_snake_king` |
    | Spawn group | `sullengard_venom_snake_king` |
    | Loot table | `king_forest_snake_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:18` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_venom_snake_king",
     "name": "King Sullengard forest snake",
     "iconID": "monsters_ld2:18",
     "maxHP": 207,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 20,
      "max": 25
     },
     "droplistID": "king_forest_snake_dl",
     "attackCost": 3,
     "attackChance": 247,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 128,
     "damageResistance": 7,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 3,
        "duration": 5,
        "chance": "43"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "trapped",
        "magnitude": 1,
        "duration": 2,
        "chance": "100"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake_king.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake_king.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake_king.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_venom_snake_king.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
