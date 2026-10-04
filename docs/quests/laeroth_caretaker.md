# Take care of the caretaker

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `laeroth_caretaker` |
| **In journal** | Yes |
| **Stages** | 21 (completes at 180) |
| **Started by** | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) |
| **NPCs involved** | [Audela](../monsters/audela.md), [Cuned](../monsters/cuned.md), [Jerelin](../monsters/jerelin.md), [Jerelin](../monsters/jerelin_b.md), [Moriath](../monsters/moriath.md), [Verigil](../monsters/verigil.md) |
| **Locations** | [laerothmanor1](../maps/laerothmanor1.md), [laerothtomb1](../maps/laerothtomb1.md) |
| **Total XP** | 18,000 |
| **Related quests** | 2 |

</div>

## Overview

> I met a caretaker at Laeroth manor. He said he cannot leave because he is bound by an oath, but not one he ever gave.

## Prerequisites to start

Start with [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)). Required:

- reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10)
- NOT reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-4) | stage 4 reached, for stage 40 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-6) | stage 6 reached, for stage 70 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-8) | stage 8 reached, for stage 90 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-10) | stage 10 reached, for stage 110 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-12) | stage 12 reached, for stage 160 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-13) | stage 13 reached, for stage 120 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-14) | stage 14 reached, for stage 170 here |
| Mutually exclusive | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-5) | stage 5 must NOT be reached, for stage 60 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-3) | stage 3 there needs stage 35 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-5) | stage 5 there needs stage 50 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-9) | stage 9 there needs stage 90 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-14) | stage 14 there needs stage 160 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-120) | stage 120 there needs stages 10, 170 here |
| Unlocks | [The last lord of Laeroth](last_lord.md#stage-10) | stage 10 there needs stage 180 here |
| Unlocks | [The last lord of Laeroth](last_lord.md#stage-15) | stage 15 there needs stage 180 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met a caretaker at Laeroth manor. He said he cannot leave because he is bound by an oath, but not one he ever gave. | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | – | – |
| <span id="stage-15"></span>15 | The caretaker said that he feels honor bound by a pledge that his great-great grandfather made many years ago. | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | stage 10 | – |
| <span id="stage-17"></span>17 | Moriath told me only the past lords can release him from the oath, but they are dead. He suggested I look in the library for information about how to talk to them.<br><span class="qnote">⚡ A scripted event can now trigger on [Laerothmanor0](../maps/laerothmanor0.md).</span> | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | stage 10 | – |
| <span id="stage-20"></span>20 | I have learned the chant needed to send spirits back to their rest on the other side.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor0](../maps/laerothmanor0.md).</span> | stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) | stage 17 | – |
| <span id="stage-30"></span>30 | I have learned how to raise the spirits of the dead with the help of an oegyth crystal. But I also need a personal item. I should talk to Moriath again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor0](../maps/laerothmanor0.md).</span> | stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) | stage 17 | – |
| <span id="stage-35"></span>35 | Moriath suggested I search the master bedroom for a personal item from the last lord, Verigil. | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | stage 10, stage 30 | – |
| <span id="stage-40"></span>40 | Verigil told me he could not release the Caretaker from his oath, because he is from the wrong branch of the family. I must talk to his uncle, Eyvipa. He has gone back to his rest.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Verigil](../monsters/verigil.md) ([laerothtomb1](../maps/laerothtomb1.md))<br>stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | removes monsters from laerothtomb1<br>gives 1× [Slightly diminished oegyth crystal](../items/oegyth1.md) |
| <span id="stage-50"></span>50 | Moriath suggested I look for an item with "E" engraved on it. This would have belonged to Eyvipa. | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | stage 10, stage 40 | – |
| <span id="stage-60"></span>60 | I have found an expensive looking candlestick with "E" engraved on it. This must have belonged to Eyvipa.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor2](../maps/laerothmanor2.md).</span> | stepping on a trigger on [laerothmanor2](../maps/laerothmanor2.md) | stage 50 | gives 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md)<br>sets stage 5 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-5) |
| <span id="stage-70"></span>70 | Eyvipa was angry that I woke him from his rest. He refused to help me because his father passed him over, and made his younger brother, Cuned, lord. I had to send him back to his rest with the chant "estray inyay eacepay".<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md), carry 1× [Slightly diminished oegyth crystal](../items/oegyth1.md) | removes monsters from laerothtomb1<br>applies condition life_drain<br>gives 1× [Diminished oegyth crystal](../items/oegyth2.md) |
| <span id="stage-80"></span>80 | I found a diary that must have belonged to Cuned.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | stage 70 | gives 1× [Cuned's diary](../items/diary_cuned.md) |
| <span id="stage-90"></span>90 | Cuned told me that Verigil is correct, and he cannot release the caretaker from his oath because he is from the wrong branch of the family. I must talk to his father, Jerelin.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Cuned](../monsters/cuned.md) ([laerothtomb1](../maps/laerothtomb1.md))<br>stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | removes monsters from laerothtomb1<br>gives 1× [Very diminished oegyth crystal](../items/oegyth3.md) |
| <span id="stage-100"></span>100 | After much searching I found a seal for Jerelin in an old chest. I must go back to the tomb again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement1](../maps/laerothbasement1.md).</span> | stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) | stage 90 | gives 1× [Jerelin's seal](../items/seal_jerelin.md)<br>sets stage 9 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-9) |
| <span id="stage-110"></span>110 | Jerelin ignored me, and went back to his resting place. I will have to ask Cuned again what to do.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Jerelin](../monsters/jerelin.md) ([laerothtomb1](../maps/laerothtomb1.md))<br>stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | removes monsters from laerothtomb1<br>gives 1× [Heavily diminished oegyth crystal](../items/oegyth4.md) |
| <span id="stage-120"></span>120 | Cuned told me to speak to his mother, Audela. Jerelin didn't listen to many people, but he listened to her.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | removes monsters from laerothtomb1<br>gives 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md) |
| <span id="stage-130"></span>130 | I have found what appears to be a jewelry box, with "A" inscribed on it. It is locked though, and too heavy to move to the tomb.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | stage 120 | – |
| <span id="stage-140"></span>140 | I have found a key in the bedroom.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | stage 130 | gives 1× [Fancy looking key](../items/laeroth_box_key.md) |
| <span id="stage-150"></span>150 | The key fitted the jewelry box! Inside I found a necklace "With love to Audela" written on the back.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span><br><span class="qnote">🗺️ Part of [Laerothmanor1](../maps/laerothmanor1.md) visibly changes.</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | hand over 1× [Fancy looking key](../items/laeroth_box_key.md), stage 140 | changes map laerothmanor1<br>gives 1× [Audela's necklace](../items/audela_necklace.md) |
| <span id="stage-160"></span>160 | Audela told me to talk to Jerelin again, but tell him Audela wants this done.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Audela](../monsters/audela.md) ([laerothtomb1](../maps/laerothtomb1.md))<br>stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | removes monsters from laerothtomb1<br>gives 1× [Nearly depleted oegyth crystal](../items/oegyth6.md) |
| <span id="stage-170"></span>170 | I spoke to Jerelin again, and told him of Audela's wishes. He told me he will release the caretaker, but with a condition. The caretakers last act must be to move his grave away from that of his nagging wife.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Jerelin](../monsters/jerelin_b.md) ([laerothtomb1](../maps/laerothtomb1.md))<br>stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | – | gives 1× [Depleted oegyth crystal](../items/oegyth7.md)<br>removes monsters from laerothtomb1 |
| <span id="stage-180"></span>180 | I told the caretaker what he has to do to be released from the oath. He thanked me, and agreed to do it. **(completes quest)**<br><span class="qnote">🗺️ Part of [Laerothtomb1](../maps/laerothtomb1.md) visibly changes.</span> | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | stage 10, stage 170 | 18,000 XP<br>removes monsters from laerothmanor1<br>sets stage 120 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-120) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “Can you tell me again why you are still here?” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); NOT reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30) → **stage 10**. NPC: “I am bound by an oath to take care of the manor. It is not an oath I ever gave though. I cannot care for everything of…”

???+ note "Stage 15: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “How can you be bound by an oath you never gave?” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); NOT reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30) → **stage 15**. NPC: “It is a matter of honor. The Lord of the manor saved my great-great grandfather from certain death many years ago. In…”

???+ note "Stage 17: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “How can I talk to the dead?” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); NOT reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30) → **stage 17**. NPC: “I have no idea. I am a caretaker, not a priest. The manor has an extensive library. Maybe you should look there.”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-17) → **stage 20**. NPC: “"To start, it must be stressed that raising the spirits of the dead is dangerous. They do not like to be disturbed.…”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-17) → **stage 30**. NPC: “It looks like I have the information I need, although it sounds dangerous.”

???+ note "Stage 35: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “I have found how to raise a spirit and talk to it. However, I need a personal item from the deceased.” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30); NOT reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40) → **stage 35**. NPC: “Well, the previous lord was Verigil. His son, Adakin, did not take any of his fathers possesions when he left. You…”

???+ note "Stage 40: 2 routes"

    1. Talk to [Verigil](../monsters/verigil.md) ([laerothtomb1](../maps/laerothtomb1.md)) → choose “Your son has left Laeroth, and his whereabouts are unknown. However, the caretaker remains, bound by an oath…” → **stage 40**; also removes monsters from laerothtomb1, gives 1× [Slightly diminished oegyth crystal](../items/oegyth1.md). NPC: “I cannot. It is not my branch of the family that bound him. You must talk to my uncle, Eyvipa. Now let me rest. [You…”
    2. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Your son has left Laeroth, and his whereabouts are unknown. However, the caretaker remains, bound by an oath…” — **conditions:** reached stage 4 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-4); NOT reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40) → **stage 40**; also removes monsters from laerothtomb1, gives 1× [Slightly diminished oegyth crystal](../items/oegyth1.md). NPC: “I cannot. It is not my branch of the family that bound him. You must talk to my uncle, Eyvipa. Now let me rest. [You…”

???+ note "Stage 50: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “I spoke to the spirit of Verigil, but he told me he cannot help. I must speak to his uncle, Eyvipa. So I…” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40); NOT reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70) → **stage 50**. NPC: “There are items from all the generations scattered around. They were fond of putting their intials on them. A mixture…”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [laerothmanor2](../maps/laerothmanor2.md) → choose “Take a look in the chest.” — **conditions:** reached stage 50 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-50); NOT reached stage 5 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-5) → **stage 60**; also gives 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md), sets stage 5 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-5). NPC: “You rummage around in the contents. Then a high quality candlestick catches your eye. It has "E" engraved on it! This…”

???+ note "Stage 70: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Estray inyay eacepay!” — **conditions:** carry 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md); carry 1× [Slightly diminished oegyth crystal](../items/oegyth1.md); NOT reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70); reached stage 6 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-6) → **stage 70**; also removes monsters from laerothtomb1, applies condition life_drain, gives 1× [Diminished oegyth crystal](../items/oegyth2.md). NPC: “The ghost of Eyvipa vanishes. You feel great relief that the chant worked. You take back the oegyth crystal, although…”

???+ note "Stage 80: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → choose “You rummage around in the clutter in the cupboards.” — **conditions:** reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70); NOT reached stage 80 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-80) → **stage 80**; also gives 1× [Cuned's diary](../items/diary_cuned.md). NPC: “You find a book, that says "My Diary" on the cover, with an ornate "C" embossed in the cover. This must surely have…”

???+ note "Stage 90: 2 routes"

    1. Talk to [Cuned](../monsters/cuned.md) ([laerothtomb1](../maps/laerothtomb1.md)) → choose “Your family has left Laeroth, and it is now abandoned. But the caretaker is still here. He is bound by an…” → **stage 90**; also removes monsters from laerothtomb1, gives 1× [Very diminished oegyth crystal](../items/oegyth3.md). NPC: “Eyvipa was not made Lord because he was lazy and irresponsible. If he chose to he could release the caretaker, but he…”
    2. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Your family has left Laeroth, and it is now abandoned. But the caretaker is still here. He is bound by an…” — **conditions:** reached stage 8 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-8); NOT reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90) → **stage 90**; also removes monsters from laerothtomb1, gives 1× [Very diminished oegyth crystal](../items/oegyth3.md). NPC: “Eyvipa was not made Lord because he was lazy and irresponsible. If he chose to he could release the caretaker, but he…”

???+ note "Stage 100: 1 route"

    1. stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) → choose “You rummage around in the clutter in the chest.” — **conditions:** reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90); NOT reached stage 100 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-100) → **stage 100**; also gives 1× [Jerelin's seal](../items/seal_jerelin.md), sets stage 9 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-9). NPC: “You find a ring that apparently served as a seal for Jerelin, as it had a large "J" on it. You take the seal.”

???+ note "Stage 110: 2 routes"

    1. Talk to [Jerelin](../monsters/jerelin.md) ([laerothtomb1](../maps/laerothtomb1.md)) → the conversation leads here automatically → **stage 110**; also removes monsters from laerothtomb1, gives 1× [Heavily diminished oegyth crystal](../items/oegyth4.md). NPC: “Hmpff. Go away! [You take the rather dull looking oegyth crystal.]”
    2. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-10); NOT reached stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110) → **stage 110**; also removes monsters from laerothtomb1, gives 1× [Heavily diminished oegyth crystal](../items/oegyth4.md). NPC: “Hmpff. Go away! [You take the rather dull looking oegyth crystal.]”

???+ note "Stage 120: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Sorry. Jerelin refused to talk to me or help me.” — **conditions:** reached stage 13 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-13); NOT reached stage 120 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-120) → **stage 120**; also removes monsters from laerothtomb1, gives 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md). NPC: “He always was stubborn. You should talk to my mother, Audela. He didn't listen to most people, but he listened to her.…”

???+ note "Stage 130: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 120 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-120); NOT reached stage 140 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-140) → **stage 130**. NPC: “This looks interesting. Could be a jewelry box. It has "A" inscribed on it. It is locked though, and too heavy to move…”

???+ note "Stage 140: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 130 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-130); NOT reached stage 140 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-140) → **stage 140**; also gives 1× [Fancy looking key](../items/laeroth_box_key.md). NPC: “You rummage around in the dresser. You have found a fancy looking key!”

???+ note "Stage 150: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 140 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-140); NOT reached stage 150 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-150); hand over 1× [Fancy looking key](../items/laeroth_box_key.md) → **stage 150**; also changes map laerothmanor1, gives 1× [Audela's necklace](../items/audela_necklace.md). NPC: “The key fits the box! You turn it, and the lid springs open. It appears to be mainly full of trinkets and keepsakes.…”

???+ note "Stage 160: 2 routes"

    1. Talk to [Audela](../monsters/audela.md) ([laerothtomb1](../maps/laerothtomb1.md)) → choose “Your family has left Laeroth, and it is now abandoned. But the caretaker is still here. He is bound by an…” → **stage 160**; also removes monsters from laerothtomb1, gives 1× [Nearly depleted oegyth crystal](../items/oegyth6.md). NPC: “So typical of my husband! He always found excuses to do something other than what I asked him to do. Either that, or…”
    2. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Your family has left Laeroth, and it is now abandoned. But the caretaker is still here. He is bound by an…” — **conditions:** reached stage 12 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-12); NOT reached stage 160 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-160) → **stage 160**; also removes monsters from laerothtomb1, gives 1× [Nearly depleted oegyth crystal](../items/oegyth6.md). NPC: “So typical of my husband! He always found excuses to do something other than what I asked him to do. Either that, or…”

???+ note "Stage 170: 2 routes"

    1. Talk to [Jerelin](../monsters/jerelin_b.md) ([laerothtomb1](../maps/laerothtomb1.md)) → choose “I spoke to Audela. She said to tell you that she insists you do this. She even made some kind of threat…” → **stage 170**; also gives 1× [Depleted oegyth crystal](../items/oegyth7.md), removes monsters from laerothtomb1. NPC: “It seems I can't escape my nagging wife even in death! OK, I release the caretaker from the oath. But there is a…”
    2. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “I spoke to Audela. She said to tell you that she insists you do this. She even made some kind of threat…” — **conditions:** reached stage 14 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-14); NOT reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170) → **stage 170**; also gives 1× [Depleted oegyth crystal](../items/oegyth7.md), removes monsters from laerothtomb1. NPC: “It seems I can't escape my nagging wife even in death! OK, I release the caretaker from the oath. But there is a…”

???+ note "Stage 180: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “Finally, success. I had to raise the spirits of many family members, but Jerelin said he would release you…” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170) → **stage 180**; also removes monsters from laerothmanor1, sets stage 120 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-120). NPC: “Thank you. I will do that if it releases me from the oath. I will do it immediately. Farewell, and thanks again.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 21 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed<br>· text: “This looks interesting. Could be a jewelry box. I has "A" inscribed o…” → “This looks interesting. Could be a jewelry box. It has "A" inscribed …” |
| [v0.8.13](../versions/0.8.13.md) | stage 170 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_caretaker.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_caretaker.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_caretaker.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_caretaker.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_caretaker.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `laeroth_caretaker` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 17, 20, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180 |
    | Dialogue nodes setting stages | 10: `moriath_caretaker_2`, 15: `moriath_caretaker_3`, 17: `moriath_caretaker_8`, 20: `book_found_4`, 30: `book_found_10`, 35: `moriath_1_1`, 40: `verigil_2`, 50: `moriath_2_1`, 60: `chest_search_2`, 70: `eyvipa_4b`, 80: `cupboard_search_2`, 90: `cuned_4`, 100: `jerelin_chest_search_2`, 110: `jerelin_1`, 120: `cuned_b_3`, 130: `jewelry_box_1`, 140: `dresser_1`, 150: `jewelry_box_2`, 160: `audela_2`, 170: `jerelin_b_3`, 180: `moriath_9_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
