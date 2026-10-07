---
description: "Scaled venomfang is an enemy in Andor's Trail (reptile) with 35 HP, worth 138 XP, found in Blackwater Mountain. Drops: Gold coins, Meat, Poison gland."
---

# ![](../assets/icons/monsters/monsters_snakes_3.png){ .sprite } Scaled venomfang

**Found in:** Blackwater Mountain: [blackwater_mountain15](../maps/blackwater_mountain15.md), Blackwater Mountain: [blackwater_mountain16](../maps/blackwater_mountain16.md), Blackwater Mountain: [blackwater_mountain17](../maps/blackwater_mountain17.md), Blackwater Mountain: [blackwater_mountain18](../maps/blackwater_mountain18.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_snakes_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Reptile |
| **HP** | 35 |
| **XP when defeated** | 138 |
| **Entry ID** | `scaled_venomfang` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 35 |
| XP when defeated | 138 |
| Damage | 2 to 4 |
| Attack chance | 150 |
| Block chance | 90 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 2 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 10 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Poison gland](../items/gland.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain15](../maps/blackwater_mountain15.md) | Blackwater Mountain | 4 | – |
| [blackwater_mountain16](../maps/blackwater_mountain16.md) | Blackwater Mountain | 11 | – |
| [blackwater_mountain17](../maps/blackwater_mountain17.md) | Blackwater Mountain | 2 | – |
| [blackwater_mountain18](../maps/blackwater_mountain18.md) | Blackwater Mountain | 7 | – |
| [blackwater_mountain3](../maps/blackwater_mountain3.md) | – | 2 | – |
| [blackwater_mountain4](../maps/blackwater_mountain4.md) | – | 5 | – |
| [blackwater_mountain5](../maps/blackwater_mountain5.md) | – | 4 | – |
| [blackwater_mountain53](../maps/blackwater_mountain53.md) | Blackwater Mountain | 4 | – |
| [blackwater_mountain56](../maps/blackwater_mountain56.md) | Blackwater Mountain | 2 | – |
| [blackwater_mountain5a](../maps/blackwater_mountain5a.md) | – | 3 | – |
| [blackwater_mountain70](../maps/blackwater_mountain70.md) | Blackwater Mountain | 2 | – |
| [blackwater_mountain71](../maps/blackwater_mountain71.md) | Blackwater Mountain | 6 | – |
| [bwmfill1](../maps/bwmfill1.md) | Blackwater Mountain | 1 | – |
| [bwmfill2](../maps/bwmfill2.md) | Blackwater Mountain | 3 | – |
| [bwmfill8](../maps/bwmfill8.md) | Blackwater Mountain | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Weak Poison](../conditions/poison_weak.md) (magnitude 1, 2 rounds, 50% chance) → (magnitude 1, 2 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `scaled_venomfang` |
    | Spawn group | `gornaud_2` |
    | Loot table | `cave_serpent` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:3` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "scaled_venomfang",
     "name": "Scaled venomfang",
     "iconID": "monsters_snakes:3",
     "maxHP": 35,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "spawnGroup": "gornaud_2",
     "droplistID": "cave_serpent",
     "attackCost": 3,
     "attackChance": 150,
     "blockChance": 90,
     "damageResistance": 2,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 1,
        "duration": 2,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scaled_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scaled_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scaled_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=scaled_venomfang.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
