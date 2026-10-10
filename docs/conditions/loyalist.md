---
description: "Feygard Loyalist is a beneficial mental condition in Andor's Trail: max HP −25, attack chance +7, damage +1, block chance +5, damage resistance +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_japozero_11.png){ .sprite } Feygard Loyalist

*Beneficial mental condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_japozero_11.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `loyalist` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Max HP | −25 |
| Attack chance | +7 |
| Attack damage | +1 |
| Block chance | +5 |
| Damage resistance | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Feygard's might](../items/feygard_might.md) | While equipped | 1 | While equipped | – |
| [Godwin's ring](../items/godwin_ring.md) | While equipped | 1 | While equipped | – |
| [Necklace of Feygard's Glory](../items/feygard_necklace.md) | While equipped | 1 | While equipped | – |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=loyalist.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=loyalist.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=loyalist.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `loyalist` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_japozero:11` |
    | Defined in | `res/raw/actorconditions_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "loyalist",
     "iconID": "actorconditions_japozero:11",
     "name": "Feygard Loyalist",
     "category": "mental",
     "isPositive": 1,
     "abilityEffect": {
      "increaseAttackChance": 7,
      "increaseAttackDamage": {
       "min": 1,
       "max": 1
      },
      "increaseMaxHP": -25,
      "increaseBlockChance": 5,
      "increaseDamageResistance": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
