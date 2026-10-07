---
description: "Clumsiness is a harmful mental condition in Andor's Trail: attack chance −7, block chance −7. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_japozero_49.png){ .sprite } Clumsiness

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_49.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `clumsiness` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −7 |
| Block chance | −7 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Feline gloves](../items/feline_gloves.md) | While equipped | 1 | While equipped | – |
| [Feline hat](../items/feline_hat.md) | While equipped | 1 | While equipped | – |
| [Feline shoes](../items/feline_shoes.md) | While equipped | 1 | While equipped | – |
| [Potion of deftness](../items/potion_deftness_bad.md) | When used | 2 | 2 rounds | 60% |
| [Valugha's gloves](../items/valugha_gloves.md) | While equipped | 1 | While equipped | – |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=clumsiness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=clumsiness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=clumsiness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `clumsiness` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_japozero:49` |
    | Defined in | `res/raw/actorconditions_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "clumsiness",
     "iconID": "actorconditions_japozero:49",
     "name": "Clumsiness",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackChance": -7,
      "increaseBlockChance": -7
     }
    }
    ```


<small>Data from v0.8.18</small>
