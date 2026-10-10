---
description: "Minor sting is a harmful physical condition in Andor's Trail: −1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_63.png){ .sprite } Minor sting

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_63.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `sting_minor` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Aggressive cave scorpion](../monsters/cave_scorpion_1.md) | When it hits you | 2 | 2 rounds | 20% | Laerothcave 2, Laerothcave 3, Lakecave 0 |
| [Aggressive yellowjacket](../monsters/yjacket6.md) | When it hits you | 2 | 5 rounds | 30% | Lodar 14, Lodar 15 |
| [Armored cave scorpion](../monsters/cave_scorpion_4.md) | When it hits you | 2 | 3 rounds | 25% | Laerothcave 2, Laerothcave 3, Lakecave 0 |
| [Cave scorpion](../monsters/cave_scorpion_0.md) | When it hits you | 1 | 3 rounds | 20% | Laerothcave 3, Lakecave 0, Lakecave 2 |
| [Enraged yellowjacket](../monsters/yjacket7.md) | When it hits you | 3 | 3 rounds | 30% | Lodar 14, Lodar 15 |
| [Fierce cave scorpion](../monsters/cave_scorpion_5.md) | When it hits you | 2 | 3 rounds | 25% | Laerothcave 2, Laerothcave 3, Lakecave 0 |
| [Giant yellowjacket](../monsters/yjacket8.md) | When it hits you | 3 | 5 rounds | 30% | Lodar 14, Lodar 15, Lodar 16 |
| [Poisonous jitterfly](../monsters/poisonous_jitterfly.md) | When it hits you | 3 | 3 rounds | 35% | Deebo's Orchard |
| [Preabola fly](../monsters/preabola_fly.md) | When it hits you | 5 | 5 rounds | 25% | Sullengard |
| [Puny cave scorpion](../monsters/cave_scorpion_2.md) | When it hits you | 1 | 2 rounds | 20% | Laerothcave 3, Lakecave 0, Lakecave 2 |
| [Puny yellowjacket](../monsters/yjacket1.md) | When it hits you | 1 | 3 rounds | 30% | Lodar 11, Lodar 14, Lodar 4 |
| [Quick yellowjacket](../monsters/yjacket5.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 11, Lodar 14, Lodar 15 |
| [Small yellowjacket](../monsters/yjacket2.md) | When it hits you | 1 | 5 rounds | 30% | Lodar 11, Lodar 14, Lodar 4 |
| [Stinging yellowjacket](../monsters/yjacket4.md) | When it hits you | 2 | 5 rounds | 30% | Lodar 11, Lodar 14, Lodar 15 |
| [Swarming yellowjacket](../monsters/yjacket3.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 11, Lodar 14, Lodar 4 |
| [Tough cave scorpion](../monsters/cave_scorpion_3.md) | When it hits you | 2 | 2 rounds | 20% | Laerothcave 2, Laerothcave 3, Lakecave 0 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Mywildcave 3](../maps/mywildcave3.md) | – | 10 rounds |
| walking into a blocked passage on [Mywildcave 2](../maps/mywildcave2.md) | – | 10 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Raider's reach](../items/raiders_reach.md) | On the enemy you hit | 1 | 2 rounds | 10% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=sting_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=sting_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=sting_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `sting_minor` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:63` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "sting_minor",
     "iconID": "actorconditions_1:63",
     "name": "Minor sting",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
