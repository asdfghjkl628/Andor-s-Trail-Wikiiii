---
description: "Roses is a quest in Andor's Trail, started by Rhodita (guynmart_wood_1). 41 stages, 10,027 XP in total. On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is worried about young Lady Hannah of Guynmart, who used to visit often but has not been seen for a week now. Rhodita asked me to…"
---

# Roses

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart` |
| **In journal** | Yes |
| **Stages** | 41 (completes at 210, 211) |
| **Started by** | [Rhodita](../monsters/guynmart_farmer.md) ([Guynmart wood 1](../maps/guynmart_wood_1.md)) |
| **NPCs involved** | [Armor](../monsters/guynmart_reward3.md), [Gold](../monsters/guynmart_reward1.md), [Guynmart](../monsters/guynmart.md), [Guynmart guard](../monsters/guynmart_gguard.md), [Guynmart guard](../monsters/guynmart_gguard.md#v-guynmart_guard_guide), [Hannah](../monsters/guynmart_hannah.md) +16 |
| **Locations** | [Guynmart](../maps/guynmart.md), [Guynmart main 0](../maps/guynmart_main_0.md), [Guynmart main 1](../maps/guynmart_main_1.md), [Guynmart main 2](../maps/guynmart_main_2.md) |
| **Total XP** | 10,027 |
| **Related quests** | 6 |

</div>

## Overview

> On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is worried about young Lady Hannah of Guynmart, who used to visit often but has not been seen for a week now. Rhodita asked me to check on her.

## Prerequisites to start

None: talk to [Rhodita](../monsters/guynmart_farmer.md) ([Guynmart wood 1](../maps/guynmart_wood_1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-32) | stage 32 reached, for stages 210, 211 here |
| Blocked by | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-2) | stage 2 must NOT be reached, for stage 164 here |
| Blocked by | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-32) | stage 32 must NOT be reached, for stages 201, 202, 203 here |
| Blocked by | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-33) | stage 33 must NOT be reached, for stages 210, 211 here |
| Unlocks | [Search for Andor](andor.md#stage-92) | stage 92 there needs stage 161 here |
| Unlocks | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-2) | stage 2 there needs stage 170 here |
| Unlocks | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-33) | stage 33 there needs stages 181, 190 here |
| Unlocks | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-36) | stage 36 there needs stages 181, 190 here |
| Unlocks | [Guynmart story flags (hidden flag)](guynmart_nondisplay.md#stage-60) | stage 60 there needs stages 161, 170 here |
| Unlocks | [Guynmart quest cook bread (hidden flag)](guynmart_quest_cook_bread.md#stage-1) | stage 1 there needs stages 40, 62 here |
| Unlocks | [Guynmart garden guard (hidden flag)](guynmart_quest_gguard.md#stage-1) | stage 1 there needs stage 30 here |
| Unlocks | [Guynmart garden guard (hidden flag)](guynmart_quest_gguard.md#stage-82) | stage 82 there needs stage 70 here |
| Unlocks | [Guest tour (hidden flag)](guynmart_quest_olav.md#stage-7) | stage 7 there needs stage 80 here |
| Unlocks | [Guynmart rope (hidden flag)](guynmart_r_rope.md#stage-11) | stage 11 there needs stage 80 here |
| Blocks | [Guynmart quest cook bread (hidden flag)](guynmart_quest_cook_bread.md#stage-1) | reaching stage 64 here closes stage 1 there |
| Blocks | [Guynmart garden guard (hidden flag)](guynmart_quest_gguard.md#stage-82) | reaching stages 100, 132 here closes stage 82 there |
| Blocks | [Guest tour (hidden flag)](guynmart_quest_olav.md#stage-7) | reaching stage 81 here closes stage 7 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is… ▸</span><span class="l">▴ less</span></summary>On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is worried about young Lady Hannah of Guynmart, who used to visit often but has not been seen for a week now. Rhodita asked me to check on her.</details> | [Rhodita](../monsters/guynmart_farmer.md) | – |
| <span id="stage-16"></span>[16](#route-16) | I got to the castle, but the main gate was shut. | [Guynmart guard](../monsters/guynmart_gguard.md#v-guynmart_guard_guide) | 12 XP, removes monsters from guynmart |
| <span id="stage-18"></span>[18](#route-18) | I got to the castle, but the main gate was shut. | [Guynmart guard](../monsters/guynmart_gguard.md#v-guynmart_guard_guide) | 15 XP, removes monsters from guynmart |
| <span id="stage-20"></span>20 | I found the way into the castle garden. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">The guard at the back door is corrupt. He agreed to let me through… ▸</span><span class="l">▴ less</span></summary>The guard at the back door is corrupt. He agreed to let me through for some gold.</details> | [Guynmart guard](../monsters/guynmart_gguard.md) | – |
| <span id="stage-32"></span>[32](#route-32) | <details class="jt"><summary><span class="s">He told me who is living at the castle: Guynmart himself, and his… ▸</span><span class="l">▴ less</span></summary>He told me who is living at the castle: Guynmart himself, and his children Hannah and Robalyrius.</details> | [Guynmart guard](../monsters/guynmart_gguard.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">In the main hall I met Unkorh the steward. He expected Guynmart to… ▸</span><span class="l">▴ less</span></summary>In the main hall I met Unkorh the steward. He expected Guynmart to return the following morning. He says I should go to the kitchen for some bread and then leave.</details> | [Unkorh](../monsters/guynmart_steward.md) | – |
| <span id="stage-45"></span>[45](#route-45) | I met Lady Hannah's little brother, Rob. | [Rob](../monsters/guynmart_rob.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">The maid told me that Hannah is missing her betrothed. I should talk… ▸</span><span class="l">▴ less</span></summary>The maid told me that Hannah is missing her betrothed. I should talk to Hannah; she is on the tower top. To get to her, I should offer the cook to take Hannah her lunch.</details> | [Maid](../monsters/guynmart_maid.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I overheard Unkorh the steward talking to himself. He plans for… ▸</span><span class="l">▴ less</span></summary>I overheard Unkorh the steward talking to himself. He plans for Guynmart to die in the castle dungeon, and after ursuping the throne he would marry Lady Hannah.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 2](../maps/guynmart_main_2.md).</span> | stepping on a trigger on [Guynmart main 2](../maps/guynmart_main_2.md) | – |
| <span id="stage-62"></span>[62](#route-62) | <details class="jt"><summary><span class="s">I suggested to Hofala the cook that I could take some lunch to Lady… ▸</span><span class="l">▴ less</span></summary>I suggested to Hofala the cook that I could take some lunch to Lady Hannah. He had no more of his special herb selection for the lunch and asked me to get some fresh herbs from Nuik in the garden.</details> | [Hofala](../monsters/guynmart_cook.md) | – |
| <span id="stage-63"></span>63 | Nuik gave some herbs to me. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-64"></span>[64](#route-64) | I should take lunch to Lady Hannah on the tower top. | [Hofala](../monsters/guynmart_cook.md) | [Hannah's lunch](../items/guynmart_lunch.md) |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">Hannah is filled with grief, she cannot think clearly without the… ▸</span><span class="l">▴ less</span></summary>Hannah is filled with grief, she cannot think clearly without the smell of a rose. Before she can tell me her whole story, she needs a fresh, fragrant rose.</details> | [Hannah](../monsters/guynmart_hannah.md) | spawns monsters on guynmart |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">Unkorh saw me talking to Hannah. He was very jealous and asked guard… ▸</span><span class="l">▴ less</span></summary>Unkorh saw me talking to Hannah. He was very jealous and asked guard Olav to show me the special guest exit.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 9](../maps/guynmart_wood_9.md).</span> | [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward3) | removes monsters from guynmart |
| <span id="stage-81"></span>[81](#route-81) | <details class="jt"><summary><span class="s">I met Norgothla, the chief of Guynmart's personal guard. He was… ▸</span><span class="l">▴ less</span></summary>I met Norgothla, the chief of Guynmart's personal guard. He was troubled about my news from the castle, and asked me to get evidence for it.</details> | [Norgothla](../monsters/guynmart_cguard.md) | – |
| <span id="stage-82"></span>82 | I got the rose from the guard at the garden door at last. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">I gave the rose to Hannah. She told me that Lovis has vanished. In… ▸</span><span class="l">▴ less</span></summary>I gave the rose to Hannah. She told me that Lovis has vanished. In the deepenst depths of her darkest dreams she hears Lovis' voice calling out.</details> | [Hannah](../monsters/guynmart_hannah.md) | – |
| <span id="stage-100"></span>[100](#route-100) | Hannah gave Lovis' flute to me, so that I might prove that I was sent by Hannah. | [Hannah](../monsters/guynmart_hannah.md) | 1× [Lovis' Flute](../items/guynmart_flute.md), removes monsters from guynmart_main_3, spawns monsters on guynmart_tower_3 |
| <span id="stage-110"></span>[110](#route-110) | <details class="jt"><summary><span class="s">I met Rob in a room above the watch chamber. Rob promised to… ▸</span><span class="l">▴ less</span></summary>I met Rob in a room above the watch chamber. Rob promised to distract the guards so that I could pass by.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 2](../maps/guynmart_tower_2.md).</span> | [Rob](../monsters/guynmart_rob.md#v-guynmart_rob3) | spawns monsters on guynmart_tower_2, removes monsters from guynmart_tower_3 |
| <span id="stage-120"></span>120 | <details class="jt"><summary><span class="s">120 obsolete - The guards were distracted and would not see anybody… ▸</span><span class="l">▴ less</span></summary>120 obsolete - The guards were distracted and would not see anybody climbing downstairs.</details> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-130"></span>130 | 130 obsolete - I jumped into the dark dungeon below the tower. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-132"></span>[132](#route-132) | <details class="jt"><summary><span class="s">I jumped into the dark dungeon below the tower where I found Lovis.… ▸</span><span class="l">▴ less</span></summary>I jumped into the dark dungeon below the tower where I found Lovis. He was overjoyed to get back his flute.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart tower 1](../maps/guynmart_tower_1.md).</span> | [Lovis](../monsters/guynmart_lovis.md) | – |
| <span id="stage-134"></span>[134](#route-134) | <details class="jt"><summary><span class="s">The dungeon door flew open. The torturer entered and demanded that… ▸</span><span class="l">▴ less</span></summary>The dungeon door flew open. The torturer entered and demanded that we stop the noise.</details> | [Lovis](../monsters/guynmart_lovis.md) | spawns monsters on guynmart_tower_0, removes monsters from guynmart_tower_0 |
| <span id="stage-136"></span>[136](#route-136) | After the torturer's death the door was open.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 0](../maps/guynmart_tower_0.md).</span> | walking into a blocked passage on [Guynmart tower 0](../maps/guynmart_tower_0.md) | – |
| <span id="stage-140"></span>140 | Lovis left and went into the woods to get Guynmart's personal guards. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-160"></span>[160](#route-160) | <details class="jt"><summary><span class="s">Guynmart was laying half dead in a cell. He asked me to open the… ▸</span><span class="l">▴ less</span></summary>Guynmart was laying half dead in a cell. He asked me to open the castle gate so that his personal guard may come in. After that I should run and hide, because there would be a dangerous battle. I should not return before the following morning.</details> | [Guynmart](../monsters/guynmart.md) | spawns monsters on guynmart_main_0, removes monsters from guynmart_tower_2 |
| <span id="stage-161"></span>[161](#route-161) | <details class="jt"><summary><span class="s">Unkorh appeared and explained many things. Then Unkorh saw that… ▸</span><span class="l">▴ less</span></summary>Unkorh appeared and explained many things. Then Unkorh saw that Guynmart tried to kill me from behind, but stumbled and fell onto his own knife. I should still open the gate, and then go to the farm in the south until the morning.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart main 0](../maps/guynmart_main_0.md).</span> | [Guynmart](../monsters/guynmart.md), [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward4) | removes monsters from guynmart_main_0 |
| <span id="stage-162"></span>[162](#route-162) | Unkorh appeared and killed Guynmart. Then he fled like a coward. | [Guynmart](../monsters/guynmart.md), [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward4) | removes monsters from guynmart_main_0 |
| <span id="stage-163"></span>[163](#route-163) | The guards let me through to the wall.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 2](../maps/guynmart_tower_2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | walking into a blocked passage on [Guynmart tower 2](../maps/guynmart_tower_2.md) | – |
| <span id="stage-164"></span>[164](#route-164) | I got the main gate open.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart gate 2](../maps/guynmart_gate_2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [Guynmart gate 2](../maps/guynmart_gate_2.md) | removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_2, removes monsters from guynmart_main_1, spawns monsters on guynmart, spawns monsters on guynmart_main_2, spawns monsters on guynmart_main_1 |
| <span id="stage-170"></span>[170](#route-170) | I went to Rhodita the farmer and stayed there for the night.<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart farmhouse](../maps/guynmart_farmhouse.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 1](../maps/guynmart_tower_1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart farmhouse](../maps/guynmart_farmhouse.md) | removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_0, removes monsters from guynmart_main_1, removes monsters from guynmart_main_2, removes monsters from guynmart_tower_2, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, spawns monsters on guynmart, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1 |
| <span id="stage-180"></span>[180](#route-180) | <details class="jt"><summary><span class="s">When I got to the castle on the next day, I saw Hannah and Lovis in… ▸</span><span class="l">▴ less</span></summary>When I got to the castle on the next day, I saw Hannah and Lovis in the throne room. The castle was decorated for a wedding and there had been a merry feast.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 1](../maps/guynmart_wood_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart main 1](../maps/guynmart_main_1.md), stepping on a trigger on [Guynmart](../maps/guynmart.md) | – |
| <span id="stage-181"></span>[181](#route-181) | <details class="jt"><summary><span class="s">When I got to the castle on the next day, I saw Unkorh the steward… ▸</span><span class="l">▴ less</span></summary>When I got to the castle on the next day, I saw Unkorh the steward in the throne room. The castle was decorated for a wedding and there had been a merry feast.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 1](../maps/guynmart_wood_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart main 1](../maps/guynmart_main_1.md), stepping on a trigger on [Guynmart](../maps/guynmart.md) | – |
| <span id="stage-190"></span>[190](#route-190) | Hannah gave me an everlasting fragrant rose as a present. | [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) | 1× [Rose](../items/guynmart_rose.md) |
| <span id="stage-200"></span>[200](#route-200) | I was allowed to choose something from the treasury. | [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) +1 | 5,000 XP, spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1 |
| <span id="stage-201"></span>[201](#route-201) | I took the money. | [Gold](../monsters/guynmart_reward1.md) | 5000× [Gold coins](../items/gold.md), removes monsters from guynmart_main_1 |
| <span id="stage-202"></span>[202](#route-202) | I took the scroll of wisdom. | [Wisdom](../monsters/guynmart_reward2.md) | 5,000 XP, 1× [Scroll of wisdom](../items/guynmart_scroll.md), removes monsters from guynmart_main_1 |
| <span id="stage-203"></span>[203](#route-203) | I took the shield. | [Armor](../monsters/guynmart_reward3.md) | 1× [Guynmart shield](../items/guynmart_shield.md), removes monsters from guynmart_main_1 |
| <span id="stage-210"></span>[210](#route-210) | Lovis prepared a surprise for me east of the castle. **(ends quest)**<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 9](../maps/guynmart_wood_9.md).</span> | [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) +1 | varies by route (see below) |
| <span id="stage-211"></span>[211](#route-211) | Then I took my leave of Unkorh. **(ends quest)** | [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) +1 | varies by route (see below) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Rhodita · 1 way"

    **Way 1:** Talk to [Rhodita](../monsters/guynmart_farmer.md), choose “Guynmart Castle? I have never heard of it. Please tell me more.”

    - *“I have too much work to do now. But maybe you could check if everything is OK with her?”*


<span id="route-16"></span>

??? note "Stage 16 · Guynmart guard · 1 way"

    **Way 1:** Talk to [Guynmart guard](../monsters/guynmart_gguard.md#v-guynmart_guard_guide), choose “OK, one kid, without guide, please.”

    - **Needs:** pay 12 gold
    - **Gives:** removes monsters from guynmart


<span id="route-18"></span>

??? note "Stage 18 · Guynmart guard · 1 way"

    **Way 1:** Talk to [Guynmart guard](../monsters/guynmart_gguard.md#v-guynmart_guard_guide), choose “One kid and a guide, please.”

    - **Needs:** pay 15 gold
    - **Gives:** removes monsters from guynmart


<span id="route-30"></span>

??? note "Stage 30 · Guynmart guard · 1 way"

    **Way 1:** Talk to [Guynmart guard](../monsters/guynmart_gguard.md), choose “Here is 100 gold.”

    - **Needs:** stage 30; pay 100 gold
    - <small>Also: sets stage 1 of [Guynmart garden guard (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1)</small>


<span id="route-32"></span>

??? note "Stage 32 · Guynmart guard · 1 way"

    **Way 1:** Talk to [Guynmart guard](../monsters/guynmart_gguard.md), choose “Here is 100 gold.”

    - **Needs:** stage 30; not yet stage 10, 32; pay 100 gold
    - *“[Gold taken] Very good. Before you enter maybe you should also know the family names: Lord Guynmart, his beautiful but complicated…”*


<span id="route-40"></span>

??? note "Stage 40 · Unkorh · 1 way"

    **Way 1:** Talk to [Unkorh](../monsters/guynmart_steward.md), choose “I would like to buy something to eat.”

    - *“The cook shall give you some bread. And he can provide you with further provisions, if you can pay for them.”*


<span id="route-45"></span>

??? note "Stage 45 · Rob · 1 way"

    **Way 1:** Talk to [Rob](../monsters/guynmart_rob.md), automatic

    - <small>Also: sets stage 1 of [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1)</small>
    - *“Hey - you found me at last! That was fun! I am Robalyrius, Guynmart's son, but please call me Rob. Who are you? Wait, I will open the…”*


<span id="route-50"></span>

??? note "Stage 50 · Maid · 1 way"

    **Way 1:** Talk to [Maid](../monsters/guynmart_maid.md), choose “Perhaps I could go and find Lovis for her.”

    - **Needs:** stage 50
    - *“Ah yes - tell the cook that I asked you to take lunch to Lady Hannah. He hates climbing stairs, so he will gladly agree.”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on guynmart_main_2 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart main 2](../maps/guynmart_main_2.md)

    - **Needs:** stage 50; not yet stage 60
    - *“[Whispering from below] Oh, how I long to take my place here...”*


<span id="route-62"></span>

??? note "Stage 62 · Hofala · 1 way"

    **Way 1:** Talk to [Hofala](../monsters/guynmart_cook.md), choose “Hannah's maid asked me to take her lunch to her.”

    - **Needs:** stage 50; not yet stage 62
    - *“Quick, run to Nuik, the old gardener. He will give you some fresh herbs.”*


<span id="route-64"></span>

??? note "Stage 64 · Hofala · 1 way"

    **Way 1:** Talk to [Hofala](../monsters/guynmart_cook.md), automatic

    - **Needs:** hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md)
    - **Gives:** [Hannah's lunch](../items/guynmart_lunch.md)
    - <small>Also: sets stage 1 of [Guynmart quest cook lunch (hidden flag)](../quests/guynmart_quest_cook_lunch.md#stage-1)</small>
    - *“...and now it is suitable for her. Hurry now, while it is still hot!”*


<span id="route-70"></span>

??? note "Stage 70 · Hannah · 1 way"

    **Way 1:** Talk to [Hannah](../monsters/guynmart_hannah.md), automatic

    - **Gives:** spawns monsters on guynmart
    - <small>Also: clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), sets stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7)</small>
    - *“I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...”*


<span id="route-80"></span>

??? note "Stage 80 · Unkorh · 1 way"

    **Way 1:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward3), choose “But...”

    - **Gives:** removes monsters from guynmart
    - *“Show our - guest - the special exit.”*


<span id="route-81"></span>

??? note "Stage 81 · Norgothla · 1 way"

    **Way 1:** Talk to [Norgothla](../monsters/guynmart_cguard.md), choose “Maybe I could go back and bring some evidence?”

    - *“By doing this, you take a great burden from my heart. I get to know what is happening at the castle, but don't have to disobey my lords…”*


<span id="route-90"></span>

??? note "Stage 90 · Hannah · 1 way"

    **Way 1:** Talk to [Hannah](../monsters/guynmart_hannah.md), automatic

    - **Needs:** carry 1× [Rose](../items/guynmart_rose.md); hand over 1× [Rose](../items/guynmart_rose.md)
    - *“[Hannah takes the rose] Now. I feel better again. Thank you.”*


<span id="route-100"></span>

??? note "Stage 100 · Hannah · 1 way"

    **Way 1:** Talk to [Hannah](../monsters/guynmart_hannah.md), choose “I will not disappoint you.”

    - **Needs:** carry 1× [Rose](../items/guynmart_rose.md); hand over 1× [Rose](../items/guynmart_rose.md)
    - **Gives:** 1× [Lovis' Flute](../items/guynmart_flute.md), removes monsters from guynmart_main_3, spawns monsters on guynmart_tower_3
    - <small>Also: sets stage 1 of [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1)</small>
    - *“So take this flute and take good care of it.”*


<span id="route-110"></span>

??? note "Stage 110 · Rob · 1 way"

    **Way 1:** Talk to [Rob](../monsters/guynmart_rob.md#v-guynmart_rob3), choose “Great idea.”

    - **Gives:** spawns monsters on guynmart_tower_2, removes monsters from guynmart_tower_3
    - *“Follow me in a minute - but make no noise.”*


<span id="route-132"></span>

??? note "Stage 132 · Lovis · 1 way"

    **Way 1:** Talk to [Lovis](../monsters/guynmart_lovis.md), choose “Here, I should give you this.”

    - **Needs:** hand over 1× [Lovis' Flute](../items/guynmart_flute.md)
    - <small>Also: sets stage 6 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-6), starts timer “guynmart_flute”</small>
    - *“My flute! How I have missed it! I believe you now.”*


<span id="route-134"></span>

??? note "Stage 134 · Lovis · 1 way"

    **Way 1:** Talk to [Lovis](../monsters/guynmart_lovis.md), automatic

    - **Needs:** stage 132, 134
    - **Gives:** spawns monsters on guynmart_tower_0, removes monsters from guynmart_tower_0
    - *“Oh no! Look! The torturer! I will run around him and look for Guynmart's personal guards outside in the wood. They will help us. I hope…”*


<span id="route-136"></span>

??? note "Stage 136 · walking into a blocked passage on guynmart_tower_0 · 1 way"

    **Way 1:** Walking into a blocked passage on [Guynmart tower 0](../maps/guynmart_tower_0.md)

    - **Needs:** killed 1× [Torturer](../monsters/guynmart_tort1.md)
    - *“The door is wide open now.”*


<span id="route-160"></span>

??? note "Stage 160 · Guynmart · 1 way"

    **Way 1:** Talk to [Guynmart](../monsters/guynmart.md), choose “Yes. I came through the garden door.”

    - **Gives:** spawns monsters on guynmart_main_0, removes monsters from guynmart_tower_2
    - *“Then you must open the gate! Go to the gatehouse and open it, so that my men can get in. Be quick. After that go to the farm south of…”*


<span id="route-161"></span>

??? note "Stage 161 · Guynmart, Unkorh · 2 ways"

    **Way 1:** Talk to [Guynmart](../monsters/guynmart.md), choose “Yes, I will trust you.”

    - **Gives:** removes monsters from guynmart_main_0
    - *“Watch out! Guynmart...”*

    **Way 2:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward4), automatic

    - **Needs:** stage 161
    - **Gives:** removes monsters from guynmart_main_0
    - *“Watch out! Guynmart...”*


<span id="route-162"></span>

??? note "Stage 162 · Guynmart, Unkorh · 2 ways"

    **Way 1:** Talk to [Guynmart](../monsters/guynmart.md), choose “Ha! So come on and try! No? I will put an end to you now!”

    - **Gives:** removes monsters from guynmart_main_0
    - *“OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...”*

    **Way 2:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward4), choose “Ha! So come on and try! No? I will put an end to you now!”

    - **Gives:** removes monsters from guynmart_main_0
    - *“OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...”*


<span id="route-163"></span>

??? note "Stage 163 · walking into a blocked passage on guynmart_tower_2 · 1 way"

    **Way 1:** Walking into a blocked passage on [Guynmart tower 2](../maps/guynmart_tower_2.md), choose “I am on a mission for Lord Guynmart.”

    - **Needs:** stage 160; not yet stage 161
    - *“OK, then hurry.”*


<span id="route-164"></span>

??? note "Stage 164 · stepping on a trigger on guynmart_gate_2 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart gate 2](../maps/guynmart_gate_2.md), choose “Open”

    - **Needs:** not reached stage 2 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-2)
    - **Gives:** removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_2, removes monsters from guynmart_main_1, spawns monsters on guynmart, spawns monsters on guynmart_main_2, spawns monsters on guynmart_main_1
    - <small>Also: sets stage 2 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-2)</small>
    - *“Done, the gate is open, and Guynmart's personal guard can enter. I should leave quickly now, maybe to the farmhouse south of here.”*


<span id="route-170"></span>

??? note "Stage 170 · stepping on a trigger on guynmart_farmhouse · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart farmhouse](../maps/guynmart_farmhouse.md)

    - **Needs:** stage 164
    - **Gives:** removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_0, removes monsters from guynmart_main_1, removes monsters from guynmart_main_2, removes monsters from guynmart_tower_2, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, spawns monsters on guynmart, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1
    - <small>Also: clears stage 34 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-34)</small>


<span id="route-180"></span>

??? note "Stage 180 · stepping on a trigger on guynmart_main_1, stepping on a trig · 2 ways"

    **Way 1:** Stepping on a trigger on [Guynmart main 1](../maps/guynmart_main_1.md)

    - **Needs:** stage 170

    **Way 2:** Stepping on a trigger on [Guynmart](../maps/guynmart.md)

    - **Needs:** stage 170


<span id="route-181"></span>

??? note "Stage 181 · stepping on a trigger on guynmart_main_1, stepping on a trig · 2 ways"

    **Way 1:** Stepping on a trigger on [Guynmart main 1](../maps/guynmart_main_1.md)

    - **Needs:** stage 161, 170
    - <small>Also: sets stage 60 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-60)</small>

    **Way 2:** Stepping on a trigger on [Guynmart](../maps/guynmart.md)

    - **Needs:** stage 161, 170
    - <small>Also: sets stage 60 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-60)</small>


<span id="route-190"></span>

??? note "Stage 190 · Hannah, Lovis · 2 ways"

    **Way 1:** Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), automatic

    - **Gives:** 1× [Rose](../items/guynmart_rose.md)
    - *“Take this rose as a token of my deepest thanks. May its lovely fragrance last forever.”*

    **Way 2:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), automatic

    - **Needs:** not yet stage 190
    - **Gives:** 1× [Rose](../items/guynmart_rose.md)
    - *“Take this rose as a token of my deepest thanks. May its lovely fragrance last forever.”*


<span id="route-200"></span>

??? note "Stage 200 · Hannah, Lovis, Unkorh · 3 ways"

    **Way 1:** Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), automatic

    - **Needs:** stage 190
    - **Gives:** spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1
    - *“You have earned your reward. Go now into our treasury.”*

    **Way 2:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), automatic

    - **Gives:** spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1
    - *“You have earned your reward. Go now into our treasury.”*

    **Way 3:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5), automatic

    - **Gives:** spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1
    - *“You have earned your reward. Go now into our treasury.”*


<span id="route-201"></span>

??? note "Stage 201 · Gold · 1 way"

    **Way 1:** Talk to [Gold](../monsters/guynmart_reward1.md), choose “You decide for the gold.”

    - **Needs:** not reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)
    - **Gives:** 5000× [Gold coins](../items/gold.md), removes monsters from guynmart_main_1
    - <small>Also: sets stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)</small>
    - *“You feel the pleasant weight of the gold in your bag.”*


<span id="route-202"></span>

??? note "Stage 202 · Wisdom · 1 way"

    **Way 1:** Talk to [Wisdom](../monsters/guynmart_reward2.md), choose “You decide for the scroll.”

    - **Needs:** not reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)
    - **Gives:** 1× [Scroll of wisdom](../items/guynmart_scroll.md), removes monsters from guynmart_main_1
    - <small>Also: sets stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)</small>
    - *“You feel an immediate benefit from the experience of others.”*


<span id="route-203"></span>

??? note "Stage 203 · Armor · 1 way"

    **Way 1:** Talk to [Armor](../monsters/guynmart_reward3.md), choose “You decide for the shield.”

    - **Needs:** not reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)
    - **Gives:** 1× [Guynmart shield](../items/guynmart_shield.md), removes monsters from guynmart_main_1
    - <small>Also: sets stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)</small>
    - *“This shield does feel good in your hands.”*


<span id="route-210"></span>

??? note "Stage 210 · Lovis, Unkorh, Hannah · 5 ways"

    **Way 1:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), choose “Oh yes - I am overwhelmed by your generosity!”

    - **Needs:** reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)
    - **Gives:** spawns monsters on guynmart_wood_9

    **Way 2:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5), choose “Oh yes - I am overwhelmed by your generosity!”

    - **Needs:** reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)
    - **Gives:** spawns monsters on guynmart_wood_9

    **Way 3:** Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), choose “I will go. Bye.”

    - **Needs:** stage 181, 190; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>

    **Way 4:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), choose “I will go. Bye.”

    - **Needs:** stage 181; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>

    **Way 5:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5), choose “I will go. Bye.”

    - **Needs:** stage 181; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>


<span id="route-211"></span>

??? note "Stage 211 · Lovis, Unkorh, Hannah · 5 ways"

    **Way 1:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), choose “Oh yes - I am overwhelmed by your generosity!”

    - **Needs:** stage 181; reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)

    **Way 2:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5), choose “Oh yes - I am overwhelmed by your generosity!”

    - **Needs:** stage 181; reached stage 32 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)

    **Way 3:** Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), choose “I will go. Bye.”

    - **Needs:** stage 181, 190; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>

    **Way 4:** Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2), choose “I will go. Bye.”

    - **Needs:** stage 181; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>

    **Way 5:** Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5), choose “I will go. Bye.”

    - **Needs:** stage 181; killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); not reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33)
    - **Gives:** removes monsters from guynmart_main_1
    - <small>Also: sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)</small>



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 40 lines added |
| [v0.7.4](../versions/0.7.4.md) | Stage 60 journal text changed |
| [v0.7.5](../versions/0.7.5.md) | Dialogue: 1 line changed |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Then you must open the gate! Go to the gatehouse and open it, so that…” → “Then you must open the gate! Go to the gatehouse and open it, so that…” |
| [v0.7.12](../versions/0.7.12.md) | Stage 210 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart` |
    | showInLog | 1 |
    | Stage IDs | 10, 16, 18, 20, 30, 32, 40, 45, 50, 60, 62, 63, 64, 70, 80, 81, 82, 90, 100, 110, 120, 130, 132, 134, 136, 140, 160, 161, 162, 163, 164, 170, 180, 181, 190, 200, 201, 202, 203, 210, 211 |
    | Dialogue nodes setting stages | 10: `guynmart_farmer_60`, 16: `guynmart_guard_guide_30`, 18: `guynmart_guard_guide_32`, 30: `guynmart_gguard_900`, 32: `guynmart_gguard_902`, 40: `guynmart_steward_30`, 45: `guynmart_rob_12`, 50: `guynmart_maid_66`, 60: `guynmart_sign_steward_2`, 62: `guynmart_cook_72`, 64: `guynmart_cook_120`, 70: `guynmart_player_02`, 70: `guynmart_hannah_20`, 80: `guynmart_steward3_52`, 81: `guynmart_cguard_80`, 90: `guynmart_hannah_114`, 100: `guynmart_hannah_150`, 110: `guynmart_rob3_40`, 132: `guynmart_lovis_40`, 134: `guynmart_lovis_200`, 136: `guynmart_key_tower0_door_30`, 160: `guynmart_100`, 161: `guynmart_steward4_210`, 162: `guynmart_steward4_60`, 163: `guynmart_key_tower1_20`, 164: `guynmart_s_gate1_58`, 170: `guynmart_s_gateopenrest_10`, 180: `guynmart_sRpl_main_1r_10`, 181: `guynmart_sRpl_main_1r_20`, 190: `guynmart_hannah2_50`, 200: `guynmart_lovis2_100`, 201: `guynmart_reward1_20`, 202: `guynmart_reward2_20`, 203: `guynmart_reward3_20`, 210: `guynmart_lovis2_140`, 210: `guynmart_lovis2_240`, 211: `guynmart_lovis2_141`, 211: `guynmart_lovis2_241` |
    | Dialogue nodes clearing stages | 164: `guynmart_s_gate1_70`, 70: `guynmart_player_04` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
