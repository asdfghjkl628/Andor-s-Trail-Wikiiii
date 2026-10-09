---
description: "Minor increased defense is a beneficial physical condition in Andor's Trail: attack chance −10, block chance +7, damage resistance +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_107.png){ .sprite } Minor increased defense

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_107.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `minor_increased_defense` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −10 |
| Block chance | +7 |
| Damage resistance | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Armored boots](../items/armored_boots.md) | When you are hit | 1 | 1 round | 3% |
| [Armored gloves](../items/armored_gloves.md) | When you are hit | 1 | 2 rounds | 3% |
| [Armored helmet](../items/armored_helmet.md) | When you are hit | 1 | 2 rounds | 3% |
| [Stormcloak armor](../items/stormcloak_armor.md) | When you are hit | 1 | 1 round | 3% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=minor_increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=minor_increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=minor_increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `minor_increased_defense` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:107` |
    | Defined in | `res/raw/actorconditions_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "minor_increased_defense",
     "iconID": "actorconditions_1:107",
     "name": "Minor increased defense",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseMaxHP": 0,
      "increaseBlockChance": 7,
      "increaseDamageResistance": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
