# laeroth_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `laeroth_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 32 |
| **Started by** | stepping on a trigger on [island_underground1](../maps/island_underground1.md), stepping on a trigger on [island_underground3](../maps/island_underground3.md) |
| **NPCs involved** | [Callista, the centaur](../monsters/lae_centaur2.md), [Forenza](../monsters/forenza.md), [Forenza](../monsters/forenza_waytobrimhaven3.md), [Gylew](../monsters/gylew.md), [Moriath](../monsters/moriath.md), [Orion, the centaur](../monsters/lae_centaur1.md) +1 |
| **Locations** | [island1](../maps/island1.md), [island2](../maps/island2.md), [island3](../maps/island3.md), [laerothbasement2](../maps/laerothbasement2.md) |
| **Related quests** | 6 |

</div>

## Overview

> island_underground2_set1

## Prerequisites to start

None: talk to stepping on a trigger on [island_underground1](../maps/island_underground1.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-10) | stage 10 reached, for stage 120 here |
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-35) | stage 35 reached, for stage 3 here |
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-50) | stage 50 reached, for stage 5 here |
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-90) | stage 90 reached, for stage 9 here |
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-160) | stage 160 reached, for stage 14 here |
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-170) | stage 170 reached, for stage 120 here |
| Requires | [The last lord of Laeroth](last_lord.md#stage-40) | stage 40 reached, for stage 140 here |
| Requires | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-47) | stage 47 reached, for stage 106 here |
| Requires | [The odd coin collector](odd_coin_collector.md#stage-40) | stage 40 reached, for stage 105 here |
| Requires | [The odd coin collector](odd_coin_collector.md#stage-45) | stage 45 reached, for stage 103 here |
| Requires | [The odd coin collector](odd_coin_collector.md#stage-62) | stage 62 reached, for stage 103 here |
| Requires | [The odd coin collector](odd_coin_collector.md#stage-63) | stage 63 reached, for stage 108 here |
| Requires | [The odd coin collector](odd_coin_collector.md#stage-65) | stage 65 reached, for stage 106 here |
| Requires | [Wanted men](wanted_men.md#stage-80) | stage 80 reached, for stage 107 here |
| Blocked by | [Shadow of the torturer](lae_torturer.md#stage-110) | stage 110 must NOT be reached, for stages 31, 32, 33, 34 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-40) | stage 40 must NOT be reached, for stage 4 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-70) | stage 70 must NOT be reached, for stage 6 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-90) | stage 90 must NOT be reached, for stages 8, 13 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-100) | stage 100 must NOT be reached, for stage 9 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-110) | stage 110 must NOT be reached, for stages 10, 14 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-120) | stage 120 must NOT be reached, for stage 13 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-160) | stage 160 must NOT be reached, for stage 12 here |
| Mutually exclusive | [Take care of the caretaker](laeroth_caretaker.md#stage-170) | stage 170 must NOT be reached, for stage 14 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-60) | stage 60 must NOT be reached, for stage 108 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-62) | stage 62 must NOT be reached, for stage 105 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-65) | stage 65 must NOT be reached, for stage 103 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-66) | stage 66 must NOT be reached, for stage 103 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-100) | stage 100 must NOT be reached, for stage 105 here |
| Mutually exclusive | [The odd coin collector](odd_coin_collector.md#stage-105) | stage 105 must NOT be reached, for stage 105 here |
| Unlocks | [Shadow of the torturer](lae_torturer.md#stage-5) | stage 5 there needs stages 31, 33, 34 here |
| Unlocks | [Shadow of the torturer](lae_torturer.md#stage-10) | stage 10 there needs stages 31, 33, 34 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-40) | stage 40 there needs stage 4 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-70) | stage 70 there needs stage 6 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-90) | stage 90 there needs stage 8 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-110) | stage 110 there needs stage 10 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-120) | stage 120 there needs stage 13 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-160) | stage 160 there needs stage 12 here |
| Unlocks | [Take care of the caretaker](laeroth_caretaker.md#stage-170) | stage 170 there needs stage 14 here |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-44) | reaching stage 103 here closes stage 44 there |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-45) | reaching stage 103 here closes stage 45 there |
| Blocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-48) | reaching stage 103 here closes stage 48 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | island_underground2_set1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Island underground1](../maps/island_underground1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Island underground3](../maps/island_underground3.md).</span> | stepping on a trigger on [island_underground1](../maps/island_underground1.md) | – | clears stage 2 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-2) |
| <span id="stage-2"></span>2 | island_underground2_set2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Island underground3](../maps/island_underground3.md).</span> | stepping on a trigger on [island_underground3](../maps/island_underground3.md) | – | clears stage 1 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-1) |
| <span id="stage-3"></span>3 | Got Verigil ring<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | – | gives 1× [Verigil's signet ring](../items/verigil_ring.md) |
| <span id="stage-4"></span>4 | placed ring on tomb<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Oegyth crystal](../items/oegyth.md), carry 1× [Verigil's signet ring](../items/verigil_ring.md), hand over 1× [Oegyth crystal](../items/oegyth.md), hand over 1× [Verigil's signet ring](../items/verigil_ring.md) | spawns monsters on laerothtomb1 |
| <span id="stage-5"></span>5 | Got Eyvipa candlestick<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor2](../maps/laerothmanor2.md).</span> | stepping on a trigger on [laerothmanor2](../maps/laerothmanor2.md) | – | gives 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md)<br>sets stage 60 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-60) |
| <span id="stage-6"></span>6 | placed candlestick on tomb<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md), carry 1× [Slightly diminished oegyth crystal](../items/oegyth1.md), hand over 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md), hand over 1× [Slightly diminished oegyth crystal](../items/oegyth1.md) | spawns monsters on laerothtomb1 |
| <span id="stage-7"></span>7 | Got Cuned's diary //obsolete,nut | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-8"></span>8 | Placed diary on tomb<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Cuned's diary](../items/diary_cuned.md), carry 1× [Diminished oegyth crystal](../items/oegyth2.md), hand over 1× [Cuned's diary](../items/diary_cuned.md), hand over 1× [Diminished oegyth crystal](../items/oegyth2.md) | spawns monsters on laerothtomb1 |
| <span id="stage-9"></span>9 | Got Jerelin's seal<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement1](../maps/laerothbasement1.md).</span> | stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) | – | sets stage 100 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-100)<br>gives 1× [Jerelin's seal](../items/seal_jerelin.md) |
| <span id="stage-10"></span>10 | Placed seal on tomb<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Jerelin's seal](../items/seal_jerelin.md), carry 1× [Very diminished oegyth crystal](../items/oegyth3.md), hand over 1× [Jerelin's seal](../items/seal_jerelin.md), hand over 1× [Very diminished oegyth crystal](../items/oegyth3.md) | spawns monsters on laerothtomb1 |
| <span id="stage-11"></span>11 | Got Audela's necklace | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-12"></span>12 | Placed necklace on tomb<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Audela's necklace](../items/audela_necklace.md), carry 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md), hand over 1× [Audela's necklace](../items/audela_necklace.md), hand over 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md) | spawns monsters on laerothtomb1 |
| <span id="stage-13"></span>13 | Raised the spirit of cuned again<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Cuned's diary](../items/diary_cuned.md), carry 1× [Diminished oegyth crystal](../items/oegyth2.md), hand over 1× [Heavily diminished oegyth crystal](../items/oegyth4.md) | spawns monsters on laerothtomb1 |
| <span id="stage-14"></span>14 | Raised Jerelin again<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothtomb1](../maps/laerothtomb1.md).</span> | stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) | carry 1× [Jerelin's seal](../items/seal_jerelin.md), carry 1× [Very diminished oegyth crystal](../items/oegyth3.md), hand over 1× [Nearly depleted oegyth crystal](../items/oegyth6.md) | spawns monsters on laerothtomb1 |
| <span id="stage-31"></span>31 | Opened cell 1<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison4](../maps/laerothprison4.md).</span><br><span class="qnote">🗺️ Part of [Laerothprison4](../maps/laerothprison4.md) visibly changes.</span> | walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) | carry 1× [Laeroth prison key](../items/lae_prison_key.md) | – |
| <span id="stage-32"></span>32 | Opened cell 2<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison4](../maps/laerothprison4.md).</span><br><span class="qnote">🗺️ Part of [Laerothprison4](../maps/laerothprison4.md) visibly changes.</span> | walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) | carry 1× [Laeroth prison key](../items/lae_prison_key.md) | – |
| <span id="stage-33"></span>33 | Opened cell 3<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison4](../maps/laerothprison4.md).</span><br><span class="qnote">🗺️ Part of [Laerothprison4](../maps/laerothprison4.md) visibly changes.</span> | walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) | carry 1× [Laeroth prison key](../items/lae_prison_key.md) | – |
| <span id="stage-34"></span>34 | Opened cell 4<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison4](../maps/laerothprison4.md).</span><br><span class="qnote">🗺️ Part of [Laerothprison4](../maps/laerothprison4.md) visibly changes.</span> | walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) | carry 1× [Laeroth prison key](../items/lae_prison_key.md) | – |
| <span id="stage-102"></span>102 | Inside the Laeroth barn basement, the PC has found the Mystery Laeroth key.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbarn1](../maps/laerothbarn1.md).</span> | stepping on a trigger on [laerothbarn1](../maps/laerothbarn1.md) | – | gives 1× [Mystery Laeroth key](../items/mystery_laeroth_key.md) |
| <span id="stage-103"></span>103 | This is just a wrapper around the odd coin collector 65 and 66 steps, it is easier to check this one when looking for confirmation that the PC found the Coin of Prestige and the Shield of the Brave.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Korhald cave hidden](../maps/korhald_cave_hidden.md).</span> | stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) | carry 1× [Coin of Prestige](../items/hero_coin.md) | sets stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65)<br>sets stage 66 of [The odd coin collector](../quests/odd_coin_collector.md#stage-66) |
| <span id="stage-104"></span>104 | The PC has helped heal Forenza. This is just a wrapper around the odd coin collector quest's "aid" Forenza steps. | [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) | hand over 1× [Bonemeal potion](../items/bonemeal_potion.md), hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md), hand over 1× [Major potion of health](../items/health_major2.md), hand over 1× [Minor potion of health](../items/health_minor2.md), hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md), hand over 1× [Regular potion of health](../items/health.md) | sets stage 42 of [The odd coin collector](../quests/odd_coin_collector.md#stage-42)<br>sets stage 43 of [The odd coin collector](../quests/odd_coin_collector.md#stage-43)<br>sets stage 44 of [The odd coin collector](../quests/odd_coin_collector.md#stage-44)<br>sets stage 46 of [The odd coin collector](../quests/odd_coin_collector.md#stage-46)<br>sets stage 47 of [The odd coin collector](../quests/odd_coin_collector.md#stage-47)<br>sets stage 48 of [The odd coin collector](../quests/odd_coin_collector.md#stage-48) |
| <span id="stage-105"></span>105 | I gave Gylew the Korhald chest. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | carry 1× [Forenza's key](../items/forenza_key.md), carry 1× [Korhald coin chest](../items/korhald_coins.md), hand over 1× [Korhald coin chest](../items/korhald_coins.md) | – |
| <span id="stage-106"></span>106 | This is just a wrapper around the odd coin collector "end" steps as there are 4 of them, it is easier to check this one when looking for confirmation that the quest is complete. | [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md))<br>[Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) | carry 1× [Coin of Prestige](../items/hero_coin.md), carry 1× [Shield of the Brave](../items/shield_of_brave.md), hand over 1× [Coin of Prestige](../items/hero_coin.md) | gives [Gold coins](../items/gold.md)<br>sets stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100)<br>clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47)<br>sets stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105)<br>sets stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115)<br>sets stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110) |
| <span id="stage-107"></span>107 | Sold 5 bronze and 5 silver coins to the coin collector. | [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md))<br>[Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | carry 50× [Bronze coin](../items/bronze_coin.md), carry 60× [Silver coin](../items/silver_coin.md), hand over 5× [Bronze coin](../items/bronze_coin.md), hand over 5× [Silver coin](../items/silver_coin.md), stage 106 | gives 160× [Gold coins](../items/gold.md) |
| <span id="stage-108"></span>108 | PC gave Forenza Gylew's key. | [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) | hand over 1× [Gylew's key](../items/gylew_key.md), hand over 1× [Korhald coin chest](../items/korhald_coins.md) | – |
| <span id="stage-120"></span>120 | Jerelin grave moved<br><span class="qnote">⚡ A scripted event can now trigger on [Laerothtomb1](../maps/laerothtomb1.md).</span> | [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) | – | removes monsters from laerothmanor1<br>sets stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180) |
| <span id="stage-140"></span>140 | Looted Adakin's chest.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement0](../maps/laerothbasement0.md).</span> | stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) | hand over 1× [Key for Adakin's chest](../items/adakin_chest_key.md) | gives 3× [Major potion of health](../items/health_major2.md)<br>gives 1× [Balanced steel sword](../items/sword_balanced_steel.md)<br>gives 1× [Ring of damage +6](../items/ring_dmg6.md) |
| <span id="stage-200"></span>200 | brute_creator_in<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake8 cave](../maps/mountainlake8_cave.md).</span> | stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) | – | changes map mountainlake8_cave |
| <span id="stage-201"></span>201 | brute_creator_key<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake8 cave](../maps/mountainlake8_cave.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Mountainlake8 cave](../maps/mountainlake8_cave.md).</span> | stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) | – | faction “brute_creator_flash” set to 1<br>sets stage 30 of [Brutes](../quests/brute_creator.md#stage-30)<br>faction “brute_creator_flash” set to 2 |
| <span id="stage-211"></span>211 | centaur1 heard | [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md)) | – | sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10) |
| <span id="stage-212"></span>212 | centaur2 heard | [Callista, the centaur](../monsters/lae_centaur2.md) ([island2](../maps/island2.md)) | – | sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10) |
| <span id="stage-213"></span>213 | centaur3 heard | [Silvanus, the centaur](../monsters/lae_centaur3.md) ([island3](../maps/island3.md)) | – | sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [island_underground1](../maps/island_underground1.md) → the conversation leads here automatically → **stage 1**; also clears stage 2 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-2)

???+ note "Stage 2: 1 route"

    1. stepping on a trigger on [island_underground3](../maps/island_underground3.md) → the conversation leads here automatically → **stage 2**; also clears stage 1 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-1)

???+ note "Stage 3: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 35 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-35); NOT reached stage 3 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-3) → **stage 3**; also gives 1× [Verigil's signet ring](../items/verigil_ring.md). NPC: “You found a ring with "V" engraved on it. This should work.”

???+ note "Stage 4: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Place Verigil's ring on the tomb.” — **conditions:** carry 1× [Verigil's signet ring](../items/verigil_ring.md); NOT reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40); carry 1× [Oegyth crystal](../items/oegyth.md); hand over 1× [Verigil's signet ring](../items/verigil_ring.md); hand over 1× [Oegyth crystal](../items/oegyth.md) → **stage 4**; also spawns monsters on laerothtomb1. NPC: “You place an oegyth crystal and Verigil's signet ring on the tomb, and chant "iseray iritspay"”

???+ note "Stage 5: 1 route"

    1. stepping on a trigger on [laerothmanor2](../maps/laerothmanor2.md) → choose “Take a look in the chest.” — **conditions:** reached stage 50 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-50); NOT reached stage 5 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-5) → **stage 5**; also gives 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md), sets stage 60 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-60). NPC: “You rummage around in the contents. Then a high quality candlestick catches your eye. It has "E" engraved on it! This…”

???+ note "Stage 6: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Place candlestick on the tomb.” — **conditions:** carry 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md); carry 1× [Slightly diminished oegyth crystal](../items/oegyth1.md); NOT reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70); hand over 1× [Eyvipa's candlestick](../items/eyvipa_candlestick.md); hand over 1× [Slightly diminished oegyth crystal](../items/oegyth1.md) → **stage 6**; also spawns monsters on laerothtomb1. NPC: “You place the slightly diminished oegyth crystal and Eyvipa's candlestick on the tomb, and chant "iseray iritspay"”

???+ note "Stage 8: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Place diary on the tomb.” — **conditions:** carry 1× [Cuned's diary](../items/diary_cuned.md); carry 1× [Diminished oegyth crystal](../items/oegyth2.md); NOT reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90); hand over 1× [Cuned's diary](../items/diary_cuned.md); hand over 1× [Diminished oegyth crystal](../items/oegyth2.md) → **stage 8**; also spawns monsters on laerothtomb1. NPC: “You place the diminished oegyth crystal and Cuned's diary on the tomb, and chant "iseray iritspay"”

???+ note "Stage 9: 1 route"

    1. stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) → choose “You rummage around in the clutter in the chest.” — **conditions:** reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90); NOT reached stage 100 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-100) → **stage 9**; also sets stage 100 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-100), gives 1× [Jerelin's seal](../items/seal_jerelin.md). NPC: “You find a ring that apparently served as a seal for Jerelin, as it had a large "J" on it. You take the seal.”

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Place seal on the tomb.” — **conditions:** carry 1× [Jerelin's seal](../items/seal_jerelin.md); carry 1× [Very diminished oegyth crystal](../items/oegyth3.md); NOT reached stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110); hand over 1× [Jerelin's seal](../items/seal_jerelin.md); hand over 1× [Very diminished oegyth crystal](../items/oegyth3.md) → **stage 10**; also spawns monsters on laerothtomb1. NPC: “You place the very diminished oegyth crystal and Jerelin's seal on the tomb, and chant "iseray iritspay"”

???+ note "Stage 12: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Place Audela's necklace on the tomb.” — **conditions:** carry 1× [Audela's necklace](../items/audela_necklace.md); carry 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md); NOT reached stage 160 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-160); hand over 1× [Audela's necklace](../items/audela_necklace.md); hand over 1× [Very heavily diminished oegyth crystal](../items/oegyth5.md) → **stage 12**; also spawns monsters on laerothtomb1. NPC: “You place the very heavily diminished oegyth crystal and Audela's necklace on the tomb, and chant "iseray iritspay"”

???+ note "Stage 13: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Call for Cuned.” — **conditions:** carry 1× [Cuned's diary](../items/diary_cuned.md); carry 1× [Diminished oegyth crystal](../items/oegyth2.md); NOT reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90); NOT reached stage 120 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-120); hand over 1× [Heavily diminished oegyth crystal](../items/oegyth4.md) → **stage 13**; also spawns monsters on laerothtomb1. NPC: “You place the heavily diminished oegyth crystal on the tomb, and chant "iseray iritspay"”

???+ note "Stage 14: 1 route"

    1. stepping on a trigger on [laerothtomb1](../maps/laerothtomb1.md) → choose “Call for Jerelin.” — **conditions:** carry 1× [Jerelin's seal](../items/seal_jerelin.md); carry 1× [Very diminished oegyth crystal](../items/oegyth3.md); NOT reached stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110); reached stage 160 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-160); NOT reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170); hand over 1× [Nearly depleted oegyth crystal](../items/oegyth6.md) → **stage 14**; also spawns monsters on laerothtomb1. NPC: “You place the nearly depleted oegyth crystal on the tomb, and chant "iseray iritspay"”

???+ note "Stage 31: 1 route"

    1. walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) → choose “Unlock.” — **conditions:** carry 1× [Laeroth prison key](../items/lae_prison_key.md); NOT reached stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110) → **stage 31**. NPC: “Click.”

???+ note "Stage 32: 1 route"

    1. walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) → choose “Unlock.” — **conditions:** carry 1× [Laeroth prison key](../items/lae_prison_key.md); NOT reached stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110) → **stage 32**. NPC: “Click.”

???+ note "Stage 33: 1 route"

    1. walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) → choose “Unlock.” — **conditions:** carry 1× [Laeroth prison key](../items/lae_prison_key.md); NOT reached stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110) → **stage 33**. NPC: “Click.”

???+ note "Stage 34: 1 route"

    1. walking into a blocked passage on [laerothprison4](../maps/laerothprison4.md) → choose “Unlock.” — **conditions:** carry 1× [Laeroth prison key](../items/lae_prison_key.md); NOT reached stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110) → **stage 34**. NPC: “Click.”

???+ note "Stage 102: 1 route"

    1. stepping on a trigger on [laerothbarn1](../maps/laerothbarn1.md) → choose “[Bend down and take a look.]” — **conditions:** NOT reached stage 102 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-102) → **stage 102**; also gives 1× [Mystery Laeroth key](../items/mystery_laeroth_key.md)

???+ note "Stage 103: 2 routes"

    1. stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) → the conversation leads here automatically — **conditions:** NOT reached stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65); carry 1× [Coin of Prestige](../items/hero_coin.md); reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62) → **stage 103**; also sets stage 65 of [The odd coin collector](../quests/odd_coin_collector.md#stage-65). NPC: “you have just found a coin and a shield. You should bring this coin back to Forenza.”
    2. stepping on a trigger on [korhald_cave_hidden](../maps/korhald_cave_hidden.md) → the conversation leads here automatically — **conditions:** NOT reached stage 66 of [The odd coin collector](../quests/odd_coin_collector.md#stage-66); reached stage 45 of [The odd coin collector](../quests/odd_coin_collector.md#stage-45); carry 1× [Coin of Prestige](../items/hero_coin.md) → **stage 103**; also sets stage 66 of [The odd coin collector](../quests/odd_coin_collector.md#stage-66). NPC: “you have just found a coin and a shield. You should bring this coin back to Gylew.”

???+ note "Stage 104: 7 routes"

    1. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Well, I have this ointment for stopping wounds. Take it.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) → **stage 104**; also sets stage 42 of [The odd coin collector](../quests/odd_coin_collector.md#stage-42). NPC: “Oh, that's wonderful. Thank you.”
    2. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Well I have a bonemeal potion. It's yours now. Take it.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Bonemeal potion](../items/bonemeal_potion.md) → **stage 104**; also sets stage 43 of [The odd coin collector](../quests/odd_coin_collector.md#stage-43). NPC: “Oh, this stuff is great!”
    3. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “Here, take it. It's a really strong potion of healing.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Major potion of health](../items/health_major2.md) → **stage 104**; also sets stage 44 of [The odd coin collector](../quests/odd_coin_collector.md#stage-44). NPC: “This stuff tastes nasty, but I swear I can feel it helping already.”
    4. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have this really special potion of healing that I got from a very wise old man. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Lodar's potion of health](../items/pot_healthlodar.md) → **stage 104**; also sets stage 46 of [The odd coin collector](../quests/odd_coin_collector.md#stage-46). NPC: “Oh, now this stuff feels like its healing power will last just a little bit longer.”
    5. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have an ordinary potion of health for you. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Regular potion of health](../items/health.md) → **stage 104**; also sets stage 47 of [The odd coin collector](../quests/odd_coin_collector.md#stage-47). NPC: “Oh, this should help. Thank you.”
    6. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I have an little health potion for you. It's all I have. Take it!” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); hand over 1× [Minor potion of health](../items/health_minor2.md) → **stage 104**; also sets stage 48 of [The odd coin collector](../quests/odd_coin_collector.md#stage-48). NPC: “Oh, this should help. I guess.”
    7. Talk to [Forenza](../monsters/forenza.md) ([laerothbasement2](../maps/laerothbasement2.md)) → choose “I'm so sorry, but I have nothing that can help you.” — **conditions:** NOT reached stage 104 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-104); NOT carry 1× [Bonemeal potion](../items/bonemeal_potion.md); NOT carry 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md); NOT carry 1× [Lodar's potion of health](../items/pot_healthlodar.md); NOT carry 1× [Major potion of health](../items/health_major2.md); NOT carry 1× [Regular potion of health](../items/health.md); NOT carry 1× [Minor potion of health](../items/health_minor2.md) → **stage 104**. NPC: “You are a disappointment. Anyways...”

???+ note "Stage 105: 1 route"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Here you go.” — **conditions:** reached stage 40 of [The odd coin collector](../quests/odd_coin_collector.md#stage-40); NOT reached stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100); NOT reached stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105); carry 1× [Korhald coin chest](../items/korhald_coins.md); carry 1× [Forenza's key](../items/forenza_key.md); NOT reached stage 62 of [The odd coin collector](../quests/odd_coin_collector.md#stage-62); hand over 1× [Korhald coin chest](../items/korhald_coins.md) → **stage 105**. NPC: “[Gylew examines the chest] What?! There are two locks! How can this be? Do you know anything about a second key?”

???+ note "Stage 106: 4 routes"

    1. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Sounds like a great deal. I'll take it.” — **conditions:** reached stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 106**; also gives [Gold coins](../items/gold.md), sets stage 100 of [The odd coin collector](../quests/odd_coin_collector.md#stage-100), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47). NPC: “Excellent. Come see me if you ever find any more interesting coins.”
    2. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Here, take it. I have enough coins.” — **conditions:** reached stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 106**; also sets stage 105 of [The odd coin collector](../quests/odd_coin_collector.md#stage-105), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47). NPC: “Oh, you are so kind. I'll tell you what. Once you find your way to Feygard, seek out my family. They will help you…”
    3. Talk to [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Here, take it. I have enough coins.” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 106**; also sets stage 115 of [The odd coin collector](../quests/odd_coin_collector.md#stage-115), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47). NPC: “Oh, how very generous of you to just hand it over for free. I'll tell you what, once you find your way to Brightport,…”
    4. Talk to [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Sounds like a great deal. I'll take it.” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-65) is 65; carry 1× [Shield of the Brave](../items/shield_of_brave.md); carry 1× [Coin of Prestige](../items/hero_coin.md); hand over 1× [Coin of Prestige](../items/hero_coin.md) → **stage 106**; also gives [Gold coins](../items/gold.md), sets stage 110 of [The odd coin collector](../quests/odd_coin_collector.md#stage-110), clears stage 47 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-47). NPC: “Excellent. Come see me if you ever find any more interesting coins.”

???+ note "Stage 107: 2 routes"

    1. Talk to [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Well, something is better than nothing.” — **conditions:** reached stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106); reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80); carry 60× [Silver coin](../items/silver_coin.md); carry 50× [Bronze coin](../items/bronze_coin.md); NOT reached stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107); hand over 5× [Silver coin](../items/silver_coin.md); hand over 5× [Bronze coin](../items/bronze_coin.md) → **stage 107**; also gives 160× [Gold coins](../items/gold.md). NPC: “Thank you so much.”
    2. Talk to [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) → choose “Well, something is better than nothing.” — **conditions:** reached stage 106 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-106); reached stage 80 of [Wanted men](../quests/wanted_men.md#stage-80); carry 50× [Bronze coin](../items/bronze_coin.md); carry 60× [Silver coin](../items/silver_coin.md); NOT reached stage 107 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107); hand over 5× [Silver coin](../items/silver_coin.md); hand over 5× [Bronze coin](../items/bronze_coin.md) → **stage 107**; also gives 160× [Gold coins](../items/gold.md). NPC: “Thank you so much.”

???+ note "Stage 108: 1 route"

    1. Talk to [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) → choose “Yes, and I also have the chest. Here, take them. [You give both items to Forenza]” — **conditions:** latest stage of [The odd coin collector](../quests/odd_coin_collector.md#stage-63) is 63; NOT reached stage 60 of [The odd coin collector](../quests/odd_coin_collector.md#stage-60); hand over 1× [Gylew's key](../items/gylew_key.md); hand over 1× [Korhald coin chest](../items/korhald_coins.md) → **stage 108**. NPC: “With an ever growing smile upon his face, Forenza inserts the first key and then the second. He then proceeds to…”

???+ note "Stage 120: 1 route"

    1. Talk to [Moriath](../monsters/moriath.md) ([laerothmanor1](../maps/laerothmanor1.md)) → choose “Finally, success. I had to raise the spirits of many family members, but Jerelin said he would release you…” — **conditions:** reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10); reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170) → **stage 120**; also removes monsters from laerothmanor1, sets stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180). NPC: “Thank you. I will do that if it releases me from the oath. I will do it immediately. Farewell, and thanks again.”

???+ note "Stage 140: 1 route"

    1. stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) → choose “Maybe I should loot the chest. After all, Adakin is not here anymore.” — **conditions:** reached stage 40 of [The last lord of Laeroth](../quests/last_lord.md#stage-40); hand over 1× [Key for Adakin's chest](../items/adakin_chest_key.md) → **stage 140**; also gives 3× [Major potion of health](../items/health_major2.md), gives 1× [Balanced steel sword](../items/sword_balanced_steel.md), gives 1× [Ring of damage +6](../items/ring_dmg6.md). NPC: “There are some nice items here. Let's see: I'll take 3 of these health potions, the sword and this ring.”

???+ note "Stage 200: 1 route"

    1. stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) → the conversation leads here automatically → **stage 200**; also changes map mountainlake8_cave. NPC: “Hey, I'm on the inside!”

???+ note "Stage 201: 2 routes"

    1. stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) → the conversation leads here automatically — **conditions:** random chance (3%) → **stage 201**; also faction “brute_creator_flash” set to 1, sets stage 30 of [Brutes](../quests/brute_creator.md#stage-30)
    2. stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) → the conversation leads here automatically — **conditions:** random chance (5%) → **stage 201**; also faction “brute_creator_flash” set to 2, sets stage 30 of [Brutes](../quests/brute_creator.md#stage-30)

???+ note "Stage 211: 1 route"

    1. Talk to [Orion, the centaur](../monsters/lae_centaur1.md) ([island1](../maps/island1.md)) → choose “Then just tell me where he is.” → **stage 211**; also sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”

???+ note "Stage 212: 1 route"

    1. Talk to [Callista, the centaur](../monsters/lae_centaur2.md) ([island2](../maps/island2.md)) → choose “Fine, I'll go see him.” → **stage 212**; also sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”

???+ note "Stage 213: 1 route"

    1. Talk to [Silvanus, the centaur](../monsters/lae_centaur3.md) ([island3](../maps/island3.md)) → choose “Enough now. I want to speak to your boss.” → **stage 213**; also sets stage 10 of [Not Pony Island](../quests/lae_centaurs.md#stage-10). NPC: “Thalos, our wise guide, is currently in the northeast of the island.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 44 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed<br>· text: “Oh, how very generous of you to just hand it over for free. I'll tell…” → “Oh, how very generous of you to just hand it over for free. I'll tell…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=laeroth_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `laeroth_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 31, 32, 33, 34, 102, 103, 104, 105, 106, 107, 108, 120, 140, 200, 201, 211, 212, 213 |
    | Dialogue nodes setting stages | 1: `island_underground2_set1`, 2: `island_underground2_set2`, 3: `nightstand_search_1`, 4: `verigil_script_2a`, 5: `chest_search_2`, 6: `eyvipa_script_2a`, 8: `cuned_script_2a`, 9: `jerelin_chest_search_2`, 10: `jerelin_script_2a`, 12: `audela_script_2a`, 13: `cuned_script_b_2a`, 14: `jerelin_script_b_2a`, 31: `lae_prison_cell1_unlock`, 32: `lae_prison_cell2_unlock`, 33: `lae_prison_cell3_unlock`, 34: `lae_prison_cell4_unlock`, 102: `laeroth_barn_basement_2`, 103: `korhald_cave_hidden_basket_examine_loot_f2`, 103: `korhald_cave_hidden_basket_examine_loot_g2`, 104: `forenza_island_injured_ointment`, 104: `forenza_island_injured_help_bm`, 104: `forenza_island_injured_help_mph`, 105: `gylew_korhald_30`, 106: `gylew_korhald_cop_50`, 106: `gylew_korhald_cop_35`, 106: `forenza_korhald_cop_35`, 107: `coin_collector_thief_coins_70`, 108: `forenza_brimhaven_10`, 120: `moriath_9_1`, 140: `adakin_chest_3a`, 200: `brute_creator_in`, 201: `brute_creator_flash_1`, 201: `brute_creator_flash_2`, 211: `lae_centaur1_8`, 212: `lae_centaur2_8`, 213: `lae_centaur3_8` |
    | Dialogue nodes clearing stages | 2: `island_underground2_set1`, 1: `island_underground2_set2`, 200: `brute_creator_out`, 201: `brute_creator_flash_0`, 31: `lae_demon4`, 32: `lae_demon4`, 33: `lae_demon4`, 34: `lae_demon4` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
