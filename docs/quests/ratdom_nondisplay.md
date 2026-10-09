---
description: "Ratdom story flags is a hidden quest in Andor's Trail, started by stepping on a trigger on home. 88 stages. 1=Ratdom active"
---

# Ratdom story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ratdom_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 88 |
| **Started by** | stepping on a trigger on [Home](../maps/home.md) |
| **NPCs involved** | [Clevred](../monsters/ratdom_rat.md), [Fraedro](../monsters/ratdom_fraedro.md), [Librarian](../monsters/ratdom_librarian.md), [Loirash](../monsters/ratdom_bone_collector.md), [Roundling](../monsters/ratdom_roundling.md#v-ratdom_roundling2), [Wart](../monsters/ratdom_rat_warden.md) +2 |
| **Locations** | [Blackwater mountain 55](../maps/blackwater_mountain55.md), [Crossglen cave](../maps/crossglen_cave.md), [Home](../maps/home.md), [Ratdom maze 1](../maps/ratdom_maze1.md) |
| **Related quests** | 11 |

</div>

## Overview

> 1=Ratdom active

## Prerequisites to start

Start with stepping on a trigger on [Home](../maps/home.md). Required:

- NOT reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
- NOT reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940)
- NOT reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942)
- NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
- reached stage 100 of [Rat infestation](../quests/odair.md#stage-100)
- reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30)
- reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
- reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115)
- reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190)
- have 9,000 gold


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [base_nondisplay](base_nondisplay.md#stage-2) | stage 2 reached, for stages 35, 36, 37 here |
| Requires | [Disallowed substance](bonemeal.md#stage-30) | stage 30 reached, for stages 1, 2, 10 here |
| Requires | [Destined for great things](charwood1.md#stage-115) | stage 115 reached, for stages 1, 2, 10 here |
| Requires | [Searching for madness](lodar2.md#stage-60) | stage 60 reached, for stages 1, 2, 10 here |
| Requires | [Rat infestation](odair.md#stage-100) | stage 100 reached, for stages 1, 2, 10 here |
| Requires | [More rats!](ratdom_mikhail.md#stage-90) | stage 90 reached, for stages 13, 21, 22, 23 here |
| Requires | [Yellow is it](ratdom_quest.md#stage-310) | stage 310 reached, for stage 192 here |
| Requires | [Yellow is it](ratdom_quest.md#stage-940) | stage 940 reached, for stage 10 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-190) | stage 190 reached, for stages 1, 2, 10 here |
| Blocked by | [base_nondisplay](base_nondisplay.md#stage-2) | stage 2 must NOT be reached, for stages 31, 32, 33, 34, 35, 36, 37 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-31) | stage 31 must NOT be reached, for stage 76 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-390) | stage 390 must NOT be reached, for stage 192 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-900) | stage 900 must NOT be reached, for stages 13, 21, 22, 23, 191 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-940) | stage 940 must NOT be reached, for stages 1, 2, 10 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-942) | stage 942 must NOT be reached, for stages 1, 2, 10 here |
| Mutually exclusive | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 must NOT be reached, for stages 1, 2, 10 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-125) | stage 125 there needs stages 40, 41, 42, 43, 44, 45, 46, 47, 48 here |
| Unlocks | [Ratdom maze (hidden flag)](ratdom_maze.md#stage-131) | stage 131 there needs stage 10 here |
| Unlocks | [Ratdom maze (hidden flag)](ratdom_maze.md#stage-132) | stage 132 there needs stage 10 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-10) | stage 10 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-20) | stage 20 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-52) | stage 52 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-54) | stage 54 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-70) | stage 70 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-74) | stage 74 there needs stage 1 here |
| Unlocks | [More rats!](ratdom_mikhail.md#stage-90) | stage 90 there needs stage 1 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-90) | stage 90 there needs stage 1 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-100) | stage 100 there needs stage 1 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-130) | stage 130 there needs stage 10 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-398) | stage 398 there needs stage 180 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-399) | stage 399 there needs stage 180 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-900) | stage 900 there needs stage 10 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-950) | stage 950 there needs stage 11 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 there needs stage 1 here |
| Blocks | [Unusual experiences and achievements](achievements.md#stage-125) | reaching stages 40, 41, 42, 43, 44, 45, 46, 47, 51 here closes stage 125 there |
| Blocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-26) | reaching stage 1 here closes stage 26 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | 1=Ratdom active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span><br><span class="qnote">🔒 An area on [Crossglen](../maps/crossglen.md) becomes blocked off.</span><br><span class="qnote">🗺️ Part of [Crossglen cave](../maps/crossglen_cave.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Crossglen](../maps/crossglen.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Home](../maps/home.md) visibly changes.</span> | stepping on a trigger on [Home](../maps/home.md) | sets stage 10 of [Yellow is it](../quests/ratdom_quest.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen |
| <span id="stage-2"></span>[2](#route-2) | 2=Rat statue act.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | stepping on a trigger on [Home](../maps/home.md) | sets stage 10 of [Yellow is it](../quests/ratdom_quest.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen |
| <span id="stage-3"></span>[3](#route-3) | 3=Maze entry open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen cave](../maps/crossglen_cave.md).</span><br><span class="qnote">🗺️ Part of [Crossglen cave](../maps/crossglen_cave.md) visibly changes.</span> | stepping on a trigger on [Crossglen cave](../maps/crossglen_cave.md) | sets stage 100 of [Yellow is it](../quests/ratdom_quest.md#stage-100) |
| <span id="stage-4"></span>4 | 4 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-5"></span>5 | 5 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-6"></span>6 | 6 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-7"></span>7 | 7 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-8"></span>8 | 8 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-9"></span>9 | 9 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-10"></span>[10](#route-10) | 10=Clevred company<br><span class="qnote">⚡ A scripted event can now trigger on [Crossglen](../maps/crossglen.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 1](../maps/ratdom_maze1.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 2](../maps/ratdom_maze2.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 402](../maps/ratdom_maze_402.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 403](../maps/ratdom_maze_403.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 413](../maps/ratdom_maze_413.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 414](../maps/ratdom_maze_414.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 416](../maps/ratdom_maze_416.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 417](../maps/ratdom_maze_417.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 418](../maps/ratdom_maze_418.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 421](../maps/ratdom_maze_421.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 422](../maps/ratdom_maze_422.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 423](../maps/ratdom_maze_423.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 424](../maps/ratdom_maze_424.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 425](../maps/ratdom_maze_425.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 426](../maps/ratdom_maze_426.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 427](../maps/ratdom_maze_427.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 428](../maps/ratdom_maze_428.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 432](../maps/ratdom_maze_432.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 433](../maps/ratdom_maze_433.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 434](../maps/ratdom_maze_434.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 435](../maps/ratdom_maze_435.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 436](../maps/ratdom_maze_436.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 437](../maps/ratdom_maze_437.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 438](../maps/ratdom_maze_438.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 441](../maps/ratdom_maze_441.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 442](../maps/ratdom_maze_442.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 443](../maps/ratdom_maze_443.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 444](../maps/ratdom_maze_444.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 445](../maps/ratdom_maze_445.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 446](../maps/ratdom_maze_446.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 447](../maps/ratdom_maze_447.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 451](../maps/ratdom_maze_451.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 452](../maps/ratdom_maze_452.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 453](../maps/ratdom_maze_453.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 454](../maps/ratdom_maze_454.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 455](../maps/ratdom_maze_455.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 456](../maps/ratdom_maze_456.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 457](../maps/ratdom_maze_457.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 458](../maps/ratdom_maze_458.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 461](../maps/ratdom_maze_461.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 463](../maps/ratdom_maze_463.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 464](../maps/ratdom_maze_464.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 466](../maps/ratdom_maze_466.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 467](../maps/ratdom_maze_467.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 476](../maps/ratdom_maze_476.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 506](../maps/ratdom_maze_506.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 513](../maps/ratdom_maze_513.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 514](../maps/ratdom_maze_514.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 516](../maps/ratdom_maze_516.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 517](../maps/ratdom_maze_517.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 521](../maps/ratdom_maze_521.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 522](../maps/ratdom_maze_522.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 523](../maps/ratdom_maze_523.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 524](../maps/ratdom_maze_524.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 525](../maps/ratdom_maze_525.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 526](../maps/ratdom_maze_526.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 527](../maps/ratdom_maze_527.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 531](../maps/ratdom_maze_531.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 532](../maps/ratdom_maze_532.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 533](../maps/ratdom_maze_533.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 534](../maps/ratdom_maze_534.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 535](../maps/ratdom_maze_535.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 536](../maps/ratdom_maze_536.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 537](../maps/ratdom_maze_537.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 538](../maps/ratdom_maze_538.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 541](../maps/ratdom_maze_541.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 542](../maps/ratdom_maze_542.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 543](../maps/ratdom_maze_543.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 544](../maps/ratdom_maze_544.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 545](../maps/ratdom_maze_545.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 546](../maps/ratdom_maze_546.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 547](../maps/ratdom_maze_547.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 551](../maps/ratdom_maze_551.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 552](../maps/ratdom_maze_552.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 553](../maps/ratdom_maze_553.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 554](../maps/ratdom_maze_554.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 555](../maps/ratdom_maze_555.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 557](../maps/ratdom_maze_557.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 558](../maps/ratdom_maze_558.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 562](../maps/ratdom_maze_562.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 563](../maps/ratdom_maze_563.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 564](../maps/ratdom_maze_564.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 565](../maps/ratdom_maze_565.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 566](../maps/ratdom_maze_566.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 567](../maps/ratdom_maze_567.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 572](../maps/ratdom_maze_572.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 611](../maps/ratdom_maze_611.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 612](../maps/ratdom_maze_612.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 616](../maps/ratdom_maze_616.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 617](../maps/ratdom_maze_617.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 618](../maps/ratdom_maze_618.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 621](../maps/ratdom_maze_621.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 622](../maps/ratdom_maze_622.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 623](../maps/ratdom_maze_623.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 624](../maps/ratdom_maze_624.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 625](../maps/ratdom_maze_625.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 626](../maps/ratdom_maze_626.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 628](../maps/ratdom_maze_628.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 631](../maps/ratdom_maze_631.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 632](../maps/ratdom_maze_632.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 633](../maps/ratdom_maze_633.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 634](../maps/ratdom_maze_634.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 635](../maps/ratdom_maze_635.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 636](../maps/ratdom_maze_636.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 637](../maps/ratdom_maze_637.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 638](../maps/ratdom_maze_638.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 641](../maps/ratdom_maze_641.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 642](../maps/ratdom_maze_642.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 643](../maps/ratdom_maze_643.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 644](../maps/ratdom_maze_644.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 645](../maps/ratdom_maze_645.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 646](../maps/ratdom_maze_646.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 647](../maps/ratdom_maze_647.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 652](../maps/ratdom_maze_652.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 653](../maps/ratdom_maze_653.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 655](../maps/ratdom_maze_655.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 656](../maps/ratdom_maze_656.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 657](../maps/ratdom_maze_657.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 658](../maps/ratdom_maze_658.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 661](../maps/ratdom_maze_661.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 662](../maps/ratdom_maze_662.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 664](../maps/ratdom_maze_664.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 666](../maps/ratdom_maze_666.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 705](../maps/ratdom_maze_705.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 1](../maps/ratdom_maze1.md).</span> | stepping on a trigger on [Ratdom maze 1](../maps/ratdom_maze1.md), stepping on a trigger on [Home](../maps/home.md) | varies by route (see below) |
| <span id="stage-11"></span>[11](#route-11) | 11=Clevred got artifact<br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 448](../maps/ratdom_maze_448.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 458](../maps/ratdom_maze_458.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span> | stepping on a trigger on [Ratdom maze 627](../maps/ratdom_maze_627.md) | sets stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900), spawns monsters on ratdom_maze_627 |
| <span id="stage-12"></span>[12](#route-12) | 12=Artifact brought back<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 448](../maps/ratdom_maze_448.md).</span> | stepping on a trigger on [Ratdom maze 448](../maps/ratdom_maze_448.md) | removes monsters from ratdom_maze_448 |
| <span id="stage-13"></span>[13](#route-13) | 13=Clevred dead/gone<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 448](../maps/ratdom_maze_448.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 627](../maps/ratdom_maze_627.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 448](../maps/ratdom_maze_448.md), [Clevred](../monsters/ratdom_rat.md) +1 | varies by route (see below) |
| <span id="stage-21"></span>[21](#route-21) | 21=Rat final_1<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span> | walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), [Clevred](../monsters/ratdom_rat.md) | varies by route (see below) |
| <span id="stage-22"></span>[22](#route-22) | 22=Rat final_2<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span> | walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), [Clevred](../monsters/ratdom_rat.md) | varies by route (see below) |
| <span id="stage-23"></span>[23](#route-23) | 23=Rat final_3<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 627](../maps/ratdom_maze_627.md).</span> | walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), [Clevred](../monsters/ratdom_rat.md) | varies by route (see below) |
| <span id="stage-30"></span>[30](#route-30) | 30=Lantern-0 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-31"></span>[31](#route-31) | 31=Lantern-1 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-32"></span>[32](#route-32) | 32=Lantern-2 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-33"></span>[33](#route-33) | 33=Lantern-3 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-34"></span>[34](#route-34) | 34=Lantern-4 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-35"></span>[35](#route-35) | 35=Lantern-5 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-36"></span>[36](#route-36) | 36=Lantern-6 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-37"></span>[37](#route-37) | 37=Lantern-7 init<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-40"></span>[40](#route-40) | 40=Lantern-0 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | varies by route (see below) |
| <span id="stage-41"></span>[41](#route-41) | 41=Lantern-1 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-42"></span>[42](#route-42) | 42=Lantern-2 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-43"></span>[43](#route-43) | 43=Lantern-3 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-44"></span>[44](#route-44) | 44=Lantern-4 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-45"></span>[45](#route-45) | 45=Lantern-5 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-46"></span>[46](#route-46) | 46=Lantern-6 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-47"></span>[47](#route-47) | 47=Lantern-7 on<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 768](../maps/ratdom_maze_768.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-48"></span>[48](#route-48) | 48=Lantern carry | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md) | – |
| <span id="stage-49"></span>[49](#route-49) | 49=Wise3 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | varies by route (see below) |
| <span id="stage-50"></span>[50](#route-50) | 50=talked to Wise3 | [Wise of the wells](../monsters/ratdom_well_wise0.md#v-ratdom_well_wise3) | – |
| <span id="stage-51"></span>[51](#route-51) | 51=Wells cheat<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 768](../maps/ratdom_maze_768.md).</span> | stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md) | removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768 |
| <span id="stage-60"></span>[60](#route-60) | 60=Water: Flag reached<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 664](../maps/ratdom_maze_664.md).</span> | stepping on a trigger on [Ratdom maze 664](../maps/ratdom_maze_664.md) | changes map ratdom_maze_664, changes map ratdom_maze_664 |
| <span id="stage-61"></span>[61](#route-61) | 61=Use ladder<br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 455a](../maps/ratdom_maze_455a.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 455a](../maps/ratdom_maze_455a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 455a](../maps/ratdom_maze_455a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 455a](../maps/ratdom_maze_455a.md) | changes map ratdom_maze_455a |
| <span id="stage-70"></span>[70](#route-70) | 70=GoldHunter above door open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 434b](../maps/ratdom_maze_434b.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 434b](../maps/ratdom_maze_434b.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 434b](../maps/ratdom_maze_434b.md) | – |
| <span id="stage-71"></span>[71](#route-71) | 71=GoldHunter bridge active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 535a](../maps/ratdom_maze_535a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-72"></span>[72](#route-72) | 72=GoldHunter talked to<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-73"></span>[73](#route-73) | 73=GoldHunter bridge burnt<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 535a](../maps/ratdom_maze_535a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-74"></span>[74](#route-74) | 74=Troll bridge thrown<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 434b](../maps/ratdom_maze_434b.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Ratdom maze 535a](../maps/ratdom_maze_535a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-75"></span>[75](#route-75) | 75=Troll bridge active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 434b](../maps/ratdom_maze_434b.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Ratdom maze 535a](../maps/ratdom_maze_535a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-76"></span>[76](#route-76) | 76=Hint Gold hunter<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 535a](../maps/ratdom_maze_535a.md).</span> | stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md) | – |
| <span id="stage-81"></span>[81](#route-81) | 81=Ghost-1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 648](../maps/ratdom_maze_648.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 648](../maps/ratdom_maze_648.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md) | removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648 |
| <span id="stage-82"></span>[82](#route-82) | 82=Ghost-1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 648](../maps/ratdom_maze_648.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 648](../maps/ratdom_maze_648.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md) | spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648 |
| <span id="stage-83"></span>[83](#route-83) | 83=Ghost-1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 648](../maps/ratdom_maze_648.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 648](../maps/ratdom_maze_648.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md) | spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648 |
| <span id="stage-84"></span>[84](#route-84) | 84=Ghost-1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 648](../maps/ratdom_maze_648.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 648](../maps/ratdom_maze_648.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md) | spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648 |
| <span id="stage-90"></span>[90](#route-90) | 90=Entered mole's cage<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 516](../maps/ratdom_maze_516.md).</span> | stepping on a trigger on [Ratdom maze 516](../maps/ratdom_maze_516.md) | removes monsters from ratdom_maze_516, spawns monsters on ratdom_maze_516 |
| <span id="stage-91"></span>[91](#route-91) | 91=531_sw open<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 531](../maps/ratdom_maze_531.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 531](../maps/ratdom_maze_531.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 531](../maps/ratdom_maze_531.md) | – |
| <span id="stage-92"></span>[92](#route-92) | 92=646 statues seen<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 646](../maps/ratdom_maze_646.md).</span> | stepping on a trigger on [Ratdom maze 646](../maps/ratdom_maze_646.md) | – |
| <span id="stage-93"></span>[93](#route-93) | 93=Librarian went away | [Librarian](../monsters/ratdom_librarian.md) | – |
| <span id="stage-94"></span>[94](#route-94) | 94=Hint Library<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 611](../maps/ratdom_maze_611.md).</span> | stepping on a trigger on [Ratdom maze 611](../maps/ratdom_maze_611.md) | – |
| <span id="stage-95"></span>[95](#route-95) | 95=Librarian reading | [Librarian](../monsters/ratdom_librarian.md) | 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md) |
| <span id="stage-100"></span>[100](#route-100) | 100=clock active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | walking into a blocked passage on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, sets stage 34 of [Yellow is it](../quests/ratdom_quest.md#stage-34), 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d |
| <span id="stage-101"></span>[101](#route-101) | 101=Lute_1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 543d](../maps/ratdom_maze_543d.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-102"></span>[102](#route-102) | 102=Horn_1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 543d](../maps/ratdom_maze_543d.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-103"></span>[103](#route-103) | 103=Drum_1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 543d](../maps/ratdom_maze_543d.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-104"></span>[104](#route-104) | 104=Cymb_1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 543d](../maps/ratdom_maze_543d.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-105"></span>[105](#route-105) | 105=Color_1 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-106"></span>[106](#route-106) | 106=Color_2 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-107"></span>[107](#route-107) | 107=Color_3 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-108"></span>[108](#route-108) | 108=Color_4 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-109"></span>[109](#route-109) | 109=Color_5 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 543d](../maps/ratdom_maze_543d.md).</span> | stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md) | – |
| <span id="stage-120"></span>[120](#route-120) | 120=Leg Bone taken<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 464](../maps/ratdom_maze_464.md).</span> | stepping on a trigger on [Ratdom maze 464](../maps/ratdom_maze_464.md) | 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md) |
| <span id="stage-121"></span>[121](#route-121) | 121=Met instrument maker | [Loirash](../monsters/ratdom_bone_collector.md) | – |
| <span id="stage-130"></span>[130](#route-130) | 130=Rah in museum.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 626](../maps/ratdom_maze_626.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 515](../maps/ratdom_maze_515.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 626](../maps/ratdom_maze_626.md) | – |
| <span id="stage-140"></span>[140](#route-140) | 140=Flora warning.<br><span class="qnote">⚡ A scripted event can now trigger on [Ratdom maze 618](../maps/ratdom_maze_618.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 618](../maps/ratdom_maze_618.md).</span> | stepping on a trigger on [Ratdom maze 618](../maps/ratdom_maze_618.md) | – |
| <span id="stage-150"></span>[150](#route-150) | 150=Empty chest seen<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 455](../maps/ratdom_maze_455.md).</span> | stepping on a trigger on [Ratdom maze 455](../maps/ratdom_maze_455.md) | – |
| <span id="stage-162"></span>[162](#route-162) | 162=Troll_2 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | – |
| <span id="stage-163"></span>[163](#route-163) | 163=Troll_3 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | removes monsters from ratdom_maze_517a |
| <span id="stage-164"></span>[164](#route-164) | 162=Troll_4 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a |
| <span id="stage-165"></span>[165](#route-165) | 162=Troll_5 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | removes monsters from ratdom_maze_517a |
| <span id="stage-166"></span>[166](#route-166) | 162=Troll_6 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a |
| <span id="stage-169"></span>[169](#route-169) | 169=Troll_9 spawned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | removes monsters from ratdom_maze_517a, spawns monsters on ratdom_maze_517a |
| <span id="stage-170"></span>[170](#route-170) | 170=Troll door 1 open<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 517](../maps/ratdom_maze_517.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517](../maps/ratdom_maze_517.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 517](../maps/ratdom_maze_517.md) | – |
| <span id="stage-171"></span>[171](#route-171) | 171=Troll door 2 open<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 517a](../maps/ratdom_maze_517a.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 517a](../maps/ratdom_maze_517a.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 517a](../maps/ratdom_maze_517a.md) | – |
| <span id="stage-172"></span>[172](#route-172) | 172=Door 533 open<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 533](../maps/ratdom_maze_533.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 533](../maps/ratdom_maze_533.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 533](../maps/ratdom_maze_533.md) | – |
| <span id="stage-173"></span>[173](#route-173) | 173=Door 412 open<br><span class="qnote">🔓 You can finally access a previously blocked area on [Ratdom maze 412](../maps/ratdom_maze_412.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 412](../maps/ratdom_maze_412.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 412](../maps/ratdom_maze_412.md) | – |
| <span id="stage-174"></span>[174](#route-174) | 174=Door 412 from south<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 412](../maps/ratdom_maze_412.md).</span> | stepping on a trigger on [Ratdom maze 412](../maps/ratdom_maze_412.md) | – |
| <span id="stage-180"></span>[180](#route-180) | 180=Veni | [Fraedro](../monsters/ratdom_fraedro.md) | – |
| <span id="stage-181"></span>[181](#route-181) | 181=Store door 1 open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 616](../maps/ratdom_maze_616.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 616](../maps/ratdom_maze_616.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 616](../maps/ratdom_maze_616.md) | – |
| <span id="stage-182"></span>[182](#route-182) | 182=Store door 2 open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 616](../maps/ratdom_maze_616.md).</span><br><span class="qnote">🗺️ Part of [Ratdom maze 616](../maps/ratdom_maze_616.md) visibly changes.</span> | stepping on a trigger on [Ratdom maze 616](../maps/ratdom_maze_616.md) | – |
| <span id="stage-183"></span>[183](#route-183) | 183=Venit | walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md) | spawns monsters on ratdom_maze_627 |
| <span id="stage-184"></span>[184](#route-184) | 184=Donation<br><span class="qnote">🗺️ Part of [Ratdom maze 515](../maps/ratdom_maze_515.md) visibly changes.</span> | walking into a blocked passage on [Ratdom maze 515](../maps/ratdom_maze_515.md) | varies by route (see below) |
| <span id="stage-191"></span>[191](#route-191) | 191=blue compass given | [Whootibarfag](../monsters/whootibarfag.md) | 1× [Blue rat necklace](../items/ratdom_compass_bwm.md) |
| <span id="stage-192"></span>[192](#route-192) | 192=orange compass given | [Wart](../monsters/ratdom_rat_warden.md) | 1× [Orange rat necklace](../items/ratdom_compass_tour.md) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · stepping on a trigger on home · 1 way"

    **Way 1:** Stepping on a trigger on [Home](../maps/home.md)

    - **Needs:** not yet stage 1; not reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940); not reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 100 of [Rat infestation](../quests/odair.md#stage-100); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115); reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190); have 9,000 gold
    - **Gives:** sets stage 10 of [Yellow is it](../quests/ratdom_quest.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen
    - <small>Also: starts timer “ratdom_rat_eatme”, starts timer “ratdom_rat_drinkme”, starts timer “ratdom_compass_tour”, starts timer “ratdom_compass_bwm”</small>


<span id="route-2"></span>

??? note "Stage 2 · stepping on a trigger on home · 1 way"

    **Way 1:** Stepping on a trigger on [Home](../maps/home.md)

    - **Needs:** not yet stage 1; not reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940); not reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 100 of [Rat infestation](../quests/odair.md#stage-100); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115); reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190); have 9,000 gold
    - **Gives:** sets stage 10 of [Yellow is it](../quests/ratdom_quest.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen
    - <small>Also: starts timer “ratdom_rat_eatme”, starts timer “ratdom_rat_drinkme”, starts timer “ratdom_compass_tour”, starts timer “ratdom_compass_bwm”</small>


<span id="route-3"></span>

??? note "Stage 3 · stepping on a trigger on crossglen_cave · 1 way"

    **Way 1:** Stepping on a trigger on [Crossglen cave](../maps/crossglen_cave.md), choose “What would happen if I put a bone into the hole?”

    - **Needs:** stage 1; not yet stage 3; hand over 1× [Bone](../items/bone.md)
    - **Gives:** sets stage 100 of [Yellow is it](../quests/ratdom_quest.md#stage-100)
    - *“The massive rock wall just disappears!”*


<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on ratdom_maze1, stepping on a trigger · 2 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 1](../maps/ratdom_maze1.md), choose “OK, let us try again to find it.”

    - **Needs:** not yet stage 10; reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940)
    - **Gives:** clears stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), sets stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), spawns monsters on ratdom_maze_627
    - <small>Also: clears stage 13 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), clears stage 21 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-21), clears stage 22 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-22), clears stage 23 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-23)</small>
    - *“Great - then let's go!”*

    **Way 2:** Stepping on a trigger on [Home](../maps/home.md)

    - **Needs:** not yet stage 1; not reached stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940); not reached stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 100 of [Rat infestation](../quests/odair.md#stage-100); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115); reached stage 190 of [Colonel Lutarc](../quests/stn_colonel.md#stage-190); have 9,000 gold
    - **Gives:** sets stage 10 of [Yellow is it](../quests/ratdom_quest.md#stage-10), changes map home, spawns monsters on home, spawns monsters on home, spawns monsters on crossglen_cave, spawns monsters on crossglen, spawns monsters on crossglen, spawns monsters on crossglen, changes map crossglen
    - <small>Also: starts timer “ratdom_rat_eatme”, starts timer “ratdom_rat_drinkme”, starts timer “ratdom_compass_tour”, starts timer “ratdom_compass_bwm”</small>


<span id="route-11"></span>

??? note "Stage 11 · stepping on a trigger on ratdom_maze_627 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 627](../maps/ratdom_maze_627.md)

    - **Needs:** stage 10; not yet stage 11
    - **Gives:** sets stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900), spawns monsters on ratdom_maze_627
    - <small>Also: clears stage 12 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-12)</small>
    - *“I got it! I got my artifact! Finally!”*


<span id="route-12"></span>

??? note "Stage 12 · stepping on a trigger on ratdom_maze_448 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 448](../maps/ratdom_maze_448.md)

    - **Needs:** stage 11
    - **Gives:** removes monsters from ratdom_maze_448
    - <small>Also: clears stage 11 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)</small>
    - *“The artifact was taken back obviously by the roundlings.”*


<span id="route-13"></span>

??? note "Stage 13 · stepping on a trigger on ratdom_maze_448, Clevred, Roundling · 3 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 448](../maps/ratdom_maze_448.md)

    - **Needs:** stage 11
    - **Gives:** sets stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950), 1× [Rat's artifact](../items/ratdom_artefact.md), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627
    - <small>Also: clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)</small>
    - *“Wait ...”*

    **Way 2:** Talk to [Clevred](../monsters/ratdom_rat.md), choose “Farewell. And sorry.”

    - **Needs:** faction “ratdom_rat_conv2” ≥ 5; not reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90)
    - **Gives:** sets stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen
    - <small>Also: clears stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)</small>
    - *“Bye. We will never meet again.”*

    **Way 3:** Talk to [Roundling](../monsters/ratdom_roundling.md#v-ratdom_roundling2), choose “Die you will, if you can't let go of it. I will leave it behind.”

    - **Gives:** sets stage 960 of [Yellow is it](../quests/ratdom_quest.md#stage-960), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1
    - <small>Also: clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-11)</small>
    - *“I see. I thought you were braver. Go then, I don't want to see you again!”*


<span id="route-21"></span>

??? note "Stage 21 · walking into a blocked passage on ratdom_maze_627, Clevred · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), choose “Are you sure?”

    - *“Of course.”*

    **Way 2:** Talk to [Clevred](../monsters/ratdom_rat.md), choose “Farewell. And sorry.”

    - **Needs:** faction “ratdom_rat_conv2” ≥ 5; not reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90)
    - **Gives:** sets stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen
    - <small>Also: clears stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)</small>
    - *“Bye. We will never meet again.”*


<span id="route-22"></span>

??? note "Stage 22 · walking into a blocked passage on ratdom_maze_627, Clevred · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), choose “Hush!”


    **Way 2:** Talk to [Clevred](../monsters/ratdom_rat.md), choose “Farewell. And sorry.”

    - **Needs:** faction “ratdom_rat_conv2” ≥ 5; not reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90)
    - **Gives:** sets stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen
    - <small>Also: clears stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)</small>
    - *“Bye. We will never meet again.”*


<span id="route-23"></span>

??? note "Stage 23 · walking into a blocked passage on ratdom_maze_627, Clevred · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), choose “He hasn't noticed us yet.”

    - *“I am not so sure. Roundlings are a strange folk.”*

    **Way 2:** Talk to [Clevred](../monsters/ratdom_rat.md), choose “Farewell. And sorry.”

    - **Needs:** faction “ratdom_rat_conv2” ≥ 5; not reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90)
    - **Gives:** sets stage 940 of [Yellow is it](../quests/ratdom_quest.md#stage-940), clears stage 942 of [Yellow is it](../quests/ratdom_quest.md#stage-942), removes monsters from home, removes monsters from ratdom_bwm1, removes monsters from ratdom_maze_448, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from crossglen, removes monsters from crossglen, removes monsters from crossglen, changes map crossglen
    - <small>Also: clears stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1), clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10)</small>
    - *“Bye. We will never meet again.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37


<span id="route-31"></span>

??? note "Stage 31 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2)


<span id="route-32"></span>

??? note "Stage 32 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%)


<span id="route-33"></span>

??? note "Stage 33 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%)


<span id="route-34"></span>

??? note "Stage 34 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%)


<span id="route-35"></span>

??? note "Stage 35 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%); reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2)


<span id="route-36"></span>

??? note "Stage 36 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%); reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2)


<span id="route-37"></span>

??? note "Stage 37 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** not yet stage 30, 31, 32, 33, 34, 35, 36, 37; not reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2); random chance (50%); reached stage 2 of [base_nondisplay](../quests/base_nondisplay.md#stage-2)


<span id="route-40"></span>

??? note "Stage 40 · walking into a blocked passage on ratdom_maze_768, stepping  · 3 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 41, 44, 45; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Gives:** removes monsters from ratdom_maze_768
    - <small>Also: clears stage 49 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-49)</small>


<span id="route-41"></span>

??? note "Stage 41 · walking into a blocked passage on ratdom_maze_768, stepping  · 3 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 44, 45; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30


<span id="route-42"></span>

??? note "Stage 42 · walking into a blocked passage on ratdom_maze_768, stepping  · 4 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 45, 47; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 44; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 4:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31


<span id="route-43"></span>

??? note "Stage 43 · walking into a blocked passage on ratdom_maze_768, stepping  · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31, 32


<span id="route-44"></span>

??? note "Stage 44 · walking into a blocked passage on ratdom_maze_768, stepping  · 4 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 45; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43, 44; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 4:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31, 32, 33


<span id="route-45"></span>

??? note "Stage 45 · walking into a blocked passage on ratdom_maze_768, stepping  · 4 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 47; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43, 44, 45; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 4:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31, 32, 33, 34


<span id="route-46"></span>

??? note "Stage 46 · walking into a blocked passage on ratdom_maze_768, stepping  · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43, 44, 45, 46; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31, 32, 33, 34, 35


<span id="route-47"></span>

??? note "Stage 47 · walking into a blocked passage on ratdom_maze_768, stepping  · 3 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43, 44, 45, 46, 47; not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)

    **Way 3:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md)

    - **Needs:** stage 30, 31, 32, 33, 34, 35, 36


<span id="route-48"></span>

??? note "Stage 48 · walking into a blocked passage on ratdom_maze_768 · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** not yet stage 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)


<span id="route-49"></span>

??? note "Stage 49 · walking into a blocked passage on ratdom_maze_768, stepping  · 5 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 44, 45; not yet stage 40, 41, 42, 43, 44, 45, 46, 47, 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768, sets stage 125 of [Unusual experiences and achievements](../quests/achievements.md#stage-125)

    **Way 2:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 42, 45, 47; not yet stage 40, 41, 42, 43, 44, 45, 46, 47, 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768, sets stage 125 of [Unusual experiences and achievements](../quests/achievements.md#stage-125)

    **Way 3:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 42, 44; not yet stage 40, 41, 42, 43, 44, 45, 46, 47, 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768, sets stage 125 of [Unusual experiences and achievements](../quests/achievements.md#stage-125)

    **Way 4:** Walking into a blocked passage on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “You throw a shimmering globe into the well.”

    - **Needs:** stage 40, 41, 42, 43, 44, 45, 46, 47, 48; not yet stage 40, 41, 42, 43, 44, 45, 46, 47, 51; hand over 1× [Shimmering globe](../items/ratdom_wells_ball.md)
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768, sets stage 125 of [Unusual experiences and achievements](../quests/achievements.md#stage-125)

    **Way 5:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “Please do. Here, take the balls.”

    - **Needs:** stage 10; faction “ratdom_wells” = 5
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768
    - <small>Also: clears stage 40 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-40), clears stage 41 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-41), clears stage 42 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-42), clears stage 43 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-43), clears stage 44 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-44), clears stage 45 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-45), clears stage 46 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-46), clears stage 47 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-47)</small>
    - *“Ready. I hope you watched closely how I did it.”*


<span id="route-50"></span>

??? note "Stage 50 · Wise of the wells · 1 way"

    **Way 1:** Talk to [Wise of the wells](../monsters/ratdom_well_wise0.md#v-ratdom_well_wise3), choose “Hi! I am $playername.”

    - **Needs:** not yet stage 50


<span id="route-51"></span>

??? note "Stage 51 · stepping on a trigger on ratdom_maze_768 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 768](../maps/ratdom_maze_768.md), choose “Please do. Here, take the balls.”

    - **Needs:** stage 10; faction “ratdom_wells” = 5
    - **Gives:** removes monsters from ratdom_maze_768, removes monsters from ratdom_maze_768, spawns monsters on ratdom_maze_768
    - <small>Also: clears stage 40 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-40), clears stage 41 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-41), clears stage 42 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-42), clears stage 43 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-43), clears stage 44 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-44), clears stage 45 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-45), clears stage 46 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-46), clears stage 47 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-47)</small>
    - *“Ready. I hope you watched closely how I did it.”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on ratdom_maze_664 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 664](../maps/ratdom_maze_664.md)

    - **Gives:** changes map ratdom_maze_664, changes map ratdom_maze_664


<span id="route-61"></span>

??? note "Stage 61 · stepping on a trigger on ratdom_maze_455a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 455a](../maps/ratdom_maze_455a.md)

    - **Needs:** not yet stage 61
    - **Gives:** changes map ratdom_maze_455a


<span id="route-70"></span>

??? note "Stage 70 · stepping on a trigger on ratdom_maze_434b · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 434b](../maps/ratdom_maze_434b.md), choose “Aww, is the little brute angry now?”

    - **Needs:** not yet stage 70
    - *“It is ENOUGH now! I'll teach you manners!”*


<span id="route-71"></span>

??? note "Stage 71 · stepping on a trigger on ratdom_maze_535a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md), choose “That's exactly what I need! Let's build a bridge ...”

    - **Needs:** not yet stage 71, 73, 74, 75; killed 1× [Gold hunter](../monsters/ratdom_goldhunter.md)
    - *“So that looks sturdy enough to carry a person.”*


<span id="route-72"></span>

??? note "Stage 72 · stepping on a trigger on ratdom_maze_535a · 2 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md)

    - **Needs:** stage 72; not killed 1× [Gold hunter](../monsters/ratdom_goldhunter.md)
    - *“Leave me alone!”*

    **Way 2:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md)

    - **Needs:** stage 72; not killed 1× [Gold hunter](../monsters/ratdom_goldhunter.md)
    - *“Leave me alone!”*


<span id="route-73"></span>

??? note "Stage 73 · stepping on a trigger on ratdom_maze_535a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md), choose “[Light the wood]”

    - **Needs:** stage 10; not yet stage 71, 73, 74, 75; killed 1× [Gold hunter](../monsters/ratdom_goldhunter.md)
    - <small>Also: starts timer “ratdom_hunter_bridge”</small>
    - *“Farewell then. I will think of you when I have the artifact in my claws!”*


<span id="route-74"></span>

??? note "Stage 74 · stepping on a trigger on ratdom_maze_535a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md)

    - **Needs:** stage 73; not yet stage 74; 6 rounds passed since timer “ratdom_hunter_bridge”
    - *“Ouch! Something heavy fell on your head!”*


<span id="route-75"></span>

??? note "Stage 75 · stepping on a trigger on ratdom_maze_535a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md), choose “Now at last let's build the bridge.”

    - **Needs:** stage 74; not yet stage 75
    - <small>Also: clears stage 73 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-73), clears stage 74 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-74)</small>
    - *“So that looks sturdy enough to carry a person.”*


<span id="route-76"></span>

??? note "Stage 76 · stepping on a trigger on ratdom_maze_535a · 2 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md)

    - **Needs:** stage 10; not yet stage 76; not reached stage 31 of [Yellow is it](../quests/ratdom_quest.md#stage-31)
    - *“Why didn't you take the bones with you?”*

    **Way 2:** Stepping on a trigger on [Ratdom maze 535a](../maps/ratdom_maze_535a.md)

    - **Needs:** not yet stage 76; not reached stage 31 of [Yellow is it](../quests/ratdom_quest.md#stage-31)
    - *“I should take a closer look back on the isle.”*


<span id="route-81"></span>

??? note "Stage 81 · stepping on a trigger on ratdom_maze_648 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md)

    - **Gives:** removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648
    - <small>Also: clears stage 82 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-82), clears stage 83 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-83), clears stage 84 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-84)</small>


<span id="route-82"></span>

??? note "Stage 82 · stepping on a trigger on ratdom_maze_648 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md)

    - **Gives:** spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648
    - <small>Also: clears stage 81 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-81), clears stage 83 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-83), clears stage 84 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-84)</small>


<span id="route-83"></span>

??? note "Stage 83 · stepping on a trigger on ratdom_maze_648 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md)

    - **Gives:** spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648, spawns monsters on ratdom_maze_648
    - <small>Also: clears stage 81 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-81), clears stage 82 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-82), clears stage 84 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-84)</small>


<span id="route-84"></span>

??? note "Stage 84 · stepping on a trigger on ratdom_maze_648 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 648](../maps/ratdom_maze_648.md)

    - **Gives:** spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, spawns monsters on ratdom_maze_648, removes monsters from ratdom_maze_648
    - <small>Also: clears stage 81 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-81), clears stage 82 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-82), clears stage 83 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-83)</small>


<span id="route-90"></span>

??? note "Stage 90 · stepping on a trigger on ratdom_maze_516 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 516](../maps/ratdom_maze_516.md)

    - **Needs:** not yet stage 90
    - **Gives:** removes monsters from ratdom_maze_516, spawns monsters on ratdom_maze_516
    - *“Thief! This is our food!!”*


<span id="route-91"></span>

??? note "Stage 91 · walking into a blocked passage on ratdom_maze_531 · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 531](../maps/ratdom_maze_531.md)

    - **Needs:** wearing [Pickhatchet](../items/ratdom_pickaxe.md)
    - *“With a single well-aimed blow, you bring down the rock face. The noise of the collapsing wall is deafening.”*


<span id="route-92"></span>

??? note "Stage 92 · stepping on a trigger on ratdom_maze_646 · 2 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 646](../maps/ratdom_maze_646.md)

    - **Needs:** stage 10; not yet stage 92
    - *“Hey - these statues are not real! We can just move through them.”*

    **Way 2:** Stepping on a trigger on [Ratdom maze 646](../maps/ratdom_maze_646.md)

    - **Needs:** not yet stage 92
    - *“These statues are not real, you can just move through them.”*


<span id="route-93"></span>

??? note "Stage 93 · Librarian · 1 way"

    **Way 1:** Talk to [Librarian](../monsters/ratdom_librarian.md), choose “Take your time, better to be be thorough!”



<span id="route-94"></span>

??? note "Stage 94 · stepping on a trigger on ratdom_maze_611 · 2 ways"

    **Way 1:** Stepping on a trigger on [Ratdom maze 611](../maps/ratdom_maze_611.md)

    - **Needs:** stage 10, 93; not yet stage 94; not carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md)
    - *“Why didn't you take the bones with you?”*

    **Way 2:** Stepping on a trigger on [Ratdom maze 611](../maps/ratdom_maze_611.md)

    - **Needs:** stage 93; not yet stage 94; not carry 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md)
    - *“I should take a closer look at the library.”*


<span id="route-95"></span>

??? note "Stage 95 · Librarian · 1 way"

    **Way 1:** Talk to [Librarian](../monsters/ratdom_librarian.md), choose “Here I have a new book for your library.”

    - **Needs:** hand over 1× [World History](../items/book_world_history.md)
    - **Gives:** 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md)
    - *“Oh! What a wonder! I always wanted to have a copy of that wonderful book! Here, take this special bone as a token of my everlasting…”*


<span id="route-100"></span>

??? note "Stage 100 · walking into a blocked passage on ratdom_maze_543d · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 543d](../maps/ratdom_maze_543d.md), choose “Sure. But I'll take this bone here with me.”

    - **Needs:** not yet stage 100
    - **Gives:** removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, removes monsters from ratdom_maze_543d, sets stage 34 of [Yellow is it](../quests/ratdom_quest.md#stage-34), 1× [Leg bones of a rat](../items/ratdom_rat_skelett_leg.md), spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d, spawns monsters on ratdom_maze_543d
    - *“You picked the bone from its pedestal. Immediatly the music stopped. Uh oh ...”*


<span id="route-101"></span>

??? note "Stage 101 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100


<span id="route-102"></span>

??? note "Stage 102 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%)


<span id="route-103"></span>

??? note "Stage 103 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%)


<span id="route-104"></span>

??? note "Stage 104 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%)


<span id="route-105"></span>

??? note "Stage 105 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%); random chance (50%); random chance (20%); random chance (25%)
    - <small>Also: clears stage 106 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-106), clears stage 107 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-107), clears stage 108 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-108), clears stage 109 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-109)</small>


<span id="route-106"></span>

??? note "Stage 106 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%); random chance (50%); random chance (20%); random chance (33%)
    - <small>Also: clears stage 105 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-105), clears stage 107 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-107), clears stage 108 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-108), clears stage 109 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-109)</small>


<span id="route-107"></span>

??? note "Stage 107 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%); random chance (50%); random chance (20%)
    - <small>Also: clears stage 105 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-105), clears stage 106 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-106), clears stage 108 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-108), clears stage 109 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-109)</small>


<span id="route-108"></span>

??? note "Stage 108 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%); random chance (50%); random chance (20%)
    - <small>Also: clears stage 105 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-105), clears stage 106 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-106), clears stage 107 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-107), clears stage 109 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-109)</small>


<span id="route-109"></span>

??? note "Stage 109 · stepping on a trigger on ratdom_maze_543d · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 543d](../maps/ratdom_maze_543d.md)

    - **Needs:** not yet stage 100; random chance (80%); random chance (1%); random chance (50%); random chance (20%)
    - <small>Also: clears stage 105 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-105), clears stage 106 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-106), clears stage 107 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-107), clears stage 108 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-108)</small>


<span id="route-120"></span>

??? note "Stage 120 · stepping on a trigger on ratdom_maze_464 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 464](../maps/ratdom_maze_464.md), choose “Take the bone.”

    - **Needs:** not yet stage 120
    - **Gives:** 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md)
    - *“You slip the bone unobtrusively into your pocket.”*


<span id="route-121"></span>

??? note "Stage 121 · Loirash · 1 way"

    **Way 1:** Talk to [Loirash](../monsters/ratdom_bone_collector.md), automatic

    - **Needs:** stage 121
    - *“This cave is a great source of bones of high quality, so I will stay until my instrument is complete.”*


<span id="route-130"></span>

??? note "Stage 130 · stepping on a trigger on ratdom_maze_626 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 626](../maps/ratdom_maze_626.md)



<span id="route-140"></span>

??? note "Stage 140 · stepping on a trigger on ratdom_maze_618 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 618](../maps/ratdom_maze_618.md)

    - **Needs:** stage 10; not yet stage 140
    - *“Wait! I know this place - it is Flora's fountain. This could be a trap!”*


<span id="route-150"></span>

??? note "Stage 150 · stepping on a trigger on ratdom_maze_455 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 455](../maps/ratdom_maze_455.md)

    - **Needs:** not yet stage 150
    - *“This chest is empty.”*


<span id="route-162"></span>

??? note "Stage 162 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 162; killed 2× [Young ogre](../monsters/ratdom_troll_1.md)


<span id="route-163"></span>

??? note "Stage 163 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 163; killed 5× [Weak ogre](../monsters/ratdom_troll_2.md)
    - **Gives:** removes monsters from ratdom_maze_517a


<span id="route-164"></span>

??? note "Stage 164 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 164; killed 10× [Angry ogre](../monsters/ratdom_troll_3.md)
    - **Gives:** removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a


<span id="route-165"></span>

??? note "Stage 165 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 165; killed 12× [Mad ogre](../monsters/ratdom_troll_4.md)
    - **Gives:** removes monsters from ratdom_maze_517a


<span id="route-166"></span>

??? note "Stage 166 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 166; killed 10× [Dangerous ogre](../monsters/ratdom_troll_5.md)
    - **Gives:** removes monsters from ratdom_maze_517a, removes monsters from ratdom_maze_517a


<span id="route-169"></span>

??? note "Stage 169 · stepping on a trigger on ratdom_maze_517a · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 517a](../maps/ratdom_maze_517a.md)

    - **Needs:** not yet stage 169; killed 5× [Ancient ogre](../monsters/ratdom_troll_6.md)
    - **Gives:** removes monsters from ratdom_maze_517a, spawns monsters on ratdom_maze_517a


<span id="route-170"></span>

??? note "Stage 170 · walking into a blocked passage on ratdom_maze_517 · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 517](../maps/ratdom_maze_517.md), choose “Sure. No risk no fun!”

    - **Needs:** stage 10


<span id="route-171"></span>

??? note "Stage 171 · walking into a blocked passage on ratdom_maze_517a · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 517a](../maps/ratdom_maze_517a.md), choose “No, Clevred. We are going inside.”

    - **Needs:** stage 10
    - *“He never listens to me, does he?”*

    **Way 2:** Walking into a blocked passage on [Ratdom maze 517a](../maps/ratdom_maze_517a.md), choose “Open anyway.”



<span id="route-172"></span>

??? note "Stage 172 · walking into a blocked passage on ratdom_maze_533 · 2 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 533](../maps/ratdom_maze_533.md), choose “Open the door.”

    - **Needs:** stage 10
    - *“Wait - the door has no handle on the other side. If we go through, we can't go back.”*

    **Way 2:** Walking into a blocked passage on [Ratdom maze 533](../maps/ratdom_maze_533.md), choose “Open the door.”

    - *“Hmm, the door has no handle on the other side. If I go through, I can't go back.”*


<span id="route-173"></span>

??? note "Stage 173 · walking into a blocked passage on ratdom_maze_412 · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 412](../maps/ratdom_maze_412.md)

    - **Needs:** killed 1× [Feygard patrol watch](../monsters/feygard_patrol_watch.md#v-ratdom_ff_guard)
    - *“Hey, this massive looking gate has a hole.”*


<span id="route-174"></span>

??? note "Stage 174 · stepping on a trigger on ratdom_maze_412 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 412](../maps/ratdom_maze_412.md)



<span id="route-180"></span>

??? note "Stage 180 · Fraedro · 1 way"

    **Way 1:** Talk to [Fraedro](../monsters/ratdom_fraedro.md), choose “King Rah's sword?”

    - **Needs:** not yet stage 180; hand over 1× [Cheese](../items/cheese.md)
    - *“You'll find it further down in the caves. Say the words 'Veni gladio fidelis'.”*


<span id="route-181"></span>

??? note "Stage 181 · stepping on a trigger on ratdom_maze_616 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 616](../maps/ratdom_maze_616.md)

    - <small>Also: clears stage 182 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-182)</small>


<span id="route-182"></span>

??? note "Stage 182 · stepping on a trigger on ratdom_maze_616 · 1 way"

    **Way 1:** Stepping on a trigger on [Ratdom maze 616](../maps/ratdom_maze_616.md)

    - <small>Also: clears stage 181 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-181)</small>


<span id="route-183"></span>

??? note "Stage 183 · walking into a blocked passage on ratdom_maze_627 · 1 way"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 627](../maps/ratdom_maze_627.md), choose “Veni gladio fidelis?”

    - **Needs:** stage 10
    - **Gives:** spawns monsters on ratdom_maze_627
    - *“Yes, yes! It moves ...”*


<span id="route-184"></span>

??? note "Stage 184 · walking into a blocked passage on ratdom_maze_515 · 4 ways"

    **Way 1:** Walking into a blocked passage on [Ratdom maze 515](../maps/ratdom_maze_515.md), choose “Sure. Here you are.”

    - **Needs:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md)
    - **Gives:** sets stage 380 of [Yellow is it](../quests/ratdom_quest.md#stage-380)
    - *“Look how nice it looks on the table over there.”*

    **Way 2:** Walking into a blocked passage on [Ratdom maze 515](../maps/ratdom_maze_515.md), choose “OK. Here you are.”

    - **Needs:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md)
    - **Gives:** sets stage 380 of [Yellow is it](../quests/ratdom_quest.md#stage-380)
    - *“Look how nice it looks on the table over there.”*

    **Way 3:** Walking into a blocked passage on [Ratdom maze 515](../maps/ratdom_maze_515.md), choose “Give me 1,000 gold for it.”

    - **Needs:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md)
    - **Gives:** sets stage 381 of [Yellow is it](../quests/ratdom_quest.md#stage-381), 1000× [Gold coins](../items/gold.md)
    - *“This is a lot of money for our museum. But here you have 1,000 gold.”*

    **Way 4:** Walking into a blocked passage on [Ratdom maze 515](../maps/ratdom_maze_515.md), choose “Give me 1,000 gold for it.”

    - **Needs:** hand over 1× [Rat King Rah's sword](../items/ratdom_rat_sword.md)
    - **Gives:** sets stage 381 of [Yellow is it](../quests/ratdom_quest.md#stage-381), 1000× [Gold coins](../items/gold.md)
    - *“This is a lot of money for our museum. But here you have 1,000 gold.”*


<span id="route-191"></span>

??? note "Stage 191 · Whootibarfag · 1 way"

    **Way 1:** Talk to [Whootibarfag](../monsters/whootibarfag.md), choose “Oh thank you! Here is the gold.”

    - **Needs:** stage 10; not yet stage 191; not reached stage 900 of [Yellow is it](../quests/ratdom_quest.md#stage-900); not have 3,333 gold; not pay 100 gold
    - **Gives:** 1× [Blue rat necklace](../items/ratdom_compass_bwm.md)


<span id="route-192"></span>

??? note "Stage 192 · Wart · 1 way"

    **Way 1:** Talk to [Wart](../monsters/ratdom_rat_warden.md), choose “Oh thank you! Here is the gold.”

    - **Needs:** not yet stage 192; reached stage 310 of [Yellow is it](../quests/ratdom_quest.md#stage-310); not reached stage 390 of [Yellow is it](../quests/ratdom_quest.md#stage-390); not have 5,555 gold; pay 100 gold
    - **Gives:** 1× [Orange rat necklace](../items/ratdom_compass_tour.md)



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 153 lines added |
| [v0.8.6](../versions/0.8.6.md) | Dialogue: 1 line changed<br>· text: “Wait! This could be a trap!” → “Wait! I know this place - it is Flora's fountain. This could be a tra…” |
| [v0.8.16.1](../versions/0.8.16.1.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “This is a lot of money for our museum. But here you have 1000 gold.” → “This is a lot of money for our museum. But here you have {1000} gold.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ratdom_nondisplay` |
    | Name in game data | `ratdom_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 60, 61, 70, 71, 72, 73, 74, 75, 76, 81, 82, 83, 84, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 120, 121, 130, 140, 150, 162, 163, 164, 165, 166, 169, 170, 171, 172, 173, 174, 180, 181, 182, 183, 184, 191, 192 |
    | Dialogue nodes setting stages | 1: `ratdom_wakeup_02`, 2: `ratdom_wakeup_02`, 3: `crossglen_cave_ratdom_key_20`, 10: `ratdom_maze_rat1_36`, 10: `ratdom_wakeup_02`, 11: `ratdom_artefact_ly_02`, 12: `ratdom_artefact_ld_10`, 13: `ratdom_artefact_la_10`, 13: `ratdom_rat_250`, 13: `ratdom_roundling2_20`, 21: `ratdom_rat_final_1_10`, 21: `ratdom_rat_250`, 22: `ratdom_rat_final_2_10`, 22: `ratdom_rat_250`, 23: `ratdom_rat_final_3_10`, 23: `ratdom_rat_250`, 30: `ratdom_wells_init_10b`, 31: `ratdom_wells_init_11b`, 32: `ratdom_wells_init_12b`, 33: `ratdom_wells_init_13b`, 34: `ratdom_wells_init_14b`, 35: `ratdom_wells_init_15b`, 36: `ratdom_wells_init_16b`, 37: `ratdom_wells_init_17b`, 40: `ratdom_well_1_13_0`, 40: `ratdom_well_4_10`, 40: `ratdom_wells_init_20`, 41: `ratdom_well_1_12_0`, 41: `ratdom_well_4_11`, 41: `ratdom_wells_init_21`, 42: `ratdom_well_2_12_0`, 42: `ratdom_well_3_11_0`, 42: `ratdom_well_4_12`, 43: `ratdom_well_4_13`, 43: `ratdom_wells_init_23`, 44: `ratdom_well_1_11_0`, 44: `ratdom_well_3_10_0`, 44: `ratdom_well_4_14`, 45: `ratdom_well_1_10_0`, 45: `ratdom_well_2_11_0`, 45: `ratdom_well_4_15`, 46: `ratdom_well_4_16`, 46: `ratdom_wells_init_26`, 47: `ratdom_well_2_10_0`, 47: `ratdom_well_4_17`, 47: `ratdom_wells_init_27`, 48: `ratdom_well_4_09`, 49: `ratdom_well_20`, 49: `ratdom_wells_chest_52`, 50: `ratdom_well_wise3_10`, 51: `ratdom_wells_chest_52`, 60: `ratdom_water_x1`, 61: `ratdom_ladder_1a`, 70: `ratdom_uglybrute_script_90`, 71: `ratdom_goldhunter_bridge_90`, 72: `ratdom_goldhunter_talk_20`, 73: `ratdom_goldhunter_bridge_80`, 74: `ratdom_goldhunter_bed_10`, 75: `ratdom_goldhunter_bed2_90`, 76: `ratdom_goldhunter_bone_reminder_20`, 76: `ratdom_goldhunter_bone_reminder_26`, 81: `ratdom_ghost1`, 82: `ratdom_ghost2`, 83: `ratdom_ghost3`, 84: `ratdom_ghost4`, 90: `ratdom_maze_mole_fence_30`, 91: `ratdom_531_sw_10`, 92: `ratdom_646_statues_10`, 92: `ratdom_646_statues_12`, 93: `ratdom_librarian_32`, 94: `ratdom_check_backbone_20`, 94: `ratdom_check_backbone_26`, 95: `ratdom_librarian_40`, 100: `ratdom_skel_bone_30`, 101: `ratdom_skel_clock_101_1`, 102: `ratdom_skel_clock_102_1`, 103: `ratdom_skel_clock_103_1`, 104: `ratdom_skel_clock_104_1`, 105: `ratdom_skel_clock_105_1`, 106: `ratdom_skel_clock_105_2`, 107: `ratdom_skel_clock_105_3`, 108: `ratdom_skel_clock_105_4`, 109: `ratdom_skel_clock_105_5`, 120: `ratdom_bone_collector_s1_14`, 121: `ratdom_bone_collector_20`, 130: `ratdom_rat_rah_complete`, 140: `ratdom_rat_flora_warn_10`, 150: `ratdom_455_chest_10`, 162: `ratdom_troll_kill_2`, 163: `ratdom_troll_kill_3`, 164: `ratdom_troll_kill_4`, 165: `ratdom_troll_kill_5`, 166: `ratdom_troll_kill_6`, 169: `ratdom_troll_kill_9`, 170: `ratdom_troll_door1_10`, 171: `ratdom_troll_door2_30`, 171: `ratdom_troll_door2_32`, 172: `ratdom_door_533_12`, 172: `ratdom_door_533_open_10`, 172: `ratdom_door_533_22`, 173: `ratdom_door_412_20`, 174: `ratdom_door_412_1`, 180: `ratdom_fraedro_cheese_30`, 181: `ratdom_store_door1`, 182: `ratdom_store_door2`, 183: `ratdom_rat_sword_key_40`, 184: `ratdom_rat_museum_sign_3e_check_12`, 184: `ratdom_rat_museum_sign_3e_check_14`, 191: `whootibarfag_48a`, 192: `ratdom_rat_warden_99a` |
    | Dialogue nodes clearing stages | 10: `ratdom_artefact_la_10`, 10: `ratdom_rat_250`, 10: `ratdom_roundling2_20`, 11: `ratdom_artefact_la_10`, 11: `ratdom_artefact_ld_10`, 11: `ratdom_roundling2_20`, 12: `ratdom_artefact_ly_02`, 120: `ratdom_bone_collector_s1_22`, 120: `ratdom_bone_collector_s3_10`, 120: `ratdom_bone_collector_54` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
