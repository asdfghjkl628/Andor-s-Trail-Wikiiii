# stn_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `stn_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 83 |
| **Started by** | walking into a blocked passage on [waytogalmore0](../maps/waytogalmore0.md) |
| **NPCs involved** | [Blornvale](../monsters/stoutford_alchemist.md), [Blornvale](../monsters/stoutford_alchemist2.md), [Caeda](../monsters/caeda.md), [Cave troll leader](../monsters/cave_troll_5.md), [Colonel Lutarc](../monsters/stn_colonel.md), [Glade key](../monsters/lakecave2_key.md) +19 |
| **Locations** | [flagstone0](../maps/flagstone0.md), [lakecave2](../maps/lakecave2.md), [remgard0](../maps/remgard0.md), [stoutford_armorer](../maps/stoutford_armorer.md) |
| **Total XP** | 50 |
| **Related quests** | 6 |

</div>

## Overview

> 4=Castle visited

## Prerequisites to start

None: talk to walking into a blocked passage on [waytogalmore0](../maps/waytogalmore0.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A secret garden](secret_garden.md#stage-10) | stage 10 reached, for stage 203 here |
| Requires | [A secret garden](secret_garden.md#stage-60) | stage 60 reached, for stage 205 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-10) | stage 10 reached, for stage 110 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-111) | stage 111 reached, for stage 120 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-121) | stage 121 reached, for stage 130 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-131) | stage 131 reached, for stage 140 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-141) | stage 141 reached, for stage 150 here |
| Requires | [Colonel Lutarc](stn_colonel.md#stage-151) | stage 151 reached, for stage 160 here |
| Requires | [Lost girl looking for lost things](stn_quest_gyra.md#stage-5) | stage 5 reached, for stage 9 here |
| Requires | [The thorns of vengeance](thorns_vengeance.md#stage-20) | stage 20 reached, for stage 202 here |
| Blocked by | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-30) | stage 30 must NOT be reached, for stage 206 here |
| Blocked by | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-32) | stage 32 must NOT be reached, for stage 206 here |
| Blocked by | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-34) | stage 34 must NOT be reached, for stage 206 here |
| Blocked by | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-36) | stage 36 must NOT be reached, for stage 206 here |
| Blocked by | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-38) | stage 38 must NOT be reached, for stage 206 here |
| Mutually exclusive | [A secret garden](secret_garden.md#stage-20) | stage 20 must NOT be reached, for stage 203 here |
| Mutually exclusive | [Colonel Lutarc](stn_colonel.md#stage-20) | stage 20 must NOT be reached, for stage 110 here |
| Mutually exclusive | [Colonel Lutarc](stn_colonel.md#stage-111) | stage 111 must NOT be reached, for stage 51 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-149) | stage 149 there needs stage 44 here |
| Unlocks | [A secret garden](secret_garden.md#stage-30) | stage 30 there needs stage 211 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-111) | stage 111 there needs stage 110 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-121) | stage 121 there needs stage 120 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-131) | stage 131 there needs stage 130 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-141) | stage 141 there needs stage 140 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-151) | stage 151 there needs stage 150 here |
| Unlocks | [Colonel Lutarc](stn_colonel.md#stage-160) | stage 160 there needs stage 160 here |
| Unlocks | [Lost girl looking for lost things](stn_quest_gyra.md#stage-50) | stage 50 there needs stages 13, 17, 21, 41, 42, 43 here |
| Unlocks | [Lost girl looking for lost things](stn_quest_gyra.md#stage-60) | stage 60 there needs stage 19 here |
| Unlocks | [Lost girl looking for lost things](stn_quest_gyra.md#stage-92) | stage 92 there needs stage 44 here |
| Unlocks | [Lost girl looking for lost things](stn_quest_gyra.md#stage-99) | stage 99 there needs stage 44 here |
| Unlocks | [Lost girl looking for lost things](stn_quest_gyra.md#stage-199) | stage 199 there needs stage 44 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-5) | stage 5 there needs stage 48 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-16) | stage 16 there needs stage 48 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-20) | stage 20 there needs stage 46 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-30) | stage 30 there needs stage 46 here |
| Blocks | [Stoutford's old castle](stoutford_castle.md#stage-5) | reaching stage 49 here closes stage 5 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-4"></span>4 | 4=Castle visited | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-5"></span>5 | 5=North gate open<br><span class="qnote">⚡ A scripted event can now trigger on [Waytogalmore0](../maps/waytogalmore0.md).</span><br><span class="qnote">🗺️ Part of [Waytogalmore0](../maps/waytogalmore0.md) visibly changes.</span> | walking into a blocked passage on [waytogalmore0](../maps/waytogalmore0.md) | – | – |
| <span id="stage-6"></span>6 | 6=Horse got food | [Horse](../monsters/stn_horse.md) ([stoutford_castle_stable](../maps/stoutford_castle_stable.md)) | – | 50 XP |
| <span id="stage-7"></span>7 | 7=Grave visited | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-8"></span>8 | 8=South gate open<br><span class="qnote">🗺️ Part of [Waytogalmore1](../maps/waytogalmore1.md) visibly changes.</span> | walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) | stage 9 | – |
| <span id="stage-9"></span>9 | 9=Odirath has repaired the gate | [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) | – | – |
| <span id="stage-10"></span>10 | 10=Gyra roaming | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-11"></span>11 | 11=Gyra in castle1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle1](../maps/stoutford_castle1.md).</span> | [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md))<br>stepping on a trigger on [stoutford_castle1](../maps/stoutford_castle1.md) | stage 12 | sets stage 30 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-30)<br>starts timer “stn_gyra_hint”<br>removes monsters from stoutford_castle1<br>spawns monsters on stoutford_castle1 |
| <span id="stage-12"></span>12 | 12=Gyra in castle0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) | stage 11, stage 13, stage 14 | spawns monsters on stoutford_castle0 |
| <span id="stage-13"></span>13 | 13=Gyra in castle2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle2](../maps/stoutford_castle2.md).</span> | stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) | stage 12 | spawns monsters on stoutford_castle2 |
| <span id="stage-14"></span>14 | 14=Gyra in waytogalmore1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore1](../maps/waytogalmore1.md).</span> | stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) | stage 12, stage 15, stage 16, stage 17, stage 23, stage 24, stage 25 | spawns monsters on waytogalmore1 |
| <span id="stage-15"></span>15 | 15=Gyra in waytogalmore0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | stage 14, stage 18, stage 28 | spawns monsters on waytogalmore0 |
| <span id="stage-16"></span>16 | 16=Gyra in wild22<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild22](../maps/wild22.md).</span> | stepping on a trigger on [wild22](../maps/wild22.md) | stage 14, stage 18, stage 20, stage 23, stage 24 | spawns monsters on wild22 |
| <span id="stage-17"></span>17 | 17=Gyra in castle_tower1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower1](../maps/stoutford_castle_tower1.md).</span> | stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) | stage 14 | spawns monsters on stoutford_castle_tower1 |
| <span id="stage-18"></span>18 | 18=Gyra in wild18<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild18](../maps/wild18.md).</span> | stepping on a trigger on [wild18](../maps/wild18.md) | stage 15, stage 16, stage 19, stage 26 | spawns monsters on wild18 |
| <span id="stage-19"></span>19 | 19=Gyra in wild19<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild19](../maps/wild19.md).</span> | stepping on a trigger on [wild19](../maps/wild19.md) | stage 18 | spawns monsters on wild19 |
| <span id="stage-20"></span>20 | 20=Gyra in barrack0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack0](../maps/stoutford_castle_barrack0.md).</span> | stepping on a trigger on [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) | stage 16, stage 21, stage 22 | spawns monsters on stoutford_castle_barrack0 |
| <span id="stage-21"></span>21 | 21=Gyra in barrack1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack1](../maps/stoutford_castle_barrack1.md).</span> | stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) | stage 20 | spawns monsters on stoutford_castle_barrack1 |
| <span id="stage-22"></span>22 | 22=Gyra in barrack2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack2](../maps/stoutford_castle_barrack2.md).</span> | stepping on a trigger on [stoutford_castle_barrack2](../maps/stoutford_castle_barrack2.md) | stage 20 | spawns monsters on stoutford_castle_barrack2 |
| <span id="stage-23"></span>23 | 23=Gyra in stable<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle stable](../maps/stoutford_castle_stable.md).</span> | stepping on a trigger on [stoutford_castle_stable](../maps/stoutford_castle_stable.md) | stage 14, stage 16 | spawns monsters on stoutford_castle_stable |
| <span id="stage-24"></span>24 | 24=Gyra in castle_tower0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower0](../maps/stoutford_castle_tower0.md).</span> | stepping on a trigger on [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md) | stage 14, stage 16 | spawns monsters on stoutford_castle_tower0 |
| <span id="stage-25"></span>25 | 25=Gyra in castle_shop<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle shop](../maps/stoutford_castle_shop.md).</span> | stepping on a trigger on [stoutford_castle_shop](../maps/stoutford_castle_shop.md) | stage 14 | spawns monsters on stoutford_castle_shop |
| <span id="stage-26"></span>26 | 26=Gyra in tower3<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford tower3](../maps/stoutford_tower3.md).</span> | stepping on a trigger on [stoutford_tower3](../maps/stoutford_tower3.md) | stage 18, stage 27 | spawns monsters on stoutford_tower3 |
| <span id="stage-27"></span>27 | 27=Gyra in tower4<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford tower4](../maps/stoutford_tower4.md).</span> | stepping on a trigger on [stoutford_tower4](../maps/stoutford_tower4.md) | stage 26 | spawns monsters on stoutford_tower4 |
| <span id="stage-28"></span>28 | 28=Gyra in flagstone0<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Flagstone0](../maps/flagstone0.md).</span> | stepping on a trigger on [flagstone0](../maps/flagstone0.md) | stage 15 | spawns monsters on flagstone0 |
| <span id="stage-29"></span>29 | 29=Gyra is carried<br><span class="qnote">⚡ A scripted event can now trigger on [Flagstone0](../maps/flagstone0.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Waytogalmore1](../maps/waytogalmore1.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Wild19](../maps/wild19.md).</span> | [Gyra](../monsters/stn_gyra1.md) ([flagstone0](../maps/flagstone0.md)) | – | applies condition fatigue_minor |
| <span id="stage-31"></span>31 | 31=First place visited<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle2](../maps/stoutford_castle2.md).</span> | stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) | stage 13, stage 32, stage 33 | – |
| <span id="stage-32"></span>32 | 32=Second place visited<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack1](../maps/stoutford_castle_barrack1.md).</span> | stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) | stage 21, stage 31, stage 33 | – |
| <span id="stage-33"></span>33 | 33=Third place visited<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower1](../maps/stoutford_castle_tower1.md).</span> | stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) | stage 17, stage 31, stage 32 | – |
| <span id="stage-41"></span>41 | 41=First place is it<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle2](../maps/stoutford_castle2.md).</span> | stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) | stage 13, stage 32, stage 33 | – |
| <span id="stage-42"></span>42 | 42=Second place is it<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack1](../maps/stoutford_castle_barrack1.md).</span> | stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) | stage 21, stage 31, stage 33 | – |
| <span id="stage-43"></span>43 | 43=Third place is it<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower1](../maps/stoutford_castle_tower1.md).</span> | stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) | stage 17, stage 31, stage 32 | – |
| <span id="stage-44"></span>44 | 44=Bourbon is informed about clearing | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | – | – |
| <span id="stage-45"></span>45 | 45=Mead given | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md), stage 44 | gives 1× [Mead](../items/mead.md) |
| <span id="stage-46"></span>46 | 46=Castle cleared of soldiers<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild18](../maps/wild18.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | – |
| <span id="stage-47"></span>47 | 47=Castle cleared completely<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild18](../maps/wild18.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | – |
| <span id="stage-48"></span>48 | 48=Fight with Erwyn | [Lord Erwyn](../monsters/erwyn.md) ([stoutford_castle0](../maps/stoutford_castle0.md)) | stage 148, stage 49 | – |
| <span id="stage-49"></span>49 | 49=Erwyn2 active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) | carry 2× [Gold coins](../items/erwyn_coin.md) | removes monsters from stoutford_castle0<br>spawns monsters on stoutford_castle0<br>clears stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48) |
| <span id="stage-50"></span>50 | 50=Tea taken<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md))<br>stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | – |
| <span id="stage-51"></span>51 | 51=Duell in progress - no leave<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span><br><span class="qnote">🔒 An area on [Waytogalmore0](../maps/waytogalmore0.md) becomes blocked off.</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | stage 110 | sets stage 111 of [Colonel Lutarc](../quests/stn_colonel.md#stage-111)<br>spawns monsters on the map |
| <span id="stage-60"></span>60 | 60=listened to merchant completely | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-61"></span>61 | 61=talked to merchant place_1 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-62"></span>62 | 62=talked to merchant place_2 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-63"></span>63 | 63=talked to merchant place_3 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-64"></span>64 | 64=talked to merchant place_4 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-65"></span>65 | 65=talked to merchant place_5 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-66"></span>66 | 66=talked to merchant place_6 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-67"></span>67 | 67=talked to merchant place_7 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-68"></span>68 | 68=talked to merchant place_8 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-69"></span>69 | 69=talked to merchant place_9 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-71"></span>71 | 71=temp merchant place_1 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-72"></span>72 | 72=temp merchant place_2 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-73"></span>73 | 73=temp merchant place_3 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-74"></span>74 | 74=temp merchant place_4 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-75"></span>75 | 75=temp merchant place_5 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-76"></span>76 | 76=temp merchant place_6 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-77"></span>77 | 77=temp merchant place_7 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-78"></span>78 | 78=temp merchant place_8 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-79"></span>79 | 79=temp merchant place_9 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-82"></span>82 | 82=bwm_7 maze 2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain1](../maps/blackwater_mountain1.md).</span><br><span class="qnote">🗺️ Part of [Blackwater mountain7](../maps/blackwater_mountain7.md) visibly changes.</span> | stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) | – | – |
| <span id="stage-83"></span>83 | 83=bwm_7 maze 3<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain1](../maps/blackwater_mountain1.md).</span><br><span class="qnote">🗺️ Part of [Blackwater mountain7](../maps/blackwater_mountain7.md) visibly changes.</span> | stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) | stage 82 | clears stage 82 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-82) |
| <span id="stage-84"></span>84 | 84=bwm_7 maze 4<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain1](../maps/blackwater_mountain1.md).</span><br><span class="qnote">🗺️ Part of [Blackwater mountain7](../maps/blackwater_mountain7.md) visibly changes.</span> | stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) | stage 83 | clears stage 83 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-83) |
| <span id="stage-85"></span>85 | 85=bwm_7 maze 5<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain1](../maps/blackwater_mountain1.md).</span><br><span class="qnote">🗺️ Part of [Blackwater mountain7](../maps/blackwater_mountain7.md) visibly changes.</span> | stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) | stage 84 | clears stage 84 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-84) |
| <span id="stage-86"></span>86 | 86=bwm_7 maze 6<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain1](../maps/blackwater_mountain1.md).</span><br><span class="qnote">🗺️ Part of [Blackwater mountain7](../maps/blackwater_mountain7.md) visibly changes.</span> | stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) | stage 85 | clears stage 85 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-85) |
| <span id="stage-110"></span>110 | 110=Monster1 waits<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md))<br>stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20) |
| <span id="stage-120"></span>120 | 120=Monster2 waits<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 112 of [Colonel Lutarc](../quests/stn_colonel.md#stage-112)<br>sets stage 113 of [Colonel Lutarc](../quests/stn_colonel.md#stage-113)<br>removes monsters from waytogalmore0 |
| <span id="stage-130"></span>130 | 130=Monster3 waits<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 122 of [Colonel Lutarc](../quests/stn_colonel.md#stage-122)<br>sets stage 123 of [Colonel Lutarc](../quests/stn_colonel.md#stage-123)<br>removes monsters from waytogalmore0 |
| <span id="stage-140"></span>140 | 140=Monster4 waits<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 132 of [Colonel Lutarc](../quests/stn_colonel.md#stage-132)<br>sets stage 133 of [Colonel Lutarc](../quests/stn_colonel.md#stage-133)<br>removes monsters from waytogalmore0 |
| <span id="stage-148"></span>148 | 148=Erwyn introduced | [Lord Erwyn](../monsters/erwyn.md) ([stoutford_castle0](../maps/stoutford_castle0.md)) | – | – |
| <span id="stage-149"></span>149 | 149=Helm given to Berbane | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-150"></span>150 | 150=Monster5 waits<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 142 of [Colonel Lutarc](../quests/stn_colonel.md#stage-142)<br>sets stage 143 of [Colonel Lutarc](../quests/stn_colonel.md#stage-143)<br>removes monsters from waytogalmore0 |
| <span id="stage-160"></span>160 | <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytogalmore0](../maps/waytogalmore0.md).</span> | stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) | – | sets stage 152 of [Colonel Lutarc](../quests/stn_colonel.md#stage-152)<br>removes monsters from waytogalmore0<br>sets stage 153 of [Colonel Lutarc](../quests/stn_colonel.md#stage-153) |
| <span id="stage-200"></span>200 | 200=Blonvale demands to kill a wolf<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford potion](../maps/stoutford_potion.md).</span> | stepping on a trigger on [stoutford_potion](../maps/stoutford_potion.md) | stage 201 | spawns monsters on stoutford_sw |
| <span id="stage-201"></span>201 | 201=Blornvales Shop1 seen | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) | – | – |
| <span id="stage-202"></span>202 | 202=Blornvales Shop2 enabled<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford potion](../maps/stoutford_potion.md).</span> | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md))<br>stepping on a trigger on [stoutford_potion](../maps/stoutford_potion.md) | stage 201 | – |
| <span id="stage-203"></span>203 | 203=Troll fights | [Cave troll leader](../monsters/cave_troll_5.md) ([lakecave2](../maps/lakecave2.md)) | – | – |
| <span id="stage-204"></span>204 | 204=wall door opened<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wild21a](../maps/wild21a.md).</span><br><span class="qnote">🗺️ Part of [Wild21a](../maps/wild21a.md) visibly changes.</span> | [Stoutford guard](../monsters/stoutford_guard_wild21a.md) ([wild21a](../maps/wild21a.md)) | – | – |
| <span id="stage-205"></span>205 | 205=Caeda retired<br><span class="qnote">🗺️ Part of [Lakecave2](../maps/lakecave2.md) visibly changes.</span> | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | – | removes monsters from remgard0<br>spawns monsters on lakecave2<br>gives 1× [Key to the glade](../items/glade_key.md)<br>removes monsters from lakecave2 |
| <span id="stage-206"></span>206 | 206=Picked a damerilia<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lakecave1](../maps/lakecave1.md).</span> | stepping on a trigger on [lakecave1](../maps/lakecave1.md) | – | gives 1× [Damerilias](../items/damerilias.md)<br>sets stage 30 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-30)<br>starts timer “lakecave1_damerilia1_fetched”<br>clears stage 31 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-31)<br>sets stage 32 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-32)<br>starts timer “lakecave1_damerilia2_fetched”<br>clears stage 33 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-33)<br>sets stage 34 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-34)<br>starts timer “lakecave1_damerilia3_fetched”<br>clears stage 35 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-35)<br>sets stage 36 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-36)<br>starts timer “lakecave1_damerilia4_fetched”<br>clears stage 37 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-37)<br>sets stage 38 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-38)<br>starts timer “lakecave1_damerilia5_fetched”<br>clears stage 39 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-39) |
| <span id="stage-207"></span>207 | 207=Lied about damerilias | dialogue `stoutford_widow_roots30_1_2`, which nothing in the data starts directly | – | – |
| <span id="stage-210"></span>210 | 210=lakecave2 first jump | [Glade key](../monsters/lakecave2_key.md) | – | – |
| <span id="stage-211"></span>211 | 211=lakecave2 shelves fallen on ground<br><span class="qnote">🗺️ Part of [Lakecave2](../maps/lakecave2.md) visibly changes.</span> | [Glade key](../monsters/lakecave2_key.md) | – | changes map lakecave2 |
| <span id="stage-212"></span>212 | 212=lakecave2 key taken<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lakecave2](../maps/lakecave2.md).</span><br><span class="qnote">🗺️ Part of [Lakecave2](../maps/lakecave2.md) visibly changes.</span> | stepping on a trigger on [lakecave2](../maps/lakecave2.md) | stage 211 | gives 1× [Key to the glade](../items/glade_key.md)<br>sets stage 30 of [A secret garden](../quests/secret_garden.md#stage-30) |
| <span id="stage-999"></span>999 | - | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 5: 1 route"

    1. walking into a blocked passage on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically → **stage 5**

???+ note "Stage 6: 1 route"

    1. Talk to [Horse](../monsters/stn_horse.md) ([stoutford_castle_stable](../maps/stoutford_castle_stable.md)) → choose “Oh I see now. They left you here without anything to drink. Wait, Here is a bucket of water.” → **stage 6**. NPC: “[After drinking greedily] Neiiieieiiigh!!”

???+ note "Stage 8: 1 route"

    1. walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 9 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-9) → **stage 8**

???+ note "Stage 9: 1 route"

    1. Talk to [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) → choose “I have tried to open the southern castle gate, but the mechanism seems broken. Can you repair it?” — **conditions:** reached stage 5 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-5); NOT reached stage 9 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-9) → **stage 9**. NPC: “The gate mechanism is broken? No problem. Now that the skeletons are gone, I can fix it for you.”

???+ note "Stage 11: 4 routes"

    1. Talk to [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md)) → choose “Of course I will help you. Just follow me.” → **stage 11**; also sets stage 30 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-30), starts timer “stn_gyra_hint”, removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1. NPC: “I started to look in the main house, but maybe we have to search the whole castle.”
    2. stepping on a trigger on [stoutford_castle1](../maps/stoutford_castle1.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-12) → **stage 11**; also spawns monsters on stoutford_castle1
    3. stepping on a trigger on [stoutford_castle1](../maps/stoutford_castle1.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-12) → **stage 11**; also spawns monsters on stoutford_castle1
    4. stepping on a trigger on [stoutford_castle1](../maps/stoutford_castle1.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-12) → **stage 11**; also spawns monsters on stoutford_castle1

???+ note "Stage 12: 4 routes"

    1. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** reached stage 11 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-11) → **stage 12**; also spawns monsters on stoutford_castle0
    2. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** reached stage 11 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-11) → **stage 12**; also spawns monsters on stoutford_castle0
    3. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** reached stage 13 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-13) → **stage 12**; also spawns monsters on stoutford_castle0
    4. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 12**; also spawns monsters on stoutford_castle0

???+ note "Stage 13: 1 route"

    1. stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-12) → **stage 13**; also spawns monsters on stoutford_castle2

???+ note "Stage 14: 11 routes"

    1. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-12) → **stage 14**; also spawns monsters on waytogalmore1
    2. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 23 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-23) → **stage 14**; also spawns monsters on waytogalmore1
    3. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 14**; also spawns monsters on waytogalmore1
    4. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 15 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-15) → **stage 14**; also spawns monsters on waytogalmore1
    5. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 15 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-15) → **stage 14**; also spawns monsters on waytogalmore1
    6. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-17) → **stage 14**; also spawns monsters on waytogalmore1
    7. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 15 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-15) → **stage 14**; also spawns monsters on waytogalmore1
    8. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 24 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-24) → **stage 14**; also spawns monsters on waytogalmore1
    9. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 14**; also spawns monsters on waytogalmore1
    10. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 23 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-23) → **stage 14**; also spawns monsters on waytogalmore1
    11. stepping on a trigger on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 25 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-25) → **stage 14**; also spawns monsters on waytogalmore1

???+ note "Stage 15: 5 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 15**; also spawns monsters on waytogalmore0
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 15**; also spawns monsters on waytogalmore0
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 15**; also spawns monsters on waytogalmore0
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** reached stage 18 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-18) → **stage 15**; also spawns monsters on waytogalmore0
    5. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** reached stage 28 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-28) → **stage 15**; also spawns monsters on waytogalmore0

???+ note "Stage 16: 7 routes"

    1. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 16**; also spawns monsters on wild22
    2. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 23 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-23) → **stage 16**; also spawns monsters on wild22
    3. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 18 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-18) → **stage 16**; also spawns monsters on wild22
    4. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-20) → **stage 16**; also spawns monsters on wild22
    5. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-20) → **stage 16**; also spawns monsters on wild22
    6. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 16**; also spawns monsters on wild22
    7. stepping on a trigger on [wild22](../maps/wild22.md) → the conversation leads here automatically — **conditions:** reached stage 24 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-24) → **stage 16**; also spawns monsters on wild22

???+ note "Stage 17: 1 route"

    1. stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 17**; also spawns monsters on stoutford_castle_tower1

???+ note "Stage 18: 4 routes"

    1. stepping on a trigger on [wild18](../maps/wild18.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 18**; also spawns monsters on wild18
    2. stepping on a trigger on [wild18](../maps/wild18.md) → the conversation leads here automatically — **conditions:** reached stage 19 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-19) → **stage 18**; also spawns monsters on wild18
    3. stepping on a trigger on [wild18](../maps/wild18.md) → the conversation leads here automatically — **conditions:** reached stage 15 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-15) → **stage 18**; also spawns monsters on wild18
    4. stepping on a trigger on [wild18](../maps/wild18.md) → the conversation leads here automatically — **conditions:** reached stage 26 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-26) → **stage 18**; also spawns monsters on wild18

???+ note "Stage 19: 1 route"

    1. stepping on a trigger on [wild19](../maps/wild19.md) → the conversation leads here automatically — **conditions:** reached stage 18 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-18) → **stage 19**; also spawns monsters on wild19

???+ note "Stage 20: 4 routes"

    1. stepping on a trigger on [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 20**; also spawns monsters on stoutford_castle_barrack0
    2. stepping on a trigger on [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 20**; also spawns monsters on stoutford_castle_barrack0
    3. stepping on a trigger on [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) → the conversation leads here automatically — **conditions:** reached stage 21 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-21) → **stage 20**; also spawns monsters on stoutford_castle_barrack0
    4. stepping on a trigger on [stoutford_castle_barrack0](../maps/stoutford_castle_barrack0.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-22) → **stage 20**; also spawns monsters on stoutford_castle_barrack0

???+ note "Stage 21: 2 routes"

    1. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-20) → **stage 21**; also spawns monsters on stoutford_castle_barrack1
    2. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-20) → **stage 21**; also spawns monsters on stoutford_castle_barrack1

???+ note "Stage 22: 1 route"

    1. stepping on a trigger on [stoutford_castle_barrack2](../maps/stoutford_castle_barrack2.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-20) → **stage 22**; also spawns monsters on stoutford_castle_barrack2

???+ note "Stage 23: 3 routes"

    1. stepping on a trigger on [stoutford_castle_stable](../maps/stoutford_castle_stable.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 23**; also spawns monsters on stoutford_castle_stable
    2. stepping on a trigger on [stoutford_castle_stable](../maps/stoutford_castle_stable.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 23**; also spawns monsters on stoutford_castle_stable
    3. stepping on a trigger on [stoutford_castle_stable](../maps/stoutford_castle_stable.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 23**; also spawns monsters on stoutford_castle_stable

???+ note "Stage 24: 2 routes"

    1. stepping on a trigger on [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 24**; also spawns monsters on stoutford_castle_tower0
    2. stepping on a trigger on [stoutford_castle_tower0](../maps/stoutford_castle_tower0.md) → the conversation leads here automatically — **conditions:** reached stage 16 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-16) → **stage 24**; also spawns monsters on stoutford_castle_tower0

???+ note "Stage 25: 1 route"

    1. stepping on a trigger on [stoutford_castle_shop](../maps/stoutford_castle_shop.md) → the conversation leads here automatically — **conditions:** reached stage 14 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-14) → **stage 25**; also spawns monsters on stoutford_castle_shop

???+ note "Stage 26: 2 routes"

    1. stepping on a trigger on [stoutford_tower3](../maps/stoutford_tower3.md) → the conversation leads here automatically — **conditions:** reached stage 27 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-27) → **stage 26**; also spawns monsters on stoutford_tower3
    2. stepping on a trigger on [stoutford_tower3](../maps/stoutford_tower3.md) → the conversation leads here automatically — **conditions:** reached stage 18 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-18) → **stage 26**; also spawns monsters on stoutford_tower3

???+ note "Stage 27: 1 route"

    1. stepping on a trigger on [stoutford_tower4](../maps/stoutford_tower4.md) → the conversation leads here automatically — **conditions:** reached stage 26 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-26) → **stage 27**; also spawns monsters on stoutford_tower4

???+ note "Stage 28: 1 route"

    1. stepping on a trigger on [flagstone0](../maps/flagstone0.md) → the conversation leads here automatically — **conditions:** reached stage 15 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-15) → **stage 28**; also spawns monsters on flagstone0

???+ note "Stage 29: 1 route"

    1. Talk to [Gyra](../monsters/stn_gyra1.md) ([flagstone0](../maps/flagstone0.md)) → choose “Let me carry you for a while.” → **stage 29**; also applies condition fatigue_minor

???+ note "Stage 31: 2 routes"

    1. stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) → the conversation leads here automatically — **conditions:** reached stage 13 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-13); NOT reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31) → **stage 31**
    2. stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) → the conversation leads here automatically — **conditions:** reached stage 13 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-13); NOT reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 31**

???+ note "Stage 32: 2 routes"

    1. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → the conversation leads here automatically — **conditions:** reached stage 21 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-21); NOT reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32) → **stage 32**
    2. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → the conversation leads here automatically — **conditions:** reached stage 21 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-21); reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); NOT reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 32**

???+ note "Stage 33: 2 routes"

    1. stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-17); NOT reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 33**
    2. stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-17); reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); NOT reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 33**

???+ note "Stage 41: 1 route"

    1. stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) → the conversation leads here automatically — **conditions:** reached stage 13 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-13); NOT reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 41**

???+ note "Stage 42: 1 route"

    1. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → the conversation leads here automatically — **conditions:** reached stage 21 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-21); reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); NOT reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 42**

???+ note "Stage 43: 1 route"

    1. stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) → the conversation leads here automatically — **conditions:** reached stage 17 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-17); reached stage 31 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-31); reached stage 32 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-32); NOT reached stage 33 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-33) → **stage 43**

???+ note "Stage 44: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “...?” — **conditions:** reached stage 44 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-44) → **stage 44**. NPC: “[Loud voice] Pay attention and listen everybody! The castle is free! The trembling is over!”

???+ note "Stage 45: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “I give up.” — **conditions:** reached stage 44 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) → **stage 45**; also gives 1× [Mead](../items/mead.md)

???+ note "Stage 46: 1 route"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 7× [Erwyn's knight](../monsters/erwyn_knight.md); killed 13× [Erwyn's soldier](../monsters/erwyn_soldier.md); killed 7× [Erwyn's soldier](../monsters/erwyn_soldier2.md); killed 4× [Erwyn's soldier](../monsters/erwyn_soldier3.md) → **stage 46**

???+ note "Stage 47: 1 route"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 7× [Erwyn's knight](../monsters/erwyn_knight.md); killed 13× [Erwyn's soldier](../monsters/erwyn_soldier.md); killed 7× [Erwyn's soldier](../monsters/erwyn_soldier2.md); killed 4× [Erwyn's soldier](../monsters/erwyn_soldier3.md); killed 1× [Karth the Unbowed](../monsters/erwyn_commander.md); killed 1× [Lord Erwyn](../monsters/erwyn2.md) → **stage 47**

???+ note "Stage 48: 1 route"

    1. Talk to [Lord Erwyn](../monsters/erwyn.md) ([stoutford_castle0](../maps/stoutford_castle0.md)) → choose “I will serve you - my weapon. Attack!” — **conditions:** reached stage 148 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-148); reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49) → **stage 48**

???+ note "Stage 49: 1 route"

    1. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** carry 2× [Gold coins](../items/erwyn_coin.md); NOT reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49) → **stage 49**; also removes monsters from stoutford_castle0, spawns monsters on stoutford_castle0, clears stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48)

???+ note "Stage 50: 2 routes"

    1. Talk to [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md)) → choose “With pleasure.” — **conditions:** NOT reached stage 110 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-110) → **stage 50**. NPC: “Here you are.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → choose “With pleasure.” — **conditions:** NOT reached stage 110 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-110) → **stage 50**. NPC: “Here you are.”

???+ note "Stage 51: 1 route"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → choose “OK, let's begin.” — **conditions:** reached stage 110 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-110); NOT reached stage 111 of [Colonel Lutarc](../quests/stn_colonel.md#stage-111) → **stage 51**; also sets stage 111 of [Colonel Lutarc](../quests/stn_colonel.md#stage-111), spawns monsters on the map. NPC: “Have a lizard as warm up.”

???+ note "Stage 82: 1 route"

    1. stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) → the conversation leads here automatically → **stage 82**

???+ note "Stage 83: 1 route"

    1. stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) → the conversation leads here automatically — **conditions:** reached stage 82 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-82) → **stage 83**; also clears stage 82 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-82)

???+ note "Stage 84: 1 route"

    1. stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) → the conversation leads here automatically — **conditions:** reached stage 83 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-83) → **stage 84**; also clears stage 83 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-83)

???+ note "Stage 85: 1 route"

    1. stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) → the conversation leads here automatically — **conditions:** reached stage 84 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-84) → **stage 85**; also clears stage 84 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-84)

???+ note "Stage 86: 1 route"

    1. stepping on a trigger on [blackwater_mountain1](../maps/blackwater_mountain1.md) → the conversation leads here automatically — **conditions:** reached stage 85 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-85) → **stage 86**; also clears stage 85 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-85)

???+ note "Stage 110: 2 routes"

    1. Talk to [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md)) → choose “Why not? A little challenge is always good.” — **conditions:** reached stage 10 of [Colonel Lutarc](../quests/stn_colonel.md#stage-10); NOT reached stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20) → **stage 110**; also sets stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20). NPC: “Good. Please go to the foot of this hill, right down there, by the gate.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → choose “Why not? A little challenge is always good.” — **conditions:** reached stage 10 of [Colonel Lutarc](../quests/stn_colonel.md#stage-10); NOT reached stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20) → **stage 110**; also sets stage 20 of [Colonel Lutarc](../quests/stn_colonel.md#stage-20). NPC: “Good. Please go to the foot of this hill, right down there, by the gate.”

???+ note "Stage 120: 4 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 1× [Lizard](../monsters/stn_colonel_mons1.md); latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-111) is 111 → **stage 120**; also sets stage 112 of [Colonel Lutarc](../quests/stn_colonel.md#stage-112). NPC: “Not bad for the first one. Let's have the next.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-111) is 111 → **stage 120**; also sets stage 113 of [Colonel Lutarc](../quests/stn_colonel.md#stage-113), removes monsters from waytogalmore0. NPC: “Lost the first fight already. Well, let's have the next.”
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-111) is 111 → **stage 120**; also sets stage 113 of [Colonel Lutarc](../quests/stn_colonel.md#stage-113), removes monsters from waytogalmore0. NPC: “Lost the first fight already. Well, let's have the next.”
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-111) is 111 → **stage 120**; also sets stage 113 of [Colonel Lutarc](../quests/stn_colonel.md#stage-113), removes monsters from waytogalmore0. NPC: “Lost the first fight already. Well, let's have the next.”

???+ note "Stage 130: 4 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 1× [Skeleton](../monsters/stn_colonel_mons2.md); latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-121) is 121 → **stage 130**; also sets stage 122 of [Colonel Lutarc](../quests/stn_colonel.md#stage-122). NPC: “Nicely done. Let's have the next.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-121) is 121 → **stage 130**; also sets stage 123 of [Colonel Lutarc](../quests/stn_colonel.md#stage-123), removes monsters from waytogalmore0. NPC: “Lost the second fight. Well, I have three more for you.”
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-121) is 121 → **stage 130**; also sets stage 123 of [Colonel Lutarc](../quests/stn_colonel.md#stage-123), removes monsters from waytogalmore0. NPC: “Lost the second fight. Well, I have three more for you.”
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-121) is 121 → **stage 130**; also sets stage 123 of [Colonel Lutarc](../quests/stn_colonel.md#stage-123), removes monsters from waytogalmore0. NPC: “Lost the second fight. Well, I have three more for you.”

???+ note "Stage 140: 4 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 2× [Mikhail](../monsters/stn_colonel_mons3.md); latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-131) is 131 → **stage 140**; also sets stage 132 of [Colonel Lutarc](../quests/stn_colonel.md#stage-132). NPC: “I am impressed. You won the fight with my poser.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-131) is 131 → **stage 140**; also sets stage 133 of [Colonel Lutarc](../quests/stn_colonel.md#stage-133), removes monsters from waytogalmore0, removes monsters from waytogalmore0. NPC: “I knew you would lose this one.”
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-131) is 131 → **stage 140**; also sets stage 133 of [Colonel Lutarc](../quests/stn_colonel.md#stage-133), removes monsters from waytogalmore0, removes monsters from waytogalmore0. NPC: “I knew you would lose this one.”
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-131) is 131 → **stage 140**; also sets stage 133 of [Colonel Lutarc](../quests/stn_colonel.md#stage-133), removes monsters from waytogalmore0, removes monsters from waytogalmore0. NPC: “I knew you would lose this one.”

???+ note "Stage 148: 1 route"

    1. Talk to [Lord Erwyn](../monsters/erwyn.md) ([stoutford_castle0](../maps/stoutford_castle0.md)) → the conversation leads here automatically → **stage 148**. NPC: “You see a heavily armed and cloaked skeleton moving towards you. This must be Lord Erwyn himself.”

???+ note "Stage 150: 4 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 1× [Giant serpent](../monsters/stn_colonel_mons4.md); latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-141) is 141 → **stage 150**; also sets stage 142 of [Colonel Lutarc](../quests/stn_colonel.md#stage-142). NPC: “Nicely done.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-141) is 141 → **stage 150**; also sets stage 143 of [Colonel Lutarc](../quests/stn_colonel.md#stage-143), removes monsters from waytogalmore0. NPC: “Lost against a little worm. Well, well, well.”
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-141) is 141 → **stage 150**; also sets stage 143 of [Colonel Lutarc](../quests/stn_colonel.md#stage-143), removes monsters from waytogalmore0. NPC: “Lost against a little worm. Well, well, well.”
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-141) is 141 → **stage 150**; also sets stage 143 of [Colonel Lutarc](../quests/stn_colonel.md#stage-143), removes monsters from waytogalmore0. NPC: “Lost against a little worm. Well, well, well.”

???+ note "Stage 160: 4 routes"

    1. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** killed 1× [Bully](../monsters/stn_colonel_mons5.md); latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-151) is 151 → **stage 160**; also sets stage 152 of [Colonel Lutarc](../quests/stn_colonel.md#stage-152), removes monsters from waytogalmore0. NPC: “That was it. Relax a bit.”
    2. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-151) is 151 → **stage 160**; also sets stage 153 of [Colonel Lutarc](../quests/stn_colonel.md#stage-153), removes monsters from waytogalmore0. NPC: “Lost the last fight, of course. I thought so.”
    3. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-151) is 151 → **stage 160**; also sets stage 153 of [Colonel Lutarc](../quests/stn_colonel.md#stage-153), removes monsters from waytogalmore0. NPC: “Lost the last fight, of course. I thought so.”
    4. stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) → the conversation leads here automatically — **conditions:** latest stage of [Colonel Lutarc](../quests/stn_colonel.md#stage-151) is 151 → **stage 160**; also sets stage 153 of [Colonel Lutarc](../quests/stn_colonel.md#stage-153), removes monsters from waytogalmore0. NPC: “Lost the last fight, of course. I thought so.”

???+ note "Stage 200: 1 route"

    1. stepping on a trigger on [stoutford_potion](../maps/stoutford_potion.md) → choose “I can handle myself - shall I prove it?” — **conditions:** reached stage 201 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-201); NOT reached stage 202 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-202); NOT reached stage 200 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-200) → **stage 200**; also spawns monsters on stoutford_sw. NPC: “I know - sometimes there is a great dark wolf behind the house. Kill him!”

???+ note "Stage 201: 1 route"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → choose “Sure.” — **conditions:** NOT reached stage 200 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-200) → **stage 201**

???+ note "Stage 202: 2 routes"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically → **stage 202**. NPC: “You have indeed killed this brute behind my house!”
    2. stepping on a trigger on [stoutford_potion](../maps/stoutford_potion.md) → choose “It is not for me of course. My father and his men are fighting in Flagstone right now. They urgently need…” — **conditions:** reached stage 201 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-201); NOT reached stage 202 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-202); NOT reached stage 200 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-200); reached stage 20 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-20) → **stage 202**. NPC: “Ah. Oh. That changes everything. Wait a second.”

???+ note "Stage 203: 1 route"

    1. Talk to [Cave troll leader](../monsters/cave_troll_5.md) ([lakecave2](../maps/lakecave2.md)) → choose “No. That statue is a blessing for the people here. Even if I could, I would not tear it down.” — **conditions:** reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10); NOT reached stage 20 of [A secret garden](../quests/secret_garden.md#stage-20) → **stage 203**. NPC: “Outrageous! I will put you in my pantry now.”

???+ note "Stage 204: 2 routes"

    1. Talk to [Stoutford guard](../monsters/stoutford_guard_wild21a.md) ([wild21a](../maps/wild21a.md)) → choose “Yes.” → **stage 204**. NPC: “OK, then you may pass.”
    2. Talk to [Stoutford guard](../monsters/stoutford_guard_wild21a.md) ([wild21a](../maps/wild21a.md)) → choose “Haha, just kidding. Of course I know it.” → **stage 204**. NPC: “Ah, I knew you did. You may pass.”

???+ note "Stage 205: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → choose “That would be great, thank you.” — **conditions:** reached stage 60 of [A secret garden](../quests/secret_garden.md#stage-60) → **stage 205**; also removes monsters from remgard0, spawns monsters on lakecave2, gives 1× [Key to the glade](../items/glade_key.md), removes monsters from lakecave2. NPC: “Here is the key. I will move to the glade and retire there. It is the most beautiful place in the world.”

???+ note "Stage 206: 5 routes"

    1. stepping on a trigger on [lakecave1](../maps/lakecave1.md) → choose “Yes” — **conditions:** NOT reached stage 30 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-30) → **stage 206**; also gives 1× [Damerilias](../items/damerilias.md), sets stage 30 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-30), starts timer “lakecave1_damerilia1_fetched”, clears stage 31 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-31). NPC: “You picked the flower.”
    2. stepping on a trigger on [lakecave1](../maps/lakecave1.md) → choose “Yes” — **conditions:** NOT reached stage 32 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-32) → **stage 206**; also gives 1× [Damerilias](../items/damerilias.md), sets stage 32 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-32), starts timer “lakecave1_damerilia2_fetched”, clears stage 33 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-33). NPC: “You picked the flower.”
    3. stepping on a trigger on [lakecave1](../maps/lakecave1.md) → choose “Yes” — **conditions:** NOT reached stage 34 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-34) → **stage 206**; also gives 1× [Damerilias](../items/damerilias.md), sets stage 34 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-34), starts timer “lakecave1_damerilia3_fetched”, clears stage 35 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-35). NPC: “You picked the flower.”
    4. stepping on a trigger on [lakecave1](../maps/lakecave1.md) → choose “Yes” — **conditions:** NOT reached stage 36 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-36) → **stage 206**; also gives 1× [Damerilias](../items/damerilias.md), sets stage 36 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-36), starts timer “lakecave1_damerilia4_fetched”, clears stage 37 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-37). NPC: “You picked the flower.”
    5. stepping on a trigger on [lakecave1](../maps/lakecave1.md) → choose “Yes” — **conditions:** NOT reached stage 38 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-38) → **stage 206**; also gives 1× [Damerilias](../items/damerilias.md), sets stage 38 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-38), starts timer “lakecave1_damerilia5_fetched”, clears stage 39 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-39). NPC: “You picked the flower.”

???+ note "Stage 210: 1 route"

    1. Talk to [Glade key](../monsters/lakecave2_key.md) → the conversation leads here automatically — **conditions:** NOT reached stage 210 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-210) → **stage 210**. NPC: “That was close - just half an inch short. Try again!”

???+ note "Stage 211: 1 route"

    1. Talk to [Glade key](../monsters/lakecave2_key.md) → the conversation leads here automatically → **stage 211**; also changes map lakecave2. NPC: “You got hold of the shelves and tore them down!”

???+ note "Stage 212: 1 route"

    1. stepping on a trigger on [lakecave2](../maps/lakecave2.md) → the conversation leads here automatically — **conditions:** reached stage 211 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-211); NOT reached stage 212 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-212) → **stage 212**; also gives 1× [Key to the glade](../items/glade_key.md), sets stage 30 of [A secret garden](../quests/secret_garden.md#stage-30). NPC: “Hey, this looks like Caeda's lost key.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 138 lines added |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Hey, this looks like Caedas lost key.” → “Hey, this looks like Caeda's lost key.” |
| [v0.8.9](../versions/0.8.9.md) | Dialogue: 1 line changed |
| [v0.8.14](../versions/0.8.14.md) | stages added: 8, 9<br>Dialogue: 3 lines added, 1 line changed<br>· text: “NO! Please not through the gate! I won't go there!” → “NO! Please not to the south! I won't go to those devasted lands!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `stn_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 82, 83, 84, 85, 86, 110, 120, 130, 140, 148, 149, 150, 160, 200, 201, 202, 203, 204, 205, 206, 207, 210, 211, 212, 999 |
    | Dialogue nodes setting stages | 5: `stn_northgate_12`, 6: `stn_horse_30`, 8: `stn_southgate_12`, 9: `odirath_8c`, 11: `stn_gyra_init_52`, 11: `stn_gyra_m11_2_spawn`, 11: `stn_gyra_m11_3_spawn`, 12: `stn_gyra_m12_1_spawn`, 12: `stn_gyra_m12_2_spawn`, 12: `stn_gyra_m12_3_spawn`, 13: `stn_gyra_m13_1_spawn`, 14: `stn_gyra_m14_1_spawn`, 14: `stn_gyra_m14_2_spawn`, 14: `stn_gyra_m14_C_spawn`, 15: `stn_gyra_m15_1_spawn`, 15: `stn_gyra_m15_2_spawn`, 15: `stn_gyra_m15_3_spawn`, 16: `stn_gyra_m16_1_spawn`, 16: `stn_gyra_m16_1b_spawn`, 16: `stn_gyra_m16_2_spawn`, 17: `stn_gyra_m17_1_spawn`, 18: `stn_gyra_m18_1_spawn`, 18: `stn_gyra_m18_2_spawn`, 18: `stn_gyra_m18_3_spawn`, 19: `stn_gyra_m19_1_spawn`, 20: `stn_gyra_m20_1_spawn`, 20: `stn_gyra_m20_2_spawn`, 20: `stn_gyra_m20_3_spawn`, 21: `stn_gyra_m21_1_spawn`, 22: `stn_gyra_m22_1_spawn`, 23: `stn_gyra_m23_1_spawn`, 23: `stn_gyra_m23_1b_spawn`, 23: `stn_gyra_m23_2_spawn`, 24: `stn_gyra_m24_1_spawn`, 24: `stn_gyra_m24_1b_spawn`, 25: `stn_gyra_m25_1_spawn`, 26: `stn_gyra_m26_1_spawn`, 26: `stn_gyra_m26_2_spawn`, 27: `stn_gyra_m27_1_spawn`, 28: `stn_gyra_m28_1_spawn`, 29: `stn_gyra_10`, 31: `stn_gyra_hlm1a_10`, 31: `stn_gyra_hlm1a_found`, 32: `stn_gyra_hlm2a_10`, 32: `stn_gyra_hlm2a_found`, 33: `stn_gyra_hlm3a_10`, 33: `stn_gyra_hlm3a_found`, 41: `stn_gyra_hlm1a_found`, 42: `stn_gyra_hlm2a_found`, 43: `stn_gyra_hlm3a_found`, 44: `berbane_102`, 45: `berbane_140`, 46: `stn_castle_cleared_1`, 47: `stn_castle_cleared_2`, 48: `stoutford_castle_5`, 49: `check_erwyn_3a`, 50: `stn_colonel_34`, 51: `stn_colonel_111`, 82: `rnd_bwm7_0`, 83: `rnd_bwm7_2`, 84: `rnd_bwm7_3`, 85: `rnd_bwm7_4`, 86: `rnd_bwm7_5`, 110: `stn_colonel_80`, 120: `stn_colonel_112`, 120: `stn_colonel_113`, 130: `stn_colonel_122`, 130: `stn_colonel_123`, 140: `stn_colonel_132`, 140: `stn_colonel_133`, 148: `stoutford_castle_3_1`, 150: `stn_colonel_142`, 150: `stn_colonel_143`, 160: `stn_colonel_152`, 160: `stn_colonel_153`, 200: `blornvale_s1_6`, 201: `blornvale_shop1_10`, 202: `blornvale_shop1_6`, 202: `blornvale_s1_4`, 203: `lakecave2_troll_90`, 204: `key_wild21a_10`, 204: `key_wild21a_30`, 205: `caeda_root60_2`, 206: `script_lakecave1_damerilia1_2`, 206: `script_lakecave1_damerilia2_2`, 206: `script_lakecave1_damerilia3_2`, 207: `stoutford_widow_roots30_1_2`, 207: `stoutford_widow_roots30_3_2`, 210: `lakecave2_key_check2_20`, 211: `lakecave2_key_check2_90`, 212: `lakecave2_script_keycheck3a` |
    | Dialogue nodes clearing stages | 210: `lakecave2_key_check2_10`, 201: `blornvale_shop2`, 48: `check_erwyn_1`, 48: `check_erwyn_2`, 48: `check_erwyn_3a`, 48: `check_erwyn_3b`, 48: `check_erwyn_4`, 49: `check_erwyn_3b`, 29: `stn_gyra_42`, 29: `stn_gyra_52` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
