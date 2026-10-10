---
description: "Yellow tooth slitherer is an enemy in Andor's Trail (reptile) with 121 HP, worth 452 XP, found in Deebo's Orchard. Drops: Snake meat, Poison gland, Venomscale scales."
---

# ![](../assets/icons/monsters/monsters_snakes_5.png){ .sprite } Yellow tooth slitherer

**Found in:** Deebo's Orchard: [Sullengard apple farm south](../maps/sullengard_apple_farm_south.md), Deebo's Orchard: [Way to sullengard east 6](../maps/way_to_sullengard_east6.md), Deebo's Orchard: [Way to sullengard east 7](../maps/way_to_sullengard_east7.md), [Cabin norcity road 4](../maps/cabin_norcity_road4.md) (+12 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_snakes_5.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Deebo's Orchard |
| **Class** | Reptile |
| **HP** | 121 |
| **XP when defeated** | 452 |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 121 |
| XP when defeated | 452 |
| Damage | 10 to 16 |
| AC | 215 |
| BC | 92 |
| DR | 3 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×2.5) |

**Its hits:** On target: [Nausea](../conditions/nausea.md) (magnitude 3, 4 rounds, 42% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Snake meat](../items/snake_meat.md) | 5% | 1 |
| [Poison gland](../items/gland.md) | 30% | 1 |
| [Venomscale scales](../items/venomscale.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Cabin norcity road 4](../maps/cabin_norcity_road4.md) | – | 2 | – |
| [Sullengard apple farm south](../maps/sullengard_apple_farm_south.md) | Deebo's Orchard | 6 | – |
| [Sullengard ravine 2](../maps/sullengard_ravine2.md) | – | 2 | – |
| [Sullengard woods 6](../maps/sullengard_woods6.md) | – | 2 | – |
| [Way to aidem camp 1](../maps/way_to_aidem_camp_1.md) | – | 3 | – |
| [Way to sullengard east 1](../maps/way_to_sullengard_east1.md) | – | 5 | – |
| [Way to sullengard east 2](../maps/way_to_sullengard_east2.md) | – | 6 | – |
| [Way to sullengard east 4](../maps/way_to_sullengard_east4.md) | – | 4 | – |
| [Way to sullengard east 4 bridge](../maps/way_to_sullengard_east4_bridge.md) | – | 3 | – |
| [Way to sullengard east 5](../maps/way_to_sullengard_east5.md) | – | 4 | – |
| [Way to sullengard east 5 filler](../maps/way_to_sullengard_east5_filler.md) | – | 5 | – |
| [Way to sullengard east 6](../maps/way_to_sullengard_east6.md) | Deebo's Orchard | 5 | – |
| [Way to sullengard east 7](../maps/way_to_sullengard_east7.md) | Deebo's Orchard | 4 | – |
| [Way to sullengard east 8](../maps/way_to_sullengard_east8.md) | – | 3 | – |
| [Way to sullengard east ravine](../maps/way_to_sullengard_east_ravine.md) | – | 5 | – |
| [Way to sullengard east ravine north](../maps/way_to_sullengard_east_ravine_north.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `yellow_tooth` |
    | Type (wiki) | Enemy |
    | Spawn group | `yellow_tooth` |
    | Loot table | `yellow_tooth_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_snakes:5` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "yellow_tooth",
     "name": "Yellow tooth slitherer",
     "iconID": "monsters_snakes:5",
     "maxHP": 121,
     "moveCost": 5,
     "monsterClass": "reptile",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 16
     },
     "spawnGroup": "yellow_tooth",
     "droplistID": "yellow_tooth_dl",
     "attackCost": 3,
     "attackChance": 215,
     "criticalSkill": 10,
     "criticalMultiplier": 2.5,
     "blockChance": 92,
     "damageResistance": 3,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 3,
        "duration": 4,
        "chance": "42"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yellow_tooth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yellow_tooth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yellow_tooth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yellow_tooth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
