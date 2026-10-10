---
description: "Deathtouch is a harmful spiritual condition in Andor's Trail: attack chance −5, damage resistance −1, −1 to 0 HP per round. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_29.png){ .sprite } Deathtouch

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_29.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | Yes |
| **Resisted by** | No resistance skill |
| **Condition ID** | `deathtouch` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −5 |
| Damage resistance | −1 |
| HP every round | −1 to 0 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** Yes (same duration → magnitudes add up).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Evil shade](../monsters/evil_shade.md) | When it hits you | 1 | 2 rounds | 25% | Undertell 3 02 |
| [Forsaken shade](../monsters/shade1.md) | When it hits you | 1 | 3 rounds | 50% | Undertell 3 02 |
| [Saki](../monsters/saki.md) | When it hits you | 1 | 3 rounds | 50% | Mt. Galmore |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** none; spiritual conditions ignore resistance skills.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=deathtouch.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=deathtouch.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=deathtouch.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `deathtouch` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:29` |
    | Defined in | `res/raw/actorconditions_undertell.json` |

    Raw data:

    ```json
    {
     "id": "deathtouch",
     "iconID": "actorconditions_1:29",
     "name": "Deathtouch",
     "category": "spiritual",
     "isStacking": 1,
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": 0
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -5,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
