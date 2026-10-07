---
description: "Weak Poison is a harmful blood condition in Andor's Trail: −1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_60.png){ .sprite } Weak Poison

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_60.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `poison_weak` |

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
| [Concentrated charwood sap](../items/drink_charwood2.md) | When used | 4 | 10 rounds | 15% |
| [Lodar's perilous concoction](../items/pot_rnd.md) | When used | 4 | 9 rounds | 10% |
| [Lowyna's rat poison](../items/drink_lowyn3.md) | When used | 2 | 10 rounds | 15% |
| [Sap of the charwood tree](../items/drink_charwood1.md) | When used | 4 | 10 rounds | 10% |
| [Weak poison](../items/pot_poison_weak.md) | When used | 1 | 5 rounds | 100% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Aggressive giant centipede](../monsters/centipede_aggressive.md) | When it hits you | 3 | 4 rounds | 50% | Lake Laeroth |
| [Aggressive venomscale](../monsters/vscale4.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 16, Lodar 17, Lodar 18 |
| [Angry cave worm](../monsters/ratdom_m11b.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Instrument maker, Library |
| [Big cave snake](../monsters/cavesnake4.md) | When it hits you | 1 | 3 rounds | 10% | 4 wells, Roundlings |
| [Biting caterpillar](../monsters/ratdom_m10b.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Gold hunter, Skeleton dance |
| [Bloated carrion centipede](../monsters/ccentip2.md) | When it hits you | 2 | 3 rounds | 50% | Charwood, Foaming Flask Tavern |
| [Breeder of venomscale](../monsters/vscaleb1.md) | When it hits you | 2 | 5 rounds | 30% | Lodar 16, Lodar 19 |
| [Burrowing glow worm](../monsters/burrowing_glow_worm.md) | When it hits you | 2 | 3 rounds | 30% | Gamjee well 1 1, Gamjee well 1 3, Gamjee well 2 1 |
| [Carrion centipede](../monsters/ccentip0.md) | When it hits you | 1 | 3 rounds | 50% | Charwood, Foaming Flask Tavern |
| [Fierce cave lizard](../monsters/ratdom_m7a.md) | When it hits you | 1 | 3 rounds | 10% | Bloskelt + Roskelt, Instrument maker, Entry |
| [Giant centipede](../monsters/centipede.md) | When it hits you | 2 | 3 rounds | 25% | Lake Laeroth |
| [Giant poisonous cave burrower](../monsters/caveburr5.md) | When it hits you | 2 | 3 rounds | 10% | Lodar 5cave 0, Lodar 5cave 1, Lodar 5cave 2 |
| [Gray venomscale](../monsters/vscale3.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 16, Lodar 20, Lodar 21 |
| [Lazy snail](../monsters/ratdom_m5a.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Bloskelt + Roskelt, Gold hunter |
| [Lord Erwyn](../monsters/erwyn.md) | When it hits you | 2 | 4 rounds | 40% | Flagstone Prison |
| [Malicious cave snake](../monsters/ratdom_m2b.md) | When it hits you | 1 | 3 rounds | 10% | Entry |
| [Malignant cave snake](../monsters/ratdom_m3a.md) | When it hits you | 1 | 3 rounds | 10% | Bloskelt + Roskelt, Roundlings, Labyrinth |
| [Nasty cave snake](../monsters/cavesnake5.md) | When it hits you | 1 | 3 rounds | 10% | Roundlings, 4 wells |
| [Nasty viper](../monsters/ratdom_m12b.md) | When it hits you | 1 | 3 rounds | 10% | Skeleton dance, Instrument maker, Pub |
| [Noxious venomfang](../monsters/noxious_venomfang.md) | When it hits you | 1 | 3 rounds | 60% | Blackwater Mountain |
| [Noxious venomfang](../monsters/noxious_venomfang.md) | When you defeat it | 3 | 2 rounds | 30% | Blackwater Mountain |
| [Old cave worm](../monsters/ratdom_m11c.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Instrument maker, Library |
| [Pernicious cave snake](../monsters/ratdom_m4a.md) | When it hits you | 1 | 3 rounds | 10% | Bloskelt + Roskelt, Gold hunter, Instrument maker |
| [Plague groundberry](../monsters/plague_groundberry.md) | When it hits you | 4 | 3 rounds | 50% | Sullengard woods 11, Sullengard woods 12, Sullengard woods 3 |
| [Poisenous snail](../monsters/ratdom_m5b.md) | When it hits you | 1 | 3 rounds | 30% | Pub, Bloskelt + Roskelt, Gold hunter |
| [Poisonous caterpillar](../monsters/ratdom_m10a.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Gold hunter, Skeleton dance |
| [Poisonous cave burrower](../monsters/caveburr3.md) | When it hits you | 1 | 3 rounds | 20% | Loneford |
| [Poisonous jitterfly](../monsters/poisonous_jitterfly.md) | When it hits you | 5 | 5 rounds | 70% | Deebo's Orchard |
| [Poisonous river frog](../monsters/frog_3.md) | When it hits you | 2 | 5 rounds | 30% | Guynmart Castle |
| [Poisonous vine](../monsters/poison_vine_top.md) | When it hits you | 3 | 5 rounds | 90% | Island underground 2, Island underground 3, Laerothcave 0 |
| [Puny venomscale](../monsters/vscale1.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 16, Lodar 20, Lodar 21 |
| [Quick venomscale](../monsters/vscale5.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 16, Lodar 17, Lodar 18 |
| [Quick viper](../monsters/ratdom_m12a.md) | When it hits you | 1 | 3 rounds | 10% | Skeleton dance, Instrument maker, Pub |
| [Ravenous carrion centipede](../monsters/ccentip1.md) | When it hits you | 1 | 3 rounds | 50% | Charwood, Foaming Flask Tavern |
| [Scaled venomfang](../monsters/scaled_venomfang.md) | When it hits you | 1 | 2 rounds | 50% | Blackwater Mountain |
| [Slippery Venomfang](../monsters/slippery_venomfang.md) | When it hits you | 1 | 3 rounds | 40% | Blackwater Mountain |
| [Slithering venomfang](../monsters/slithering_venomfang.md) | When it hits you | 1 | 2 rounds | 20% | Stoutford, Blackwater Mountain, Prim |
| [Snappy cave lizard](../monsters/ratdom_m7b.md) | When it hits you | 1 | 3 rounds | 10% | Bloskelt + Roskelt, Instrument maker, Entry |
| [Strong poisonous cave burrower](../monsters/caveburr4.md) | When it hits you | 1 | 5 rounds | 10% | Lodar 5cave 0, Lodar 5cave 1, Lodar 5cave 2 |
| [Strong venomscale](../monsters/vscale7.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 18, Lodar 19, Lodar 21 |
| [Tough venomfang](../monsters/tough_venomfang.md) | When it hits you | 1 | 2 rounds | 50% | Blackwater Mountain, Flagstone Prison |
| [Tough venomscale](../monsters/vscale8.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 19 |
| [Venomous beach crawler](../monsters/beach_crawler_1.md) | When it hits you | 3 | 4 rounds | 45% | Island 3, Island 4, Laerothcave 0 |
| [Venomous cave snake](../monsters/venomous_cave_snake.md) | When it hits you | 1 | 1 round | 10% | Brimhaven, Bloskelt + Roskelt, Entry |
| [Venomscale master](../monsters/vscaleb2.md) | When it hits you | 2 | 5 rounds | 30% | Lodar 17, Lodar 19 |
| [Vicious cave snake](../monsters/ratdom_m2a.md) | When it hits you | 1 | 3 rounds | 10% | Entry |
| [Vicious venomscale](../monsters/vscale6.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 18, Lodar 19, Lodar 21 |
| [Virulent cave snake](../monsters/ratdom_m4b.md) | When it hits you | 1 | 3 rounds | 10% | Bloskelt + Roskelt, Gold hunter, Instrument maker |
| [Young cave worm](../monsters/ratdom_m11a.md) | When it hits you | 1 | 3 rounds | 10% | Pub, Instrument maker, Library |
| [Young venomscale](../monsters/vscale2.md) | When it hits you | 2 | 3 rounds | 30% | Lodar 16, Lodar 20, Lodar 21 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [Ratdom maze 632](../maps/ratdom_maze_632.md) | – | 9 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blackwater poisoned dagger](../items/bwm_dagger_venom.md) | On the enemy you hit | 1 | 5 rounds | 50% |
| [Ring of venom](../items/ring_venom.md) | On the enemy that hits you | 1 | 12 rounds | 10% |
| [Serpent's fang](../items/clmr_serp.md) | On the enemy you hit | 1 | 5 rounds | 25% |
| [Venomfang dirk](../items/venomfang_dagger.md) | On the enemy you hit | 1 | 3 rounds | 20% |
| [Venomous Dagger](../items/dagger_venom.md) | On the enemy you hit | 1 | 2 rounds | 35% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** [Pure Blood](../skills/resistanceBlood.md), −10% of the chance per level (30% → 27% at level 1). 100% chances can't be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** −5% of the chance for any condition.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per round to weaken one timed harmful condition by 1.
- **Removed by** [Weak poison antidote](../items/pot_poison_weak_antidote.md) (when used).
- **Immunity** from [Ring of poison immunity](../items/ring_antipoison.md) (while equipped; while equipped).
- **Duration and rest:** timed ones wear off, or rest them away.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_weak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_weak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=poison_weak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `poison_weak` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:60` |
    | Defined in | `res/raw/actorconditions_v069.json` |

    Raw data:

    ```json
    {
     "id": "poison_weak",
     "iconID": "actorconditions_1:60",
     "name": "Weak Poison",
     "category": "blood",
     "roundEffect": {
      "visualEffectID": "greenSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
