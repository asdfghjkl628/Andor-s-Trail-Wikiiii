---
description: "Increased defense is a beneficial physical condition in Andor's Trail: block chance +15, damage resistance +2. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_107.png){ .sprite } Increased defense

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_107.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `increased_defense` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | +15 |
| Damage resistance | +2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Giant's hauberk](../items/haub_giant.md) | When you are hit | 1 | 3 rounds | 15% |
| [Greataxe of broken promises](../items/great_axe_of_bp.md) | When you hit with it | 1 | 3 rounds | 10% |
| [Tonic of blood](../items/tonic_of_blood.md) | When used | 2 | 3 rounds | 15% |
| [Undertell shovel](../items/undertell_shovel.md) | When you defeat an enemy | 1 | 2 rounds | 100% |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Mulgrith](../monsters/mulgrith.md) | On itself, when you hit it | 1 | 1 round | 50% | Galmore 19 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=increased_defense.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `increased_defense` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:107` |
    | Defined in | `res/raw/actorconditions_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "increased_defense",
     "iconID": "actorconditions_1:107",
     "name": "Increased defense",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseMaxHP": 0,
      "increaseBlockChance": 15,
      "increaseDamageResistance": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
