---
description: "A strange looking dagger is a quest in Andor's Trail, started by Edrin (brimhaven_metalsmith). 26 stages, 3,000 XP in total. I asked Edrin about the strange-looking dagger I purchased. He told me he recognizes it because he made it many years ago, and it used to have a gem mounted in the pommel. …"
---

# A strange looking dagger

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_dagger` |
| **In journal** | Yes |
| **Stages** | 26 (completes at 70, 115, 120, 200, 230) |
| **Started by** | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Edrin](../monsters/brv_metalsmith.md), [Forlin](../monsters/brv_tavern1_guest2.md), [Ito](../monsters/brv_guard_deputy.md), [Kizzo](../monsters/loneford_tavern_patron.md), [Ogea](../monsters/brv_villager3.md) +3 |
| **Locations** | [brimhaven2](../maps/brimhaven2.md), [brimhaven2_laundry](../maps/brimhaven2_laundry.md), [brimhaven4](../maps/brimhaven4.md), [brimhaven_church_basement](../maps/brimhaven_church_basement.md) |
| **Total XP** | 3,000 |
| **Related quests** | 2 |

</div>

## Overview

> I asked Edrin about the strange-looking dagger I purchased. He told me he recognizes it because he made it many years ago, and it used to have a gem mounted in the pommel. If I can find the gem he can remount it in the dagger, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn.

## Prerequisites to start

Start with [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)). Required:

- carry 1× [A strange looking dagger](../items/strange_dagger.md)
- NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70)
- NOT reached stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50)
- NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25)
- NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80)
- NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20)
- NOT carry 1× [A strange-looking gem](../items/strange_gem.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-20) | stage 20 reached, for stage 40 here |
| Requires | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 reached, for stages 120, 130 here |
| Requires | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-60) | stage 60 reached, for stage 220 here |
| Blocked by | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-10) | stage 10 must NOT be reached, for stage 40 here |
| Blocked by | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-20) | stage 20 must NOT be reached, for stage 30 here |
| Blocked by | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-30) | stage 30 must NOT be reached, for stages 30, 90 here |
| Blocked by | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-40) | stage 40 must NOT be reached, for stages 40, 90 here |
| Mutually exclusive | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 must NOT be reached, for stage 115 here |
| Unlocks | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-30) | stage 30 there needs stage 30 here |
| Unlocks | [brv_dagger_nondisplay (hidden flag)](brv_dagger_nondisplay.md#stage-40) | stage 40 there needs stage 40 here |
| Unlocks | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 there needs stage 110 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I asked Edrin about the strange-looking dagger I purchased. He told me he recognizes it because he made it many years ago, and it used to have a gem mounted in the pommel. If I can find the gem he can remount it in the dagger, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md) | – |
| <span id="stage-20"></span>20 | I asked Edrin about the strange-looking gem I purchased, and whether he has any idea what it might have been mounted in. He told me he recognizes it, and it used to be mounted in the pommel of a dagger that he made many years ago. If I can find the dagger he can remount the gem, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange-looking gem](../items/strange_gem.md) | – |
| <span id="stage-25"></span>25 | I asked Edrin about the strange-looking dagger and the strange-looking gem I purchased. He told me he recognizes them because he made the dagger many years ago. The gem was originally mounted in the pommel, giving the dagger special properties. He offered to repair it for me. Apparently it used to belong to someone named Lawellyn. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md) | – |
| <span id="stage-30"></span>30 | I asked the thief if the dagger he has originally had the gem I purchased in the pommel. His reply was 'maybe', and that the dagger was no longer available except at a 'special' price. | [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I asked the thief if the gem he has was originally in the pommel of the dagger I purchased. His reply was 'maybe', and that the gem was no longer available except at a 'special' price. | [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) | stage 10 | – |
| <span id="stage-50"></span>50 | I showed the strange-looking dagger and the strange-looking gem to Edrin. He said they match, and he can repair the dagger by mounting the gem in the pommel again. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md), stage 10, stage 20 | – |
| <span id="stage-60"></span>60 | Edrin wants 800 gold to repair the dagger. I told him I will think about it. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md), stage 10, stage 20 | – |
| <span id="stage-70"></span>70 | Edrin wants 800 gold to repair the dagger. I told him that was too expensive. I will keep the strange-looking dagger and the strange-looking gem. **(completes quest)** | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md), stage 10, stage 20 | 500 XP |
| <span id="stage-80"></span>80 | Edrin wants 800 gold to repair the dagger. I agreed. Edrin took the dagger and the gem and told me to come back later. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md), hand over 1× [A strange looking dagger](../items/strange_dagger.md), hand over 1× [A strange-looking gem](../items/strange_gem.md), pay 800 gold, stage 10, stage 20 | starts timer “Dagger_repair” |
| <span id="stage-90"></span>90 | I collected the repaired dagger from Edrin. Apparently there was something mysterious about Lawellyn's death. I should ask people in town to find out more. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | stage 80 | 600 XP<br>gives 1× [Assassin's blade](../items/dagger_assassin.md) |
| <span id="stage-100"></span>100 | I collected the repaired dagger from Edrin. Apparently there was something mysterious about Lawellyn's death. I should ask people in town to find out more. | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | stage 80 | 300 XP<br>gives 1× [Assassin's blade](../items/dagger_assassin.md) |
| <span id="stage-105"></span>105 | Zorvan told me Lawellyn is dead and buried, but could tell me little more other than that his death was suspicious. | [Zorvan](../monsters/brv_undertaker.md) ([brimhaven_church_basement](../maps/brimhaven_church_basement.md)) | stage 100 | – |
| <span id="stage-110"></span>110 | I've found a gravestone that told me that Lawellyn was related to Arlish. I should try to find her. | reading a sign on [brimhaven2](../maps/brimhaven2.md) | stage 105 | 100 XP |
| <span id="stage-115"></span>115 | Arlish couldn't tell me anything about the dagger because I no longer have it. **(completes quest)** | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 110 | – |
| <span id="stage-120"></span>120 | I decided to not help Arlish by investigating Lawellyn's disappearance. **(completes quest)** | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 110 | – |
| <span id="stage-130"></span>130 | I decided to help Arlish by investigating Lawellyn's disappearance. | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 110 | – |
| <span id="stage-140"></span>140 | In Brimhaven's eastern tavern, I met a man named Forlin who recommended that I speak to Kizzo in the Loneford tavern. | [Forlin](../monsters/brv_tavern1_guest2.md) ([brimhaven_tavern1](../maps/brimhaven_tavern1.md)) | stage 130 | – |
| <span id="stage-150"></span>150 | Kizzo suggested that I look for the scene of the murder in the woods between Loneford and Brimhaven. | [Kizzo](../monsters/loneford_tavern_patron.md) ([loneford6](../maps/loneford6.md)) | stage 140 | – |
| <span id="stage-160"></span>160 | I should take the evidence to Kizzo.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven1](../maps/waytobrimhaven1.md).</span> | stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) | stage 150 | 200 XP<br>gives 1× [Suspect's glove](../items/ogea_glove.md) |
| <span id="stage-170"></span>170 | Kizzo recommended that I ask Venanra in Brimhaven about the glove. | [Kizzo](../monsters/loneford_tavern_patron.md) ([loneford6](../maps/loneford6.md)) | carry 1× [Suspect's glove](../items/ogea_glove.md) | – |
| <span id="stage-180"></span>180 | After speaking with Venanra, I learned that the glove belonged to Ogea. | [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) | carry 1× [Suspect's glove](../items/ogea_glove.md), stage 170 | – |
| <span id="stage-190"></span>190 | I accepted Ogea's side of the story. | [Ogea](../monsters/brv_villager3.md) ([brimhaven4](../maps/brimhaven4.md)) | carry 1× [Suspect's glove](../items/ogea_glove.md), stage 180 | – |
| <span id="stage-200"></span>200 | I was not able to help Arlish find out more about the death of her father. **(completes quest)** | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 130, stage 190 | 300 XP |
| <span id="stage-210"></span>210 | I decided that Ogea should be punished. | [Ogea](../monsters/brv_villager3.md) ([brimhaven4](../maps/brimhaven4.md)) | carry 1× [Suspect's glove](../items/ogea_glove.md), stage 180 | – |
| <span id="stage-220"></span>220 | I informed the authorities of the results of my investigation. | [Ito](../monsters/brv_guard_deputy.md) ([brimhaven2](../maps/brimhaven2.md)) | – | removes monsters from brimhaven4<br>spawns monsters on brimhaven_prison |
| <span id="stage-230"></span>230 | Arlish thanked me for finding her father's murderer, and gave me his dagger as a gift. **(completes quest)** | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 130, stage 220 | 1,000 XP<br>gives 1× [Assassin's blade](../items/dagger_assassin.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “If you have those skills I would like you to look at something I purchased locally. A strange-looking dagger.” — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 10**. NPC: “I recognize this. I made it, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this recess…”

???+ note "Stage 20: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “If you have those skills I would like you to look at something I purchased locally. A strange-looking gem.” — **conditions:** carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 50 of [A strange looking dagger](../quests/brv_dagger.md#stage-50); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 20**. NPC: “I recognize this. It was used in something I made, many years ago. It was set into the pommel of a dagger I made for a…”

???+ note "Stage 25: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “If you have those skills I would like you to look at two items I purchased locally. A strange-looking dagger…” — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70) → **stage 25**. NPC: “I recognize these. I made the dagger, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this…”

???+ note "Stage 30: 1 route"

    1. Talk to [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) → choose “Was the gem I purchased originally mounted in the pommel of the dagger you have?” — **conditions:** reached stage 10 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 20 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 30 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); NOT reached stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30); reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20) → **stage 30**. NPC: “Maybe. Why? Anyway, the dagger is no longer available, except perhaps at a special price.”

???+ note "Stage 40: 1 route"

    1. Talk to [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) → choose “Was the gem you have originally in the pommel of the dagger I purchased?” — **conditions:** reached stage 20 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 10 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 40 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40); NOT reached stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40); reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10) → **stage 40**. NPC: “Maybe. Why? Anyway, the gem is no longer available, except perhaps at a special price.”

???+ note "Stage 50: 2 routes"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “I have a gem. I think it's the right one for the dagger we discussed.” — **conditions:** reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 50**. NPC: “Yes, that's the one that matches the dagger! Now that I have both pieces, I can repair the dagger for you if you wish.”
    2. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “I have a dagger. I think it's the one that matches the gem we discussed.” — **conditions:** reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 50**. NPC: “Yes, that's the one that matches the gem! Now that I have both pieces, I can repair the dagger for you if you wish.”

???+ note "Stage 60: 3 routes"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's expensive. I'll think about it.” — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70) → **stage 60**. NPC: “Feel free to come back when you decide.”
    2. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's expensive. I'll think about it.” — **conditions:** reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 60**. NPC: “Feel free to come back when you decide.”
    3. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's expensive. I'll think about it.” — **conditions:** reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 60**. NPC: “Feel free to come back when you decide.”

???+ note "Stage 70: 3 routes"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's too expensive. I'll keep the dagger and the gem I have.” — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70) → **stage 70**. NPC: “That is up to you, although I think you have made a mistake.”
    2. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's too expensive. I'll keep the dagger and the gem I have.” — **conditions:** reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 70**. NPC: “That is up to you, although I think you have made a mistake.”
    3. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “That's too expensive. I'll keep the dagger and the gem I have.” — **conditions:** reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 70**. NPC: “That is up to you, although I think you have made a mistake.”

???+ note "Stage 80: 3 routes"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “OK. I agree. Here are the dagger and the gem.” — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); NOT reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md) → **stage 80**; also starts timer “Dagger_repair”. NPC: “This will take me some time. Please come back later to collect the repaired dagger.”
    2. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “OK. I agree. Here are the dagger and the gem.” — **conditions:** reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md) → **stage 80**; also starts timer “Dagger_repair”. NPC: “This will take me some time. Please come back later to collect the repaired dagger.”
    3. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “OK. I agree. Here are the dagger and the gem.” — **conditions:** reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20); NOT reached stage 25 of [A strange looking dagger](../quests/brv_dagger.md#stage-25); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md) → **stage 80**; also starts timer “Dagger_repair”. NPC: “This will take me some time. Please come back later to collect the repaired dagger.”

???+ note "Stage 90: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “Have you repaired the dagger?” — **conditions:** reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); 30 rounds passed since timer “Dagger_repair”; NOT reached stage 30 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); NOT reached stage 40 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40) → **stage 90**; also gives 1× [Assassin's blade](../items/dagger_assassin.md). NPC: “Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory.…”

???+ note "Stage 100: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “Have you repaired the dagger?” — **conditions:** reached stage 80 of [A strange looking dagger](../quests/brv_dagger.md#stage-80); NOT reached stage 70 of [A strange looking dagger](../quests/brv_dagger.md#stage-70); NOT reached stage 90 of [A strange looking dagger](../quests/brv_dagger.md#stage-90); NOT reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100); 30 rounds passed since timer “Dagger_repair” → **stage 100**; also gives 1× [Assassin's blade](../items/dagger_assassin.md). NPC: “Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory.…”

???+ note "Stage 105: 1 route"

    1. Talk to [Zorvan](../monsters/brv_undertaker.md) ([brimhaven_church_basement](../maps/brimhaven_church_basement.md)) → choose “Can you tell me anything about what happened to Lawellyn?” — **conditions:** reached stage 100 of [A strange looking dagger](../quests/brv_dagger.md#stage-100) → **stage 105**. NPC: “Not really. I buried him some time ago. The circumstances of his death were apparently suspicious, but I don't know…”

???+ note "Stage 110: 1 route"

    1. reading a sign on [brimhaven2](../maps/brimhaven2.md) → the conversation leads here automatically — **conditions:** reached stage 105 of [A strange looking dagger](../quests/brv_dagger.md#stage-105) → **stage 110**. NPC: “Here lies Lawellyn the weak. Survived by Arlish”

???+ note "Stage 115: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “I was just curious, I was told that a dagger I had was Lawellyn's, but I no longer have it.” — **conditions:** reached stage 110 of [A strange looking dagger](../quests/brv_dagger.md#stage-110); NOT reached stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115); NOT reached stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); NOT carry 1× [Assassin's blade](../items/dagger_assassin.md); NOT wearing [Assassin's blade](../items/dagger_assassin.md); NOT reached stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50) → **stage 115**. NPC: “Well, he did have a dagger, but I can't say if the one you had was his if I can't look at it.”

???+ note "Stage 120: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “I'm sorry, but I just don't have the time.” — **conditions:** reached stage 110 of [A strange looking dagger](../quests/brv_dagger.md#stage-110); NOT reached stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115); NOT reached stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); reached stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50); NOT reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130) → **stage 120**. NPC: “I'm sorry to hear this.”

???+ note "Stage 130: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “Yes. Of course I will go investigate a little. You are in need.” — **conditions:** reached stage 110 of [A strange looking dagger](../quests/brv_dagger.md#stage-110); NOT reached stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115); NOT reached stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); reached stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50) → **stage 130**. NPC: “Oh thank you so much.”

???+ note "Stage 140: 1 route"

    1. Talk to [Forlin](../monsters/brv_tavern1_guest2.md) ([brimhaven_tavern1](../maps/brimhaven_tavern1.md)) → choose “Well, I've been asked by Lawellyn's daughter, Arlish, to investigate his death.” — **conditions:** reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130) → **stage 140**. NPC: “I suggest that you go talk to Kizzo.”

???+ note "Stage 150: 1 route"

    1. Talk to [Kizzo](../monsters/loneford_tavern_patron.md) ([loneford6](../maps/loneford6.md)) → choose “I met a man named Forlin who recommended that I speak with you in regards to a possible murder investigation…” — **conditions:** reached stage 140 of [A strange looking dagger](../quests/brv_dagger.md#stage-140); NOT reached stage 150 of [A strange looking dagger](../quests/brv_dagger.md#stage-150) → **stage 150**. NPC: “That's all I know. Maybe you could find out more if you can find the scene of the murder?”

???+ note "Stage 160: 1 route"

    1. stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) → choose “Look closer.” — **conditions:** reached stage 150 of [A strange looking dagger](../quests/brv_dagger.md#stage-150); NOT reached stage 160 of [A strange looking dagger](../quests/brv_dagger.md#stage-160) → **stage 160**; also gives 1× [Suspect's glove](../items/ogea_glove.md). NPC: “[Upon inspection, you notice what appears to be leather peeking out from under some leaves. You pull at it, and find a…”

???+ note "Stage 170: 1 route"

    1. Talk to [Kizzo](../monsters/loneford_tavern_patron.md) ([loneford6](../maps/loneford6.md)) → choose “Where would someone get just one glove?” — **conditions:** carry 1× [Suspect's glove](../items/ogea_glove.md); NOT reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 210 of [A strange looking dagger](../quests/brv_dagger.md#stage-210) → **stage 170**. NPC: “Well, I know Venanra in Brimhaven does some great work with cloth and leather items.”

???+ note "Stage 180: 1 route"

    1. Talk to [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) → choose “Are you sure?” — **conditions:** reached stage 170 of [A strange looking dagger](../quests/brv_dagger.md#stage-170); carry 1× [Suspect's glove](../items/ogea_glove.md) → **stage 180**. NPC: “Oh, absolutely. I'm sure.”

???+ note "Stage 190: 1 route"

    1. Talk to [Ogea](../monsters/brv_villager3.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Yes” — **conditions:** reached stage 180 of [A strange looking dagger](../quests/brv_dagger.md#stage-180); carry 1× [Suspect's glove](../items/ogea_glove.md); NOT reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 210 of [A strange looking dagger](../quests/brv_dagger.md#stage-210) → **stage 190**. NPC: “I'm glad to hear it. Thank you.”

???+ note "Stage 200: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “I'm sorry, but I was not able to find any new information that would determine what happened to your father.” — **conditions:** reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190) → **stage 200**. NPC: “I'm sorry too. Thank you for trying.”

???+ note "Stage 210: 1 route"

    1. Talk to [Ogea](../monsters/brv_villager3.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “No. In fact, I want to know more. Like, what did you do with Lawellyn's dagger?” — **conditions:** reached stage 180 of [A strange looking dagger](../quests/brv_dagger.md#stage-180); carry 1× [Suspect's glove](../items/ogea_glove.md); NOT reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 210 of [A strange looking dagger](../quests/brv_dagger.md#stage-210) → **stage 210**. NPC: “Well, after the fight, I noticed that the gem broke off of it. I took both the gem and the dagger and sold them to a…”

???+ note "Stage 220: 1 route"

    1. Talk to [Ito](../monsters/brv_guard_deputy.md) ([brimhaven2](../maps/brimhaven2.md)) → choose “No, thanks. I just want Ogea punished.” — **conditions:** reached stage 60 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-60); NOT reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220) → **stage 220**; also removes monsters from brimhaven4, spawns monsters on brimhaven_prison. NPC: “That is as good as done.”

???+ note "Stage 230: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “I have some good news for you.” — **conditions:** reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220) → **stage 230**; also gives 1× [Assassin's blade](../items/dagger_assassin.md). NPC: “It would be my honor if you take Lawellyn's dagger. He would want you to have it.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 18 lines added |
| [v0.7.12](../versions/0.7.12.md) | renamed “A strange-looking dagger” → “A strange looking dagger”; stages added: 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230; stage 10 journal text changed; stage 20 journal text changed; stage 25 journal text changed; stage 60 journal text changed (+8 more)<br>Dialogue: 15 lines added, 5 lines changed<br>· text: “I recognize this. I made it, many years ago. See this recess in the p…” → “I recognize this. I made it, many years ago, for a man called Lawelly…”<br>· text: “Yes, it is done. Here is the repaired dagger.” → “Yes, it is done. Here is the repaired dagger. It's nice to see Lawell…” |
| [v0.7.13](../versions/0.7.13.md) | stage 140 journal text changed<br>Dialogue: 1 line changed<br>· text: “That is as good as done” → “That is as good as done.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_dagger` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230 |
    | Dialogue nodes setting stages | 10: `edrin_2_1`, 20: `edrin_3_1`, 25: `edrin_4_1`, 30: `quiet_thief_2_1`, 40: `quiet_thief_3_1`, 50: `edrin_5_0`, 50: `edrin_6_0`, 60: `edrin_4_3c`, 60: `edrin_5_2c`, 60: `edrin_6_2c`, 70: `edrin_4_3a`, 70: `edrin_5_2a`, 70: `edrin_6_2a`, 80: `edrin_4_3b`, 80: `edrin_5_2b`, 80: `edrin_6_2b`, 90: `edrin_7_1a`, 100: `edrin_7_1b`, 105: `zorvan_2_0`, 110: `brv2_grave_9_1`, 115: `arlish_asd_15`, 120: `arlish_asd_90`, 130: `arlish_asd_80`, 140: `brv_tavern1_guest2_asd_40`, 150: `kizzo_asd_30`, 160: `brv_crime_scene_20`, 170: `kizzo_asd_70`, 180: `brv_laundry_boss_40`, 190: `brv_villager3_asd_90`, 200: `arlish_asd_110`, 210: `brv_villager3_asd_100`, 220: `brv_guard_deputy_asd_30`, 230: `arlish_asd_130` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
