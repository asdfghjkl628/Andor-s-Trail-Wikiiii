---
description: "Concussion is a harmful physical condition in Andor's Trail: attack chance −30. Caused by: items, enemies, dialogue and events, skills."
---

# ![](../assets/icons/conditions/actorconditions_1_80.png){ .sprite } Concussion

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_80.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `concussion` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −30 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Gamjee](../monsters/gamjee.md) | When it hits you | 1 | 2 rounds | 5% | gamjee_well_4_1 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [elm_mine5](../maps/elm_mine5.md) | [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-30) | 5 rounds |
| stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-1) | 10 rounds |
| stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | – | 10 rounds |
| walking into a blocked passage on [galmore_33](../maps/galmore_33.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-50) | 10 rounds |
| walking into a blocked passage on [brightport_cave6](../maps/brightport_cave6.md), walking into a blocked passage on [brightport_cave20](../maps/brightport_cave20.md) | – | 3 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [War Axe of the Shadow](../items/war_axe_shadow.md) | On the enemy you hit | 1 | 3 rounds | 20% |

**Skills**

| Skill | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Concussion](../skills/concussion.md) | On a hit when your attack chance exceeds the target's block chance by more than 50 | 1 | 5 rounds | 15% per skill level |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Immunity** from [Spiritbane potion](../items/spiritbane_potion.md) (when used; 6 rounds).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.

## Checked in dialogue

- stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) ([Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-2)) checks whether you have this condition.
- stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) ([Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-3)) checks whether you do not have this condition.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=concussion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=concussion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=concussion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `concussion` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:80` |
    | Defined in | `res/raw/actorconditions_v0611_2.json` |

    Raw data:

    ```json
    {
     "id": "concussion",
     "iconID": "actorconditions_1:80",
     "name": "Concussion",
     "category": "physical",
     "isStacking": 1,
     "abilityEffect": {
      "increaseAttackChance": -30
     }
    }
    ```


<small>Data from v0.8.18</small>
