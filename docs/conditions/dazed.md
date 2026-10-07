---
description: "Dazed is a harmful mental condition in Andor's Trail: block chance −40. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_65.png){ .sprite } Dazed

*Harmful mental condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Mental](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Strong Mind](../skills/resistanceMental.md) |
| **Condition ID** | `dazed` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Block chance | −40 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Lowyna's rat poison](../items/drink_lowyn3.md) | When used | 1 | 5 rounds | 100% |
| [Polyphem's favourite wine](../items/ll2_wine.md) | When used | 1 | 10 rounds | 100% |
| [Restore fear](../items/pot_fear_restore.md) | When used | 1 | 5 rounds | 20% |
| [Restore stunned](../items/pot_stunned_restore.md) | When used | 1 | 4 rounds | 30% |
| [Rusty claymore](../items/clmr_rst.md) | While equipped | 1 | While equipped | – |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Ancient stone worm](../monsters/ancient_stone_worm.md) | When it hits you | 1 | 8 rounds | 15% | mywildcave, mywildcave2, mywildcave3 |
| [Angry stone worm](../monsters/angry_stoneworm.md) | When it hits you | 1 | 2 rounds | 33% | mywildcave2, mywildcave3 |
| [Azurite Gornaud](../monsters/gornaud_4.md) | When it hits you | 1 | 3 rounds | 25% | arulircave1, arulircave2, arulircave6 |
| [Cave troll shaman](../monsters/cave_troll_4.md) | When it hits you | 1 | 3 rounds | 10% | lakecave0, lakecave2 |
| [Garnet Gornaud](../monsters/gornaud_5.md) | When it hits you | 1 | 3 rounds | 25% | arulircave1, arulircave2, arulircave6 |
| [Gornaud](../monsters/gornaud.md) | When it hits you | 1 | 5 rounds | 50% | Blackwater Mountain |
| [Gornaud leader](../monsters/gornaud_boss.md) | When it hits you | 3 | 3 rounds | 50% | Blackwater Mountain |
| [Nephrite Gornaud](../monsters/gornaud_6.md) | When it hits you | 1 | 3 rounds | 25% | arulircave1, arulircave2, arulircave6 |
| [Old stone worm](../monsters/old_stone_worm.md) | When it hits you | 1 | 4 rounds | 15% | mywildcave, mywildcave1, mywildcave2 |
| [Stone worm](../monsters/stone_worm_2.md) | When it hits you | 1 | 2 rounds | 10% | mywildcave, mywildcave1, mywildcave2 |
| [Strong gornaud](../monsters/strong_gornaud.md) | When it hits you | 1 | 5 rounds | 70% | Blackwater Mountain |
| [Young gornaud](../monsters/young_gornaud.md) | When it hits you | 1 | 5 rounds | 20% | Stoutford, Blackwater Mountain, Prim |
| [Zortak leader](../monsters/zortakb.md) | When it hits you | 2 | 4 rounds | 20% | lodar8 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-1) | 5 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Bronzed grasps](../items/bronzed_gloves.md) | On the enemy you hit | 1 | 4 rounds | 20% |
| [Feygard plated gloves](../items/feygard_plated_gloves.md) | On the enemy you hit | 1 | 4 rounds | 20% |
| [Giant's flail](../items/flail_giant.md) | On the enemy you hit | 1 | 3 rounds | 20% |
| [Gleaming claymore of ruin](../items/clmr_ruin.md) | On the enemy you hit | 1 | 3 rounds | 30% |
| [Iron morningstar](../items/morn_iron.md) | On the enemy you hit | 1 | 4 rounds | 5% |
| [Thunderguard Copper sword](../items/thunderguard_2h_sword.md) | On the enemy you hit | 1 | 3 rounds | 25% |
| [Worn plated gloves](../items/hglv_plat1.md) | On the enemy you hit | 1 | 4 rounds | 20% |
| [Xul'viir](../items/xulviir.md) | On the enemy you hit | 1 | 2 rounds | 10% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Strong Mind](../skills/resistanceMental.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Restore dazed](../items/pot_dazed_restore.md) (when used).
- **Removed by** [Potion of alertness](../items/pot_alertness.md) (when used).
- **Removed by** [Potion of sound mind](../items/pot_sound_mind.md) (when used).
- **Immunity** from [Circlet of clarity](../items/circlet_clarity.md) (when you are hit; 3 rounds).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier; permanent applications (from equipment or story events) are not removed by resting.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=dazed.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=dazed.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=dazed.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `dazed` |
    | Category (internal) | `mental` |
    | Icon | `actorconditions_1:65` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "dazed",
     "iconID": "actorconditions_1:65",
     "name": "Dazed",
     "category": "mental",
     "abilityEffect": {
      "increaseBlockChance": -40
     }
    }
    ```


<small>Data from v0.8.18</small>
