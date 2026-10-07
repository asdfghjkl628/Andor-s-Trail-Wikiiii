---
description: "Requiescence is a harmful mental condition in Andor's Trail: max AP −4, attack chance −50, damage −5, block chance −80, damage resistance −2, critical skill −20, attack cost +2, item use cost −1, re-equip cost −1, +2 HP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_omi2_4.png){ .sprite } Requiescence

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_omi2_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `relax` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | −4 |
| Attack chance | −50 |
| Attack damage | −5 |
| Block chance | −80 |
| Damage resistance | −2 |
| Critical skill | −20 |
| Attack cost (AP) | +2 |
| Use item cost (AP) | −1 |
| Re-equip cost (AP) | −1 |
| HP every round | +2 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Gloriosa mushroom soup](../items/gloriosa_mushroom_soup.md) | When used | 1 | 5 rounds | 5% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [elm_2f_2](../maps/elm_2f_2.md) | – | 1 round |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Strong Mind](../skills/resistanceMental.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=relax.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=relax.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=relax.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `relax` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_omi2:4` |
    | Defined in | `res/raw/actorconditions_omi2.json` |

    Raw data:

    ```json
    {
     "id": "relax",
     "iconID": "actorconditions_omi2:4",
     "name": "Requiescence",
     "category": "mental",
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": 2,
       "max": 2
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -50,
      "increaseAttackDamage": {
       "min": -5,
       "max": -5
      },
      "increaseMaxAP": -4,
      "increaseUseItemCost": -1,
      "increaseReequipCost": -1,
      "increaseAttackCost": 2,
      "increaseCriticalSkill": -20,
      "increaseBlockChance": -80,
      "increaseDamageResistance": -2
     }
    }
    ```


<small>Data from v0.8.18</small>
