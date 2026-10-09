---
description: "Nausea is a harmful physical condition in Andor's Trail: attack chance −10, block chance −10. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_japozero_2.png){ .sprite } Nausea

*Harmful physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_japozero_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `nausea` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −10 |
| Block chance | −10 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Boiled tripe](../items/tripe_boiled.md) | When used | 2 | 3 rounds | 3% |
| [Fermented garlic](../items/ferm-garlic.md) | When used | 1 | 5 rounds | 100% |
| [Salt pork](../items/salt_pork.md) | When used | 1 | 8 rounds | 15% |
| [Toasted inkyfish](../items/bwm_fish3.md) | When used | 2 | 7 rounds | 5% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Aggresive woodworm](../monsters/elm_woodworm2.md) | When you hit it | 2 | 2 rounds | 30% | Elm 2f 1, Elm 3f, Elm 4f 1 |
| [Contaminated miner's skeleton](../monsters/elm_miner3.md) | When you hit it | 4 | 3 rounds | 20% | Elm 5f 1, Elm 5f 2, Elm 4f 1 |
| [Contaminated olm](../monsters/bwm_olm5.md) | When you hit it | 2 | 2 rounds | 15% | Elm 2f 1, Elm 3f, Elm 4f 1 |
| [Contaminated woodworm](../monsters/elm_woodworm.md) | When you hit it | 2 | 3 rounds | 30% | Elm 2f 1, Elm 3f, Elm 4f 1 |
| [Dried kazarite golem](../monsters/elm_golem2.md) | When you hit it | 4 | 4 rounds | 15% | Elm 5f 1, Elm 5f 2, Elm 3f |
| [Glowing mudfiend](../monsters/elm_fiend1.md) | When you hit it | 3 | 3 rounds | 20% | Elm 5f 2, Elm 2f 1, Elm 3f |
| [Kazarite golem](../monsters/elm_golem1.md) | When you hit it | 3 | 5 rounds | 15% | Elm 5f 1, Elm 5f 2, Elm 3f |
| [King Sullengard forest snake](../monsters/sullengard_venom_snake_king.md) | When it hits you | 3 | 5 rounds | 43% | Way to sullengard east 8 |
| [King yellow tooth slitherer](../monsters/yellow_tooth_king.md) | When it hits you | 3 | 4 rounds | 49% | Way to sullengard east 1 |
| [Plague groundberry](../monsters/plague_groundberry.md) | When it hits you | 2 | 2 rounds | 25% | Sullengard woods 11, Sullengard woods 12, Sullengard woods 3 |
| [Prim guard skeleton](../monsters/elm_miner4.md) | When you hit it | 5 | 2 rounds | 25% | Elm 5f 1, Elm 5f 2, Elm 4f 1 |
| [Queen Sullengard forest snake](../monsters/sullengard_venom_snake_queen.md) | When it hits you | 3 | 5 rounds | 43% | Way to sullengard east 9 |
| [Ravenous glowing mudfiend](../monsters/elm_fiend2.md) | When you hit it | 3 | 5 rounds | 30% | Elm 5f 2, Elm 2f 1, Elm 3f |
| [Sullengard forest snake](../monsters/sullengard_venom_snake.md) | When it hits you | 3 | 5 rounds | 40% | Sullengard |
| [Sullengard red forest snake](../monsters/sull_red_forest_snake.md) | When it hits you | 3 | 5 rounds | 50% | Sullengard west ravine, Sullengard woods 1, Sullengard woods 13 |
| [Undead Kamelio](../monsters/kamelio2.md) | When you hit it | 4 | 2 rounds | 30% | Elm 5f 2 |
| [Yczorah](../monsters/elm_yzczorah2.md) | When you hit it | 5 | 3 rounds | 20% | Elm 5f 1, Elm 5f 2 |
| [Yczorah marauder](../monsters/elm_yczorah1.md) | When you hit it | 5 | 2 rounds | 20% | Elm 5f 1, Elm 5f 2 |
| [Yellow tooth slitherer](../monsters/yellow_tooth.md) | When it hits you | 3 | 4 rounds | 42% | Deebo's Orchard |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Elm mine 5](../maps/elm_mine5.md) | – | 6 rounds |
| walking into a blocked passage on [Elm mine 5](../maps/elm_mine5.md) | [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-29) | 12 rounds |
| stepping on a trigger on [Elm 5f 1](../maps/elm5f_1.md), stepping on a trigger on [Elm 5f 2](../maps/elm5f_2.md) | – | 5 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Yczorah nucleus](../items/yczorah2.md) | On the enemy that hits you | 4 | 3 rounds | 20% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Enduring Body](../skills/resistancePhysical.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Deebo's apple cider](../items/apple_orchard_cider.md) (when used).
- **Removed by** [Pink potion of stomach calming](../items/pink_potion.md) (when used).
- **Immunity** from [Boletus spelunca](../items/elm_mushroom1.md) (when used; 75 rounds).
- **Immunity** from [Kazarite cloak](../items/kamelio_drop3.md) (while equipped; while equipped).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=nausea.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=nausea.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=nausea.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `nausea` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_japozero:2` |
    | Defined in | `res/raw/actorconditions_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "nausea",
     "iconID": "actorconditions_japozero:2",
     "name": "Nausea",
     "category": "physical",
     "abilityEffect": {
      "increaseAttackChance": -10,
      "increaseBlockChance": -10
     }
    }
    ```


<small>Data from v0.8.18</small>
