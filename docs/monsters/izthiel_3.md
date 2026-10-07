---
description: "Strong izthiel is an enemy in Andor's Trail (reptile) with 52 HP, worth 182 XP, found in Flagstone Prison, Brimhaven. Drops: Gold coins, Izthiel claw, Jinxed ring of damage resistance, Polished ring."
---

# ![](../assets/icons/monsters/monsters_rltiles2_48.png){ .sprite } Strong izthiel

**Found in:** Brimhaven: [waterway12](../maps/waterway12.md), Brimhaven: [waterway6](../maps/waterway6.md), Flagstone Prison: [lake_shore_road_6](../maps/lake_shore_road_6.md), Flagstone Prison: [lake_shore_road_7](../maps/lake_shore_road_7.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_48.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Brimhaven |
| **Class** | Reptile |
| **HP** | 52 |
| **XP when defeated** | 182 |
| **Entry ID** | `izthiel_3` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 52 |
| XP when defeated | 182 |
| Damage | 2 to 7 |
| Attack chance | 80 |
| Block chance | 60 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 2, 4 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 15 |
| [Izthiel claw](../items/izthiel_claw.md) | 30% | 1 |
| [Jinxed ring of damage resistance](../items/ring_jinxed1.md) | 1% | 1 |
| [Polished ring](../items/ring2.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lake_shore_road_3](../maps/lake_shore_road_3.md) | – | 2 | – |
| [lake_shore_road_6](../maps/lake_shore_road_6.md) | Flagstone Prison | 1 | – |
| [lake_shore_road_7](../maps/lake_shore_road_7.md) | Flagstone Prison | 1 | – |
| [waterway1](../maps/waterway1.md) | – | 4 | – |
| [waterway12](../maps/waterway12.md) | Brimhaven | 2 | – |
| [waterway13](../maps/waterway13.md) | – | 3 | – |
| [waterway2](../maps/waterway2.md) | – | 2 | – |
| [waterway3](../maps/waterway3.md) | – | 6 | – |
| [waterway4](../maps/waterway4.md) | – | 6 | – |
| [waterway5](../maps/waterway5.md) | – | 4 | – |
| [waterway6](../maps/waterway6.md) | Brimhaven | 4 | – |
| [waterway7](../maps/waterway7.md) | – | 2 | – |
| [waterway8](../maps/waterway8.md) | – | 4 | – |
| [waterway9](../maps/waterway9.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 2, 4 rounds, 40% chance) → (magnitude 2, 4 rounds, 40% chance)<br>Renamed “Strong Izthiel” → “Strong izthiel” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `izthiel_3` |
    | Spawn group | `izthiel_3` |
    | Loot table | `izthiel` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:48` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "izthiel_3",
     "name": "Strong izthiel",
     "iconID": "monsters_rltiles2:48",
     "maxHP": 52,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 7
     },
     "spawnGroup": "izthiel_3",
     "droplistID": "izthiel",
     "attackCost": 3,
     "attackChance": 80,
     "blockChance": 60,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 2,
        "duration": 4,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
