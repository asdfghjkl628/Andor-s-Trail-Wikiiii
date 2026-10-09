---
description: "Ablaze is a harmful physical condition in Andor's Trail: attack chance −15, −1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_1.png){ .sprite } Ablaze

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `fire` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −15 |
| HP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Stuffed pepper](../items/brightport_red.md) | When used | 1 | 2 rounds | 30% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Ancient walking inferno](../monsters/fire9.md) | When it hits you | 3 | 5 rounds | 20% | Lostmine 11 |
| [Blazing abcess](../monsters/fire2.md) | When it hits you | 5 | 4 rounds | 20% | Lostmine 6, Lostmine 7, Lostmine 8 |
| [Embergeist](../monsters/embergeist.md) | When you hit it | 2 | 5 rounds | 90% | Mt. Galmore |
| [Flame spawn](../monsters/fire6.md) | When it hits you | 2 | 5 rounds | 10% | Lostmine 10, Lostmine 9 |
| [Glowing abcess](../monsters/fire1.md) | When it hits you | 5 | 3 rounds | 20% | Lostmine 6, Lostmine 7, Lostmine 8 |
| [Glowing flame](../monsters/fire5.md) | When it hits you | 1 | 5 rounds | 20% | Lostmine 10, Lostmine 9 |
| [Lava spawn](../monsters/fire3.md) | When it hits you | 1 | 4 rounds | 10% | Lostmine 7, Lostmine 8, Lostmine 9 |
| [Pyreling behemoth](../monsters/Pyreling_behemoth.md) | When you hit it | 2 | 4 rounds | 75% | Galmore 71 |
| [Spitfire bug](../monsters/spitfire_bug.md) | When it hits you | 2 | 4 rounds | 50% | Mt. Galmore |
| [Thukuzun](../monsters/thukuzun.md) | When it hits you | 3 | 7 rounds | 30% | Lostmine 11 |
| [Tough lava spawn](../monsters/fire4.md) | When it hits you | 1 | 5 rounds | 10% | Lostmine 7, Lostmine 8, Lostmine 9 |
| [Walking flame](../monsters/fire7.md) | When it hits you | 2 | 5 rounds | 20% | Lostmine 10, Lostmine 11 |
| [Walking inferno](../monsters/fire8.md) | When it hits you | 3 | 5 rounds | 20% | Lostmine 10, Lostmine 11 |
| [Young spitfire bug](../monsters/young_spitfire_bug.md) | When it hits you | 2 | 4 rounds | 50% | Mt. Galmore |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [Arulircave 6](../maps/arulircave6.md) | – | 1 round |
| stepping on a trigger on [Arulircave 6](../maps/arulircave6.md) | – | 2 rounds |
| [Flaming orb](../monsters/ratdom_maze_boulder1.md) ([Ratdom maze 551](../maps/ratdom_maze_551.md)), [Flaming orb](../monsters/ratdom_maze_boulder1.md#v-ratdom_maze_boulder2) ([Ratdom maze 551](../maps/ratdom_maze_551.md)) | – | 3 rounds |
| stepping on a trigger on [Mountainlake 8 cave](../maps/mountainlake8_cave.md) | – | 3 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blazebite](../items/blazebite.md) | On the enemy you hit | 2 | 4 rounds | 15% |
| [Emberwylde](../items/emberwylde.md) | On the enemy that hits you | 2 | 2 rounds | 8% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Immunity** from [Iced leather armor](../items/armor5.md) (while equipped; while equipped).
- **Immunity** from [Heartfire pendant of Kazaul](../items/heartfire_pendant.md) (while equipped; while equipped).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fire.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `fire` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:1` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "fire",
     "iconID": "actorconditions_1:1",
     "name": "Ablaze",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     },
     "abilityEffect": {
      "increaseAttackChance": -15
     }
    }
    ```


<small>Data from v0.8.18</small>
