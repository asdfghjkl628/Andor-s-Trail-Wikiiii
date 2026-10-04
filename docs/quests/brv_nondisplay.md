# brv_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 36 |
| **Started by** | stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Churrie](../monsters/churrie.md), [Feygard soldier](../monsters/patrol2_roaming.md), [Feygard soldier](../monsters/patrol_roaming.md), [Feygard soldier](../monsters/patrol2_captain.md), [Gnossath](../monsters/brv_employer.md) +5 |
| **Locations** | [brimhaven1](../maps/brimhaven1.md), [brimhaven4](../maps/brimhaven4.md), [brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md), [brimhaven_house1](../maps/brimhaven_house1.md) |
| **Total XP** | 500 |
| **Related quests** | 7 |

</div>

## Overview

> butcher state

## Prerequisites to start

None: talk to stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Work for debts](brv_employee.md#stage-1) | stage 1 reached, for stage 11 here |
| Requires | [Much water](brv_flood.md#stage-52) | stage 52 reached, for stages 71, 81, 100 here |
| Requires | [Much water](brv_flood.md#stage-70) | stage 70 reached, for stages 71, 81, 100 here |
| Requires | [Much water](brv_flood.md#stage-200) | stage 200 reached, for stages 110, 120 here |
| Requires | [Young merchant](quest_burhczyd.md#stage-80) | stage 80 reached, for stage 142 here |
| Blocked by | [Work for debts](brv_employee.md#stage-90) | stage 90 must NOT be reached, for stage 89 here |
| Blocked by | [Much water](brv_flood.md#stage-54) | stage 54 must NOT be reached, for stages 71, 81, 100 here |
| Blocked by | [Much water](brv_flood.md#stage-70) | stage 70 must NOT be reached, for stages 71, 81, 100 here |
| Blocked by | [Much water](brv_flood.md#stage-80) | stage 80 must NOT be reached, for stages 71, 81, 100 here |
| Blocked by | [bwmfill_nondisplay (hidden flag)](bwmfill_nondisplay.md#stage-41) | stage 41 must NOT be reached, for stage 142 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-100) | stage 100 there needs stage 83 here |
| Unlocks | [Much water](brv_flood.md#stage-100) | stage 100 there needs stage 100 here |
| Unlocks | [Much water](brv_flood.md#stage-110) | stage 110 there needs stage 100 here |
| Unlocks | [Honor your parents](brv_present.md#stage-10) | stage 10 there needs stage 130 here |
| Unlocks | [Honor your parents](brv_present.md#stage-20) | stage 20 there needs stage 130 here |
| Unlocks | [The exploded star](mg2_exploded_star.md#stage-60) | stage 60 there needs stage 144 here |
| Unlocks | [The exploded star](mg2_exploded_star.md#stage-62) | stage 62 there needs stage 144 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | butcher state<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven inn east](../maps/brimhaven_inn_east.md) visibly changes.</span> | stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) | – | – |
| <span id="stage-11"></span>11 | 11=1 Employee is at home | [Gnossath](../monsters/brv_employer.md) ([brimhaven1](../maps/brimhaven1.md)) | – | removes monsters from brimhaven_tavern1<br>removes monsters from brimhaven_employee<br>spawns monsters on brimhaven_employee<br>spawns monsters on brimhaven_tavern1 |
| <span id="stage-21"></span>21 | - Employee Msg 21 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-22"></span>22 | - Employee Msg 22 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-23"></span>23 | - Employee Msg 23 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-70"></span>70 | 70=passage to river closed<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven2](../maps/waytobrimhaven2.md).</span><br><span class="qnote">🔒 An area on [Brimhaven1](../maps/brimhaven1.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Waytobrimhaven2](../maps/waytobrimhaven2.md) becomes blocked off.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md)<br>stepping on a trigger on [waytobrimhaven2](../maps/waytobrimhaven2.md)<br>stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) | stage 83, stage 87 | clears stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89)<br>clears stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87)<br>removes monsters from waytobrimhaven2 |
| <span id="stage-71"></span>71 | 71=Stage-1 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | wearing [Hand Axe](../items/hand_axe.md) | sets stage 54 of [Much water](../quests/brv_flood.md#stage-54)<br>sets stage 56 of [Much water](../quests/brv_flood.md#stage-56)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4<br>sets stage 80 of [Much water](../quests/brv_flood.md#stage-80) |
| <span id="stage-72"></span>72 | 72=stage-2 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 71 | clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81) |
| <span id="stage-73"></span>73 | 73=stage-3 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 72 | clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82) |
| <span id="stage-79"></span>79 | 79=End flood | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-80"></span>80 | 80=Start flood | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-81"></span>81 | 81=Stage-1 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven1](../maps/brimhaven1.md) visibly changes.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | wearing [Hand Axe](../items/hand_axe.md) | sets stage 54 of [Much water](../quests/brv_flood.md#stage-54)<br>sets stage 56 of [Much water](../quests/brv_flood.md#stage-56)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4<br>sets stage 80 of [Much water](../quests/brv_flood.md#stage-80) |
| <span id="stage-82"></span>82 | 82=stage-2 flood<br><span class="qnote">⚡ A scripted event can now trigger on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven1](../maps/brimhaven1.md) visibly changes.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 71 | clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81) |
| <span id="stage-83"></span>83 | 83=stage-3 flood<br><span class="qnote">⚡ A scripted event can now trigger on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Waytobrimhaven2](../maps/waytobrimhaven2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven1](../maps/brimhaven1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Brimhaven4](../maps/brimhaven4.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven2](../maps/waytobrimhaven2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven3](../maps/waytobrimhaven3.md) visibly changes.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md)<br>stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) | stage 72, stage 87 | clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82)<br>clears stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89)<br>clears stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87)<br>removes monsters from waytobrimhaven2 |
| <span id="stage-87"></span>87 | 87=flood pending | [Churrie](../monsters/churrie.md) ([waytobrimhaven2](../maps/waytobrimhaven2.md)) | pay 2,500 gold | – |
| <span id="stage-88"></span>88 | 88=drain pending | [Tamarukh](../monsters/tamarukh.md) ([waytobrimhaven2](../maps/waytobrimhaven2.md)) | pay 2,500 gold | – |
| <span id="stage-89"></span>89 | 89=End flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven1](../maps/brimhaven1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Brimhaven4](../maps/brimhaven4.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven2](../maps/waytobrimhaven2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven3](../maps/waytobrimhaven3.md) visibly changes.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md)<br>stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md), stage 88 | removes monsters from brimhaven_tavern1<br>removes monsters from brimhaven_employee<br>sets stage 90 of [Work for debts](../quests/brv_employee.md#stage-90)<br>changes map brimhaven1<br>spawns monsters on brimhaven_employee<br>spawns monsters on brimhaven_tavern1<br>clears stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83)<br>clears stage 70 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-70)<br>clears stage 88 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-88)<br>removes monsters from waytobrimhaven2 |
| <span id="stage-100"></span>100 | Leaving Brimhaven is forbidden<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span><br><span class="qnote">🔒 An area on [Brimhaven3](../maps/brimhaven3.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Brimhaven4](../maps/brimhaven4.md) becomes blocked off.</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | wearing [Hand Axe](../items/hand_axe.md) | sets stage 54 of [Much water](../quests/brv_flood.md#stage-54)<br>sets stage 56 of [Much water](../quests/brv_flood.md#stage-56)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4<br>sets stage 80 of [Much water](../quests/brv_flood.md#stage-80) |
| <span id="stage-110"></span>110 | Alkapoan told about the captain | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | – | – |
| <span id="stage-120"></span>120 | captain told about burning the letters | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | stage 110 | – |
| <span id="stage-130"></span>130 | showed money to shop owner | [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) | have 1,000 gold | – |
| <span id="stage-138"></span>138 | Tember active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard prison](../maps/remgard_prison.md).</span> | stepping on a trigger on [remgard_prison](../maps/remgard_prison.md) | – | spawns monsters on remgard_prison<br>removes monsters from remgard0<br>changes map remgard0 |
| <span id="stage-139"></span>139 | Feygard patrol wall<br><span class="qnote">🗺️ Part of [Remgard prison](../maps/remgard_prison.md) visibly changes.</span> | [Tember](../monsters/remgard_prison_thief.md) ([remgard_prison](../maps/remgard_prison.md)) | – | – |
| <span id="stage-140"></span>140 | Movement blocked by the Feygard patrol<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span><br><span class="qnote">🔒 An area on [Brimhaven4](../maps/brimhaven4.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Crossroads](../maps/crossroads.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Fields6](../maps/fields6.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Remgard0](../maps/remgard0.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Road1](../maps/road1.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Wild6](../maps/wild6.md) becomes blocked off.</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | – | spawns monsters on the map |
| <span id="stage-141"></span>141 | Has met the Feygard patrol before | [Feygard soldier](../monsters/patrol_roaming.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Feygard soldier](../monsters/patrol2_roaming.md) ([remgard0](../maps/remgard0.md)) | – | clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140)<br>removes monsters from the map<br>changes map remgard0<br>clears stage 138 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-138)<br>clears stage 139 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-139)<br>starts timer “remgard_prison”<br>removes monsters from remgard_prison |
| <span id="stage-142"></span>142 | Confiscated bonemeals<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | – | sets stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40)<br>sets stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41) |
| <span id="stage-143"></span>143 | Never true<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven3](../maps/brimhaven3.md).</span> | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-144"></span>144 | Told fortune teller about andor | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | – | – |
| <span id="stage-145"></span>145 | Fortune teller told about gold behind father's house - brv_fortune_hero_70 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |
| <span id="stage-146"></span>146 | Fortune teller found gold behind father's house<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [crossglen](../maps/crossglen.md) | stage 145 | 500 XP<br>gives 1500× [Gold coins](../items/gold.md) |
| <span id="stage-147"></span>147 | brv_fortune_hero_130 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |
| <span id="stage-148"></span>148 | brv_fortune_hero_30 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |
| <span id="stage-149"></span>149 | brv_fortune_hero_10 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |
| <span id="stage-150"></span>150 | brv_fortune_andor_30 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |
| <span id="stage-151"></span>151 | brv_fortune_andor_10 | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | have 100 gold, stage 144 | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) → the conversation leads here automatically → **stage 1**

???+ note "Stage 11: 1 route"

    1. Talk to [Gnossath](../monsters/brv_employer.md) ([brimhaven1](../maps/brimhaven1.md)) → the conversation leads here automatically — **conditions:** reached stage 1 of [Work for debts](../quests/brv_employee.md#stage-1) → **stage 11**; also removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1. NPC: “I am waiting for Stebbarik. Have you seen him?”

???+ note "Stage 70: 3 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83) → **stage 70**
    2. stepping on a trigger on [waytobrimhaven2](../maps/waytobrimhaven2.md) → the conversation leads here automatically — **conditions:** reached stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83) → **stage 70**
    3. stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87) → **stage 70**; also clears stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89), clears stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87), removes monsters from waytobrimhaven2

???+ note "Stage 71: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Start hacking on the wood.” — **conditions:** NOT reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); NOT reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md) → **stage 71**; also sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through the hole in the dam. A lot of water!”
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); NOT reached stage 80 of [Much water](../quests/brv_flood.md#stage-80) → **stage 71**; also sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”

???+ note "Stage 72: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71); NOT reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72) → **stage 72**; also clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71); NOT reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72) → **stage 72**; also clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)

???+ note "Stage 73: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72); NOT reached stage 73 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-73) → **stage 73**; also clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82)
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72); NOT reached stage 73 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-73) → **stage 73**; also clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82)

???+ note "Stage 81: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Start hacking on the wood.” — **conditions:** NOT reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); NOT reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md) → **stage 81**; also sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through the hole in the dam. A lot of water!”
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); NOT reached stage 80 of [Much water](../quests/brv_flood.md#stage-80) → **stage 81**; also sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”

???+ note "Stage 82: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71); NOT reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72) → **stage 82**; also clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71); NOT reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72) → **stage 82**; also clears stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)

???+ note "Stage 83: 3 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72); NOT reached stage 73 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-73) → **stage 83**; also clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82)
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 72 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-72); NOT reached stage 73 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-73) → **stage 83**; also clears stage 82 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-82)
    3. stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87) → **stage 83**; also clears stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89), clears stage 87 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-87), removes monsters from waytobrimhaven2

???+ note "Stage 87: 1 route"

    1. Talk to [Churrie](../monsters/churrie.md) ([waytobrimhaven2](../maps/waytobrimhaven2.md)) → choose “It should not fail because of a lack of money. Here you have 2,500 gold.” — **conditions:** pay 2,500 gold → **stage 87**. NPC: “Oh, wow! I will take care of it. So much money! Probably tonight ...”

???+ note "Stage 88: 1 route"

    1. Talk to [Tamarukh](../monsters/tamarukh.md) ([waytobrimhaven2](../maps/waytobrimhaven2.md)) → choose “It should not fail because of a lack of money. Here you have 2,500 gold.” — **conditions:** pay 2,500 gold → **stage 88**. NPC: “That is very noble of you. I will take care of it.”

???+ note "Stage 89: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 25; NOT reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90) → **stage 89**; also removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, sets stage 90 of [Work for debts](../quests/brv_employee.md#stage-90), changes map brimhaven1, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1, clears stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83). NPC: “Wow, you got it.”
    2. stepping on a trigger on [waytobrimhaven1](../maps/waytobrimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 88 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-88) → **stage 89**; also clears stage 70 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-70), clears stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83), clears stage 88 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-88), removes monsters from waytobrimhaven2

???+ note "Stage 100: 2 routes"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Start hacking on the wood.” — **conditions:** NOT reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); NOT reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md) → **stage 100**; also sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through the hole in the dam. A lot of water!”
    2. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); NOT reached stage 80 of [Much water](../quests/brv_flood.md#stage-80) → **stage 100**; also sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”

???+ note "Stage 110: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Laugh while you can. The captain is here and now you will get your deserved punishment!” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200) → **stage 110**. NPC: “Let's see who is laughing in the end. The captain came to talk, not arrest me. Now she owns a new horse and I will be…”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “Laugh while you can. The captain is here and now you will get your deserved punishment!” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200) → **stage 110**. NPC: “Let's see who is laughing in the end. The captain came to talk, not arrest me. Now she owns a new horse and I will be…”

???+ note "Stage 120: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 110 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-110) → **stage 120**. NPC: “It seems Alkapoan's letters accidentally fell into a fire and I am sure some unknown evil spies from Loneford…”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 110 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-110) → **stage 120**. NPC: “It seems Alkapoan's letters accidentally fell into a fire and I am sure some unknown evil spies from Loneford…”

???+ note "Stage 130: 1 route"

    1. Talk to [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) → choose “[You slowly pull out your coin bag and show him your gold.]” — **conditions:** have 1,000 gold → **stage 130**. NPC: “[His eyes widen.] Oh I was just kidding, child... I mean... honored customer!”

???+ note "Stage 138: 1 route"

    1. stepping on a trigger on [remgard_prison](../maps/remgard_prison.md) → the conversation leads here automatically — **conditions:** 5 rounds passed since timer “remgard_prison”; NOT reached stage 138 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-138) → **stage 138**; also spawns monsters on remgard_prison, removes monsters from remgard0, changes map remgard0

???+ note "Stage 139: 1 route"

    1. Talk to [Tember](../monsters/remgard_prison_thief.md) ([remgard_prison](../maps/remgard_prison.md)) → choose “What? How can we leave?” → **stage 139**. NPC: “Oh, that is easy. Check the back wall - it is fake. We had it exchanged secretly, and those stupid guards haven't…”

???+ note "Stage 140: 1 route"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** NOT carry 1× [Bonemeal potion](../items/bonemeal_potion.md); NOT carry 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md); NOT carry 1× [Kazaul bonemeal](../items/pot_bm_kazaul.md) → **stage 140**; also spawns monsters on the map. NPC: “Stop in the name of Feygard! [The soldiers approach and search your belongings]”

???+ note "Stage 141: 4 routes"

    1. Talk to [Feygard soldier](../monsters/patrol_roaming.md) ([brimhaven4](../maps/brimhaven4.md)) → the conversation leads here automatically — **conditions:** reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141); NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142) → **stage 141**; also clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map. NPC: “Everything is OK. Stay clean.”
    2. Talk to [Feygard soldier](../monsters/patrol_roaming.md) ([brimhaven4](../maps/brimhaven4.md)) → the conversation leads here automatically — **conditions:** reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141) → **stage 141**; also clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map. NPC: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate…”
    3. Talk to [Feygard soldier](../monsters/patrol2_roaming.md) ([remgard0](../maps/remgard0.md)) → the conversation leads here automatically — **conditions:** reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141); NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142) → **stage 141**; also clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, removes monsters from the map. NPC: “Everything is OK. Stay clean.”
    4. Talk to [Feygard soldier](../monsters/patrol2_roaming.md) ([remgard0](../maps/remgard0.md)) → the conversation leads here automatically — **conditions:** reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141) → **stage 141**; also clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, changes map remgard0, clears stage 138 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-138), clears stage 139 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-139), starts timer “remgard_prison”, removes monsters from remgard_prison. NPC: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate…”

???+ note "Stage 142: 2 routes"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically → **stage 142**
    2. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41); reached stage 80 of [Young merchant](../quests/quest_burhczyd.md#stage-80) → **stage 142**; also sets stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40), sets stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41)

???+ note "Stage 144: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “I am searching...” → **stage 144**. NPC: “I feel that you are on a search... at the beginning of a long and dangerous search for a relative of yours.”

???+ note "Stage 145: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; NOT reached stage 145 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-145) → **stage 145**. NPC: “I see you picking up a lot of coins from a hole in the ground. Can it be behind your father's house?”

???+ note "Stage 146: 1 route"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → choose “Could this be the place? [Start digging with my hands]” — **conditions:** reached stage 145 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-145); NOT reached stage 146 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-146) → **stage 146**; also gives 1500× [Gold coins](../items/gold.md). NPC: “After digging for some time you find a lot of gold coins! You take them and then close the hole.”

???+ note "Stage 147: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; random chance (50%); NOT reached stage 147 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-147) → **stage 147**. NPC: “I see a man pacing up and down in a little house. He seems to be waiting for someone.”

???+ note "Stage 148: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; random chance (33%); NOT reached stage 148 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-148) → **stage 148**. NPC: “I see a thief. He will take something from you.”

???+ note "Stage 149: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; random chance (25%); NOT reached stage 149 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-149) → **stage 149**. NPC: “I see you walking up a path on a mountain. Beware! There is something waiting for you ahead. I see you being attacked…”

???+ note "Stage 150: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; random chance (20%); NOT reached stage 150 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-150) → **stage 150**. NPC: “Your brother is in league with dark forces.”

???+ note "Stage 151: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” — **conditions:** reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144); have 100 gold; NOT 0 rounds passed since timer “brv_fortune”; random chance (17%); NOT reached stage 151 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-151) → **stage 151**. NPC: “I see you talking to your brother, somewhere far from here in a big city. Feygard or Nor City, I think.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 33 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added, 1 line changed<br>· text: “Alkapoan's letters accidently fell into a fire and I am sure some unk…” → “It seems Alkapoan's letters accidentally fell into a fire and I am su…” |
| [v0.7.14](../versions/0.7.14.md) | stages added: 138, 139<br>Dialogue: 7 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “I see you walking up a path on a mountain. Beware! There is something…” → “I see you walking up a path on a mountain. Beware! There is something…” |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines changed<br>· text: “[His eyes widen.] Oh I was just kidding, child... I mean... Sir!” → “[His eyes widen.] Oh I was just kidding, child... I mean... honored c…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 11, 21, 22, 23, 70, 71, 72, 73, 79, 80, 81, 82, 83, 87, 88, 89, 100, 110, 120, 130, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151 |
    | Dialogue nodes setting stages | 1: `brv_butcher_clock_30`, 11: `brv_employer_01`, 70: `brv_flood_key_set1a_10`, 70: `brv_ctrl_flood_10`, 71: `brv_flood_0_10`, 71: `brv_flood_20_10`, 72: `brv_flood_1_10`, 73: `brv_flood_2a_10`, 81: `brv_flood_0_10`, 81: `brv_flood_20_10`, 82: `brv_flood_1_10`, 83: `brv_flood_2a_10`, 83: `brv_ctrl_flood_10`, 87: `churrie_30`, 88: `tamarukh_30`, 89: `brv_employer_put_boulder_90`, 89: `brv_ctrl_flood_20`, 100: `brv_flood_0_10`, 100: `brv_flood_20_10`, 110: `brv_guard_captain_and_rich_man_30`, 120: `brv_guard_captain_and_rich_man_40`, 130: `brv_shop_owner_10`, 138: `remgard_prison_step_10`, 139: `remgard_prison_thief_112`, 140: `brv_patrol_stop_hero`, 140: `brv_patrol2_stop_hero`, 141: `brv_patrol_roaming_100`, 141: `brv_patrol_bonemeals_removed`, 141: `brv_patrol2_roaming_100`, 142: `brv_patrol_remove_all_bonemeals`, 142: `brv_patrol2_remove_all_bonemeals`, 142: `brv_patrol_stop_hero_bur`, 144: `brv_fortune_40`, 145: `brv_fortune_hero_70`, 146: `crossglen_fortune_teller_10`, 147: `brv_fortune_hero_130`, 148: `brv_fortune_hero_30`, 149: `brv_fortune_hero_10`, 150: `brv_fortune_andor_30`, 151: `brv_fortune_andor_10` |
    | Dialogue nodes clearing stages | 11: `brv_employee2`, 83: `brv_employer_put_boulder_90`, 83: `brv_ctrl_flood_20`, 70: `brv_flood_key_set1`, 70: `brv_flood_key_set1a_20`, 70: `brv_ctrl_flood_20`, 70: `brv_flood_key_set3`, 81: `brv_flood_1_10`, 82: `brv_flood_2a_10`, 100: `brv_guard_captain_30` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
