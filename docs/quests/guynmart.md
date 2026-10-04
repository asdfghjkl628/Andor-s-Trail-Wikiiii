# Roses

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart` |
| **In journal** | Yes |
| **Stages** | 41 (completes at 210, 211) |
| **Started by** | [Rhodita](../monsters/guynmart_farmer.md) ([guynmart_wood_1](../maps/guynmart_wood_1.md)) |
| **NPCs involved** | [Armor](../monsters/guynmart_reward3.md), [Gold](../monsters/guynmart_reward1.md), [Guynmart](../monsters/guynmart.md), [Guynmart guard](../monsters/guynmart_gguard.md), [Guynmart guard](../monsters/guynmart_guard_guide.md), [Hannah](../monsters/guynmart_hannah.md) +16 |
| **Locations** | [guynmart](../maps/guynmart.md), [guynmart_main_0](../maps/guynmart_main_0.md), [guynmart_main_1](../maps/guynmart_main_1.md), [guynmart_main_2](../maps/guynmart_main_2.md) |
| **Total XP** | 10,027 |
| **Related quests** | 6 |

</div>

## Overview

> On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is worried about young Lady Hannah of Guynmart, who used to visit often but has not been seen for a week now. Rhodita asked me to check on her.

## Prerequisites to start

None: talk to [Rhodita](../monsters/guynmart_farmer.md) ([guynmart_wood_1](../maps/guynmart_wood_1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-32) | stage 32 reached, for stages 210, 211 here |
| Blocked by | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-2) | stage 2 must NOT be reached, for stage 164 here |
| Blocked by | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-32) | stage 32 must NOT be reached, for stages 201, 202, 203 here |
| Blocked by | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-33) | stage 33 must NOT be reached, for stages 210, 211 here |
| Unlocks | [Search for Andor](andor.md#stage-92) | stage 92 there needs stage 161 here |
| Unlocks | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-2) | stage 2 there needs stage 170 here |
| Unlocks | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-33) | stage 33 there needs stages 181, 190 here |
| Unlocks | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-36) | stage 36 there needs stages 181, 190 here |
| Unlocks | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-60) | stage 60 there needs stages 161, 170 here |
| Unlocks | [guynmart_quest_cook_bread (hidden flag)](guynmart_quest_cook_bread.md#stage-1) | stage 1 there needs stages 40, 62 here |
| Unlocks | [gardenGuard blocks (hidden flag)](guynmart_quest_gguard.md#stage-1) | stage 1 there needs stage 30 here |
| Unlocks | [gardenGuard blocks (hidden flag)](guynmart_quest_gguard.md#stage-82) | stage 82 there needs stage 70 here |
| Unlocks | [Guest tour (hidden flag)](guynmart_quest_olav.md#stage-7) | stage 7 there needs stage 80 here |
| Unlocks | [guynmart rope (hidden flag)](guynmart_r_rope.md#stage-11) | stage 11 there needs stage 80 here |
| Blocks | [guynmart_quest_cook_bread (hidden flag)](guynmart_quest_cook_bread.md#stage-1) | reaching stage 64 here closes stage 1 there |
| Blocks | [gardenGuard blocks (hidden flag)](guynmart_quest_gguard.md#stage-82) | reaching stages 100, 132 here closes stage 82 there |
| Blocks | [Guest tour (hidden flag)](guynmart_quest_olav.md#stage-7) | reaching stage 81 here closes stage 7 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | On a farm I heard of Guynmart Castle nearby. The farmer Rhodita is worried about young Lady Hannah of Guynmart, who used to visit often but has not been seen for a week now. Rhodita asked me to check on her. | [Rhodita](../monsters/guynmart_farmer.md) ([guynmart_wood_1](../maps/guynmart_wood_1.md)) | – | – |
| <span id="stage-16"></span>16 | I got to the castle, but the main gate was shut. | [Guynmart guard](../monsters/guynmart_guard_guide.md) ([guynmart](../maps/guynmart.md)) | pay 12 gold | 12 XP<br>removes monsters from guynmart |
| <span id="stage-18"></span>18 | I got to the castle, but the main gate was shut. | [Guynmart guard](../monsters/guynmart_guard_guide.md) ([guynmart](../maps/guynmart.md)) | pay 15 gold | 15 XP<br>removes monsters from guynmart |
| <span id="stage-20"></span>20 | I found the way into the castle garden. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-30"></span>30 | The guard at the back door is corrupt. He agreed to let me through for some gold. | [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) | pay 100 gold | sets stage 1 of [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1) |
| <span id="stage-32"></span>32 | He told me who is living at the castle: Guynmart himself, and his children Hannah and Robalyrius. | [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) | pay 100 gold, stage 30 | – |
| <span id="stage-40"></span>40 | In the main hall I met Unkorh the steward. He expected Guynmart to return the following morning. He says I should go to the kitchen for some bread and then leave. | [Unkorh](../monsters/guynmart_steward.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | – | – |
| <span id="stage-45"></span>45 | I met Lady Hannah's little brother, Rob. | [Rob](../monsters/guynmart_rob.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) | – | sets stage 1 of [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1) |
| <span id="stage-50"></span>50 | The maid told me that Hannah is missing her betrothed. I should talk to Hannah; she is on the tower top. To get to her, I should offer the cook to take Hannah her lunch. | [Maid](../monsters/guynmart_maid.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) | – | – |
| <span id="stage-60"></span>60 | I overheard Unkorh the steward talking to himself. He plans for Guynmart to die in the castle dungeon, and after ursuping the throne he would marry Lady Hannah.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 2](../maps/guynmart_main_2.md).</span> | stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) | stage 50 | – |
| <span id="stage-62"></span>62 | I suggested to Hofala the cook that I could take some lunch to Lady Hannah. He had no more of his special herb selection for the lunch and asked me to get some fresh herbs from Nuik in the garden. | [Hofala](../monsters/guynmart_cook.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) | stage 50 | – |
| <span id="stage-63"></span>63 | Nuik gave some herbs to me. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-64"></span>64 | I should take lunch to Lady Hannah on the tower top. | [Hofala](../monsters/guynmart_cook.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) | hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md) | gives [Hannah's lunch](../items/guynmart_lunch.md)<br>sets stage 1 of [guynmart_quest_cook_lunch (hidden flag)](../quests/guynmart_quest_cook_lunch.md#stage-1) |
| <span id="stage-70"></span>70 | Hannah is filled with grief, she cannot think clearly without the smell of a rose. Before she can tell me her whole story, she needs a fresh, fragrant rose. | [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) | – | spawns monsters on guynmart<br>clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1)<br>sets stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7) |
| <span id="stage-80"></span>80 | Unkorh saw me talking to Hannah. He was very jealous and asked guard Olav to show me the special guest exit.<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 9](../maps/guynmart_wood_9.md).</span> | [Unkorh](../monsters/guynmart_steward3.md) ([guynmart](../maps/guynmart.md)) | – | removes monsters from guynmart |
| <span id="stage-81"></span>81 | I met Norgothla, the chief of Guynmart's personal guard. He was troubled about my news from the castle, and asked me to get evidence for it. | [Norgothla](../monsters/guynmart_cguard.md) ([guynmart_wood_4](../maps/guynmart_wood_4.md)) | – | – |
| <span id="stage-82"></span>82 | I got the rose from the guard at the garden door at last. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-90"></span>90 | I gave the rose to Hannah. She told me that Lovis has vanished. In the deepenst depths of her darkest dreams she hears Lovis' voice calling out. | [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) | carry 1× [Rose](../items/guynmart_rose.md), hand over 1× [Rose](../items/guynmart_rose.md) | – |
| <span id="stage-100"></span>100 | Hannah gave Lovis' flute to me, so that I might prove that I was sent by Hannah. | [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) | carry 1× [Rose](../items/guynmart_rose.md), hand over 1× [Rose](../items/guynmart_rose.md) | gives 1× [Lovis' Flute](../items/guynmart_flute.md)<br>sets stage 1 of [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1)<br>removes monsters from guynmart_main_3<br>spawns monsters on guynmart_tower_3 |
| <span id="stage-110"></span>110 | I met Rob in a room above the watch chamber. Rob promised to distract the guards so that I could pass by.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 2](../maps/guynmart_tower_2.md).</span> | [Rob](../monsters/guynmart_rob3.md) ([guynmart_tower_3](../maps/guynmart_tower_3.md)) | – | spawns monsters on guynmart_tower_2<br>removes monsters from guynmart_tower_3 |
| <span id="stage-120"></span>120 | 120 obsolete - The guards were distracted and would not see anybody climbing downstairs. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-130"></span>130 | 130 obsolete - I jumped into the dark dungeon below the tower. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-132"></span>132 | I jumped into the dark dungeon below the tower where I found Lovis. He was overjoyed to get back his flute.<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart tower 1](../maps/guynmart_tower_1.md).</span> | [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) | hand over 1× [Lovis' Flute](../items/guynmart_flute.md) | sets stage 6 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-6)<br>starts timer “guynmart_flute” |
| <span id="stage-134"></span>134 | The dungeon door flew open. The torturer entered and demanded that we stop the noise. | [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) | stage 132 | spawns monsters on guynmart_tower_0<br>removes monsters from guynmart_tower_0 |
| <span id="stage-136"></span>136 | After the torturer's death the door was open.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 0](../maps/guynmart_tower_0.md).</span> | walking into a blocked passage on [guynmart_tower_0](../maps/guynmart_tower_0.md) | – | – |
| <span id="stage-140"></span>140 | Lovis left and went into the woods to get Guynmart's personal guards. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-160"></span>160 | Guynmart was laying half dead in a cell. He asked me to open the castle gate so that his personal guard may come in. After that I should run and hide, because there would be a dangerous battle. I should not return before the following morning. | [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) | – | spawns monsters on guynmart_main_0<br>removes monsters from guynmart_tower_2 |
| <span id="stage-161"></span>161 | Unkorh appeared and explained many things. Then Unkorh saw that Guynmart tried to kill me from behind, but stumbled and fell onto his own knife. I should still open the gate, and then go to the farm in the south until the morning.<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart main 0](../maps/guynmart_main_0.md).</span> | [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward4.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) | – | removes monsters from guynmart_main_0 |
| <span id="stage-162"></span>162 | Unkorh appeared and killed Guynmart. Then he fled like a coward. | [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward4.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) | – | removes monsters from guynmart_main_0 |
| <span id="stage-163"></span>163 | The guards let me through to the wall.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 2](../maps/guynmart_tower_2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | walking into a blocked passage on [guynmart_tower_2](../maps/guynmart_tower_2.md) | stage 160 | – |
| <span id="stage-164"></span>164 | I got the main gate open.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart gate 2](../maps/guynmart_gate_2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_gate_2](../maps/guynmart_gate_2.md) | – | sets stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2)<br>removes monsters from guynmart<br>removes monsters from guynmart_main_2<br>removes monsters from guynmart_main_1<br>spawns monsters on guynmart<br>spawns monsters on guynmart_main_2<br>spawns monsters on guynmart_main_1 |
| <span id="stage-170"></span>170 | I went to Rhodita the farmer and stayed there for the night.<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart farmhouse](../maps/guynmart_farmhouse.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart tower 1](../maps/guynmart_tower_1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart_farmhouse](../maps/guynmart_farmhouse.md) | stage 164 | removes monsters from guynmart<br>removes monsters from guynmart_main_0<br>removes monsters from guynmart_main_1<br>removes monsters from guynmart_main_2<br>removes monsters from guynmart_tower_2<br>removes monsters from guynmart_wood_4<br>spawns monsters on guynmart<br>spawns monsters on guynmart_main_1<br>clears stage 34 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-34) |
| <span id="stage-180"></span>180 | When I got to the castle on the next day, I saw Hannah and Lovis in the throne room. The castle was decorated for a wedding and there had been a merry feast.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 1](../maps/guynmart_wood_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md)<br>stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 170 | – |
| <span id="stage-181"></span>181 | When I got to the castle on the next day, I saw Unkorh the steward in the throne room. The castle was decorated for a wedding and there had been a merry feast.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 1](../maps/guynmart_wood_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md)<br>stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 161, stage 170 | sets stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60) |
| <span id="stage-190"></span>190 | Hannah gave me an everlasting fragrant rose as a present. | [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) | – | gives 1× [Rose](../items/guynmart_rose.md) |
| <span id="stage-200"></span>200 | I was allowed to choose something from the treasury. | [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | stage 190 | 5,000 XP<br>spawns monsters on guynmart_main_1<br>removes monsters from guynmart_main_1 |
| <span id="stage-201"></span>201 | I took the money. | [Gold](../monsters/guynmart_reward1.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | – | sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)<br>gives 5000× [Gold coins](../items/gold.md)<br>removes monsters from guynmart_main_1 |
| <span id="stage-202"></span>202 | I took the scroll of wisdom. | [Wisdom](../monsters/guynmart_reward2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | – | 5,000 XP<br>sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)<br>gives 1× [Scroll of wisdom](../items/guynmart_scroll.md)<br>removes monsters from guynmart_main_1 |
| <span id="stage-203"></span>203 | I took the shield. | [Armor](../monsters/guynmart_reward3.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | – | sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32)<br>gives 1× [Guynmart shield](../items/guynmart_shield.md)<br>removes monsters from guynmart_main_1 |
| <span id="stage-210"></span>210 | Lovis prepared a surprise for me east of the castle. **(completes quest)**<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart wood 9](../maps/guynmart_wood_9.md).</span> | [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | stage 181, stage 190 | spawns monsters on guynmart_wood_9<br>sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)<br>removes monsters from guynmart_main_1 |
| <span id="stage-211"></span>211 | Then I took my leave of Unkorh. **(completes quest)** | [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | stage 181, stage 190 | sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36)<br>removes monsters from guynmart_main_1 |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Rhodita](../monsters/guynmart_farmer.md) ([guynmart_wood_1](../maps/guynmart_wood_1.md)) → choose “Guynmart Castle? I have never heard of it. Please tell me more.” → **stage 10**. NPC: “I have too much work to do now. But maybe you could check if everything is OK with her?”

???+ note "Stage 16: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_guard_guide.md) ([guynmart](../maps/guynmart.md)) → choose “OK, one kid, without guide, please.” — **conditions:** pay 12 gold → **stage 16**; also removes monsters from guynmart

???+ note "Stage 18: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_guard_guide.md) ([guynmart](../maps/guynmart.md)) → choose “One kid and a guide, please.” — **conditions:** pay 15 gold → **stage 18**; also removes monsters from guynmart

???+ note "Stage 30: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) → choose “Here is 100 gold.” — **conditions:** reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold → **stage 30**; also sets stage 1 of [gardenGuard blocks (hidden flag)](../quests/guynmart_quest_gguard.md#stage-1)

???+ note "Stage 32: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) → choose “Here is 100 gold.” — **conditions:** reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold; NOT reached stage 10 of [Roses](../quests/guynmart.md#stage-10); NOT reached stage 32 of [Roses](../quests/guynmart.md#stage-32) → **stage 32**. NPC: “[Gold taken] Very good. Before you enter maybe you should also know the family names: Lord Guynmart, his beautiful but…”

???+ note "Stage 40: 1 route"

    1. Talk to [Unkorh](../monsters/guynmart_steward.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I would like to buy something to eat.” → **stage 40**. NPC: “The cook shall give you some bread. And he can provide you with further provisions, if you can pay for them.”

???+ note "Stage 45: 1 route"

    1. Talk to [Rob](../monsters/guynmart_rob.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) → the conversation leads here automatically → **stage 45**; also sets stage 1 of [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1). NPC: “Hey - you found me at last! That was fun! I am Robalyrius, Guynmart's son, but please call me Rob. Who are you? Wait,…”

???+ note "Stage 50: 1 route"

    1. Talk to [Maid](../monsters/guynmart_maid.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) → choose “Perhaps I could go and find Lovis for her.” — **conditions:** reached stage 50 of [Roses](../quests/guynmart.md#stage-50) → **stage 50**. NPC: “Ah yes - tell the cook that I asked you to take lunch to Lady Hannah. He hates climbing stairs, so he will gladly agree.”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Roses](../quests/guynmart.md#stage-50); NOT reached stage 60 of [Roses](../quests/guynmart.md#stage-60) → **stage 60**. NPC: “[Whispering from below] Oh, how I long to take my place here...”

???+ note "Stage 62: 1 route"

    1. Talk to [Hofala](../monsters/guynmart_cook.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) → choose “Hannah's maid asked me to take her lunch to her.” — **conditions:** reached stage 50 of [Roses](../quests/guynmart.md#stage-50); NOT reached stage 62 of [Roses](../quests/guynmart.md#stage-62) → **stage 62**. NPC: “Quick, run to Nuik, the old gardener. He will give you some fresh herbs.”

???+ note "Stage 64: 1 route"

    1. Talk to [Hofala](../monsters/guynmart_cook.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) → the conversation leads here automatically — **conditions:** hand over 1× [Hannah's special herbs](../items/guynmart_herbs.md) → **stage 64**; also gives [Hannah's lunch](../items/guynmart_lunch.md), sets stage 1 of [guynmart_quest_cook_lunch (hidden flag)](../quests/guynmart_quest_cook_lunch.md#stage-1). NPC: “...and now it is suitable for her. Hurry now, while it is still hot!”

???+ note "Stage 70: 1 route"

    1. Talk to [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) → the conversation leads here automatically → **stage 70**; also spawns monsters on guynmart, clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), sets stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7). NPC: “I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...”

???+ note "Stage 80: 1 route"

    1. Talk to [Unkorh](../monsters/guynmart_steward3.md) ([guynmart](../maps/guynmart.md)) → choose “But...” → **stage 80**; also removes monsters from guynmart. NPC: “Show our - guest - the special exit.”

???+ note "Stage 81: 1 route"

    1. Talk to [Norgothla](../monsters/guynmart_cguard.md) ([guynmart_wood_4](../maps/guynmart_wood_4.md)) → choose “Maybe I could go back and bring some evidence?” → **stage 81**. NPC: “By doing this, you take a great burden from my heart. I get to know what is happening at the castle, but don't have to…”

???+ note "Stage 90: 1 route"

    1. Talk to [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) → the conversation leads here automatically — **conditions:** carry 1× [Rose](../items/guynmart_rose.md); hand over 1× [Rose](../items/guynmart_rose.md) → **stage 90**. NPC: “[Hannah takes the rose] Now. I feel better again. Thank you.”

???+ note "Stage 100: 1 route"

    1. Talk to [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) → choose “I will not disappoint you.” — **conditions:** carry 1× [Rose](../items/guynmart_rose.md); hand over 1× [Rose](../items/guynmart_rose.md) → **stage 100**; also gives 1× [Lovis' Flute](../items/guynmart_flute.md), sets stage 1 of [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1), removes monsters from guynmart_main_3, spawns monsters on guynmart_tower_3. NPC: “So take this flute and take good care of it.”

???+ note "Stage 110: 1 route"

    1. Talk to [Rob](../monsters/guynmart_rob3.md) ([guynmart_tower_3](../maps/guynmart_tower_3.md)) → choose “Great idea.” → **stage 110**; also spawns monsters on guynmart_tower_2, removes monsters from guynmart_tower_3. NPC: “Follow me in a minute - but make no noise.”

???+ note "Stage 132: 1 route"

    1. Talk to [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) → choose “Here, I should give you this.” — **conditions:** hand over 1× [Lovis' Flute](../items/guynmart_flute.md) → **stage 132**; also sets stage 6 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-6), starts timer “guynmart_flute”. NPC: “My flute! How I have missed it! I believe you now.”

???+ note "Stage 134: 1 route"

    1. Talk to [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) → the conversation leads here automatically — **conditions:** reached stage 132 of [Roses](../quests/guynmart.md#stage-132); reached stage 134 of [Roses](../quests/guynmart.md#stage-134) → **stage 134**; also spawns monsters on guynmart_tower_0, removes monsters from guynmart_tower_0. NPC: “Oh no! Look! The torturer! I will run around him and look for Guynmart's personal guards outside in the wood. They…”

???+ note "Stage 136: 1 route"

    1. walking into a blocked passage on [guynmart_tower_0](../maps/guynmart_tower_0.md) → the conversation leads here automatically — **conditions:** killed 1× [Torturer](../monsters/guynmart_tort1.md) → **stage 136**. NPC: “The door is wide open now.”

???+ note "Stage 160: 1 route"

    1. Talk to [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Yes. I came through the garden door.” → **stage 160**; also spawns monsters on guynmart_main_0, removes monsters from guynmart_tower_2. NPC: “Then you must open the gate! Go to the gatehouse and open it, so that my men can get in. Be quick. After that go to…”

???+ note "Stage 161: 2 routes"

    1. Talk to [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Yes, I will trust you.” → **stage 161**; also removes monsters from guynmart_main_0. NPC: “Watch out! Guynmart...”
    2. Talk to [Unkorh](../monsters/guynmart_steward4.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → the conversation leads here automatically — **conditions:** reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 161**; also removes monsters from guynmart_main_0. NPC: “Watch out! Guynmart...”

???+ note "Stage 162: 2 routes"

    1. Talk to [Guynmart](../monsters/guynmart.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Ha! So come on and try! No? I will put an end to you now!” → **stage 162**; also removes monsters from guynmart_main_0. NPC: “OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...”
    2. Talk to [Unkorh](../monsters/guynmart_steward4.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Ha! So come on and try! No? I will put an end to you now!” → **stage 162**; also removes monsters from guynmart_main_0. NPC: “OK. I will go now. But I will not forget you - fear my revenge! And before I leave, I will stab your beloved Guynmart...”

???+ note "Stage 163: 1 route"

    1. walking into a blocked passage on [guynmart_tower_2](../maps/guynmart_tower_2.md) → choose “I am on a mission for Lord Guynmart.” — **conditions:** reached stage 160 of [Roses](../quests/guynmart.md#stage-160); NOT reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 163**. NPC: “OK, then hurry.”

???+ note "Stage 164: 1 route"

    1. stepping on a trigger on [guynmart_gate_2](../maps/guynmart_gate_2.md) → choose “Open” — **conditions:** NOT reached stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2) → **stage 164**; also sets stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2), removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_2, removes monsters from guynmart_main_1, spawns monsters on guynmart, spawns monsters on guynmart_main_2, spawns monsters on guynmart_main_1. NPC: “Done, the gate is open, and Guynmart's personal guard can enter. I should leave quickly now, maybe to the farmhouse…”

???+ note "Stage 170: 1 route"

    1. stepping on a trigger on [guynmart_farmhouse](../maps/guynmart_farmhouse.md) → the conversation leads here automatically — **conditions:** reached stage 164 of [Roses](../quests/guynmart.md#stage-164) → **stage 170**; also removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_0, removes monsters from guynmart_main_1, removes monsters from guynmart_main_2, removes monsters from guynmart_tower_2, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, removes monsters from guynmart_wood_4, spawns monsters on guynmart, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, spawns monsters on guynmart_main_1, clears stage 34 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-34)

???+ note "Stage 180: 2 routes"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170) → **stage 180**
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170) → **stage 180**

???+ note "Stage 181: 2 routes"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 181**; also sets stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60)
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 181**; also sets stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60)

???+ note "Stage 190: 2 routes"

    1. Talk to [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → the conversation leads here automatically → **stage 190**; also gives 1× [Rose](../items/guynmart_rose.md). NPC: “Take this rose as a token of my deepest thanks. May its lovely fragrance last forever.”
    2. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 190 of [Roses](../quests/guynmart.md#stage-190) → **stage 190**; also gives 1× [Rose](../items/guynmart_rose.md). NPC: “Take this rose as a token of my deepest thanks. May its lovely fragrance last forever.”

???+ note "Stage 200: 3 routes"

    1. Talk to [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → the conversation leads here automatically — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190) → **stage 200**; also spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1. NPC: “You have earned your reward. Go now into our treasury.”
    2. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → the conversation leads here automatically → **stage 200**; also spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1. NPC: “You have earned your reward. Go now into our treasury.”
    3. Talk to [Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → the conversation leads here automatically → **stage 200**; also spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1. NPC: “You have earned your reward. Go now into our treasury.”

???+ note "Stage 201: 1 route"

    1. Talk to [Gold](../monsters/guynmart_reward1.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the gold.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 201**; also sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32), gives 5000× [Gold coins](../items/gold.md), removes monsters from guynmart_main_1. NPC: “You feel the pleasant weight of the gold in your bag.”

???+ note "Stage 202: 1 route"

    1. Talk to [Wisdom](../monsters/guynmart_reward2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the scroll.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 202**; also sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32), gives 1× [Scroll of wisdom](../items/guynmart_scroll.md), removes monsters from guynmart_main_1. NPC: “You feel an immediate benefit from the experience of others.”

???+ note "Stage 203: 1 route"

    1. Talk to [Armor](../monsters/guynmart_reward3.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the shield.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 203**; also sets stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32), gives 1× [Guynmart shield](../items/guynmart_shield.md), removes monsters from guynmart_main_1. NPC: “This shield does feel good in your hands.”

???+ note "Stage 210: 5 routes"

    1. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 210**; also spawns monsters on guynmart_wood_9
    2. Talk to [Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 210**; also spawns monsters on guynmart_wood_9
    3. Talk to [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190); killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 210**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    4. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 210**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    5. Talk to [Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 210**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9

???+ note "Stage 211: 5 routes"

    1. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 211**
    2. Talk to [Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 211**
    3. Talk to [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190); killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 211**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1
    4. Talk to [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 211**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1
    5. Talk to [Unkorh](../monsters/guynmart_steward5.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/guynmart_sheep.md); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 211**; also sets stage 36 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 40 lines added |
| [v0.7.4](../versions/0.7.4.md) | stage 60 journal text changed |
| [v0.7.5](../versions/0.7.5.md) | Dialogue: 1 line changed |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Then you must open the gate! Go to the gatehouse and open it, so that…” → “Then you must open the gate! Go to the gatehouse and open it, so that…” |
| [v0.7.12](../versions/0.7.12.md) | stage 210 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
