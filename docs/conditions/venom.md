---
description: "Venom is a harmful blood condition in Andor's Trail: max HP −2, −1 HP per round. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_2.png){ .sprite } Venom

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
| **Condition ID** | `venom` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | −2 |
| HP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Corrupted swamp core](../items/corrupted_swamp_core.md) | When used | 3 | 5 rounds | 100% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Cave serpent](../monsters/cave_serpent.md) | When it hits you | 1 | 2 rounds | 10% | Basiliskcave 1 1 1, Basiliskcave 1 1 2, Basiliskcave 1 1 3 |
| [Giant snake](../monsters/giant_snake.md) | When it hits you | 2 | 4 rounds | 50% | Fallhaven |
| [Shadowfang](../monsters/shadowfang1.md) | When it hits you | 2 | 4 rounds | 10% | Blackwater mountain 76, Elm 2f 1, Elm 2f 3 |
| [Steelthorn hexileg](../monsters/steelthorn_hexileg.md) | When it hits you | 2 | 4 rounds | 25% | Flagstone Prison |
| [Tough cave serpent](../monsters/tough_cave_serpent.md) | When it hits you | 1 | 3 rounds | 10% | Basiliskcave 1 1 3, Basiliskcave 1 1 4, Basiliskcave 1 1 5 |
| [Venomous cave serpent](../monsters/venomous_cave_serpent.md) | When it hits you | 1 | 3 rounds | 10% | Basiliskcave 1 1 3, Basiliskcave 1 1 4, Basiliskcave 1 1 5 |
| [Young cave serpent](../monsters/young_cave_serpent.md) | When it hits you | 1 | 2 rounds | 10% | Basiliskcave 1 1 1, Basiliskcave 1 1 2, Basiliskcave 1 1 3 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Immunity** from [Ring of poison immunity](../items/ring_antipoison.md) (while equipped; while equipped).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=venom.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `venom` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_japozero:2` |
    | Defined in | `res/raw/actorconditions_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "venom",
     "iconID": "actorconditions_japozero:2",
     "name": "Venom",
     "category": "blood",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "greenSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseMaxHP": -2
     }
    }
    ```


<small>Data from v0.8.18</small>
