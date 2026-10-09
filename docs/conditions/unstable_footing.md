---
description: "Unstable footing is a harmful physical condition in Andor's Trail: attack cost +1, move cost +1, −1 AP per round. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_japozero_12.png){ .sprite } Unstable footing

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_12.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | Enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `unstable_footing` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack cost (AP) | +1 |
| Move cost (AP) | +1 |
| AP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

Nothing in the game data applies this condition to you.

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Bridgebreaker](../items/bridgebreaker.md) | On the enemy you hit | 1 | 5 rounds | 5% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=unstable_footing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=unstable_footing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=unstable_footing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `unstable_footing` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_japozero:12` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "unstable_footing",
     "iconID": "actorconditions_japozero:12",
     "name": "Unstable footing",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentAP": {
       "min": -1,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseMoveCost": 1,
      "increaseAttackCost": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
