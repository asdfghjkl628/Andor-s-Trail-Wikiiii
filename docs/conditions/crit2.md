---
description: "Fracture is a harmful physical condition in Andor's Trail: block chance −50, damage resistance −2. Caused by: items, dialogue and events, skills."
---

# ![](../assets/icons/conditions/actorconditions_1_89.png){ .sprite } Fracture

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_89.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `crit2` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | −50 |
| Damage resistance | −2 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 3 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 4 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 5 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 6 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 8 rounds |
| walking into a blocked passage on [galmore_47](../maps/galmore_47.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-14) | 10 rounds |
| walking into a blocked passage on [galmore_24](../maps/galmore_24.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-24) | 10 rounds |
| walking into a blocked passage on [galmore_33](../maps/galmore_33.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-50) | 15 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Cragbreaker](../items/cragbreaker.md) | On the enemy you hit | 1 | 3 rounds | 3% |
| [Heartsteel doomhammer](../items/heartsteel_2h_hammer.md) | On the enemy you hit | 1 | 3 rounds | 5% |
| [Heartsteel mace](../items/heartstone_mace.md) | On the enemy you hit | 1 | 3 rounds | 5% |

**Skills**

| Skill | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Fracture](../skills/crit2.md) | On a critical hit | 1 | 5 rounds | 50% per skill level |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Immunity** from [Spiritbane potion](../items/spiritbane_potion.md) (when used; 6 rounds).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=crit2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=crit2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=crit2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `crit2` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:89` |
    | Defined in | `res/raw/actorconditions_v0611_2.json` |

    Raw data:

    ```json
    {
     "id": "crit2",
     "iconID": "actorconditions_1:89",
     "name": "Fracture",
     "category": "physical",
     "isStacking": 1,
     "abilityEffect": {
      "increaseBlockChance": -50,
      "increaseDamageResistance": -2
     }
    }
    ```


<small>Data from v0.8.18</small>
