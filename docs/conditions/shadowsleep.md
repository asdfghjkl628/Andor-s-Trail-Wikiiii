---
description: "Shadow sleepiness is a harmful mental condition in Andor's Trail: max AP −2. Caused by: enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_28.png){ .sprite } Shadow sleepiness

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_28.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `shadowsleep` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Anoa](../monsters/anoa.md) | When it hits you | 1 | 1 round | 25% | Undertell 3 02 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Jolnor](../monsters/jolnor.md) ([Vilegard chapel](../maps/vilegard_chapel.md)) | [Shadows](../quests/shadows.md#stage-110) | Until you rest |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) during [Shadows](../quests/shadows.md#stage-160).
- **Duration and rest:** timed ones wear off, or rest them away.

## Checked in dialogue

- [Jolnor](../monsters/jolnor.md) ([Vilegard chapel](../maps/vilegard_chapel.md)) checks whether you do not have this condition.
- [Borvis](../monsters/dds_borvis.md) ([Galmore 41](../maps/galmore_41.md)) checks whether you have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowsleep.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowsleep.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadowsleep.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `shadowsleep` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:28` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "shadowsleep",
     "iconID": "actorconditions_1:28",
     "name": "Shadow sleepiness",
     "category": "mental",
     "abilityEffect": {
      "increaseMaxAP": -2
     }
    }
    ```


<small>Data from v0.8.18</small>
