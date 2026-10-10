---
description: "Minor berserker rage is a beneficial mental condition in Andor's Trail: max HP +35, attack chance +60, block chance −90, damage resistance −1. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_90.png){ .sprite } Minor berserker rage

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_90.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `rage_minor` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | +35 |
| Attack chance | +60 |
| Block chance | −90 |
| Damage resistance | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Hunter's Sword](../items/hunters_sword.md) | When you defeat an enemy | 1 | 3 rounds | 10% |
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 2 | 9 rounds | 15% |
| [Potion of blind rage](../items/pot_blind_rage.md) | When used | 1 | 5 rounds | 100% |
| [Specially peppered lamb meat](../items/lamb_meat2.md) | When used | 2 | 11 rounds | 100% |
| [Sword of Shadow's rage](../items/clouded_rage.md) | When you defeat an enemy | 1 | 1 round | 50% |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Arulir Pack Leader](../monsters/arulir_leader.md) | On itself, when it hits you | 1 | 1 round | 50% | Arulircave 6 |
| [Ridgehowler](../monsters/ridgehowler.md) | On itself, when you hit it | 1 | 1 round | 50% | Mt. Galmore |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rage_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rage_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=rage_minor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `rage_minor` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:90` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "rage_minor",
     "iconID": "actorconditions_1:90",
     "name": "Minor berserker rage",
     "category": "mental",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": 60,
      "increaseMaxHP": 35,
      "increaseBlockChance": -90,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
