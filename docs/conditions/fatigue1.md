---
description: "Fatigue is a harmful physical condition in Andor's Trail: −1 HP per round, −1 AP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_89.png){ .sprite } Fatigue

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_89.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `fatigue1` |

</div>

!!! note "Other conditions named Fatigue"
    The game data defines 4 separate conditions with this name, each with its own effects: [`fatigue2`](fatigue2.md), [`fatigue3`](fatigue3.md), [`fatigue4`](fatigue4.md).

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −1 |
| AP every round | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | – | 99 rounds |
| walking into a blocked passage on [brimhaven1](../maps/brimhaven1.md) | – | 99 rounds |
| [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) | [Shadows](../quests/shadows.md#stage-140) | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** stepping on a trigger on [brimhaven1](../maps/brimhaven1.md).
- **Removed by** [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) during [Shadows](../quests/shadows.md#stage-160).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.

## Checked in dialogue

- stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) checks whether you have this condition.
- stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) checks whether you do not have this condition.
- [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) checks whether you have this condition.
- [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) checks whether you do not have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `fatigue1` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:89` |
    | Defined in | `res/raw/actorconditions_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "fatigue1",
     "iconID": "actorconditions_1:89",
     "name": "Fatigue",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      },
      "increaseCurrentAP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
