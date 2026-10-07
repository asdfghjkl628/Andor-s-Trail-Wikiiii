---
description: "Minor weapon feebleness is a harmful mental condition in Andor's Trail: damage −3. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_74.png){ .sprite } Minor weapon feebleness

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_74.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `feebleness_minor` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack damage | −3 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Garnet whisper ring](../items/old_lady_ring.md) | While equipped | 1 | While equipped | – |
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 3 | 6 rounds | 5% |
| [Olwyn's curse](../items/hmr_olwyns.md) | While equipped | 1 | While equipped | – |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Allaceph](../monsters/allaceph_2.md) | When it hits you | 2 | 3 rounds | 20% | waytobrimhavencave1, waytobrimhavencave2 |
| [Ancient allaceph](../monsters/allaceph_6.md) | When it hits you | 3 | 3 rounds | 20% | waytobrimhavencave3, waytobrimhavencave3a, waytobrimhavencave3b |
| [Eliszylae](../monsters/stoutford_lich.md) | When it hits you | 2 | 2 rounds | 15% | Stoutford |
| [Radiant allaceph](../monsters/allaceph_5.md) | When it hits you | 3 | 3 rounds | 20% | waytobrimhavencave3, waytobrimhavencave3a, waytobrimhavencave3b |
| [Radiant guardian](../monsters/toszylae_guard.md) | When it hits you | 2 | 3 rounds | 20% | waytobrimhavencave3a |
| [Rock eater](../monsters/rock_eater.md) | When you hit it | 1 | 1 round | 25% | Mt. Galmore |
| [Strong allaceph](../monsters/allaceph_3.md) | When it hits you | 2 | 3 rounds | 20% | waytobrimhavencave2, waytobrimhavencave3 |
| [Toszylae](../monsters/toszylae.md) | When it hits you | 3 | 3 rounds | 20% | waytobrimhavencave3a |
| [Tough allaceph](../monsters/allaceph_4.md) | When it hits you | 3 | 3 rounds | 20% | waytobrimhavencave2, waytobrimhavencave3 |
| [Vaeregh](../monsters/vaeregh_1.md) | When it hits you | 4 | 3 rounds | 20% | waytobrimhavencave3a, waytobrimhavencave3b |
| [Young allaceph](../monsters/allaceph_1.md) | When it hits you | 2 | 3 rounds | 20% | waytobrimhavencave1, waytobrimhavencave2 |
| [Young rock eater](../monsters/young_rock_eater.md) | When you hit it | 1 | 1 round | 25% | undertell_12, undertell_13, undertell_14 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) ([blackwater_mountain32](../maps/blackwater_mountain32.md)), walking into a blocked passage on [blackwater_mountain32](../maps/blackwater_mountain32.md) | – | 10 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Strong Mind](../skills/resistanceMental.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Restore weapon feebleness](../items/pot_feebleness_restore.md) (when used).
- **Removed by** [Potion of dexterity](../items/pot_dexterity.md) (when used).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier; permanent applications (from equipment or story events) are not removed by resting.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=feebleness_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `feebleness_minor` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:74` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "feebleness_minor",
     "iconID": "actorconditions_1:74",
     "name": "Minor weapon feebleness",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackDamage": {
       "min": -3,
       "max": -3
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
