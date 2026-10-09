---
description: "Blessing of Shadow strength is a beneficial spiritual condition in Andor's Trail: damage +1. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_70.png){ .sprite } Blessing of Shadow strength

*Beneficial spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_70.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `shadowbless_str` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack damage | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Talion](../monsters/talion.md) | – | 30 rounds |
| [Talion](../monsters/talion.md) | [Shadows](../quests/shadows.md#stage-90) | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) during [Shadows](../quests/shadows.md#stage-160).
- **Duration and rest:** timed ones wear off, or rest them away.

## Checked in dialogue

- [Talion](../monsters/talion.md) checks whether you do not have this condition.
- [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) checks whether you have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowbless_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `shadowbless_str` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:70` |
    | Defined in | `res/raw/actorconditions_v0611_2.json` |

    Raw data:

    ```json
    {
     "id": "shadowbless_str",
     "iconID": "actorconditions_1:70",
     "name": "Blessing of Shadow strength",
     "category": "spiritual",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
