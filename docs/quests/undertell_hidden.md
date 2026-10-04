# hidden_undertell

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `undertell_hidden` |
| **In journal** | No (hidden flag) |
| **Stages** | 39 |
| **Started by** | walking into a blocked passage on [galmore_58](../maps/galmore_58.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Brenor](../monsters/brenor.md), [Drunkard](../monsters/drunkard.md), [Lethgar miner ghost](../monsters/lethgar_miner_ghost2.md), [Lethgar slave ghost](../monsters/lethgar_female_ghost.md), [Morvath](../monsters/morvath.md) +8 |
| **Locations** | [brimhaven4](../maps/brimhaven4.md), [brimhaven_house1](../maps/brimhaven_house1.md), [fallhaven_nw](../maps/fallhaven_nw.md), [undertell_00](../maps/undertell_00.md) |
| **Related quests** | 10 |

</div>

## Overview

> 3 = PC has encountered the Galmore encampment barricades.

## Prerequisites to start

None: talk to walking into a blocked passage on [galmore_58](../maps/galmore_58.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [About a girl](about_a_girl.md#stage-40) | stage 40 reached, for stage 90 here |
| Requires | [About a girl](about_a_girl.md#stage-70) | stage 70 reached, for stage 85 here |
| Requires | [Much water](brv_flood.md#stage-200) | stage 200 reached, for stage 15 here |
| Requires | [The fifth master](fifth_master.md#stage-65) | stage 65 reached, for stage 50 here |
| Requires | [hidden_devotion (hidden flag)](hidden_devotion.md#stage-450) | stage 450 reached, for stage 82 here |
| Requires | [Lost treasures](nocmar.md#stage-10) | stage 10 reached, for stage 10 here |
| Requires | [Lost treasures](nocmar.md#stage-20) | stage 20 reached, for stage 10 here |
| Requires | [Lost treasures](nocmar.md#stage-100) | stage 100 reached, for stages 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 here |
| Requires | [Sutdove_nondisplay (hidden flag)](sutdover_hidden.md#stage-2) | stage 2 reached, for stage 60 here |
| Requires | [Undertell: What was not written](undertell_book.md#stage-40) | stage 40 reached, for stage 70 here |
| Blocked by | [About a girl](about_a_girl.md#stage-50) | stage 50 must NOT be reached, for stage 95 here |
| Blocked by | [About a girl](about_a_girl.md#stage-70) | stage 70 must NOT be reached, for stage 90 here |
| Blocked by | [About a girl](about_a_girl.md#stage-80) | stage 80 must NOT be reached, for stage 85 here |
| Mutually exclusive | [Lost treasures](nocmar.md#stage-90) | stage 90 must NOT be reached, for stage 10 here |
| Blocked by | [A place to forge](place_to_forge.md#stage-50) | stage 50 must NOT be reached, for stage 15 here |
| Blocked by | [A place to forge](place_to_forge.md#stage-60) | stage 60 must NOT be reached, for stage 10 here |
| Blocked by | [You shall pass](undertell_barricades.md#stage-130) | stage 130 must NOT be reached, for stage 55 here |
| Unlocks | [About a girl](about_a_girl.md#stage-80) | stage 80 there needs stage 85 here |
| Unlocks | [The fifth master](fifth_master.md#stage-70) | stage 70 there needs stage 45 here |
| Unlocks | [The fifth master](fifth_master.md#stage-72) | stage 72 there needs stage 45 here |
| Unlocks | [Lost treasures](nocmar.md#stage-35) | stage 35 there needs stage 3 here |
| Unlocks | [Lost treasures](nocmar.md#stage-80) | stage 80 there needs stage 10 here |
| Unlocks | [Lost treasures](nocmar.md#stage-110) | stage 110 there needs stages 38, 45 here |
| Unlocks | [Lost treasures](nocmar.md#stage-200) | stage 200 there needs stages 25, 30, 31, 32, 33, 34, 35, 36, 37 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-30) | stage 30 there needs stage 15 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-35) | stage 35 there needs stage 15 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-40) | stage 40 there needs stage 15 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-50) | stage 50 there needs stage 15 here |
| Unlocks | [You shall pass](undertell_barricades.md#stage-130) | stage 130 there needs stage 55 here |
| Unlocks | [Undertell: What was not written](undertell_book.md#stage-70) | stage 70 there needs stage 75 here |
| Blocks | [Dominion](dominion.md#stage-50) | reaching stage 7 here closes stage 50 there |
| Blocks | [The fifth master](fifth_master.md#stage-65) | reaching stage 50 here closes stage 65 there |
| Blocks | [The fifth master](fifth_master.md#stage-70) | reaching stage 50 here closes stage 70 there |
| Blocks | [The fifth master](fifth_master.md#stage-72) | reaching stage 50 here closes stage 72 there |
| Blocks | [Undertell: What was not written](undertell_book.md#stage-30) | reaching stage 7 here closes stage 30 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-3"></span>3 | 3 = PC has encountered the Galmore encampment barricades. | walking into a blocked passage on [galmore_58](../maps/galmore_58.md) | – | – |
| <span id="stage-5"></span>5 | 5 = PC has met a kazaul master. | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))<br>[Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))<br>[Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md))<br>+1 more | – | – |
| <span id="stage-7"></span>7 | PC found the "The Five Aspects" ritual and let the Masters know about it. | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))<br>[Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))<br>[Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md))<br>+1 more | carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md), hand over 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) | sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78)<br>sets stage 80 of [The fifth master](../quests/fifth_master.md#stage-80)<br>spawns monsters on undertell_5 |
| <span id="stage-8"></span>8 | 8 = PC found the Undertell pickaxe<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell 22](../maps/undertell_22.md).</span><br><span class="qnote">🗺️ Part of [Undertell 22](../maps/undertell_22.md) visibly changes.</span> | stepping on a trigger on [undertell_22](../maps/undertell_22.md) | – | gives 1× [Undertell pickaxe](../items/undertell_pickaxe.md) |
| <span id="stage-10"></span>10 | 10 = PC has handed over the heartstone to Nocmar. | [Nocmar](../monsters/nocmar.md) | hand over 1× [Heartstone](../items/heartstone.md) | – |
| <span id="stage-15"></span>15 | 15 = PC was able to get Mustura out of the way in order to talk to Alkapoan. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | – | – |
| <span id="stage-25"></span>25 | 25 = PC has seen Nocmar's inventory. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-30"></span>30 | 30 = PC chose to forge the claymore. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-31"></span>31 | 31 = PC chose to forge the one-handed sword. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-32"></span>32 | 32 = PC chose to forge the dagger. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-33"></span>33 | 33 = PC chose to forge the glaive. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-34"></span>34 | 34 = PC chose to forge the greateaxe. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-35"></span>35 | 35 = PC chose to forge the hand axe. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-36"></span>36 | 36 = PC chose to forge the mace. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-37"></span>37 | 37 = PC chose to forge the parrying weapon. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-38"></span>38 | 38 = PC chose to forge no weapon. | [Nocmar](../monsters/nocmar.md) | stage 25 | sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200) |
| <span id="stage-39"></span>39 | 39 = PC gave Nocmar an answer. | [Nocmar](../monsters/nocmar.md) | stage 25, stage 30, stage 31, stage 32, stage 33, stage 34, stage 35, stage 36, stage 37 | sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200) |
| <span id="stage-45"></span>45 | 45 = white house - going down the basement stairs<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house](../maps/white_house.md).</span> | stepping on a trigger on [white_house](../maps/white_house.md) | – | – |
| <span id="stage-50"></span>50 | 50 = PC has "talked" to the white house dragon.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house basement](../maps/white_house_basement.md).</span> | walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md)<br>stepping on a trigger on [white_house_basement](../maps/white_house_basement.md)<br>[Lethgar miner ghost](../monsters/lethgar_miner_ghost2.md) ([undertell_1_1](../maps/undertell_1_1.md)) | carry 1× [Ash covered dragon scales](../items/ancient_dragon_scales.md), stage 45 | – |
| <span id="stage-55"></span>55 | 55 = PC gave the Potion of heightened senses to Rain. | [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) | have 5,000 gold | – |
| <span id="stage-60"></span>60 | 60 = PC gave Nixite crystal to the rock eater. | [Rock eater](../monsters/rock_eater.md) ([undertell_exit](../maps/undertell_exit.md)) | hand over 1× [Nixite crystal](../items/nixite_crystal.md) | removes monsters from undertell_exit<br>spawns monsters on undertell_exit |
| <span id="stage-65"></span>65 | 65 = PC confirmed exit from the Lake of Fire.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Undertell 5](../maps/undertell_5.md).</span> | walking into a blocked passage on [undertell_5](../maps/undertell_5.md) | – | faction “undertellIsland” set to 0 |
| <span id="stage-66"></span>66 | 66 = PC confirmed entry to the Lake of Fire.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Undertell 4 01](../maps/undertell_4_01.md).</span> | walking into a blocked passage on [undertell_4_01](../maps/undertell_4_01.md) | – | faction “undertellIsland” set to 1 |
| <span id="stage-70"></span>70 | 70 = PC has yelled down to Cora. | walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md) | – | removes monsters from undertell_1_1 |
| <span id="stage-75"></span>75 | 75 = PC has chased Cora down to the first floor.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell 01](../maps/undertell_01.md).</span> | stepping on a trigger on [undertell_01](../maps/undertell_01.md) | stage 70 | spawns monsters on undertell_1_1 |
| <span id="stage-78"></span>78 | 78 = PC has entered archival room at least once.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell archive2](../maps/undertell_archive2.md).</span> | stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) | – | applies condition kazaul_mortality<br>applies condition burning<br>applies condition kazarite_misery |
| <span id="stage-80"></span>80 | 80 = PC has been pinched. | [Lethgar slave ghost](../monsters/lethgar_female_ghost.md) ([undertell_1_1](../maps/undertell_1_1.md)) | – | – |
| <span id="stage-81"></span>81 | 81 = PC has seen the sleep quarters.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell 1 0](../maps/undertell_1_0.md).</span> | stepping on a trigger on [undertell_1_0](../maps/undertell_1_0.md) | – | – |
| <span id="stage-82"></span>82 | 82 = PC can sleep in Undertell now.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Undertell 1 0](../maps/undertell_1_0.md).</span> | [Lethgar slave ghost](../monsters/lethgar_female_ghost.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 81 | – |
| <span id="stage-83"></span>83 | 83 = Looted chest on undertell_00<br><span class="qnote">🗺️ Part of [Undertell 00](../maps/undertell_00.md) visibly changes.</span> | walking into a blocked passage on [undertell_00](../maps/undertell_00.md) | stage 5 | gives 2100× [Gold coins](../items/gold.md) |
| <span id="stage-84"></span>84 | 84 = Looted chest of rare coins.<br><span class="qnote">🗺️ Part of [Undertell 3 02](../maps/undertell_3_02.md) visibly changes.</span> | walking into a blocked passage on [undertell_3_02](../maps/undertell_3_02.md) | – | gives 1× [Rare coins](../items/rare_coins.md) |
| <span id="stage-85"></span>85 | 85 = PC gave the talisman to Syrra. | walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) | carry 1× [Folded copper talisman](../items/folded_copper_talisman.md), hand over 1× [Folded copper talisman](../items/folded_copper_talisman.md) | – |
| <span id="stage-86"></span>86 | 86 = PC entered archival room.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell archive2](../maps/undertell_archive2.md).</span> | stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) | – | applies condition kazaul_mortality<br>applies condition burning<br>applies condition kazarite_misery |
| <span id="stage-87"></span>87 | 87 = PC took the crown.<br><span class="qnote">🗺️ Part of [Undertell archive2](../maps/undertell_archive2.md) visibly changes.</span> | walking into a blocked passage on [undertell_archive2](../maps/undertell_archive2.md) | – | gives 1× [Crown of studied defiance](../items/undertell_lgd_headgear.md) |
| <span id="stage-88"></span>88 | 88 = Galmore_58 barricades removed. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-89"></span>89 | 89 = PC has talked to Vaelzahr about Oegyth crystals. | [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) | carry 1× [oegyth_crystal](../items/oegyth_crystal.md) | – |
| <span id="stage-90"></span>90 | about_a_girl1 runs away from PC on map under_3_12<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell 3 12](../maps/undertell_3_12.md).</span> | [Terrified teenager](../monsters/about_a_girl1.md) ([undertell_3_12](../maps/undertell_3_12.md))<br>stepping on a trigger on [undertell_3_12](../maps/undertell_3_12.md) | – | removes monsters from undertell_3_12<br>spawns monsters on undertell_3_12 |
| <span id="stage-95"></span>95 | PC met a hungry campanite. | [Tocsin](../monsters/tocsin.md) ([undertell_4_00](../maps/undertell_4_00.md)) | carry 1× [Rotten meat](../items/meat2.md) | – |
| <span id="stage-100"></span>100 | The PC learned from an Undertell ghost that during the Rise of the Shadow, a cult of descendants of Kazaul priests calling themselves the Shadow, used hearsteel weapons to defeat the  Elytharan mages. | [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md)) | wearing [#heartsteel_filter](../items/#heartsteel_filter.md) | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 3: 1 route"

    1. walking into a blocked passage on [galmore_58](../maps/galmore_58.md) → the conversation leads here automatically → **stage 3**. NPC: “You can't proceed any further with these barricades in your way. Maybe there's a way to remove them?”

???+ note "Stage 5: 4 routes"

    1. Talk to [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)) → choose “"Our"? There's more of you bosses?” — **conditions:** NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5) → **stage 5**. NPC: “We are "masters", not "bosses". And yes, there are five of us.”
    2. Talk to [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) → choose “"Our"? There's more of you bosses?” — **conditions:** NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5) → **stage 5**. NPC: “We are "masters", not "bosses". And yes, there are five of us.”
    3. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → choose “"Our"? There's more of you bosses?” — **conditions:** NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5) → **stage 5**. NPC: “We are "masters", not "bosses". And yes, there are five of us.”
    4. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → choose “"Our"? There's more of you bosses?” — **conditions:** NOT reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5) → **stage 5**. NPC: “We are "masters", not "bosses". And yes, there are five of us.”

???+ note "Stage 7: 4 routes"

    1. Talk to [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 7**; also sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”
    2. Talk to [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 7**; also sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”
    3. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 7**; also sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”
    4. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → choose “Then I will take it to the shrine.” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md); hand over 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 7**; also sets stage 80 of [The fifth master](../quests/fifth_master.md#stage-80), spawns monsters on undertell_5. NPC: “No. Give it to me and I will give it to the kin. You have done what none of the living could. Do not fail now, mortal.…”

???+ note "Stage 8: 1 route"

    1. stepping on a trigger on [undertell_22](../maps/undertell_22.md) → choose “Yes!” — **conditions:** NOT reached stage 8 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-8) → **stage 8**; also gives 1× [Undertell pickaxe](../items/undertell_pickaxe.md). NPC: “Kneeling down, you push aside loose dirt with your fingers, you pick up the pickaxe.”

???+ note "Stage 10: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Yes, at last I found it.” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20); hand over 1× [Heartstone](../items/heartstone.md); NOT carry 1× [Heartstone](../items/heartstone_unrefined.md) → **stage 10**. NPC: “So you truly have it? The heartstone...beautiful and intact. Remarkable. You've done what few would dare. Can you see…”

???+ note "Stage 15: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50) → **stage 15**. NPC: “What do you want, foolish child?”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50) → **stage 15**. NPC: “What do you want, foolish child?”

???+ note "Stage 25: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “What?! I only get one? But how will I decide which one I want?” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100 → **stage 25**. NPC: “Oh, that's easier than you might think. Here, I will show you a list of the items and their capabilities. Then after…”

???+ note "Stage 30: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the claymore.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 30 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-30) → **stage 30**. NPC: “The bellows heave and the dragon's breath draws down into the furnace. I fold the heartstone's cooled core into the…”

???+ note "Stage 31: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the one-handed sword” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 31 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-31) → **stage 31**. NPC: “A one-handed war blade, balanced and quick. Heartsteel will make it sing in your hand and cleave with a will of its own.”

???+ note "Stage 32: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the dagger” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 32 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-32) → **stage 32**. NPC: “I work the heartstone down to a keen edge fit for a dagger. The heartsteel takes to a small shape with a bitter bite.…”

???+ note "Stage 33: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the glaive” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 33 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-33) → **stage 33**. NPC: “A glaive demands balance and spring. I ring the shaft and bind the heartsteel head to it, coaxing a reach that will…”

???+ note "Stage 34: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the greate axe” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 34 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-34) → **stage 34**. NPC: “A great axe needs weight and a true center. I work the heartsteel into a ferocious head, then temper it in the…”

???+ note "Stage 35: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the hand axe” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 35 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-35) → **stage 35**. NPC: “The hand axe will be compact and reliable. I shape the edge and set the haft so it fits your grip like a second thought.”

???+ note "Stage 36: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the mace” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 36 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-36) → **stage 36**. NPC: “A mace it is. I imbue the head to carry both blunt force and uncanny true weight. This will crush bone and resolve…”

???+ note "Stage 37: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the parrying weapon” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 37 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-37) → **stage 37**. NPC: “A parrying weapon it is. This will hinder your attacker's weapon.”

???+ note "Stage 38: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Yeah, I'm sure. Thanks anyway.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 25 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-25); NOT reached stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39) → **stage 38**; also sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200). NPC: “Okay.”

???+ note "Stage 39: 9 routes"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the parrying weapon” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 37 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-37) → **stage 39**. NPC: “A parrying weapon it is. This will hinder your attacker's weapon.”
    2. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the claymore.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 30 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-30) → **stage 39**. NPC: “The bellows heave and the dragon's breath draws down into the furnace. I fold the heartstone's cooled core into the…”
    3. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the dagger” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 32 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-32) → **stage 39**. NPC: “I work the heartstone down to a keen edge fit for a dagger. The heartsteel takes to a small shape with a bitter bite.…”
    4. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the glaive” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 33 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-33) → **stage 39**. NPC: “A glaive demands balance and spring. I ring the shaft and bind the heartsteel head to it, coaxing a reach that will…”
    5. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the greate axe” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 34 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-34) → **stage 39**. NPC: “A great axe needs weight and a true center. I work the heartsteel into a ferocious head, then temper it in the…”
    6. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the hand axe” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 35 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-35) → **stage 39**. NPC: “The hand axe will be compact and reliable. I shape the edge and set the haft so it fits your grip like a second thought.”
    7. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the mace” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 36 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-36) → **stage 39**. NPC: “A mace it is. I imbue the head to carry both blunt force and uncanny true weight. This will crush bone and resolve…”
    8. Talk to [Nocmar](../monsters/nocmar.md) → choose “Yeah, I'm sure. Thanks anyway.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 25 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-25); NOT reached stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39) → **stage 39**; also sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200). NPC: “Okay.”
    9. Talk to [Nocmar](../monsters/nocmar.md) → choose “I chose the one-handed sword” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 31 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-31) → **stage 39**. NPC: “A one-handed war blade, balanced and quick. Heartsteel will make it sing in your hand and cleave with a will of its own.”

???+ note "Stage 45: 1 route"

    1. stepping on a trigger on [white_house](../maps/white_house.md) → the conversation leads here automatically → **stage 45**

???+ note "Stage 50: 3 routes"

    1. walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md) → choose “I will not wake you. I only wanted to see.” → **stage 50**. NPC: “The dragon settles, and the warm hush returns. Its breath is a slow tide through the stone vents. The glow above you…”
    2. stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) → choose “I will not wake you. I only wanted to see.” — **conditions:** reached stage 45 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-45); NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50) → **stage 50**. NPC: “The dragon settles, and the warm hush returns. Its breath is a slow tide through the stone vents. The glow above you…”
    3. Talk to [Lethgar miner ghost](../monsters/lethgar_miner_ghost2.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “Then maybe the legend was real.” — **conditions:** latest stage of [The fifth master](../quests/fifth_master.md#stage-65) is 65; NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50); carry 1× [Ash covered dragon scales](../items/ancient_dragon_scales.md) → **stage 50**. NPC: “If he still lives, child, best let him sleep. Some fires burn long after they should have gone out.”

???+ note "Stage 55: 1 route"

    1. Talk to [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) → choose “Shannal sent me.” — **conditions:** reached stage 55 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-55); NOT reached stage 130 of [You shall pass](../quests/undertell_barricades.md#stage-130); have 5,000 gold → **stage 55**. NPC: “Shannal? That name sounds familiar to me, yet distant to me.”

???+ note "Stage 60: 1 route"

    1. Talk to [Rock eater](../monsters/rock_eater.md) ([undertell_exit](../maps/undertell_exit.md)) → choose “Here, I have it. Take it.” — **conditions:** reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2); hand over 1× [Nixite crystal](../items/nixite_crystal.md) → **stage 60**; also removes monsters from undertell_exit, spawns monsters on undertell_exit. NPC: “Wonderful! Now move along before I change my mind.”

???+ note "Stage 65: 1 route"

    1. walking into a blocked passage on [undertell_5](../maps/undertell_5.md) → choose “Yes.” → **stage 65**; also faction “undertellIsland” set to 0

???+ note "Stage 66: 1 route"

    1. walking into a blocked passage on [undertell_4_01](../maps/undertell_4_01.md) → choose “Yes.” → **stage 66**; also faction “undertellIsland” set to 1

???+ note "Stage 70: 1 route"

    1. walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md) → choose “Hello?” — **conditions:** reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); NOT reached stage 70 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-70) → **stage 70**; also removes monsters from undertell_1_1. NPC: “[Talking to yourself...]”

???+ note "Stage 75: 1 route"

    1. stepping on a trigger on [undertell_01](../maps/undertell_01.md) → the conversation leads here automatically — **conditions:** reached stage 70 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-70); NOT reached stage 75 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-75) → **stage 75**; also spawns monsters on undertell_1_1

???+ note "Stage 78: 1 route"

    1. stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 86 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-86) → **stage 78**; also applies condition kazaul_mortality, applies condition burning, applies condition kazarite_misery. NPC: “You step into a chamber where nothing is displayed for reverence. Every object is placed as if awaiting judgment. The…”

???+ note "Stage 80: 1 route"

    1. Talk to [Lethgar slave ghost](../monsters/lethgar_female_ghost.md) ([undertell_1_1](../maps/undertell_1_1.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 80 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-80) → **stage 80**. NPC: “She reaches out and pinches your arm to confirm that you are in fact human.”

???+ note "Stage 81: 1 route"

    1. stepping on a trigger on [undertell_1_0](../maps/undertell_1_0.md) → the conversation leads here automatically — **conditions:** NOT reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81) → **stage 81**

???+ note "Stage 82: 1 route"

    1. Talk to [Lethgar slave ghost](../monsters/lethgar_female_ghost.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “I would really like to rest here now.” — **conditions:** reached stage 450 of [hidden_devotion (hidden flag)](../quests/hidden_devotion.md#stage-450); reached stage 81 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-81) → **stage 82**. NPC: “The Kha'zaan are no more, thanks to you. So yes, you are free to sleep in any of the desirable beds.”

???+ note "Stage 83: 1 route"

    1. walking into a blocked passage on [undertell_00](../maps/undertell_00.md) → choose “Of course I do. I'm poor and really need these coins.” — **conditions:** NOT reached stage 83 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-83); reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5) → **stage 83**; also gives 2100× [Gold coins](../items/gold.md). NPC: “While stuffing the gold into your coin purse, you try counting the coins..twenty-one hundred coins!”

???+ note "Stage 84: 1 route"

    1. walking into a blocked passage on [undertell_3_02](../maps/undertell_3_02.md) → choose “You bet I do! I will take the risk and steal these babies.” — **conditions:** NOT reached stage 84 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-84) → **stage 84**; also gives 1× [Rare coins](../items/rare_coins.md). NPC: “You reach into the crate. The coins slide together with a familiar sound.”

???+ note "Stage 85: 1 route"

    1. walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) → choose “[Toss the talisman to her.]” — **conditions:** reached stage 70 of [About a girl](../quests/about_a_girl.md#stage-70); NOT reached stage 80 of [About a girl](../quests/about_a_girl.md#stage-80); carry 1× [Folded copper talisman](../items/folded_copper_talisman.md); hand over 1× [Folded copper talisman](../items/folded_copper_talisman.md) → **stage 85**. NPC: “She fumbles, then grips it tightly. Her breathing slows.”

???+ note "Stage 86: 1 route"

    1. stepping on a trigger on [undertell_archive2](../maps/undertell_archive2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 86 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-86) → **stage 86**; also applies condition kazaul_mortality, applies condition burning, applies condition kazarite_misery. NPC: “You step into a chamber where nothing is displayed for reverence. Every object is placed as if awaiting judgment. The…”

???+ note "Stage 87: 1 route"

    1. walking into a blocked passage on [undertell_archive2](../maps/undertell_archive2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 87 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-87) → **stage 87**; also gives 1× [Crown of studied defiance](../items/undertell_lgd_headgear.md). NPC: “As you lift the crown from the table, the space around it feels suddenly incomplete, as though the room was arranged…”

???+ note "Stage 89: 1 route"

    1. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → choose “So this crystal is a tool?” — **conditions:** carry 1× [oegyth_crystal](../items/oegyth_crystal.md) → **stage 89**. NPC: “We no longer shape the world so openly. But what was shaped does not forget the hand that shaped it.”

???+ note "Stage 90: 2 routes"

    1. Talk to [Terrified teenager](../monsters/about_a_girl1.md) ([undertell_3_12](../maps/undertell_3_12.md)) → choose “What is wrong?” → **stage 90**; also removes monsters from undertell_3_12, spawns monsters on undertell_3_12. NPC: “STAY AWAY FROM ME!”
    2. stepping on a trigger on [undertell_3_12](../maps/undertell_3_12.md) → choose “What is wrong?” — **conditions:** reached stage 40 of [About a girl](../quests/about_a_girl.md#stage-40); NOT reached stage 70 of [About a girl](../quests/about_a_girl.md#stage-70); NOT reached stage 90 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-90) → **stage 90**; also removes monsters from undertell_3_12, spawns monsters on undertell_3_12. NPC: “STAY AWAY FROM ME!”

???+ note "Stage 95: 1 route"

    1. Talk to [Tocsin](../monsters/tocsin.md) ([undertell_4_00](../maps/undertell_4_00.md)) → the conversation leads here automatically — **conditions:** carry 1× [Rotten meat](../items/meat2.md); NOT reached stage 50 of [About a girl](../quests/about_a_girl.md#stage-50) → **stage 95**. NPC: “The creature lunges forward...you pull back moments before it clamps onto your hand!”

???+ note "Stage 100: 1 route"

    1. Talk to [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md)) → choose “Executioner's tool?” — **conditions:** wearing [#heartsteel_filter](../items/#heartsteel_filter.md) → **stage 100**. NPC: “When the Shadow rose, many who came for the Elytharans carried heartsteel. It cut through armor with frightening ease,…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 44 lines added, 1 line changed<br>· text: “By the Shadow. You actually found a heartstone. I thought I wouldn't …” → “So you truly have it? The heartstone...beautiful and intact. Remarkab…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `undertell_hidden` |
    | showInLog | 0 |
    | Stage IDs | 3, 5, 7, 8, 10, 15, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 45, 50, 55, 60, 65, 66, 70, 75, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 100 |
    | Dialogue nodes setting stages | 3: `undertell_barricade_key_message`, 5: `kazaul_masters_not_met_20`, 7: `masters_send_to_thalen_20`, 7: `thalen_receives_ritual_30`, 8: `undertell_22_axe_20`, 10: `nocmar_complete`, 15: `talk_about_white_house_20`, 25: `nocmar_forge_one_item_20`, 30: `nocmar_claymore_10`, 31: `nocmar_onehanded_10`, 32: `nocmar_dagger_10`, 33: `nocmar_glaive_10`, 34: `nocmar_greateaxe_10`, 35: `nocmar_handaxe_10`, 36: `nocmar_mace_10`, 37: `nocmar_bladeBreaker_10`, 38: `nocmar_no_weapon_15`, 39: `nocmar_bladeBreaker_10`, 39: `nocmar_claymore_10`, 39: `nocmar_dagger_10`, 45: `white_house_going_downstairs`, 50: `dragon_leave`, 50: `lethgar_miner_ghost2_dragon_50`, 55: `fallhaven_drunk_potion_30`, 60: `rock_eater_pc_give_nixite_10`, 65: `undertell5_leave_confirmed`, 66: `undertell5_lof_confirmed`, 70: `cora_pit_yell_20`, 75: `undertell_put_cora_back_10`, 78: `undertell_archival_10`, 80: `lethgar_female_ghost_pinch_10`, 81: `undertell_player_seen_beds_reward`, 82: `lethgar_female_ghost_rest_yes`, 83: `undertell_00_chest_loot`, 84: `undertell_3_02_looting_chest_10`, 85: `about_girl_meet_50`, 86: `undertell_archival_10`, 87: `undertell_crown_take_20`, 89: `master_oegyth_50`, 90: `about_girl_scream_20`, 95: `tocsin_rotten_20`, 100: `brenor_heartsteel_30` |
    | Dialogue nodes clearing stages | 87: `passive_achievement_check_remove_hidden_quest_step`, 87: `undertell_crown_put_back_20`, 86: `porter_player_does_not_have_crown_10`, 65: `undertell5_enter_yes`, 66: `undertell5_exit_yes`, 45: `white_house_basement_down_10`, 45: `white_house_basement_voice` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
