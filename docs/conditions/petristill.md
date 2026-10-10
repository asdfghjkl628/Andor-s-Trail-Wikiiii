---
description: "Petristill is a harmful physical condition in Andor's Trail: block chance −10, damage resistance +1. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_11.png){ .sprite } Petristill

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_11.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | Enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `petristill` |

</div>

> A creeping layer of stone overtakes the infliced's form, dulling its reflexes but hardening its body against harm.

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | −10 |
| Damage resistance | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

Nothing in the game data applies this condition to you.

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Kazaul statue](../monsters/dds_kazaul_statue.md) | On itself, when you hit it | 1 | 20 rounds | 100% | Mt. Galmore |
| [Rock eater](../monsters/rock_eater.md) | On itself, when you hit it | 1 | 10 rounds | 100% | Mt. Galmore |
| [Young rock eater](../monsters/young_rock_eater.md) | On itself, when you hit it | 1 | 5 rounds | 45% | Undertell 12, Undertell 13, Undertell 14 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=petristill.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=petristill.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=petristill.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `petristill` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:11` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "petristill",
     "iconID": "actorconditions_1:11",
     "name": "Petristill",
     "description": "A creeping layer of stone overtakes the infliced's form, dulling its reflexes but hardening its body against harm.",
     "category": "physical",
     "isStacking": 1,
     "abilityEffect": {
      "increaseBlockChance": -10,
      "increaseDamageResistance": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
