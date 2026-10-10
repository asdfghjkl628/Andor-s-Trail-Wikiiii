---
description: "Strength is a beneficial physical condition in Andor's Trail: damage +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_70.png){ .sprite } Strength

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_70.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `str` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack damage | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Cyclopea root](../items/cyclopea_root.md) | When used | 4 | 5 rounds | 100% |
| [Gleaming claymore of ruin](../items/clmr_ruin.md) | When you hit with it | 1 | 2 rounds | 15% |
| [Healthier worm meat](../items/better_worm_meat.md) | When used | 2 | 3 rounds | 100% |
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 2 | 9 rounds | 10% |
| [Minor potion of strength](../items/pot_str.md) | When used | 1 | 5 rounds | 100% |
| [Thunderguard Copper sword](../items/thunderguard_2h_sword.md) | When you hit with it | 1 | 2 rounds | 10% |
| [Toasted inkyfish](../items/bwm_fish3.md) | When used | 3 | 5 rounds | 10% |
| [Wraith's massive claymore](../items/clmr_wrmas.md) | When you defeat an enemy | 2 | 5 rounds | 55% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `str` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:70` |
    | Defined in | `res/raw/actorconditions_v069.json` |

    Raw data:

    ```json
    {
     "id": "str",
     "iconID": "actorconditions_1:70",
     "name": "Strength",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
