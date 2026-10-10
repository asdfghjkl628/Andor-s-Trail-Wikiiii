---
description: "Kazaul possession is a harmful spiritual condition in Andor's Trail: attack chance +10, block chance +10, damage resistance +1, −3 to −2 HP per round. Caused by: items, enemies."
---

# ![](../assets/icons/conditions/actorconditions_1_91.png){ .sprite } Kazaul possession

*Harmful spiritual condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_91.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Spiritual](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | No resistance skill |
| **Condition ID** | `kazarite_misery` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | +10 |
| Block chance | +10 |
| Damage resistance | +1 |
| HP every round | −3 to −2 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Corrupted swamp core](../items/corrupted_swamp_core.md) | When used | 10 | 10 rounds | 100% |
| [Heartfire pendant of Kazaul](../items/heartfire_pendant.md) | While equipped | 1 | While equipped | – |
| [Kazarite cloak](../items/kamelio_drop3.md) | While equipped | 1 | While equipped | – |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | When used | 4 | 4 rounds | 20% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Anoa](../monsters/anoa.md) | When you hit it | 3 | 2 rounds | 50% | Undertell 3 02 |
| [Kazaul crimson arbiter lich](../monsters/kazaul_crimson_arbiter_lich.md) | When you hit it | 1 | 2 rounds | 5% | Undertell 4 00, Undertell 4 01, Undertell 4 10 |
| [Kazaul seer lich](../monsters/kazaul_seer_lich.md) | When you hit it | 1 | 2 rounds | 10% | Undertell 4 01, Undertell 5 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** none; spiritual conditions ignore resistance skills.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Removed by** stepping on a trigger on [Undertell archive 2](../maps/undertell_archive2.md) during [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-78).
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazarite_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazarite_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=kazarite_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `kazarite_misery` |
    | Category (internal) | `spiritual` |
    | Icon | `actorconditions_1:91` |
    | Defined in | `res/raw/actorconditions_omi2.json` |

    Raw data:

    ```json
    {
     "id": "kazarite_misery",
     "iconID": "actorconditions_1:91",
     "name": "Kazaul possession",
     "category": "spiritual",
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -3,
       "max": -2
      }
     },
     "abilityEffect": {
      "increaseAttackChance": 10,
      "increaseBlockChance": 10,
      "increaseDamageResistance": 1
     }
    }
    ```


<small>Data from v0.8.18</small>
