---
description: "Bone fracture is a harmful physical condition in Andor's Trail: −20 HP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_2_0.png){ .sprite } Bone fracture

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_2_0.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `bone_fracture` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −20 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [Guynmart](../maps/guynmart.md) | [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-71) | 1 round |
| stepping on a trigger on [Guynmart wood 3](../maps/guynmart_wood_3.md) | [Guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-2) | 1 round |
| walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) | [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-1) | 1 round |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bone_fracture.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bone_fracture.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bone_fracture.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `bone_fracture` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_2:0` |
    | Defined in | `res/raw/actorconditions_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "bone_fracture",
     "iconID": "actorconditions_2:0",
     "name": "Bone fracture",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -20,
       "max": -20
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
