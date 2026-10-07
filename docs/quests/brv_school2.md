---
description: "Lessons learned is a quest in Andor's Trail, started by stepping on a trigger on brimhaven_school. 22 stages, 9,500 XP in total. I entered a classroom in Brimhaven's school. The teacher told me to sit down."
---

# Lessons learned

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_school2` |
| **In journal** | Yes |
| **Stages** | 22 (completes at 200, 210, 220, 230, 240) |
| **Started by** | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md), stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) |
| **NPCs involved** | [Golin](../monsters/golin.md), [Pupil](../monsters/brv_pupil1.md#v-brv_pupil5), [Pupil](../monsters/brv_pupil1.md#v-brv_pupil3), [Pupil](../monsters/brv_pupil1.md), [Pupil](../monsters/brv_pupil1.md#v-brv_pupil2), [Pupil](../monsters/brv_pupil1.md#v-brv_pupil4) +5 |
| **Locations** | [brimhaven_school](../maps/brimhaven_school.md) |
| **Total XP** | 9,500 |
| **Related quests** | 1 |

</div>

## Overview

> I entered a classroom in Brimhaven's school. The teacher told me to sit down.

## Prerequisites to start

Start with stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md). Required:

- NOT reached stage 10 of [Lessons learned](../quests/brv_school2.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-21) | stage 21 reached, for stage 40 here |
| Requires | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-22) | stage 22 reached, for stage 220 here |
| Requires | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-30) | stage 30 reached, for stage 150 here |
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-20) | stage 20 there needs stage 30 here |
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-21) | stage 21 there needs stage 30 here |
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-22) | stage 22 there needs stage 100 here |
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-40) | stage 40 there needs stages 104, 120, 124, 152 here |
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-50) | stage 50 there needs stages 60, 100, 102, 120, 150 here |
| Blocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-10) | reaching stage 60 here closes stage 10 there |
| Blocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-30) | reaching stages 100, 102, 104, 120, 122, 124 here closes stage 30 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I entered a classroom in Brimhaven's school. The teacher told me to sit down.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | – | – |
| <span id="stage-12"></span>12 | I noticed an evil-looking statue in a corner. Who on earth puts such an ugly, hideous thing in a school? | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-20"></span>20 | I found a free place next to a student named Golin.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-30"></span>30 | The teacher was droning endlessly about Brimhaven history.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-40"></span>40 | Then a practice lesson started.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | Everyone should take a set of practice weapons from the chest and sit down again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | I should look for a dueling partner.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | carry 1× [Paper shield](../items/brv_school_shield.md), carry 1× [Wooden sword](../items/brv_school_sword.md), stage 50 | changes map brimhaven_school |
| <span id="stage-100"></span>100 | I started a fight with Golin. | [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 60 | – |
| <span id="stage-102"></span>102 | I started a fight with Golin and killed him.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | stage 100 | clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100) |
| <span id="stage-104"></span>104 | I started a fight with Golin, but I broke off the duel. Very good.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 100 | 500 XP<br>clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100)<br>faction “brv_fct_school_duel” set to 10<br>removes monsters from brimhaven_school<br>spawns monsters on brimhaven_school |
| <span id="stage-110"></span>110 | I tried to fight a pupil, but they all ran away screaming. | [Pupil](../monsters/brv_pupil1.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 60 | sets stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50)<br>removes monsters from brimhaven_school |
| <span id="stage-120"></span>120 | I started a fight with the teacher. | [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 60, wearing [Paper shield](../items/brv_school_shield.md), wearing [Wooden sword](../items/brv_school_sword.md) | – |
| <span id="stage-122"></span>122 | I started a fight with the teacher and killed her.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | stage 120 | 1,000 XP<br>clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120)<br>faction “brv_fct_school_duel” set to 10<br>sets stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50)<br>removes monsters from brimhaven_school |
| <span id="stage-124"></span>124 | I started a fight with the teacher, but I broke off the duel. Very good.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 120 | 500 XP<br>clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120)<br>removes monsters from brimhaven_school<br>spawns monsters on brimhaven_school |
| <span id="stage-130"></span>130 | I feel the evil stare of the statue. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-150"></span>150 | The evil grinning statue suddenly grew to an incredible size and attacked me! | [Statue](../monsters/brv_school_statue.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | removes monsters from brimhaven_school<br>spawns monsters on brimhaven_school |
| <span id="stage-152"></span>152 | I killed the evil statue.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | stage 150 | clears stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150) |
| <span id="stage-200"></span>200 | The teacher thanked me for saving her. School is over for me. I can go to the general store and get a cake for good performance. **(completes quest)** | [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 152 | 5,000 XP |
| <span id="stage-210"></span>210 | I cheated during the duel. The teacher noticed it and banned me from the school. **(completes quest)** | [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 104 | 500 XP |
| <span id="stage-220"></span>220 | The teacher was very satisfied with my performance in the duel. School is over for me. I can go to the general store and get a cake for good performance. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md))<br>stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | stage 104, stage 120, stage 124 | 1,000 XP<br>sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40) |
| <span id="stage-230"></span>230 | The teacher sent me away, because I killed Golin in the duel. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 100, stage 102 | 500 XP |
| <span id="stage-240"></span>240 | Golin was horrified by my murder of the teacher and attacked me to avenge her. **(completes quest)** | [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | stage 122 | 500 XP<br>faction “brv_fct_school_duel” -10 |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [Lessons learned](../quests/brv_school2.md#stage-10) → **stage 10**. NPC: “Who do we have here? A new kid? You are late for class. Sit down now, and be punctual next time.”
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [Lessons learned](../quests/brv_school2.md#stage-10) → **stage 10**. NPC: “Who do we have here? A new kid? You are late for class. Sit down now, and be punctual next time.”

???+ note "Stage 20: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically → **stage 20**. NPC: “Hi kid. I am Golin.”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically → **stage 20**. NPC: “Hi kid. I am Golin.”

???+ note "Stage 30: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30) → **stage 30**. NPC: “In the glorious days of year 2177, the enslavement of men ended.”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “[nod silently]” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30) → **stage 30**. NPC: “In the glorious days of year 2177, the enslavement of men ended.”

???+ note "Stage 40: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “[keep silent]” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30); reached stage 21 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-21) → **stage 40**. NPC: “And now we will do something completely different. Let's practice fighting, so that you learn how to defend yourselves.”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “[keep silent]” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30); reached stage 21 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-21) → **stage 40**. NPC: “And now we will do something completely different. Let's practice fighting, so that you learn how to defend yourselves.”

???+ note "Stage 50: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40) → **stage 50**. NPC: “Everybody get your practice gear out of the chest over there. Each of you take one wooden sword and one paper shield,…”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Hush, the teacher is talking again.” — **conditions:** reached stage 50 of [Lessons learned](../quests/brv_school2.md#stage-50); reached stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40) → **stage 50**. NPC: “Everybody get your practice gear out of the chest over there. Each of you take one wooden sword and one paper shield,…”

???+ note "Stage 60: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “Anybody?” — **conditions:** carry 1× [Wooden sword](../items/brv_school_sword.md); carry 1× [Paper shield](../items/brv_school_shield.md) → **stage 60**; also changes map brimhaven_school. NPC: “Just go ahead. But don't forget: You must use the school weapon and shield.”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Anybody?” — **conditions:** reached stage 50 of [Lessons learned](../quests/brv_school2.md#stage-50); carry 1× [Wooden sword](../items/brv_school_sword.md); carry 1× [Paper shield](../items/brv_school_shield.md) → **stage 60**; also changes map brimhaven_school. NPC: “Just go ahead. But don't forget: You must use the school weapon and shield.”

???+ note "Stage 100: 1 route"

    1. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Yes, en Garde!” — **conditions:** reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60) → **stage 100**

???+ note "Stage 102: 1 route"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); killed 1× [Golin](../monsters/golin.md) → **stage 102**; also clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100)

???+ note "Stage 104: 3 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100) → **stage 104**; also clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100), faction “brv_fct_school_duel” set to 10, removes monsters from brimhaven_school, spawns monsters on brimhaven_school
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); killed 1× [Golin](../monsters/golin.md); reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104) → **stage 104**; also clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100), spawns monsters on brimhaven_school. NPC: “Hey, you are not bad! We should stop here indeed. Otherwise you might get hurt.”
    3. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100) → **stage 104**; also clears stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100), spawns monsters on brimhaven_school. NPC: “Hey, you are not bad! We should stop here indeed. Otherwise you might get hurt.”

???+ note "Stage 110: 1 route"

    1. Talk to [Pupil](../monsters/brv_pupil1.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Wait, I'll show you...” — **conditions:** reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60) → **stage 110**; also sets stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50), removes monsters from brimhaven_school. NPC: “[He jumps up and runs screaming out of the room. The other little students follow in panic.]”

???+ note "Stage 120: 1 route"

    1. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Draw your weapon!” — **conditions:** reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60); wearing [Wooden sword](../items/brv_school_sword.md); wearing [Paper shield](../items/brv_school_shield.md) → **stage 120**

???+ note "Stage 122: 1 route"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120); killed 1× [Teacher](../monsters/brv_teacher.md) → **stage 122**; also clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), faction “brv_fct_school_duel” set to 10, sets stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50), removes monsters from brimhaven_school. NPC: “When the little students see how you killed their teacher, a panic breaks out. Screaming, they all run out of the…”

???+ note "Stage 124: 3 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120) → **stage 124**; also clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), removes monsters from brimhaven_school, spawns monsters on brimhaven_school
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120) → **stage 124**; also clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), spawns monsters on brimhaven_school. NPC: “Enough - stop now! I have seen enough. You have an interesting fighting style.”
    3. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120) → **stage 124**; also clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), spawns monsters on brimhaven_school. NPC: “Enough - stop now! I have seen enough. You have an interesting fighting style.”

???+ note "Stage 150: 1 route"

    1. Talk to [Statue](../monsters/brv_school_statue.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Um, yes. Let's try, and see how long you might be able to defend yourself.” — **conditions:** reached stage 30 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-30); NOT reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); NOT reached stage 102 of [Lessons learned](../quests/brv_school2.md#stage-102); NOT reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104); NOT reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120); NOT reached stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122); NOT reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124) → **stage 150**; also removes monsters from brimhaven_school, spawns monsters on brimhaven_school. NPC: “Suddenly the small ugly figure begins to grow! Bigger and bigger, until it seems to almost fill the whole room.”

???+ note "Stage 152: 1 route"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150); killed 1× [Statue](../monsters/brv_school_statue.md#v-brv_school_statue2) → **stage 152**; also clears stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150)

???+ note "Stage 200: 1 route"

    1. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “I just destroyed the evil statue in the corner.” — **conditions:** reached stage 152 of [Lessons learned](../quests/brv_school2.md#stage-152) → **stage 200**. NPC: “The statue is gone? What a relief - I don't know how to thank you! I never had a good feeling about it.”

???+ note "Stage 210: 1 route"

    1. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Eh, yes...” — **conditions:** reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104) → **stage 210**. NPC: “I cannot accept such a behaviour! You have to leave our school - now!”

???+ note "Stage 220: 3 routes"

    1. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Thank you!” — **conditions:** reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104); reached stage 22 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-22) → **stage 220**. NPC: “I can't teach you things that are new for you. Leave now, you don't need to come to school anymore.”
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “Thank you.” — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120) → **stage 220**; also sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40). NPC: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.”
    3. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “It was no big thing...” — **conditions:** reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124) → **stage 220**; also sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40). NPC: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.”

???+ note "Stage 230: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “Eh...” — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); killed 1× [Golin](../monsters/golin.md) → **stage 230**. NPC: “I still can't believe it. Leave the school - now!”
    2. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Eh...” — **conditions:** reached stage 102 of [Lessons learned](../quests/brv_school2.md#stage-102) → **stage 230**. NPC: “I still can't believe it. Leave the school - now!”

???+ note "Stage 240: 1 route"

    1. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically — **conditions:** reached stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122) → **stage 240**; also faction “brv_fct_school_duel” -10. NPC: “I will avenge her. Prepare to die!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 23 lines added |
| [v0.7.12](../versions/0.7.12.md) | Stage 10 journal text changed<br>Stage 12 journal text changed<br>Stage 20 journal text changed<br>Stage 60 journal text changed<br>Stage 100 journal text changed<br>Stage 102 journal text changed<br>Stage 104 journal text changed<br>Stage 110 journal text changed<br>Stage 120 journal text changed<br>Stage 122 journal text changed<br>(+9 more)<br>Dialogue: 1 line changed<br>· text: “And now we get to a completely different thing. Let's have some pract…” → “And now we will do something completely different. Let's practice fig…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_school2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_school2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_school2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_school2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_school2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_school2` |
    | showInLog | 1 |
    | Stage IDs | 10, 12, 20, 30, 40, 50, 60, 100, 102, 104, 110, 120, 122, 124, 130, 150, 152, 200, 210, 220, 230, 240 |
    | Dialogue nodes setting stages | 10: `brv_school_enter_10`, 20: `brv_school_seated_12`, 30: `brv_school_history_10`, 40: `brv_school_history_200`, 50: `brv_school_practice_10`, 60: `brv_school_practice_30`, 100: `golin_60_30`, 102: `brv_school_check_duel_12a`, 104: `brv_school_check_duel_12b`, 104: `golin_100`, 110: `brv_school_pupil_60_20`, 120: `brv_teacher_60_26`, 122: `brv_school_check_duel_20`, 124: `brv_school_check_duel_28`, 124: `brv_teacher_120`, 150: `brv_school_statue_80`, 152: `brv_school_check_duel_30`, 200: `brv_teacher_152_10`, 210: `brv_teacher_104b_20`, 220: `brv_teacher_104a_30`, 220: `brv_teacher_124_20`, 230: `brv_teacher_102_20`, 240: `golin_122_10` |
    | Dialogue nodes clearing stages | 100: `brv_school_check_duel_12a`, 100: `brv_school_check_duel_12b`, 100: `golin_100`, 120: `brv_school_check_duel_20`, 120: `brv_school_check_duel_28`, 120: `brv_teacher_120`, 150: `brv_school_check_duel_30` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
