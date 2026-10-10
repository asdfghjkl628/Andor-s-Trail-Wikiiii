---
description: "Mind fog is a harmful mental condition in Andor's Trail: attack chance −10, block chance −10. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_81.png){ .sprite } Mind fog

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_81.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `mind_fog` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −10 |
| Block chance | −10 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Helm of Foreseeing](../items/Helm_foreseeing.md) | When you defeat an enemy | 2 | 5 rounds | 4% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Dense foggerlump](../monsters/feygard_fogmonster5.md) | When it hits you | 2 | 3 rounds | 50% | Swamp 6 |
| [Dizzy foggerlump](../monsters/feygard_fogmonster4.md) | When it hits you | 2 | 3 rounds | 50% | Swamp 5 |
| [Icy foggerlump](../monsters/feygard_fogmonster2.md) | When it hits you | 2 | 3 rounds | 50% | Swamp 2 |
| [Kazaul seer lich](../monsters/kazaul_seer_lich.md) | When it hits you | 1 | 2 rounds | 18% | Undertell 4 01, Undertell 5 |
| [Mindless disgrace](../monsters/mindless_disgrace.md) | When you hit it | 3 | 4 rounds | 25% | Haunted house, Haunted house basement, Haunted underground 1 |
| [Shiny Foggerlump](../monsters/feygard_fogmonster9.md) | When it hits you | 2 | 3 rounds | 50% | Guynmart Castle |
| [Wet foggerlump](../monsters/feygard_fogmonster3.md) | When it hits you | 2 | 3 rounds | 50% | Swamp 4 |
| [Wobbling foggerlump](../monsters/feygard_fogmonster1.md) | When it hits you | 2 | 3 rounds | 50% | Guynmart Castle |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Quarterstaff](../items/swampwitch_staff.md) | On the enemy you hit | 2 | 4 rounds | 33% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Immunity** from [Circlet of clarity](../items/circlet_clarity.md) (when you are hit; 2 rounds).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mind_fog.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mind_fog.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=mind_fog.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `mind_fog` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:81` |
    | Defined in | `res/raw/actorconditions_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "mind_fog",
     "iconID": "actorconditions_1:81",
     "name": "Mind fog",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseBlockChance": -10
     }
    }
    ```


<small>Data from v0.8.18</small>
