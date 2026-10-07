---
description: "Fatigue is a harmful physical condition in Andor's Trail: −2 HP per round, −1 AP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_89.png){ .sprite } Fatigue

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_89.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `fatigue2` |

</div>

!!! note "Other conditions named Fatigue"
    The game data defines 4 separate conditions with this name, each with its own effects: [`fatigue1`](fatigue1.md), [`fatigue3`](fatigue3.md), [`fatigue4`](fatigue4.md).

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −2 |
| AP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Undertell shovel](../items/undertell_shovel.md) | When you hit with it | 1 | 1 round | 10% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – | 99 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md).
- **Duration and rest:** timed ones wear off, or rest them away.

## Checked in dialogue

- stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) checks whether you have this condition.
- stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) checks whether you do not have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `fatigue2` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:89` |
    | Defined in | `res/raw/actorconditions_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "fatigue2",
     "iconID": "actorconditions_1:89",
     "name": "Fatigue",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": -2
      },
      "increaseCurrentAP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
