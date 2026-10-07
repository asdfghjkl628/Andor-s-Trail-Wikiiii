---
description: "Kazaul exposure is a harmful spiritual condition in Andor's Trail: damage resistance −3. Caused by: enemies."
---

# ![](../assets/icons/conditions/actorconditions_japozero_58.png){ .sprite } Kazaul exposure

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_58.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `kazaul_exposure` |

</div>

> Defensive structure is methodically compromised, reducing resistance to damage.

## Effects

| Effect | Per magnitude level |
|---|---|
| Damage resistance | −3 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Bone-Marshal lich](../monsters/bone_marshal_lich.md) | When it hits you | 1 | 2 rounds | 25% | Undertell 11, Undertell 12, Undertell 21 |
| [Dreadstaff lich](../monsters/dreadblade.md) | When it hits you | 2 | 3 rounds | 18% | Undertell 3 lava 10, Undertell 3 lava 11, Undertell 4 11 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** none; spiritual conditions ignore resistance skills.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_exposure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_exposure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazaul_exposure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `kazaul_exposure` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_japozero:58` |
    | Defined in | `res/raw/actorconditions_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_exposure",
     "iconID": "actorconditions_japozero:58",
     "name": "Kazaul exposure",
     "description": "Defensive structure is methodically compromised, reducing resistance to damage.",
     "category": "spiritual",
     "abilityEffect": {
      "increaseDamageResistance": -3
     }
    }
    ```


<small>Data from v0.8.18</small>
