---
description: "Not Pony Island is a quest in Andor's Trail, started by Orion, the centaur (island1). 17 stages, 10,000 XP in total. The island west of Remgard was inhabited by centaurs who were very angry about your visit. They told me to seek out their leader, Thalos. He should be in the northeast of the islan…"
---

# Not Pony Island

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lae_centaurs` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 310) |
| **Started by** | [Orion, the centaur](../monsters/lae_centaur1.md) ([Island 1](../maps/island1.md)), [Callista, the centaur](../monsters/lae_centaur2.md) ([Island 2](../maps/island2.md)) |
| **NPCs involved** | [Algangror](../monsters/algangror.md#v-lae_algangror2), [Algangror](../monsters/algangror.md#v-lae_algangror1), [Algangror](../monsters/algangror.md#v-lae_algangror3), [Andor](../monsters/dds_andor.md#v-lae_andor2), [Callista, the centaur](../monsters/lae_centaur2.md), [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld3) +5 |
| **Locations** | [Final cave 1](../maps/final_cave1.md), [Final cave 2](../maps/final_cave2.md), [Island 1](../maps/island1.md), [Island 2](../maps/island2.md) |
| **Total XP** | 10,000 |
| **Related quests** | 1 |

</div>

## Overview

> The island west of Remgard was inhabited by centaurs who were very angry about your visit. They told me to seek out their leader, Thalos. He should be in the northeast of the island.

## Prerequisites to start

None: talk to [Orion, the centaur](../monsters/lae_centaur1.md) ([Island 1](../maps/island1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Final cave (hidden flag)](final_cave.md#stage-1) | stage 1 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-2) | stage 2 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-3) | stage 3 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-4) | stage 4 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-5) | stage 5 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-6) | stage 6 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-7) | stage 7 reached, for stage 150 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-10) | stage 10 reached, for stages 150, 190 here |
| Requires | [Final cave (hidden flag)](final_cave.md#stage-11) | stage 11 reached, for stage 140 here |
| Mutually exclusive | [Final cave (hidden flag)](final_cave.md#stage-9) | stage 9 must NOT be reached, for stage 150 here |
| Mutually exclusive | [Final cave (hidden flag)](final_cave.md#stage-11) | stage 11 must NOT be reached, for stage 130 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">The island west of Remgard was inhabited by centaurs who were very… ▸</span><span class="l">▴ less</span></summary>The island west of Remgard was inhabited by centaurs who were very angry about your visit. They told me to seek out their leader, Thalos. He should be in the northeast of the island.</details> | [Orion, the centaur](../monsters/lae_centaur1.md), [Callista, the centaur](../monsters/lae_centaur2.md) +1 | – |
| <span id="stage-20"></span>[20](#route-20) | I have met Thalos. | [Thalos, the centaur](../monsters/lae_centaur9.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">He ordered me to slay a foul creature that hides in a cave on the… ▸</span><span class="l">▴ less</span></summary>He ordered me to slay a foul creature that hides in a cave on the hills of Laeroth Island, because the centaurs can't enter it.</details> | [Thalos, the centaur](../monsters/lae_centaur9.md) | removes monsters from island4 |
| <span id="stage-110"></span>[110](#route-110) | In the cave entrance I have met Algangror, who asked for help. | [Algangror](../monsters/algangror.md#v-lae_algangror1) | – |
| <span id="stage-112"></span>[112](#route-112) | In a cave entrance I have met Jhaeld of Remgard, who asked for help. | [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1) | – |
| <span id="stage-120"></span>[120](#route-120) | A common friend would be trapped deeper in the cave and I should free him. | [Algangror](../monsters/algangror.md#v-lae_algangror1), [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1) | – |
| <span id="stage-130"></span>[130](#route-130) | <details class="jt"><summary><span class="s">Down in the cave I have found my brother Andor, locked in a room… ▸</span><span class="l">▴ less</span></summary>Down in the cave I have found my brother Andor, locked in a room with no doors or other entrances.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span> | stepping on a trigger on [Final cave 1](../maps/final_cave1.md) | removes monsters from island_4_cave1, removes monsters from island_4_cave1 |
| <span id="stage-140"></span>[140](#route-140) | <details class="jt"><summary><span class="s">To open an entrance I had to find the four scrolls of elements and… ▸</span><span class="l">▴ less</span></summary>To open an entrance I had to find the four scrolls of elements and the three color globes. These were hidden all over the island. The scrolls and globes would need to be properly placed around Andor's golden prison.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span> | stepping on a trigger on [Final cave 1](../maps/final_cave1.md) | – |
| <span id="stage-150"></span>[150](#route-150) | The wall opened and gave access to the interior of the room.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), stepping on a trigger on [Final cave 1](../maps/final_cave1.md) | faction “final_cave_hint” set to 999 |
| <span id="stage-160"></span>[160](#route-160) | With an intense sound, the wall built up again. I've been locked up!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span> | stepping on a trigger on [Final cave 1](../maps/final_cave1.md) | faction “final_cave_e” set to 0 |
| <span id="stage-170"></span>[170](#route-170) | <details class="jt"><summary><span class="s">The only way out was down a staircase, which, however, seemed to be… ▸</span><span class="l">▴ less</span></summary>The only way out was down a staircase, which, however, seemed to be magically secured.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Final cave 1](../maps/final_cave1.md).</span> | [Andor](../monsters/dds_andor.md#v-lae_andor2) | – |
| <span id="stage-180"></span>180 | <details class="jt"><summary><span class="s">The only way out was down a staircase, which, however, seemed to be… ▸</span><span class="l">▴ less</span></summary>The only way out was down a staircase, which, however, seemed to be magically secured.</details> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-190"></span>[190](#route-190) | It was no problem going downstairs, but something was wrong there.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 2](../maps/final_cave2.md).</span> | stepping on a trigger on [Final cave 2](../maps/final_cave2.md) | removes monsters from final_cave1, removes monsters from final_cave1, removes monsters from final_cave1 |
| <span id="stage-200"></span>[200](#route-200) | <details class="jt"><summary><span class="s">The whole thing was just a big scam to lure me into this cave to… ▸</span><span class="l">▴ less</span></summary>The whole thing was just a big scam to lure me into this cave to serve Dorhantarh as dinner.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Final cave 2](../maps/final_cave2.md).</span> | [Algangror](../monsters/algangror.md#v-lae_algangror3) | – |
| <span id="stage-210"></span>[210](#route-210) | <details class="jt"><summary><span class="s">The moment I placed the Scroll of Fire on the table, it exploded. At… ▸</span><span class="l">▴ less</span></summary>The moment I placed the Scroll of Fire on the table, it exploded. At the same time the wall opened again.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 2](../maps/final_cave2.md).</span> | walking into a blocked passage on [Final cave 2](../maps/final_cave2.md), stepping on a trigger on [Final cave 2](../maps/final_cave2.md) | varies by route (see below) |
| <span id="stage-300"></span>[300](#route-300) | <details class="jt"><summary><span class="s">I brought the monster's heart to Thalos and told him that the danger… ▸</span><span class="l">▴ less</span></summary>I brought the monster's heart to Thalos and told him that the danger has been averted. He was impressed and relieved at the same time.</details> | [Thalos, the centaur](../monsters/lae_centaur9.md) | – |
| <span id="stage-310"></span>[310](#route-310) | Since then I have been a welcome guest of the centaurs. **(ends quest)** | [Thalos, the centaur](../monsters/lae_centaur9.md) | 10,000 XP |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Orion, the centaur, Callista, the centaur, Silvanus, the cen · 3 ways"

    **Way 1:** Talk to [Orion, the centaur](../monsters/lae_centaur1.md), choose “Then just tell me where he is.”

    - <small>Also: sets stage 211 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-211)</small>
    - *“Thalos, our wise guide, is currently in the northeast of the island.”*

    **Way 2:** Talk to [Callista, the centaur](../monsters/lae_centaur2.md), choose “Fine, I'll go see him.”

    - <small>Also: sets stage 212 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-212)</small>
    - *“Thalos, our wise guide, is currently in the northeast of the island.”*

    **Way 3:** Talk to [Silvanus, the centaur](../monsters/lae_centaur3.md), choose “Enough now. I want to speak to your boss.”

    - <small>Also: sets stage 213 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-213)</small>
    - *“Thalos, our wise guide, is currently in the northeast of the island.”*


<span id="route-20"></span>

??? note "Stage 20 · Thalos, the centaur · 1 way"

    **Way 1:** Talk to [Thalos, the centaur](../monsters/lae_centaur9.md), automatic

    - *“I am Thalos. Human, you are not welcome here.”*


<span id="route-30"></span>

??? note "Stage 30 · Thalos, the centaur · 1 way"

    **Way 1:** Talk to [Thalos, the centaur](../monsters/lae_centaur9.md), automatic

    - **Needs:** stage 30
    - **Gives:** removes monsters from island4
    - *“Go and slay this beast. Then I will reconsider your intentions.”*


<span id="route-110"></span>

??? note "Stage 110 · Algangror · 1 way"

    **Way 1:** Talk to [Algangror](../monsters/algangror.md#v-lae_algangror1), automatic

    - *“$playername - good that you are here! I need your help urgently.”*


<span id="route-112"></span>

??? note "Stage 112 · Jhaeld · 1 way"

    **Way 1:** Talk to [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1), automatic

    - *“$playername - good that you are here! I need your help urgently.”*


<span id="route-120"></span>

??? note "Stage 120 · Algangror, Jhaeld · 2 ways"

    **Way 1:** Talk to [Algangror](../monsters/algangror.md#v-lae_algangror1), choose “So how can I help you?”

    - *“You know him very well by the way. We have to help him!”*

    **Way 2:** Talk to [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1), choose “Why? Don't coming around on your own anymore?”

    - *“You know him very well by the way. We have to help him!”*


<span id="route-130"></span>

??? note "Stage 130 · stepping on a trigger on final_cave1 · 1 way"

    **Way 1:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md), choose “What?!”

    - **Needs:** not yet stage 150; not reached stage 11 of [Final cave (hidden flag)](../quests/final_cave.md#stage-11); random chance (25%)
    - **Gives:** removes monsters from island_4_cave1, removes monsters from island_4_cave1
    - <small>Also: sets stage 11 of [Final cave (hidden flag)](../quests/final_cave.md#stage-11)</small>
    - *“I entered this room to find a powerful weapon against the enemy, when suddenly the walls closed around me.”*


<span id="route-140"></span>

??? note "Stage 140 · stepping on a trigger on final_cave1 · 1 way"

    **Way 1:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md), choose “Can you be a little more specific?”

    - **Needs:** not yet stage 150; reached stage 11 of [Final cave (hidden flag)](../quests/final_cave.md#stage-11)
    - *“There are four scrolls and three globes. Get them here and place them around this room.”*


<span id="route-150"></span>

??? note "Stage 150 · walking into a blocked passage on final_cave1, stepping on a · 8 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** reached stage 1 of [Final cave (hidden flag)](../quests/final_cave.md#stage-1); faction “final_cave_f” = 1; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** reached stage 2 of [Final cave (hidden flag)](../quests/final_cave.md#stage-2); faction “final_cave_r” = 2; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** reached stage 3 of [Final cave (hidden flag)](../quests/final_cave.md#stage-3); faction “final_cave_f” = 3; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** reached stage 4 of [Final cave (hidden flag)](../quests/final_cave.md#stage-4); faction “final_cave_r” = 4; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 5:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** reached stage 5 of [Final cave (hidden flag)](../quests/final_cave.md#stage-5); faction “final_cave_f” = 5; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 6:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** reached stage 6 of [Final cave (hidden flag)](../quests/final_cave.md#stage-6); faction “final_cave_r” = 6; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 7:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** reached stage 7 of [Final cave (hidden flag)](../quests/final_cave.md#stage-7); faction “final_cave_f” = 7; not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*

    **Way 8:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md)

    - **Needs:** reached stage 10 of [Final cave (hidden flag)](../quests/final_cave.md#stage-10); not reached stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air!”*


<span id="route-160"></span>

??? note "Stage 160 · stepping on a trigger on final_cave1 · 1 way"

    **Way 1:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md)

    - **Gives:** faction “final_cave_e” set to 0
    - <small>Also: clears stage 1 of [Final cave (hidden flag)](../quests/final_cave.md#stage-1)</small>


<span id="route-170"></span>

??? note "Stage 170 · Andor · 1 way"

    **Way 1:** Talk to [Andor](../monsters/dds_andor.md#v-lae_andor2), choose “What is down there?”

    - *“We can't use those stairs. Some invisible force holds us back. But maybe you can do it?”*


<span id="route-190"></span>

??? note "Stage 190 · stepping on a trigger on final_cave2 · 1 way"

    **Way 1:** Stepping on a trigger on [Final cave 2](../maps/final_cave2.md)

    - **Needs:** reached stage 10 of [Final cave (hidden flag)](../quests/final_cave.md#stage-10)
    - **Gives:** removes monsters from final_cave1, removes monsters from final_cave1, removes monsters from final_cave1
    - *“You call back upstairs that there was no problem going down.”*


<span id="route-200"></span>

??? note "Stage 200 · Algangror · 1 way"

    **Way 1:** Talk to [Algangror](../monsters/algangror.md#v-lae_algangror3), automatic

    - **Needs:** stage 200
    - *“Now go ahead, you'll be a tasty dinner for our master Dorhantarh tonight.”*


<span id="route-210"></span>

??? note "Stage 210 · walking into a blocked passage on final_cave2, stepping on a · 2 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 2](../maps/final_cave2.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_e” set to 0, faction “final_cave_g” set to 0, faction “final_cave_f” set to 0, faction “final_cave_b” set to 0, faction “final_cave_a” set to 0, faction “final_cave_r” set to 0, faction “final_cave_w” set to 0, faction “final_cave_hint” set to 999, applies condition bleeding_wound
    - <small>Also: clears stage 1 of [Final cave (hidden flag)](../quests/final_cave.md#stage-1), clears stage 2 of [Final cave (hidden flag)](../quests/final_cave.md#stage-2), clears stage 3 of [Final cave (hidden flag)](../quests/final_cave.md#stage-3), clears stage 4 of [Final cave (hidden flag)](../quests/final_cave.md#stage-4), clears stage 5 of [Final cave (hidden flag)](../quests/final_cave.md#stage-5), clears stage 6 of [Final cave (hidden flag)](../quests/final_cave.md#stage-6), clears stage 7 of [Final cave (hidden flag)](../quests/final_cave.md#stage-7), sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“A loud rumbling fills the air! - At the same time the scroll of fire explodes.”*

    **Way 2:** Stepping on a trigger on [Final cave 2](../maps/final_cave2.md)

    - **Needs:** not yet stage 210; killed 123× [Dorhantarh](../monsters/lae_island_boss.md)
    - **Gives:** faction “final_cave_hint” set to 999
    - <small>Also: sets stage 9 of [Final cave (hidden flag)](../quests/final_cave.md#stage-9)</small>
    - *“You hear a loud rumbling from above. Seems to be the walls are opened up again.”*


<span id="route-300"></span>

??? note "Stage 300 · Thalos, the centaur · 1 way"

    **Way 1:** Talk to [Thalos, the centaur](../monsters/lae_centaur9.md), automatic

    - **Needs:** stage 300
    - *“That foul creature is no more. A great burden is lifted from my heart.”*


<span id="route-310"></span>

??? note "Stage 310 · Thalos, the centaur · 1 way"

    **Way 1:** Talk to [Thalos, the centaur](../monsters/lae_centaur9.md), automatic

    - **Needs:** stage 310
    - *“You have proven yourself to be more than just another ignorant human.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 19 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lae_centaurs` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 110, 112, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 300, 310 |
    | Dialogue nodes setting stages | 10: `lae_centaur1_8`, 10: `lae_centaur2_8`, 10: `lae_centaur3_8`, 20: `lae_centaur9_1`, 30: `lae_centaur9_30`, 110: `lae_algangror1`, 112: `lae_jhaeld1`, 120: `lae_algangror1_22`, 130: `lae_andor1_42`, 140: `lae_andor1_60`, 150: `final_cave_kx_open`, 160: `final_cave_s9`, 170: `lae_algangror2_50`, 190: `lae_fc2_s1_10`, 200: `lae_algangror3_40`, 210: `final_cave2_k1_10_f`, 210: `lae_fc2_s1_6`, 300: `lae_centaur9_302`, 310: `lae_centaur9_310` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
