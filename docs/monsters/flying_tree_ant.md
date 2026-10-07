---
description: "Flying tree ant is an enemy in Andor's Trail (insect) with 119 HP, worth 479 XP, found in Stoutford, Flagstone Prison, Sullengard. Drops: Insect wing, Insect stinger."
---

# ![](../assets/icons/monsters/monsters_omi2_5.png){ .sprite } Flying tree ant

**Found in:** Deebo's Orchard: [way_to_sullengard_east6](../maps/way_to_sullengard_east6.md), Deebo's Orchard: [way_to_sullengard_east7](../maps/way_to_sullengard_east7.md), Deebo's Orchard: [way_to_sullengard_east7a](../maps/way_to_sullengard_east7a.md), Flagstone Prison: [lake_shore_road7a](../maps/lake_shore_road7a.md) (+22 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford, Flagstone Prison, Sullengard |
| **Class** | Insect |
| **HP** | 119 |
| **XP when defeated** | 479 |
| **Entry ID** | `flying_tree_ant` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 119 |
| XP when defeated | 479 |
| Damage | 9 to 15 |
| Attack chance | 144 |
| Block chance | 207 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 20 |
| Critical multiplier | 3.0 |
| Critical hit chance | 15% |

**On hit:** On target: [Blood poisoning](../conditions/poison_blood.md) (magnitude 5, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Insect wing](../items/insectwing.md) | 10% | 1 |
| [Insect stinger](../items/insect_stinger.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_camp](../maps/aidem_camp.md) | – | 4 | – |
| [galmore_10a](../maps/galmore_10a.md) | – | 2 | – |
| [galmore_13](../maps/galmore_13.md) | Stoutford | 11 | – |
| [galmore_14](../maps/galmore_14.md) | – | 7 | – |
| [galmore_23](../maps/galmore_23.md) | – | 1 | – |
| [lake_shore_road7a](../maps/lake_shore_road7a.md) | Flagstone Prison | 4 | – |
| [lake_shore_road_9](../maps/lake_shore_road_9.md) | – | 3 | – |
| [sullengard_pond](../maps/sullengard_pond.md) | Sullengard | 3 | – |
| [sullengard_west_ravine](../maps/sullengard_west_ravine.md) | – | 2 | – |
| [way_to_sullengard_east11](../maps/way_to_sullengard_east11.md) | – | 6 | – |
| [way_to_sullengard_east2](../maps/way_to_sullengard_east2.md) | – | 4 | – |
| [way_to_sullengard_east2a](../maps/way_to_sullengard_east2a.md) | – | 2 | – |
| [way_to_sullengard_east4](../maps/way_to_sullengard_east4.md) | – | 3 | – |
| [way_to_sullengard_east5](../maps/way_to_sullengard_east5.md) | – | 9 | – |
| [way_to_sullengard_east6](../maps/way_to_sullengard_east6.md) | Deebo's Orchard | 8 | – |
| [way_to_sullengard_east7](../maps/way_to_sullengard_east7.md) | Deebo's Orchard | 13 | – |
| [way_to_sullengard_east7a](../maps/way_to_sullengard_east7a.md) | Deebo's Orchard | 5 | – |
| [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md) | – | 1 | – |
| [way_to_sullengard_east9a](../maps/way_to_sullengard_east9a.md) | – | 1 | – |
| [way_to_sullengard_east_ravine_cabin](../maps/way_to_sullengard_east_ravine_cabin.md) | – | 9 | – |
| [way_to_sullengard_east_ravine_north](../maps/way_to_sullengard_east_ravine_north.md) | – | 7 | – |
| [way_to_sullengard_west_0](../maps/way_to_sullengard_west_0.md) | – | 10 | – |
| [way_to_sullengard_west_1](../maps/way_to_sullengard_west_1.md) | – | 4 | – |
| [way_to_sullengard_west_3](../maps/way_to_sullengard_west_3.md) | – | 4 | – |
| [way_to_sullengard_west_4](../maps/way_to_sullengard_west_4.md) | – | 2 | – |
| [way_to_sullengard_west_5](../maps/way_to_sullengard_west_5.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.14](../versions/0.8.14.md) | Attack cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `flying_tree_ant` |
    | Spawn group | `flying_tree_ant` |
    | Loot table | `flying_insect_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi2:5` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "flying_tree_ant",
     "name": "Flying tree ant",
     "iconID": "monsters_omi2:5",
     "maxHP": 119,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 9,
      "max": 15
     },
     "spawnGroup": "flying_tree_ant",
     "droplistID": "flying_insect_dl",
     "attackCost": 5,
     "attackChance": 144,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 207,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_blood",
        "magnitude": 5,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flying_tree_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flying_tree_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flying_tree_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flying_tree_ant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
