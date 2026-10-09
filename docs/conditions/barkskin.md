---
description: "Bark skin is a beneficial physical condition in Andor's Trail: damage resistance +1. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_20.png){ .sprite } Bark skin

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `barkskin` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Damage resistance | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Engraved steel helmet](../items/brimhaven_engraved_steel_helmet.md) | When you are hit | 1 | 2 rounds | 5% |
| [Guynmart shield](../items/guynmart_shield.md) | When you are hit | 2 | 2 rounds | 20% |
| [Potion of bark skin](../items/pot_barkskin.md) | When used | 1 | 15 rounds | 100% |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [River snapper](../monsters/sutdover_snapper.md) | On itself, when you hit it | 1 | 3 rounds | 15% | Mt. Galmore |
| [Snapmaw](../monsters/snapmaw.md) | On itself, when you hit it | 1 | 3 rounds | 15% | Mt. Galmore |
| [Sullengard snapper](../monsters/sullengard_snapper.md) | On itself, when you hit it | 1 | 5 rounds | 5% | Sullengard |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=barkskin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=barkskin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=barkskin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `barkskin` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:20` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "barkskin",
     "iconID": "actorconditions_1:20",
     "name": "Bark skin",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseDamageResistance": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
