---
description: "Divine punishment is a harmful spiritual condition in Andor's Trail: attack chance −10, block chance −20, −2 to −1 HP per round. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_30.png){ .sprite } Divine punishment

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_30.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `divine_punishment` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −10 |
| Block chance | −20 |
| HP every round | −2 to −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Judicar](../items/judicar.md) | When you hit with it | 1 | 2 rounds | 5% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Kazaul crimson arbiter lich](../monsters/kazaul_crimson_arbiter_lich.md) | When you defeat it | 1 | 2 rounds | 100% | Undertell 4 00, Undertell 4 01, Undertell 4 10 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** none; spiritual conditions ignore resistance skills.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=divine_punishment.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=divine_punishment.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=divine_punishment.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `divine_punishment` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_japozero:30` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "divine_punishment",
     "iconID": "actorconditions_japozero:30",
     "name": "Divine punishment",
     "category": "spiritual",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseBlockChance": -20
     }
    }
    ```


<small>Data from v0.8.18</small>
