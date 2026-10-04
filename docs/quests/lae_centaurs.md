# Not Pony Island

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lae_centaurs` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 310) |
| **Started by** | [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md)), [Callista, the centaur](../monsters/lae_centaur2.md) ([island2](../maps/island2.md)) |
| **NPCs involved** | [Algangror](../monsters/lae_algangror3.md), [Algangror](../monsters/lae_algangror2.md), [Algangror](../monsters/lae_algangror1.md), [Andor](../monsters/lae_andor2.md), [Callista, the centaur](../monsters/lae_centaur2.md), [Jhaeld](../monsters/lae_jhaeld1.md) +5 |
| **Locations** | [final_cave1](../maps/final_cave1.md), [final_cave2](../maps/final_cave2.md), [island1](../maps/island1.md), [island2](../maps/island2.md) |
| **Total XP** | 10,000 |
| **Related quests** | 1 |

</div>

## Overview

> The island west of Remgard was inhabited by centaurs who were very angry about your visit. They told me to seek out their leader, Thalos. He should be in the northeast of the island.

## Prerequisites to start

None: talk to [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [final_cave (hidden flag)](final_cave.md#stage-1) | stage 1 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-2) | stage 2 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-3) | stage 3 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-4) | stage 4 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-5) | stage 5 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-6) | stage 6 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-7) | stage 7 reached, for stage 150 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-10) | stage 10 reached, for stages 150, 190 here |
| Requires | [final_cave (hidden flag)](final_cave.md#stage-11) | stage 11 reached, for stage 140 here |
| Mutually exclusive | [final_cave (hidden flag)](final_cave.md#stage-9) | stage 9 must NOT be reached, for stage 150 here |
| Mutually exclusive | [final_cave (hidden flag)](final_cave.md#stage-11) | stage 11 must NOT be reached, for stage 130 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | The island west of Remgard was inhabited by centaurs who were very angry about your visit. They told me to seek out their leader, Thalos. He should be in the northeast of the island. | [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md))<br>[Callista, the centaur](../monsters/lae_centaur2.md) ([island2](../maps/island2.md))<br>[Silvanus, the centaur](../monsters/lae_centaur3.md) ([island3](../maps/island3.md)) | – | sets stage 211 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-211)<br>sets stage 212 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-212)<br>sets stage 213 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-213) |
| <span id="stage-20"></span>20 | I have met Thalos. | [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) | – | – |
| <span id="stage-30"></span>30 | He ordered me to slay a foul creature that hides in a cave on the hills of Laeroth Island, because the centaurs can't enter it. | [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) | – | removes monsters from island4 |
| <span id="stage-110"></span>110 | In the cave entrance I have met Algangror, who asked for help. | [Algangror](../monsters/lae_algangror1.md) ([island_4_cave1](../maps/island_4_cave1.md)) | – | – |
| <span id="stage-112"></span>112 | In a cave entrance I have met Jhaeld of Remgard, who asked for help. | [Jhaeld](../monsters/lae_jhaeld1.md) ([island_4_cave1](../maps/island_4_cave1.md)) | – | – |
| <span id="stage-120"></span>120 | A common friend would be trapped deeper in the cave and I should free him. | [Algangror](../monsters/lae_algangror1.md) ([island_4_cave1](../maps/island_4_cave1.md))<br>[Jhaeld](../monsters/lae_jhaeld1.md) ([island_4_cave1](../maps/island_4_cave1.md)) | – | – |
| <span id="stage-130"></span>130 | Down in the cave I have found my brother Andor, locked in a room with no doors or other entrances.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave1](../maps/final_cave1.md).</span> | stepping on a trigger on [final_cave1](../maps/final_cave1.md) | – | sets stage 11 of [final_cave (hidden flag)](../quests/final_cave.md#stage-11)<br>removes monsters from island_4_cave1 |
| <span id="stage-140"></span>140 | To open an entrance I had to find the four scrolls of elements and the three color globes. These were hidden all over the island. The scrolls and globes would need to be properly placed around Andor's golden prison.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave1](../maps/final_cave1.md).</span> | stepping on a trigger on [final_cave1](../maps/final_cave1.md) | – | – |
| <span id="stage-150"></span>150 | The wall opened and gave access to the interior of the room.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave1](../maps/final_cave1.md).</span> | walking into a blocked passage on [final_cave1](../maps/final_cave1.md)<br>stepping on a trigger on [final_cave1](../maps/final_cave1.md) | – | sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9)<br>faction “final_cave_hint” set to 999 |
| <span id="stage-160"></span>160 | With an intense sound, the wall built up again. I've been locked up!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave1](../maps/final_cave1.md).</span> | stepping on a trigger on [final_cave1](../maps/final_cave1.md) | – | clears stage 1 of [final_cave (hidden flag)](../quests/final_cave.md#stage-1)<br>faction “final_cave_e” set to 0 |
| <span id="stage-170"></span>170 | The only way out was down a staircase, which, however, seemed to be magically secured.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Final cave1](../maps/final_cave1.md).</span> | [Andor](../monsters/lae_andor2.md) ([final_cave1](../maps/final_cave1.md)) | – | – |
| <span id="stage-180"></span>180 | The only way out was down a staircase, which, however, seemed to be magically secured. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-190"></span>190 | It was no problem going downstairs, but something was wrong there.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave2](../maps/final_cave2.md).</span> | stepping on a trigger on [final_cave2](../maps/final_cave2.md) | – | removes monsters from final_cave1 |
| <span id="stage-200"></span>200 | The whole thing was just a big scam to lure me into this cave to serve Dorhantarh as dinner.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Final cave2](../maps/final_cave2.md).</span> | [Algangror](../monsters/lae_algangror3.md) ([final_cave2](../maps/final_cave2.md)) | – | – |
| <span id="stage-210"></span>210 | The moment I placed the Scroll of Fire on the table, it exploded. At the same time the wall opened again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave2](../maps/final_cave2.md).</span> | walking into a blocked passage on [final_cave2](../maps/final_cave2.md)<br>stepping on a trigger on [final_cave2](../maps/final_cave2.md) | hand over 1× [Scroll of fire](../items/final_cave_f.md) | clears stage 1 of [final_cave (hidden flag)](../quests/final_cave.md#stage-1)<br>clears stage 2 of [final_cave (hidden flag)](../quests/final_cave.md#stage-2)<br>clears stage 3 of [final_cave (hidden flag)](../quests/final_cave.md#stage-3)<br>clears stage 4 of [final_cave (hidden flag)](../quests/final_cave.md#stage-4)<br>clears stage 5 of [final_cave (hidden flag)](../quests/final_cave.md#stage-5)<br>clears stage 6 of [final_cave (hidden flag)](../quests/final_cave.md#stage-6)<br>clears stage 7 of [final_cave (hidden flag)](../quests/final_cave.md#stage-7)<br>faction “final_cave_e” set to 0<br>faction “final_cave_g” set to 0<br>faction “final_cave_f” set to 0<br>faction “final_cave_b” set to 0<br>faction “final_cave_a” set to 0<br>faction “final_cave_r” set to 0<br>faction “final_cave_w” set to 0<br>sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9)<br>faction “final_cave_hint” set to 999<br>applies condition bleeding_wound |
| <span id="stage-300"></span>300 | I brought the monster's heart to Thalos and told him that the danger has been averted. He was impressed and relieved at the same time. | [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) | – | – |
| <span id="stage-310"></span>310 | Since then I have been a welcome guest of the centaurs. **(completes quest)** | [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) | – | 10,000 XP |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 3 routes"

    1. Talk to [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md)) → choose “Then just tell me where he is.” → **stage 10**; also sets stage 211 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-211). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”
    2. Talk to [Callista, the centaur](../monsters/lae_centaur2.md) ([island2](../maps/island2.md)) → choose “Fine, I'll go see him.” → **stage 10**; also sets stage 212 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-212). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”
    3. Talk to [Silvanus, the centaur](../monsters/lae_centaur3.md) ([island3](../maps/island3.md)) → choose “Enough now. I want to speak to your boss.” → **stage 10**; also sets stage 213 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-213). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”

???+ note "Stage 20: 1 route"

    1. Talk to [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) → the conversation leads here automatically → **stage 20**. NPC: “I am Thalos. Human, you are not welcome here.”

???+ note "Stage 30: 1 route"

    1. Talk to [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Not Pony Island](../quests/lae_centaurs.md#stage-30) → **stage 30**; also removes monsters from island4. NPC: “Go and slay this beast. Then I will reconsider your intentions.”

???+ note "Stage 110: 1 route"

    1. Talk to [Algangror](../monsters/lae_algangror1.md) ([island_4_cave1](../maps/island_4_cave1.md)) → the conversation leads here automatically → **stage 110**. NPC: “$playername - good that you are here! I need your help urgently.”

???+ note "Stage 112: 1 route"

    1. Talk to [Jhaeld](../monsters/lae_jhaeld1.md) ([island_4_cave1](../maps/island_4_cave1.md)) → the conversation leads here automatically → **stage 112**. NPC: “$playername - good that you are here! I need your help urgently.”

???+ note "Stage 120: 2 routes"

    1. Talk to [Algangror](../monsters/lae_algangror1.md) ([island_4_cave1](../maps/island_4_cave1.md)) → choose “So how can I help you?” → **stage 120**. NPC: “You know him very well by the way. We have to help him!”
    2. Talk to [Jhaeld](../monsters/lae_jhaeld1.md) ([island_4_cave1](../maps/island_4_cave1.md)) → choose “Why? Don't coming around on your own anymore?” → **stage 120**. NPC: “You know him very well by the way. We have to help him!”

???+ note "Stage 130: 1 route"

    1. stepping on a trigger on [final_cave1](../maps/final_cave1.md) → choose “What?!” — **conditions:** NOT reached stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150); NOT reached stage 11 of [final_cave (hidden flag)](../quests/final_cave.md#stage-11); random chance (25%) → **stage 130**; also sets stage 11 of [final_cave (hidden flag)](../quests/final_cave.md#stage-11), removes monsters from island_4_cave1, removes monsters from island_4_cave1. NPC: “I entered this room to find a powerful weapon against the enemy, when suddenly the walls closed around me.”

???+ note "Stage 140: 1 route"

    1. stepping on a trigger on [final_cave1](../maps/final_cave1.md) → choose “Can you be a little more specific?” — **conditions:** NOT reached stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150); reached stage 11 of [final_cave (hidden flag)](../quests/final_cave.md#stage-11) → **stage 140**. NPC: “There are four scrolls and three globes. Get them here and place them around this room.”

???+ note "Stage 150: 8 routes"

    1. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my scroll of fire.” — **conditions:** reached stage 1 of [final_cave (hidden flag)](../quests/final_cave.md#stage-1); faction “final_cave_f” = 1; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    2. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my red globe.” — **conditions:** reached stage 2 of [final_cave (hidden flag)](../quests/final_cave.md#stage-2); faction “final_cave_r” = 2; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    3. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my scroll of fire.” — **conditions:** reached stage 3 of [final_cave (hidden flag)](../quests/final_cave.md#stage-3); faction “final_cave_f” = 3; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    4. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my red globe.” — **conditions:** reached stage 4 of [final_cave (hidden flag)](../quests/final_cave.md#stage-4); faction “final_cave_r” = 4; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    5. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my scroll of fire.” — **conditions:** reached stage 5 of [final_cave (hidden flag)](../quests/final_cave.md#stage-5); faction “final_cave_f” = 5; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    6. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my red globe.” — **conditions:** reached stage 6 of [final_cave (hidden flag)](../quests/final_cave.md#stage-6); faction “final_cave_r” = 6; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    7. walking into a blocked passage on [final_cave1](../maps/final_cave1.md) → choose “I take back my scroll of fire.” — **conditions:** reached stage 7 of [final_cave (hidden flag)](../quests/final_cave.md#stage-7); faction “final_cave_f” = 7; NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”
    8. stepping on a trigger on [final_cave1](../maps/final_cave1.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [final_cave (hidden flag)](../quests/final_cave.md#stage-10); NOT reached stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9); faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7 → **stage 150**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “A loud rumbling fills the air!”

???+ note "Stage 160: 1 route"

    1. stepping on a trigger on [final_cave1](../maps/final_cave1.md) → the conversation leads here automatically → **stage 160**; also clears stage 1 of [final_cave (hidden flag)](../quests/final_cave.md#stage-1), faction “final_cave_e” set to 0

???+ note "Stage 170: 1 route"

    1. Talk to [Andor](../monsters/lae_andor2.md) ([final_cave1](../maps/final_cave1.md)) → choose “What is down there?” → **stage 170**. NPC: “We can't use those stairs. Some invisible force holds us back. But maybe you can do it?”

???+ note "Stage 190: 1 route"

    1. stepping on a trigger on [final_cave2](../maps/final_cave2.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [final_cave (hidden flag)](../quests/final_cave.md#stage-10) → **stage 190**; also removes monsters from final_cave1, removes monsters from final_cave1, removes monsters from final_cave1. NPC: “You call back upstairs that there was no problem going down.”

???+ note "Stage 200: 1 route"

    1. Talk to [Algangror](../monsters/lae_algangror3.md) ([final_cave2](../maps/final_cave2.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Not Pony Island](../quests/lae_centaurs.md#stage-200) → **stage 200**. NPC: “Now go ahead, you'll be a tasty dinner for our master Dorhantarh tonight.”

???+ note "Stage 210: 2 routes"

    1. walking into a blocked passage on [final_cave2](../maps/final_cave2.md) → choose “The scroll of fire” — **conditions:** hand over 1× [Scroll of fire](../items/final_cave_f.md) → **stage 210**; also clears stage 1 of [final_cave (hidden flag)](../quests/final_cave.md#stage-1), clears stage 2 of [final_cave (hidden flag)](../quests/final_cave.md#stage-2), clears stage 3 of [final_cave (hidden flag)](../quests/final_cave.md#stage-3), clears stage 4 of [final_cave (hidden flag)](../quests/final_cave.md#stage-4), clears stage 5 of [final_cave (hidden flag)](../quests/final_cave.md#stage-5), clears stage 6 of [final_cave (hidden flag)](../quests/final_cave.md#stage-6), clears stage 7 of [final_cave (hidden flag)](../quests/final_cave.md#stage-7), faction “final_cave_e” set to 0, faction “final_cave_g” set to 0, faction “final_cave_f” set to 0, faction “final_cave_b” set to 0, faction “final_cave_a” set to 0, faction “final_cave_r” set to 0, faction “final_cave_w” set to 0, sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999, applies condition bleeding_wound. NPC: “A loud rumbling fills the air! - At the same time the scroll of fire explodes.”
    2. stepping on a trigger on [final_cave2](../maps/final_cave2.md) → the conversation leads here automatically — **conditions:** killed 123× [Dorhantarh](../monsters/lae_island_boss.md); NOT reached stage 210 of [Not Pony Island](../quests/lae_centaurs.md#stage-210) → **stage 210**; also sets stage 9 of [final_cave (hidden flag)](../quests/final_cave.md#stage-9), faction “final_cave_hint” set to 999. NPC: “You hear a loud rumbling from above. Seems to be the walls are opened up again.”

???+ note "Stage 300: 1 route"

    1. Talk to [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) → the conversation leads here automatically — **conditions:** reached stage 300 of [Not Pony Island](../quests/lae_centaurs.md#stage-300) → **stage 300**. NPC: “That foul creature is no more. A great burden is lifted from my heart.”

???+ note "Stage 310: 1 route"

    1. Talk to [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) → the conversation leads here automatically — **conditions:** reached stage 310 of [Not Pony Island](../quests/lae_centaurs.md#stage-310) → **stage 310**. NPC: “You have proven yourself to be more than just another ignorant human.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 19 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_centaurs.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
