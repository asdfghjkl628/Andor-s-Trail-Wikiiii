---
description: "Spiked cyclopea creeper is an enemy in Andor's Trail (reptile) with 238 HP, worth 558 XP, found in way_to_sullengard_west_2, way_to_sullengard_west_4. Drops: Cyclopean eye gem, Cyclopea root, Photosynthetic leaf."
---

# ![](../assets/icons/monsters/monsters_newb_1_1088.png){ .sprite } Spiked cyclopea creeper

**Found in:** [way_to_sullengard_west_2](../maps/way_to_sullengard_west_2.md), [way_to_sullengard_west_4](../maps/way_to_sullengard_west_4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_1088.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | way_to_sullengard_west_2, way_to_sullengard_west_4 |
| **Class** | Reptile |
| **HP** | 238 |
| **XP when defeated** | 558 |
| **Entry ID** | `spiked_cyclopea_creeper` |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 238 |
| XP when defeated | 558 |
| Damage | 4 to 6 |
| Attack chance | 140 |
| Block chance | 183 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 6 AP |
| Attacks per turn | 2 |
| Move cost | 8 AP |
| Critical skill | 12 |
| Critical multiplier | 2.0 |
| Critical hit chance | 10% |

**On hit:** On target: [Rootsnare](../conditions/rootsnare.md) (magnitude 1, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Cyclopean eye gem](../items/cyclopean_eye_gem.md) | 2% | 1 |
| [Cyclopea root](../items/cyclopea_root.md) | 3% | 1 |
| [Photosynthetic leaf](../items/photosynthetic_leaf.md) | 4% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [way_to_sullengard_west_2](../maps/way_to_sullengard_west_2.md) | – | 3 | – |
| [way_to_sullengard_west_4](../maps/way_to_sullengard_west_4.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `spiked_cyclopea_creeper` |
    | Spawn group | `spiked_cyclopea_creeper` |
    | Loot table | `spiked_cyclopea_creeper_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_newb_1:1088` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "spiked_cyclopea_creeper",
     "name": "Spiked cyclopea creeper",
     "iconID": "monsters_newb_1:1088",
     "maxHP": 238,
     "maxAP": 12,
     "moveCost": 8,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 4,
      "max": 6
     },
     "droplistID": "spiked_cyclopea_creeper_dl",
     "attackCost": 6,
     "attackChance": 140,
     "criticalSkill": 12,
     "criticalMultiplier": 2.0,
     "blockChance": 183,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "rootsnare",
        "magnitude": 1,
        "duration": 3,
        "chance": "20"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spiked_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spiked_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spiked_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spiked_cyclopea_creeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
