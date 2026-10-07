---
description: "Haste is a beneficial physical condition in Andor's Trail: max AP +2, move cost −1, item use cost −2, re-equip cost −2. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_87.png){ .sprite } Haste

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_87.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `haste` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max AP | +2 |
| Move cost (AP) | −1 |
| Use item cost (AP) | −2 |
| Re-equip cost (AP) | −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Feydelight](../items/feydelight.md) | When used | 1 | 15 rounds | 100% |
| [Potion of haste](../items/pot_haste.md) | When used | 1 | 11 rounds | 100% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Philippa](../monsters/village_philippa.md) ([Wexlow village south-east house](../maps/wexlow_village_se_house.md)) | – | 2 rounds |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Strong mountain wolf](../monsters/mwolf_7.md) | On itself, when it hits you | 1 | 2 rounds | 15% | – |
| [Trained mountain wolf](../monsters/mountain_wolf_2.md) | On itself, when it hits you | 1 | 2 rounds | 20% | Blackwater Mountain |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** timed ones wear off, or rest them away.

## Checked in dialogue

- stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md), stepping on a trigger on [Guynmart wood 18b](../maps/guynmart_wood_18b.md) checks whether you do not have this condition.
- stepping on a trigger on [Guynmart wood 18c](../maps/guynmart_wood_18c.md) checks whether you do not have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=haste.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=haste.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=haste.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `haste` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:87` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "haste",
     "iconID": "actorconditions_1:87",
     "name": "Haste",
     "category": "physical",
     "isPositive": 1,
     "abilityEffect": {
      "increaseMaxAP": 2,
      "increaseMoveCost": -1,
      "increaseUseItemCost": -2,
      "increaseReequipCost": -2
     }
    }
    ```


<small>Data from v0.8.18</small>
