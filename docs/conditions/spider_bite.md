---
description: "Spider bite is a harmful blood condition in Andor's Trail: −4 to −1 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_omi2_3.png){ .sprite } Spider bite

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_omi2_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `spider_bite` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −4 to −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Basement spider](../monsters/laerothbasement_spider.md) | When it hits you | 1 | 4 rounds | 15% | Lake Laeroth |
| [Dirt spider](../monsters/dirt_spider.md) | When it hits you | 1 | 4 rounds | 15% | Stoutford, Mt. Galmore |
| [Giant spider](../monsters/spider_massive.md) | When it hits you | 2 | 4 rounds | 30% | Lake Laeroth |
| [Grass spider](../monsters/grass_spider.md) | When it hits you | 1 | 4 rounds | 15% | Mt. Galmore, Flagstone Prison, Wexlow Village |
| [Queen spider](../monsters/spider_queen.md) | When it hits you | 3 | 5 rounds | 70% | Laerothcave 2, Secretpassage 1, Undertell 1 1 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spider_bite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spider_bite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spider_bite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `spider_bite` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_omi2:3` |
    | Defined in | `res/raw/actorconditions_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "spider_bite",
     "iconID": "actorconditions_omi2:3",
     "name": "Spider bite",
     "category": "blood",
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": -4,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
