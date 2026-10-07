---
description: "Bleeding wound is a harmful blood condition in Andor's Trail: −1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_2_0.png){ .sprite } Bleeding wound

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | Yes |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `bleeding_wound` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | −1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** Yes. A second application with the same duration adds its magnitude to the existing one; one with a different duration is kept as a separate instance.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Miner's hooded tunic](../items/miner_hood.md) | While equipped | 1 | While equipped | – |
| [Miner's tunic](../items/miner_tunic.md) | While equipped | 1 | While equipped | – |

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Aggresive woodworm](../monsters/elm_woodworm2.md) | When it hits you | 2 | 2 rounds | 20% | elm_2f_1, elm_3f, elm_4f_1 |
| [Ancient branchtender](../monsters/brtender_cr.md) | When it hits you | 1 | 5 rounds | 20% | lodar15 |
| [Animated debris](../monsters/elm_debris.md) | When it hits you | 3 | 5 rounds | 20% | elm5f_2, elm_2f_1 |
| [Cave mole](../monsters/ratdom_maze_mole.md) | When it hits you | 1 | 2 rounds | 75% | Bloskelt + Roskelt |
| [Contaminated miner's skeleton](../monsters/elm_miner3.md) | When it hits you | 4 | 3 rounds | 20% | elm5f_1, elm5f_2, elm_4f_1 |
| [Contaminated olm](../monsters/bwm_olm5.md) | When it hits you | 2 | 2 rounds | 10% | elm_2f_1, elm_3f, elm_4f_1 |
| [Contaminated woodworm](../monsters/elm_woodworm.md) | When it hits you | 1 | 2 rounds | 20% | elm_2f_1, elm_3f, elm_4f_1 |
| [Dread zombie](../monsters/oldcaveboss.md) | When it hits you | 5 | 7 rounds | 30% | Foaming Flask Tavern |
| [Dried kazarite golem](../monsters/elm_golem2.md) | When it hits you | 8 | 2 rounds | 10% | elm5f_1, elm5f_2, elm_3f |
| [Frantic branchtender](../monsters/brtender2.md) | When it hits you | 1 | 5 rounds | 20% | lodar19 |
| [Glowing mudfiend](../monsters/elm_fiend1.md) | When it hits you | 3 | 3 rounds | 15% | elm5f_2, elm_2f_1, elm_3f |
| [Golden jackal](../monsters/golden_jackal.md) | When it hits you | 3 | 3 rounds | 15% | sullengard_west_ravine, sullengard_woods12, sullengard_woods4 |
| [Hira'zinn](../monsters/hirazinn.md) | When it hits you | 3 | 3 rounds | 30% | lodarcave4a |
| [Izthiel guardian](../monsters/izthiel_4.md) | When it hits you | 3 | 5 rounds | 50% | Brimhaven |
| [Kazarite golem](../monsters/elm_golem1.md) | When it hits you | 7 | 2 rounds | 10% | elm5f_1, elm5f_2, elm_3f |
| [Madame Mim](../monsters/swamp_witch.md) | When it hits you | 2 | 10 rounds | 50% | swamp_hut |
| [Prim guard skeleton](../monsters/elm_miner4.md) | When it hits you | 5 | 2 rounds | 25% | elm5f_1, elm5f_2, elm_4f_1 |
| [Ravenous glowing mudfiend](../monsters/elm_fiend2.md) | When it hits you | 3 | 5 rounds | 20% | elm5f_2, elm_2f_1, elm_3f |
| [River snapper](../monsters/sutdover_snapper.md) | When you hit it | 3 | 3 rounds | 15% | Mt. Galmore |
| [Shadowfang](../monsters/shadowfang1.md) | When it hits you | 3 | 2 rounds | 5% | blackwater_mountain76, elm_2f_1, elm_2f_3 |
| [Snapmaw](../monsters/snapmaw.md) | When you hit it | 4 | 4 rounds | 15% | Mt. Galmore |
| [Stoneclaw prowler](../monsters/stoneclaw_prowler.md) | When it hits you | 3 | 4 rounds | 30% | Stoutford, Flagstone Prison |
| [Strong izthiel](../monsters/izthiel_3.md) | When it hits you | 2 | 4 rounds | 40% | Flagstone Prison, Brimhaven |
| [Sullengard snapper](../monsters/sullengard_snapper.md) | When you hit it | 1 | 5 rounds | 10% | Sullengard |
| [Thorny vine](../monsters/thorny_vine_bottom.md) | When you hit it | 8 | 3 rounds | 100% | Mt. Galmore |
| [Undead Kamelio](../monsters/kamelio2.md) | When it hits you | 4 | 4 rounds | 30% | elm5f_2 |
| [Yczorah](../monsters/elm_yzczorah2.md) | When it hits you | 6 | 2 rounds | 10% | elm5f_1, elm5f_2 |
| [Yczorah marauder](../monsters/elm_yczorah1.md) | When it hits you | 5 | 2 rounds | 10% | elm5f_1, elm5f_2 |

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 7 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 3 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 5 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 4 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 6 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 7 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 8 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 9 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 10 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave3](../maps/arulircave3.md) | – | 5 rounds |
| stepping on a trigger on [arulircave1](../maps/arulircave1.md), stepping on a trigger on [arulircave2](../maps/arulircave2.md) | – | 9 rounds |
| stepping on a trigger on [mushroom_m2_2](../maps/mushroom_m2_2.md) | [mushroomcave_trap (hidden flag)](../quests/mushroomcave_trap.md#stage-10) | 10 rounds |
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) ([blackwater_mountain32](../maps/blackwater_mountain32.md)), walking into a blocked passage on [blackwater_mountain32](../maps/blackwater_mountain32.md) | – | 10 rounds |
| stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) | [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-28) | 4 rounds |
| walking into a blocked passage on [elm_mine5](../maps/elm_mine5.md) | – | 8 rounds |
| stepping on a trigger on [elm_mine5](../maps/elm_mine5.md) | [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-30) | 6 rounds |
| stepping on a trigger on [elm5f_1](../maps/elm5f_1.md), stepping on a trigger on [elm5f_2](../maps/elm5f_2.md) | – | 6 rounds |
| [Sullengard snapper](../monsters/sullengard_snapper.md) ([sullengard5](../maps/sullengard5.md)) | – | 5 rounds |
| walking into a blocked passage on [final_cave2](../maps/final_cave2.md) | [Not Pony Island](../quests/lae_centaurs.md#stage-210) | 3 rounds |
| stepping on a trigger on [laerothbasement2](../maps/laerothbasement2.md) | – | 7 rounds |
| stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-1) | 15 rounds |
| stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | – | 15 rounds |
| walking into a blocked passage on [galmore_33](../maps/galmore_33.md) | [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-50) | 20 rounds |
| stepping on a trigger on [waytobrightport0](../maps/waytobrightport0.md) | [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-252) | 3 rounds |
| stepping on a trigger on [waytobrightport0](../maps/waytobrightport0.md) | – | 3 rounds |
| stepping on a trigger on [waytobrightport10](../maps/waytobrightport10.md) | [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-253) | 3 rounds |

## Applied to enemies

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Barbed dagger](../items/dagger_barbed.md) | On the enemy you hit | 1 | 5 rounds | 50% |
| [Blood seeker](../items/bloodseeker.md) | On the enemy you hit | 5 | 5 rounds | 25% |
| [Glaive of Imeria](../items/glaive_butcher.md) | On the enemy you hit | 2 | 4 rounds | 20% |
| [LifeTaker](../items/lifetaker.md) | On the enemy you hit | 1 | 2 rounds | 15% |
| [Obsidian dagger](../items/obsidian_dagger.md) | On the enemy you hit | 3 | 5 rounds | 20% |
| [Spiked club of bleeding](../items/club_bld.md) | On the enemy you hit | 1 | 2 rounds | 15% |
| [Spiked Gloves](../items/gauntlet_omi2_1.md) | On the enemy you hit | 1 | 2 rounds | 5% |
| [Steel shortsword](../items/shortsword2.md) | On the enemy you hit | 2 | 2 rounds | 10% |
| [Undertell pickaxe](../items/undertell_pickaxe.md) | On the enemy you hit | 3 | 2 rounds | 20% |
| [Xul'viir](../items/xulviir.md) | On the enemy you hit | 3 | 3 rounds | 15% |
| [Yczorah nucleus](../items/yczorah2.md) | On the enemy you hit | 2 | 2 rounds | 10% |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Pure Blood](../skills/resistanceBlood.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **[Rejuvenation](../skills/rejuvenation.md):** each round, a 20% chance per skill level to reduce the magnitude of one random timed harmful condition by 1.
- **Removed by** [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) (when used).
- **Removed by** [Bandage](../items/bandage.md) (when used).
- **Removed by** [Leech](../items/leech_usable.md) (when used).
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier; permanent applications (from equipment or story events) are not removed by resting.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bleeding_wound.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bleeding_wound.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=bleeding_wound.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `bleeding_wound` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_2:0` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "bleeding_wound",
     "iconID": "actorconditions_2:0",
     "name": "Bleeding wound",
     "category": "blood",
     "isStacking": 1,
     "roundEffect": {
      "visualEffectID": "redSplash",
      "increaseCurrentHP": {
       "min": -1,
       "max": -1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
