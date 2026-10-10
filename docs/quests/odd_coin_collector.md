---
description: "The odd coin collector is a quest in Andor's Trail, started by Gylew (waterway5). 25 stages, 28,150 XP in total. I traded 5 of my 'mermaid coins' to Gylew for 500 gold."
---

# The odd coin collector

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `odd_coin_collector` |
| **In journal** | Yes |
| **Stages** | 25 (completes at 100, 105, 110, 115) |
| **Started by** | [Gylew](../monsters/gylew.md) ([Waterway 5](../maps/waterway5.md)) |
| **NPCs involved** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), [Forenza](../monsters/forenza.md), [Gylew](../monsters/gylew.md) |
| **Locations** | [Laerothbasement 2](../maps/laerothbasement2.md), [Waterway 5](../maps/waterway5.md), [Waytobrimhaven 3](../maps/waytobrimhaven3.md) |
| **Total XP** | 28,150 |
| **Related quests** | 5 |

</div>

## Overview

> I traded 5 of my 'mermaid coins' to Gylew for 500 gold.

## Prerequisites to start

Start with [Gylew](../monsters/gylew.md) ([Waterway 5](../maps/waterway5.md)). Required:

- NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100)
- NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105)
- NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20)
- reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220)
- have 5 gold
- NOT reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10)
- NOT reached stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11)
- pay 5 gold


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The silver scale](mermaid_scale.md#stage-220) | stage 220 reached, for stages 10, 11 here |
| Requires | [General story flags (hidden flag)](nondisplay.md#stage-47) | stage 47 reached, for stages 100, 105 here |
| Requires | [General story flags 2 (hidden flag)](nondisplay_2.md#stage-250) | stage 250 reached, for stages 12, 13 here |
| Mutually exclusive | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-104) | stage 104 must NOT be reached, for stages 41, 42, 43, 44, 46, 47, 48 here |
| Blocked by | [General story flags 2 (hidden flag)](nondisplay_2.md#stage-170) | stage 170 must NOT be reached, for stage 20 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-183) | stage 183 there needs stage 115 here |
| Unlocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-103) | stage 103 there needs stages 45, 62 here |
| Unlocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-105) | stage 105 there needs stage 40 here |
| Unlocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-106) | stage 106 there needs stage 65 here |
| Unlocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-108) | stage 108 there needs stage 63 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-44) | stage 44 there needs stages 40, 60, 63 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-45) | stage 45 there needs stages 40, 60, 63 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-47) | stage 47 there needs stage 65 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-48) | stage 48 there needs stages 40, 60, 63 here |
| Blocks | [General story flags (hidden flag)](nondisplay.md#stage-44) | reaching stages 60, 62, 100, 105 here closes stage 44 there |
| Blocks | [General story flags (hidden flag)](nondisplay.md#stage-45) | reaching stages 60, 62, 100, 105 here closes stage 45 there |
| Blocks | [General story flags (hidden flag)](nondisplay.md#stage-48) | reaching stages 60, 62, 100, 105 here closes stage 48 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | I traded 5 of my 'mermaid coins' to Gylew for 500 gold. | [Gylew](../monsters/gylew.md) | 500 XP, 500× [Gold coins](../items/gold.md) |
| <span id="stage-11"></span>[11](#route-11) | I foolishly gave 5 of my 'mermaid coins' to Gylew. | [Gylew](../monsters/gylew.md) | 100 XP |
| <span id="stage-12"></span>[12](#route-12) | I sold the 10 coins that I looted from the Arulir secret room to Gylew. | [Gylew](../monsters/gylew.md) | 750 XP, 550× [Gold coins](../items/gold.md) |
| <span id="stage-13"></span>[13](#route-13) | I gave Gylew the 10 coins that I looted from the Arulir secret room. | [Gylew](../monsters/gylew.md) | 950 XP, -10× [Gold coins](../items/gold.md), 1× [Feygard plated gloves](../items/feygard_plated_gloves.md) |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I have agreed to set off to Laeroth Manor in pursuit of the Korhald… ▸</span><span class="l">▴ less</span></summary>I have agreed to set off to Laeroth Manor in pursuit of the Korhald coins and to bring them back to Gylew.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Laerothbasement 1](../maps/laerothbasement1.md).</span> | [Gylew](../monsters/gylew.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">In the Laeroth basement, I noticed a sign on the wall that i could… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I noticed a sign on the wall that i could not read in its entirety, but I was able make out the name 'Korhald'. This makes me wonder if this is a clue?</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 2](../maps/laerothbasement2.md).</span> | stepping on a trigger on [Laerothbasement 2](../maps/laerothbasement2.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">In the Laeroth basement, I discovered and looted the chest… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I discovered and looted the chest containing the 'Korhald coins'.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 2](../maps/laerothbasement2.md).</span><br><span class="qnote">🗺️ Part of [Laerothbasement 2](../maps/laerothbasement2.md) visibly changes.</span> | stepping on a trigger on [Laerothbasement 2](../maps/laerothbasement2.md) | 1,000 XP, spawns monsters on laerothbasement2, 1× [Korhald coin chest](../items/korhald_coins.md), spawns monsters on laerothbasement2 |
| <span id="stage-41"></span>[41](#route-41) | In the Laeroth basement, I encountered an injured man named Forenza. | [Forenza](../monsters/forenza.md) | – |
| <span id="stage-42"></span>[42](#route-42) | I aided Forenza with an ointment for bleeding wounds. | [Forenza](../monsters/forenza.md) | 1,000 XP |
| <span id="stage-43"></span>[43](#route-43) | <details class="jt"><summary><span class="s">In the Laeroth basement, I was able to help out Forenza by giving… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I was able to help out Forenza by giving him a bonemeal potion.</details> | [Forenza](../monsters/forenza.md) | 500 XP |
| <span id="stage-44"></span>[44](#route-44) | <details class="jt"><summary><span class="s">In the Laeroth basement, I was able to help out Forenza by giving… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I was able to help out Forenza by giving him a major health potion.</details> | [Forenza](../monsters/forenza.md) | 250 XP |
| <span id="stage-45"></span>[45](#route-45) | <details class="jt"><summary><span class="s">I have decided to attack Forenza. I should return to Gylew with the… ▸</span><span class="l">▴ less</span></summary>I have decided to attack Forenza. I should return to Gylew with the key once he is dead.</details> | [Forenza](../monsters/forenza.md) | – |
| <span id="stage-46"></span>[46](#route-46) | <details class="jt"><summary><span class="s">In the Laeroth basement, I was able to help out Forenza by giving… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I was able to help out Forenza by giving him a potion of health from Lodar.</details> | [Forenza](../monsters/forenza.md) | 450 XP |
| <span id="stage-47"></span>[47](#route-47) | <details class="jt"><summary><span class="s">In the Laeroth basement, I was able to help out Forenza by giving… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I was able to help out Forenza by giving him a regular health potion.</details> | [Forenza](../monsters/forenza.md) | 100 XP |
| <span id="stage-48"></span>[48](#route-48) | <details class="jt"><summary><span class="s">In the Laeroth basement, I was able to help out Forenza by giving… ▸</span><span class="l">▴ less</span></summary>In the Laeroth basement, I was able to help out Forenza by giving him a minor health potion.</details> | [Forenza](../monsters/forenza.md) | 50 XP |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I've decided to help Forenza by agreeing to get the second key from… ▸</span><span class="l">▴ less</span></summary>I've decided to help Forenza by agreeing to get the second key from Gylew. I should go back to Gylew now. Forenza has left the Manor island and has asked that I meet him outside of Brimhaven after my "business" with Gylew is complete.</details> | [Forenza](../monsters/forenza.md) | removes monsters from laerothbasement2, spawns monsters on waytobrimhaven3 |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">We discovered a mysterious map inside the Korhald chest and I need… ▸</span><span class="l">▴ less</span></summary>We discovered a mysterious map inside the Korhald chest and I need to follow the river going east.</details> | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), [Gylew](../monsters/gylew.md) | 500 XP, 1× [Mysterious Korhald map](../items/korhald_map.md), 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md) |
| <span id="stage-62"></span>[62](#route-62) | <details class="jt"><summary><span class="s">I have decided to attack Gylew. I should return to Forenza with the… ▸</span><span class="l">▴ less</span></summary>I have decided to attack Gylew. I should return to Forenza with the key once he is dead.</details> | [Gylew](../monsters/gylew.md) | – |
| <span id="stage-63"></span>[63](#route-63) | I killed Gylew and should return to Forenza with Gylew's key.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterway 5](../maps/waterway5.md).</span> | stepping on a trigger on [Waterway 5](../maps/waterway5.md) | – |
| <span id="stage-65"></span>[65](#route-65) | <details class="jt"><summary><span class="s">Inside the Korhald cave, I found the Coin of Prestige and the Shield… ▸</span><span class="l">▴ less</span></summary>Inside the Korhald cave, I found the Coin of Prestige and the Shield of the Brave. I should return to Forenza and show him the coin.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Korhald cave hidden](../maps/korhald_cave_hidden.md).</span> | stepping on a trigger on [Korhald cave hidden](../maps/korhald_cave_hidden.md) | – |
| <span id="stage-66"></span>[66](#route-66) | <details class="jt"><summary><span class="s">Inside the Korhald cave, I found the Coin of Prestige and the Shield… ▸</span><span class="l">▴ less</span></summary>Inside the Korhald cave, I found the Coin of Prestige and the Shield of the Brave. I should return to Gylew and show him the coin.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Korhald cave hidden](../maps/korhald_cave_hidden.md).</span> | stepping on a trigger on [Korhald cave hidden](../maps/korhald_cave_hidden.md) | – |
| <span id="stage-100"></span>[100](#route-100) | I sold Gylew the Coin of Prestige and he rewarded me handsomely for it. **(ends quest)** | [Gylew](../monsters/gylew.md) | 5,000 XP, [Gold coins](../items/gold.md) |
| <span id="stage-105"></span>[105](#route-105) | <details class="jt"><summary><span class="s">I gave Gylew the Coin of Prestige and he told me that if I ever make… ▸</span><span class="l">▴ less</span></summary>I gave Gylew the Coin of Prestige and he told me that if I ever make my way to Feygrad, to seek out his family and they will 'make that shield a little bit better". Whatever that means.</details> **(ends quest)** | [Gylew](../monsters/gylew.md) | 6,000 XP |
| <span id="stage-110"></span>[110](#route-110) | I sold Forenza the Coin of Prestige and he rewarded me handsomely for it. **(ends quest)** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) | 5,000 XP, [Gold coins](../items/gold.md) |
| <span id="stage-115"></span>[115](#route-115) | <details class="jt"><summary><span class="s">I gave Forenza the Coin of Prestige and he told me that if I ever… ▸</span><span class="l">▴ less</span></summary>I gave Forenza the Coin of Prestige and he told me that if I ever make my way to Brightport, to seek out his family and they will 'reward" me. Whatever that means.</details> **(ends quest)** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) | 6,000 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “OK. What do you have of value?”

    - **Needs:** not yet stage 10, 11, 20, 100, 105; reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220); have 5 gold; pay 5 gold
    - **Gives:** 500× [Gold coins](../items/gold.md)
    - *“Here is 500 gold.”*


<span id="route-11"></span>

??? note "Stage 11 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Here, take it.”

    - **Needs:** not yet stage 10, 11, 20, 100, 105; reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220); have 5 gold; pay 5 gold
    - *“That was foolish of you. This is very valuable and you just gave it to me.”*


<span id="route-12"></span>

??? note "Stage 12 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “OK. What do you have of value?”

    - **Needs:** not yet stage 12, 13, 20, 100, 105; reached stage 250 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-250); have 10 gold; pay 10 gold
    - **Gives:** 550× [Gold coins](../items/gold.md)
    - *“Here is 550 gold”*


<span id="route-13"></span>

??? note "Stage 13 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Here, take it.”

    - **Needs:** not yet stage 12, 13, 20, 100, 105; reached stage 250 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-250); have 10 gold
    - **Gives:** -10× [Gold coins](../items/gold.md), 1× [Feygard plated gloves](../items/feygard_plated_gloves.md)
    - *“Much appreciated. Thank you.”*


<span id="route-20"></span>

??? note "Stage 20 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Yes, of course, you need my help.”

    - **Needs:** stage 10; not yet stage 20, 100, 105; not reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170)
    - *“Then please head to the east and return to me when you find the Korhald coins.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on laerothbasement2 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 2](../maps/laerothbasement2.md), choose “Oops, that's really going to cost me.”

    - **Needs:** not yet stage 30
    - *“As you approach the crates, you notice an almost illegible sign hanging on the wall. Upon further examination, you can make out the word…”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on laerothbasement2 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 2](../maps/laerothbasement2.md), choose “[Examine the crate.]”

    - **Needs:** stage 30; not yet stage 40
    - **Gives:** spawns monsters on laerothbasement2, 1× [Korhald coin chest](../items/korhald_coins.md), spawns monsters on laerothbasement2
    - *“You pull out a small, richly covered box.”*


<span id="route-41"></span>

??? note "Stage 41 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “What kind of help?”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)
    - *“Seriously?! Can't you see that I am bleeding and weak?”*


<span id="route-42"></span>

??? note "Stage 42 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “Well, I have this ointment for stopping wounds. Take it.”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“Oh, that's wonderful. Thank you.”*


<span id="route-43"></span>

??? note "Stage 43 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “Well I have a bonemeal potion. It's yours now. Take it.”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Bonemeal potion](../items/bonemeal_potion.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“Oh, this stuff is great!”*


<span id="route-44"></span>

??? note "Stage 44 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “Here, take it. It's a really strong potion of healing.”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Major potion of health](../items/health_major2.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“This stuff tastes nasty, but I swear I can feel it helping already.”*


<span id="route-45"></span>

??? note "Stage 45 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “Gylew is the rightful owner of his father's estate and that key belongs to the estate.”

    - **Needs:** not yet stage 45
    - *“What are you going to do about it?”*


<span id="route-46"></span>

??? note "Stage 46 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “I have this really special potion of healing that I got from a very wise old man. Take it!”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“Oh, now this stuff feels like its healing power will last just a little bit longer.”*


<span id="route-47"></span>

??? note "Stage 47 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “I have an ordinary potion of health for you. Take it!”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Regular potion of health](../items/health.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“Oh, this should help. Thank you.”*


<span id="route-48"></span>

??? note "Stage 48 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “I have an little health potion for you. It's all I have. Take it!”

    - **Needs:** not reached stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Minor potion of health](../items/health_minor2.md)
    - <small>Also: sets stage 104 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-104)</small>
    - *“Oh, this should help. I guess.”*


<span id="route-50"></span>

??? note "Stage 50 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md), choose “Yes.”

    - **Needs:** not yet stage 45
    - **Gives:** removes monsters from laerothbasement2, spawns monsters on waytobrimhaven3
    - *“Great. Go to Gylew and get his key. Then bring it and the chest to me. I will meet you outside of Brimhaven.”*


<span id="route-60"></span>

??? note "Stage 60 · Forenza, Gylew · 2 ways"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), choose “Yeah, I can see what you mean.”

    - **Needs:** not yet stage 60; latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) is 63; hand over 1× [Gylew's key](../items/gylew_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md)
    - **Gives:** 1× [Mysterious Korhald map](../items/korhald_map.md), 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md)
    - <small>Also: sets stage 44 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-48)</small>
    - *“Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.”*

    **Way 2:** Talk to [Gylew](../monsters/gylew.md), choose “Yeah, I can see what you mean.”

    - **Needs:** stage 40; not yet stage 62, 100, 105; carry 1× [Korhald coin chest](../items/korhald_coins.md); carry 1× [Forenza's key](../items/forenza_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md); hand over 1× [Forenza's key](../items/forenza_key.md)
    - **Gives:** 1× [Mysterious Korhald map](../items/korhald_map.md), 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md)
    - <small>Also: sets stage 44 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-48)</small>
    - *“Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.”*


<span id="route-62"></span>

??? note "Stage 62 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Yes, I found the Korhald coins, but you are not getting them...[Attack]”

    - **Needs:** stage 40, 50; not yet stage 100, 105
    - *“What? Why?”*


<span id="route-63"></span>

??? note "Stage 63 · stepping on a trigger on waterway5 · 1 way"

    **Way 1:** Stepping on a trigger on [Waterway 5](../maps/waterway5.md)

    - **Needs:** not yet stage 63; killed 1× [Gylew](../monsters/gylew.md)
    - *“You've killed the defenseless coin collector.”*


<span id="route-65"></span>

??? note "Stage 65 · stepping on a trigger on korhald_cave_hidden · 1 way"

    **Way 1:** Stepping on a trigger on [Korhald cave hidden](../maps/korhald_cave_hidden.md)

    - **Needs:** stage 62; not yet stage 65; carry 1× [Coin of Prestige](../items/hero_coin.md)
    - <small>Also: sets stage 103 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-103)</small>
    - *“you have just found a coin and a shield. You should bring this coin back to Forenza.”*


<span id="route-66"></span>

??? note "Stage 66 · stepping on a trigger on korhald_cave_hidden · 1 way"

    **Way 1:** Stepping on a trigger on [Korhald cave hidden](../maps/korhald_cave_hidden.md)

    - **Needs:** stage 45; not yet stage 66; carry 1× [Coin of Prestige](../items/hero_coin.md)
    - <small>Also: sets stage 103 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-103)</small>
    - *“you have just found a coin and a shield. You should bring this coin back to Gylew.”*


<span id="route-100"></span>

??? note "Stage 100 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Sounds like a great deal. I'll take it.”

    - **Needs:** reached stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md)
    - **Gives:** [Gold coins](../items/gold.md)
    - <small>Also: clears stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)</small>
    - *“Excellent. Come see me if you ever find any more interesting coins.”*


<span id="route-105"></span>

??? note "Stage 105 · Gylew · 1 way"

    **Way 1:** Talk to [Gylew](../monsters/gylew.md), choose “Here, take it. I have enough coins.”

    - **Needs:** reached stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md)
    - <small>Also: clears stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)</small>
    - *“Oh, you are so kind. I'll tell you what. Once you find your way to Feygard, seek out my family. They will help you make that shield a…”*


<span id="route-110"></span>

??? note "Stage 110 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), choose “Sounds like a great deal. I'll take it.”

    - **Needs:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md)
    - **Gives:** [Gold coins](../items/gold.md)
    - <small>Also: clears stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)</small>
    - *“Excellent. Come see me if you ever find any more interesting coins.”*


<span id="route-115"></span>

??? note "Stage 115 · Forenza · 1 way"

    **Way 1:** Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), choose “Here, take it. I have enough coins.”

    - **Needs:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md)
    - <small>Also: clears stage 47 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-106)</small>
    - *“Oh, how very generous of you to just hand it over for free. I'll tell you what, once you find your way to Brightport, seek out my family.…”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 25 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 3 lines changed<br>· text: “Oh, how very generous of you to just hand it over for free. I'll tell…” → “Oh, how very generous of you to just hand it over for free. I'll tell…” |
| [v0.8.13](../versions/0.8.13.md) | Stage 12 journal text changed<br>Stage 20 journal text changed<br>Stage 30 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odd_coin_collector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odd_coin_collector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odd_coin_collector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odd_coin_collector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odd_coin_collector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `odd_coin_collector` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 12, 13, 20, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 60, 62, 63, 65, 66, 100, 105, 110, 115 |
    | Dialogue nodes setting stages | 10: `gylew7a_2`, 11: `gylew7a_3`, 12: `gylew8a_3`, 13: `gylew8a_4`, 20: `gylew13`, 30: `laerothbasement2_korhald_sign_30`, 40: `laerothbasement2_chest_examine_50`, 41: `forenza_island_injured_explained`, 42: `forenza_island_injured_ointment`, 43: `forenza_island_injured_help_bm`, 44: `forenza_island_injured_help_mph`, 45: `forenza_island_170_attack`, 46: `forenza_island_injured_help_lph`, 47: `forenza_island_injured_help_rph`, 48: `forenza_island_injured_help_minor_ph`, 50: `forenza_island_180`, 60: `korhald_chest_examine_50`, 62: `gylew_attack`, 63: `gylew_defeated_5`, 65: `korhald_cave_hidden_basket_examine_loot_f2`, 66: `korhald_cave_hidden_basket_examine_loot_g2`, 100: `gylew_korhald_cop_50`, 105: `gylew_korhald_cop_35`, 110: `forenza_korhald_cop_50`, 115: `forenza_korhald_cop_35` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
