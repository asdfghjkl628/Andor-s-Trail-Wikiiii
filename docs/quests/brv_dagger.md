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
| **Started by** | [Edrin](../monsters/brv_metalsmith.md) ([Brimhaven metalsmith](../maps/brimhaven_metalsmith.md)) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Edrin](../monsters/brv_metalsmith.md), [Forlin](../monsters/brv_tavern1_guest2.md), [Ito](../monsters/brv_guard_deputy.md), [Kizzo](../monsters/loneford_tavern_patron.md), [Ogea](../monsters/brv_villager3.md) +3 |
| **Locations** | [Brimhaven 2](../maps/brimhaven2.md), [Brimhaven 2 laundry](../maps/brimhaven2_laundry.md), [Brimhaven 4](../maps/brimhaven4.md), [Brimhaven church basement](../maps/brimhaven_church_basement.md) |
| **Total XP** | 3,000 |
| **Related quests** | 2 |

</div>

## Overview

> I asked Edrin about the strange-looking dagger I purchased. He told me he recognizes it because he made it many years ago, and it used to have a gem mounted in the pommel. If I can find the gem he can remount it in the dagger, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn.

## Prerequisites to start

Start with [Edrin](../monsters/brv_metalsmith.md) ([Brimhaven metalsmith](../maps/brimhaven_metalsmith.md)). Required:

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
| Requires | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-20) | stage 20 reached, for stage 40 here |
| Requires | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 reached, for stages 120, 130 here |
| Requires | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-60) | stage 60 reached, for stage 220 here |
| Blocked by | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-10) | stage 10 must NOT be reached, for stage 40 here |
| Blocked by | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-20) | stage 20 must NOT be reached, for stage 30 here |
| Blocked by | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-30) | stage 30 must NOT be reached, for stages 30, 90 here |
| Blocked by | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-40) | stage 40 must NOT be reached, for stages 40, 90 here |
| Mutually exclusive | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 must NOT be reached, for stage 115 here |
| Unlocks | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-30) | stage 30 there needs stage 30 here |
| Unlocks | [Brimhaven dagger story flags (hidden flag)](brv_dagger_nondisplay.md#stage-40) | stage 40 there needs stage 40 here |
| Unlocks | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-50) | stage 50 there needs stage 110 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I asked Edrin about the strange-looking dagger I purchased. He told… ▸</span><span class="l">▴ less</span></summary>I asked Edrin about the strange-looking dagger I purchased. He told me he recognizes it because he made it many years ago, and it used to have a gem mounted in the pommel. If I can find the gem he can remount it in the dagger, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn.</details> | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I asked Edrin about the strange-looking gem I purchased, and whether… ▸</span><span class="l">▴ less</span></summary>I asked Edrin about the strange-looking gem I purchased, and whether he has any idea what it might have been mounted in. He told me he recognizes it, and it used to be mounted in the pommel of a dagger that he made many years ago. If I can find the dagger he can remount the gem, and the dagger will have special properties. Apparently it used to belong to someone named Lawellyn.</details> | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-25"></span>[25](#route-25) | <details class="jt"><summary><span class="s">I asked Edrin about the strange-looking dagger and the… ▸</span><span class="l">▴ less</span></summary>I asked Edrin about the strange-looking dagger and the strange-looking gem I purchased. He told me he recognizes them because he made the dagger many years ago. The gem was originally mounted in the pommel, giving the dagger special properties. He offered to repair it for me. Apparently it used to belong to someone named Lawellyn.</details> | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I asked the thief if the dagger he has originally had the gem I… ▸</span><span class="l">▴ less</span></summary>I asked the thief if the dagger he has originally had the gem I purchased in the pommel. His reply was 'maybe', and that the dagger was no longer available except at a 'special' price.</details> | [Pixtumn](../monsters/quiet_thief.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I asked the thief if the gem he has was originally in the pommel of… ▸</span><span class="l">▴ less</span></summary>I asked the thief if the gem he has was originally in the pommel of the dagger I purchased. His reply was 'maybe', and that the gem was no longer available except at a 'special' price.</details> | [Pixtumn](../monsters/quiet_thief.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I showed the strange-looking dagger and the strange-looking gem to… ▸</span><span class="l">▴ less</span></summary>I showed the strange-looking dagger and the strange-looking gem to Edrin. He said they match, and he can repair the dagger by mounting the gem in the pommel again.</details> | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-60"></span>[60](#route-60) | Edrin wants 800 gold to repair the dagger. I told him I will think about it. | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">Edrin wants 800 gold to repair the dagger. I told him that was too… ▸</span><span class="l">▴ less</span></summary>Edrin wants 800 gold to repair the dagger. I told him that was too expensive. I will keep the strange-looking dagger and the strange-looking gem.</details> **(ends quest)** | [Edrin](../monsters/brv_metalsmith.md) | 500 XP |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">Edrin wants 800 gold to repair the dagger. I agreed. Edrin took the… ▸</span><span class="l">▴ less</span></summary>Edrin wants 800 gold to repair the dagger. I agreed. Edrin took the dagger and the gem and told me to come back later.</details> | [Edrin](../monsters/brv_metalsmith.md) | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">I collected the repaired dagger from Edrin. Apparently there was… ▸</span><span class="l">▴ less</span></summary>I collected the repaired dagger from Edrin. Apparently there was something mysterious about Lawellyn's death. I should ask people in town to find out more.</details> | [Edrin](../monsters/brv_metalsmith.md) | 600 XP, 1× [Assassin's blade](../items/dagger_assassin.md) |
| <span id="stage-100"></span>[100](#route-100) | <details class="jt"><summary><span class="s">I collected the repaired dagger from Edrin. Apparently there was… ▸</span><span class="l">▴ less</span></summary>I collected the repaired dagger from Edrin. Apparently there was something mysterious about Lawellyn's death. I should ask people in town to find out more.</details> | [Edrin](../monsters/brv_metalsmith.md) | 300 XP, 1× [Assassin's blade](../items/dagger_assassin.md) |
| <span id="stage-105"></span>[105](#route-105) | <details class="jt"><summary><span class="s">Zorvan told me Lawellyn is dead and buried, but could tell me little… ▸</span><span class="l">▴ less</span></summary>Zorvan told me Lawellyn is dead and buried, but could tell me little more other than that his death was suspicious.</details> | [Zorvan](../monsters/brv_undertaker.md) | – |
| <span id="stage-110"></span>[110](#route-110) | <details class="jt"><summary><span class="s">I've found a gravestone that told me that Lawellyn was related to… ▸</span><span class="l">▴ less</span></summary>I've found a gravestone that told me that Lawellyn was related to Arlish. I should try to find her.</details> | reading a sign on [Brimhaven 2](../maps/brimhaven2.md) | 100 XP |
| <span id="stage-115"></span>[115](#route-115) | Arlish couldn't tell me anything about the dagger because I no longer have it. **(ends quest)** | [Arlish](../monsters/arlish.md) | – |
| <span id="stage-120"></span>[120](#route-120) | I decided to not help Arlish by investigating Lawellyn's disappearance. **(ends quest)** | [Arlish](../monsters/arlish.md) | – |
| <span id="stage-130"></span>[130](#route-130) | I decided to help Arlish by investigating Lawellyn's disappearance. | [Arlish](../monsters/arlish.md) | – |
| <span id="stage-140"></span>[140](#route-140) | <details class="jt"><summary><span class="s">In Brimhaven's eastern tavern, I met a man named Forlin who… ▸</span><span class="l">▴ less</span></summary>In Brimhaven's eastern tavern, I met a man named Forlin who recommended that I speak to Kizzo in the Loneford tavern.</details> | [Forlin](../monsters/brv_tavern1_guest2.md) | – |
| <span id="stage-150"></span>[150](#route-150) | <details class="jt"><summary><span class="s">Kizzo suggested that I look for the scene of the murder in the woods… ▸</span><span class="l">▴ less</span></summary>Kizzo suggested that I look for the scene of the murder in the woods between Loneford and Brimhaven.</details> | [Kizzo](../monsters/loneford_tavern_patron.md) | – |
| <span id="stage-160"></span>[160](#route-160) | I should take the evidence to Kizzo.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 1](../maps/waytobrimhaven1.md).</span> | stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | 200 XP, 1× [Suspect's glove](../items/ogea_glove.md) |
| <span id="stage-170"></span>[170](#route-170) | Kizzo recommended that I ask Venanra in Brimhaven about the glove. | [Kizzo](../monsters/loneford_tavern_patron.md) | – |
| <span id="stage-180"></span>[180](#route-180) | After speaking with Venanra, I learned that the glove belonged to Ogea. | [Venanra](../monsters/brv_laundry_boss.md) | – |
| <span id="stage-190"></span>[190](#route-190) | I accepted Ogea's side of the story. | [Ogea](../monsters/brv_villager3.md) | – |
| <span id="stage-200"></span>[200](#route-200) | I was not able to help Arlish find out more about the death of her father. **(ends quest)** | [Arlish](../monsters/arlish.md) | 300 XP |
| <span id="stage-210"></span>[210](#route-210) | I decided that Ogea should be punished. | [Ogea](../monsters/brv_villager3.md) | – |
| <span id="stage-220"></span>[220](#route-220) | I informed the authorities of the results of my investigation. | [Ito](../monsters/brv_guard_deputy.md) | removes monsters from brimhaven4, spawns monsters on brimhaven_prison |
| <span id="stage-230"></span>[230](#route-230) | <details class="jt"><summary><span class="s">Arlish thanked me for finding her father's murderer, and gave me his… ▸</span><span class="l">▴ less</span></summary>Arlish thanked me for finding her father's murderer, and gave me his dagger as a gift.</details> **(ends quest)** | [Arlish](../monsters/arlish.md) | 1,000 XP, 1× [Assassin's blade](../items/dagger_assassin.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Edrin · 1 way"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “If you have those skills I would like you to look at something I purchased locally. A strange-looking dagger.”

    - **Needs:** not yet stage 20, 25, 50, 70, 80; carry 1× [A strange looking dagger](../items/strange_dagger.md); not carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“I recognize this. I made it, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this recess in the pommel? There…”*


<span id="route-20"></span>

??? note "Stage 20 · Edrin · 1 way"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “If you have those skills I would like you to look at something I purchased locally. A strange-looking gem.”

    - **Needs:** not yet stage 10, 25, 50, 70, 80; carry 1× [A strange-looking gem](../items/strange_gem.md); not carry 1× [A strange looking dagger](../items/strange_dagger.md)
    - *“I recognize this. It was used in something I made, many years ago. It was set into the pommel of a dagger I made for a man called…”*


<span id="route-25"></span>

??? note "Stage 25 · Edrin · 1 way"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “If you have those skills I would like you to look at two items I purchased locally. A strange-looking dagger…”

    - **Needs:** not yet stage 10, 20, 70, 80; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“I recognize these. I made the dagger, many years ago, for a man called Lawellyn. Alas, I hear he is now dead. See this recess in the…”*


<span id="route-30"></span>

??? note "Stage 30 · Pixtumn · 1 way"

    **Way 1:** Talk to [Pixtumn](../monsters/quiet_thief.md), choose “Was the gem I purchased originally mounted in the pommel of the dagger you have?”

    - **Needs:** stage 20; not yet stage 30; reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); not reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); not reached stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30)
    - *“Maybe. Why? Anyway, the dagger is no longer available, except perhaps at a special price.”*


<span id="route-40"></span>

??? note "Stage 40 · Pixtumn · 1 way"

    **Way 1:** Talk to [Pixtumn](../monsters/quiet_thief.md), choose “Was the gem you have originally in the pommel of the dagger I purchased?”

    - **Needs:** stage 10; not yet stage 40; reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); not reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); not reached stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40)
    - *“Maybe. Why? Anyway, the gem is no longer available, except perhaps at a special price.”*


<span id="route-50"></span>

??? note "Stage 50 · Edrin · 2 ways"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “I have a gem. I think it's the right one for the dagger we discussed.”

    - **Needs:** stage 10; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md)
    - *“Yes, that's the one that matches the dagger! Now that I have both pieces, I can repair the dagger for you if you wish.”*

    **Way 2:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “I have a dagger. I think it's the one that matches the gem we discussed.”

    - **Needs:** stage 20; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“Yes, that's the one that matches the gem! Now that I have both pieces, I can repair the dagger for you if you wish.”*


<span id="route-60"></span>

??? note "Stage 60 · Edrin · 3 ways"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's expensive. I'll think about it.”

    - **Needs:** not yet stage 10, 20, 70, 80; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“Feel free to come back when you decide.”*

    **Way 2:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's expensive. I'll think about it.”

    - **Needs:** stage 10; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md)
    - *“Feel free to come back when you decide.”*

    **Way 3:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's expensive. I'll think about it.”

    - **Needs:** stage 20; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“Feel free to come back when you decide.”*


<span id="route-70"></span>

??? note "Stage 70 · Edrin · 3 ways"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's too expensive. I'll keep the dagger and the gem I have.”

    - **Needs:** not yet stage 10, 20, 70, 80; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“That is up to you, although I think you have made a mistake.”*

    **Way 2:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's too expensive. I'll keep the dagger and the gem I have.”

    - **Needs:** stage 10; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md)
    - *“That is up to you, although I think you have made a mistake.”*

    **Way 3:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “That's too expensive. I'll keep the dagger and the gem I have.”

    - **Needs:** stage 20; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)
    - *“That is up to you, although I think you have made a mistake.”*


<span id="route-80"></span>

??? note "Stage 80 · Edrin · 3 ways"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “OK. I agree. Here are the dagger and the gem.”

    - **Needs:** not yet stage 10, 20, 70, 80; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md)
    - <small>Also: starts timer “Dagger_repair”</small>
    - *“This will take me some time. Please come back later to collect the repaired dagger.”*

    **Way 2:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “OK. I agree. Here are the dagger and the gem.”

    - **Needs:** stage 10; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md)
    - <small>Also: starts timer “Dagger_repair”</small>
    - *“This will take me some time. Please come back later to collect the repaired dagger.”*

    **Way 3:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “OK. I agree. Here are the dagger and the gem.”

    - **Needs:** stage 20; not yet stage 25, 70, 80, 90, 100; carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md); pay 800 gold; hand over 1× [A strange looking dagger](../items/strange_dagger.md); hand over 1× [A strange-looking gem](../items/strange_gem.md)
    - <small>Also: starts timer “Dagger_repair”</small>
    - *“This will take me some time. Please come back later to collect the repaired dagger.”*


<span id="route-90"></span>

??? note "Stage 90 · Edrin · 1 way"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “Have you repaired the dagger?”

    - **Needs:** stage 80; not yet stage 70, 90, 100; 30 rounds passed since timer “Dagger_repair”; not reached stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); not reached stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40)
    - **Gives:** 1× [Assassin's blade](../items/dagger_assassin.md)
    - *“Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory. There is some mystery…”*


<span id="route-100"></span>

??? note "Stage 100 · Edrin · 1 way"

    **Way 1:** Talk to [Edrin](../monsters/brv_metalsmith.md), choose “Have you repaired the dagger?”

    - **Needs:** stage 80; not yet stage 70, 90, 100; 30 rounds passed since timer “Dagger_repair”
    - **Gives:** 1× [Assassin's blade](../items/dagger_assassin.md)
    - *“Yes, it is done. Here is the repaired dagger. It's nice to see Lawellyn's dagger brought back to its original glory. There is some mystery…”*


<span id="route-105"></span>

??? note "Stage 105 · Zorvan · 1 way"

    **Way 1:** Talk to [Zorvan](../monsters/brv_undertaker.md), choose “Can you tell me anything about what happened to Lawellyn?”

    - **Needs:** stage 100
    - *“Not really. I buried him some time ago. The circumstances of his death were apparently suspicious, but I don't know anything more. My job…”*


<span id="route-110"></span>

??? note "Stage 110 · reading a sign on brimhaven2 · 1 way"

    **Way 1:** Reading a sign on [Brimhaven 2](../maps/brimhaven2.md)

    - **Needs:** stage 105
    - *“Here lies Lawellyn the weak. Survived by Arlish”*


<span id="route-115"></span>

??? note "Stage 115 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “I was just curious, I was told that a dagger I had was Lawellyn's, but I no longer have it.”

    - **Needs:** stage 110; not yet stage 115, 120, 200, 230; not carry 1× [Assassin's blade](../items/dagger_assassin.md); not wearing [Assassin's blade](../items/dagger_assassin.md); not reached stage 50 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50)
    - *“Well, he did have a dagger, but I can't say if the one you had was his if I can't look at it.”*


<span id="route-120"></span>

??? note "Stage 120 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “I'm sorry, but I just don't have the time.”

    - **Needs:** stage 110; not yet stage 115, 120, 130, 200, 230; reached stage 50 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50)
    - *“I'm sorry to hear this.”*


<span id="route-130"></span>

??? note "Stage 130 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “Yes. Of course I will go investigate a little. You are in need.”

    - **Needs:** stage 110; not yet stage 115, 120, 200, 230; reached stage 50 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50)
    - *“Oh thank you so much.”*


<span id="route-140"></span>

??? note "Stage 140 · Forlin · 1 way"

    **Way 1:** Talk to [Forlin](../monsters/brv_tavern1_guest2.md), choose “Well, I've been asked by Lawellyn's daughter, Arlish, to investigate his death.”

    - **Needs:** stage 130
    - *“I suggest that you go talk to Kizzo.”*


<span id="route-150"></span>

??? note "Stage 150 · Kizzo · 1 way"

    **Way 1:** Talk to [Kizzo](../monsters/loneford_tavern_patron.md), choose “I met a man named Forlin who recommended that I speak with you in regards to a possible murder investigation…”

    - **Needs:** stage 140; not yet stage 150
    - *“That's all I know. Maybe you could find out more if you can find the scene of the murder?”*


<span id="route-160"></span>

??? note "Stage 160 · stepping on a trigger on waytobrimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md), choose “Look closer.”

    - **Needs:** stage 150; not yet stage 160
    - **Gives:** 1× [Suspect's glove](../items/ogea_glove.md)
    - *“[Upon inspection, you notice what appears to be leather peeking out from under some leaves. You pull at it, and find a glove. It has what…”*


<span id="route-170"></span>

??? note "Stage 170 · Kizzo · 1 way"

    **Way 1:** Talk to [Kizzo](../monsters/loneford_tavern_patron.md), choose “Where would someone get just one glove?”

    - **Needs:** not yet stage 190, 210; carry 1× [Suspect's glove](../items/ogea_glove.md)
    - *“Well, I know Venanra in Brimhaven does some great work with cloth and leather items.”*


<span id="route-180"></span>

??? note "Stage 180 · Venanra · 1 way"

    **Way 1:** Talk to [Venanra](../monsters/brv_laundry_boss.md), choose “Are you sure?”

    - **Needs:** stage 170; carry 1× [Suspect's glove](../items/ogea_glove.md)
    - *“Oh, absolutely. I'm sure.”*


<span id="route-190"></span>

??? note "Stage 190 · Ogea · 1 way"

    **Way 1:** Talk to [Ogea](../monsters/brv_villager3.md), choose “Yes”

    - **Needs:** stage 180; not yet stage 190, 210; carry 1× [Suspect's glove](../items/ogea_glove.md)
    - *“I'm glad to hear it. Thank you.”*


<span id="route-200"></span>

??? note "Stage 200 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “I'm sorry, but I was not able to find any new information that would determine what happened to your father.”

    - **Needs:** stage 130, 190; not yet stage 200, 230
    - *“I'm sorry too. Thank you for trying.”*


<span id="route-210"></span>

??? note "Stage 210 · Ogea · 1 way"

    **Way 1:** Talk to [Ogea](../monsters/brv_villager3.md), choose “No. In fact, I want to know more. Like, what did you do with Lawellyn's dagger?”

    - **Needs:** stage 180; not yet stage 190, 210; carry 1× [Suspect's glove](../items/ogea_glove.md)
    - *“Well, after the fight, I noticed that the gem broke off of it. I took both the gem and the dagger and sold them to a thief. So all I'm…”*


<span id="route-220"></span>

??? note "Stage 220 · Ito · 1 way"

    **Way 1:** Talk to [Ito](../monsters/brv_guard_deputy.md), choose “No, thanks. I just want Ogea punished.”

    - **Needs:** not yet stage 220; reached stage 60 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-60)
    - **Gives:** removes monsters from brimhaven4, spawns monsters on brimhaven_prison
    - *“That is as good as done.”*


<span id="route-230"></span>

??? note "Stage 230 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “I have some good news for you.”

    - **Needs:** stage 130, 220; not yet stage 200, 230
    - **Gives:** 1× [Assassin's blade](../items/dagger_assassin.md)
    - *“It would be my honor if you take Lawellyn's dagger. He would want you to have it.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 18 lines added |
| [v0.7.12](../versions/0.7.12.md) | Renamed “A strange-looking dagger” → “A strange looking dagger”<br>Stages added: 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230<br>Stage 10 journal text changed<br>Stage 20 journal text changed<br>Stage 25 journal text changed<br>Stage 60 journal text changed<br>Stage 70 journal text changed<br>Stage 80 journal text changed<br>Stage 90 journal text changed<br>Stage 90 no longer completes the quest<br>(+4 more)<br>Dialogue: 15 lines added, 5 lines changed<br>· text: “I recognize these. I made the dagger, many years ago. See this recess…” → “I recognize these. I made the dagger, many years ago, for a man calle…”<br>· text: “Yes, it is done. Here is the repaired dagger.” → “Yes, it is done. Here is the repaired dagger. It's nice to see Lawell…” |
| [v0.7.13](../versions/0.7.13.md) | Stage 140 journal text changed<br>Dialogue: 1 line changed<br>· text: “That is as good as done” → “That is as good as done.” |

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
