---
description: "Blistering skin is a harmful blood condition in Andor's Trail: −1 HP per round. Caused by: enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_15.png){ .sprite } Blistering skin

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_15.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `blister` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Black plaguecrawler](../monsters/plaguesp_4.md) | When it hits you | 3 | 5 rounds | 20% | mountainlake0, waytolake0, waytolake1 |
| [Hardshell plaguestrider](../monsters/plaguesp_6.md) | When it hits you | 4 | 5 rounds | 20% | mountainlake0, waytolake0, waytolake1 |
| [Nesting plaguestrider](../monsters/plaguesp_11.md) | When it hits you | 5 | 5 rounds | 50% | waytolake4, waytolake5 |
| [Plaguecrawler](../monsters/plaguesp_2.md) | When it hits you | 2 | 5 rounds | 20% | waytolake0, waytolake1, waytolake2 |
| [Plaguestrider](../monsters/plaguesp_5.md) | When it hits you | 3 | 5 rounds | 20% | mountainlake0, waytolake0, waytolake1 |
| [Plaguestrider master](../monsters/plaguesp_13.md) | When it hits you | 6 | 5 rounds | 50% | waytolake5 |
| [Plaguestrider master](../monsters/plaguesp_13.md) | When it hits you | 3 | 5 rounds | 50% | waytolake5 |
| [Plaguestrider servant](../monsters/plaguesp_12.md) | When it hits you | 6 | 5 rounds | 50% | waytolake4, waytolake5 |
| [Poisonous vine](../monsters/poison_vine_top.md) | When it hits you | 3 | 4 rounds | 80% | island_underground2, island_underground3, laerothcave0 |
| [Puny plaguecrawler](../monsters/plaguesp_1.md) | When it hits you | 1 | 5 rounds | 20% | waytolake0, waytolake1, waytolake2 |
| [Tough plaguecrawler](../monsters/plaguesp_3.md) | When it hits you | 2 | 5 rounds | 20% | waytolake0, waytolake1, waytolake2 |
| [Tough plaguestrider](../monsters/plaguesp_7.md) | When it hits you | 4 | 5 rounds | 20% | mountainlake0, waytolake11, waytolake12 |
| [Tough wooly plaguestrider](../monsters/plaguesp_9.md) | When it hits you | 5 | 5 rounds | 50% | mountainlake0, waytolake11, waytolake12 |
| [Vile plaguestrider](../monsters/plaguesp_10.md) | When it hits you | 5 | 5 rounds | 50% | waytolake4, waytolake5 |
| [Wooly plaguestrider](../monsters/plaguesp_8.md) | When it hits you | 5 | 5 rounds | 50% | mountainlake0, waytolake11, waytolake12 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [remgard_church_basement](../maps/remgard_church_basement.md) | – | 5 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Pure Blood](../skills/resistanceBlood.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blister.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blister.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blister.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `blister` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:15` |
    | Defined in | `res/raw/actorconditions_v0611.json` |

    Raw data:

    ```json
    {
     "id": "blister",
     "iconID": "actorconditions_1:15",
     "name": "Blistering skin",
     "category": "blood",
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
