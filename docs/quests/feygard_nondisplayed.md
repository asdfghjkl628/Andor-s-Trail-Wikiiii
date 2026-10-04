# feygard_nondisplayed

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_nondisplayed` |
| **In journal** | No (hidden flag) |
| **Stages** | 35 |
| **Started by** | walking into a blocked passage on [guynmart_wood_16](../maps/guynmart_wood_16.md) |
| **NPCs involved** | [Athamyr](../monsters/athamyr.md), [Gamjee](../monsters/gamjee.md), [Gamjee](../monsters/gamjee_oc.md), [Godelieve](../monsters/village_godelieve.md), [Godoe](../monsters/godoe2.md), [Godoe](../monsters/godoe1.md) +5 |
| **Locations** | [beekeeper1](../maps/beekeeper1.md), [fallhaven_clothes](../maps/fallhaven_clothes.md), [gamjee_well_4_1](../maps/gamjee_well_4_1.md), [guynmart_wood_18](../maps/guynmart_wood_18.md) |
| **Total XP** | 1,101 |
| **Related quests** | 3 |

</div>

## Overview

> 1=Stolen from offering to Elythara

## Prerequisites to start

Start with walking into a blocked passage on [guynmart_wood_16](../maps/guynmart_wood_16.md). Required:

- faction “feygard_offering_sum” ≥ 1
- reached stage 1 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-1)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Key of Luthor](bucus.md#stage-100) | stage 100 reached, for stage 60 here |
| Requires | [Echoes of enchantment](echoes_of_enchantment.md#stage-5) | stage 5 reached, for stages 4, 5, 6 here |
| Requires | [Echoes of enchantment](echoes_of_enchantment.md#stage-8) | stage 8 reached, for stage 6 here |
| Requires | [Echoes of enchantment](echoes_of_enchantment.md#stage-12) | stage 12 reached, for stage 9 here |
| Requires | [A Feygard delicacy](feygard_delicacy.md#stage-7) | stage 7 reached, for stage 12 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-5) | stage 5 must NOT be reached, for stages 3, 5 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-8) | stage 8 must NOT be reached, for stages 3, 4, 5, 6 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-9) | stage 9 must NOT be reached, for stage 2 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-10) | stage 10 must NOT be reached, for stages 2, 11 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-11) | stage 11 must NOT be reached, for stage 2 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-12) | stage 12 must NOT be reached, for stage 6 here |
| Blocked by | [Echoes of enchantment](echoes_of_enchantment.md#stage-13) | stage 13 must NOT be reached, for stages 2, 3, 5 here |
| Unlocks | [Echoes of enchantment](echoes_of_enchantment.md#stage-9) | stage 9 there needs stage 4 here |
| Unlocks | [Echoes of enchantment](echoes_of_enchantment.md#stage-11) | stage 11 there needs stage 3 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=Stolen from offering to Elythara | walking into a blocked passage on [guynmart_wood_16](../maps/guynmart_wood_16.md) | – | applies condition stunned<br>applies condition bone_fracture<br>spawns monsters on guynmart_wood_16<br>applies condition elytharabless_heal |
| <span id="stage-2"></span>2 | The PC threw an Oegyth Crystal down the well in Wexlow Village.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wexlow village](../maps/wexlow_village.md).</span> | stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | hand over 1× [Oegyth crystal](../items/oegyth.md) | spawns monsters on gamjee_well_4_1<br>removes monsters from gamjee_well_4_1 |
| <span id="stage-3"></span>3 | The PC has attacked Gamjee the troll under the village of Wexlow without knowing that Gamjee has those villagers held captive. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | – | – |
| <span id="stage-4"></span>4 | The PC has attacked Gamjee the troll under the village of Wexlow after learning that Gamjee has those villagers held captive. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | – | – |
| <span id="stage-5"></span>5 | The PC has attacked Gamjee the troll under the village of Wexlow. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | – | – |
| <span id="stage-6"></span>6 | Gamjee, the troll under the village of Wexlow has sent the villager back to Wexlow. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | – | removes monsters from gamjee_well_4_1<br>sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12)<br>spawns monsters on wexlow_village |
| <span id="stage-7"></span>7 | PC gave Godwin, a villager from Wexlow, his lost ring. [wrapper for 13, 14, 15] | [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) | carry 1× [Godwin's ring](../items/godwin_ring.md), hand over 1× [Godwin's ring](../items/godwin_ring.md) | gives 2000× [Gold coins](../items/gold.md)<br>gives 3000× [Gold coins](../items/gold.md)<br>gives 100× [Gold coins](../items/gold.md) |
| <span id="stage-8"></span>8 | PC learns that Rosmara sells fruits and vegetables | [Rosmara](../monsters/rosmara.md) ([wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md)) | – | – |
| <span id="stage-9"></span>9 | PC can sleep in Wexlow Village.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wexlow village nw house](../maps/wexlow_village_nw_house.md).</span> | [Godelieve](../monsters/village_godelieve.md) ([wexlow_village_nw_house](../maps/wexlow_village_nw_house.md)) | – | – |
| <span id="stage-10"></span>10 | PC has learned what the beekeeper, Leofric does for work. | [Leofric](../monsters/leofric.md) ([beekeeper1](../maps/beekeeper1.md)) | – | – |
| <span id="stage-11"></span>11 | In Wexlow Village, the PC has learned that there are missing residents. | walking into a blocked passage on [wexlow_village_n_house](../maps/wexlow_village_n_house.md)<br>walking into a blocked passage on [wexlow_village_nw_house](../maps/wexlow_village_nw_house.md) | – | – |
| <span id="stage-12"></span>12 | PC is not being patient while waiting for the Feydelight to be cooked. | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | – | – |
| <span id="stage-13"></span>13 | PC gave Godwin, a villager from Wexlow, his lost ring for free. | [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) | carry 1× [Godwin's ring](../items/godwin_ring.md), hand over 1× [Godwin's ring](../items/godwin_ring.md) | 1,000 XP<br>gives 100× [Gold coins](../items/gold.md) |
| <span id="stage-14"></span>14 | PC gave Godwin, a villager from Wexlow, his lost ring for 2k gold. | [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) | carry 1× [Godwin's ring](../items/godwin_ring.md), hand over 1× [Godwin's ring](../items/godwin_ring.md) | 100 XP<br>gives 2000× [Gold coins](../items/gold.md) |
| <span id="stage-15"></span>15 | PC gave Godwin, a villager from Wexlow, his lost ring for 3k gold. | [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) | carry 1× [Godwin's ring](../items/godwin_ring.md), hand over 1× [Godwin's ring](../items/godwin_ring.md) | 1 XP<br>gives 3000× [Gold coins](../items/gold.md) |
| <span id="stage-20"></span>20 | 20=Road to Feygard closed (wayto_feygard_duleian_2)<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wayto feygard duleian 2](../maps/wayto_feygard_duleian_2.md).</span> | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-30"></span>30 | boat0 clear<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) | – | faction “boat0” set to 1 |
| <span id="stage-31"></span>31 | boat0 sunk<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) | – | faction “boat0” set to 5<br>applies condition drowning |
| <span id="stage-32"></span>32 | boat0 save<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) | stage 31 | faction “boat0” set to 9<br>applies condition drowning |
| <span id="stage-60"></span>60 | 60=talked to Arthamyr | [Athamyr](../monsters/athamyr.md) | – | – |
| <span id="stage-61"></span>61 | 61=ladder placed | [Athamyr](../monsters/athamyr.md) | carry 10× [Cooked meat](../items/meat_cooked.md), hand over 10× [Cooked meat](../items/meat_cooked.md), stage 60 | – |
| <span id="stage-62"></span>62 | 62=tried window | walking into a blocked passage on [catacombs1](../maps/catacombs1.md) | – | – |
| <span id="stage-63"></span>63 | 63=church window unlocked | [Athamyr](../monsters/athamyr.md) | carry 20× [Cooked meat](../items/meat_cooked.md), hand over 20× [Cooked meat](../items/meat_cooked.md), stage 62 | clears stage 72 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-72) |
| <span id="stage-65"></span>65 | 65=jewel taken | walking into a blocked passage on [fallhaven_clothes](../maps/fallhaven_clothes.md) | stage 66 | gives 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md) |
| <span id="stage-66"></span>66 | 66=passed window towards tailor<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven ne](../maps/fallhaven_ne.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span> | stepping on a trigger on [fallhaven_ne](../maps/fallhaven_ne.md) | – | – |
| <span id="stage-68"></span>68 | 68=seen<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span> | [Tailor](../monsters/tailor.md) ([fallhaven_clothes](../maps/fallhaven_clothes.md))<br>stepping on a trigger on [fallhaven_clothes](../maps/fallhaven_clothes.md)<br>walking into a blocked passage on [fallhaven_clothes](../maps/fallhaven_clothes.md) | stage 66 | – |
| <span id="stage-69"></span>69 | 69=closed<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven ne](../maps/fallhaven_ne.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven nw](../maps/fallhaven_nw.md).</span> | stepping on a trigger on [fallhaven_clothes](../maps/fallhaven_clothes.md)<br>stepping on a trigger on [fallhaven_ne](../maps/fallhaven_ne.md) | carry 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md), stage 65 | clears stage 73 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-73) |
| <span id="stage-71"></span>71 | 71=ladder place 1<br><span class="qnote">🗺️ Part of [Catacombs1](../maps/catacombs1.md) visibly changes.</span> | [Athamyr](../monsters/athamyr.md) | carry 10× [Cooked meat](../items/meat_cooked.md), hand over 10× [Cooked meat](../items/meat_cooked.md), stage 60 | – |
| <span id="stage-72"></span>72 | 72=ladder place 2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Catacombs1](../maps/catacombs1.md).</span><br><span class="qnote">🗺️ Part of [Catacombs1](../maps/catacombs1.md) visibly changes.</span> | stepping on a trigger on [catacombs1](../maps/catacombs1.md) | stage 71 | clears stage 71 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-71) |
| <span id="stage-73"></span>73 | 73=windows church unlocked from inside<br><span class="qnote">🔓 You can finally access a previously blocked area on [Catacombs1](../maps/catacombs1.md).</span><br><span class="qnote">🗺️ Part of [Catacombs1](../maps/catacombs1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Fallhaven clothes](../maps/fallhaven_clothes.md) visibly changes.</span> | [Athamyr](../monsters/athamyr.md) | carry 20× [Cooked meat](../items/meat_cooked.md), hand over 20× [Cooked meat](../items/meat_cooked.md), stage 62 | clears stage 72 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-72) |
| <span id="stage-80"></span>80 | 80=Path open<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | [Godoe](../monsters/godoe1.md) ([guynmart_wood_18](../maps/guynmart_wood_18.md))<br>walking into a blocked passage on [guynmart_wood_18](../maps/guynmart_wood_18.md) | hand over 5× [Ruby gem](../items/gem2.md) | faction “guynmart18” set to 0 |
| <span id="stage-81"></span>81 | 81=Godoe in the south<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18b](../maps/guynmart_wood_18b.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18c](../maps/guynmart_wood_18c.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span> | stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) | – | spawns monsters on guynmart_wood_18<br>removes monsters from guynmart_wood_18 |
| <span id="stage-90"></span>90 | 90=Ravine blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17b](../maps/guynmart_wood_17b.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 19](../maps/guynmart_wood_19.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md) | – | clears stage 91 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-91)<br>clears stage 92 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-92) |
| <span id="stage-91"></span>91 | 91=Ravine outlets blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) | – | clears stage 90 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-90)<br>clears stage 92 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-92) |
| <span id="stage-92"></span>92 | 92=Ravine free<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) | – | clears stage 90 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-90)<br>clears stage 91 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-91)<br>spawns monsters on guynmart_wood_18 |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. walking into a blocked passage on [guynmart_wood_16](../maps/guynmart_wood_16.md) → choose “Take 1 gold coin.” — **conditions:** faction “feygard_offering_sum” ≥ 1; reached stage 1 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-1) → **stage 1**; also applies condition stunned, applies condition bone_fracture, spawns monsters on guynmart_wood_16, applies condition elytharabless_heal. NPC: “Elythara is known for her thirst for revenge. Fear her wrath!”

???+ note "Stage 2: 1 route"

    1. stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) → choose “[Throw an Oegyth Crystal]” — **conditions:** NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10); NOT reached stage 11 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 9 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9); hand over 1× [Oegyth crystal](../items/oegyth.md); NOT reached stage 2 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-2) → **stage 2**; also spawns monsters on gamjee_well_4_1, removes monsters from gamjee_well_4_1. NPC: “Glowing thing... pretty, but useless! Gamjee no care for it!”

???+ note "Stage 3: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “I don't believe you! Prove it.” — **conditions:** NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8) → **stage 3**. NPC: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”

???+ note "Stage 4: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “It's time to make me righteous!” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8) → **stage 4**. NPC: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”

???+ note "Stage 5: 2 routes"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “I don't believe you! Prove it.” — **conditions:** NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8) → **stage 5**. NPC: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”
    2. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “It's time to make me righteous!” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8) → **stage 5**. NPC: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”

???+ note "Stage 6: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “Alright. Let's make this work.” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12) → **stage 6**; also removes monsters from gamjee_well_4_1, sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12), spawns monsters on wexlow_village. NPC: “You human, go back village now.”

???+ note "Stage 7: 3 routes"

    1. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “Sounds good.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 7**; also gives 2000× [Gold coins](../items/gold.md). NPC: “Thank you so much! Here take these coins.”
    2. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “3,000 gold or no ring.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 7**; also gives 3000× [Gold coins](../items/gold.md). NPC: “Fine! Take the coins you thief.”
    3. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “Sure. Here, it's yours.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 7**; also gives 100× [Gold coins](../items/gold.md). NPC: “Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.”

???+ note "Stage 8: 1 route"

    1. Talk to [Rosmara](../monsters/rosmara.md) ([wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md)) → choose “What is it?” → **stage 8**. NPC: “I sell fruits and vegetables.”

???+ note "Stage 9: 1 route"

    1. Talk to [Godelieve](../monsters/village_godelieve.md) ([wexlow_village_nw_house](../maps/wexlow_village_nw_house.md)) → choose “Would it be OK with you if I slept here? I'm pretty tired.” — **conditions:** reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12) → **stage 9**. NPC: “Of course. Just use the mat over there in the corner.”

???+ note "Stage 10: 1 route"

    1. Talk to [Leofric](../monsters/leofric.md) ([beekeeper1](../maps/beekeeper1.md)) → choose “Do you have anything for sale?” → **stage 10**. NPC: “Aye, I have many wares to offer. Jars of honey, beeswax and some fine mead. But that's it for now as my supply is…”

???+ note "Stage 11: 2 routes"

    1. walking into a blocked passage on [wexlow_village_n_house](../maps/wexlow_village_n_house.md) → choose “I sure do.” — **conditions:** NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10) → **stage 11**. NPC: “Dear Theodora, I've come to visit you again today, but once more, I find your home empty. It's been nearly a month…”
    2. walking into a blocked passage on [wexlow_village_nw_house](../maps/wexlow_village_nw_house.md) → choose “I think I should.” — **conditions:** NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10) → **stage 11**. NPC: “It's been days since anyone has seen Odilia. At first, we thought she might have gone to visit her sister in Feygard,…”

???+ note "Stage 12: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “I am wondering, is my Feydelight ready yet?” — **conditions:** latest stage of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) is 7; NOT reached stage 12 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-12) → **stage 12**. NPC: “Sorry, no it is not. Please come back later.”

???+ note "Stage 13: 1 route"

    1. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “Sure. Here, it's yours.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 13**; also gives 100× [Gold coins](../items/gold.md). NPC: “Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.”

???+ note "Stage 14: 1 route"

    1. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “Sounds good.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 14**; also gives 2000× [Gold coins](../items/gold.md). NPC: “Thank you so much! Here take these coins.”

???+ note "Stage 15: 1 route"

    1. Talk to [Godwin](../monsters/village_godwin.md) ([wexlow_village](../maps/wexlow_village.md)) → choose “3,000 gold or no ring.” — **conditions:** NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7); carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md) → **stage 15**; also gives 3000× [Gold coins](../items/gold.md). NPC: “Fine! Take the coins you thief.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) → the conversation leads here automatically — **conditions:** NOT reached stage 30 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-30) → **stage 30**; also faction “boat0” set to 1

???+ note "Stage 31: 1 route"

    1. stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) → the conversation leads here automatically — **conditions:** NOT reached stage 31 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-31) → **stage 31**; also faction “boat0” set to 5, applies condition drowning. NPC: “The boat seems to have a leak!”

???+ note "Stage 32: 1 route"

    1. stepping on a trigger on [gapfillerhole](../maps/gapfillerhole.md) → the conversation leads here automatically — **conditions:** reached stage 31 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-31); NOT reached stage 32 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-32) → **stage 32**; also faction “boat0” set to 9, applies condition drowning. NPC: “Phew, I almost drowned in that puddle!”

???+ note "Stage 60: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Are you crazy?” — **conditions:** reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); NOT reached stage 60 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-60); NOT reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69); NOT carry 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md); NOT wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md) → **stage 60**. NPC: “Then you can climb through a window and reach a path right to the back of the tailor's house.”

???+ note "Stage 61: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Here, take it.” — **conditions:** reached stage 60 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-60); NOT reached stage 61 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-61); NOT reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69); carry 10× [Cooked meat](../items/meat_cooked.md); hand over 10× [Cooked meat](../items/meat_cooked.md) → **stage 61**. NPC: “I knew you would do that, my friend. So I have already hidden the ladder in the basement near the window.”

???+ note "Stage 62: 1 route"

    1. walking into a blocked passage on [catacombs1](../maps/catacombs1.md) → the conversation leads here automatically → **stage 62**. NPC: “Hey, the window won't open. I hope Athamyr has a good excuse for that.”

???+ note "Stage 63: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Here take it. And don't forget to unlock the window.” — **conditions:** reached stage 62 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-62); NOT reached stage 63 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-63); NOT reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69); carry 20× [Cooked meat](../items/meat_cooked.md); hand over 20× [Cooked meat](../items/meat_cooked.md) → **stage 63**; also clears stage 72 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-72). NPC: “The window is already unlocked.”

???+ note "Stage 65: 1 route"

    1. walking into a blocked passage on [fallhaven_clothes](../maps/fallhaven_clothes.md) → choose “Take it.” — **conditions:** reached stage 66 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-66); NOT reached stage 65 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-65) → **stage 65**; also gives 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md). NPC: “Softly, softly now. We don't want to rush the tailor... Got it.”

???+ note "Stage 66: 1 route"

    1. stepping on a trigger on [fallhaven_ne](../maps/fallhaven_ne.md) → the conversation leads here automatically → **stage 66**

???+ note "Stage 68: 3 routes"

    1. Talk to [Tailor](../monsters/tailor.md) ([fallhaven_clothes](../maps/fallhaven_clothes.md)) → the conversation leads here automatically — **conditions:** reached stage 66 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-66) → **stage 68**. NPC: “Hey! What are you doing here? How did you get in?”
    2. stepping on a trigger on [fallhaven_clothes](../maps/fallhaven_clothes.md) → the conversation leads here automatically — **conditions:** reached stage 66 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-66); NOT reached stage 68 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-68); random chance (2%) → **stage 68**. NPC: “Hey! What are you doing here? How did you get in?”
    3. walking into a blocked passage on [fallhaven_clothes](../maps/fallhaven_clothes.md) → the conversation leads here automatically — **conditions:** reached stage 66 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-66); NOT reached stage 68 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-68); random chance (20%) → **stage 68**. NPC: “Hey! What are you doing here? How did you get in?”

???+ note "Stage 69: 2 routes"

    1. stepping on a trigger on [fallhaven_clothes](../maps/fallhaven_clothes.md) → the conversation leads here automatically — **conditions:** NOT reached stage 65 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-65); carry 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md) → **stage 69**
    2. stepping on a trigger on [fallhaven_ne](../maps/fallhaven_ne.md) → the conversation leads here automatically — **conditions:** reached stage 65 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-65) → **stage 69**; also clears stage 73 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-73)

???+ note "Stage 71: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Here, take it.” — **conditions:** reached stage 60 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-60); NOT reached stage 61 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-61); NOT reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69); carry 10× [Cooked meat](../items/meat_cooked.md); hand over 10× [Cooked meat](../items/meat_cooked.md) → **stage 71**. NPC: “I knew you would do that, my friend. So I have already hidden the ladder in the basement near the window.”

???+ note "Stage 72: 1 route"

    1. stepping on a trigger on [catacombs1](../maps/catacombs1.md) → choose “There is the ladder. [Fetch it]” — **conditions:** reached stage 71 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-71) → **stage 72**; also clears stage 71 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-71). NPC: “You place the ladder below the tiny window.”

???+ note "Stage 73: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Here take it. And don't forget to unlock the window.” — **conditions:** reached stage 62 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-62); NOT reached stage 63 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-63); NOT reached stage 69 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-69); carry 20× [Cooked meat](../items/meat_cooked.md); hand over 20× [Cooked meat](../items/meat_cooked.md) → **stage 73**; also clears stage 72 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-72). NPC: “The window is already unlocked.”

???+ note "Stage 80: 3 routes"

    1. Talk to [Godoe](../monsters/godoe1.md) ([guynmart_wood_18](../maps/guynmart_wood_18.md)) → choose “Sure, I have plenty of them.” — **conditions:** hand over 5× [Ruby gem](../items/gem2.md) → **stage 80**; also faction “guynmart18” set to 0. NPC: “Good, good! Here you go. But don't waste time.”
    2. walking into a blocked passage on [guynmart_wood_18](../maps/guynmart_wood_18.md) → choose “Sure, I have plenty of them.” — **conditions:** hand over 5× [Ruby gem](../items/gem2.md) → **stage 80**; also faction “guynmart18” set to 0. NPC: “Good, good! Here you go. But don't waste time.”
    3. walking into a blocked passage on [guynmart_wood_18](../maps/guynmart_wood_18.md) → choose “Sure, I have plenty of them.” — **conditions:** hand over 5× [Ruby gem](../items/gem2.md) → **stage 80**; also faction “guynmart18” set to 0. NPC: “Good, good! Here you go. But don't waste time.”

???+ note "Stage 81: 1 route"

    1. stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) → the conversation leads here automatically — **conditions:** NOT reached stage 81 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-81); timeEquals SS 1 → **stage 81**; also spawns monsters on guynmart_wood_18, removes monsters from guynmart_wood_18

???+ note "Stage 90: 1 route"

    1. stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md) → the conversation leads here automatically → **stage 90**; also clears stage 91 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-91), clears stage 92 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-92)

???+ note "Stage 91: 1 route"

    1. stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) → the conversation leads here automatically → **stage 91**; also clears stage 90 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-90), clears stage 92 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-92)

???+ note "Stage 92: 1 route"

    1. stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) → the conversation leads here automatically → **stage 92**; also clears stage 90 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-90), clears stage 91 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-91), spawns monsters on guynmart_wood_18, spawns monsters on guynmart_wood_18


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 36 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_nondisplayed` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 31, 32, 60, 61, 62, 63, 65, 66, 68, 69, 71, 72, 73, 80, 81, 90, 91, 92 |
    | Dialogue nodes setting stages | 1: `feygard_offering_44`, 2: `wexlow_well_throw_oegyth_crystal`, 3: `gamjee_villagers_unknown_attack`, 4: `gamjee_villagers_known_fight`, 5: `gamjee_villagers_unknown_attack`, 5: `gamjee_villagers_known_fight`, 6: `gamjee_compromise_9`, 7: `village_godwin_lost_ring_take_ring`, 7: `village_godwin_lost_ring_3k`, 7: `village_godwin_lost_ring_give_ring_free`, 8: `rosmara_explain_4`, 9: `village_godelieve_bed`, 10: `leofric_sell`, 11: `wexlow_mother_letter`, 11: `wexlow_godwin_journal`, 12: `village_philippa_fd_complete_no`, 13: `village_godwin_lost_ring_give_ring_free`, 14: `village_godwin_lost_ring_take_ring`, 15: `village_godwin_lost_ring_3k`, 30: `boat0_0a`, 31: `boat0_5a`, 32: `boat0_9a`, 60: `athamyr_coup_24`, 61: `athamyr_coup_28`, 62: `fallhaven_coup_62`, 63: `athamyr_coup_38`, 65: `fallhaven_clothes_coup_30`, 66: `fallhaven_clothes_window_in`, 68: `fallhaven_clothes_10`, 69: `fallhaven_clothes_coup_1`, 69: `fallhaven_clothes_coup_end_10`, 71: `athamyr_coup_28`, 72: `sign_catacombs1_grave3_10`, 73: `athamyr_coup_38`, 80: `godoe_10`, 81: `guynmart18_s1_20`, 90: `guynmart18_passage0`, 91: `guynmart18_passage1`, 92: `guynmart18_passage2` |
    | Dialogue nodes clearing stages | 72: `athamyr_coup_38`, 71: `sign_catacombs1_grave3_10`, 1: `feygard_offering`, 91: `guynmart18_passage0`, 91: `guynmart18_passage2`, 92: `guynmart18_passage0`, 92: `guynmart18_passage1`, 90: `guynmart18_passage1`, 90: `guynmart18_passage2`, 81: `guynmart18_s2_20` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
