---
description: "Regeneration is a beneficial physical condition in Andor's Trail: +1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_35.png){ .sprite } Regeneration

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `regen2` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blackwater ring of combat](../items/bwm_combat_ring.md) | When you hit with it | 1 | 3 rounds | 20% |
| [Heartfire pendant of Kazaul](../items/heartfire_pendant.md) | While equipped | 4 | While equipped | – |
| [Heartsteel trident](../items/heartstone_glaive.md) | When an attack misses you | 5 | 1 round | 10% |
| [Kazarite cloak](../items/kamelio_drop3.md) | When you hit with it | 5 | 1 round | 10% |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | When used | 3 | 5 rounds | 100% |
| [Lodar's bonemeal potion](../items/pot_bm_lodar.md) | When used | 3 | 5 rounds | 100% |
| [Lodar's bonemeal potion](../items/pot_bm_lodar.md) | When used | 5 | 5 rounds | 20% |
| [Lodar's potion of health](../items/pot_healthlodar.md) | When used | 3 | 8 rounds | 100% |
| [Nimael's vegetable soup](../items/nimael_soup.md) | When used | 1 | 5 rounds | 100% |
| [Photosynthetic leaf](../items/photosynthetic_leaf.md) | When used | 4 | 3 rounds | 100% |
| [Potion of minor regeneration](../items/pot_regen1.md) | When used | 1 | 4 rounds | 100% |
| [Tonic of blood](../items/tonic_of_blood.md) | When used | 4 | 5 rounds | 60% |
| [Vaelric's elixir of vitality](../items/vaelric_pot_health.md) | When used | 5 | 6 rounds | 100% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Ratdom maze 632](../maps/ratdom_maze_632.md) | – | 20 rounds |
| walking into a blocked passage on [Swamp hut](../maps/swamp_hut.md) | – | 5 rounds |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Benzimos](../monsters/haunted_benzimos.md) | On itself, when you hit it | 7 | 1 round | 100% | Haunted house basement |
| [Death wrecker](../monsters/death_wrecker.md) | On itself, when you hit it | 6 | 1 round | 100% | Haunted house, Haunted house basement, Haunted underground 1 |
| [Grieveless dead](../monsters/grieveless_dead.md) | On itself, when you hit it | 6 | 1 round | 100% | Haunted cemetery 1, Haunted cemetery 2, Haunted forest 17 |
| [Mulgrith](../monsters/mulgrith.md) | On itself, when you hit it | 10 | 1 round | 100% | Galmore 19 |
| [Musty prowler](../monsters/musty_prowler.md) | On itself, when you hit it | 4 | 1 round | 100% | Haunted cemetery 1, Haunted cemetery 2, Haunted forest 12 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted. Yes, it also lowers your chance of getting this *beneficial* one.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **Duration and rest:** timed ones wear off, or rest them away; permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=regen2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=regen2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=regen2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `regen2` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:35` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "regen2",
     "iconID": "actorconditions_1:35",
     "name": "Regeneration",
     "category": "physical",
     "isPositive": 1,
     "roundEffect": {
      "visualEffectID": "blueSwirl",
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
