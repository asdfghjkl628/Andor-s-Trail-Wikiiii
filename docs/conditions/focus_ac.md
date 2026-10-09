---
description: "Focused accuracy is a beneficial mental condition in Andor's Trail: attack chance +40, attack cost +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_98.png){ .sprite } Focused accuracy

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_98.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `focus_ac` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +40 |
| Attack cost (AP) | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Potion of accuracy focus](../items/pot_focus_ac.md) | When used | 1 | 4 rounds | 100% |
| [Strong potion of accuracy focus](../items/pot_focus_ac2.md) | When used | 2 | 4 rounds | 100% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=focus_ac.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=focus_ac.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=focus_ac.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `focus_ac` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:98` |
    | Defined in | `res/raw/actorconditions_v0611.json` |

    Raw data:

    ```json
    {
     "id": "focus_ac",
     "iconID": "actorconditions_1:98",
     "name": "Focused accuracy",
     "category": "mental",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": 40,
      "increaseAttackCost": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
