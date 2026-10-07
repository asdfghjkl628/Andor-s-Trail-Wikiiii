---
description: "Angel of death is an enemy in Andor's Trail (undead) with 198 HP, worth 595 XP, found in haunted_cemetery1, haunted_cemetery2, haunted_forest16. Drops: Angel feather, Gold coins, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_rltiles1_33.png){ .sprite } Angel of death

**Found in:** [haunted_cemetery1](../maps/haunted_cemetery1.md), [haunted_cemetery2](../maps/haunted_cemetery2.md), [haunted_forest16](../maps/haunted_forest16.md), [haunted_forest17](../maps/haunted_forest17.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_33.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | haunted_cemetery1, haunted_cemetery2, haunted_forest16 |
| **Class** | Undead |
| **HP** | 198 |
| **XP when defeated** | 595 |
| **Entry ID** | `angel_death` |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 198 |
| XP when defeated | 595 |
| Damage | 18 to 21 |
| Attack chance | 170 |
| Block chance | 140 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 8 |
| Critical multiplier | 2.0 |
| Critical hit chance | 7% |

**On hit:** On target: Death Plague (magnitude 3, 3 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Angel feather](../items/angel_feather.md) | 5% | 1 |
| [Gold coins](../items/gold.md) | 35% | 10 to 18 |
| [Tonic of blood](../items/tonic_of_blood.md) | 15% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_cemetery1](../maps/haunted_cemetery1.md) | – | 5 | – |
| [haunted_cemetery2](../maps/haunted_cemetery2.md) | – | 4 | – |
| [haunted_forest16](../maps/haunted_forest16.md) | – | 2 | – |
| [haunted_forest17](../maps/haunted_forest17.md) | – | 3 | – |
| [haunted_forest20](../maps/haunted_forest20.md) | – | 1 | – |
| [haunted_forest21](../maps/haunted_forest21.md) | – | 6 | – |
| [haunted_forest22](../maps/haunted_forest22.md) | – | 4 | – |
| [haunted_forest23](../maps/haunted_forest23.md) | – | 2 | – |
| [haunted_forest_way_to_house4](../maps/haunted_forest_way_to_house4.md) | – | 2 | – |
| [haunted_house](../maps/haunted_house.md) | – | 2 | – |
| [vilegard_sullengard_filler1](../maps/vilegard_sullengard_filler1.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `angel_death` |
    | Spawn group | `angel_death` |
    | Loot table | `angel_death_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles1:33` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "angel_death",
     "name": "Angel of death",
     "iconID": "monsters_rltiles1:33",
     "maxHP": 198,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 18,
      "max": 21
     },
     "droplistID": "angel_death_dl",
     "attackCost": 4,
     "attackChance": 170,
     "criticalSkill": 8,
     "criticalMultiplier": 2.0,
     "blockChance": 140,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "death_plague",
        "magnitude": 3,
        "duration": 3,
        "chance": "15"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=angel_death.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=angel_death.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=angel_death.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=angel_death.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
