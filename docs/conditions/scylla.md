---
description: "Scylla's bite is a harmful physical condition in Andor's Trail: −10 to −5 HP per round. Caused by: enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_83.png){ .sprite } Scylla's bite

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_83.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `scylla` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −10 to −5 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Enraged Scylla](../monsters/scylla_c1.md) | When it hits you | 5 | 1 round | 100% | Mountainlake 32 |
| [Furious Scylla](../monsters/scylla_b1.md) | When it hits you | 3 | 1 round | 100% | Mountainlake 32 |
| [Scylla](../monsters/scylla_1.md) | When it hits you | 1 | 1 round | 100% | Mountainlake 32 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| a scripted event | [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-60) | 1 round |
| stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) | [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-60) | 1 round |
| stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) | [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-62) | 2 rounds |
| stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) | [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-66) | 5 rounds |
| stepping on a trigger on [Mountainlake 32](../maps/mountainlake32.md) | – | 2 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=scylla.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=scylla.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=scylla.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `scylla` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:83` |
    | Defined in | `res/raw/actorconditions_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "scylla",
     "iconID": "actorconditions_1:83",
     "name": "Scylla's bite",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": -10,
       "max": -5
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
