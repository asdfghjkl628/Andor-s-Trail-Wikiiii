# Lake Laeroth nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ll2_nd` |
| **In journal** | No (hidden flag) |
| **Stages** | 25 |
| **Started by** | stepping on a trigger on [mountainlake22](../maps/mountainlake22.md), stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) |
| **Related quests** | 1 |

</div>

## Overview

> 10=Boat afloat

## Prerequisites to start

**Route 1** (stepping on a trigger on [mountainlake22](../maps/mountainlake22.md)):

- NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)

**Route 2** (stepping on a trigger on [mountainlake27](../maps/mountainlake27.md)):

- reached stage 59 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-59)
- NOT reached stage 40 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-40)
- NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)

**Route 3** (stepping on a trigger on [mountainlake14](../maps/mountainlake14.md)):

- NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)

**Route 4** (stepping on a trigger on [remgard2a](../maps/remgard2a.md)):

- NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A map of the Great Lake Laeroth](lake_map.md#stage-10) | stage 10 reached, for stage 11 here |
| Requires | [A map of the Great Lake Laeroth](lake_map.md#stage-59) | stage 59 reached, for stages 10, 14, 40 here |
| Mutually exclusive | [A map of the Great Lake Laeroth](lake_map.md#stage-50) | stage 50 must NOT be reached, for stage 110 here |
| Unlocks | [A map of the Great Lake Laeroth](lake_map.md#stage-31) | stage 31 there needs stage 10 here |
| Unlocks | [A map of the Great Lake Laeroth](lake_map.md#stage-78) | stage 78 there needs stages 33, 34, 35, 36, 37 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | 10=Boat afloat<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake14](../maps/mountainlake14.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake22](../maps/mountainlake22.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake27](../maps/mountainlake27.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard2a](../maps/remgard2a.md).</span> | stepping on a trigger on [mountainlake22](../maps/mountainlake22.md)<br>stepping on a trigger on [mountainlake27](../maps/mountainlake27.md)<br>stepping on a trigger on [mountainlake14](../maps/mountainlake14.md)<br>+1 more | – | clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11)<br>clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12)<br>clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13)<br>clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14) |
| <span id="stage-11"></span>11 | 11=Boat anchored in Remgard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard2](../maps/remgard2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard2a](../maps/remgard2a.md).</span><br><span class="qnote">🗺️ Part of [Remgard2a](../maps/remgard2a.md) visibly changes.</span> | stepping on a trigger on [remgard2](../maps/remgard2.md)<br>stepping on a trigger on [remgard2a](../maps/remgard2a.md) | stage 10 | clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)<br>clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12)<br>clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13)<br>clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14) |
| <span id="stage-12"></span>12 | 12=Boat anchored at Kalypso<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake14](../maps/mountainlake14.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake14](../maps/mountainlake14.md) visibly changes.</span> | stepping on a trigger on [mountainlake14](../maps/mountainlake14.md) | stage 10 | clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)<br>clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11)<br>clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13)<br>clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14) |
| <span id="stage-13"></span>13 | 13=Boat anchored at Circe<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake22](../maps/mountainlake22.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake22](../maps/mountainlake22.md) visibly changes.</span> | stepping on a trigger on [mountainlake22](../maps/mountainlake22.md) | stage 10 | clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)<br>clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11)<br>clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12)<br>clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14) |
| <span id="stage-14"></span>14 | 14=Boat anchored at Cyclops<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake27](../maps/mountainlake27.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake27](../maps/mountainlake27.md) visibly changes.</span> | stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) | stage 10 | clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10)<br>clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11)<br>clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12)<br>clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13) |
| <span id="stage-20"></span>20 | 20=Sub Boat afloat<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake sub](../maps/mountainlake_sub.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake sub](../maps/mountainlake_sub.md) visibly changes.</span> | stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) | – | – |
| <span id="stage-21"></span>21 | Shallow spot message given | walking into a blocked passage on [mountainlake1](../maps/mountainlake1.md) | – | – |
| <span id="stage-31"></span>31 | 31=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | spawns monsters on mountainlake31<br>removes monsters from mountainlake33<br>removes monsters from mountainlake34<br>removes monsters from mountainlake35<br>removes monsters from mountainlake36<br>removes monsters from mountainlake37<br>clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33)<br>clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34)<br>clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35)<br>clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36)<br>clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37) |
| <span id="stage-33"></span>33 | 33=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | removes monsters from mountainlake31<br>spawns monsters on mountainlake33<br>removes monsters from mountainlake34<br>removes monsters from mountainlake35<br>removes monsters from mountainlake36<br>removes monsters from mountainlake37<br>clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31)<br>clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34)<br>clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35)<br>clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36)<br>clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37) |
| <span id="stage-34"></span>34 | 34=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | removes monsters from mountainlake31<br>removes monsters from mountainlake33<br>spawns monsters on mountainlake34<br>removes monsters from mountainlake35<br>removes monsters from mountainlake36<br>removes monsters from mountainlake37<br>clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31)<br>clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33)<br>clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35)<br>clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36)<br>clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37) |
| <span id="stage-35"></span>35 | 35=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | removes monsters from mountainlake31<br>removes monsters from mountainlake33<br>removes monsters from mountainlake34<br>spawns monsters on mountainlake35<br>removes monsters from mountainlake36<br>removes monsters from mountainlake37<br>clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31)<br>clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33)<br>clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34)<br>clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36)<br>clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37) |
| <span id="stage-36"></span>36 | 36=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | removes monsters from mountainlake31<br>removes monsters from mountainlake33<br>removes monsters from mountainlake34<br>removes monsters from mountainlake35<br>spawns monsters on mountainlake36<br>removes monsters from mountainlake37<br>clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31)<br>clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33)<br>clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34)<br>clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35)<br>clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37) |
| <span id="stage-37"></span>37 | 37=Charybdis aktiv<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake31](../maps/mountainlake31.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake33](../maps/mountainlake33.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake34](../maps/mountainlake34.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake35](../maps/mountainlake35.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake36](../maps/mountainlake36.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake37](../maps/mountainlake37.md).</span> | stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) | – | removes monsters from mountainlake31<br>removes monsters from mountainlake33<br>removes monsters from mountainlake34<br>removes monsters from mountainlake35<br>removes monsters from mountainlake36<br>removes monsters from mountainlake37<br>clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31)<br>clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33)<br>clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34)<br>clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35)<br>clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36) |
| <span id="stage-40"></span>40 | 40=Cyclops roast mentioned<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake27](../maps/mountainlake27.md).</span><br><span class="qnote">🔒 An area on [Mountainlake28](../maps/mountainlake28.md) becomes blocked off.</span> | stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) | – | – |
| <span id="stage-41"></span>41 | 41=Cling to sheep again<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake27](../maps/mountainlake27.md).</span> | stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) | – | removes monsters from mountainlake27<br>changes map mountainlake27 |
| <span id="stage-100"></span>100 | 100=Leofric not needed anymore | walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) | hand over 4× [Earplugs](../items/earplugs.md) | sets stage 42 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-42)<br>removes monsters from remgard_tavern0 |
| <span id="stage-104"></span>104 | 104=Sirene passage free<br><span class="qnote">🔓 You can finally access a previously blocked area on [Mountainlake21](../maps/mountainlake21.md).</span> | walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) | hand over 4× [Earplugs](../items/earplugs.md) | sets stage 44 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-44)<br>sets stage 46 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-46) |
| <span id="stage-110"></span>110 | 110=Polyphem door closed<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ll2 cyclops cave](../maps/ll2_cyclops_cave.md).</span><br><span class="qnote">🔒 An area on [Ll2 cyclops cave](../maps/ll2_cyclops_cave.md) becomes blocked off.</span><br><span class="qnote">🗺️ Part of [Ll2 cyclops cave](../maps/ll2_cyclops_cave.md) visibly changes.</span> | stepping on a trigger on [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | spawns monsters on ll2_cyclops_cave<br>sets stage 50 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-50) |
| <span id="stage-111"></span>111 | 111=Door 1 open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake sub](../maps/mountainlake_sub.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake sub](../maps/mountainlake_sub.md) visibly changes.</span> | stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) | hand over 1× [Wooden green key from Kalypso](../items/ll2_key_kalypso.md) | – |
| <span id="stage-112"></span>112 | 112=Door 2 open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake sub](../maps/mountainlake_sub.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake sub](../maps/mountainlake_sub.md) visibly changes.</span> | stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) | hand over 1× [Golden key from Circe](../items/ll2_key_circe.md) | – |
| <span id="stage-113"></span>113 | 113=Door 3 open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake sub](../maps/mountainlake_sub.md).</span><br><span class="qnote">🗺️ Part of [Mountainlake sub](../maps/mountainlake_sub.md) visibly changes.</span> | stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) | hand over 1× [Tiny grey stone key from Polyphem](../items/ll2_key_polyphem.md) | – |
| <span id="stage-121"></span>121 | 121=Taurophag hit 1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake29](../maps/mountainlake29.md).</span> | stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) | – | applies condition solid_impact |
| <span id="stage-122"></span>122 | 122=Taurophag hit 2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake29](../maps/mountainlake29.md).</span> | stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) | stage 121 | applies condition solid_impact |
| <span id="stage-123"></span>123 | 123=Taurophag hit 3+<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake29](../maps/mountainlake29.md).</span> | stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) | stage 122 | applies condition solid_impact |
| <span id="stage-129"></span>129 | 129=Taurophag dead shown<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake29](../maps/mountainlake29.md).</span> | stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) | – | – |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 4 routes"

    1. stepping on a trigger on [mountainlake22](../maps/mountainlake22.md) → choose “Lift anchors!” — **conditions:** NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 10**; also clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)
    2. stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) → choose “Lift anchors!” — **conditions:** reached stage 59 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-59); NOT reached stage 40 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-40); NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 10**; also clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)
    3. stepping on a trigger on [mountainlake14](../maps/mountainlake14.md) → choose “Lift anchors!” — **conditions:** NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 10**; also clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)
    4. stepping on a trigger on [remgard2a](../maps/remgard2a.md) → choose “Lift anchors!” — **conditions:** NOT reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 10**; also clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)

???+ note "Stage 11: 2 routes"

    1. stepping on a trigger on [remgard2](../maps/remgard2.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-10) → **stage 11**; also clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)
    2. stepping on a trigger on [remgard2a](../maps/remgard2a.md) → choose “Land the ship!” — **conditions:** reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 11**; also clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)

???+ note "Stage 12: 1 route"

    1. stepping on a trigger on [mountainlake14](../maps/mountainlake14.md) → choose “Land the ship!” — **conditions:** reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 12**; also clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10), clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)

???+ note "Stage 13: 1 route"

    1. stepping on a trigger on [mountainlake22](../maps/mountainlake22.md) → choose “Land the ship!” — **conditions:** reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 13**; also clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10), clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 14 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-14)

???+ note "Stage 14: 1 route"

    1. stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) → choose “Land the ship!” — **conditions:** reached stage 59 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-59); NOT reached stage 40 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-40); reached stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10) → **stage 14**; also clears stage 10 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-10), clears stage 11 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-11), clears stage 12 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-12), clears stage 13 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-13)

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) → choose “Lift anchors!” — **conditions:** NOT reached stage 20 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-20) → **stage 20**

???+ note "Stage 21: 1 route"

    1. walking into a blocked passage on [mountainlake1](../maps/mountainlake1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 21 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-21) → **stage 21**. NPC: “Someone is shouting: "Shallows ahead!"”

???+ note "Stage 31: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically → **stage 31**; also spawns monsters on mountainlake31, removes monsters from mountainlake33, removes monsters from mountainlake34, removes monsters from mountainlake35, removes monsters from mountainlake36, removes monsters from mountainlake37, clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33), clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34), clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35), clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36), clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37)

???+ note "Stage 33: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically — **conditions:** random chance (1/2%) → **stage 33**; also removes monsters from mountainlake31, spawns monsters on mountainlake33, removes monsters from mountainlake34, removes monsters from mountainlake35, removes monsters from mountainlake36, removes monsters from mountainlake37, clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31), clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34), clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35), clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36), clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37)

???+ note "Stage 34: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically — **conditions:** random chance (1/3%) → **stage 34**; also removes monsters from mountainlake31, removes monsters from mountainlake33, spawns monsters on mountainlake34, removes monsters from mountainlake35, removes monsters from mountainlake36, removes monsters from mountainlake37, clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31), clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33), clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35), clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36), clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37)

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically — **conditions:** random chance (1/4%) → **stage 35**; also removes monsters from mountainlake31, removes monsters from mountainlake33, removes monsters from mountainlake34, spawns monsters on mountainlake35, removes monsters from mountainlake36, removes monsters from mountainlake37, clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31), clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33), clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34), clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36), clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37)

???+ note "Stage 36: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically — **conditions:** random chance (1/5%) → **stage 36**; also removes monsters from mountainlake31, removes monsters from mountainlake33, removes monsters from mountainlake34, removes monsters from mountainlake35, spawns monsters on mountainlake36, removes monsters from mountainlake37, clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31), clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33), clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34), clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35), clears stage 37 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-37)

???+ note "Stage 37: 1 route"

    1. stepping on a trigger on [mountainlake31](../maps/mountainlake31.md) → the conversation leads here automatically — **conditions:** random chance (1/6%) → **stage 37**; also removes monsters from mountainlake31, removes monsters from mountainlake33, removes monsters from mountainlake34, removes monsters from mountainlake35, removes monsters from mountainlake36, removes monsters from mountainlake37, clears stage 31 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-31), clears stage 33 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-33), clears stage 34 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-34), clears stage 35 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-35), clears stage 36 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-36)

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) → the conversation leads here automatically — **conditions:** reached stage 59 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-59); NOT reached stage 40 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-40) → **stage 40**. NPC: “Ahoy $playername! Have you brought us a fine roast? What a splendid fellow!”

???+ note "Stage 41: 1 route"

    1. stepping on a trigger on [mountainlake27](../maps/mountainlake27.md) → the conversation leads here automatically → **stage 41**; also removes monsters from mountainlake27, changes map mountainlake27. NPC: “So let's get to the ship. The ram can carry me there again.”

???+ note "Stage 100: 1 route"

    1. walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) → choose “Look, I have earplugs here, take them and you can drive through here as often as you like without any…” — **conditions:** hand over 4× [Earplugs](../items/earplugs.md) → **stage 100**; also sets stage 42 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-42), removes monsters from remgard_tavern0. NPC: “Sounds like a plan. And you? How do you plan to stop yourself from simply jumping overboard?”

???+ note "Stage 104: 2 routes"

    1. walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) → choose “I'll take earplugs too, of course.” — **conditions:** hand over 4× [Earplugs](../items/earplugs.md) → **stage 104**; also sets stage 44 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-44). NPC: “That's what we'll do. We'll be the first to cross the Sirens' Passage alive.”
    2. walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) → choose “Just tie me to the mast. And whatever you do, don't untie me, no matter how much I beg.” — **conditions:** hand over 4× [Earplugs](../items/earplugs.md) → **stage 104**; also sets stage 46 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-46). NPC: “That's what we'll do. We'll be the first to cross the Sirens' Passage alive.”

???+ note "Stage 110: 1 route"

    1. stepping on a trigger on [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) → the conversation leads here automatically — **conditions:** NOT reached stage 50 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-50) → **stage 110**; also spawns monsters on ll2_cyclops_cave, spawns monsters on ll2_cyclops_cave, spawns monsters on ll2_cyclops_cave, sets stage 50 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-50)

???+ note "Stage 111: 1 route"

    1. stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) → choose “Use Kalypso's key.” — **conditions:** hand over 1× [Wooden green key from Kalypso](../items/ll2_key_kalypso.md) → **stage 111**. NPC: “You hear a sharp click and a faint rumbling. The key vanishes.”

???+ note "Stage 112: 1 route"

    1. stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) → choose “Use Circe's key.” — **conditions:** hand over 1× [Golden key from Circe](../items/ll2_key_circe.md) → **stage 112**. NPC: “You hear a sharp click and a faint rumbling. The key vanishes.”

???+ note "Stage 113: 1 route"

    1. stepping on a trigger on [mountainlake_sub](../maps/mountainlake_sub.md) → choose “Use Polyphem's key.” — **conditions:** hand over 1× [Tiny grey stone key from Polyphem](../items/ll2_key_polyphem.md) → **stage 113**. NPC: “You hear a sharp click and a faint rumbling. The key vanishes.”

???+ note "Stage 121: 1 route"

    1. stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) → the conversation leads here automatically → **stage 121**; also applies condition solid_impact. NPC: “BOOM!”

???+ note "Stage 122: 1 route"

    1. stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) → the conversation leads here automatically — **conditions:** reached stage 121 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-121) → **stage 122**; also applies condition solid_impact. NPC: “BOOOOOM!”

???+ note "Stage 123: 2 routes"

    1. stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) → the conversation leads here automatically — **conditions:** reached stage 122 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-122) → **stage 123**; also applies condition solid_impact. NPC: “BOOM! BOOOOOM!!”
    2. stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) → the conversation leads here automatically — **conditions:** reached stage 123 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-123) → **stage 123**; also applies condition solid_impact. NPC: “BOOOOM!”

???+ note "Stage 129: 1 route"

    1. stepping on a trigger on [mountainlake29](../maps/mountainlake29.md) → the conversation leads here automatically — **conditions:** killed 1× [Taurophag](../monsters/taurophag.md); NOT reached stage 129 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-129) → **stage 129**. NPC: “The Taurophag is no more. We have survived it!”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ll2_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ll2_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ll2_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ll2_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ll2_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ll2_nd` |
    | showInLog | 0 |
    | Stage IDs | 10, 11, 12, 13, 14, 20, 21, 31, 33, 34, 35, 36, 37, 40, 41, 100, 104, 110, 111, 112, 113, 121, 122, 123, 129 |
    | Dialogue nodes setting stages | 10: `ll2_boat_afloat`, 11: `ll2_boat_init_10`, 11: `ll2_boat_remgard_10`, 12: `ll2_boat_kalypso_10`, 13: `ll2_boat_circe_10`, 14: `ll2_boat_cyclops_10`, 20: `ll2_boat_sub_20`, 21: `ll2_shallow_10`, 31: `ll2_setwhirl_31_1`, 33: `ll2_setwhirl_33_1`, 34: `ll2_setwhirl_34_1`, 35: `ll2_setwhirl_35_1`, 36: `ll2_setwhirl_36_1`, 37: `ll2_setwhirl_37_1`, 40: `ll2_boat_cyclops_4`, 41: `ll2_cyclops_killed`, 100: `ll2_sirene_key_60`, 104: `ll2_sirene_key_70`, 104: `ll2_sirene_key_80`, 110: `polyphem_spawn_10`, 111: `ll2_sub_key1_10`, 112: `ll2_sub_key2_10`, 113: `ll2_sub_key3_10`, 121: `ll2_taurophag_hit_120`, 122: `ll2_taurophag_hit_121`, 123: `ll2_taurophag_hit_122`, 123: `ll2_taurophag_hit_123`, 129: `ll2_taurophag_hit_129` |
    | Dialogue nodes clearing stages | 10: `ll2_boat_init_10`, 10: `ll2_boat_remgard_10`, 10: `ll2_boat_kalypso_10`, 10: `ll2_boat_circe_10`, 10: `ll2_boat_cyclops_10`, 12: `ll2_boat_init_10`, 12: `ll2_boat_remgard_10`, 12: `ll2_boat_afloat`, 12: `ll2_boat_circe_10`, 12: `ll2_boat_cyclops_10` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
