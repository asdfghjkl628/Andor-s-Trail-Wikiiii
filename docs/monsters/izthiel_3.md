# ![](../assets/icons/monsters/monsters_rltiles2_48.png){ .sprite } Strong izthiel

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_48.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `izthiel_3` |
| **Type** | Enemy |
| **Class** | Reptile |
| **HP** | 52 |
| **XP when killed** | 182 |
| **Found in** | Flagstone Prison, Brimhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 52 |
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
| Crit chance | none (needs critical skill and a multiplier) |

**On hit:** On target: Bleeding wound (magnitude 2, 4 rounds, 40% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

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
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 40, "c… → {"conditionsTarget": [{"chance": "40", …; name: Strong Izthiel → Strong izthiel |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=izthiel_3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `izthiel_3` |
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


<small>Data from v0.8.18</small>
