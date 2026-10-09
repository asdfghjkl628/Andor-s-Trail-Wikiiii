---
description: "Pull of the mark is a harmful spiritual condition in Andor's Trail: attack cost +1, move cost +1. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_newb_1.png){ .sprite } Pull of the mark

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_newb_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `pull_of_the_mark` |

</div>

> You feel an inexplicable pull toward something familiar, as if a piece of you is tethered to a distant past. An echo of guidance whispers faintly in your mind, urging you to seek clarity from those who once knew you best.

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack cost (AP) | +1 |
| Move cost (AP) | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Galmore 32](../maps/galmore_32.md) | [A familiar shadow](../quests/familiar_shadow.md#stage-10) | Permanent |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** stepping on a trigger on [Galmore 32](../maps/galmore_32.md) during [A familiar shadow](../quests/familiar_shadow.md#stage-60).
- **Duration and rest:** permanent ones (equipment, story events) stay through rest.

## Checked in dialogue

- stepping on a trigger on [Galmore 10](../maps/galmore_10.md), stepping on a trigger on [Galmore 12a](../maps/galmore_12a.md) ([Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-1)) checks whether you have this condition.
- stepping on a trigger on [Galmore 10](../maps/galmore_10.md), stepping on a trigger on [Galmore 12a](../maps/galmore_12a.md) ([Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-2)) checks whether you have this condition.
- stepping on a trigger on [Galmore 10](../maps/galmore_10.md), stepping on a trigger on [Galmore 12a](../maps/galmore_12a.md) checks whether you have this condition.
- walking into a blocked passage on [Crossglen](../maps/crossglen.md) ([Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-1)) checks whether you have this condition.
- walking into a blocked passage on [Crossglen](../maps/crossglen.md) ([Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-2)) checks whether you have this condition.
- walking into a blocked passage on [Crossglen](../maps/crossglen.md) checks whether you have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=pull_of_the_mark.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=pull_of_the_mark.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=pull_of_the_mark.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `pull_of_the_mark` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_newb:1` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "pull_of_the_mark",
     "iconID": "actorconditions_newb:1",
     "name": "Pull of the mark",
     "description": "You feel an inexplicable pull toward something familiar, as if a piece of you is tethered to a distant past. An echo of guidance whispers faintly in your mind, urging you to seek clarity from those who once knew you best.",
     "category": "spiritual",
     "abilityEffect": {
      "increaseMoveCost": 1,
      "increaseAttackCost": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
