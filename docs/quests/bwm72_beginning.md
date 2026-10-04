# Hidden: events in bwm

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bwm72_beginning` |
| **In journal** | No (hidden flag) |
| **Stages** | 42 |
| **Started by** | stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md), stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) |
| **NPCs involved** | [Arghest](../monsters/arghest.md), [Dying general's henchman](../monsters/ortholion_guard8.md), [Ehrenfest](../monsters/ehrenfest.md), [General Ortholion](../monsters/ortholion.md), [Jern](../monsters/prim_bar_regular.md), [Kamelio](../monsters/kamelio.md) +4 |
| **Locations** | [blackwater_mountain11](../maps/blackwater_mountain11.md), [blackwater_mountain13](../maps/blackwater_mountain13.md), [blackwater_mountain22](../maps/blackwater_mountain22.md), [blackwater_mountain29](../maps/blackwater_mountain29.md) |
| **Total XP** | 850 |
| **Related quests** | 1 |

</div>

## Overview

> First corpse discovered

## Prerequisites to start

None: talk to stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-5) | stage 5 reached, for stages 5, 6, 7 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-6) | stage 6 reached, for stage 5 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-11) | stage 11 reached, for stage 8 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-20) | stage 20 reached, for stages 9, 10 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-23) | stage 23 reached, for stage 37 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-33) | stage 33 reached, for stages 15, 16, 21 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-34) | stage 34 reached, for stage 21 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-36) | stage 36 reached, for stage 17 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-40) | stage 40 reached, for stage 20 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-45) | stage 45 reached, for stage 16 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-47) | stage 47 reached, for stage 22 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-54) | stage 54 reached, for stage 41 here |
| Requires | [Climbing up is forbidden](Omi2_bwm1.md#stage-56) | stage 56 reached, for stages 42, 43 here |
| Blocked by | [Climbing up is forbidden](Omi2_bwm1.md#stage-21) | stage 21 must NOT be reached, for stage 10 here |
| Blocked by | [Climbing up is forbidden](Omi2_bwm1.md#stage-41) | stage 41 must NOT be reached, for stage 20 here |
| Blocked by | [Climbing up is forbidden](Omi2_bwm1.md#stage-54) | stage 54 must NOT be reached, for stage 38 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-5) | stage 5 there needs stage 3 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-10) | stage 10 there needs stage 6 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-11) | stage 11 there needs stage 7 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-21) | stage 21 there needs stage 9 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-24) | stage 24 there needs stage 12 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-30) | stage 30 there needs stage 13 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-31) | stage 31 there needs stage 14 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-40) | stage 40 there needs stage 18 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-45) | stage 45 there needs stage 21 here |
| Unlocks | [Climbing up is forbidden](Omi2_bwm1.md#stage-50) | stage 50 there needs stage 35 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | First corpse discovered <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain72](../maps/blackwater_mountain72.md).</span> | stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) | – | – |
| <span id="stage-2"></span>2 | Second corpse discovered<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain72](../maps/blackwater_mountain72.md).</span> | stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) | stage 1 | – |
| <span id="stage-3"></span>3 | Third corpse discovered<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain72](../maps/blackwater_mountain72.md).</span> | stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) | stage 2 | – |
| <span id="stage-4"></span>4 | Torture signs discovered<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain72](../maps/blackwater_mountain72.md).</span> | stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) | stage 3 | 300 XP<br>gives 1× [Blood-stained rope](../items/bwm72_rope.md)<br>sets stage 5 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-5)<br>spawns monsters on blackwater_mountain11 |
| <span id="stage-5"></span>5 | Keyfield on Bwm29<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain11](../maps/blackwater_mountain11.md).</span><br><span class="qnote">🔒 An area on [Blackwater mountain29](../maps/blackwater_mountain29.md) becomes blocked off.</span> | stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md)<br>[Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | carry 1× [Blood-stained rope](../items/bwm72_rope.md) | sets stage 7 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-7)<br>spawns monsters on blackwater_mountain29 |
| <span id="stage-6"></span>6 | Conversation with Ehrenfest starts before Ortholion appears.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain11](../maps/blackwater_mountain11.md).</span> | stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md)<br>[Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | carry 1× [Blood-stained rope](../items/bwm72_rope.md) | – |
| <span id="stage-7"></span>7 | Conversation with Ehrenfest starts after Ortholion leaves.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain11](../maps/blackwater_mountain11.md).</span> | stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md)<br>[Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | carry 1× [Blood-stained rope](../items/bwm72_rope.md), stage 6 | sets stage 10 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-10)<br>spawns monsters on blackwater_mountain10<br>spawns monsters on blackwater_mountain11 |
| <span id="stage-8"></span>8 | Ehrenfest notices your presence in the mine and calls you.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain13](../maps/blackwater_mountain13.md).</span> | stepping on a trigger on [blackwater_mountain13](../maps/blackwater_mountain13.md) | – | – |
| <span id="stage-9"></span>9 | Moyra's info. | [Moyra](../monsters/moyra.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | – | 125 XP |
| <span id="stage-10"></span>10 | Prim's Evoker info. | [Prim evoker](../monsters/prim_evoker.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | – | 75 XP |
| <span id="stage-11"></span>11 | Wellspring dialogue & hole. (Never-true condition)<br><span class="qnote">🔓 You can finally access a previously blocked area on [Blackwater mountain74 h](../maps/blackwater_mountain74_h.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Blackwater mountain75](../maps/blackwater_mountain75.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm 2f 1](../maps/elm_2f_1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm 4f 5](../maps/elm_4f_5.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine2](../maps/elm_mine2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine3](../maps/elm_mine3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine4](../maps/elm_mine4.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine5](../maps/elm_mine5.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm5f 2](../maps/elm5f_2.md).</span> | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-12"></span>12 | One bottle of water. | walking into a blocked passage on [blackwater_mountain75](../maps/blackwater_mountain75.md) | hand over 1× [Empty flask](../items/vial_empty3.md) | gives [Cold bottle of mountain water](../items/bwm_water1_quest.md) |
| <span id="stage-13"></span>13 | Middle point conversation with Jern. | [Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) | – | – |
| <span id="stage-14"></span>14 | Choice (Ehrenfest vs Jern) | [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) | – | – |
| <span id="stage-15"></span>15 | Cabin warning<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain30](../maps/blackwater_mountain30.md).</span> | stepping on a trigger on [blackwater_mountain30](../maps/blackwater_mountain30.md) | – | spawns monsters on blackwater_mountain31 |
| <span id="stage-16"></span>16 | Cabin compulsory exploration.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain30](../maps/blackwater_mountain30.md).</span><br><span class="qnote">🔒 An area on [Blackwater mountain30](../maps/blackwater_mountain30.md) becomes blocked off.</span> | stepping on a trigger on [blackwater_mountain30](../maps/blackwater_mountain30.md)<br>walking into a blocked passage on [blackwater_mountain30](../maps/blackwater_mountain30.md) | – | spawns monsters on blackwater_mountain31 |
| <span id="stage-17"></span>17 | Jern vs Guard Captain<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain11](../maps/blackwater_mountain11.md).</span> | stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md) | – | removes monsters from blackwater_mountain29<br>spawns monsters on blackwater_mountain29 |
| <span id="stage-18"></span>18 | Jern & Guard Cap. convo. | [Prim guard captain](../monsters/prim_guard5.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md))<br>[Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) | – | – |
| <span id="stage-20"></span>20 | Subdued Feygard mountain scout<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain32](../maps/blackwater_mountain32.md).</span><br><span class="qnote">🔒 An area on [Blackwater mountain32](../maps/blackwater_mountain32.md) becomes blocked off.</span> | stepping on a trigger on [blackwater_mountain32](../maps/blackwater_mountain32.md) | – | spawns monsters on blackwater_mountain32 |
| <span id="stage-21"></span>21 | Ortholion's kick. | [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md))<br>[General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | applies condition confusion |
| <span id="stage-22"></span>22 | Arghest small talk.<br><span class="qnote">🗺️ Part of [Blackwater mountain13](../maps/blackwater_mountain13.md) visibly changes.</span> | [Arghest](../monsters/arghest.md) ([blackwater_mountain13](../maps/blackwater_mountain13.md)) | hand over 1× [Minor potion of strength](../items/pot_str.md) | – |
| <span id="stage-23"></span>23 | Torch secret<br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine2](../maps/elm_mine2.md).</span> | walking into a blocked passage on [elm_mine2](../maps/elm_mine2.md) | hand over 1× [Miner's lamp fuel](../items/torch.md) | 100 XP |
| <span id="stage-24"></span>24 | Elm3 corpse. | walking into a blocked passage on [elm_mine3](../maps/elm_mine3.md) | – | applies condition shadow_prot<br>gives [Iqhan pendant](../items/iqhan_pendant.md), [Torn shirt](../items/shirt_torn.md), [Gold coins](../items/gold.md) |
| <span id="stage-25"></span>25 | Elm2 chest.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm mine2](../maps/elm_mine2.md).</span> | walking into a blocked passage on [elm_mine2](../maps/elm_mine2.md) | hand over 1× [Rusted key](../items/elm2_key.md) | 250 XP |
| <span id="stage-26"></span>26 | Elm4 sign (north)<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm mine4](../maps/elm_mine4.md).</span> | stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) | – | clears stage 27 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-27) |
| <span id="stage-27"></span>27 | Elm4 sign (south)<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm mine4](../maps/elm_mine4.md).</span> | stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) | – | clears stage 26 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-26) |
| <span id="stage-28"></span>28 | Elm4 hole <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm mine4](../maps/elm_mine4.md).</span><br><span class="qnote">🗺️ Part of [Elm mine4](../maps/elm_mine4.md) visibly changes.</span> | stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) | – | applies condition bleeding_wound |
| <span id="stage-29"></span>29 | Elm5 first ore.<br><span class="qnote">🗺️ Part of [Elm mine5](../maps/elm_mine5.md) visibly changes.</span> | walking into a blocked passage on [elm_mine5](../maps/elm_mine5.md) | carry 1× [Blackwater rusted pickaxe](../items/bwm_pick.md) | gives 1× [Unknown gem (extracted from the Elm mine)](../items/elm_gem_u.md)<br>applies condition nausea |
| <span id="stage-30"></span>30 | Elm5 hole.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm mine5](../maps/elm_mine5.md).</span><br><span class="qnote">🗺️ Part of [Elm mine5](../maps/elm_mine5.md) visibly changes.</span> | stepping on a trigger on [elm_mine5](../maps/elm_mine5.md) | – | applies condition bleeding_wound<br>applies condition concussion |
| <span id="stage-31"></span>31 | Elm5 plunder. | [Dying general's henchman](../monsters/ortholion_guard8.md) ([elm_mine5](../maps/elm_mine5.md)) | stage 32 | starts timer “elm5_corpse” |
| <span id="stage-32"></span>32 | Elm5 corpse. | [Dying general's henchman](../monsters/ortholion_guard8.md) ([elm_mine5](../maps/elm_mine5.md)) | – | – |
| <span id="stage-33"></span>33 | Elm2f2 chest<br><span class="qnote">🔓 You can finally access a previously blocked area on [Elm 2f 2](../maps/elm_2f_2.md).</span> | walking into a blocked passage on [elm_2f_2](../maps/elm_2f_2.md) | – | changes map elm_2f_2 |
| <span id="stage-34"></span>34 | Elm3f timer starts.<br><span class="qnote">🔒 An area on [Elm 3f](../maps/elm_3f.md) becomes blocked off.</span> | [Ortholion's henchman](../monsters/ortholion_guard9.md) ([elm_3f](../maps/elm_3f.md)) | – | starts timer “elm3f_grow” |
| <span id="stage-35"></span>35 | Bad opinion from Ortholion's remaining henchman | [Ortholion's henchman](../monsters/ortholion_guard9.md) ([elm_3f](../maps/elm_3f.md)) | – | clears stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34)<br>sets stage 50 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-50) |
| <span id="stage-36"></span>36 | Elm 4f level 0 to 1.<br><span class="qnote">⚡ A scripted event can now trigger on [Elm 4f 1](../maps/elm_4f_1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm 4f 1](../maps/elm_4f_1.md).</span><br><span class="qnote">🗺️ Part of [Elm 4f 1](../maps/elm_4f_1.md) visibly changes.</span> | stepping on a trigger on [elm_4f_1](../maps/elm_4f_1.md) | – | – |
| <span id="stage-37"></span>37 | Fight against Kamelio (1) already started. | [Kamelio](../monsters/kamelio.md) ([elm5f_2](../maps/elm5f_2.md)) | – | spawns monsters on elm5f_2 |
| <span id="stage-38"></span>38 | Kamelio's first death.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Elm5f 2](../maps/elm5f_2.md).</span><br><span class="qnote">🔒 An area on [Elm5f 2](../maps/elm5f_2.md) becomes blocked off.</span> | stepping on a trigger on [elm5f_2](../maps/elm5f_2.md) | – | – |
| <span id="stage-39"></span>39 | Kamelio's resurrection | [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | applies condition putrefaction<br>spawns monsters on elm5f_2 |
| <span id="stage-40"></span>40 | Celebration<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain13](../maps/blackwater_mountain13.md).</span> | stepping on a trigger on [blackwater_mountain13](../maps/blackwater_mountain13.md) | stage 41 | spawns monsters on elm_mine1 |
| <span id="stage-41"></span>41 | Pre-celebration<br><span class="qnote">⚡ A scripted event can now trigger on [Elm5f 2](../maps/elm5f_2.md).</span> | [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-42"></span>42 | "Climbing up is forbidden" finished. | [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | gives 2000× [Gold coins](../items/gold.md)<br>starts timer “ortholion_next1”<br>sets stage 59 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-59)<br>gives 30× [Mundane necklace](../items/junk_necklace0.md)<br>gives 20× [Mundane ring](../items/ring1.md)<br>sets stage 60 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-60)<br>sets stage 61 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-61)<br>gives 50× [Gold coins](../items/gold.md)<br>sets stage 62 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-62)<br>gives 1× [Ortholion's talisman](../items/ortholion_reward.md)<br>sets stage 63 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-63) |
| <span id="stage-43"></span>43 | Conversation with Jern & the Captain. | [Prim guard captain](../monsters/prim_guard5.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md))<br>[Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) | stage 18 | gives 1× [Rusted key](../items/elm2_key.md)<br>removes monsters from blackwater_mountain29 |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 3 routes"

    1. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically → **stage 1**. NPC: “You see a corpse, much more decomposed than the one you saw on the hillside, and wrapped up in cobwebs. What kind of…”
    2. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically → **stage 1**. NPC: “You see a corpse, much more decomposed than the one you saw on the hillside, and wrapped up in cobwebs. What kind of…”
    3. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically → **stage 1**. NPC: “You see a corpse, much more decomposed than the one you saw on the hillside, and wrapped up in cobwebs. What kind of…”

???+ note "Stage 2: 6 routes"

    1. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “Yet another corpse in the same state as the previous one. One of its legs seems violently fractured.”
    2. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “Yet another corpse in the same state as the previous one. One of its legs seems violently fractured.”
    3. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “Yet another corpse in the same state as the previous one. One of its legs seems violently fractured.”
    4. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → choose “Take a closer look.” — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “That is certainly not a wound one of these spiders would cause. There's something strange about all this.”
    5. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → choose “Take a closer look.” — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “That is certainly not a wound one of these spiders would cause. There's something strange about all this.”
    6. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → choose “Take a closer look.” — **conditions:** reached stage 1 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-1) → **stage 2**. NPC: “That is certainly not a wound one of these spiders would cause. There's something strange about all this.”

???+ note "Stage 3: 3 routes"

    1. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-2) → **stage 3**. NPC: “This one is the most decayed of all corpses you saw here. Who are these people?”
    2. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-2) → **stage 3**. NPC: “This one is the most decayed of all corpses you saw here. Who are these people?”
    3. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-2) → **stage 3**. NPC: “This one is the most decayed of all corpses you saw here. Who are these people?”

???+ note "Stage 4: 1 route"

    1. stepping on a trigger on [blackwater_mountain72](../maps/blackwater_mountain72.md) → choose “Examine the scene.” — **conditions:** reached stage 3 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-3) → **stage 4**; also gives 1× [Blood-stained rope](../items/bwm72_rope.md), sets stage 5 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-5), spawns monsters on blackwater_mountain11. NPC: “After several minutes of careful but fruitless search, you decide to take one of the ropes as evidence of the torture.”

???+ note "Stage 5: 2 routes"

    1. stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md) → choose “You never know...” — **conditions:** latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-5) is 5; carry 1× [Blood-stained rope](../items/bwm72_rope.md) → **stage 5**; also sets stage 7 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-7), spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29. NPC: “OK, kid. Do it, and I'll wait here for your return, heh. By the way, my name is Ehrenfest.”
    2. Talk to [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “I will try anyway, thanks.” — **conditions:** latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-6) is 6 → **stage 5**; also sets stage 7 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-7), spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29. NPC: “OK, kid. Do it, and I'll wait here for your return, heh. By the way, my name is Ehrenfest.”

???+ note "Stage 6: 2 routes"

    1. stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md) → choose “Care to explain?” — **conditions:** latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-5) is 5; carry 1× [Blood-stained rope](../items/bwm72_rope.md) → **stage 6**. NPC: “This is not a good place to talk about this. But trust me, there is much at stake and Prim's situation is only going…”
    2. Talk to [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → the conversation leads here automatically — **conditions:** reached stage 6 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-6) → **stage 6**. NPC: “This is not a good place to talk about this. But trust me, there is much at stake and Prim's situation is only going…”

???+ note "Stage 7: 2 routes"

    1. stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md) → choose “Care to explain?” — **conditions:** latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-5) is 5; carry 1× [Blood-stained rope](../items/bwm72_rope.md) → **stage 7**; also sets stage 10 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-10), spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain11, spawns monsters on blackwater_mountain11. NPC: “Yes, my general.”
    2. Talk to [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → the conversation leads here automatically — **conditions:** reached stage 6 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-6) → **stage 7**; also sets stage 10 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-10), spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain10, spawns monsters on blackwater_mountain11, spawns monsters on blackwater_mountain11. NPC: “Yes, my general.”

???+ note "Stage 8: 1 route"

    1. stepping on a trigger on [blackwater_mountain13](../maps/blackwater_mountain13.md) → the conversation leads here automatically — **conditions:** reached stage 11 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-11); NOT reached stage 8 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-8) → **stage 8**. NPC: “Someone is whispering: "Psst, come! Come here!" The voice is coming from the dining room.”

???+ note "Stage 9: 1 route"

    1. Talk to [Moyra](../monsters/moyra.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “What about his partners?” — **conditions:** reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 9 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-9) → **stage 9**. NPC: “They're still missing, but I don't know...”

???+ note "Stage 10: 1 route"

    1. Talk to [Prim evoker](../monsters/prim_evoker.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “Right, uhm...don't you remember anything about him?” — **conditions:** reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 21 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-21) → **stage 10**. NPC: “Uhm, well. I heard Lorn was popular among the children here in Prim because of his scary stories about, you know, the…”

???+ note "Stage 12: 1 route"

    1. walking into a blocked passage on [blackwater_mountain75](../maps/blackwater_mountain75.md) → choose “Fill a bottle of water.” — **conditions:** hand over 1× [Empty flask](../items/vial_empty3.md); NOT reached stage 12 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-12) → **stage 12**; also gives [Cold bottle of mountain water](../items/bwm_water1_quest.md). NPC: “You fill the bottle with water.”

???+ note "Stage 13: 1 route"

    1. Talk to [Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) → the conversation leads here automatically — **conditions:** reached stage 13 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-13) → **stage 13**. NPC: “Lorn must have discovered something. Just a week or two ago we were right here bantering and chatting, trying to…”

???+ note "Stage 14: 1 route"

    1. Talk to [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → the conversation leads here automatically — **conditions:** reached stage 14 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-14) → **stage 14**. NPC: “I won't try to convince you. Now you must decide whether to help me or not. I won't ask twice, so make your choice…”

???+ note "Stage 15: 1 route"

    1. stepping on a trigger on [blackwater_mountain30](../maps/blackwater_mountain30.md) → the conversation leads here automatically — **conditions:** reached stage 33 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-33); NOT reached stage 15 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-15) → **stage 15**; also spawns monsters on blackwater_mountain31. NPC: “[You hear noises and steps coming from the cabin]”

???+ note "Stage 16: 2 routes"

    1. stepping on a trigger on [blackwater_mountain30](../maps/blackwater_mountain30.md) → the conversation leads here automatically — **conditions:** reached stage 33 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-33); NOT reached stage 15 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-15) → **stage 16**; also spawns monsters on blackwater_mountain31. NPC: “[You hear noises and steps coming from the cabin]”
    2. walking into a blocked passage on [blackwater_mountain30](../maps/blackwater_mountain30.md) → the conversation leads here automatically — **conditions:** reached stage 45 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-45) → **stage 16**

???+ note "Stage 17: 1 route"

    1. stepping on a trigger on [blackwater_mountain11](../maps/blackwater_mountain11.md) → the conversation leads here automatically — **conditions:** reached stage 36 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-36); NOT reached stage 17 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-17) → **stage 17**; also removes monsters from blackwater_mountain29, spawns monsters on blackwater_mountain29, spawns monsters on blackwater_mountain29. NPC: “*crush* WHAT THE HELL JERN?! [A fight is happening inside, better to hurry up]”

???+ note "Stage 18: 2 routes"

    1. Talk to [Prim guard captain](../monsters/prim_guard5.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 18 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-18) → **stage 18**. NPC: “We're short of men, and we don't even know where he is right now. *Meanwhile Jern stares at you.*”
    2. Talk to [Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) → the conversation leads here automatically — **conditions:** reached stage 18 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-18) → **stage 18**. NPC: “We're short of men, and we don't even know where he is right now. *Meanwhile Jern stares at you.*”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [blackwater_mountain32](../maps/blackwater_mountain32.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-40); NOT reached stage 20 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-20); NOT reached stage 41 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-41) → **stage 20**; also spawns monsters on blackwater_mountain32. NPC: “You hear steps up in the mountain. It seems a Feygard soldier is guarding the cave entrance. General Ortholion must…”

???+ note "Stage 21: 2 routes"

    1. Talk to [Ehrenfest](../monsters/ehrenfest.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “Die!” — **conditions:** reached stage 34 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-34); reached stage 33 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-33); NOT reached stage 21 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-21) → **stage 21**; also applies condition confusion. NPC: “Just before starting to launch an attack, General Ortholion moves and disarms you with a single blow.”
    2. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Die!” — **conditions:** reached stage 34 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-34); reached stage 33 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-33); NOT reached stage 21 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-21) → **stage 21**; also applies condition confusion. NPC: “Just before starting to launch an attack, General Ortholion moves and disarms you with a single blow.”

???+ note "Stage 22: 1 route"

    1. Talk to [Arghest](../monsters/arghest.md) ([blackwater_mountain13](../maps/blackwater_mountain13.md)) → choose “Would you like this 'Minor potion of strength'?” — **conditions:** reached stage 47 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-47); NOT reached stage 22 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-22); hand over 1× [Minor potion of strength](../items/pot_str.md) → **stage 22**. NPC: “Really? Many many thanks - you make my old heart cry!”

???+ note "Stage 23: 1 route"

    1. walking into a blocked passage on [elm_mine2](../maps/elm_mine2.md) → choose “Add fuel to the miner's lamp.” — **conditions:** hand over 1× [Miner's lamp fuel](../items/torch.md) → **stage 23**. NPC: “A weak fire illuminates the place. The tunnel is collapsed, but there are some trinkets and clothes on the floor.”

???+ note "Stage 24: 2 routes"

    1. walking into a blocked passage on [elm_mine3](../maps/elm_mine3.md) → choose “May the Shadow be with your soul.” → **stage 24**; also applies condition shadow_prot. NPC: “After a few seconds, you feel a little dumb talking to a corpse and leave.”
    2. walking into a blocked passage on [elm_mine3](../maps/elm_mine3.md) → choose “Plunder the corpse.” → **stage 24**; also gives [Iqhan pendant](../items/iqhan_pendant.md), [Torn shirt](../items/shirt_torn.md), [Gold coins](../items/gold.md). NPC: “Everything seems too old and stinky to be worth anything much, but after half a minute of searching you see a strange…”

???+ note "Stage 25: 1 route"

    1. walking into a blocked passage on [elm_mine2](../maps/elm_mine2.md) → choose “Use Jern's rusty key.” — **conditions:** hand over 1× [Rusted key](../items/elm2_key.md) → **stage 25**. NPC: “Despite the rust, you introduce the key in the lock without major trouble. It seems to fit well enough. The chest is…”

???+ note "Stage 26: 1 route"

    1. stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) → the conversation leads here automatically → **stage 26**; also clears stage 27 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-27)

???+ note "Stage 27: 1 route"

    1. stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) → the conversation leads here automatically → **stage 27**; also clears stage 26 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-26)

???+ note "Stage 28: 1 route"

    1. stepping on a trigger on [elm_mine4](../maps/elm_mine4.md) → the conversation leads here automatically → **stage 28**; also applies condition bleeding_wound, applies condition bleeding_wound, applies condition bleeding_wound. NPC: “The floor collapses below you, and you fall onto a muddy floor.”

???+ note "Stage 29: 1 route"

    1. walking into a blocked passage on [elm_mine5](../maps/elm_mine5.md) → choose “Take the ore.” — **conditions:** carry 1× [Blackwater rusted pickaxe](../items/bwm_pick.md) → **stage 29**; also gives 1× [Unknown gem (extracted from the Elm mine)](../items/elm_gem_u.md), applies condition nausea, applies condition nausea. NPC: “After some minutes of intense mining you finally get a gem and put it in a safe pocket in your backpack.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [elm_mine5](../maps/elm_mine5.md) → the conversation leads here automatically → **stage 30**; also applies condition bleeding_wound, applies condition bleeding_wound, applies condition bleeding_wound, applies condition concussion. NPC: “There was a hole in the floor just below you and the rails. You stumble upon a crossbar and land flat on your face,…”

???+ note "Stage 31: 1 route"

    1. Talk to [Dying general's henchman](../monsters/ortholion_guard8.md) ([elm_mine5](../maps/elm_mine5.md)) → choose “Plunder.” — **conditions:** reached stage 32 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-32); NOT reached stage 31 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-31) → **stage 31**; also starts timer “elm5_corpse”. NPC: “You try to pull off the armor first but you soon discover both the man and the armor itself are covered by that…”

???+ note "Stage 32: 1 route"

    1. Talk to [Dying general's henchman](../monsters/ortholion_guard8.md) ([elm_mine5](../maps/elm_mine5.md)) → choose “What's wrong?” → **stage 32**. NPC: “*ignoring you*... You idiot kid... *cough*. It's a trap, THE WHOLE THING *cough*, *cough* is... ...This mine is...…”

???+ note "Stage 33: 1 route"

    1. walking into a blocked passage on [elm_2f_2](../maps/elm_2f_2.md) → choose “Try harder.” — **conditions:** faction “elm2f2_chest” = 6 → **stage 33**; also changes map elm_2f_2, changes map elm_2f_2. NPC: “You try pulling the lid again with all your strength. The chest finally tips over and all of its content gets dropped…”

???+ note "Stage 34: 1 route"

    1. Talk to [Ortholion's henchman](../monsters/ortholion_guard9.md) ([elm_3f](../maps/elm_3f.md)) → choose “Why?” — **conditions:** NOT reached stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34) → **stage 34**; also starts timer “elm3f_grow”. NPC: “Look *points to the large crystals*...It grows.”

???+ note "Stage 35: 1 route"

    1. Talk to [Ortholion's henchman](../monsters/ortholion_guard9.md) ([elm_3f](../maps/elm_3f.md)) → the conversation leads here automatically — **conditions:** reached stage 35 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-35) → **stage 35**; also clears stage 34 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-34), sets stage 50 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-50). NPC: “I will leave this place right now and come back with more men anyway! Kids these days...Annoying.”

???+ note "Stage 36: 1 route"

    1. stepping on a trigger on [elm_4f_1](../maps/elm_4f_1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 36 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-36) → **stage 36**

???+ note "Stage 37: 4 routes"

    1. Talk to [Kamelio](../monsters/kamelio.md) ([elm5f_2](../maps/elm5f_2.md)) → choose “I need your help! There's a man lying unconscious there.” → **stage 37**; also spawns monsters on elm5f_2, spawns monsters on elm5f_2. NPC: “Ah...Yes. Don't worry, you go first. *approaches you*”
    2. Talk to [Kamelio](../monsters/kamelio.md) ([elm5f_2](../maps/elm5f_2.md)) → choose “Jern will be glad you're alright.” — **conditions:** reached stage 23 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-23) → **stage 37**; also spawns monsters on elm5f_2, spawns monsters on elm5f_2. NPC: “*approaching you* He's not going to see you alive again.”
    3. Talk to [Kamelio](../monsters/kamelio.md) ([elm5f_2](../maps/elm5f_2.md)) → choose “Hmm, yeah sure. Goodbye.” → **stage 37**; also spawns monsters on elm5f_2, spawns monsters on elm5f_2. NPC: “Not so fast. My mind is clear, you need to die now along with that Feygard scum.”
    4. Talk to [Kamelio](../monsters/kamelio.md) ([elm5f_2](../maps/elm5f_2.md)) → choose “What do you have to do?” → **stage 37**; also spawns monsters on elm5f_2, spawns monsters on elm5f_2. NPC: “Kill you first, then kill the guy over there. That's it.”

???+ note "Stage 38: 2 routes"

    1. stepping on a trigger on [elm5f_2](../maps/elm5f_2.md) → the conversation leads here automatically — **conditions:** killed 1× [Kamelio](../monsters/kamelio.md) → **stage 38**
    2. stepping on a trigger on [elm5f_2](../maps/elm5f_2.md) → the conversation leads here automatically — **conditions:** killed 1× [Kamelio](../monsters/kamelio.md); NOT reached stage 54 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-54) → **stage 38**

???+ note "Stage 39: 1 route"

    1. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “(Lie) I got rid of him.” — **conditions:** killed 1× [Kamelio](../monsters/kamelio.md); NOT reached stage 39 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-39) → **stage 39**; also applies condition putrefaction, applies condition putrefaction, applies condition putrefaction, spawns monsters on elm5f_2, spawns monsters on elm5f_2. NPC: “...D...Die...”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [blackwater_mountain13](../maps/blackwater_mountain13.md) → the conversation leads here automatically — **conditions:** reached stage 41 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-41); NOT reached stage 40 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-40) → **stage 40**; also spawns monsters on elm_mine1, spawns monsters on elm_mine1, spawns monsters on elm_mine1, spawns monsters on elm_mine1, spawns monsters on elm_mine1

???+ note "Stage 41: 1 route"

    1. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Scared?” — **conditions:** reached stage 54 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-54) → **stage 41**. NPC: “Yes, yes... I'll get out of this cave. Meet me at the entrance of the mine. There is a large dining room. That will…”

???+ note "Stage 42: 5 routes"

    1. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “[Take the gold]” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56) → **stage 42**; also gives 2000× [Gold coins](../items/gold.md), starts timer “ortholion_next1”, sets stage 59 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-59). NPC: “Fine. Now let some days pass and meet me again here. I may need your help and you may want more gold.”
    2. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Great! [Take the large bag]” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56) → **stage 42**; also gives 30× [Mundane necklace](../items/junk_necklace0.md), gives 20× [Mundane ring](../items/ring1.md), sets stage 60 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-60), starts timer “ortholion_next1”. NPC: “Fine, it's all for you. Maybe this way you'll learn a lesson. Come see me in some days, you might be of use.”
    3. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “[Take the gold] Finally...” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56) → **stage 42**; also sets stage 61 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-61), starts timer “ortholion_next1”, gives 50× [Gold coins](../items/gold.md). NPC: “Should I be surprised? That shows how valuable your word currently is. Come back in a few days and I may change my…”
    4. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “I can't accept gold for saving someone's life...” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56) → **stage 42**; also sets stage 62 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-62), starts timer “ortholion_next1”, gives 1× [Ortholion's talisman](../items/ortholion_reward.md). NPC: “*Withdraws his hand with the gold bag and makes a nod of approval* Good, good. I accept your choice. Since you said…”
    5. Talk to [General Ortholion](../monsters/ortholion.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “My family is the most important thing to me.” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56) → **stage 42**; also sets stage 63 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-63), starts timer “ortholion_next1”. NPC: “I would say that is a ... very ignorant reply, but I will not judge you today. Go back home and spend some time with…”

???+ note "Stage 43: 2 routes"

    1. Talk to [Prim guard captain](../monsters/prim_guard5.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “You are needed here more.” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56); reached stage 18 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-18) → **stage 43**; also gives 1× [Rusted key](../items/elm2_key.md), removes monsters from blackwater_mountain29. NPC: “Thank you again. *looks at the captain* I'll be going.”
    2. Talk to [Jern](../monsters/prim_bar_regular.md) ([blackwater_mountain22](../maps/blackwater_mountain22.md)) → choose “You are needed here more.” — **conditions:** reached stage 56 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-56); reached stage 18 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-18) → **stage 43**; also gives 1× [Rusted key](../items/elm2_key.md), removes monsters from blackwater_mountain29. NPC: “Thank you again. *looks at the captain* I'll be going.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 56 lines added |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 2 lines changed |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 2 lines changed<br>· text: “Everything seems too old and stinky to be worth a penny, but after ha…” → “Everything seems too old and stinky to be worth anything much, but af…” |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 2 lines changed<br>· text: “Just before starting to launch any attack, General Ortholion moves an…” → “Just before starting to launch an attack, General Ortholion moves and…”<br>· text: “You try to put off the armor first but you soon discover both the man…” → “You try to pull off the armor first but you soon discover both the ma…” |
| [v0.8.8](../versions/0.8.8.md) | stages added: 43<br>Dialogue: 1 line added, 2 lines changed<br>· text: “This is humilating enough... I'll get out of this cave. I'll be at th…” → “Yes, yes... I'll get out of this cave. Meet me at the entrance of the…” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm72_beginning.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm72_beginning.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm72_beginning.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm72_beginning.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm72_beginning.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bwm72_beginning` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 |
    | Dialogue nodes setting stages | 1: `bwm72_corpse1_1`, 2: `bwm72_corpse2_1`, 2: `bwm72_corpse2_2`, 3: `bwm72_corpse3_1`, 4: `bwm72_torture_2`, 5: `ehrenfest_3a`, 6: `ehrenfest_3b`, 7: `ehrenfest_conversation_4`, 8: `ehrenfest_calling_1`, 9: `moyra_11`, 10: `prim_commoner4_6`, 12: `bwm_wellspring_2a`, 13: `prim_tavern_guest4_33a`, 14: `ehrenfest_38a`, 15: `bwm30_ortholion_guards`, 16: `bwm30_ortholion_guards`, 16: `bwm30_ortholion_warning_2`, 17: `jern_shouting_1`, 18: `capvjern_15`, 20: `ortholion_subdued_0`, 21: `ortholion_conversation2_6a2`, 22: `arghest_alert_8`, 23: `elm2_passage2_3`, 24: `elm3_corpse_3b`, 24: `elm3_corpse_3a`, 25: `elm2_chest_open`, 26: `elm4_sign_north`, 27: `elm4_sign_south`, 28: `elm4_hole`, 29: `elm5_ore_success`, 30: `elm5_hole`, 31: `ortholion_guard8_plunder`, 32: `ortholion_guard8_2`, 33: `elm2f2_chest_4`, 34: `orhtolion_guard9_2`, 35: `ortholion_guard9_11`, 36: `elmf4_up_1`, 37: `kamelio_2c`, 37: `kamelio_3b`, 37: `kamelio_5a`, 38: `elm5f_kamelio_d`, 38: `elm5f_kamelio_e1`, 39: `kamelio_undead`, 40: `ortholion_celebration_2`, 41: `ortholion_11`, 42: `ortholion_19a`, 42: `ortholion_20a`, 42: `ortholion_19c`, 43: `capvjern_32a` |
    | Dialogue nodes clearing stages | 5: `ortholion_conversation_14`, 16: `ortholion_gw_2b`, 20: `ortholion_subdued_5`, 27: `elm4_sign_north`, 26: `elm4_sign_south`, 34: `ortholion_guard9_10a`, 34: `ortholion_guard9_11`, 36: `elm4f_down_1`, 38: `elm5f_kamelio_d2` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
