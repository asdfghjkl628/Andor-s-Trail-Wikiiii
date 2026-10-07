---
description: "Fear is a harmful mental condition in Andor's Trail: attack chance −5, damage −1, block chance −10, damage resistance −1. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_30.png){ .sprite } Fear

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_30.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `fear` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −5 |
| Attack damage | −1 |
| Block chance | −10 |
| Damage resistance | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Feline hat](../items/feline_hat.md) | When you are hit | 1 | 2 rounds | 5% |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Benzimos](../monsters/haunted_benzimos.md) | When it hits you | 3 | 3 rounds | 50% | haunted_house_basement |
| [Death wrecker](../monsters/death_wrecker.md) | When it hits you | 4 | 3 rounds | 25% | haunted_house, haunted_house_basement, haunted_underground_1 |
| [Dread guardian](../monsters/tesrekan_guardian.md) | When it hits you | 2 | 3 rounds | 35% | waterwayacave1 |
| [Hira'zinn](../monsters/hirazinn.md) | When it hits you | 4 | 3 rounds | 30% | lodarcave4a |
| [Tesrekan](../monsters/tesrekan.md) | When it hits you | 3 | 5 rounds | 50% | waterwayacave4 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-30) | 15 rounds |
| stepping on a trigger on [guynmart_tower_0](../maps/guynmart_tower_0.md) | – | 8 rounds |
| stepping on a trigger on [mushroom_m3_1](../maps/mushroom_m3_1.md) | [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-10) | 8 rounds |
| [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | 15 rounds |
| stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) | [The Dead are Walking](../quests/dead_walking.md#stage-50) | 5 rounds |
| stepping on a trigger on [ratdom_maze_542](../maps/ratdom_maze_542.md) | – | 25 rounds |
| stepping on a trigger on [ratdom_maze_648](../maps/ratdom_maze_648.md) | – | 10 rounds |
| stepping on a trigger on [korhald_cave_outdoor1](../maps/korhald_cave_outdoor1.md) | [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-41) | 3 rounds |
| walking into a blocked passage on [galmore_32](../maps/galmore_32.md) | [A familiar shadow](../quests/familiar_shadow.md#stage-10) | 15 rounds |
| stepping on a trigger on [galmore_10](../maps/galmore_10.md), stepping on a trigger on [galmore_12a](../maps/galmore_12a.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-1) | 1 round |
| stepping on a trigger on [galmore_10](../maps/galmore_10.md), stepping on a trigger on [galmore_12a](../maps/galmore_12a.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-2) | 3 rounds |
| stepping on a trigger on [galmore_10](../maps/galmore_10.md), stepping on a trigger on [galmore_12a](../maps/galmore_12a.md) | – | 5 rounds |
| walking into a blocked passage on [galmore_32](../maps/galmore_32.md), walking into a blocked passage on [crossglen](../maps/crossglen.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-1) | 1 round |
| walking into a blocked passage on [crossglen](../maps/crossglen.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-2) | 3 rounds |
| walking into a blocked passage on [crossglen](../maps/crossglen.md) | – | 5 rounds |
| stepping on a trigger on [galmore_15](../maps/galmore_15.md) | – | 3 rounds |
| walking into a blocked passage on [undertell_10](../maps/undertell_10.md) | [Lost treasures](../quests/nocmar.md#stage-60) | 7 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Axe of fear](../items/axe_fear.md) | On the enemy you hit | 1 | 3 rounds | 20% |
| [Shadowstalker](../items/shdstlk.md) | On the enemy you hit | 1 | 5 rounds | 20% |
| [Shield of dark reflections](../items/shield_dark_ref.md) | On the enemy that hits you | 1 | 4 rounds | 18% |
| [Stormcloak armor](../items/stormcloak_armor.md) | On the enemy you hit | 1 | 5 rounds | 20% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Strong Mind](../skills/resistanceMental.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Restore fear](../items/pot_fear_restore.md) (when used).
- **Removed by** [Potion of heroism](../items/pot_heroism.md) (when used).
- **Immunity** from [Ortholion's talisman](../items/ortholion_reward.md) (while equipped; while equipped).
- **Immunity** from [Shield of the Brave](../items/shield_of_brave.md) (when you hit with it; 3 rounds).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fear.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fear.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=fear.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `fear` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:30` |
    | Defined in | `res/raw/actorconditions_v070.json` |

    Raw data:

    ```json
    {
     "id": "fear",
     "iconID": "actorconditions_1:30",
     "name": "Fear",
     "category": "mental",
     "abilityEffect": {
      "increaseAttackChance": -5,
      "increaseAttackDamage": {
       "min": -1,
       "max": -1
      },
      "increaseBlockChance": -10,
      "increaseDamageResistance": -1
     }
    }
    ```


<small>Data from v0.8.18</small>
