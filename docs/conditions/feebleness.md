---
description: "Weapon feebleness is a harmful mental condition in Andor's Trail: attack chance −5, damage −2. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_74.png){ .sprite } Weapon feebleness

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_74.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | Enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `feebleness` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −5 |
| Attack damage | −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

Nothing in the game data applies this condition to you.

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Heartsteel blade breaker](../items/heartstone_blade_breaker.md) | On the enemy that misses you | 3 | 3 rounds | 8% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `feebleness` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:74` |
    | Defined in | `res/raw/actorconditions_undertell.json` |

    Raw data:

    ```json
    {
     "id": "feebleness",
     "iconID": "actorconditions_1:74",
     "name": "Weapon feebleness",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackChance": -5,
      "increaseAttackDamage": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
