---
description: "Potent venom is a harmful blood condition in Andor's Trail: max HP −3, move cost +1, −3 to −2 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_2.png){ .sprite } Potent venom

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `potent_venom` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | −3 |
| Move cost (AP) | +1 |
| HP every round | −3 to −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Venomous swamp creature](../monsters/venomous_swamp_creature.md) | When it hits you | 1 | 3 rounds | 15% | Galmore 28 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=potent_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=potent_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=potent_venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `potent_venom` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_japozero:2` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "potent_venom",
     "iconID": "actorconditions_japozero:2",
     "name": "Potent venom",
     "category": "blood",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "greenSplash",
      "increaseCurrentHP": {
       "min": -3,
       "max": -2
      }
     },
     "abilityEffect": {
      "increaseMaxHP": -3,
      "increaseMoveCost": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
