---
description: "Poisonous vapors is a harmful blood condition in Andor's Trail: −2 to 0 HP per round, −2 to 0 HP per 25 s. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_58.png){ .sprite } Poisonous vapors

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_58.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `brightport_poison` |

</div>

> Emitted by the creatures adapted to the poisoned environment.

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −2 to 0 |
| HP every 25 seconds (outside combat) | −2 to 0 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Moonwalker tree stump](../monsters/brightport_tree.md) | When you defeat it | 2 | 4 rounds | 15% | Brightport |
| [Blooming amoeba](../monsters/brightport_amoeba.md) | When you hit it | 1 | 8 rounds | 80% | Brightport |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `brightport_poison` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:58` |
    | Defined in | `res/raw/actorconditions_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_poison",
     "iconID": "actorconditions_1:58",
     "name": "Poisonous vapors",
     "description": "Emitted by the creatures adapted to the poisoned environment.",
     "category": "blood",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": 0
      }
     },
     "fullRoundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": 0
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
