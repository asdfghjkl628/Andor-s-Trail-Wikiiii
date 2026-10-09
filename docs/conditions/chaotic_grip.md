---
description: "Chaotic grip is a harmful mental condition in Andor's Trail: block chance −10, damage resistance −1. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_96.png){ .sprite } Chaotic grip

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_96.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `chaotic_grip` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | −10 |
| Damage resistance | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Iqhan chaos beast](../monsters/iqhan_chb_1a.md) | When it hits you | 5 | 5 rounds | 50% | Pwcave 2a, Pwcave 4 |
| [Iqhan chaos enslaver](../monsters/iqhan_boss.md) | When it hits you | 7 | 5 rounds | 50% | Pwcave 4 |
| [Iqhan chaos evoker](../monsters/iqhan_ch_1a.md) | When it hits you | 2 | 5 rounds | 20% | Pwcave 2, Pwcave 2a, Pwcave 3 |
| [Iqhan chaos master](../monsters/iqhan_ch_3a.md) | When it hits you | 4 | 5 rounds | 50% | Pwcave 2a, Pwcave 3, Pwcave 4 |
| [Iqhan chaos servant](../monsters/iqhan_ch_2a.md) | When it hits you | 4 | 5 rounds | 50% | Pwcave 3, Pwcave 4 |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Branch of twilight](../items/branch_of_twilight.md) | On the enemy you hit | 3 | 2 rounds | 25% |
| [Chaosreaper](../items/chaosreaper.md) | On the enemy you hit | 5 | 3 rounds | 50% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=chaotic_grip.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=chaotic_grip.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=chaotic_grip.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `chaotic_grip` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:96` |
    | Defined in | `res/raw/actorconditions_v0610.json` |

    Raw data:

    ```json
    {
     "id": "chaotic_grip",
     "iconID": "actorconditions_1:96",
     "name": "Chaotic grip",
     "category": "mental",
     "abilityEffect": {
      "increaseBlockChance": -10,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
