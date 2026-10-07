---
description: "Kazaul mortality is a harmful spiritual condition in Andor's Trail: −50 to 0 HP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_japozero_1.png){ .sprite } Kazaul mortality

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `kazaul_mortality` |

</div>

> A severing influence that withdraws the Kazaul gaze, returning the body to its natural and fragile state.

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −50 to 0 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [undertell_4_00](../maps/undertell_4_00.md), [Kha'zaan Porter](../monsters/porter.md) ([undertell_4_00](../maps/undertell_4_00.md)) | – | 1 round |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) during [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-78).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_mortality.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_mortality.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_mortality.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `kazaul_mortality` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_japozero:1` |
    | Defined in | `res/raw/actorconditions_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_mortality",
     "iconID": "actorconditions_japozero:1",
     "name": "Kazaul mortality",
     "description": "A severing influence that withdraws the Kazaul gaze, returning the body to its natural and fragile state.",
     "category": "spiritual",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -50,
       "max": 0
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
