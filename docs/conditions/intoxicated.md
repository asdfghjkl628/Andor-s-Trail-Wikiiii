---
description: "Intoxicated is a beneficial mental condition in Andor's Trail: max HP +15, attack chance −30, damage +4, attack cost +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_2_1.png){ .sprite } Intoxicated

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_2_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `intoxicated` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | +15 |
| Attack chance | −30 |
| Attack damage | +4 |
| Attack cost (AP) | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Bandit's Brew](../items/sullengrad_bandit_brew.md) | When used | 1 | 3 rounds | 10% |
| [Blackwater brew](../items/bwm_brew.md) | When used | 1 | 10 rounds | 100% |
| [Dark Beer Sour](../items/sullengard_dark_beer_sour.md) | When used | 2 | 5 rounds | 70% |
| [Forest Ale](../items/sullengard_forest_ale.md) | When used | 1 | 3 rounds | 30% |
| [Lowyna's foul brew](../items/drink_lowyn1.md) | When used | 1 | 20 rounds | 100% |
| [Lowyna's foul brew](../items/drink_lowyn1.md) | When used | 3 | 20 rounds | 30% |
| [Lowyna's special brew](../items/drink_lowyn2.md) | When used | 1 | 20 rounds | 100% |
| [Lowyna's special brew](../items/drink_lowyn2.md) | When used | 3 | 20 rounds | 30% |
| [Mountain Top Juice](../items/sullengard_mtn_tj.md) | When used | 1 | 3 rounds | 33% |
| [Southernhaze](../items/sullengrad_southernhaze.md) | When used | 1 | 2 rounds | 40% |
| [Spring Squeeze](../items/sullengard_spring_squeeze.md) | When used | 1 | 4 rounds | 25% |
| [Sullengard's Finest](../items/sullengrad_finest.md) | When used | 1 | 2 rounds | 15% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Strong Mind](../skills/resistanceMental.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=intoxicated.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=intoxicated.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=intoxicated.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `intoxicated` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_2:1` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "intoxicated",
     "iconID": "actorconditions_2:1",
     "name": "Intoxicated",
     "category": "mental",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": -30,
      "increaseAttackDamage": {
       "min": 4,
       "max": 4
      },
      "increaseMaxHP": 15,
      "increaseAttackCost": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
