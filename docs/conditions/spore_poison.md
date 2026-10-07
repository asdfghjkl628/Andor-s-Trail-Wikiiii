---
description: "Spore poisoning is a harmful blood condition in Andor's Trail: attack chance −10, move cost +1, item use cost +1, re-equip cost +2. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_61.png){ .sprite } Spore poisoning

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_61.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `spore_poison` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −10 |
| Move cost (AP) | +1 |
| Use item cost (AP) | +1 |
| Re-equip cost (AP) | +2 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Angry dangerous fungi](../monsters/dangerous_fungi_1.md) | When it hits you | 1 | 3 rounds | 10% | mushroom_m3_2 |
| [Angry fungi](../monsters/mid_fungi_1.md) | When it hits you | 1 | 2 rounds | 10% | mushroom_m3_2 |
| [Dangerous fungi](../monsters/dangerous_fungi.md) | When it hits you | 1 | 3 rounds | 10% | bogsten3, bogsten4, mushroom_m2_1 |
| [Fungi](../monsters/mid_fungi.md) | When it hits you | 1 | 2 rounds | 10% | bogsten2, bogsten3, bogsten4 |
| [Great fungi](../monsters/boss_fungi.md) | When it hits you | 2 | 5 rounds | 20% | mushroom_m3_2 |
| [Mushroom guardian](../monsters/guardian_mushroom.md) | When it hits you | 2 | 5 rounds | 20% | Flagstone Prison |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Pure Blood](../skills/resistanceBlood.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Spore poison immunity](../skills/sporeImmunity.md)** prevents this condition entirely (unless the chance is 100%).
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Zuul'khan](../monsters/zuul_khan.md) ([bogsten4](../maps/bogsten4.md)) during [Fungi panic](../quests/fungi_panic.md#stage-155).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spore_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spore_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=spore_poison.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `spore_poison` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:61` |
    | Defined in | `res/raw/actorconditions_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "spore_poison",
     "iconID": "actorconditions_1:61",
     "name": "Spore poisoning",
     "category": "blood",
     "isStacking": 1,
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseMoveCost": 1,
      "increaseUseItemCost": 1,
      "increaseReequipCost": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
