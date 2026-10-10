---
description: "Life drain is a harmful spiritual condition in Andor's Trail: −2 HP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_82.png){ .sprite } Life drain

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_82.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `life_drain` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Luthor's Ring](../items/ring_luthor.md) | While equipped | 5 | While equipped | – |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [Laerothtomb 1](../maps/laerothtomb1.md) | – | 0 rounds |
| [Favlon](../monsters/dds_favlon.md) ([Nw sullengard 1](../maps/nw_sullengard_1.md)) | [Shadows](../quests/shadows.md#stage-140) | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** stepping on a trigger on [Laerothtomb 1](../maps/laerothtomb1.md) during [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70).
- **Removed by** [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) during [Shadows](../quests/shadows.md#stage-160).
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.

## Checked in dialogue

- [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) checks whether you have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=life_drain.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=life_drain.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=life_drain.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `life_drain` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:82` |
    | Defined in | `res/raw/actorconditions_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "life_drain",
     "iconID": "actorconditions_1:82",
     "name": "Life drain",
     "category": "spiritual",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": -2
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
