# Yellow is it

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ratdom_quest` |
| **In journal** | Yes |
| **Stages** | 44 (completes at 940, 948, 999) |
| **Started by** | stepping on a trigger on [home](../maps/home.md), [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) |
| **NPCs involved** | [Andor's statue](../monsters/ratdom_rat_statue.md), [Audir](../monsters/audir.md), [Bloskelt](../monsters/ratdom_skeleton_boss2.md), [Clevred](../monsters/ratdom_rat.md), [Clevred](../monsters/ratdom_rat_bwm1.md), [Fraedro](../monsters/ratdom_fraedro.md) +6 |
| **Locations** | [blackwater_mountain55](../maps/blackwater_mountain55.md), [crossglen_cave](../maps/crossglen_cave.md), [home](../maps/home.md), [ratdom_bwm1](../maps/ratdom_bwm1.md) |
| **Total XP** | 47,910 |
| **Related quests** | 7 |

</div>

## Overview

> I woke up when I felt that something had bitten my toe. Apparently I had a nightmare - there were rats everywhere! Anyway, I wasn't even slightly recovered.

## Prerequisites to start

**Route 1** (stepping on a trigger on [home](../maps/home.md)):

- NOT reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
- NOT reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940)
- NOT reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942)
- NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
- reached stage 100 of [odair (hidden flag)](../quests/odair.md#stage-100)
- reached stage 30 of [bonemeal (hidden flag)](../quests/bonemeal.md#stage-30)
- reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
- reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115)
- reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190)
- have 9,000 gold

**Route 2** ([Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md))):

- nothing

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Destined for great things](charwood1.md#stage-115) | stage 115 reached, for stage 10 here |
| Requires | [Searching for madness](lodar2.md#stage-60) | stage 60 reached, for stage 10 here |
| Requires | [More rats!](ratdom_mikhail.md#stage-10) | stage 10 reached, for stage 50 here |
| Requires | [More rats!](ratdom_mikhail.md#stage-90) | stage 90 reached, for stages 940, 999 here |
| Requires | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 reached, for stages 90, 100, 999 here |
| Requires | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 reached, for stages 130, 900 here |
| Requires | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-11) | stage 11 reached, for stage 950 here |
| Requires | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-180) | stage 180 reached, for stages 398, 399 here |
| Requires | [Skeleton brothers](ratdom_skeleton.md#stage-61) | stage 61 reached, for stage 37 here |
| Requires | [Skeleton brothers](ratdom_skeleton.md#stage-62) | stage 62 reached, for stage 37 here |
| Requires | [Skeleton brothers](ratdom_skeleton.md#stage-71) | stage 71 reached, for stage 37 here |
| Requires | [Skeleton brothers](ratdom_skeleton.md#stage-72) | stage 72 reached, for stage 37 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-190) | stage 190 reached, for stage 10 here |
| Mutually exclusive | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 must NOT be reached, for stage 10 here |
| Mutually exclusive | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-3) | stage 3 must NOT be reached, for stages 90, 100 here |
| Mutually exclusive | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 must NOT be reached, for stage 942 here |
| Mutually exclusive | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-11) | stage 11 must NOT be reached, for stage 900 here |
| Mutually exclusive | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-100) | stage 100 must NOT be reached, for stage 34 here |
| Unlocks | [Ratdom_maze (hidden flag)](ratdom_maze.md#stage-132) | stage 132 there needs stage 310 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-10) | stage 10 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-20) | stage 20 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-52) | stage 52 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-54) | stage 54 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-70) | stage 70 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-74) | stage 74 there needs stage 950 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-90) | stage 90 there needs stage 950 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 there needs stage 940 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-192) | stage 192 there needs stage 310 here |
| Blocks | [Ratdom_maze (hidden flag)](ratdom_maze.md#stage-132) | reaching stage 390 here closes stage 132 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-10) | reaching stage 999 here closes stage 10 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-20) | reaching stage 999 here closes stage 20 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-52) | reaching stage 999 here closes stage 52 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-54) | reaching stage 999 here closes stage 54 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-70) | reaching stage 999 here closes stage 70 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-74) | reaching stage 999 here closes stage 74 there |
| Blocks | [More rats!](ratdom_mikhail.md#stage-90) | reaching stage 999 here closes stage 90 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I woke up when I felt that something had bitten my toe. Apparently I had a nightmare - there were rats everywhere! Anyway, I wasn't even slightly recovered.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span><br><span class="qnote">🔒 An area on [Ratdom maze 627](../maps/ratdom_maze_627.md) becomes blocked off.</span> | stepping on a trigger on [home](../maps/home.md)<br>[Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | have 9,000 gold | sets stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)<br>sets stage 2 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-2)<br>sets stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)<br>changes map home<br>spawns monsters on home<br>spawns monsters on crossglen_cave<br>spawns monsters on crossglen<br>changes map crossglen<br>starts timer “ratdom_rat_eatme”<br>starts timer “ratdom_rat_drinkme”<br>starts timer “ratdom_compass_tour”<br>starts timer “ratdom_compass_bwm” |
| <span id="stage-30"></span>30 | An ancient meditating man rewarded me with a rat skull for a wise discussion. | [Wise of the wells](../monsters/ratdom_well_wise3.md) ([ratdom_maze_768](../maps/ratdom_maze_768.md)) | – | gives 1× [Rat skull](../items/ratdom_rat_skelett_skull.md) |
| <span id="stage-31"></span>31 | I took a leg bone of a rat from a gold hunter.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span> | stepping on a trigger on [ratdom_maze_535a](../maps/ratdom_maze_535a.md) | – | – |
| <span id="stage-32"></span>32 | I stole a leg bone of a rat from the instrument maker.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 464](../maps/ratdom_maze_464.md).</span> | stepping on a trigger on [ratdom_maze_464](../maps/ratdom_maze_464.md) | carry 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md), hand over 1× [Bone](../items/bone.md), hand over 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md) | gives 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md) |
| <span id="stage-33"></span>33 | In the center of a labyrinth I found a leg bone of a rat.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 568](../maps/ratdom_maze_568.md).</span> | stepping on a trigger on [ratdom_maze_568](../maps/ratdom_maze_568.md) | – | – |
| <span id="stage-34"></span>34 | I took a leg bone of a rat from the dancing but vengeful and unforgiving skeletons.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | walking into a blocked passage on [ratdom_maze_543d](../maps/ratdom_maze_543d.md) | – | removes monsters from ratdom_maze_543d<br>sets stage 100 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-100)<br>gives 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md)<br>spawns monsters on ratdom_maze_543d |
| <span id="stage-35"></span>35 | I found the tail bones of a dead rat on a platform in a lake.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 664](../maps/ratdom_maze_664.md).</span> | stepping on a trigger on [ratdom_maze_664](../maps/ratdom_maze_664.md) | – | gives 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md) |
| <span id="stage-36"></span>36 | In a library I found the back bone of a big rat.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 611](../maps/ratdom_maze_611.md).</span> | stepping on a trigger on [ratdom_maze_611](../maps/ratdom_maze_611.md) | carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md) | – |
| <span id="stage-37"></span>37 | I got some rib bones of a rat from the skeleton leader. | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md))<br>[Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) | – | sets stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90)<br>gives 18× [Gold coins](../items/gold.md)<br>gives 2× [Glass gem](../items/gem1.md)<br>gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) |
| <span id="stage-50"></span>50 | A small, naughty rat called Clevred claimed that he could help me get out of here. In return, he required of me to help to find a yellow, round artifact. | [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | – |
| <span id="stage-52"></span>52 | I should look around in the rat cave. Clevred probably meant the Crossglen's supply cave. | [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 50 | – |
| <span id="stage-60"></span>60 | In the depth of the supply cave I found a new statue, that resembles to my brother Andor. | [Andor's statue](../monsters/ratdom_rat_statue.md) ([crossglen_cave](../maps/crossglen_cave.md)) | – | – |
| <span id="stage-70"></span>70 | The rats had erected the statue in honor of Andor for never killing rats. I should begin your search behind this statue. | [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 50, stage 60 | – |
| <span id="stage-80"></span>80 | I would need a pickaxe to tear down the statue. | [Andor's statue](../monsters/ratdom_rat_statue.md) ([crossglen_cave](../maps/crossglen_cave.md)) | stage 70 | – |
| <span id="stage-82"></span>82 | Audir, the smith of Crossglen, sold me an old, sturdy pickaxe. | [Audir](../monsters/audir.md) | pay 80 gold, stage 80 | gives 1× [Pickhatchet](../items/ratdom_pickaxe.md) |
| <span id="stage-90"></span>90 | I tore down the statue of Andor. Behind it in the wall I found a hole in the shape of a bone.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen cave](../maps/crossglen_cave.md).</span> | stepping on a trigger on [crossglen_cave](../maps/crossglen_cave.md) | – | – |
| <span id="stage-100"></span>100 | I have put a bone into the hole, and the wall crumbled to dust.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen cave](../maps/crossglen_cave.md).</span> | stepping on a trigger on [crossglen_cave](../maps/crossglen_cave.md) | hand over 1× [Bone](../items/bone.md) | 200 XP<br>sets stage 3 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-3) |
| <span id="stage-110"></span>110 | A torch could help to see in the dark. Unfortunately, the torch is so heavy, that I would have to lift it with both hands. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-120"></span>120 | I found a platform with a good view over Crossglen. Andor seemed to have been here many times. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-130"></span>130 | I found Andor's hideout. | [Clevred](../monsters/ratdom_rat_bwm1.md) ([ratdom_bwm1](../maps/ratdom_bwm1.md)) | – | 200 XP |
| <span id="stage-200"></span>200 | I found an exit from the caves to the surface. Cold icy wind was swirling up here on the Black Water mountain top.  Astonishingly I wasn't alone here - Whootibarfag, a very old hermit seemed to have been waiting for me. | [Whootibarfag](../monsters/whootibarfag.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | 500 XP |
| <span id="stage-210"></span>210 | Whootibarfag was delighted with my help in rescuing Rat King Rah's skeleton. As a thank you, he let me in on the secret of the rat escape. This increased my ability to flee. | [Whootibarfag](../monsters/whootibarfag.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 390 | +1 [Evasion](../skills/evasion.md) |
| <span id="stage-310"></span>310 | Wart, the warden to the halls of memory told me, that the access would be closed, until the rat memorial is restored. I should seek the bones of King Rah's skeleton. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | – | – |
| <span id="stage-320"></span>320 | Wart told me that he needed the head, the ribs and the back bone, 4 legs and the tail. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), stage 310 | – |
| <span id="stage-321"></span>321 | Wart said that I just have to find the skull. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md), carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md), carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), stage 310 | – |
| <span id="stage-322"></span>322 | Wart said that I just have to find the back bone. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md), carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md), carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), stage 310 | – |
| <span id="stage-323"></span>323 | Wart said that I have to find the rib bones. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md), carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), stage 310 | – |
| <span id="stage-324"></span>324 | Wart said that I just have to find the tail. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md), carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), stage 310 | – |
| <span id="stage-325"></span>325 | Wart said that I just have to find the fourth leg. | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md), carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md), stage 310 | – |
| <span id="stage-380"></span>380 | I donated King Rah's sword to the memory hall. | walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) | hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) | 5,000 XP<br>sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184) |
| <span id="stage-381"></span>381 | I sold King Rah's sword to the memory hall. | walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) | hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) | sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184)<br>gives 1000× [Gold coins](../items/gold.md) |
| <span id="stage-390"></span>390 | Wart was glad to have his rat memorial restored. He granted access to the memory hall now.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 624](../maps/ratdom_maze_624.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 624](../maps/ratdom_maze_624.md) visibly changes.</span> | [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) | hand over 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), hand over 1× [Rat skull](../items/ratdom_rat_skelett_skull.md), hand over 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md), hand over 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md), hand over 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), stage 310 | 1,000 XP |
| <span id="stage-392"></span>392 | Wart told me that Fraedro was captured. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-395"></span>395 | Wart allowed me to go deeper into the cave and have a word with Fraedro.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 515](../maps/ratdom_maze_515.md).</span> | [Wart](../monsters/ratdom_rat_warden2.md) ([ratdom_maze_515](../maps/ratdom_maze_515.md)) | have 100 gold, pay 100 gold | – |
| <span id="stage-398"></span>398 | I believed in Fraedro's innocence and released him. | [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) | – | gives 1× [Fraedro's key](../items/ratdom_fraedro_key.md)<br>removes monsters from ratdom_maze_626 |
| <span id="stage-399"></span>399 | I attacked Fraedro to avenge the theft of King Rah. | [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) | – | – |
| <span id="stage-400"></span>400 | I tried Fraedro's tiny golden key in a hole of the cavewall near to his prison. Immediatly the wall gave way to another passage.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 626](../maps/ratdom_maze_626.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 626](../maps/ratdom_maze_626.md) visibly changes.</span> | walking into a blocked passage on [ratdom_maze_626](../maps/ratdom_maze_626.md) | hand over 1× [Fraedro's key](../items/ratdom_fraedro_key.md) | – |
| <span id="stage-900"></span>900 | I finally found the yellow artifact: It was a big round and smelly cheese! Golden yellow and so large that it would provide almost unlimited food. Clevred was overjoyed!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span> | stepping on a trigger on [ratdom_maze_627](../maps/ratdom_maze_627.md) | – | sets stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)<br>clears stage 12 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-12)<br>spawns monsters on ratdom_maze_627 |
| <span id="stage-940"></span>940 | I told Clevred that I you couldn't help him further with the search. He then left me to search on his own. **(completes quest)** | [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942)<br>clears stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)<br>clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)<br>sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13)<br>sets stage 21 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-21)<br>sets stage 22 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-22)<br>sets stage 23 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-23)<br>removes monsters from home<br>removes monsters from ratdom_bwm1<br>removes monsters from ratdom_maze_448<br>removes monsters from ratdom_maze_627<br>removes monsters from crossglen<br>changes map crossglen |
| <span id="stage-942"></span>942 | Although I had told Clevred that I couldn't help him further with the search and he then left me, I met him in the caves again. I have decided to start the search again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze1](../maps/ratdom_maze1.md).</span> | stepping on a trigger on [ratdom_maze1](../maps/ratdom_maze1.md) | stage 940 | clears stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940)<br>sets stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)<br>clears stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13)<br>clears stage 21 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-21)<br>clears stage 22 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-22)<br>clears stage 23 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-23)<br>spawns monsters on ratdom_maze_627 |
| <span id="stage-948"></span>948 | The big yellow cheese now weighs heavily in my bag. Small consolation for the loss of a friend, though. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 448](../maps/ratdom_maze_448.md).</span> | stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) | carry 1× [Rat's artifact](../items/ratdom_artefact.md), stage 942 | 20,000 XP |
| <span id="stage-950"></span>950 | I fought my way through the roundlings. But Clevred was seriously wounded in the fight. He was just able to give me his beloved artifact.  With a last breath he thanked me for my company and died in my arms.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 448](../maps/ratdom_maze_448.md).</span> | stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) | – | 1,000 XP<br>clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)<br>clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)<br>sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13)<br>gives 1× [Rat's artifact](../items/ratdom_artefact.md)<br>removes monsters from home<br>removes monsters from ratdom_bwm1<br>removes monsters from ratdom_maze_448<br>removes monsters from ratdom_maze_627 |
| <span id="stage-960"></span>960 | I persuaded Clevred to leave the artifact behind. Clevred obeyed disappointedly, but he left me on the spot. | [Roundling](../monsters/ratdom_roundling2.md) ([ratdom_maze_448](../maps/ratdom_maze_448.md)) | – | 10 XP<br>clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)<br>clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)<br>sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13)<br>removes monsters from ratdom_maze_627<br>removes monsters from ratdom_maze_448<br>removes monsters from home<br>removes monsters from ratdom_bwm1 |
| <span id="stage-999"></span>999 | I fell asleep just in front of my bed. After long hours of deep and dreamless sleep I woke up - all the rats were gone! Was it only a dream? **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | stepping on a trigger on [home](../maps/home.md) | stage 950 | 20,000 XP<br>clears stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)<br>removes monsters from crossglen<br>changes map crossglen |

<span id="untraced"></span>*No trigger*: nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 2 routes"

    1. stepping on a trigger on [home](../maps/home.md) → the conversation leads here automatically — **conditions:** NOT reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); NOT reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940); NOT reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 100 of [odair (hidden flag)](../quests/odair.md#stage-100); reached stage 30 of [bonemeal (hidden flag)](../quests/bonemeal.md#stage-30); reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115); reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190); have 9,000 gold → **stage 10**; also sets stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), sets stage 2 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-2), sets stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen, starts timer “ratdom_rat_eatme”, starts timer “ratdom_rat_drinkme”, starts timer “ratdom_compass_tour”, starts timer “ratdom_compass_bwm”
    2. Talk to [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → the conversation leads here automatically → **stage 10**. NPC: “This is my bed - go away!”

???+ note "Stage 30: 1 route"

    1. Talk to [Wise of the wells](../monsters/ratdom_well_wise3.md) ([ratdom_maze_768](../maps/ratdom_maze_768.md)) → choose “Omm... ommm... ommmmm...” — **conditions:** NOT reached stage 30 of [Yellow is it](../quests/ratdom_quest.md#stage-30) → **stage 30**; also gives 1× [Rat skull](../items/ratdom_rat_skelett_skull.md). NPC: “In gratitude for the great joy I give you this rat skull.”

???+ note "Stage 31: 1 route"

    1. stepping on a trigger on [ratdom_maze_535a](../maps/ratdom_maze_535a.md) → the conversation leads here automatically — **conditions:** NOT reached stage 31 of [Yellow is it](../quests/ratdom_quest.md#stage-31) → **stage 31**. NPC: “You grab the content of the gold hunters chest: Some gold nuggets - and a leg bone of a rat!?”

???+ note "Stage 32: 2 routes"

    1. stepping on a trigger on [ratdom_maze_464](../maps/ratdom_maze_464.md) → choose “A bone.” — **conditions:** carry 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md); hand over 1× [Bone](../items/bone.md); hand over 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md) → **stage 32**; also gives 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md). NPC: “You exchange the ancient bone for the wrong bone and try to look as innocent as possible.”
    2. stepping on a trigger on [ratdom_maze_464](../maps/ratdom_maze_464.md) → the conversation leads here automatically — **conditions:** hand over 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md) → **stage 32**; also gives 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md)

???+ note "Stage 33: 1 route"

    1. stepping on a trigger on [ratdom_maze_568](../maps/ratdom_maze_568.md) → the conversation leads here automatically → **stage 33**

???+ note "Stage 34: 1 route"

    1. walking into a blocked passage on [ratdom_maze_543d](../maps/ratdom_maze_543d.md) → choose “Sure. But I'll take this bone here with me.” — **conditions:** NOT reached stage 100 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-100) → **stage 34**; also removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, sets stage 100 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-100), gives 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d. NPC: “You picked the bone from its pedestal. Immediatly the music stopped. Uh oh ...”

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [ratdom_maze_664](../maps/ratdom_maze_664.md) → the conversation leads here automatically — **conditions:** NOT reached stage 35 of [Yellow is it](../quests/ratdom_quest.md#stage-35) → **stage 35**; also gives 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md). NPC: “You find some rat bones on the ground behind the flag.”

???+ note "Stage 36: 1 route"

    1. stepping on a trigger on [ratdom_maze_611](../maps/ratdom_maze_611.md) → the conversation leads here automatically — **conditions:** carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); NOT reached stage 36 of [Yellow is it](../quests/ratdom_quest.md#stage-36) → **stage 36**. NPC: “You wonder why you have found some rat bones in a library.”

???+ note "Stage 37: 2 routes"

    1. Talk to [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) → choose “Yes. Your brother is dead.” — **conditions:** reached stage 71 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-71); reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61) → **stage 37**; also sets stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90), gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md). NPC: “Good. I will shower you with gold, jewels and bones.”
    2. Talk to [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) → choose “Yes. Your brother is dead.” — **conditions:** reached stage 72 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-72); reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62) → **stage 37**; also sets stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90), gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md). NPC: “Good. I will shower you with gold, jewels and bones.”

???+ note "Stage 50: 1 route"

    1. Talk to [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Great. Show me the way out of this rat infested place here.” — **conditions:** reached stage 10 of [More rats!](../quests/ratdom_mikhail.md#stage-10); NOT reached stage 70 of [Yellow is it](../quests/ratdom_quest.md#stage-70) → **stage 50**. NPC: “Sure. You must do me a favor first. Help me to find a yellow, round artifact. Then I'll show you the exit.”

???+ note "Stage 52: 1 route"

    1. Talk to [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “If you say so. And where is this marvel?” — **conditions:** reached stage 50 of [Yellow is it](../quests/ratdom_quest.md#stage-50); NOT reached stage 70 of [Yellow is it](../quests/ratdom_quest.md#stage-70) → **stage 52**. NPC: “It is deep in the rat cave, of course. Use your eyes.”

???+ note "Stage 60: 1 route"

    1. Talk to [Andor's statue](../monsters/ratdom_rat_statue.md) ([crossglen_cave](../maps/crossglen_cave.md)) → the conversation leads here automatically → **stage 60**. NPC: “You see a beautifully crafted statue of your brother Andor.”

???+ note "Stage 70: 1 route"

    1. Talk to [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Not yet. I didn't even know there was a statue in our supply cave. How long has it been there?” — **conditions:** reached stage 60 of [Yellow is it](../quests/ratdom_quest.md#stage-60); reached stage 50 of [Yellow is it](../quests/ratdom_quest.md#stage-50); NOT reached stage 80 of [Yellow is it](../quests/ratdom_quest.md#stage-80) → **stage 70**. NPC: “We erected the statue in honor of Andor for never killing rats.”

???+ note "Stage 80: 1 route"

    1. Talk to [Andor's statue](../monsters/ratdom_rat_statue.md) ([crossglen_cave](../maps/crossglen_cave.md)) → the conversation leads here automatically — **conditions:** reached stage 70 of [Yellow is it](../quests/ratdom_quest.md#stage-70) → **stage 80**. NPC: “Andor's statue may be cleared away with a pickaxe. Hadn't I mentioned it?”

???+ note "Stage 82: 1 route"

    1. Talk to [Audir](../monsters/audir.md) → choose “Great, I'll take it.” — **conditions:** reached stage 80 of [Yellow is it](../quests/ratdom_quest.md#stage-80); NOT reached stage 82 of [Yellow is it](../quests/ratdom_quest.md#stage-82); pay 80 gold → **stage 82**; also gives 1× [Pickhatchet](../items/ratdom_pickaxe.md). NPC: “Here you are.”

???+ note "Stage 90: 1 route"

    1. stepping on a trigger on [crossglen_cave](../maps/crossglen_cave.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); NOT reached stage 3 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-3) → **stage 90**. NPC: “The rock wall looks quite massive. There is just a tiny little hole in the shape of a bone.”

???+ note "Stage 100: 1 route"

    1. stepping on a trigger on [crossglen_cave](../maps/crossglen_cave.md) → choose “What would happen if I put a bone into the hole?” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); NOT reached stage 3 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-3); hand over 1× [Bone](../items/bone.md) → **stage 100**; also sets stage 3 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-3). NPC: “The massive rock wall just disappears!”

???+ note "Stage 130: 1 route"

    1. Talk to [Clevred](../monsters/ratdom_rat_bwm1.md) ([ratdom_bwm1](../maps/ratdom_bwm1.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10) → **stage 130**. NPC: “Your brother was here often. He had made himself rather comfortable.”

???+ note "Stage 200: 1 route"

    1. Talk to [Whootibarfag](../monsters/whootibarfag.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → the conversation leads here automatically → **stage 200**. NPC: “Greetings, young being.”

???+ note "Stage 210: 1 route"

    1. Talk to [Whootibarfag](../monsters/whootibarfag.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “[You hold your breath - from tension, and because of his bad breath.]” — **conditions:** reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); NOT reached stage 210 of [Yellow is it](../quests/ratdom_quest.md#stage-210); NOT Evasion level 4+ → **stage 210**; also +1 [Evasion](../skills/evasion.md). NPC: “Whootibarfag let you in on the secret of the rat escape. This increases your ability to flee and escape.”

???+ note "Stage 310: 2 routes"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “If the skeleton is back, may I pass?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390) → **stage 310**. NPC: “If King Rah is with us again, that would be great! Of course you can then go to our memory hall. You would be our…”
    2. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390) → **stage 310**. NPC: “I can't let you enter our Memorial Hall. We have to get back our skeleton statue of King Rah first.”

???+ note "Stage 320: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md) → **stage 320**. NPC: “Let's have a look ... In total we need the head, the ribs and the back bone, 4 legs and the tail of course.”

???+ note "Stage 321: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) → **stage 321**. NPC: “Let's have a look ... Great! Only King Rah's head is missing. You will find it too, I am sure.”

???+ note "Stage 322: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) → **stage 322**. NPC: “Let's have a look ... Great! Only King Rah's back bone is missing. You will find it too, I am sure.”

???+ note "Stage 323: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md) → **stage 323**. NPC: “Let's have a look ... Great! Only King Rah's rib bones are missing. You will find them too, I am sure.”

???+ note "Stage 324: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) → **stage 324**. NPC: “Let's have a look ... Great! Only King Rah's tail is missing. You will find it too, I am sure.”

???+ note "Stage 325: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); carry 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); carry 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); carry 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) → **stage 325**. NPC: “Let's have a look ... Great! Now we only need the fourth leg. You will find it too, I am sure.”

???+ note "Stage 380: 2 routes"

    1. walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) → choose “Sure. Here you are.” — **conditions:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) → **stage 380**; also sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184). NPC: “Look how nice it looks on the table over there.”
    2. walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) → choose “OK. Here you are.” — **conditions:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) → **stage 380**; also sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184). NPC: “Look how nice it looks on the table over there.”

???+ note "Stage 381: 2 routes"

    1. walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) → choose “Give me 1,000 gold for it.” — **conditions:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) → **stage 381**; also sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184), gives 1000× [Gold coins](../items/gold.md). NPC: “This is a lot of money for our museum. But here you have 1,000 gold.”
    2. walking into a blocked passage on [ratdom_maze_515](../maps/ratdom_maze_515.md) → choose “Give me 1,000 gold for it.” — **conditions:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md) → **stage 381**; also sets stage 184 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-184), gives 1000× [Gold coins](../items/gold.md). NPC: “This is a lot of money for our museum. But here you have 1,000 gold.”

???+ note "Stage 390: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden.md) ([ratdom_maze_624](../maps/ratdom_maze_624.md)) → choose “I have found some bones. May I enter now?” — **conditions:** reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); hand over 1× [Rat skull](../items/ratdom_rat_skelett_skull.md); hand over 4× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md); hand over 1× [Tail bones of a rat](../items/ratdom_rat_skelett_tail.md); hand over 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md); hand over 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) → **stage 390**. NPC: “Let's have a look. Oh, what are my old eyes seeing? King Rah is back, completely! I am overwhelmed with joy! You may…”

???+ note "Stage 395: 1 route"

    1. Talk to [Wart](../monsters/ratdom_rat_warden2.md) ([ratdom_maze_515](../maps/ratdom_maze_515.md)) → choose “Well, if you don't want the gold ...” — **conditions:** NOT reached stage 130 of [Yellow is it](../quests/ratdom_quest.md#stage-130); NOT reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); have 100 gold; pay 100 gold → **stage 395**. NPC: “Wait! [He takes the gold hastily] Sure you can talk to Fraedro. Do you see the stairs over there? Just walk along…”

???+ note "Stage 398: 1 route"

    1. Talk to [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) → choose “I believe you. Go now, while you can.” — **conditions:** reached stage 180 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-180) → **stage 398**; also gives 1× [Fraedro's key](../items/ratdom_fraedro_key.md), removes monsters from ratdom_maze_626. NPC: “What? Thank you, thank you! [Fraedro turns to flee, losing a small golden key in the process]”

???+ note "Stage 399: 1 route"

    1. Talk to [Fraedro](../monsters/ratdom_fraedro.md) ([ratdom_maze_626](../maps/ratdom_maze_626.md)) → choose “Die now!” — **conditions:** reached stage 180 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-180) → **stage 399**

???+ note "Stage 400: 1 route"

    1. walking into a blocked passage on [ratdom_maze_626](../maps/ratdom_maze_626.md) → choose “Insert Fraedro's golden key into the hole.” — **conditions:** hand over 1× [Fraedro's key](../items/ratdom_fraedro_key.md) → **stage 400**. NPC: “The key easily slipped into the hole and vanished! Suddenly a big rumbling makes you close your eyes.”

???+ note "Stage 900: 1 route"

    1. stepping on a trigger on [ratdom_maze_627](../maps/ratdom_maze_627.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10); NOT reached stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11) → **stage 900**; also sets stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), clears stage 12 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-12), spawns monsters on ratdom_maze_627. NPC: “I got it! I got my artifact! Finally!”

???+ note "Stage 940: 1 route"

    1. Talk to [Clevred](../monsters/ratdom_rat.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Farewell. And sorry.” — **conditions:** faction “ratdom_rat_conv2” ≥ 5; NOT reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90) → **stage 940**; also clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), clears stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), sets stage 21 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-21), sets stage 22 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-22), sets stage 23 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-23), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen. NPC: “Bye. We will never meet again.”

???+ note "Stage 942: 1 route"

    1. stepping on a trigger on [ratdom_maze1](../maps/ratdom_maze1.md) → choose “OK, let us try again to find it.” — **conditions:** NOT reached stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10); reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940) → **stage 942**; also clears stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), sets stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), clears stage 21 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-21), clears stage 22 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-22), clears stage 23 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-23), spawns monsters on ratdom_maze_627. NPC: “Great - then let's go!”

???+ note "Stage 948: 1 route"

    1. stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) → the conversation leads here automatically — **conditions:** carry 1× [Rat's artifact](../items/ratdom_artefact.md); reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942); NOT reached stage 948 of [Yellow is it](../quests/ratdom_quest.md#stage-948) → **stage 948**. NPC: “The big yellow cheese now weighs heavily in your bag. Small consolation for the loss of a friend, though.”

???+ note "Stage 950: 1 route"

    1. stepping on a trigger on [ratdom_maze_448](../maps/ratdom_maze_448.md) → the conversation leads here automatically — **conditions:** reached stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11) → **stage 950**; also clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), gives 1× [Rat's artifact](../items/ratdom_artefact.md), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627. NPC: “Wait ...”

???+ note "Stage 960: 1 route"

    1. Talk to [Roundling](../monsters/ratdom_roundling2.md) ([ratdom_maze_448](../maps/ratdom_maze_448.md)) → choose “Die you will, if you can't let go of it. I will leave it behind.” → **stage 960**; also clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1. NPC: “I see. I thought you were braver. Go then, I don't want to see you again!”

???+ note "Stage 999: 1 route"

    1. stepping on a trigger on [home](../maps/home.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90) → **stage 999**; also clears stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen. NPC: “You didn't make it to your bed - again. Nevertheless you took some minutes of sleep. When you woke up, something had…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ratdom_quest` |
    | showInLog | 1 |
    | Stage IDs | 10, 30, 31, 32, 33, 34, 35, 36, 37, 50, 52, 60, 70, 80, 82, 90, 100, 110, 120, 130, 200, 210, 310, 320, 321, 322, 323, 324, 325, 380, 381, 390, 392, 395, 398, 399, 400, 900, 940, 942, 948, 950, 960, 999 |
    | Dialogue nodes setting stages | 10: `ratdom_wakeup_02`, 10: `ratdom_rat`, 30: `ratdom_well_wise3_52`, 31: `ratdom_goldhunter_bone_10`, 32: `ratdom_bone_collector_s1_30`, 32: `ratdom_bone_collector_s2_10`, 33: `ratdom_mz_center_s`, 34: `ratdom_skel_bone_30`, 35: `ratdom_water_x1_10`, 36: `ratdom_check_backbone_10`, 37: `ratdom_skeleton_boss_70_10`, 50: `ratdom_rat_10_10`, 52: `ratdom_rat_52`, 60: `ratdom_rat_statue_20`, 70: `ratdom_rat_60_10`, 80: `ratdom_rat_statue_30`, 82: `ratdom_audir_2`, 90: `crossglen_cave_ratdom_key_10`, 100: `crossglen_cave_ratdom_key_20`, 130: `ratdom_rat_bwm1_10`, 200: `whootibarfag`, 210: `whootibarfag_230`, 310: `ratdom_rat_warden_48`, 310: `ratdom_rat_warden_80`, 320: `ratdom_rat_warden_79`, 321: `ratdom_rat_warden_70a`, 322: `ratdom_rat_warden_76a`, 323: `ratdom_rat_warden_77a`, 324: `ratdom_rat_warden_75a`, 325: `ratdom_rat_warden_71a`, 380: `ratdom_rat_museum_sign_3e_check_12`, 381: `ratdom_rat_museum_sign_3e_check_14`, 390: `ratdom_rat_warden_52`, 395: `ratdom_rat_warden2_r_16b`, 398: `ratdom_fraedro_20`, 399: `ratdom_fraedro_14`, 400: `ratdom_fraedro_key_20`, 900: `ratdom_artefact_ly_02`, 940: `ratdom_rat_250`, 942: `ratdom_maze_rat1_36`, 948: `ratdom_artefact_lc_10`, 950: `ratdom_artefact_la_10`, 960: `ratdom_roundling2_20`, 999: `ratdom_wakeup_92` |
    | Dialogue nodes clearing stages | 940: `ratdom_maze_rat1_36`, 942: `ratdom_rat_250` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
