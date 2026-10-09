---
description: "Feygard story flags is a hidden quest in Andor's Trail, started by walking into a blocked passage on guynmart_wood_16. 35 stages, 1,101 XP in total. 1=Stolen from offering to Elythara"
---

# Feygard story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_nondisplayed` |
| **In journal** | No (hidden flag) |
| **Stages** | 35 |
| **Started by** | walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) |
| **NPCs involved** | [Athamyr](../monsters/athamyr.md), [Gamjee](../monsters/gamjee.md), [Gamjee](../monsters/gamjee.md#v-gamjee_oc), [Godelieve](../monsters/village_godelieve.md), [Godoe](../monsters/godoe1.md#v-godoe2), [Godoe](../monsters/godoe1.md) +5 |
| **Locations** | [Beekeeper 1](../maps/beekeeper1.md), [Fallhaven clothes](../maps/fallhaven_clothes.md), [Gamjee well 4 1](../maps/gamjee_well_4_1.md), [Guynmart wood 18](../maps/guynmart_wood_18.md) |
| **Total XP** | 1,101 |
| **Related quests** | 3 |

</div>

## Overview

> 1=Stolen from offering to Elythara

## Prerequisites to start

Start with walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md). Required:

- faction “feygard_offering_sum” ≥ 1
- reached stage 1 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-1)


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

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | 1=Stolen from offering to Elythara | walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md) | applies condition stunned, applies condition bone_fracture, spawns monsters on guynmart_wood_16, applies condition elytharabless_heal |
| <span id="stage-2"></span>[2](#route-2) | The PC threw an Oegyth Crystal down the well in Wexlow Village.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wexlow village](../maps/wexlow_village.md).</span> | stepping on a trigger on [Wexlow village](../maps/wexlow_village.md) | spawns monsters on gamjee_well_4_1, removes monsters from gamjee_well_4_1 |
| <span id="stage-3"></span>[3](#route-3) | <details class="jt"><summary><span class="s">The PC has attacked Gamjee the troll under the village of Wexlow… ▸</span><span class="l">▴ less</span></summary>The PC has attacked Gamjee the troll under the village of Wexlow without knowing that Gamjee has those villagers held captive.</details> | [Gamjee](../monsters/gamjee.md) | – |
| <span id="stage-4"></span>[4](#route-4) | <details class="jt"><summary><span class="s">The PC has attacked Gamjee the troll under the village of Wexlow… ▸</span><span class="l">▴ less</span></summary>The PC has attacked Gamjee the troll under the village of Wexlow after learning that Gamjee has those villagers held captive.</details> | [Gamjee](../monsters/gamjee.md) | – |
| <span id="stage-5"></span>[5](#route-5) | The PC has attacked Gamjee the troll under the village of Wexlow. | [Gamjee](../monsters/gamjee.md) | – |
| <span id="stage-6"></span>[6](#route-6) | <details class="jt"><summary><span class="s">Gamjee, the troll under the village of Wexlow has sent the villager… ▸</span><span class="l">▴ less</span></summary>Gamjee, the troll under the village of Wexlow has sent the villager back to Wexlow.</details> | [Gamjee](../monsters/gamjee.md) | removes monsters from gamjee_well_4_1, sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12), spawns monsters on wexlow_village |
| <span id="stage-7"></span>[7](#route-7) | PC gave Godwin, a villager from Wexlow, his lost ring. [wrapper for 13, 14, 15] | [Godwin](../monsters/village_godwin.md) | varies by route (see below) |
| <span id="stage-8"></span>[8](#route-8) | PC learns that Rosmara sells fruits and vegetables | [Rosmara](../monsters/rosmara.md) | – |
| <span id="stage-9"></span>[9](#route-9) | PC can sleep in Wexlow Village.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wexlow village north-west house](../maps/wexlow_village_nw_house.md).</span> | [Godelieve](../monsters/village_godelieve.md) | – |
| <span id="stage-10"></span>[10](#route-10) | PC has learned what the beekeeper, Leofric does for work. | [Leofric](../monsters/leofric.md) | – |
| <span id="stage-11"></span>[11](#route-11) | In Wexlow Village, the PC has learned that there are missing residents. | walking into a blocked passage on [Wexlow village north house](../maps/wexlow_village_n_house.md), walking into a blocked passage on [Wexlow village north-west house](../maps/wexlow_village_nw_house.md) | – |
| <span id="stage-12"></span>[12](#route-12) | PC is not being patient while waiting for the Feydelight to be cooked. | [Philippa](../monsters/village_philippa.md) | – |
| <span id="stage-13"></span>[13](#route-13) | PC gave Godwin, a villager from Wexlow, his lost ring for free. | [Godwin](../monsters/village_godwin.md) | 1,000 XP, 100× [Gold coins](../items/gold.md) |
| <span id="stage-14"></span>[14](#route-14) | PC gave Godwin, a villager from Wexlow, his lost ring for 2k gold. | [Godwin](../monsters/village_godwin.md) | 100 XP, 2000× [Gold coins](../items/gold.md) |
| <span id="stage-15"></span>[15](#route-15) | PC gave Godwin, a villager from Wexlow, his lost ring for 3k gold. | [Godwin](../monsters/village_godwin.md) | 1 XP, 3000× [Gold coins](../items/gold.md) |
| <span id="stage-20"></span>20 | 20=Road to Feygard closed (wayto_feygard_duleian_2)<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wayto feygard duleian 2](../maps/wayto_feygard_duleian_2.md).</span> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-30"></span>[30](#route-30) | boat0 clear<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md) | faction “boat0” set to 1 |
| <span id="stage-31"></span>[31](#route-31) | boat0 sunk<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md) | faction “boat0” set to 5, applies condition drowning |
| <span id="stage-32"></span>[32](#route-32) | boat0 save<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfillerhole](../maps/gapfillerhole.md).</span> | stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md) | faction “boat0” set to 9, applies condition drowning |
| <span id="stage-60"></span>[60](#route-60) | 60=talked to Arthamyr | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-61"></span>[61](#route-61) | 61=ladder placed | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-62"></span>[62](#route-62) | 62=tried window | walking into a blocked passage on [Catacombs 1](../maps/catacombs1.md) | – |
| <span id="stage-63"></span>[63](#route-63) | 63=church window unlocked | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-65"></span>[65](#route-65) | 65=jewel taken | walking into a blocked passage on [Fallhaven clothes](../maps/fallhaven_clothes.md) | 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md) |
| <span id="stage-66"></span>[66](#route-66) | 66=passed window towards tailor<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven north-east](../maps/fallhaven_ne.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span> | stepping on a trigger on [Fallhaven north-east](../maps/fallhaven_ne.md) | – |
| <span id="stage-68"></span>[68](#route-68) | 68=seen<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span> | [Tailor](../monsters/tailor.md), stepping on a trigger on [Fallhaven clothes](../maps/fallhaven_clothes.md) +1 | – |
| <span id="stage-69"></span>[69](#route-69) | 69=closed<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven clothes](../maps/fallhaven_clothes.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven north-east](../maps/fallhaven_ne.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven north-west](../maps/fallhaven_nw.md).</span> | stepping on a trigger on [Fallhaven clothes](../maps/fallhaven_clothes.md), stepping on a trigger on [Fallhaven north-east](../maps/fallhaven_ne.md) | – |
| <span id="stage-71"></span>[71](#route-71) | 71=ladder place 1<br><span class="qnote">🗺️ Part of [Catacombs 1](../maps/catacombs1.md) visibly changes.</span> | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-72"></span>[72](#route-72) | 72=ladder place 2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Catacombs 1](../maps/catacombs1.md).</span><br><span class="qnote">🗺️ Part of [Catacombs 1](../maps/catacombs1.md) visibly changes.</span> | stepping on a trigger on [Catacombs 1](../maps/catacombs1.md) | – |
| <span id="stage-73"></span>[73](#route-73) | 73=windows church unlocked from inside<br><span class="qnote">🔓 You can finally access a previously blocked area on [Catacombs 1](../maps/catacombs1.md).</span><br><span class="qnote">🗺️ Part of [Catacombs 1](../maps/catacombs1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Fallhaven clothes](../maps/fallhaven_clothes.md) visibly changes.</span> | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-80"></span>[80](#route-80) | 80=Path open<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | [Godoe](../monsters/godoe1.md), walking into a blocked passage on [Guynmart wood 18](../maps/guynmart_wood_18.md) | faction “guynmart18” set to 0 |
| <span id="stage-81"></span>[81](#route-81) | 81=Godoe in the south<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18b](../maps/guynmart_wood_18b.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 18c](../maps/guynmart_wood_18c.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span> | stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md) | spawns monsters on guynmart_wood_18, removes monsters from guynmart_wood_18 |
| <span id="stage-90"></span>[90](#route-90) | 90=Ravine blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17b](../maps/guynmart_wood_17b.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 19](../maps/guynmart_wood_19.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md) | – |
| <span id="stage-91"></span>[91](#route-91) | 91=Ravine outlets blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md) | – |
| <span id="stage-92"></span>[92](#route-92) | 92=Ravine free<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 18](../maps/guynmart_wood_18.md) visibly changes.</span> | stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md) | spawns monsters on guynmart_wood_18, spawns monsters on guynmart_wood_18 |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · walking into a blocked passage on guynmart_wood_16 · 1 way"

    **Way 1:** Walking into a blocked passage on [Guynmart wood 16](../maps/guynmart_wood_16.md), choose “Take 1 gold coin.”

    - **Needs:** stage 1; faction “feygard_offering_sum” ≥ 1
    - **Gives:** applies condition stunned, applies condition bone_fracture, spawns monsters on guynmart_wood_16, applies condition elytharabless_heal
    - *“Elythara is known for her thirst for revenge. Fear her wrath!”*


<span id="route-2"></span>

??? note "Stage 2 · stepping on a trigger on wexlow_village · 1 way"

    **Way 1:** Stepping on a trigger on [Wexlow village](../maps/wexlow_village.md), choose “[Throw an Oegyth Crystal]”

    - **Needs:** not yet stage 2; not reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10); not reached stage 11 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11); not reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); not reached stage 9 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9); hand over 1× [Oegyth crystal](../items/oegyth.md)
    - **Gives:** spawns monsters on gamjee_well_4_1, removes monsters from gamjee_well_4_1
    - *“Glowing thing... pretty, but useless! Gamjee no care for it!”*


<span id="route-3"></span>

??? note "Stage 3 · Gamjee · 1 way"

    **Way 1:** Talk to [Gamjee](../monsters/gamjee.md), choose “I don't believe you! Prove it.”

    - **Needs:** not reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); not reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); not reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)
    - *“No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”*


<span id="route-4"></span>

??? note "Stage 4 · Gamjee · 1 way"

    **Way 1:** Talk to [Gamjee](../monsters/gamjee.md), choose “It's time to make me righteous!”

    - **Needs:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); not reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)
    - *“No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”*


<span id="route-5"></span>

??? note "Stage 5 · Gamjee · 2 ways"

    **Way 1:** Talk to [Gamjee](../monsters/gamjee.md), choose “I don't believe you! Prove it.”

    - **Needs:** not reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); not reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); not reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)
    - *“No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”*

    **Way 2:** Talk to [Gamjee](../monsters/gamjee.md), choose “It's time to make me righteous!”

    - **Needs:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); not reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)
    - *“No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.”*


<span id="route-6"></span>

??? note "Stage 6 · Gamjee · 1 way"

    **Way 1:** Talk to [Gamjee](../monsters/gamjee.md), choose “Alright. Let's make this work.”

    - **Needs:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); not reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); not reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12)
    - **Gives:** removes monsters from gamjee_well_4_1, sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12), spawns monsters on wexlow_village
    - *“You human, go back village now.”*


<span id="route-7"></span>

??? note "Stage 7 · Godwin · 3 ways"

    **Way 1:** Talk to [Godwin](../monsters/village_godwin.md), choose “Sounds good.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 2000× [Gold coins](../items/gold.md)
    - *“Thank you so much! Here take these coins.”*

    **Way 2:** Talk to [Godwin](../monsters/village_godwin.md), choose “3,000 gold or no ring.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 3000× [Gold coins](../items/gold.md)
    - *“Fine! Take the coins you thief.”*

    **Way 3:** Talk to [Godwin](../monsters/village_godwin.md), choose “Sure. Here, it's yours.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 100× [Gold coins](../items/gold.md)
    - *“Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.”*


<span id="route-8"></span>

??? note "Stage 8 · Rosmara · 1 way"

    **Way 1:** Talk to [Rosmara](../monsters/rosmara.md), choose “What is it?”

    - *“I sell fruits and vegetables.”*


<span id="route-9"></span>

??? note "Stage 9 · Godelieve · 1 way"

    **Way 1:** Talk to [Godelieve](../monsters/village_godelieve.md), choose “Would it be OK with you if I slept here? I'm pretty tired.”

    - **Needs:** reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12)
    - *“Of course. Just use the mat over there in the corner.”*


<span id="route-10"></span>

??? note "Stage 10 · Leofric · 1 way"

    **Way 1:** Talk to [Leofric](../monsters/leofric.md), choose “Do you have anything for sale?”

    - *“Aye, I have many wares to offer. Jars of honey, beeswax and some fine mead. But that's it for now as my supply is lower than normal. Take…”*


<span id="route-11"></span>

??? note "Stage 11 · walking into a blocked passage on wexlow_village_n_house, wa · 2 ways"

    **Way 1:** Walking into a blocked passage on [Wexlow village north house](../maps/wexlow_village_n_house.md), choose “I sure do.”

    - **Needs:** not reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10)
    - *“Dear Theodora, I've come to visit you again today, but once more, I find your home empty. It's been nearly a month since I last saw you,…”*

    **Way 2:** Walking into a blocked passage on [Wexlow village north-west house](../maps/wexlow_village_nw_house.md), choose “I think I should.”

    - **Needs:** not reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10)
    - *“It's been days since anyone has seen Odilia. At first, we thought she might have gone to visit her sister in Feygard, but she never…”*


<span id="route-12"></span>

??? note "Stage 12 · Philippa · 1 way"

    **Way 1:** Talk to [Philippa](../monsters/village_philippa.md), choose “I am wondering, is my Feydelight ready yet?”

    - **Needs:** not yet stage 12; latest stage of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) is 7
    - *“Sorry, no it is not. Please come back later.”*


<span id="route-13"></span>

??? note "Stage 13 · Godwin · 1 way"

    **Way 1:** Talk to [Godwin](../monsters/village_godwin.md), choose “Sure. Here, it's yours.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 100× [Gold coins](../items/gold.md)
    - *“Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.”*


<span id="route-14"></span>

??? note "Stage 14 · Godwin · 1 way"

    **Way 1:** Talk to [Godwin](../monsters/village_godwin.md), choose “Sounds good.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 2000× [Gold coins](../items/gold.md)
    - *“Thank you so much! Here take these coins.”*


<span id="route-15"></span>

??? note "Stage 15 · Godwin · 1 way"

    **Way 1:** Talk to [Godwin](../monsters/village_godwin.md), choose “3,000 gold or no ring.”

    - **Needs:** not yet stage 7; carry 1× [Godwin's ring](../items/godwin_ring.md); hand over 1× [Godwin's ring](../items/godwin_ring.md)
    - **Gives:** 3000× [Gold coins](../items/gold.md)
    - *“Fine! Take the coins you thief.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on gapfillerhole · 1 way"

    **Way 1:** Stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md)

    - **Needs:** not yet stage 30
    - **Gives:** faction “boat0” set to 1


<span id="route-31"></span>

??? note "Stage 31 · stepping on a trigger on gapfillerhole · 1 way"

    **Way 1:** Stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md)

    - **Needs:** not yet stage 31
    - **Gives:** faction “boat0” set to 5, applies condition drowning
    - *“The boat seems to have a leak!”*


<span id="route-32"></span>

??? note "Stage 32 · stepping on a trigger on gapfillerhole · 1 way"

    **Way 1:** Stepping on a trigger on [Gapfillerhole](../maps/gapfillerhole.md)

    - **Needs:** stage 31; not yet stage 32
    - **Gives:** faction “boat0” set to 9, applies condition drowning
    - *“Phew, I almost drowned in that puddle!”*


<span id="route-60"></span>

??? note "Stage 60 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Are you crazy?”

    - **Needs:** not yet stage 60, 69; reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); not carry 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md); not wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md)
    - *“Then you can climb through a window and reach a path right to the back of the tailor's house.”*


<span id="route-61"></span>

??? note "Stage 61 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Here, take it.”

    - **Needs:** stage 60; not yet stage 61, 69; carry 10× [Cooked meat](../items/meat_cooked.md); hand over 10× [Cooked meat](../items/meat_cooked.md)
    - *“I knew you would do that, my friend. So I have already hidden the ladder in the basement near the window.”*


<span id="route-62"></span>

??? note "Stage 62 · walking into a blocked passage on catacombs1 · 1 way"

    **Way 1:** Walking into a blocked passage on [Catacombs 1](../maps/catacombs1.md)

    - *“Hey, the window won't open. I hope Athamyr has a good excuse for that.”*


<span id="route-63"></span>

??? note "Stage 63 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Here take it. And don't forget to unlock the window.”

    - **Needs:** stage 62; not yet stage 63, 69; carry 20× [Cooked meat](../items/meat_cooked.md); hand over 20× [Cooked meat](../items/meat_cooked.md)
    - <small>Also: clears stage 72 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-72)</small>
    - *“The window is already unlocked.”*


<span id="route-65"></span>

??? note "Stage 65 · walking into a blocked passage on fallhaven_clothes · 1 way"

    **Way 1:** Walking into a blocked passage on [Fallhaven clothes](../maps/fallhaven_clothes.md), choose “Take it.”

    - **Needs:** stage 66; not yet stage 65
    - **Gives:** 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md)
    - *“Softly, softly now. We don't want to rush the tailor... Got it.”*


<span id="route-66"></span>

??? note "Stage 66 · stepping on a trigger on fallhaven_ne · 1 way"

    **Way 1:** Stepping on a trigger on [Fallhaven north-east](../maps/fallhaven_ne.md)



<span id="route-68"></span>

??? note "Stage 68 · Tailor, stepping on a trigger on fallhaven_clothes, walking  · 3 ways"

    **Way 1:** Talk to [Tailor](../monsters/tailor.md), automatic

    - **Needs:** stage 66
    - *“Hey! What are you doing here? How did you get in?”*

    **Way 2:** Stepping on a trigger on [Fallhaven clothes](../maps/fallhaven_clothes.md)

    - **Needs:** stage 66; not yet stage 68; random chance (2%)
    - *“Hey! What are you doing here? How did you get in?”*

    **Way 3:** Walking into a blocked passage on [Fallhaven clothes](../maps/fallhaven_clothes.md)

    - **Needs:** stage 66; not yet stage 68; random chance (20%)
    - *“Hey! What are you doing here? How did you get in?”*


<span id="route-69"></span>

??? note "Stage 69 · stepping on a trigger on fallhaven_clothes, stepping on a tr · 2 ways"

    **Way 1:** Stepping on a trigger on [Fallhaven clothes](../maps/fallhaven_clothes.md)

    - **Needs:** not yet stage 65; carry 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md)

    **Way 2:** Stepping on a trigger on [Fallhaven north-east](../maps/fallhaven_ne.md)

    - **Needs:** stage 65
    - <small>Also: clears stage 73 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-73)</small>


<span id="route-71"></span>

??? note "Stage 71 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Here, take it.”

    - **Needs:** stage 60; not yet stage 61, 69; carry 10× [Cooked meat](../items/meat_cooked.md); hand over 10× [Cooked meat](../items/meat_cooked.md)
    - *“I knew you would do that, my friend. So I have already hidden the ladder in the basement near the window.”*


<span id="route-72"></span>

??? note "Stage 72 · stepping on a trigger on catacombs1 · 1 way"

    **Way 1:** Stepping on a trigger on [Catacombs 1](../maps/catacombs1.md), choose “There is the ladder. [Fetch it]”

    - **Needs:** stage 71
    - <small>Also: clears stage 71 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-71)</small>
    - *“You place the ladder below the tiny window.”*


<span id="route-73"></span>

??? note "Stage 73 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Here take it. And don't forget to unlock the window.”

    - **Needs:** stage 62; not yet stage 63, 69; carry 20× [Cooked meat](../items/meat_cooked.md); hand over 20× [Cooked meat](../items/meat_cooked.md)
    - <small>Also: clears stage 72 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-72)</small>
    - *“The window is already unlocked.”*


<span id="route-80"></span>

??? note "Stage 80 · Godoe, walking into a blocked passage on guynmart_wood_18 · 3 ways"

    **Way 1:** Talk to [Godoe](../monsters/godoe1.md), choose “Sure, I have plenty of them.”

    - **Needs:** hand over 5× [Ruby gem](../items/gem2.md)
    - **Gives:** faction “guynmart18” set to 0
    - *“Good, good! Here you go. But don't waste time.”*

    **Way 2:** Walking into a blocked passage on [Guynmart wood 18](../maps/guynmart_wood_18.md), choose “Sure, I have plenty of them.”

    - **Needs:** hand over 5× [Ruby gem](../items/gem2.md)
    - **Gives:** faction “guynmart18” set to 0
    - *“Good, good! Here you go. But don't waste time.”*

    **Way 3:** Walking into a blocked passage on [Guynmart wood 18](../maps/guynmart_wood_18.md), choose “Sure, I have plenty of them.”

    - **Needs:** hand over 5× [Ruby gem](../items/gem2.md)
    - **Gives:** faction “guynmart18” set to 0
    - *“Good, good! Here you go. But don't waste time.”*


<span id="route-81"></span>

??? note "Stage 81 · stepping on a trigger on guynmart_wood_18 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md)

    - **Needs:** not yet stage 81; timeEquals SS 1
    - **Gives:** spawns monsters on guynmart_wood_18, removes monsters from guynmart_wood_18


<span id="route-90"></span>

??? note "Stage 90 · stepping on a trigger on guynmart_wood_17 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md)

    - <small>Also: clears stage 91 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-91), clears stage 92 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-92)</small>


<span id="route-91"></span>

??? note "Stage 91 · stepping on a trigger on guynmart_wood_18 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md)

    - <small>Also: clears stage 90 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-90), clears stage 92 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-92)</small>


<span id="route-92"></span>

??? note "Stage 92 · stepping on a trigger on guynmart_wood_18 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md)

    - **Gives:** spawns monsters on guynmart_wood_18, spawns monsters on guynmart_wood_18
    - <small>Also: clears stage 90 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-90), clears stage 91 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-91)</small>



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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_nondisplayed` |
    | Name in game data | `feygard_nondisplayed` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 31, 32, 60, 61, 62, 63, 65, 66, 68, 69, 71, 72, 73, 80, 81, 90, 91, 92 |
    | Dialogue nodes setting stages | 1: `feygard_offering_44`, 2: `wexlow_well_throw_oegyth_crystal`, 3: `gamjee_villagers_unknown_attack`, 4: `gamjee_villagers_known_fight`, 5: `gamjee_villagers_unknown_attack`, 5: `gamjee_villagers_known_fight`, 6: `gamjee_compromise_9`, 7: `village_godwin_lost_ring_take_ring`, 7: `village_godwin_lost_ring_3k`, 7: `village_godwin_lost_ring_give_ring_free`, 8: `rosmara_explain_4`, 9: `village_godelieve_bed`, 10: `leofric_sell`, 11: `wexlow_mother_letter`, 11: `wexlow_godwin_journal`, 12: `village_philippa_fd_complete_no`, 13: `village_godwin_lost_ring_give_ring_free`, 14: `village_godwin_lost_ring_take_ring`, 15: `village_godwin_lost_ring_3k`, 30: `boat0_0a`, 31: `boat0_5a`, 32: `boat0_9a`, 60: `athamyr_coup_24`, 61: `athamyr_coup_28`, 62: `fallhaven_coup_62`, 63: `athamyr_coup_38`, 65: `fallhaven_clothes_coup_30`, 66: `fallhaven_clothes_window_in`, 68: `fallhaven_clothes_10`, 69: `fallhaven_clothes_coup_1`, 69: `fallhaven_clothes_coup_end_10`, 71: `athamyr_coup_28`, 72: `sign_catacombs1_grave3_10`, 73: `athamyr_coup_38`, 80: `godoe_10`, 81: `guynmart18_s1_20`, 90: `guynmart18_passage0`, 91: `guynmart18_passage1`, 92: `guynmart18_passage2` |
    | Dialogue nodes clearing stages | 72: `athamyr_coup_38`, 71: `sign_catacombs1_grave3_10`, 1: `feygard_offering`, 91: `guynmart18_passage0`, 91: `guynmart18_passage2`, 92: `guynmart18_passage0`, 92: `guynmart18_passage1`, 90: `guynmart18_passage1`, 90: `guynmart18_passage2`, 81: `guynmart18_s2_20` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
