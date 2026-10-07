---
description: "Panic is a harmful mental condition in Andor's Trail: max AP +4, attack chance +10, block chance +10, critical skill +10, −1 to +1 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_omi2_0.png){ .sprite } Panic

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_omi2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | Enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `panic` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | +4 |
| Attack chance | +10 |
| Block chance | +10 |
| Critical skill | +10 |
| HP every round | −1 to +1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

Nothing in the game data applies this condition to you.

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Albino olm](../monsters/bwm_olm2.md) | On itself, when you hit it | 1 | 3 rounds | 20% | blackwater_mountain74, blackwater_mountain74_h, blackwater_mountain75 |
| [Blackened olm](../monsters/bwm_olm4.md) | On itself, when you hit it | 1 | 3 rounds | 30% | blackwater_mountain75, elm_4f_5, elm_mine2 |
| [Contaminated olm](../monsters/bwm_olm5.md) | On itself, when you hit it | 1 | 3 rounds | 30% | elm_2f_1, elm_3f, elm_4f_1 |
| [Dun olm](../monsters/bwm_olm1.md) | On itself, when you hit it | 1 | 1 round | 20% | blackwater_mountain74, blackwater_mountain74_h, blackwater_mountain75 |
| [Hard-skinned olm](../monsters/bwm_olm3.md) | On itself, when you hit it | 1 | 2 rounds | 20% | blackwater_mountain75, elm_4f_5, elm_mine2 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=panic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=panic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=panic.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `panic` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_omi2:0` |
    | Defined in | `res/raw/actorconditions_omi2.json` |

    Raw data:

    ```json
    {
     "id": "panic",
     "iconID": "actorconditions_omi2:0",
     "name": "Panic",
     "category": "mental",
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": -1,
       "max": 1
      }
     },
     "abilityEffect": {
      "increaseAttackChance": 10,
      "increaseMaxAP": 4,
      "increaseCriticalSkill": 10,
      "increaseBlockChance": 10
     }
    }
    ```


<small>Data from v0.8.18</small>
