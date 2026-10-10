---
description: "Bless is a beneficial spiritual condition in Andor's Trail: attack chance +5. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_41.png){ .sprite } Bless

*Beneficial spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_41.png" alt=""></p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | No resistance skill |
| **Condition ID** | `bless` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +5 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Elythara's ring](../items/elythara_ring.md) | While equipped | 1 | While equipped | – |
| [Elythara's ring](../items/elythara_ring_upgraded.md) | While equipped | 1 | While equipped | – |
| [Elytharan gloves](../items/elytharan_gloves.md) | While equipped | 1 | While equipped | – |
| [Elytharan redeemer](../items/elytharan_redeemer.md) | While equipped | 1 | While equipped | – |
| [Elytharan tabi](../items/elytharan_tabi.md) | While equipped | 1 | While equipped | – |
| [Enchanted evergreen rod](../items/witch_scepter.md) | While equipped | 2 | While equipped | – |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bless.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bless.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bless.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `bless` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:41` |
    | Defined in | `res/raw/actorconditions_v069.json` |

    Raw data:

    ```json
    {
     "id": "bless",
     "iconID": "actorconditions_1:41",
     "name": "Bless",
     "category": "spiritual",
     "isPositive": 1,
     "isStacking": 1,
     "abilityEffect": {
      "increaseAttackChance": 5
     }
    }
    ```


<small>Data from v0.8.18</small>
