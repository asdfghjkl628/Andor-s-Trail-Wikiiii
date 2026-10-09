---
description: "Blessing of Shadow accuracy is a beneficial spiritual condition in Andor's Trail: attack chance +30. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_98.png){ .sprite } Blessing of Shadow accuracy

*Beneficial spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_98.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `shadowbless_acc` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +30 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Talion](../monsters/talion.md) | – | 30 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_acc.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_acc.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_acc.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `shadowbless_acc` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:98` |
    | Defined in | `res/raw/actorconditions_v0611_2.json` |

    Raw data:

    ```json
    {
     "id": "shadowbless_acc",
     "iconID": "actorconditions_1:98",
     "name": "Blessing of Shadow accuracy",
     "category": "spiritual",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": 30
     }
    }
    ```


<small>Data from v0.8.18</small>
