---
description: "Putrefaction is a harmful physical condition in Andor's Trail: max AP −1. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_21.png){ .sprite } Putrefaction

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_21.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `putrefaction` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Angry graveyard corpse](../monsters/graveyard_corpse2.md) | When it hits you | 2 | 3 rounds | 30% | Graveyard 1 |
| [Graveyard corpse](../monsters/graveyard_corpse.md) | When it hits you | 1 | 3 rounds | 25% | Graveyard 1 |
| [Graveyard king](../monsters/graveyardking.md) | When it hits you | 3 | 3 rounds | 50% | Graveyard 1 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [General Ortholion](../monsters/ortholion.md) ([Blackwater mountain 29](../maps/blackwater_mountain29.md)), walking into a blocked passage on [Elm 5f 2](../maps/elm5f_2.md) | [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-39) | 5 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Branch of twilight](../items/branch_of_twilight.md) | On the enemy you hit | 1 | 2 rounds | 3% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Immunity** from [Cave fern](../items/elm_fern.md) (when used; 10 rounds).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=putrefaction.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=putrefaction.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=putrefaction.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `putrefaction` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:21` |
    | Defined in | `res/raw/actorconditions_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "putrefaction",
     "iconID": "actorconditions_1:21",
     "name": "Putrefaction",
     "category": "physical",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "greenSplash"
     },
     "abilityEffect": {
      "increaseMaxHP": 0,
      "increaseMaxAP": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
