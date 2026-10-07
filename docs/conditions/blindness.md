---
description: "Blindness is a harmful physical condition in Andor's Trail: attack chance −5, block chance −5. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_27.png){ .sprite } Blindness

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_27.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `blindness` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −5 |
| Block chance | −5 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Aggressive spitting serpent](../monsters/spit_serpent_3.md) | When it hits you | 3 | 4 rounds | 25% | Lake Laeroth |
| [Eryndor](../monsters/mg_eryndor.md) | When you hit it | 1 | 3 rounds | 80% | mt_galmore0_h1, mt_galmore0_h1_2, mt_galmore_nw_tower_f2 |
| [Spitting serpent](../monsters/spit_serpent_1.md) | When it hits you | 2 | 3 rounds | 15% | Lake Laeroth |
| [Young spitting serpent](../monsters/spit_serpent_2.md) | When it hits you | 1 | 3 rounds | 10% | Lake Laeroth |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Serpent meat](../items/serpent_meat.md) (when used).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blindness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blindness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blindness.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `blindness` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:27` |
    | Defined in | `res/raw/actorconditions_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "blindness",
     "iconID": "actorconditions_1:27",
     "name": "Blindness",
     "category": "physical",
     "isStacking": 1,
     "abilityEffect": {
      "increaseAttackChance": -5,
      "increaseBlockChance": -5
     }
    }
    ```


<small>Data from v0.8.18</small>
