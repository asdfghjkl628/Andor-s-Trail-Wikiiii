---
description: "Minor fatigue is a harmful physical condition in Andor's Trail: damage −1, attack cost +2, move cost +2. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_14.png){ .sprite } Minor fatigue

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `fatigue_minor` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack damage | −1 |
| Attack cost (AP) | +2 |
| Move cost (AP) | +2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 1 | 5 rounds | 15% |
| [Lowyna's rat poison](../items/drink_lowyn3.md) | When used | 1 | 5 rounds | 100% |
| [Restore dazed](../items/pot_dazed_restore.md) | When used | 1 | 5 rounds | 25% |
| [Shadowfang](../items/shadowfang.md) | When you hit with it | 1 | 3 rounds | 20% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Cave troll shaman](../monsters/cave_troll_4.md) | When it hits you | 1 | 4 rounds | 10% | Lakecave 0, Lakecave 2 |
| [Guardian of the bridge](../monsters/lbridge.md) | When it hits you | 1 | 7 rounds | 30% | Lodar 8 |
| [Hatchling white wyrm](../monsters/hatchling_white_wyrm.md) | When it hits you | 1 | 5 rounds | 10% | Blackwater Mountain |
| [Morkin elder](../monsters/morkin_cr.md) | When it hits you | 1 | 3 rounds | 30% | Lodar 12 |
| [White wyrm](../monsters/white_wyrm.md) | When it hits you | 1 | 5 rounds | 50% | Blackwater Mountain |
| [Wyrm apprentice](../monsters/wyrm_apprentice.md) | When it hits you | 1 | 10 rounds | 70% | Blackwater Mountain |
| [Wyrm trainer](../monsters/wyrm_trainer.md) | When it hits you | 1 | 10 rounds | 70% | Blackwater Mountain |
| [Young white wyrm](../monsters/young_white_wyrm.md) | When it hits you | 1 | 5 rounds | 20% | Blackwater Mountain |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Gyra](../monsters/stn_gyra.md#v-stn_gyra1) ([Flagstone 0](../maps/flagstone0.md)), [Gyra](../monsters/stn_gyra.md#v-stn_gyra2) ([Flagstone 0](../maps/flagstone0.md)) | [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-29) | 99 rounds |
| stepping on a trigger on [Swamp hut](../maps/swamp_hut.md) | – | 15 rounds |
| [Lytwing](../monsters/lytwing_fallhaven.md) ([Gapfiller 2](../maps/gapfiller2.md)) | [It's knot funny](../quests/fallhaven_lytwings.md#stage-11) | 6 rounds |
| [Lytwing](../monsters/lytwing_fallhaven.md) ([Gapfiller 2](../maps/gapfiller2.md)) | – | 6 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Greataxe of shattered hope](../items/graxe_shatter.md) | On the enemy you hit | 1 | 3 rounds | 20% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Restore fatigue](../items/pot_fatigue_restore.md) (when used).
- **Removed by** [Orchard apple](../items/deebo_apples.md) (when used).
- **Removed by** stepping on a trigger on [Waytogalmore 1](../maps/waytogalmore1.md).
- **Removed by** stepping on a trigger on [Flagstone 0](../maps/flagstone0.md), walking into a blocked passage on [Flagstone 0](../maps/flagstone0.md).
- **Removed by** stepping on a trigger on [Wild 19](../maps/wild19.md) during [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60).
- **Removed by** stepping on a trigger on [Wild 19](../maps/wild19.md).
- **Removed by** stepping on a trigger on [Stoutford castle 1](../maps/stoutford_castle1.md), stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fatigue_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `fatigue_minor` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:14` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "fatigue_minor",
     "iconID": "actorconditions_1:14",
     "name": "Minor fatigue",
     "category": "physical",
     "abilityEffect": {
      "increaseAttackDamage": {
       "min": -1,
       "max": -1
      },
      "increaseMoveCost": 2,
      "increaseAttackCost": 2
     }
    }
    ```


<small>Data from v0.8.18</small>
