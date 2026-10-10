---
description: "Brimhaven story flags is a hidden quest in Andor's Trail, started by stepping on a trigger on brimhaven_inn_east. 36 stages, 500 XP in total. butcher state"
---

# Brimhaven story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 36 |
| **Started by** | stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Churrie](../monsters/churrie.md), [Feygard soldier](../monsters/patrol_roaming.md#v-patrol2_roaming), [Feygard soldier](../monsters/patrol_roaming.md#v-patrol2_captain), [Feygard soldier](../monsters/patrol_roaming.md), [Gnossath](../monsters/brv_employer.md) +5 |
| **Locations** | [Brimhaven 1](../maps/brimhaven1.md), [Brimhaven 4](../maps/brimhaven4.md), [Brimhaven fortune teller](../maps/brimhaven_fortune_teller.md), [Brimhaven house 1](../maps/brimhaven_house1.md) |
| **Total XP** | 500 |
| **Related quests** | 7 |

</div>

## Overview

> butcher state

## Prerequisites to start

None: talk to stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) to begin.


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
| Blocked by | [Blackwater Mountain story flags (hidden flag)](bwmfill_nondisplay.md#stage-41) | stage 41 must NOT be reached, for stage 142 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-100) | stage 100 there needs stage 83 here |
| Unlocks | [Much water](brv_flood.md#stage-100) | stage 100 there needs stage 100 here |
| Unlocks | [Much water](brv_flood.md#stage-110) | stage 110 there needs stage 100 here |
| Unlocks | [Honor your parents](brv_present.md#stage-10) | stage 10 there needs stage 130 here |
| Unlocks | [Honor your parents](brv_present.md#stage-20) | stage 20 there needs stage 130 here |
| Unlocks | [The exploded star](mg2_exploded_star.md#stage-60) | stage 60 there needs stage 144 here |
| Unlocks | [The exploded star](mg2_exploded_star.md#stage-62) | stage 62 there needs stage 144 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | butcher state<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven inn east](../maps/brimhaven_inn_east.md) visibly changes.</span> | stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – |
| <span id="stage-11"></span>[11](#route-11) | 11=1 Employee is at home | [Gnossath](../monsters/brv_employer.md) | removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1 |
| <span id="stage-21"></span>21 | - Employee Msg 21 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-22"></span>22 | - Employee Msg 22 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-23"></span>23 | - Employee Msg 23 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-70"></span>[70](#route-70) | 70=passage to river closed<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 2](../maps/waytobrimhaven2.md).</span><br><span class="qnote">🔒 An area on [Brimhaven 1](../maps/brimhaven1.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Waytobrimhaven 2](../maps/waytobrimhaven2.md) becomes blocked off.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), stepping on a trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md) +1 | varies by route (see below) |
| <span id="stage-71"></span>[71](#route-71) | 71=Stage-1 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | varies by route (see below) |
| <span id="stage-72"></span>[72](#route-72) | 72=stage-2 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-73"></span>[73](#route-73) | 73=stage-3 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-79"></span>79 | 79=End flood | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-80"></span>80 | 80=Start flood | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-81"></span>[81](#route-81) | 81=Stage-1 flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven 1](../maps/brimhaven1.md) visibly changes.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | varies by route (see below) |
| <span id="stage-82"></span>[82](#route-82) | 82=stage-2 flood<br><span class="qnote">⚡ A scripted event can now trigger on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven 1](../maps/brimhaven1.md) visibly changes.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-83"></span>[83](#route-83) | 83=stage-3 flood<br><span class="qnote">⚡ A scripted event can now trigger on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven 1](../maps/brimhaven1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Brimhaven 4](../maps/brimhaven4.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven 2](../maps/waytobrimhaven2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven 3](../maps/waytobrimhaven3.md) visibly changes.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | varies by route (see below) |
| <span id="stage-87"></span>[87](#route-87) | 87=flood pending | [Churrie](../monsters/churrie.md) | – |
| <span id="stage-88"></span>[88](#route-88) | 88=drain pending | [Tamarukh](../monsters/tamarukh.md) | – |
| <span id="stage-89"></span>[89](#route-89) | 89=End flood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 1](../maps/waytobrimhaven1.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven 1](../maps/brimhaven1.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Brimhaven 4](../maps/brimhaven4.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven 2](../maps/waytobrimhaven2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Waytobrimhaven 3](../maps/waytobrimhaven3.md) visibly changes.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | varies by route (see below) |
| <span id="stage-100"></span>[100](#route-100) | Leaving Brimhaven is forbidden<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span><br><span class="qnote">🔒 An area on [Brimhaven 3](../maps/brimhaven3.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Brimhaven 4](../maps/brimhaven4.md) becomes blocked off.</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | varies by route (see below) |
| <span id="stage-110"></span>[110](#route-110) | Alkapoan told about the captain | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-120"></span>[120](#route-120) | captain told about burning the letters | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-130"></span>[130](#route-130) | showed money to shop owner | [Shop Owner](../monsters/brv_shop_owner.md) | – |
| <span id="stage-138"></span>[138](#route-138) | Tember active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard prison](../maps/remgard_prison.md).</span> | stepping on a trigger on [Remgard prison](../maps/remgard_prison.md) | spawns monsters on remgard_prison, removes monsters from remgard0, changes map remgard0 |
| <span id="stage-139"></span>[139](#route-139) | Feygard patrol wall<br><span class="qnote">🗺️ Part of [Remgard prison](../maps/remgard_prison.md) visibly changes.</span> | [Tember](../monsters/remgard_prison_thief.md) | – |
| <span id="stage-140"></span>[140](#route-140) | Movement blocked by the Feygard patrol<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields 6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard 0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road 1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild 6](../maps/wild6.md).</span><br><span class="qnote">🔒 An area on [Brimhaven 4](../maps/brimhaven4.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Crossroads](../maps/crossroads.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Fields 6](../maps/fields6.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Remgard 0](../maps/remgard0.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Road 1](../maps/road1.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md) becomes blocked off.</span><br><span class="qnote">🔒 An area on [Wild 6](../maps/wild6.md) becomes blocked off.</span> | stepping on a trigger on [Brimhaven 4](../maps/brimhaven4.md) | spawns monsters on the map |
| <span id="stage-141"></span>[141](#route-141) | Has met the Feygard patrol before | [Feygard soldier](../monsters/patrol_roaming.md), [Feygard soldier](../monsters/patrol_roaming.md#v-patrol2_roaming) | varies by route (see below) |
| <span id="stage-142"></span>[142](#route-142) | Confiscated bonemeals<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields 6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard 0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road 1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild 6](../maps/wild6.md).</span> | stepping on a trigger on [Brimhaven 4](../maps/brimhaven4.md) | – |
| <span id="stage-143"></span>143 | Never true<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven 3](../maps/brimhaven3.md).</span> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-144"></span>[144](#route-144) | Told fortune teller about andor | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-145"></span>[145](#route-145) | Fortune teller told about gold behind father's house - brv_fortune_hero_70 | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-146"></span>[146](#route-146) | Fortune teller found gold behind father's house<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [Crossglen](../maps/crossglen.md) | 500 XP, 1500× [Gold coins](../items/gold.md) |
| <span id="stage-147"></span>[147](#route-147) | brv_fortune_hero_130 | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-148"></span>[148](#route-148) | brv_fortune_hero_30 | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-149"></span>[149](#route-149) | brv_fortune_hero_10 | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-150"></span>[150](#route-150) | brv_fortune_andor_30 | [Pangitain](../monsters/brv_fortune_teller.md) | – |
| <span id="stage-151"></span>[151](#route-151) | brv_fortune_andor_10 | [Pangitain](../monsters/brv_fortune_teller.md) | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · stepping on a trigger on brimhaven_inn_east · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)



<span id="route-11"></span>

??? note "Stage 11 · Gnossath · 1 way"

    **Way 1:** Talk to [Gnossath](../monsters/brv_employer.md), automatic

    - **Needs:** reached stage 1 of [Work for debts](../quests/brv_employee.md#stage-1)
    - **Gives:** removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1
    - *“I am waiting for Stebbarik. Have you seen him?”*


<span id="route-70"></span>

??? note "Stage 70 · stepping on a trigger on brimhaven1, stepping on a trigger o · 3 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 83

    **Way 2:** Stepping on a trigger on [Waytobrimhaven 2](../maps/waytobrimhaven2.md)

    - **Needs:** stage 83

    **Way 3:** Stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md)

    - **Needs:** stage 87
    - **Gives:** removes monsters from waytobrimhaven2
    - <small>Also: clears stage 89 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-89), clears stage 87 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-87)</small>


<span id="route-71"></span>

??? note "Stage 71 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Start hacking on the wood.”

    - **Needs:** not reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); not reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md)
    - **Gives:** sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through the hole in the dam. A lot of water!”*

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); not reached stage 80 of [Much water](../quests/brv_flood.md#stage-80)
    - **Gives:** sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”*


<span id="route-72"></span>

??? note "Stage 72 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 71; not yet stage 72
    - <small>Also: clears stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81)</small>

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 71; not yet stage 72
    - <small>Also: clears stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81)</small>


<span id="route-73"></span>

??? note "Stage 73 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 72; not yet stage 73
    - <small>Also: clears stage 82 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-82)</small>

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 72; not yet stage 73
    - <small>Also: clears stage 82 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-82)</small>


<span id="route-81"></span>

??? note "Stage 81 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Start hacking on the wood.”

    - **Needs:** not reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); not reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md)
    - **Gives:** sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through the hole in the dam. A lot of water!”*

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); not reached stage 80 of [Much water](../quests/brv_flood.md#stage-80)
    - **Gives:** sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”*


<span id="route-82"></span>

??? note "Stage 82 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 71; not yet stage 72
    - <small>Also: clears stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81)</small>

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 71; not yet stage 72
    - <small>Also: clears stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81)</small>


<span id="route-83"></span>

??? note "Stage 83 · stepping on a trigger on brimhaven1, stepping on a trigger o · 3 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 72; not yet stage 73
    - <small>Also: clears stage 82 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-82)</small>

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 72; not yet stage 73
    - <small>Also: clears stage 82 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-82)</small>

    **Way 3:** Stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md)

    - **Needs:** stage 87
    - **Gives:** removes monsters from waytobrimhaven2
    - <small>Also: clears stage 89 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-89), clears stage 87 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-87)</small>


<span id="route-87"></span>

??? note "Stage 87 · Churrie · 1 way"

    **Way 1:** Talk to [Churrie](../monsters/churrie.md), choose “It should not fail because of a lack of money. Here you have 2,500 gold.”

    - **Needs:** pay 2,500 gold
    - *“Oh, wow! I will take care of it. So much money! Probably tonight ...”*


<span id="route-88"></span>

??? note "Stage 88 · Tamarukh · 1 way"

    **Way 1:** Talk to [Tamarukh](../monsters/tamarukh.md), choose “It should not fail because of a lack of money. Here you have 2,500 gold.”

    - **Needs:** pay 2,500 gold
    - *“That is very noble of you. I will take care of it.”*


<span id="route-89"></span>

??? note "Stage 89 · stepping on a trigger on brimhaven1, stepping on a trigger o · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 25; not reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90)
    - **Gives:** removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, sets stage 90 of [Work for debts](../quests/brv_employee.md#stage-90), changes map brimhaven1, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1
    - <small>Also: clears stage 83 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-83)</small>
    - *“Wow, you got it.”*

    **Way 2:** Stepping on a trigger on [Waytobrimhaven 1](../maps/waytobrimhaven1.md)

    - **Needs:** stage 88
    - **Gives:** removes monsters from waytobrimhaven2
    - <small>Also: clears stage 70 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-70), clears stage 83 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-83), clears stage 88 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-88)</small>


<span id="route-100"></span>

??? note "Stage 100 · stepping on a trigger on brimhaven1 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Start hacking on the wood.”

    - **Needs:** not reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); not reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md)
    - **Gives:** sets stage 54 of [Much water](../quests/brv_flood.md#stage-54), sets stage 56 of [Much water](../quests/brv_flood.md#stage-56), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through the hole in the dam. A lot of water!”*

    **Way 2:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); not reached stage 80 of [Much water](../quests/brv_flood.md#stage-80)
    - **Gives:** sets stage 80 of [Much water](../quests/brv_flood.md#stage-80), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - *“Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”*


<span id="route-110"></span>

??? note "Stage 110 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “Laugh while you can. The captain is here and now you will get your deserved punishment!”

    - **Needs:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200)
    - *“Let's see who is laughing in the end. The captain came to talk, not arrest me. Now she owns a new horse and I will be earning a lot of…”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “Laugh while you can. The captain is here and now you will get your deserved punishment!”

    - **Needs:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200)
    - *“Let's see who is laughing in the end. The captain came to talk, not arrest me. Now she owns a new horse and I will be earning a lot of…”*


<span id="route-120"></span>

??? note "Stage 120 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), automatic

    - **Needs:** stage 110; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200)
    - *“It seems Alkapoan's letters accidentally fell into a fire and I am sure some unknown evil spies from Loneford destroyed the dam. You…”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), automatic

    - **Needs:** stage 110; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200)
    - *“It seems Alkapoan's letters accidentally fell into a fire and I am sure some unknown evil spies from Loneford destroyed the dam. You…”*


<span id="route-130"></span>

??? note "Stage 130 · Shop Owner · 1 way"

    **Way 1:** Talk to [Shop Owner](../monsters/brv_shop_owner.md), choose “[You slowly pull out your coin bag and show him your gold.]”

    - **Needs:** have 1,000 gold
    - *“[His eyes widen.] Oh I was just kidding, child... I mean... honored customer!”*


<span id="route-138"></span>

??? note "Stage 138 · stepping on a trigger on remgard_prison · 1 way"

    **Way 1:** Stepping on a trigger on [Remgard prison](../maps/remgard_prison.md)

    - **Needs:** not yet stage 138; 5 rounds passed since timer “remgard_prison”
    - **Gives:** spawns monsters on remgard_prison, removes monsters from remgard0, changes map remgard0


<span id="route-139"></span>

??? note "Stage 139 · Tember · 1 way"

    **Way 1:** Talk to [Tember](../monsters/remgard_prison_thief.md), choose “What? How can we leave?”

    - *“Oh, that is easy. Check the back wall - it is fake. We had it exchanged secretly, and those stupid guards haven't found out yet.”*


<span id="route-140"></span>

??? note "Stage 140 · stepping on a trigger on brimhaven4 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 4](../maps/brimhaven4.md)

    - **Needs:** not carry 1× [Bonemeal potion](../items/bonemeal_potion.md); not carry 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md); not carry 1× [Kazaul bonemeal](../items/pot_bm_kazaul.md)
    - **Gives:** spawns monsters on the map
    - *“Stop in the name of Feygard! [The soldiers approach and search your belongings]”*


<span id="route-141"></span>

??? note "Stage 141 · Feygard soldier · 4 ways"

    **Way 1:** Talk to [Feygard soldier](../monsters/patrol_roaming.md), automatic

    - **Needs:** stage 141; not yet stage 142
    - **Gives:** removes monsters from the map
    - <small>Also: clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140)</small>
    - *“Everything is OK. Stay clean.”*

    **Way 2:** Talk to [Feygard soldier](../monsters/patrol_roaming.md), automatic

    - **Needs:** stage 141
    - **Gives:** removes monsters from the map
    - <small>Also: clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140)</small>
    - *“What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you…”*

    **Way 3:** Talk to [Feygard soldier](../monsters/patrol_roaming.md#v-patrol2_roaming), automatic

    - **Needs:** stage 141; not yet stage 142
    - **Gives:** removes monsters from the map, removes monsters from the map
    - <small>Also: clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140)</small>
    - *“Everything is OK. Stay clean.”*

    **Way 4:** Talk to [Feygard soldier](../monsters/patrol_roaming.md#v-patrol2_roaming), automatic

    - **Needs:** stage 141
    - **Gives:** removes monsters from the map, changes map remgard0, removes monsters from remgard_prison
    - <small>Also: clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140), clears stage 138 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-138), clears stage 139 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-139), starts timer “remgard_prison”</small>
    - *“What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you…”*


<span id="route-142"></span>

??? note "Stage 142 · stepping on a trigger on brimhaven4 · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven 4](../maps/brimhaven4.md)


    **Way 2:** Stepping on a trigger on [Brimhaven 4](../maps/brimhaven4.md)

    - **Needs:** not reached stage 41 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41); reached stage 80 of [Young merchant](../quests/quest_burhczyd.md#stage-80)
    - <small>Also: sets stage 40 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40), sets stage 41 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41)</small>


<span id="route-144"></span>

??? note "Stage 144 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “I am searching...”

    - *“I feel that you are on a search... at the beginning of a long and dangerous search for a relative of yours.”*


<span id="route-145"></span>

??? note "Stage 145 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 145; have 100 gold; not 0 rounds passed since timer “brv_fortune”
    - *“I see you picking up a lot of coins from a hole in the ground. Can it be behind your father's house?”*


<span id="route-146"></span>

??? note "Stage 146 · stepping on a trigger on crossglen · 1 way"

    **Way 1:** Stepping on a trigger on [Crossglen](../maps/crossglen.md), choose “Could this be the place? [Start digging with my hands]”

    - **Needs:** stage 145; not yet stage 146
    - **Gives:** 1500× [Gold coins](../items/gold.md)
    - *“After digging for some time you find a lot of gold coins! You take them and then close the hole.”*


<span id="route-147"></span>

??? note "Stage 147 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 147; have 100 gold; not 0 rounds passed since timer “brv_fortune”; random chance (50%)
    - *“I see a man pacing up and down in a little house. He seems to be waiting for someone.”*


<span id="route-148"></span>

??? note "Stage 148 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 148; have 100 gold; not 0 rounds passed since timer “brv_fortune”; random chance (33%)
    - *“I see a thief. He will take something from you.”*


<span id="route-149"></span>

??? note "Stage 149 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 149; have 100 gold; not 0 rounds passed since timer “brv_fortune”; random chance (25%)
    - *“I see you walking up a path on a mountain. Beware! There is something waiting for you ahead. I see you being attacked by monsters and they…”*


<span id="route-150"></span>

??? note "Stage 150 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 150; have 100 gold; not 0 rounds passed since timer “brv_fortune”; random chance (20%)
    - *“Your brother is in league with dark forces.”*


<span id="route-151"></span>

??? note "Stage 151 · Pangitain · 1 way"

    **Way 1:** Talk to [Pangitain](../monsters/brv_fortune_teller.md), choose “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]”

    - **Needs:** stage 144; not yet stage 151; have 100 gold; not 0 rounds passed since timer “brv_fortune”; random chance (17%)
    - *“I see you talking to your brother, somewhere far from here in a big city. Feygard or Nor City, I think.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 33 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added, 1 line changed<br>· text: “Alkapoan's letters accidently fell into a fire and I am sure some unk…” → “It seems Alkapoan's letters accidentally fell into a fire and I am su…” |
| [v0.7.14](../versions/0.7.14.md) | Stages added: 138, 139<br>Dialogue: 7 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “I see you walking up a path on a mountain. Beware! There is something…” → “I see you walking up a path on a mountain. Beware! There is something…” |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines changed<br>· text: “[His eyes widen.] Oh I was just kidding, child... I mean... Sir!” → “[His eyes widen.] Oh I was just kidding, child... I mean... honored c…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_nondisplay` |
    | Name in game data | `brv_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 11, 21, 22, 23, 70, 71, 72, 73, 79, 80, 81, 82, 83, 87, 88, 89, 100, 110, 120, 130, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151 |
    | Dialogue nodes setting stages | 1: `brv_butcher_clock_30`, 11: `brv_employer_01`, 70: `brv_flood_key_set1a_10`, 70: `brv_ctrl_flood_10`, 71: `brv_flood_0_10`, 71: `brv_flood_20_10`, 72: `brv_flood_1_10`, 73: `brv_flood_2a_10`, 81: `brv_flood_0_10`, 81: `brv_flood_20_10`, 82: `brv_flood_1_10`, 83: `brv_flood_2a_10`, 83: `brv_ctrl_flood_10`, 87: `churrie_30`, 88: `tamarukh_30`, 89: `brv_employer_put_boulder_90`, 89: `brv_ctrl_flood_20`, 100: `brv_flood_0_10`, 100: `brv_flood_20_10`, 110: `brv_guard_captain_and_rich_man_30`, 120: `brv_guard_captain_and_rich_man_40`, 130: `brv_shop_owner_10`, 138: `remgard_prison_step_10`, 139: `remgard_prison_thief_112`, 140: `brv_patrol_stop_hero`, 140: `brv_patrol2_stop_hero`, 141: `brv_patrol_roaming_100`, 141: `brv_patrol_bonemeals_removed`, 141: `brv_patrol2_roaming_100`, 142: `brv_patrol_remove_all_bonemeals`, 142: `brv_patrol2_remove_all_bonemeals`, 142: `brv_patrol_stop_hero_bur`, 144: `brv_fortune_40`, 145: `brv_fortune_hero_70`, 146: `crossglen_fortune_teller_10`, 147: `brv_fortune_hero_130`, 148: `brv_fortune_hero_30`, 149: `brv_fortune_hero_10`, 150: `brv_fortune_andor_30`, 151: `brv_fortune_andor_10` |
    | Dialogue nodes clearing stages | 11: `brv_employee2`, 83: `brv_employer_put_boulder_90`, 83: `brv_ctrl_flood_20`, 70: `brv_flood_key_set1`, 70: `brv_flood_key_set1a_20`, 70: `brv_ctrl_flood_20`, 70: `brv_flood_key_set3`, 81: `brv_flood_1_10`, 82: `brv_flood_2a_10`, 100: `brv_guard_captain_30` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
