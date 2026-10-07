---
description: "It makes no fence is a quest in Andor's Trail, started by Tunlon (bwmfill3). 16 stages, 7,005 XP in total. I found Tunlon, a sheep farmer, on the hill next to Crossglen. He asked me to help him get some wood for new fences. Since Crossglen doesn't have a lumberjack, I should go to Fallhaven and a…"
---

# It makes no fence

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `tunlon_fence` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 12, 250) |
| **Started by** | [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) |
| **NPCs involved** | [Hadracor](../monsters/hadracor.md), [Jakrar](../monsters/jakrar.md), [Tinlyn](../monsters/tinlyn.md), [Tunlon](../monsters/tunlon.md), [Villager](../monsters/loneford_villager0.md#v-loneford_villager2), [Wood craftsman](../monsters/brv_woodcraftsman.md) |
| **Locations** | [brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md), [bwmfill3](../maps/bwmfill3.md), [fallhaven_sw](../maps/fallhaven_sw.md), [fields6](../maps/fields6.md) |
| **Total XP** | 7,005 |
| **Related quests** | 5 |

</div>

## Overview

> I found Tunlon, a sheep farmer, on the hill next to Crossglen. He asked me to help him get some wood for new fences. Since Crossglen doesn't have a lumberjack, I should go to Fallhaven and ask there.

## Prerequisites to start

Start with [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)). Required:

- reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250)
- NOT reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Cheap cuts](benbyr.md#stage-21) | stage 21 reached, for stages 40, 110 here |
| Requires | [Devastated land](hadracor.md#stage-10) | stage 10 reached, for stages 30, 32 here |
| Requires | [A path to the Duleian Road](pathway_fallhaven.md#stage-50) | stage 50 reached, for stage 20 here |
| Requires | [Lost sheep](tinlyn.md#stage-31) | stage 31 reached, for stage 100 here |
| Blocked by | [bwmfill_nondisplay (hidden flag)](bwmfill_nondisplay.md#stage-44) | stage 44 must NOT be reached, for stage 12 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I found Tunlon, a sheep farmer, on the hill next to Crossglen. He asked me to help him get some wood for new fences. Since Crossglen doesn't have a lumberjack, I should go to Fallhaven and ask there. | [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | stage 250 | gives [Gold coins](../items/gold.md) |
| <span id="stage-12"></span>12 | Tunlon got furious when he saw that I killed his sheep. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bwmfill3](../maps/bwmfill3.md).</span> | stepping on a trigger on [bwmfill3](../maps/bwmfill3.md)<br>[Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | stage 10 | 5 XP |
| <span id="stage-20"></span>20 | I talked to Fallhaven's woodcutter. He told me that he had done a lot of work lately and therefore can't get any more wood for me. However, I should ask the woodcutters near Crossroads Guardhouse if they can help me. | [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | The woodcutters told me that they have a lot of wood after clearing out the field around them, however all they have is firewood. Apparently this is not suitable for making fences. I should explain this to Tunlon. | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | stage 20 | – |
| <span id="stage-32"></span>32 | Hadracor opened up a passage to the south, so I wouldn't have to take the long way up to Tunlon any more.<br><span class="qnote">🗺️ Part of [Bwmfill1](../maps/bwmfill1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Roadtocarntower0](../maps/roadtocarntower0.md) visibly changes.</span> | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | stage 30 | – |
| <span id="stage-40"></span>40 | I talked to Tunlon again and he told me to talk to his brother Tinlyn if he knew any person who could help me out. | [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | stage 10, stage 20, stage 32 | – |
| <span id="stage-100"></span>100 | Tinlyn was glad to meet me. He said that Loneford had a woodcutter who could maybe help me out. | [Tinlyn](../monsters/tinlyn.md) ([fields6](../maps/fields6.md)) | stage 40 | – |
| <span id="stage-110"></span>110 | Tinlyn wasn't really happy to see me. However, he told me to go to Loneford. | [Tinlyn](../monsters/tinlyn.md) ([fields6](../maps/fields6.md)) | stage 40 | – |
| <span id="stage-150"></span>150 | In Loneford, I met a villager who told me he had some spare fences made. I should bring them to Tunlon. | [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) | pay 100 gold, stage 100 | gives [Sturdy fence](../items/tunlon_fence1.md) |
| <span id="stage-200"></span>200 | Tunlon took a close look at the fences I brought him, but he didn't like them a lot. The fence posts were too short he said. I should go back and ask for taller ones. | [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | carry 10× [Sturdy fence](../items/tunlon_fence1.md), stage 40 | 2,000 XP |
| <span id="stage-210"></span>210 | The woodcutter in Loneford however said he couldn't make any fences, as he just cuts the wood. He recommended giving Brimhaven's woodcutter a visit, as he thinks that he can do some basic woodwork. | [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) | stage 200 | – |
| <span id="stage-220"></span>220 | I gave the woodcutter in Brimhaven a visit and he told me to bring some wood, so the craftsman can make fences out of it. Loneford's woodcutter should have plenty, so I should go back and ask him for wood. | [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) | stage 210 | – |
| <span id="stage-230"></span>230 | I got a pile of wood for the fences. | [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) | stage 220 | gives [Pile of wood](../items/tunlon_wood.md) |
| <span id="stage-235"></span>235 | I gave the wood to the woodcraftsman in Brimhaven. | [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) | hand over 1× [Pile of wood](../items/tunlon_wood.md), stage 230 | – |
| <span id="stage-240"></span>240 | Brimhaven's wood craftsman sold me some nice looking fences. | [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) | pay 200 gold, stage 235 | gives [New fence](../items/tunlon_fence2.md) |
| <span id="stage-250"></span>250 | Tunlon was happy to see the fences I brought him. These should be just fine, he said. **(completes quest)** | [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | hand over 10× [New fence](../items/tunlon_fence2.md), stage 200 | 5,000 XP<br>gives [Gold coins](../items/gold.md), [Specially peppered lamb meat](../items/lamb_meat2.md), [Red Pepper](../items/red_pepper.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → choose “Not for me! I know the way perfectly well.” — **conditions:** reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250); NOT reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10) → **stage 10**; also gives [Gold coins](../items/gold.md). NPC: “Thank you so much! Here is a bit of gold so you can pay for it.”

???+ note "Stage 12: 4 routes"

    1. stepping on a trigger on [bwmfill3](../maps/bwmfill3.md) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250); NOT reached stage 12 of [It makes no fence](../quests/tunlon_fence.md#stage-12) → **stage 12**
    2. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 250 of [It makes no fence](../quests/tunlon_fence.md#stage-250); NOT reached stage 12 of [It makes no fence](../quests/tunlon_fence.md#stage-12) → **stage 12**
    3. stepping on a trigger on [bwmfill3](../maps/bwmfill3.md) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); NOT reached stage 44 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44) → **stage 12**. NPC: “My poor sheep! What have you done?!”
    4. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); NOT reached stage 44 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44) → **stage 12**. NPC: “My poor sheep! What have you done?!”

???+ note "Stage 20: 1 route"

    1. Talk to [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Oh, alright. But where should I ask then?” — **conditions:** reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50); reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20) → **stage 20**. NPC: “I have heard that a forest to the north was cleared out recently. Sure enough they got some wood laying around there.”

???+ note "Stage 30: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → choose “No, but I wanted to ask if you have some spare wood to make fences out of.” — **conditions:** reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10); reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20); NOT reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30) → **stage 30**. NPC: “Oh we do have a lot of wood indeed. However, all of this is very brittle and can only be used as firewood.”

???+ note "Stage 32: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → choose “Well, I try to avoid it. The route past Stoutford and Prim is long and arduous.” — **conditions:** reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10); reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30); NOT reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32) → **stage 32**. NPC: “I like to believe that. Look, I told my men to cut down some trees for you. You can now take a shortcut.”

???+ note "Stage 40: 1 route"

    1. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → choose “Well ... yeah I know him.” — **conditions:** reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20); reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32); reached stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21) → **stage 40**. NPC: “Please go and ask him, if he knows anyone who could help.”

???+ note "Stage 100: 1 route"

    1. Talk to [Tinlyn](../monsters/tinlyn.md) ([fields6](../maps/fields6.md)) → choose “Yes. And he made me ask you if you knew where you could get fences from.” — **conditions:** reached stage 31 of [Lost sheep](../quests/tinlyn.md#stage-31); reached stage 40 of [It makes no fence](../quests/tunlon_fence.md#stage-40); NOT reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 110 of [It makes no fence](../quests/tunlon_fence.md#stage-110) → **stage 100**. NPC: “There is a woodcutter in Loneford. He should be able to help you out. Have a great day!”

???+ note "Stage 110: 1 route"

    1. Talk to [Tinlyn](../monsters/tinlyn.md) ([fields6](../maps/fields6.md)) → choose “I am sorry. But your brother sent me to ask if you knew where I could get fences for his sheep.” — **conditions:** reached stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21); reached stage 40 of [It makes no fence](../quests/tunlon_fence.md#stage-40); NOT reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 110 of [It makes no fence](../quests/tunlon_fence.md#stage-110) → **stage 110**. NPC: “[grumbles] Maybe I do. Go over to Loneford and leave me alone.”

???+ note "Stage 150: 1 route"

    1. Talk to [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) → choose “Great, I'll take them.” — **conditions:** reached stage 100 of [It makes no fence](../quests/tunlon_fence.md#stage-100); NOT reached stage 150 of [It makes no fence](../quests/tunlon_fence.md#stage-150); pay 100 gold → **stage 150**; also gives [Sturdy fence](../items/tunlon_fence1.md). NPC: “Here you go.”

???+ note "Stage 200: 1 route"

    1. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → choose “Sure! No problem.” — **conditions:** reached stage 40 of [It makes no fence](../quests/tunlon_fence.md#stage-40); carry 10× [Sturdy fence](../items/tunlon_fence1.md) → **stage 200**. NPC: “Thank you. I knew I could trust you.”

???+ note "Stage 210: 1 route"

    1. Talk to [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) → choose “So ... could you make any?” — **conditions:** reached stage 200 of [It makes no fence](../quests/tunlon_fence.md#stage-200); NOT reached stage 210 of [It makes no fence](../quests/tunlon_fence.md#stage-210) → **stage 210**. NPC: “Kid, look. I am a woodcutter, not a craftsman. Go east to Brimhaven if you want other fences.”

???+ note "Stage 220: 1 route"

    1. Talk to [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) → choose “Hello. The woodcutter in Loneford said that you can make me fences for a shepherd. Is that true?” — **conditions:** reached stage 210 of [It makes no fence](../quests/tunlon_fence.md#stage-210); NOT reached stage 220 of [It makes no fence](../quests/tunlon_fence.md#stage-220) → **stage 220**. NPC: “But I'm afraid I haven't got enough wood right now. Please go back to Loneford's woodcutter. We have a deal that he…”

???+ note "Stage 230: 1 route"

    1. Talk to [Villager](../monsters/loneford_villager0.md#v-loneford_villager2) ([loneford2](../maps/loneford2.md)) → choose “The Craftsman told me that I should get some wood from you.” — **conditions:** reached stage 220 of [It makes no fence](../quests/tunlon_fence.md#stage-220); NOT reached stage 230 of [It makes no fence](../quests/tunlon_fence.md#stage-230) → **stage 230**; also gives [Pile of wood](../items/tunlon_wood.md). NPC: “[pointing to a pile of wood] There.”

???+ note "Stage 235: 1 route"

    1. Talk to [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) → choose “Here is your wood.” — **conditions:** reached stage 230 of [It makes no fence](../quests/tunlon_fence.md#stage-230); hand over 1× [Pile of wood](../items/tunlon_wood.md); NOT reached stage 240 of [It makes no fence](../quests/tunlon_fence.md#stage-240) → **stage 235**. NPC: “Perfect! Thank you for helping out, kid. Just wait a few minutes.”

???+ note "Stage 240: 1 route"

    1. Talk to [Wood craftsman](../monsters/brv_woodcraftsman.md) ([brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)) → choose “200 ... gold pieces - well, OK.” — **conditions:** reached stage 235 of [It makes no fence](../quests/tunlon_fence.md#stage-235); NOT reached stage 240 of [It makes no fence](../quests/tunlon_fence.md#stage-240); random chance (10%); pay 200 gold → **stage 240**; also gives [New fence](../items/tunlon_fence2.md). NPC: “Thank you. Bye!”

???+ note "Stage 250: 1 route"

    1. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → choose “Here, I hope these are better.” — **conditions:** reached stage 200 of [It makes no fence](../quests/tunlon_fence.md#stage-200); hand over 10× [New fence](../items/tunlon_fence2.md) → **stage 250**; also gives [Gold coins](../items/gold.md), [Specially peppered lamb meat](../items/lamb_meat2.md), [Red Pepper](../items/red_pepper.md). NPC: “Yeah, these posts are looking really good! Thank you, kid. Here, take this as a small reward.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added<br>Dialogue: 17 lines added |
| [v0.8.11](../versions/0.8.11.md) | stage 12 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tunlon_fence.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tunlon_fence.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tunlon_fence.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tunlon_fence.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tunlon_fence.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `tunlon_fence` |
    | showInLog | 1 |
    | Stage IDs | 10, 12, 20, 30, 32, 40, 100, 110, 150, 200, 210, 220, 230, 235, 240, 250 |
    | Dialogue nodes setting stages | 10: `tunlon_quest_5`, 12: `bwmfill_killsheep_12`, 12: `bwmfill_killsheep_22`, 20: `fallhaven_lumberjack_18`, 30: `hadracor_fence_1`, 32: `hadracor_fence_3`, 40: `tunlon_prog_5`, 100: `tinlyn_fence_1a`, 110: `tinlyn_fence_2`, 150: `loneford_villager2_fence1`, 200: `tunlon_prog_18`, 210: `loneford_villager2_fence3`, 220: `brv_woodcraftsman_fence1a`, 230: `loneford_villager2_fence4`, 235: `brv_woodcraftsman_fence2`, 240: `brv_woodcraftsman_fence6`, 250: `tunlon_prog_22` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
