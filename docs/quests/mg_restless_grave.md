# Restless in the grave

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `mg_restless_grave` |
| **In journal** | Yes |
| **Stages** | 25 (completes at 115, 120, 130) |
| **Started by** | stepping on a trigger on [galmore_47](../maps/galmore_47.md) |
| **NPCs involved** | [Celdar](../monsters/celdar.md), [Eryndor](../monsters/mg_eryndor.md), [Maddalena](../monsters/sullengard_town_clerk.md), [Vaelric](../monsters/vaelric.md) |
| **Locations** | [galmore_17_house](../maps/galmore_17_house.md), [houseatcrossroads0](../maps/houseatcrossroads0.md), [mt_galmore0_h1](../maps/mt_galmore0_h1.md), [mt_galmore0_h1_2](../maps/mt_galmore0_h1_2.md) |
| **Total XP** | 10,600 |
| **Related quests** | 3 |

</div>

## Overview

> I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past. I should ask Vaelric about this.

## Prerequisites to start

Start with stepping on a trigger on [galmore_47](../maps/galmore_47.md). Required:

- NOT reached stage 5 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-5)
- reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-5) | stage 5 reached, for stage 20 here |
| Requires | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-17) | stage 17 reached, for stage 90 here |
| Requires | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-19) | stage 19 reached, for stage 130 here |
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-37) | stage 37 reached, for stage 125 here |
| Requires | [The swamp healer](swamp_healer.md#stage-30) | stage 30 reached, for stages 10, 20, 63, 70, 80, 95, 97, 115, 120 here |
| Mutually exclusive | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-5) | stage 5 must NOT be reached, for stages 10, 15 here |
| Blocked by | [The swamp healer](swamp_healer.md#stage-30) | stage 30 must NOT be reached, for stage 15 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-16) | stage 16 there needs stage 20 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-17) | stage 17 there needs stage 70 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-19) | stage 19 there needs stage 123 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past. I should ask Vaelric about this.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span> | stepping on a trigger on [galmore_47](../maps/galmore_47.md) | – | – |
| <span id="stage-15"></span>15 | I noticed that one of the Galmore grave plots looked to have been dug-up in the not-so-distant past.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span> | stepping on a trigger on [galmore_47](../maps/galmore_47.md) | – | – |
| <span id="stage-20"></span>20 | After I mentioned to Vaelric that the graveyard near the Galmore encampment has a dug-up grave plot, he asked me to investigate it. I agreed to look for clues. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | – | – |
| <span id="stage-30"></span>30 | Just outside of the graveyard, I found a bell attached to a broken rope. It was partially buried and covered by grass, but I retrieved it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span><br><span class="qnote">🗺️ Part of [Galmore 47](../maps/galmore_47.md) visibly changes.</span> | stepping on a trigger on [galmore_47](../maps/galmore_47.md) | stage 20 | gives 1× [Broken bell](../items/mg_broken_bell.md) |
| <span id="stage-40"></span>40 | I discovered a music box in the graveyard. It was partially buried and obscured by overgrown grass.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 47](../maps/galmore_47.md).</span><br><span class="qnote">🗺️ Part of [Galmore 47](../maps/galmore_47.md) visibly changes.</span> | stepping on a trigger on [galmore_47](../maps/galmore_47.md) | stage 20 | gives 1× [Mysterious music box](../items/mg_music_box.md) |
| <span id="stage-45"></span>45 | I discovered the skeletal remains of a human beneath a covering of grass and weeds. I wonder if it's related to why that grave plot is dug up?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 48](../maps/galmore_48.md).</span> | stepping on a trigger on [galmore_48](../maps/galmore_48.md) | stage 20 | sets stage 16 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-16) |
| <span id="stage-50"></span>50 | I brought the bell and music box to the Galmore encampment and encountered a ghost named Eryndor that told me the items were his. I gave them to him in exchange for being "friends". | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | – | – |
| <span id="stage-60"></span>60 | Eryndor told me his story and said he would leave Vaelric alone if I returned his ring. I should return to Vaelric. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | – | – |
| <span id="stage-63"></span>63 | Vaelric has told me his side of the story. He claimed that Eryndor came to him desperate, in a severe condition and Vaeltic said he did everything he could to save Eryndor's life. Thinking that Eryndor was dead, Vaelric buried him. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 60 | – |
| <span id="stage-65"></span>65 | After hearing Eryndor's story, I decided that he has been wronged. I also agreed to get his ring back from Vaelric. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | stage 60 | – |
| <span id="stage-70"></span>70 | I informed Vaelric of the ghost's terms, and he agreed. He also gave me Eryndor's ring and now I should return it to Eryndor. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 60, stage 63 | gives 1× [Cursed ring of focus](../items/cursed_ring_focus.md) |
| <span id="stage-77"></span>77 | I've stolen the ring from Vaelric's attic. | walking into a blocked passage on [galmore_17_house_2f](../maps/galmore_17_house_2f.md) | stage 65 | gives 1× [Cursed ring of focus](../items/cursed_ring_focus.md) |
| <span id="stage-80"></span>80 | I lied to Vaelric as I informed him that I was not able to find any clues surrounding the grave site or anywhere else. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 65 | – |
| <span id="stage-85"></span>85 | I brought the ring back to Eryndor. Vaelric received no relief from the haunting. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | hand over 1× [Cursed ring of focus](../items/cursed_ring_focus.md), stage 77 | – |
| <span id="stage-90"></span>90 | I brought the ring back to Eryndor and he agreed to stop haunting Vaelric. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | stage 70 | clears stage 15 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-15)<br>removes monsters from mt_galmore_nw_tower_f2<br>removes monsters from mt_galmore_sw_tower_f2<br>removes monsters from mt_galmore0_h1<br>removes monsters from mt_galmore0_h1_2 |
| <span id="stage-95"></span>95 | Vaelric rewarded me by offering to make Insectbane Tonics if I bring him the right ingredients. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 90 | – |
| <span id="stage-97"></span>97 | I need to bring Vaelric the following ingredients in order for him to make his "Insectbane Tonic": five Duskbloom flowers, five Mosquito proboscises, ten bottles of swamp water and one sample of Mudfiend goo. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 95 | gives 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md) |
| <span id="stage-100"></span>100 | I brought the ring back to Eryndor just to tell him that I've decided to keep it. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-110"></span>110 | When I refused to return the ring, Eryndor attacked me. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | carry 1× [Cursed ring of focus](../items/cursed_ring_focus.md), stage 70 | – |
| <span id="stage-111"></span>111 | I defeated Eryndor and prevented the hauntings of Vaelric...for now, but I feel that they will resume someday.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore north-west tower f2](../maps/mt_galmore_nw_tower_f2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore south-west tower f2](../maps/mt_galmore_sw_tower_f2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore0 h1 2](../maps/mt_galmore0_h1_2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mt galmore0 h1](../maps/mt_galmore0_h1.md).</span> | stepping on a trigger on [mt_galmore0_h1](../maps/mt_galmore0_h1.md) | – | clears stage 15 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-15) |
| <span id="stage-115"></span>115 | Vaelric is now able to mix up some Insectbane tonic for me. **(completes quest)** | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | carry 10× [Pondslime extract](../items/pondslime_extract.md), carry 1× [Mudfiend goo](../items/mudfiend.md), carry 5× [Duskbloom](../items/duskbloom_flower.md), carry 5× [Mosquito proboscis](../items/mosquito_proboscis.md), have 4,800 gold, stage 97 | 6,000 XP |
| <span id="stage-120"></span>120 | I've informed Vaelric that I defeated Eryndor but was not able to promise an end to the hauntings, Vaelric was dissatisfied with me and the outcome even going as far as saying that Andor is a better person than I am. **(completes quest)** | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | stage 111 | 100 XP |
| <span id="stage-123"></span>123 | Eryndor has asked me to find Celdar, a woman from Sullengard and give her the mysterious music box because he has no need for it and it's the right thing to do. I think I remember hearing that name, "Celdar" somewhere. Eryndor stated that Celdar is intolerant of fools and petty trades and wears a garish purple dress. | [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) | stage 85 | gives 1× [Mysterious music box](../items/mg_music_box.md) |
| <span id="stage-125"></span>125 | In Sullengard, Maddalena informed me that Celdar was headed for Brimhaven, but may have stopped to rest along the way as it is a long trip to Brimhaven. | [Maddalena](../monsters/sullengard_town_clerk.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) | stage 123 | – |
| <span id="stage-130"></span>130 | I gave Celdar the 'Mysterious music box' just as Eryndor had instructed and she gave me her longsword. **(completes quest)** | [Celdar](../monsters/celdar.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) | stage 123 | 4,500 XP<br>gives 1× [Blood seeker](../items/bloodseeker.md) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [galmore_47](../maps/galmore_47.md) → the conversation leads here automatically — **conditions:** NOT reached stage 5 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30) → **stage 10**. NPC: “You wonder if Vaelric knows anything about this.”

???+ note "Stage 15: 1 route"

    1. stepping on a trigger on [galmore_47](../maps/galmore_47.md) → the conversation leads here automatically — **conditions:** NOT reached stage 5 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); NOT reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30) → **stage 15**. NPC: “But you really don't know what to think about it.”

???+ note "Stage 20: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “OK, but this better be worth my time.” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 5 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); NOT reached stage 60 of [Restless in the grave](../quests/mg_restless_grave.md#stage-60); NOT reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20) → **stage 20**. NPC: “Look for anything that might tell us more about who was buried there and why the grave was disturbed.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [galmore_47](../maps/galmore_47.md) → choose “[Investigate.]” — **conditions:** reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20); NOT reached stage 30 of [Restless in the grave](../quests/mg_restless_grave.md#stage-30) → **stage 30**; also gives 1× [Broken bell](../items/mg_broken_bell.md). NPC: “Kneeling down, you brush aside the thick grass to uncover what appears to be a small, rusted bell, almost entirely…”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [galmore_47](../maps/galmore_47.md) → choose “[Investigate.]” — **conditions:** reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20); NOT reached stage 40 of [Restless in the grave](../quests/mg_restless_grave.md#stage-40) → **stage 40**; also gives 1× [Mysterious music box](../items/mg_music_box.md). NPC: “Kneeling down, you push aside loose dirt and grass with your fingers. Bit by bit, you uncover a weathered music box,…”

???+ note "Stage 45: 1 route"

    1. stepping on a trigger on [galmore_48](../maps/galmore_48.md) → choose “[Take a closer look.]” — **conditions:** reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20); NOT reached stage 45 of [Restless in the grave](../quests/mg_restless_grave.md#stage-45) → **stage 45**; also sets stage 16 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-16). NPC: “You kneel down and brush the blades aside, revealing the unmistakable curve of a bone partially buried in the soil.…”

???+ note "Stage 50: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “I already did.” — **conditions:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-50) is 50 → **stage 50**. NPC: “Thank you, friend.”

???+ note "Stage 60: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → the conversation leads here automatically — **conditions:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-60) is 60 → **stage 60**. NPC: “Return my ring, and this torment ends for both of us. Vaelric can go on with his life, and I will trouble him no more.…”

???+ note "Stage 63: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “He says you treated him once, but you buried him alive. That's why he haunts you. He wants his ring back, or…” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 60 of [Restless in the grave](../quests/mg_restless_grave.md#stage-60); NOT reached stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70); NOT reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65) → **stage 63**. NPC: “I had no choice but to lay him to rest. There was no kin to claim him, no priest to see to his rites. So I carried him…”

???+ note "Stage 65: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “You have been wronged, and I will not let that stand. I will get your ring back, one way or another.” — **conditions:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-60) is 60 → **stage 65**. NPC: “Then you see the truth. Vaelric took from me when I had nothing, and now he clings to what is not his. I will be…”

???+ note "Stage 70: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “Please tell me more about Eryndor.” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 60 of [Restless in the grave](../quests/mg_restless_grave.md#stage-60); NOT reached stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70); NOT reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-63) is 63 → **stage 70**; also gives 1× [Cursed ring of focus](../items/cursed_ring_focus.md). NPC: “If his spirit will rest with this ring, take it. If that will end this curse, then let it be done.”

???+ note "Stage 77: 1 route"

    1. walking into a blocked passage on [galmore_17_house_2f](../maps/galmore_17_house_2f.md) → the conversation leads here automatically — **conditions:** NOT reached stage 77 of [Restless in the grave](../quests/mg_restless_grave.md#stage-77); reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65) → **stage 77**; also gives 1× [Cursed ring of focus](../items/cursed_ring_focus.md). NPC: “Various trinkets and vials clutter the space, but your eyes are drawn to a small, unassuming pouch tucked toward the…”

???+ note "Stage 80: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “I wasn't able to find any clues surrounding the grave site. Is there something you're not telling me?” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65); NOT reached stage 80 of [Restless in the grave](../quests/mg_restless_grave.md#stage-80) → **stage 80**. NPC: “No, just a suspicion I had. In any event, thanks for looking into it for me. Good luck on your search for Andor.”

???+ note "Stage 85: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “Yes, here it is. [Hand it over]” — **conditions:** reached stage 77 of [Restless in the grave](../quests/mg_restless_grave.md#stage-77); NOT reached stage 85 of [Restless in the grave](../quests/mg_restless_grave.md#stage-85); hand over 1× [Cursed ring of focus](../items/cursed_ring_focus.md) → **stage 85**. NPC: “Eryndor's ghost flickers with anticipation as you hold out the ring. His spectral fingers pass through it at first,…”

???+ note "Stage 90: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “I already gave it to you.” — **conditions:** reached stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70); NOT reached stage 90 of [Restless in the grave](../quests/mg_restless_grave.md#stage-90); reached stage 17 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-17); NOT carry 1× [Cursed ring of focus](../items/cursed_ring_focus.md) → **stage 90**; also clears stage 15 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-15), removes monsters from mt_galmore_nw_tower_f2, removes monsters from mt_galmore_sw_tower_f2, removes monsters from mt_galmore0_h1, removes monsters from mt_galmore0_h1_2. NPC: “I have been bound to this world by resentment, by the belief that my suffering was without meaning. But now, with my…”

???+ note "Stage 95: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “Yes. Hence my being here with my hand out.” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-90) is 90 → **stage 95**. NPC: “This tonic does more than ease a fever or numb the pain of a bite. It eliminates the infection entirely. If you have…”

???+ note "Stage 97: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “What do I need to give you in order for you to make those Insectbane tonics? I want some now.” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-95) is 95 → **stage 97**; also gives 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md). NPC: “But such a remedy does not come cheaply. If you wish for me to prepare this tonic, you must gather the necessary…”

???+ note "Stage 110: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “I have it, but I've decided to keep it for myself.” — **conditions:** reached stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70); NOT reached stage 90 of [Restless in the grave](../quests/mg_restless_grave.md#stage-90); carry 1× [Cursed ring of focus](../items/cursed_ring_focus.md) → **stage 110**. NPC: “You dare? That ring is mine by right! It was stolen from me in death, just as my life was stolen before its time. I…”

???+ note "Stage 111: 1 route"

    1. stepping on a trigger on [mt_galmore0_h1](../maps/mt_galmore0_h1.md) → the conversation leads here automatically — **conditions:** killed 1× [Eryndor](../monsters/mg_eryndor.md); NOT reached stage 111 of [Restless in the grave](../quests/mg_restless_grave.md#stage-111) → **stage 111**; also clears stage 15 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-15). NPC: “The hauntings have ceased. Vaelric will know relief, at least for a time. And yet, a lingering unease settles in your…”

???+ note "Stage 115: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “Can we talk about the Insectbane tonic?” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); reached stage 97 of [Restless in the grave](../quests/mg_restless_grave.md#stage-97); NOT reached stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115); carry 5× [Duskbloom](../items/duskbloom_flower.md); carry 10× [Pondslime extract](../items/pondslime_extract.md); carry 5× [Mosquito proboscis](../items/mosquito_proboscis.md); carry 1× [Mudfiend goo](../items/mudfiend.md); have 4,800 gold → **stage 115**. NPC: “I'll take all of the ingredients and your 4,800 gold now and I will mix you up a batch of ten tonics”

???+ note "Stage 120: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “But, but...” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-111) is 111 → **stage 120**. NPC: “[Turning away, he mutters:] I will take what peace I can, while it lasts. But do not expect my gratitude.”

???+ note "Stage 123: 1 route"

    1. Talk to [Eryndor](../monsters/mg_eryndor.md) ([mt_galmore0_h1](../maps/mt_galmore0_h1.md)) → choose “"Celdar", you say? I think I met her.” — **conditions:** latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-85) is 85 → **stage 123**; also gives 1× [Mysterious music box](../items/mg_music_box.md). NPC: “Celdar is from Sullengard. If you don't recall speaking with her, that would be the place to start. But I suspect you…”

???+ note "Stage 125: 1 route"

    1. Talk to [Maddalena](../monsters/sullengard_town_clerk.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) → choose “What? No. I am looking for Celdar. I've heard she lives here. Is she around by chance?” — **conditions:** reached stage 37 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-37); latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-123) is 123 → **stage 125**. NPC: “Yes she is a local, but she hasn't been seen around here for a while. Last I heard, she was headed for Brimhaven to do…”

???+ note "Stage 130: 1 route"

    1. Talk to [Celdar](../monsters/celdar.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) → choose “I just gave you that music box...” — **conditions:** reached stage 123 of [Restless in the grave](../quests/mg_restless_grave.md#stage-123); NOT reached stage 130 of [Restless in the grave](../quests/mg_restless_grave.md#stage-130); reached stage 19 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-19) → **stage 130**; also gives 1× [Blood seeker](../items/bloodseeker.md). NPC: “Here, take this longsword, I have no need for it. But...”


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

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mg_restless_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
