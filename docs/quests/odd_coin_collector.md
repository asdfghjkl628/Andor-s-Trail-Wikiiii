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
| **Started by** | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) |
| **NPCs involved** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3), [Forenza](../monsters/forenza.md), [Gylew](../monsters/gylew.md) |
| **Locations** | [laerothbasement2](../maps/laerothbasement2.md), [waterway5](../maps/waterway5.md), [waytobrimhaven3](../maps/waytobrimhaven3.md) |
| **Total XP** | 28,150 |
| **Related quests** | 5 |

</div>

## Overview

> I traded 5 of my 'mermaid coins' to Gylew for 500 gold.

## Prerequisites to start

Start with [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)). Required:

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
| Requires | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-47) | stage 47 reached, for stages 100, 105 here |
| Requires | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-250) | stage 250 reached, for stages 12, 13 here |
| Mutually exclusive | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-104) | stage 104 must NOT be reached, for stages 41, 42, 43, 44, 46, 47, 48 here |
| Blocked by | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-170) | stage 170 must NOT be reached, for stage 20 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-183) | stage 183 there needs stage 115 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-103) | stage 103 there needs stages 45, 62 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-105) | stage 105 there needs stage 40 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-106) | stage 106 there needs stage 65 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-108) | stage 108 there needs stage 63 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-44) | stage 44 there needs stages 40, 60, 63 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-45) | stage 45 there needs stages 40, 60, 63 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-47) | stage 47 there needs stage 65 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-48) | stage 48 there needs stages 40, 60, 63 here |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-44) | reaching stages 60, 62, 100, 105 here closes stage 44 there |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-45) | reaching stages 60, 62, 100, 105 here closes stage 45 there |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-48) | reaching stages 60, 62, 100, 105 here closes stage 48 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I traded 5 of my 'mermaid coins' to Gylew for 500 gold. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | have 5 gold, pay 5 gold | 500 XP<br>gives 500× [Gold coins](../items/gold.md) |
| <span id="stage-11"></span>11 | I foolishly gave 5 of my 'mermaid coins' to Gylew. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | have 5 gold, pay 5 gold | 100 XP |
| <span id="stage-12"></span>12 | I sold the 10 coins that I looted from the Arulir secret room to Gylew. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | have 10 gold, pay 10 gold | 750 XP<br>gives 550× [Gold coins](../items/gold.md) |
| <span id="stage-13"></span>13 | I gave Gylew the 10 coins that I looted from the Arulir secret room. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | have 10 gold | 950 XP<br>gives -10× [Gold coins](../items/gold.md)<br>gives 1× [Feygard plated gloves](../items/feygard_plated_gloves.md) |
| <span id="stage-20"></span>20 | I have agreed to set off to Laeroth Manor in pursuit of the Korhald coins and to bring them back to Gylew.<br><span class="qnote">⚡ A scripted event can now trigger on [Laerothbasement1](../maps/laerothbasement1.md).</span> | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | In the Laeroth basement, I noticed a sign on the wall that i could not read in its entirety, but I was able make out the name 'Korhald'. This makes me wonder if this is a clue?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement2](../maps/laerothbasement2.md).</span> | stepping on a trigger on [laerothbasement2](../maps/laerothbasement2.md) | – | – |
| <span id="stage-40"></span>40 | In the Laeroth basement, I discovered and looted the chest containing the 'Korhald coins'.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement2](../maps/laerothbasement2.md).</span><br><span class="qnote">🗺️ Part of [Laerothbasement2](../maps/laerothbasement2.md) visibly changes.</span> | stepping on a trigger on [laerothbasement2](../maps/laerothbasement2.md) | stage 30 | 1,000 XP<br>spawns monsters on laerothbasement2<br>gives 1× [Korhald coin chest](../items/korhald_coins.md) |
| <span id="stage-41"></span>41 | In the Laeroth basement, I encountered an injured man named Forenza. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | – | – |
| <span id="stage-42"></span>42 | I aided Forenza with an ointment for bleeding wounds. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 1,000 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-43"></span>43 | In the Laeroth basement, I was able to help out Forenza by giving him a bonemeal potion. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Bonemeal potion](../items/bonemeal_potion.md) | 500 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-44"></span>44 | In the Laeroth basement, I was able to help out Forenza by giving him a major health potion. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Major potion of health](../items/health_major2.md) | 250 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-45"></span>45 | I have decided to attack Forenza. I should return to Gylew with the key once he is dead. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | – | – |
| <span id="stage-46"></span>46 | In the Laeroth basement, I was able to help out Forenza by giving him a potion of health from Lodar. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md) | 450 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-47"></span>47 | In the Laeroth basement, I was able to help out Forenza by giving him a regular health potion. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Regular potion of health](../items/health.md) | 100 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-48"></span>48 | In the Laeroth basement, I was able to help out Forenza by giving him a minor health potion. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Minor potion of health](../items/health_minor2.md) | 50 XP<br>sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) |
| <span id="stage-50"></span>50 | I've decided to help Forenza by agreeing to get the second key from Gylew. I should go back to Gylew now. Forenza has left the Manor island and has asked that I meet him outside of Brimhaven after my "business" with Gylew is complete. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | – | removes monsters from laerothbasement2<br>spawns monsters on waytobrimhaven3 |
| <span id="stage-60"></span>60 | We discovered a mysterious map inside the Korhald chest and I need to follow the river going east. | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md))<br>[Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | carry 1× [Forenza's key](../items/forenza_key.md), carry 1× [Korhald coin chest](../items/korhald_coins.md), hand over 1× [Forenza's key](../items/forenza_key.md), hand over 1× [Gylew's key](../items/gylew_key.md), hand over 1× [Korhald coin chest](../items/korhald_coins.md), stage 40, stage 63 | 500 XP<br>gives 1× [Mysterious Korhald map](../items/korhald_map.md)<br>gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md)<br>sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44)<br>sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45)<br>sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48) |
| <span id="stage-62"></span>62 | I have decided to attack Gylew. I should return to Forenza with the key once he is dead. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | stage 40, stage 50 | – |
| <span id="stage-63"></span>63 | I killed Gylew and should return to Forenza with Gylew's key.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterway5](../maps/waterway5.md).</span> | stepping on a trigger on [waterway5](../maps/waterway5.md) | – | – |
| <span id="stage-65"></span>65 | Inside the Korhald cave, I found the Coin of Prestige and the Shield of the Brave. I should return to Forenza and show him the coin.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Korhald cave hidden](../maps/korhald_cave_hidden.md).</span> | stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) | carry 1× [Coin of Prestige](../items/hero_coin.md), stage 62 | sets stage 103 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-103) |
| <span id="stage-66"></span>66 | Inside the Korhald cave, I found the Coin of Prestige and the Shield of the Brave. I should return to Gylew and show him the coin.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Korhald cave hidden](../maps/korhald_cave_hidden.md).</span> | stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) | carry 1× [Coin of Prestige](../items/hero_coin.md), stage 45 | sets stage 103 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-103) |
| <span id="stage-100"></span>100 | I sold Gylew the Coin of Prestige and he rewarded me handsomely for it. **(completes quest)** | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | hand over 1× [Coin of Prestige](../items/hero_coin.md) | 5,000 XP<br>gives [Gold coins](../items/gold.md)<br>clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)<br>sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106) |
| <span id="stage-105"></span>105 | I gave Gylew the Coin of Prestige and he told me that if I ever make my way to Feygrad, to seek out his family and they will 'make that shield a little bit better". Whatever that means. **(completes quest)** | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | hand over 1× [Coin of Prestige](../items/hero_coin.md) | 6,000 XP<br>clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)<br>sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106) |
| <span id="stage-110"></span>110 | I sold Forenza the Coin of Prestige and he rewarded me handsomely for it. **(completes quest)** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) | carry 1× [Coin of Prestige](../items/hero_coin.md), carry 1× [Shield of the Brave](../items/shield_of_brave.md), hand over 1× [Coin of Prestige](../items/hero_coin.md), stage 65 | 5,000 XP<br>gives [Gold coins](../items/gold.md)<br>clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)<br>sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106) |
| <span id="stage-115"></span>115 | I gave Forenza the Coin of Prestige and he told me that if I ever make my way to Brightport, to seek out his family and they will 'reward" me. Whatever that means. **(completes quest)** | [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) | carry 1× [Coin of Prestige](../items/hero_coin.md), carry 1× [Shield of the Brave](../items/shield_of_brave.md), hand over 1× [Coin of Prestige](../items/hero_coin.md), stage 65 | 6,000 XP<br>clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)<br>sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “OK. What do you have of value?” — **conditions:** NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20); reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220); have 5 gold; NOT reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10); NOT reached stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11); pay 5 gold → **stage 10**; also gives 500× [Gold coins](../items/gold.md). NPC: “Here is 500 gold.”

???+ note "Stage 11: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Here, take it.” — **conditions:** NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20); reached stage 220 of [The silver scale](../quests/mermaid_scale.md#stage-220); have 5 gold; NOT reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10); NOT reached stage 11 of [The odd coin collector](../quests/odd_coin_collector.md#stage-11); pay 5 gold → **stage 11**. NPC: “That was foolish of you. This is very valuable and you just gave it to me.”

???+ note "Stage 12: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “OK. What do you have of value?” — **conditions:** NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20); reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250); NOT reached stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12); have 10 gold; NOT reached stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13); pay 10 gold → **stage 12**; also gives 550× [Gold coins](../items/gold.md). NPC: “Here is 550 gold”

???+ note "Stage 13: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Here, take it.” — **conditions:** NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20); reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250); NOT reached stage 12 of [The odd coin collector](../quests/odd_coin_collector.md#stage-12); have 10 gold; NOT reached stage 13 of [The odd coin collector](../quests/odd_coin_collector.md#stage-13) → **stage 13**; also gives -10× [Gold coins](../items/gold.md), gives 1× [Feygard plated gloves](../items/feygard_plated_gloves.md). NPC: “Much appreciated. Thank you.”

???+ note "Stage 20: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Yes, of course, you need my help.” — **conditions:** NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); NOT reached stage 20 of [The odd coin collector](../quests/odd_coin_collector.md#stage-20); reached stage 10 of [The odd coin collector](../quests/odd_coin_collector.md#stage-10); NOT reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170) → **stage 20**. NPC: “Then please head to the east and return to me when you find the Korhald coins.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [laerothbasement2](../maps/laerothbasement2.md) → choose “Oops, that's really going to cost me.” — **conditions:** NOT reached stage 30 of [The odd coin collector](../quests/odd_coin_collector.md#stage-30) → **stage 30**. NPC: “As you approach the crates, you notice an almost illegible sign hanging on the wall. Upon further examination, you can…”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [laerothbasement2](../maps/laerothbasement2.md) → choose “[Examine the crate.]” — **conditions:** reached stage 30 of [The odd coin collector](../quests/odd_coin_collector.md#stage-30); NOT reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40) → **stage 40**; also spawns monsters on laerothbasement2, gives 1× [Korhald coin chest](../items/korhald_coins.md), spawns monsters on laerothbasement2. NPC: “You pull out a small, richly covered box.”

???+ note "Stage 41: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “What kind of help?” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104) → **stage 41**. NPC: “Seriously?! Can't you see that I am bleeding and weak?”

???+ note "Stage 42: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Well, I have this ointment for stopping wounds. Take it.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) → **stage 42**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “Oh, that's wonderful. Thank you.”

???+ note "Stage 43: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Well I have a bonemeal potion. It's yours now. Take it.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Bonemeal potion](../items/bonemeal_potion.md) → **stage 43**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “Oh, this stuff is great!”

???+ note "Stage 44: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Here, take it. It's a really strong potion of healing.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Major potion of health](../items/health_major2.md) → **stage 44**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “This stuff tastes nasty, but I swear I can feel it helping already.”

???+ note "Stage 45: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Gylew is the rightful owner of his father's estate and that key belongs to the estate.” — **conditions:** NOT reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45) → **stage 45**. NPC: “What are you going to do about it?”

???+ note "Stage 46: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have this really special potion of healing that I got from a very wise old man. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md) → **stage 46**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “Oh, now this stuff feels like its healing power will last just a little bit longer.”

???+ note "Stage 47: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have an ordinary potion of health for you. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Regular potion of health](../items/health.md) → **stage 47**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “Oh, this should help. Thank you.”

???+ note "Stage 48: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have an little health potion for you. It's all I have. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Minor potion of health](../items/health_minor2.md) → **stage 48**; also sets stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104). NPC: “Oh, this should help. I guess.”

???+ note "Stage 50: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Yes.” — **conditions:** NOT reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45) → **stage 50**; also removes monsters from laerothbasement2, spawns monsters on waytobrimhaven3. NPC: “Great. Go to Gylew and get his key. Then bring it and the chest to me. I will meet you outside of Brimhaven.”

???+ note "Stage 60: 2 routes"

    1. Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Yeah, I can see what you mean.” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) is 63; NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60); hand over 1× [Gylew's key](../items/gylew_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md) → **stage 60**; also gives 1× [Mysterious Korhald map](../items/korhald_map.md), gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md), sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48). NPC: “Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.”
    2. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Yeah, I can see what you mean.” — **conditions:** reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40); NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); carry 1× [Korhald coin chest](../items/korhald_coins.md); carry 1× [Forenza's key](../items/forenza_key.md); NOT reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62); hand over 1× [Korhald coin chest](../items/korhald_coins.md); hand over 1× [Forenza's key](../items/forenza_key.md) → **stage 60**; also gives 1× [Mysterious Korhald map](../items/korhald_map.md), gives 1× [Mysterious Korhald pendant](../items/korhald_chamber_key.md), sets stage 44 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-44), sets stage 45 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-45), sets stage 48 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-48). NPC: “Here, take the map and the pendant. If you need me, I'll be here for a little bit longer.”

???+ note "Stage 62: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Yes, I found the Korhald coins, but you are not getting them...[Attack]” — **conditions:** reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40); NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); reached stage 50 of [The odd coin collector](../quests/odd_coin_collector.md#stage-50) → **stage 62**. NPC: “What? Why?”

???+ note "Stage 63: 1 route"

    1. stepping on a trigger on [waterway5](../maps/waterway5.md) → the conversation leads here automatically — **conditions:** killed 1× [Gylew](../monsters/gylew.md); NOT reached stage 63 of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) → **stage 63**. NPC: “You've killed the defenseless coin collector.”

???+ note "Stage 65: 1 route"

    1. stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) → the conversation leads here automatically — **conditions:** NOT reached stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65); carry 1× [Coin of Prestige](../items/hero_coin.md); reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62) → **stage 65**; also sets stage 103 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-103). NPC: “you have just found a coin and a shield. You should bring this coin back to Forenza.”

???+ note "Stage 66: 1 route"

    1. stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) → the conversation leads here automatically — **conditions:** NOT reached stage 66 of [The odd coin collector](../quests/odd_coin_collector.md#stage-66); reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45); carry 1× [Coin of Prestige](../items/hero_coin.md) → **stage 66**; also sets stage 103 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-103). NPC: “you have just found a coin and a shield. You should bring this coin back to Gylew.”

???+ note "Stage 100: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Sounds like a great deal. I'll take it.” — **conditions:** reached stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 100**; also gives [Gold coins](../items/gold.md), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106). NPC: “Excellent. Come see me if you ever find any more interesting coins.”

???+ note "Stage 105: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Here, take it. I have enough coins.” — **conditions:** reached stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 105**; also clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106). NPC: “Oh, you are so kind. I'll tell you what. Once you find your way to Feygard, seek out my family. They will help you…”

???+ note "Stage 110: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Sounds like a great deal. I'll take it.” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 110**; also gives [Gold coins](../items/gold.md), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106). NPC: “Excellent. Come see me if you ever find any more interesting coins.”

???+ note "Stage 115: 1 route"

    1. Talk to [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Here, take it. I have enough coins.” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 115**; also clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47), sets stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106). NPC: “Oh, how very generous of you to just hand it over for free. I'll tell you what, once you find your way to Brightport,…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 25 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 3 lines changed<br>· text: “Oh, how very generous of you to just hand it over for free. I'll tell…” → “Oh, how very generous of you to just hand it over for free. I'll tell…” |
| [v0.8.13](../versions/0.8.13.md) | stage 12 journal text changed; stage 20 journal text changed; stage 30 journal text changed |

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
