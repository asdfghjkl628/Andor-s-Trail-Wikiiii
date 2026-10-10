---
description: "Confusion is a harmful mental condition in Andor's Trail: max AP −1, attack chance −10. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_japozero_5.png){ .sprite } Confusion

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_japozero_5.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `confusion` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | −1 |
| Attack chance | −10 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blue rat necklace](../items/ratdom_compass_bwm.md) | While equipped | 1 | While equipped | – |
| [Orange rat necklace](../items/ratdom_compass_tour.md) | While equipped | 1 | While equipped | – |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Ancient kobold](../monsters/kobold3.md) | When it hits you | 1 | 3 rounds | 5% | Guynmart wood 18, Guynmart wood 18b |
| [Ancient kobold](../monsters/kobold3.md) | When it hits you | 1 | 6 rounds | 1% | Guynmart wood 18, Guynmart wood 18b |
| [Kobold](../monsters/kobold2.md) | When it hits you | 1 | 3 rounds | 5% | Guynmart wood 18, Guynmart wood 18b, Guynmart wood 18c |
| [Kobold](../monsters/kobold2.md) | When it hits you | 1 | 6 rounds | 1% | Guynmart wood 18, Guynmart wood 18b, Guynmart wood 18c |
| [Madame Mim](../monsters/swamp_witch.md) | When it hits you | 1 | 2 rounds | 50% | Swamp hut |
| [Quick kobold](../monsters/kobold1.md) | When it hits you | 1 | 3 rounds | 5% | Guynmart wood 18, Guynmart wood 18b, Guynmart wood 18c |
| [Quick kobold](../monsters/kobold1.md) | When it hits you | 1 | 6 rounds | 1% | Guynmart wood 18, Guynmart wood 18b, Guynmart wood 18c |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Ehrenfest](../monsters/ehrenfest.md) ([Blackwater mountain 11](../maps/blackwater_mountain11.md)), [General Ortholion](../monsters/ortholion.md) ([Blackwater mountain 29](../maps/blackwater_mountain29.md)) | [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-21) | 75 rounds |
| [Ehrenfest](../monsters/ehrenfest.md) ([Blackwater mountain 11](../maps/blackwater_mountain11.md)), [General Ortholion](../monsters/ortholion.md) ([Blackwater mountain 29](../maps/blackwater_mountain29.md)) | [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-46) | 15 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Robe of the Sublimate](../items/robe_sublime.md) | On the enemy you hit | 1 | 2 rounds | 20% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Immunity** from [Boletus spelunca](../items/elm_mushroom1.md) (when used; 10 rounds).
- **Immunity** from [Circlet of clarity](../items/circlet_clarity.md) (when you defeat an enemy; 4 rounds).
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=confusion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=confusion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=confusion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `confusion` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_japozero:5` |
    | Defined in | `res/raw/actorconditions_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "confusion",
     "iconID": "actorconditions_japozero:5",
     "name": "Confusion",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseMaxAP": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
