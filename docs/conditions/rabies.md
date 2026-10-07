---
description: "Rabies is a harmful physical condition in Andor's Trail: attack chance −25, block chance −10, −5 to −3 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_35.png){ .sprite } Rabies

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `rabies` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −25 |
| Block chance | −10 |
| HP every round | −5 to −3 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Agile aroughcun](../monsters/aroughcun_agile.md) | When it hits you | 2 | 2 rounds | 25% | Mt. Galmore |
| [Aroughcun](../monsters/aroughcun.md) | When it hits you | 2 | 2 rounds | 30% | Mt. Galmore |
| [Gravewing](../monsters/undertell_bat.md) | When it hits you | 1 | 3 rounds | 15% | undertell_03, undertell_04, undertell_05 |
| [Nightfur rat](../monsters/nightfur_rat.md) | When it hits you | 1 | 5 rounds | 25% | witch_house_basement |
| [Ny'Ratees](../monsters/nyratees.md) | When it hits you | 1 | 8 rounds | 25% | undertell_1_0, undertell_1_1 |
| [Scardy aroughcun](../monsters/scardy_aroughcun.md) | When it hits you | 2 | 2 rounds | 25% | Mt. Galmore |
| [Sow aroughcun](../monsters/aroughcun_sow.md) | When it hits you | 2 | 2 rounds | 30% | Mt. Galmore |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rabies.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rabies.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rabies.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `rabies` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_japozero:35` |
    | Defined in | `res/raw/actorconditions_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "rabies",
     "iconID": "actorconditions_japozero:35",
     "name": "Rabies",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -5,
       "max": -3
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -25,
      "increaseBlockChance": -10
     }
    }
    ```


<small>Data from v0.8.18</small>
