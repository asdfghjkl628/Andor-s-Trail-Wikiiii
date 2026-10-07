---
description: "Shadow's protection is a beneficial spiritual condition in Andor's Trail: block chance +10, damage resistance +2, +1 HP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_28.png){ .sprite } Shadow's protection

*Beneficial spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_28.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `shadow_prot` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | +10 |
| Damage resistance | +2 |
| HP every round | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blade of the protector](../items/blade_protector.md) | When you are hit | 2 | 2 rounds | 15% |
| [Tears of the Shadow](../items/pot_shadowtear.md) | When used | 2 | 20 rounds | 100% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Elm mine 3](../maps/elm_mine3.md) | [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-24) | 10 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** none; spiritual conditions ignore resistance skills.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadow_prot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadow_prot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=shadow_prot.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `shadow_prot` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:28` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "shadow_prot",
     "iconID": "actorconditions_1:28",
     "name": "Shadow's protection",
     "category": "spiritual",
     "isPositive": 1,
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     },
     "abilityEffect": {
      "increaseBlockChance": 10,
      "increaseDamageResistance": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
