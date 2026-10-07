---
description: "Courage is a beneficial mental condition in Andor's Trail: attack chance +3, damage +2, block chance +3, +1 HP per round. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_92.png){ .sprite } Courage

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_92.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `courage` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +3 |
| Attack damage | +2 |
| Block chance | +3 |
| HP every round | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Elythara's ring](../items/elythara_ring_upgraded.md) | When an attack misses you | 1 | 2 rounds | 25% |
| [Elythara's ring](../items/elythara_ring_upgraded.md) | When you defeat an enemy | 1 | 2 rounds | 35% |
| [Hat of the protector](../items/hat_of_protector.md) | When you defeat an enemy | 1 | 3 rounds | 10% |
| [Klingenlied](../items/klingenlied.md) | When you defeat an enemy | 1 | 2 rounds | 5% |
| [Liquid courage](../items/pot_courage.md) | When used | 2 | 5 rounds | 100% |
| [Shield of the Brave](../items/shield_of_brave.md) | When you defeat an enemy | 1 | 3 rounds | 20% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=courage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=courage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=courage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `courage` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:92` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "courage",
     "iconID": "actorconditions_1:92",
     "name": "Courage",
     "category": "mental",
     "isPositive": 1,
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     },
     "abilityEffect": {
      "increaseAttackChance": 3,
      "increaseAttackDamage": {
       "min": 2,
       "max": 2
      },
      "increaseBlockChance": 3
     }
    }
    ```


<small>Data from v0.8.18</small>
