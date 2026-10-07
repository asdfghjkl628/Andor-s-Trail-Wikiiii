---
description: "guynmart nondisplay is a hidden quest in Andor's Trail, started by stepping on a trigger on guynmart_wood_2. 29 stages. 1=Puppy revenged"
---

# guynmart nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 29 |
| **Started by** | stepping on a trigger on [guynmart_wood_2](../maps/guynmart_wood_2.md) |
| **NPCs involved** | [Armor](../monsters/guynmart_reward3.md), [Fjoerkard](../monsters/guynmart_drunkard1.md), [Gold](../monsters/guynmart_reward1.md), [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2), [Hannah](../monsters/guynmart_hannah.md), [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah3) +6 |
| **Locations** | [guynmart](../maps/guynmart.md), [guynmart_main_0](../maps/guynmart_main_0.md), [guynmart_main_1](../maps/guynmart_main_1.md), [guynmart_main_2](../maps/guynmart_main_2.md) |
| **Related quests** | 3 |

</div>

## Overview

> 1=Puppy revenged

## Prerequisites to start

Start with stepping on a trigger on [guynmart_wood_2](../maps/guynmart_wood_2.md). Required:

- killed 1× [Cute dog puppy](../monsters/guynmart_dog_puppy.md)
- NOT reached stage 1 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-1)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Roses](guynmart.md#stage-161) | stage 161 reached, for stage 60 here |
| Requires | [Roses](guynmart.md#stage-170) | stage 170 reached, for stages 2, 60 here |
| Requires | [Roses](guynmart.md#stage-181) | stage 181 reached, for stages 33, 36 here |
| Requires | [Roses](guynmart.md#stage-190) | stage 190 reached, for stages 33, 36 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-60) | stage 60 there needs stage 59 here |
| Unlocks | [Roses](guynmart.md#stage-210) | stage 210 there needs stage 32 here |
| Unlocks | [Roses](guynmart.md#stage-211) | stage 211 there needs stage 32 here |
| Unlocks | [Rare delicacies](guynmart_wise.md#stage-10) | stage 10 there needs stage 35 here |
| Unlocks | [Rare delicacies](guynmart_wise.md#stage-20) | stage 20 there needs stage 35 here |
| Unlocks | [Rare delicacies](guynmart_wise.md#stage-30) | stage 30 there needs stage 35 here |
| Unlocks | [Rare delicacies](guynmart_wise.md#stage-90) | stage 90 there needs stage 35 here |
| Blocks | [Roses](guynmart.md#stage-164) | reaching stage 2 here closes stage 164 there |
| Blocks | [Roses](guynmart.md#stage-201) | reaching stage 32 here closes stage 201 there |
| Blocks | [Roses](guynmart.md#stage-202) | reaching stage 32 here closes stage 202 there |
| Blocks | [Roses](guynmart.md#stage-203) | reaching stage 32 here closes stage 203 there |
| Blocks | [Roses](guynmart.md#stage-210) | reaching stage 33 here closes stage 210 there |
| Blocks | [Roses](guynmart.md#stage-211) | reaching stage 33 here closes stage 211 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=Puppy revenged<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 2](../maps/guynmart_wood_2.md).</span> | stepping on a trigger on [guynmart_wood_2](../maps/guynmart_wood_2.md) | – | spawns monsters on guynmart_wood_2 |
| <span id="stage-2"></span>2 | 2=Gate open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart gate 2](../maps/guynmart_gate_2.md).</span><br><span class="qnote">🗺️ Part of [Guynmart](../maps/guynmart.md) visibly changes.</span> | stepping on a trigger on [guynmart_gate_2](../maps/guynmart_gate_2.md) | – | sets stage 164 of [Roses](../quests/guynmart.md#stage-164)<br>removes monsters from guynmart<br>removes monsters from guynmart_main_2<br>removes monsters from guynmart_main_1<br>spawns monsters on guynmart<br>spawns monsters on guynmart_main_2<br>spawns monsters on guynmart_main_1 |
| <span id="stage-3"></span>3 | 3=Dungeonhole OK | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-4"></span>4 | 4=Fjoerkard asked for wine | [Fjoerkard](../monsters/guynmart_drunkard1.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) | carry 1× [Wine](../items/guynmart_wine.md) | – |
| <span id="stage-5"></span>5 | 5=Seated next to Fjoerkard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 2](../maps/guynmart_main_2.md).</span> | stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) | – | – |
| <span id="stage-6"></span>6 |  | [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) | hand over 1× [Lovis' Flute](../items/guynmart_flute.md) | sets stage 132 of [Roses](../quests/guynmart.md#stage-132)<br>starts timer “guynmart_flute” |
| <span id="stage-30"></span>30 | 30=Hero introduced<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) | – | – |
| <span id="stage-31"></span>31 | 31=Hero in throne room<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) | – | – |
| <span id="stage-32"></span>32 | 32=Reward chosen | [Gold](../monsters/guynmart_reward1.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Wisdom](../monsters/guynmart_reward2.md) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Armor](../monsters/guynmart_reward3.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) | – | sets stage 201 of [Roses](../quests/guynmart.md#stage-201)<br>gives 5000× [Gold coins](../items/gold.md)<br>removes monsters from guynmart_main_1<br>sets stage 202 of [Roses](../quests/guynmart.md#stage-202)<br>gives 1× [Scroll of wisdom](../items/guynmart_scroll.md)<br>sets stage 203 of [Roses](../quests/guynmart.md#stage-203)<br>gives 1× [Guynmart shield](../items/guynmart_shield.md) |
| <span id="stage-33"></span>33 | 33=Sheep payed | [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md)) | pay 2,500 gold | removes monsters from guynmart_main_1 |
| <span id="stage-34"></span>34 | 34=Alone in throne room<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) | – | removes monsters from guynmart_main_1<br>removes monsters from guynmart_main_2 |
| <span id="stage-35"></span>35 | 35=Wise met | [Old man](../monsters/old_man.md#v-guynmart_wise) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | – |
| <span id="stage-36"></span>36 | 36=Guynmart done | [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md))<br>[Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md))<br>[Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)) | stage 32 | sets stage 210 of [Roses](../quests/guynmart.md#stage-210)<br>removes monsters from guynmart_main_1<br>spawns monsters on guynmart_wood_9<br>sets stage 211 of [Roses](../quests/guynmart.md#stage-211) |
| <span id="stage-41"></span>41 | 41=Hill1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 10](../maps/guynmart_wood_10.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 11](../maps/guynmart_wood_11.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 10](../maps/guynmart_wood_10.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 11](../maps/guynmart_wood_11.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) | – | clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42)<br>clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43)<br>clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44)<br>clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45) |
| <span id="stage-42"></span>42 | 42=Hill1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 10](../maps/guynmart_wood_10.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 11](../maps/guynmart_wood_11.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 10](../maps/guynmart_wood_10.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 11](../maps/guynmart_wood_11.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) | – | clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41)<br>clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43)<br>clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44)<br>clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45) |
| <span id="stage-43"></span>43 | 43=Hill1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 11](../maps/guynmart_wood_11.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 10](../maps/guynmart_wood_10.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 11](../maps/guynmart_wood_11.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_11](../maps/guynmart_wood_11.md) | – | clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41)<br>clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42)<br>clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44)<br>clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45) |
| <span id="stage-44"></span>44 | 44=Hill1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 10](../maps/guynmart_wood_10.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 11](../maps/guynmart_wood_11.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 10](../maps/guynmart_wood_10.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 11](../maps/guynmart_wood_11.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) | – | clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41)<br>clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42)<br>clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43)<br>clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45) |
| <span id="stage-45"></span>45 | 45=Hill1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 10](../maps/guynmart_wood_10.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 10](../maps/guynmart_wood_10.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 11](../maps/guynmart_wood_11.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) | – | clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41)<br>clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42)<br>clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43)<br>clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44) |
| <span id="stage-50"></span>50 | 50=Clearing started | [Rob](../monsters/guynmart_rob.md#v-guynmart_rob5) ([guynmart_wood_6](../maps/guynmart_wood_6.md)) | – | – |
| <span id="stage-51"></span>51 | 51=Clearing_winter<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | – | clears stage 59 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-59) |
| <span id="stage-52"></span>52 | 52=Clearing_tropic<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 51 | clears stage 51 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-51) |
| <span id="stage-53"></span>53 | 53=Clearing_lava<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 52 | clears stage 52 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-52) |
| <span id="stage-54"></span>54 | 54=Clearing_abstract<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 53 | clears stage 53 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-53) |
| <span id="stage-55"></span>55 | 55=Clearing_inverted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 54 | clears stage 54 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-54) |
| <span id="stage-59"></span>59 | 59=Clearing_normal<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Beekeeper2](../maps/beekeeper2.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 55 | clears stage 55 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-55) |
| <span id="stage-60"></span>60 | 60=Hannah rant 0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 1](../maps/guynmart_wood_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 8](../maps/guynmart_wood_8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md)<br>stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 63 | sets stage 181 of [Roses](../quests/guynmart.md#stage-181)<br>clears stage 63 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-63) |
| <span id="stage-61"></span>61 | 61=Hannah rant 1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) | stage 60 | clears stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60) |
| <span id="stage-62"></span>62 | 62=Hannah rant 2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) | stage 61 | clears stage 61 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-61) |
| <span id="stage-63"></span>63 | 63=Hannah rant 3<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart main 1](../maps/guynmart_main_1.md).</span> | stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) | stage 62 | clears stage 62 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-62) |
| <span id="stage-99"></span>99 | 99 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [guynmart_wood_2](../maps/guynmart_wood_2.md) → the conversation leads here automatically — **conditions:** killed 1× [Cute dog puppy](../monsters/guynmart_dog_puppy.md); NOT reached stage 1 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-1) → **stage 1**; also spawns monsters on guynmart_wood_2, spawns monsters on guynmart_wood_2

???+ note "Stage 2: 2 routes"

    1. stepping on a trigger on [guynmart_gate_2](../maps/guynmart_gate_2.md) → choose “Open” — **conditions:** NOT reached stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2); reached stage 170 of [Roses](../quests/guynmart.md#stage-170) → **stage 2**. NPC: “Done, the gate is open.”
    2. stepping on a trigger on [guynmart_gate_2](../maps/guynmart_gate_2.md) → choose “Open” — **conditions:** NOT reached stage 2 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-2) → **stage 2**; also sets stage 164 of [Roses](../quests/guynmart.md#stage-164), removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart, removes monsters from guynmart_main_2, removes monsters from guynmart_main_1, spawns monsters on guynmart, spawns monsters on guynmart_main_2, spawns monsters on guynmart_main_1. NPC: “Done, the gate is open, and Guynmart's personal guard can enter. I should leave quickly now, maybe to the farmhouse…”

???+ note "Stage 4: 2 routes"

    1. Talk to [Fjoerkard](../monsters/guynmart_drunkard1.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) → the conversation leads here automatically → **stage 4**. NPC: “Hey, get us some bottles of wine and then take a seat. I could tell you things you wouldn't believe!”
    2. Talk to [Fjoerkard](../monsters/guynmart_drunkard1.md) ([guynmart_main_2](../maps/guynmart_main_2.md)) → the conversation leads here automatically — **conditions:** carry 1× [Wine](../items/guynmart_wine.md) → **stage 4**. NPC: “Hey, why don't you take a seat and open one of those bottles of wine you have. I could tell you things you wouldn't…”

???+ note "Stage 5: 3 routes"

    1. stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) → the conversation leads here automatically → **stage 5**
    2. stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) → the conversation leads here automatically → **stage 5**
    3. stepping on a trigger on [guynmart_main_2](../maps/guynmart_main_2.md) → the conversation leads here automatically → **stage 5**

???+ note "Stage 6: 1 route"

    1. Talk to [Lovis](../monsters/guynmart_lovis.md) ([guynmart_tower_0](../maps/guynmart_tower_0.md)) → choose “Here, I should give you this.” — **conditions:** hand over 1× [Lovis' Flute](../items/guynmart_flute.md) → **stage 6**; also sets stage 132 of [Roses](../quests/guynmart.md#stage-132), starts timer “guynmart_flute”. NPC: “My flute! How I have missed it! I believe you now.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → choose “$playername, please.” — **conditions:** NOT reached stage 31 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-31); NOT reached stage 30 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-30) → **stage 30**

???+ note "Stage 31: 2 routes"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 31 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-31) → **stage 31**. NPC: “$playername enters!”
    2. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 31 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-31); NOT reached stage 30 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-30) → **stage 31**. NPC: “Who may I please announce?”

???+ note "Stage 32: 3 routes"

    1. Talk to [Gold](../monsters/guynmart_reward1.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the gold.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 32**; also sets stage 201 of [Roses](../quests/guynmart.md#stage-201), gives 5000× [Gold coins](../items/gold.md), removes monsters from guynmart_main_1. NPC: “You feel the pleasant weight of the gold in your bag.”
    2. Talk to [Wisdom](../monsters/guynmart_reward2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the scroll.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 32**; also sets stage 202 of [Roses](../quests/guynmart.md#stage-202), gives 1× [Scroll of wisdom](../items/guynmart_scroll.md), removes monsters from guynmart_main_1. NPC: “You feel an immediate benefit from the experience of others.”
    3. Talk to [Armor](../monsters/guynmart_reward3.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “You decide for the shield.” — **conditions:** NOT reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 32**; also sets stage 203 of [Roses](../quests/guynmart.md#stage-203), gives 1× [Guynmart shield](../items/guynmart_shield.md), removes monsters from guynmart_main_1. NPC: “This shield does feel good in your hands.”

???+ note "Stage 33: 3 routes"

    1. Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “Here is the gold.” — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190); killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181); killed 25× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); pay 2,500 gold → **stage 33**; also removes monsters from guynmart_main_1. NPC: “[Gold taken] All the sheep you killed are paid for, so now we will forget the whole thing.”
    2. Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Here is the gold.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181); killed 25× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); pay 2,500 gold → **stage 33**; also removes monsters from guynmart_main_1. NPC: “[Gold taken] All the sheep you killed are paid for, so now we will forget the whole thing.”
    3. Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “Here is the gold.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181); killed 25× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); pay 2,500 gold → **stage 33**; also removes monsters from guynmart_main_1. NPC: “[Gold taken] All the sheep you killed are paid for, so now we will forget the whole thing.”

???+ note "Stage 34: 1 route"

    1. Talk to [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) → the conversation leads here automatically → **stage 34**; also removes monsters from guynmart_main_1, removes monsters from guynmart_main_2

???+ note "Stage 35: 1 route"

    1. Talk to [Old man](../monsters/old_man.md#v-guynmart_wise) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “I am not afraid. What happened to you?” → **stage 35**. NPC: “From time to time a friendly soul brings me some food, but no one stays for long. I have noticed that their pace…”

???+ note "Stage 36: 8 routes"

    1. Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 36**
    2. Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “Oh yes - I am overwhelmed by your generosity!” — **conditions:** reached stage 32 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) → **stage 36**
    3. Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190); killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 210 of [Roses](../quests/guynmart.md#stage-210), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    4. Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 210 of [Roses](../quests/guynmart.md#stage-210), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    5. Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 210 of [Roses](../quests/guynmart.md#stage-210), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9
    6. Talk to [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** reached stage 190 of [Roses](../quests/guynmart.md#stage-190); killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 211 of [Roses](../quests/guynmart.md#stage-211), removes monsters from guynmart_main_1
    7. Talk to [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2) ([guynmart_main_0](../maps/guynmart_main_0.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 211 of [Roses](../quests/guynmart.md#stage-211), removes monsters from guynmart_main_1
    8. Talk to [Unkorh](../monsters/guynmart_steward.md#v-guynmart_steward5) ([guynmart_main_1](../maps/guynmart_main_1.md)) → choose “I will go. Bye.” — **conditions:** killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-33); reached stage 181 of [Roses](../quests/guynmart.md#stage-181) → **stage 36**; also sets stage 211 of [Roses](../quests/guynmart.md#stage-211), removes monsters from guynmart_main_1

???+ note "Stage 41: 1 route"

    1. stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) → the conversation leads here automatically → **stage 41**; also clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42), clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43), clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44), clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45)

???+ note "Stage 42: 1 route"

    1. stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) → the conversation leads here automatically → **stage 42**; also clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41), clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43), clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44), clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45)

???+ note "Stage 43: 1 route"

    1. stepping on a trigger on [guynmart_wood_11](../maps/guynmart_wood_11.md) → the conversation leads here automatically → **stage 43**; also clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41), clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42), clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44), clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45)

???+ note "Stage 44: 1 route"

    1. stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) → the conversation leads here automatically → **stage 44**; also clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41), clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42), clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43), clears stage 45 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-45)

???+ note "Stage 45: 1 route"

    1. stepping on a trigger on [guynmart_wood_10](../maps/guynmart_wood_10.md) → the conversation leads here automatically → **stage 45**; also clears stage 41 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-41), clears stage 42 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-42), clears stage 43 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-43), clears stage 44 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-44)

???+ note "Stage 50: 1 route"

    1. Talk to [Rob](../monsters/guynmart_rob.md#v-guynmart_rob5) ([guynmart_wood_6](../maps/guynmart_wood_6.md)) → the conversation leads here automatically → **stage 50**. NPC: “I like this place very much. Each time I return here, I get a surprise.”

???+ note "Stage 51: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 51**; also clears stage 59 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-59)

???+ note "Stage 52: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 51 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-51) → **stage 52**; also clears stage 51 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-51)

???+ note "Stage 53: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 52 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-52) → **stage 53**; also clears stage 52 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-52)

???+ note "Stage 54: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 53 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-53) → **stage 54**; also clears stage 53 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-53)

???+ note "Stage 55: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 54 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-54) → **stage 55**; also clears stage 54 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-54)

???+ note "Stage 59: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 55 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-55) → **stage 59**; also clears stage 55 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-55)

???+ note "Stage 60: 3 routes"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 60**; also sets stage 181 of [Roses](../quests/guynmart.md#stage-181)
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 170 of [Roses](../quests/guynmart.md#stage-170); reached stage 161 of [Roses](../quests/guynmart.md#stage-161) → **stage 60**; also sets stage 181 of [Roses](../quests/guynmart.md#stage-181)
    3. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 63 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-63) → **stage 60**; also clears stage 63 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-63). NPC: “You love to watch my misery, don't you? Do you think I'm crazy?”

???+ note "Stage 61: 1 route"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60) → **stage 61**; also clears stage 60 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-60). NPC: “DON'T COME ANY CLOSER!”

???+ note "Stage 62: 1 route"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 61 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-61) → **stage 62**; also clears stage 61 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-61). NPC: “You dare to come here again! I hate you!”

???+ note "Stage 63: 1 route"

    1. stepping on a trigger on [guynmart_main_1](../maps/guynmart_main_1.md) → the conversation leads here automatically — **conditions:** reached stage 62 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-62) → **stage 63**; also clears stage 62 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-62). NPC: “Leave now, or I will call the guards!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 44 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 7 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 30, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 99 |
    | Dialogue nodes setting stages | 1: `guynmart_s_dog_puppy_10`, 2: `guynmart_s_gate1_56`, 2: `guynmart_s_gate1_58`, 4: `guynmart_drunkard1_20`, 4: `guynmart_drunkard1_30`, 5: `guynmart_seat1`, 5: `guynmart_seat3`, 5: `guynmart_seat5`, 6: `guynmart_lovis_40`, 30: `guynmart_s_herold_14`, 31: `guynmart_s_herold_10`, 31: `guynmart_s_herold_12`, 32: `guynmart_reward1_20`, 32: `guynmart_reward2_20`, 32: `guynmart_reward3_20`, 33: `guynmart_lovis2_360`, 34: `guynmart_hannah_10`, 35: `guynmart_wise_102`, 36: `guynmart_lovis2_130`, 36: `guynmart_lovis2_240`, 36: `guynmart_lovis2_241`, 41: `guynmart_s_hill1`, 42: `guynmart_s_hill2`, 43: `guynmart_s_hill3`, 44: `guynmart_s_hill4`, 45: `guynmart_s_hill5`, 50: `guynmart_rob5_30`, 51: `guynmart_s_clearing_51`, 52: `guynmart_s_clearing_52`, 53: `guynmart_s_clearing_53`, 54: `guynmart_s_clearing_54`, 55: `guynmart_s_clearing_55`, 59: `guynmart_s_clearing_59`, 60: `guynmart_sRpl_main_1r_20`, 60: `guynmart_s_hannah_63`, 61: `guynmart_s_hannah_60`, 62: `guynmart_s_hannah_61`, 63: `guynmart_s_hannah_62` |
    | Dialogue nodes clearing stages | 5: `guynmart_seat2`, 5: `guynmart_seat4`, 2: `guynmart_s_gate1_62`, 2: `guynmart_s_gate1_64`, 60: `guynmart_s_hannah_60`, 61: `guynmart_s_hannah_61`, 62: `guynmart_s_hannah_62`, 63: `guynmart_s_hannah_63`, 31: `guynmart_s_herold_out`, 34: `guynmart_s_gateopenrest_10` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
