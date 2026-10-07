---
description: "Kazaul rotworms is a harmful physical condition in Andor's Trail: max HP −15, max AP −3, damage resistance −1. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_82.png){ .sprite } Kazaul rotworms

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_82.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `rotworm` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | −15 |
| Max AP | −3 |
| Damage resistance | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | [I have it in me](../quests/maggots.md#stage-10) | Permanent |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** [Talion](../monsters/talion.md) during [I have it in me](../quests/maggots.md#stage-50).
- **Duration and rest:** permanent applications (from equipment or story events) are not removed by resting.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rotworm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rotworm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rotworm.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `rotworm` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:82` |
    | Defined in | `res/raw/actorconditions_v0611_2.json` |

    Raw data:

    ```json
    {
     "id": "rotworm",
     "iconID": "actorconditions_1:82",
     "name": "Kazaul rotworms",
     "category": "physical",
     "abilityEffect": {
      "increaseMaxHP": -15,
      "increaseMaxAP": -3,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
