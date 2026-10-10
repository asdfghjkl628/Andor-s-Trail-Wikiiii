---
description: "Elythara's refreshment is a beneficial spiritual condition in Andor's Trail: +1 HP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_35.png){ .sprite } Elythara's refreshment

*Beneficial spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_35.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `elytharabless_heal` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Elythara's ring](../items/elythara_ring_upgraded.md) | While equipped | 1 | While equipped | – |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) | – | 101 rounds |
| walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) | – | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-1).
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=elytharabless_heal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=elytharabless_heal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=elytharabless_heal.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `elytharabless_heal` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:35` |
    | Defined in | `res/raw/actorconditions_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "elytharabless_heal",
     "iconID": "actorconditions_1:35",
     "name": "Elythara's refreshment",
     "category": "spiritual",
     "isPositive": 1,
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
