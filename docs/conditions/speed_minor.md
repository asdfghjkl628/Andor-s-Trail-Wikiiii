---
description: "Minor speed is a beneficial physical condition in Andor's Trail: max AP +2. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_87.png){ .sprite } Minor speed

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_87.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `speed_minor` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | +2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Axe of whirlwind](../items/axe_whirl.md) | When you hit with it | 1 | 3 rounds | 5% |
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 2 | 4 rounds | 10% |
| [Major potion of speed](../items/major_potion_speed.md) | When used | 2 | 5 rounds | 100% |
| [Minor potion of speed](../items/pot_speed_1.md) | When used | 1 | 5 rounds | 100% |
| [Stiletto](../items/stiletto.md) | When you defeat an enemy | 2 | 2 rounds | 5% |
| [Superior stiletto](../items/stiletto_superior.md) | When you hit with it | 2 | 2 rounds | 1% |
| [Thieves' cloak of whispers](../items/thieve_clock_whispers.md) | When you defeat an enemy | 1 | 3 rounds | 10% |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Rubycrest strider](../monsters/rubycrest_strider.md) | On itself, when you hit it | 1 | 1 round | 50% | Stoutford |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=speed_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=speed_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=speed_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `speed_minor` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:87` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "speed_minor",
     "iconID": "actorconditions_1:87",
     "name": "Minor speed",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseMaxAP": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
