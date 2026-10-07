---
description: "Drowning is a harmful physical condition in Andor's Trail: −80 to −40 HP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_68.png){ .sprite } Drowning

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_68.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `drowning` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −80 to −40 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), stepping on a trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md) | – | 990 rounds |
| stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – | 990 rounds |
| stepping on a trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md) | – | 990 rounds |
| stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md) | [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-31) | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), stepping on a trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md).
- **Removed by** stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md) during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-32).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=drowning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=drowning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=drowning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `drowning` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:68` |
    | Defined in | `res/raw/actorconditions_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "drowning",
     "iconID": "actorconditions_1:68",
     "name": "Drowning",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -80,
       "max": -40
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
