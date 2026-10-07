---
description: "Concentration is a beneficial mental condition in Andor's Trail: attack chance +10, block chance +10, critical skill +10. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_106.png){ .sprite } Concentration

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_106.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `g03_concentration` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +10 |
| Block chance | +10 |
| Critical skill | +10 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Corrupted swamp core](../items/corrupted_swamp_core.md) | When used | 2 | 8 rounds | 100% |
| [Cursed ring of focus](../items/cursed_ring_focus.md) | While equipped | 1 | While equipped | – |
| [Emberwylde](../items/emberwylde.md) | While equipped | 1 | While equipped | – |
| [Heartsteel claymore](../items/heartstone_2h_sword.md) | When an attack misses you | 1 | 2 rounds | 8% |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Crackshot](../monsters/g03_crackshot.md) | On itself, when you hit it | 1 | 2 rounds | 33% | crackshot_hideout3 |
| [Defy](../monsters/g04_defy.md) | On itself, when you hit it | 1 | 2 rounds | 40% | aidem_base_2 |
| [Thief warden](../monsters/g03_thief_2.md) | On itself, when you hit it | 1 | 2 rounds | 25% | crackshot_hideout3 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Strong Mind](../skills/resistanceMental.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted. Note that resistance also applies to beneficial conditions: it lowers the chance of receiving this one from sources with a chance below 100%.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier; permanent applications (from equipment or story events) are not removed by resting.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=g03_concentration.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=g03_concentration.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=g03_concentration.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `g03_concentration` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:106` |
    | Defined in | `res/raw/actorconditions_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_concentration",
     "iconID": "actorconditions_1:106",
     "name": "Concentration",
     "category": "mental",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 10,
      "increaseBlockChance": 10
     }
    }
    ```


<small>Data from v0.8.18</small>
