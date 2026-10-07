---
description: "Rootsnare is a harmful physical condition in Andor's Trail: max AP −1, damage resistance +2. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_61.png){ .sprite } Rootsnare

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_61.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `rootsnare` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | −1 |
| Damage resistance | +2 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Bonicksa](../monsters/wicked_witch_first.md) | When it hits you | 1 | 3 rounds | 25% | witch_house |
| [Bonicksa](../monsters/wicked_witch_first.md) | When it hits you | 1 | 3 rounds | 30% | witch_house |
| [Crimoculus Cyclopea creeper](../monsters/agg_cyclopea_creeper.md) | When it hits you | 1 | 4 rounds | 25% | nw_sullengard_1 |
| [Cyclopea creeper](../monsters/cyclopea_creeper.md) | When it hits you | 1 | 4 rounds | 25% | nw_sullengard_1, way_to_sullengard_west_4 |
| [Spiked cyclopea creeper](../monsters/spiked_cyclopea_creeper.md) | When it hits you | 1 | 3 rounds | 20% | way_to_sullengard_west_2, way_to_sullengard_west_4 |
| [Verdant cyclopea creeper](../monsters/verdant_cyclopea_creeper.md) | When it hits you | 1 | 2 rounds | 15% | way_to_sullengard_west_2, way_to_sullengard_west_5 |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Enchanted evergreen rod](../items/witch_scepter.md) | On the enemy you hit | 1 | 3 rounds | 3% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Immunity** from [Hexapede crawler slime](../items/hexapede_crawler_slime.md) (when used; 5 rounds).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rootsnare.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rootsnare.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rootsnare.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `rootsnare` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:61` |
    | Defined in | `res/raw/actorconditions_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "rootsnare",
     "iconID": "actorconditions_1:61",
     "name": "Rootsnare",
     "category": "physical",
     "isStacking": 1,
     "abilityEffect": {
      "increaseMaxAP": -1,
      "increaseDamageResistance": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
