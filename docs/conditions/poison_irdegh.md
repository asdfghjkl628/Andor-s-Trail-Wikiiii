---
description: "Irdegh poison is a harmful blood condition in Andor's Trail: −1 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_60.png){ .sprite } Irdegh poison

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_60.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `poison_irdegh` |

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
| [Ancient piercing irdegh](../monsters/irdegh_4.md) | When it hits you | 3 | 4 rounds | 70% | Waytomountaincave 2 |
| [Irdegh](../monsters/irdegh_1.md) | When it hits you | 3 | 4 rounds | 50% | Waterway 11 east, Waytomountaincave 0 |
| [Irdegh spawn](../monsters/irdegh_sp_1.md) | When it hits you | 2 | 3 rounds | 10% | Brightport |
| [Piercing irdegh](../monsters/irdegh_3.md) | When it hits you | 3 | 4 rounds | 50% | Waytomountaincave 1, Waytomountaincave 2 |
| [Venomous irdegh](../monsters/irdegh_2.md) | When it hits you | 3 | 4 rounds | 50% | Waytomountaincave 0, Waytomountaincave 1, Waytomountaincave 2 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Irdegh poison elixir](../items/pot_irdegh_poison_elixir.md) (when used).
- **Immunity** from [Ring of poison immunity](../items/ring_antipoison.md) (while equipped; while equipped).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_irdegh.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_irdegh.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_irdegh.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `poison_irdegh` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:60` |
    | Defined in | `res/raw/actorconditions_v0611.json` |

    Raw data:

    ```json
    {
     "id": "poison_irdegh",
     "iconID": "actorconditions_1:60",
     "name": "Irdegh poison",
     "category": "blood",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "greenSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
