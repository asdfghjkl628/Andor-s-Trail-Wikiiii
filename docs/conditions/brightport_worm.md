---
description: "Brainworm infection is a harmful blood condition in Andor's Trail: attack chance −15, block chance −10, −1 to −2 HP per round. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_52.png){ .sprite } Brainworm infection

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_japozero_52.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `brightport_worm` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −15 |
| Block chance | −10 |
| HP every round | −1 to −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Raw venison](../items/brightport_rawmeat.md) | When used | 1 | 10 rounds | 10% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Virulent forest deer](../monsters/brightport_deer.md) | When it hits you | 1 | 3 rounds | 40% | Brightport |
| [Virulent forest deer](../monsters/brightport_deer.md) | When you defeat it | 2 | 4 rounds | 70% | Brightport |
| [Virulent forest fawn](../monsters/brightport_fawn.md) | When it hits you | 1 | 3 rounds | 40% | Brightport |
| [Virulent forest fawn](../monsters/brightport_fawn.md) | When you defeat it | 2 | 4 rounds | 70% | Brightport |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_worm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_worm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=brightport_worm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `brightport_worm` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_japozero:52` |
    | Defined in | `res/raw/actorconditions_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_worm",
     "iconID": "actorconditions_japozero:52",
     "name": "Brainworm infection",
     "category": "blood",
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -2
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -15,
      "increaseMaxHP": 0,
      "increaseBlockChance": -10
     }
    }
    ```


<small>Data from v0.8.18</small>
