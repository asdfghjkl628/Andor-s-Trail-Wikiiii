---
description: "Flesh rot is a harmful physical condition in Andor's Trail: block chance −5, −1 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_82.png){ .sprite } Flesh rot

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_82.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `flesh_rot` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | −5 |
| HP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Resurrected miner's skeleton](../monsters/elm_miner1.md) | When it hits you | 4 | 2 rounds | 25% | Elm 5f 1, Elm 5f 2, Elm 4f 2 |
| [Revenant](../monsters/revenant.md) | When it hits you | 2 | 3 rounds | 20% | Waterwayacave 2, Waterwayacave 3, Waterwayacave 4 |
| [Revenant servant](../monsters/revenant_servant.md) | When it hits you | 1 | 3 rounds | 10% | Waterwayacave 2, Waterwayacave 3, Waterwayacave 4 |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Resurrected miner's skeleton](../monsters/elm_miner1.md) | On itself, when it hits you | 4 | 2 rounds | 25% | Elm 5f 1, Elm 5f 2, Elm 4f 2 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=flesh_rot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=flesh_rot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=flesh_rot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `flesh_rot` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:82` |
    | Defined in | `res/raw/actorconditions_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "flesh_rot",
     "iconID": "actorconditions_1:82",
     "name": "Flesh rot",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseBlockChance": -5
     }
    }
    ```


<small>Data from v0.8.18</small>
