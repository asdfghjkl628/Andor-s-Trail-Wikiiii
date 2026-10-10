---
description: "Food-poisoning is a harmful physical condition in Andor's Trail: −1 HP per round. Caused by: items, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_2_2.png){ .sprite } Food-poisoning

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_2_2.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `foodp` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Bogsten's mushroom](../items/mushroom_bogsten.md) | When used | 3 | 3 rounds | 50% |
| [Bramblefin](../items/bramblefin_fish.md) | When used | 3 | 10 rounds | 10% |
| [Curative potion against mushroom wounding](../items/fungi_panic_cure.md) | When used | 22 | 1 round | 100% |
| [Headless fish](../items/headless_fish.md) | When used | 3 | 8 rounds | 50% |
| [Healthier worm meat](../items/better_worm_meat.md) | When used | 5 | 6 rounds | 22% |
| [Hexi egg](../items/hexi_egg.md) | When used | 4 | 6 rounds | 18% |
| [Izthiel claw](../items/izthiel_claw.md) | When used | 3 | 10 rounds | 20% |
| [Lowyna's special brew](../items/drink_lowyn2.md) | When used | 5 | 12 rounds | 10% |
| [Meat](../items/meat.md) | When used | 3 | 10 rounds | 10% |
| [Mountain eel meat](../items/eel_meat.md) | When used | 2 | 9 rounds | 30% |
| [Nutritious snake meat](../items/ratdom_maze_mole_food.md) | When used | 5 | 9 rounds | 10% |
| [Potion of quick death](../items/pot_quickdeath.md) | When used | 20 | 50 rounds | 100% |
| [Raw inkyfish](../items/bwm_fish.md) | When used | 3 | 10 rounds | 10% |
| [Raw lamb meat](../items/lamb_meat_raw.md) | When used | 2 | 12 rounds | 25% |
| [Raw perch](../items/rawperch.md) | When used | 3 | 8 rounds | 10% |
| [Raw venison](../items/brightport_rawmeat.md) | When used | 4 | 10 rounds | 15% |
| [Rotten apple](../items/rotten_apple.md) | When used | 3 | 5 rounds | 100% |
| [Rotten fish](../items/rotten_fish.md) | When used | 5 | 10 rounds | 100% |
| [Rotten meat](../items/meat2.md) | When used | 5 | 10 rounds | 100% |
| [Serpent meat](../items/serpent_meat.md) | When used | 2 | 8 rounds | 8% |
| [Snake meat](../items/snake_meat.md) | When used | 3 | 10 rounds | 10% |
| [Spider eggs](../items/spider_eggs.md) | When used | 3 | 10 rounds | 5% |
| [Warg veal](../items/warg_veal.md) | When used | 3 | 6 rounds | 10% |
| [Worm meat](../items/meat3.md) | When used | 3 | 7 rounds | 30% |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Ratdom maze 632](../maps/ratdom_maze_632.md) | – | 4 rounds |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Antidote](../items/antifoodp.md) (when used).
- **Removed by** [Fermented garlic](../items/ferm-garlic.md) (when used).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=foodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=foodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=foodp.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `foodp` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_2:2` |
    | Defined in | `res/raw/actorconditions_v0612_2.json` |

    Raw data:

    ```json
    {
     "id": "foodp",
     "iconID": "actorconditions_2:2",
     "name": "Food-poisoning",
     "category": "physical",
     "roundEffect": {
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
