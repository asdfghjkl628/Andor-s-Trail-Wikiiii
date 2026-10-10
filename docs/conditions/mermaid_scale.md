---
description: "Mermaid curse is a harmful spiritual condition in Andor's Trail: max HP −15, max AP −3, attack chance −20, block chance −10, damage resistance −1, −1 to 0 HP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_22.png){ .sprite } Mermaid curse

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_22.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `mermaid_scale` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | −15 |
| Max AP | −3 |
| Attack chance | −20 |
| Block chance | −10 |
| Damage resistance | −1 |
| HP every round | −1 to 0 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Tjure](../monsters/tjure.md) ([Blackwater mountain 54](../maps/blackwater_mountain54.md)) | [The silver scale](../quests/mermaid_scale.md#stage-100) | Permanent |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Removed by** stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md) during [The silver scale](../quests/mermaid_scale.md#stage-200).
- **Duration and rest:** permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mermaid_scale.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mermaid_scale.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mermaid_scale.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `mermaid_scale` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:22` |
    | Defined in | `res/raw/actorconditions_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "mermaid_scale",
     "iconID": "actorconditions_1:22",
     "name": "Mermaid curse",
     "category": "spiritual",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": 0
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -20,
      "increaseMaxHP": -15,
      "increaseMaxAP": -3,
      "increaseBlockChance": -10,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
