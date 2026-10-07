---
description: "Burning is a harmful physical condition in Andor's Trail: attack chance −5, block chance −5, −2 to −1 HP per round, −1 AP per round. Caused by: dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_2.png){ .sprite } Burning

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `burning` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −5 |
| Block chance | −5 |
| HP every round | −2 to −1 |
| AP every round | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [galmore_32](../maps/galmore_32.md), stepping on a trigger on [galmore_33](../maps/galmore_33.md) | – | 1 round |
| stepping on a trigger on [undertell_00](../maps/undertell_00.md), stepping on a trigger on [undertell_01](../maps/undertell_01.md) | – | 3 rounds |
| stepping on a trigger on [undertell_00](../maps/undertell_00.md), stepping on a trigger on [undertell_01](../maps/undertell_01.md) | – | 4 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) during [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-78).
- **Immunity** from [Heartfire pendant of Kazaul](../items/heartfire_pendant.md) (while equipped; while equipped).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=burning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=burning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=burning.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `burning` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:2` |
    | Defined in | `res/raw/actorconditions_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "burning",
     "iconID": "actorconditions_1:2",
     "name": "Burning",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -2,
       "max": -1
      },
      "increaseCurrentAP": {
       "min": -1,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -5,
      "increaseBlockChance": -5
     }
    }
    ```


<small>Data from v0.8.18</small>
