---
description: "Restless in the grave is a quest in Andor's Trail, started by stepping on a trigger on galmore_47. 25 stages, 10,600 XP in total. I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past. I should ask Vaelric about this."
---

# Restless in the grave

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `mg_restless_grave` |
| **In journal** | Yes |
| **Stages** | 25 (completes at 115, 120, 130) |
| **Started by** | stepping on a trigger on [Galmore 47](../maps/galmore_47.md) |
| **NPCs involved** | [Celdar](../monsters/celdar.md), [Eryndor](../monsters/mg_eryndor.md), [Maddalena](../monsters/sullengard_town_clerk.md), [Vaelric](../monsters/vaelric.md) |
| **Locations** | [Galmore 17 house](../maps/galmore_17_house.md), [Houseatcrossroads 0](../maps/houseatcrossroads0.md), [Mt galmore 0 h 1](../maps/mt_galmore0_h1.md), [Mt galmore 0 h 1 2](../maps/mt_galmore0_h1_2.md) |
| **Total XP** | 10,600 |
| **Related quests** | 3 |

</div>

## Overview

> I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past. I should ask Vaelric about this.

## Prerequisites to start

Start with stepping on a trigger on [Galmore 47](../maps/galmore_47.md). Required:

- NOT reached stage 5 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-5)
- reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-5) | stage 5 reached, for stage 20 here |
| Requires | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-17) | stage 17 reached, for stage 90 here |
| Requires | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-19) | stage 19 reached, for stage 130 here |
| Requires | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-37) | stage 37 reached, for stage 125 here |
| Requires | [The swamp healer](swamp_healer.md#stage-30) | stage 30 reached, for stages 10, 20, 63, 70, 80, 95, 97, 115, 120 here |
| Mutually exclusive | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-5) | stage 5 must NOT be reached, for stages 10, 15 here |
| Blocked by | [The swamp healer](swamp_healer.md#stage-30) | stage 30 must NOT be reached, for stage 15 here |
| Unlocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-16) | stage 16 there needs stage 20 here |
| Unlocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-17) | stage 17 there needs stage 70 here |
| Unlocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-19) | stage 19 there needs stage 123 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I noticed that one of the Galmore grave plots looked to have been… ▸</span><span class="l">▴ less</span></summary>I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past. I should ask Vaelric about this.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span> | stepping on a trigger on [Galmore 47](../maps/galmore_47.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">I noticed that one of the Galmore grave plots looked to have been… ▸</span><span class="l">▴ less</span></summary>I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span> | stepping on a trigger on [Galmore 47](../maps/galmore_47.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">After I mentioned to Vaelric that the graveyard near the Galmore… ▸</span><span class="l">▴ less</span></summary>After I mentioned to Vaelric that the graveyard near the Galmore encampment has a dug-up grave plot, he asked me to investigate it. I agreed to look for clues.</details> | [Vaelric](../monsters/vaelric.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Just outside of the graveyard, I found a bell attached to a broken… ▸</span><span class="l">▴ less</span></summary>Just outside of the graveyard, I found a bell attached to a broken rope. It was partially buried and covered by grass, but I retrieved it.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span><br><span class="qnote">🗺️ Part of [Galmore 47](../maps/galmore_47.md) visibly changes.</span> | stepping on a trigger on [Galmore 47](../maps/galmore_47.md) | 1× [Broken bell](../items/mg_broken_bell.md) |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I discovered a music box in the graveyard. It was partially buried… ▸</span><span class="l">▴ less</span></summary>I discovered a music box in the graveyard. It was partially buried and obscured by overgrown grass.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span><br><span class="qnote">🗺️ Part of [Galmore 47](../maps/galmore_47.md) visibly changes.</span> | stepping on a trigger on [Galmore 47](../maps/galmore_47.md) | 1× [Mysterious music box](../items/mg_music_box.md) |
| <span id="stage-45"></span>[45](#route-45) | <details class="jt"><summary><span class="s">I discovered the skeletal remains of a human beneath a covering of… ▸</span><span class="l">▴ less</span></summary>I discovered the skeletal remains of a human beneath a covering of grass and weeds. I wonder if it's related to why that grave plot is dug up?</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 48](../maps/galmore_48.md).</span> | stepping on a trigger on [Galmore 48](../maps/galmore_48.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I brought the bell and music box to the Galmore encampment and… ▸</span><span class="l">▴ less</span></summary>I brought the bell and music box to the Galmore encampment and encountered a ghost named Eryndor that told me the items were his. I gave them to him in exchange for being "friends".</details> | [Eryndor](../monsters/mg_eryndor.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">Eryndor told me his story and said he would leave Vaelric alone if I… ▸</span><span class="l">▴ less</span></summary>Eryndor told me his story and said he would leave Vaelric alone if I returned his ring. I should return to Vaelric.</details> | [Eryndor](../monsters/mg_eryndor.md) | – |
| <span id="stage-63"></span>[63](#route-63) | <details class="jt"><summary><span class="s">Vaelric has told me his side of the story. He claimed that Eryndor… ▸</span><span class="l">▴ less</span></summary>Vaelric has told me his side of the story. He claimed that Eryndor came to him desperate, in a severe condition and Vaeltic said he did everything he could to save Eryndor's life. Thinking that Eryndor was dead, Vaelric buried him.</details> | [Vaelric](../monsters/vaelric.md) | – |
| <span id="stage-65"></span>[65](#route-65) | <details class="jt"><summary><span class="s">After hearing Eryndor's story, I decided that he has been wronged. I… ▸</span><span class="l">▴ less</span></summary>After hearing Eryndor's story, I decided that he has been wronged. I also agreed to get his ring back from Vaelric.</details> | [Eryndor](../monsters/mg_eryndor.md) | – |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I informed Vaelric of the ghost's terms, and he agreed. He also gave… ▸</span><span class="l">▴ less</span></summary>I informed Vaelric of the ghost's terms, and he agreed. He also gave me Eryndor's ring and now I should return it to Eryndor.</details> | [Vaelric](../monsters/vaelric.md) | 1× [Cursed ring of focus](../items/cursed_ring_focus.md) |
| <span id="stage-77"></span>[77](#route-77) | I've stolen the ring from Vaelric's attic. | walking into a blocked passage on [Galmore 17 house 2f](../maps/galmore_17_house_2f.md) | 1× [Cursed ring of focus](../items/cursed_ring_focus.md) |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">I lied to Vaelric as I informed him that I was not able to find any… ▸</span><span class="l">▴ less</span></summary>I lied to Vaelric as I informed him that I was not able to find any clues surrounding the grave site or anywhere else.</details> | [Vaelric](../monsters/vaelric.md) | – |
| <span id="stage-85"></span>[85](#route-85) | <details class="jt"><summary><span class="s">I brought the ring back to Eryndor. Vaelric received no relief from… ▸</span><span class="l">▴ less</span></summary>I brought the ring back to Eryndor. Vaelric received no relief from the haunting.</details> | [Eryndor](../monsters/mg_eryndor.md) | – |
| <span id="stage-90"></span>[90](#route-90) | I brought the ring back to Eryndor and he agreed to stop haunting Vaelric. | [Eryndor](../monsters/mg_eryndor.md) | removes monsters from mt_galmore_nw_tower_f2, removes monsters from mt_galmore_sw_tower_f2, removes monsters from mt_galmore0_h1, removes monsters from mt_galmore0_h1_2 |
| <span id="stage-95"></span>[95](#route-95) | <details class="jt"><summary><span class="s">Vaelric rewarded me by offering to make Insectbane Tonics if I bring… ▸</span><span class="l">▴ less</span></summary>Vaelric rewarded me by offering to make Insectbane Tonics if I bring him the right ingredients.</details> | [Vaelric](../monsters/vaelric.md) | – |
| <span id="stage-97"></span>[97](#route-97) | <details class="jt"><summary><span class="s">I need to bring Vaelric the following ingredients in order for him… ▸</span><span class="l">▴ less</span></summary>I need to bring Vaelric the following ingredients in order for him to make his "Insectbane Tonic": five Duskbloom flowers, five Mosquito proboscises, ten bottles of swamp water and one sample of Mudfiend goo.</details> | [Vaelric](../monsters/vaelric.md) | 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md) |
| <span id="stage-100"></span>100 | <details class="jt"><summary><span class="s">I brought the ring back to Eryndor just to tell him that I've… ▸</span><span class="l">▴ less</span></summary>I brought the ring back to Eryndor just to tell him that I've decided to keep it.</details> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-110"></span>[110](#route-110) | When I refused to return the ring, Eryndor attacked me. | [Eryndor](../monsters/mg_eryndor.md) | – |
| <span id="stage-111"></span>[111](#route-111) | <details class="jt"><summary><span class="s">I defeated Eryndor and prevented the hauntings of Vaelric...for now,… ▸</span><span class="l">▴ less</span></summary>I defeated Eryndor and prevented the hauntings of Vaelric...for now, but I feel that they will resume someday.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore 0 h 1 2](../maps/mt_galmore0_h1_2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore 0 h 1](../maps/mt_galmore0_h1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore north-west tower f 2](../maps/mt_galmore_nw_tower_f2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore south-west tower f 2](../maps/mt_galmore_sw_tower_f2.md).</span> | stepping on a trigger on [Mt galmore 0 h 1](../maps/mt_galmore0_h1.md) | – |
| <span id="stage-115"></span>[115](#route-115) | Vaelric is now able to mix up some Insectbane tonic for me. **(ends quest)** | [Vaelric](../monsters/vaelric.md) | 6,000 XP |
| <span id="stage-120"></span>[120](#route-120) | <details class="jt"><summary><span class="s">I've informed Vaelric that I defeated Eryndor but was not able to… ▸</span><span class="l">▴ less</span></summary>I've informed Vaelric that I defeated Eryndor but was not able to promise an end to the hauntings, Vaelric was dissatisfied with me and the outcome even going as far as saying that Andor is a better person than I am.</details> **(ends quest)** | [Vaelric](../monsters/vaelric.md) | 100 XP |
| <span id="stage-123"></span>[123](#route-123) | <details class="jt"><summary><span class="s">Eryndor has asked me to find Celdar, a woman from Sullengard and… ▸</span><span class="l">▴ less</span></summary>Eryndor has asked me to find Celdar, a woman from Sullengard and give her the mysterious music box because he has no need for it and it's the right thing to do. I think I remember hearing that name, "Celdar" somewhere. Eryndor stated that Celdar is intolerant of fools and petty trades and wears a garish purple dress.</details> | [Eryndor](../monsters/mg_eryndor.md) | 1× [Mysterious music box](../items/mg_music_box.md) |
| <span id="stage-125"></span>[125](#route-125) | <details class="jt"><summary><span class="s">In Sullengard, Maddalena informed me that Celdar was headed for… ▸</span><span class="l">▴ less</span></summary>In Sullengard, Maddalena informed me that Celdar was headed for Brimhaven, but may have stopped to rest along the way as it is a long trip to Brimhaven.</details> | [Maddalena](../monsters/sullengard_town_clerk.md) | – |
| <span id="stage-130"></span>[130](#route-130) | <details class="jt"><summary><span class="s">I gave Celdar the 'Mysterious music box' just as Eryndor had… ▸</span><span class="l">▴ less</span></summary>I gave Celdar the 'Mysterious music box' just as Eryndor had instructed and she gave me her longsword.</details> **(ends quest)** | [Celdar](../monsters/celdar.md) | 4,500 XP, 1× [Blood seeker](../items/bloodseeker.md) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on galmore_47 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 47](../maps/galmore_47.md)

    - **Needs:** not reached stage 5 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)
    - *“You wonder if Vaelric knows anything about this.”*


<span id="route-15"></span>

??? note "Stage 15 · stepping on a trigger on galmore_47 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 47](../maps/galmore_47.md)

    - **Needs:** not reached stage 5 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); not reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)
    - *“But you really don't know what to think about it.”*


<span id="route-20"></span>

??? note "Stage 20 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “OK, but this better be worth my time.”

    - **Needs:** not yet stage 20, 60; reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 5 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-5)
    - *“Look for anything that might tell us more about who was buried there and why the grave was disturbed.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on galmore_47 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 47](../maps/galmore_47.md), choose “[Investigate.]”

    - **Needs:** stage 20; not yet stage 30
    - **Gives:** 1× [Broken bell](../items/mg_broken_bell.md)
    - *“Kneeling down, you brush aside the thick grass to uncover what appears to be a small, rusted bell, almost entirely concealed by the earth.…”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on galmore_47 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 47](../maps/galmore_47.md), choose “[Investigate.]”

    - **Needs:** stage 20; not yet stage 40
    - **Gives:** 1× [Mysterious music box](../items/mg_music_box.md)
    - *“Kneeling down, you push aside loose dirt and grass with your fingers. Bit by bit, you uncover a weathered music box, its edges worn smooth…”*


<span id="route-45"></span>

??? note "Stage 45 · stepping on a trigger on galmore_48 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 48](../maps/galmore_48.md), choose “[Take a closer look.]”

    - **Needs:** stage 20; not yet stage 45
    - <small>Also: sets stage 16 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-16)</small>
    - *“You kneel down and brush the blades aside, revealing the unmistakable curve of a bone partially buried in the soil. Carefully clearing…”*


<span id="route-50"></span>

??? note "Stage 50 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “I already did.”

    - **Needs:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-50) is 50
    - *“Thank you, friend.”*


<span id="route-60"></span>

??? note "Stage 60 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), automatic

    - **Needs:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-60) is 60
    - *“Return my ring, and this torment ends for both of us. Vaelric can go on with his life, and I will trouble him no more. That is my offer.”*


<span id="route-63"></span>

??? note "Stage 63 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “He says you treated him once, but you buried him alive. That's why he haunts you. He wants his ring back, or…”

    - **Needs:** stage 60; not yet stage 65, 70; reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)
    - *“I had no choice but to lay him to rest. There was no kin to claim him, no priest to see to his rites. So I carried him to the graveyard…”*


<span id="route-65"></span>

??? note "Stage 65 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “You have been wronged, and I will not let that stand. I will get your ring back, one way or another.”

    - **Needs:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-60) is 60
    - *“Then you see the truth. Vaelric took from me when I had nothing, and now he clings to what is not his. I will be waiting, but not always…”*


<span id="route-70"></span>

??? note "Stage 70 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “Please tell me more about Eryndor.”

    - **Needs:** stage 60; not yet stage 65, 70; reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-63) is 63
    - **Gives:** 1× [Cursed ring of focus](../items/cursed_ring_focus.md)
    - *“If his spirit will rest with this ring, take it. If that will end this curse, then let it be done.”*


<span id="route-77"></span>

??? note "Stage 77 · walking into a blocked passage on galmore_17_house_2f · 1 way"

    **Way 1:** Walking into a blocked passage on [Galmore 17 house 2f](../maps/galmore_17_house_2f.md)

    - **Needs:** stage 65; not yet stage 77
    - **Gives:** 1× [Cursed ring of focus](../items/cursed_ring_focus.md)
    - *“Various trinkets and vials clutter the space, but your eyes are drawn to a small, unassuming pouch tucked toward the back. It feels too…”*


<span id="route-80"></span>

??? note "Stage 80 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “I wasn't able to find any clues surrounding the grave site. Is there something you're not telling me?”

    - **Needs:** stage 65; not yet stage 80; reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)
    - *“No, just a suspicion I had. In any event, thanks for looking into it for me. Good luck on your search for Andor.”*


<span id="route-85"></span>

??? note "Stage 85 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “Yes, here it is. [Hand it over]”

    - **Needs:** stage 77; not yet stage 85; hand over 1× [Cursed ring of focus](../items/cursed_ring_focus.md)
    - *“Eryndor's ghost flickers with anticipation as you hold out the ring. His spectral fingers pass through it at first, but he quickly pulls…”*


<span id="route-90"></span>

??? note "Stage 90 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “I already gave it to you.”

    - **Needs:** stage 70; not yet stage 90; reached stage 17 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-17); not carry 1× [Cursed ring of focus](../items/cursed_ring_focus.md)
    - **Gives:** removes monsters from mt_galmore_nw_tower_f2, removes monsters from mt_galmore_sw_tower_f2, removes monsters from mt_galmore0_h1, removes monsters from mt_galmore0_h1_2
    - <small>Also: clears stage 15 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-15)</small>
    - *“I have been bound to this world by resentment, by the belief that my suffering was without meaning. But now, with my ring returned, I…”*


<span id="route-95"></span>

??? note "Stage 95 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “Yes. Hence my being here with my hand out.”

    - **Needs:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-90) is 90
    - *“This tonic does more than ease a fever or numb the pain of a bite. It eliminates the infection entirely. If you have already fallen victim…”*


<span id="route-97"></span>

??? note "Stage 97 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “What do I need to give you in order for you to make those Insectbane tonics? I want some now.”

    - **Needs:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-95) is 95
    - **Gives:** 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md)
    - *“But such a remedy does not come cheaply. If you wish for me to prepare this tonic, you must gather the necessary ingredients yourself.…”*


<span id="route-110"></span>

??? note "Stage 110 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “I have it, but I've decided to keep it for myself.”

    - **Needs:** stage 70; not yet stage 90; carry 1× [Cursed ring of focus](../items/cursed_ring_focus.md)
    - *“You dare? That ring is mine by right! It was stolen from me in death, just as my life was stolen before its time. I will not suffer…”*


<span id="route-111"></span>

??? note "Stage 111 · stepping on a trigger on mt_galmore0_h1 · 1 way"

    **Way 1:** Stepping on a trigger on [Mt galmore 0 h 1](../maps/mt_galmore0_h1.md)

    - **Needs:** not yet stage 111; killed 1× [Eryndor](../monsters/mg_eryndor.md)
    - <small>Also: clears stage 15 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-15)</small>
    - *“The hauntings have ceased. Vaelric will know relief, at least for a time. And yet, a lingering unease settles in your gut. Something about…”*


<span id="route-115"></span>

??? note "Stage 115 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “Can we talk about the Insectbane tonic?”

    - **Needs:** stage 97; not yet stage 115; reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); carry 5× [Duskbloom](../items/duskbloom_flower.md); carry 10× [Pondslime extract](../items/pondslime_extract.md); carry 5× [Mosquito proboscis](../items/mosquito_proboscis.md); carry 1× [Mudfiend goo](../items/mudfiend.md); have 4,800 gold
    - *“I'll take all of the ingredients and your 4,800 gold now and I will mix you up a batch of ten tonics”*


<span id="route-120"></span>

??? note "Stage 120 · Vaelric · 1 way"

    **Way 1:** Talk to [Vaelric](../monsters/vaelric.md), choose “But, but...”

    - **Needs:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-111) is 111
    - *“[Turning away, he mutters:] I will take what peace I can, while it lasts. But do not expect my gratitude.”*


<span id="route-123"></span>

??? note "Stage 123 · Eryndor · 1 way"

    **Way 1:** Talk to [Eryndor](../monsters/mg_eryndor.md), choose “"Celdar", you say? I think I met her.”

    - **Needs:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-85) is 85
    - **Gives:** 1× [Mysterious music box](../items/mg_music_box.md)
    - *“Celdar is from Sullengard. If you don't recall speaking with her, that would be the place to start. But I suspect you have met her before.…”*


<span id="route-125"></span>

??? note "Stage 125 · Maddalena · 1 way"

    **Way 1:** Talk to [Maddalena](../monsters/sullengard_town_clerk.md), choose “What? No. I am looking for Celdar. I've heard she lives here. Is she around by chance?”

    - **Needs:** reached stage 37 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-37); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-123) is 123
    - *“Yes she is a local, but she hasn't been seen around here for a while. Last I heard, she was headed for Brimhaven to do some shopping.…”*


<span id="route-130"></span>

??? note "Stage 130 · Celdar · 1 way"

    **Way 1:** Talk to [Celdar](../monsters/celdar.md), choose “I just gave you that music box...”

    - **Needs:** stage 123; not yet stage 130; reached stage 19 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-19)
    - **Gives:** 1× [Blood seeker](../items/bloodseeker.md)
    - *“Here, take this longsword, I have no need for it. But...”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 24 lines added |
| [v0.8.15](../versions/0.8.15.md) | Dialogue: 2 lines changed |
| [v0.8.16.1](../versions/0.8.16.1.md) | Dialogue: 2 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “I'll take all of the ingredients and your 4800 gold now and I will mi…” → “I'll take all of the ingredients and your {4800} gold now and I will …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `mg_restless_grave` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 45, 50, 60, 63, 65, 70, 77, 80, 85, 90, 95, 97, 100, 110, 111, 115, 120, 123, 125, 130 |
    | Dialogue nodes setting stages | 10: `galmore_47_graveyard_sh_reward_10`, 15: `galmore_47_graveyard_sh_reward_15`, 20: `vaelric_restless_grave_15`, 30: `galmore_rg_bell_20`, 40: `galmore_rg_musicbox_20`, 45: `galmore_rg_skeleton_20`, 50: `mg_eryndor_vaelric_friend`, 60: `mg_eryndor_vaelric_30`, 63: `mg_vaelric_story_40`, 65: `mg_eryndor_vaelric_side_with_eryndor_10`, 70: `mg_vaelric_story_80`, 77: `mg_steal_ghost_ring_10`, 80: `mg_lie_to_vaelric_20`, 85: `mg_eryndor_give_stolen_ring_20`, 90: `mg_eryndor_give_ring_110`, 95: `mg_vaelric_reward_30`, 97: `mg_vaelric_reward_40`, 110: `mg_eryndor_keep_ring_10`, 111: `mg_eryndor_defeated_15`, 115: `mg_vaelric_reward_60`, 120: `mg_vaelric_defeated_eryndor_90`, 123: `mg_eryndor_music_box_40`, 125: `sullengard_town_clerk_celdar_20`, 130: `celdar_musicbox_55` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
