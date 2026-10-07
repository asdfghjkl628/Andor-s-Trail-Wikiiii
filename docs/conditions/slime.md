---
description: "Corrosive slime is a harmful physical condition in Andor's Trail: −2 to −1 HP per round, −1 AP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_56.png){ .sprite } Corrosive slime

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_56.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `slime` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −2 to −1 |
| AP every round | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Crimson jelly](../monsters/jelly5.md) | When it hits you | 3 | 5 rounds | 40% | roadcave1 |
| [Emerald jelly](../monsters/jelly2.md) | When it hits you | 1 | 4 rounds | 40% | Crossroads Guardhouse |
| [Emerald ooze](../monsters/jelly6.md) | When it hits you | 3 | 5 rounds | 40% | roadcave1 |
| [Ochre jelly](../monsters/jelly4.md) | When it hits you | 2 | 5 rounds | 40% | Crossroads Guardhouse |
| [Olive ooze](../monsters/jelly1.md) | When it hits you | 1 | 3 rounds | 40% | Crossroads Guardhouse |
| [Poisonous ooze](../monsters/jelly3.md) | When it hits you | 1 | 5 rounds | 40% | Crossroads Guardhouse |
| [Slime](../monsters/ratdom_maze_slime.md) | When it hits you | 1 | 2 rounds | 30% | Gold hunter |
| [Spotted tentaslime](../monsters/spotted_tentaslime.md) | When it hits you | 3 | 5 rounds | 40% | gamjee_well_1_1, gamjee_well_2_1, gamjee_well_3_1 |
| [ViridToxin dartmaw](../monsters/virid_toxin.md) | When it hits you | 4 | 5 rounds | 60% | Flagstone Prison |
| [Young ViridToxin dartmaw](../monsters/young_virid_toxin.md) | When it hits you | 4 | 5 rounds | 50% | Flagstone Prison |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Vaelric's purging wash](../items/vaelric_purging_wash.md) (when used).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=slime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `slime` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:56` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "slime",
     "iconID": "actorconditions_1:56",
     "name": "Corrosive slime",
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
     }
    }
    ```


<small>Data from v0.8.18</small>
