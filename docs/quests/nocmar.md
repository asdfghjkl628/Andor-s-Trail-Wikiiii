# Lost treasures

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `nocmar` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 200) |
| **Started by** | [Unnmir](../monsters/unnmir.md) |
| **NPCs involved** | [Myrelis](../monsters/mg_myrelis.md), [Nocmar](../monsters/nocmar.md), [Unnmir](../monsters/unnmir.md) |
| **Locations** | [galmore_58](../maps/galmore_58.md) |
| **Total XP** | 10,036 |
| **Related quests** | 5 |

</div>

!!! history "Version note"
    From v0.7.0 to v0.8.17, this quest could not be completed: its final step needed Heartstone, which could not be obtained anywhere. It became completable in [v0.8.18](../versions/0.8.18.md).

## Overview

> Unnmir told me he used to be an adventurer, and gave me a hint to go see Nocmar. His house is just southwest of the tavern in Fallhaven.

## Prerequisites to start

Start with [Unnmir](../monsters/unnmir.md). Required:

- reached stage 100 of [Drunken tale](../quests/fallhavendrunk.md#stage-100)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Drunken tale](fallhavendrunk.md#stage-100) | stage 100 reached, for stage 10 here |
| Requires | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-9) | stage 9 reached, for stage 35 here |
| Requires | [A place to forge](place_to_forge.md#stage-60) | stage 60 reached, for stage 90 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-3) | stage 3 reached, for stage 35 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-10) | stage 10 reached, for stage 80 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-25) | stage 25 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-30) | stage 30 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-31) | stage 31 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-32) | stage 32 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-33) | stage 33 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-34) | stage 34 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-35) | stage 35 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-36) | stage 36 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-37) | stage 37 reached, for stage 200 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-38) | stage 38 reached, for stage 110 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-45) | stage 45 reached, for stage 110 here |
| Mutually exclusive | [A place to forge](place_to_forge.md#stage-60) | stage 60 must NOT be reached, for stages 20, 30, 48, 80 here |
| Mutually exclusive | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-39) | stage 39 must NOT be reached, for stage 200 here |
| Mutually exclusive | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-50) | stage 50 must NOT be reached, for stage 110 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-10) | stage 10 there needs stages 10, 80 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-20) | stage 20 there needs stages 10, 80 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-60) | stage 60 there needs stages 10, 80 here |
| Unlocks | [You shall pass](undertell_barricades.md#stage-10) | stage 10 there needs stage 35 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-10) | stage 10 there needs stages 10, 20 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-25) | stage 25 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-30) | stage 30 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-31) | stage 31 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-32) | stage 32 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-33) | stage 33 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-34) | stage 34 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-35) | stage 35 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-36) | stage 36 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-37) | stage 37 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-38) | stage 38 there needs stage 100 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-39) | stage 39 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Unnmir told me he used to be an adventurer, and gave me a hint to go see Nocmar. His house is just southwest of the tavern in Fallhaven. | [Unnmir](../monsters/unnmir.md) | – | – |
| <span id="stage-20"></span>20 | Nocmar tells me he used to be a smith. But Lord Geomyr has banned the use of heartsteel, so he cannot forge his weapons anymore. If I can find a heartstone and bring it to Nocmar, he should be able to forge the heartsteel again. | [Nocmar](../monsters/nocmar.md) | stage 10 | – |
| <span id="stage-30"></span>30 | Nocmar, the Fallhaven smith, said that I could find a heartstone in a place called Undertell which is somewhere near Galmore Mountain. | [Nocmar](../monsters/nocmar.md) | stage 10, stage 20 | – |
| <span id="stage-35"></span>35 | Myrelis, the ghost artist I met in the Galmore encampment, informed me that the entrance to Undertell is located just southwest of his building. | [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) | stage 20, stage 30 | – |
| <span id="stage-40"></span>40 | I discovered the heartstone deep inside Undertell, but it was far too hot to move or even touch. Maybe Unnmir knows what I should do next? | walking into a blocked passage on [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | – | – |
| <span id="stage-45"></span>45 | I discovered a heartstone deep inside Undertell. It's time to put Nocmar to work.<br><span class="qnote">🗺️ Part of [Undertell 10](../maps/undertell_10.md) visibly changes.</span> | walking into a blocked passage on [undertell_10](../maps/undertell_10.md) | – | gives 1× [Heartstone](../items/heartstone_unrefined.md) |
| <span id="stage-48"></span>48 | Nocmar informed me that I must return the unrefined heartstone back to where I found it so it could "become whole".<br><span class="qnote">🔒 An area on [Undertell 10](../maps/undertell_10.md) becomes blocked off.</span> | [Nocmar](../monsters/nocmar.md) | carry 1× [Heartstone](../items/heartstone.md), carry 1× [Heartstone](../items/heartstone_unrefined.md), stage 10, stage 20 | – |
| <span id="stage-50"></span>50 | Unnmir told me that the only way to cool the heartstone enough to carry it is to use a block of Galmore ice which he said I could find at the top of Galmore Mountain guarded by the snow beasts. This rare ice does not melt in the lowlands, only when placed against something extremely hot like lava or the heartstone itself. | [Unnmir](../monsters/unnmir.md) | stage 40 | – |
| <span id="stage-60"></span>60 | I was spooked by a sound causing me to lose my grip on the unrefined heartstone, causing me to drop it. Thus shattering it into pieces.<br><span class="qnote">🗺️ Part of [Undertell 10](../maps/undertell_10.md) visibly changes.</span> | walking into a blocked passage on [undertell_10](../maps/undertell_10.md) | carry 1× [Heartstone](../items/heartstone_unrefined.md), hand over 1× [Heartstone](../items/heartstone_unrefined.md) | applies condition fear |
| <span id="stage-70"></span>70 | I placed the Galmore ice on the heartstone. The block hissed and steamed as it melted away, cooling the heartstone until it was safe to touch. I picked it up at last.<br><span class="qnote">🗺️ Part of [Undertell 3 lava 01](../maps/undertell_3_lava_01.md) visibly changes.</span> | walking into a blocked passage on [undertell_3_lava_01](../maps/undertell_3_lava_01.md) | hand over 1× [Galmore ice](../items/galmore_ice.md), stage 50 | gives 1× [Heartstone](../items/heartstone.md) |
| <span id="stage-80"></span>80 | I returned to Nocmar with the cooled heartstone. He was eager to begin his work, but... not in his Fallhaven shop. | [Nocmar](../monsters/nocmar.md) | stage 10, stage 20 | – |
| <span id="stage-90"></span>90 | Nocmar told me to meet him at the glowing white house south of Fallhaven. He says the lock will no longer bar my entry, as he must prepare the forge and make sure the place is safe.<br><span class="qnote">⚡ A scripted event can now trigger on [Gapfiller2](../maps/gapfiller2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Gapfiller2](../maps/gapfiller2.md).</span> | [Nocmar](../monsters/nocmar.md) | – | removes monsters from fallhaven_nocmar |
| <span id="stage-100"></span>100 | I met Nocmar inside the glowing white house, where the ever-burning forge waits. He explained that with the heartstone I recovered, he can forge one heartsteel weapon of my choice. | [Nocmar](../monsters/nocmar.md) | stage 90 | – |
| <span id="stage-110"></span>110 | As I refused a heartsteel weapon from Nocmar, Falkour, the forge dragon beneath the glowing house, gifted me a pendant.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house basement](../maps/white_house_basement.md).</span> | walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md)<br>stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) | – | gives 1× [Heartfire pendant of Kazaul](../items/heartfire_pendant.md) |
| <span id="stage-200"></span>200 | Nocmar forged the heartsteel once again and rewarded me with a weapon type of my choice, reforged in the lost art. **(completes quest)**<br><span class="qnote">🔒 An area on [White house basement](../maps/white_house_basement.md) becomes blocked off.</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [White house](../maps/white_house.md).</span> | [Nocmar](../monsters/nocmar.md) | stage 100 | 10,036 XP<br>gives 1× [Heartsteel blade breaker](../items/heartstone_blade_breaker.md)<br>gives 1× [Heartsteel claymore](../items/heartstone_2h_sword.md)<br>gives 1× [Heartsteel dagger](../items/heartstone_dagger.md)<br>gives 1× [Heartsteel trident](../items/heartstone_glaive.md)<br>gives 1× [Heartsteel greataxe](../items/heartstone_greataxe.md)<br>gives 1× [Heartsteel handaxe](../items/heartstone_handaxe.md)<br>gives 1× [Heartsteel mace](../items/heartstone_mace.md)<br>sets stage 38 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-38)<br>sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)<br>gives 1× [Heartsteel warblade](../items/heartstone_1h_sword.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Unnmir](../monsters/unnmir.md) → choose “Yes” — **conditions:** reached stage 100 of [Drunken tale](../quests/fallhavendrunk.md#stage-100) → **stage 10**. NPC: “Nice. I'll give you a hint, kid. *snickering* Go see Nocmar over by the west side of town. Tell him I sent you.”

???+ note "Stage 20: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Unnmir sent me.” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60) → **stage 20**. NPC: “Unnmir sent you huh? I guess it must be important then.”

???+ note "Stage 30: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Undertell? Is that where I could find a heartstone?” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20) → **stage 30**. NPC: “Undertell; the pits of the lost souls. Travel south to the devastated wastelands of Galmore Mountain and follow the…”

???+ note "Stage 35: 2 routes"

    1. Talk to [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) → choose “I'm looking for some place called "Undertell", do you know where it is?” — **conditions:** reached stage 9 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-9); latest stage of [Lost treasures](../quests/nocmar.md#stage-30) is 30 → **stage 35**. NPC: “Over there, but it looks like it's blocked.”
    2. Talk to [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) → choose “I was wondering, why are those barricades there? [pointing southwest]” — **conditions:** reached stage 9 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-9); latest stage of [Lost treasures](../quests/nocmar.md#stage-20) is 20; reached stage 3 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-3) → **stage 35**. NPC: “[With a terrified expression on his face] Oh those? Yeah, you don't want to go past those. Past them is the entrance…”

???+ note "Stage 40: 1 route"

    1. walking into a blocked passage on [undertell_3_lava_01](../maps/undertell_3_lava_01.md) → the conversation leads here automatically — **conditions:** NOT reached stage 70 of [Lost treasures](../quests/nocmar.md#stage-70) → **stage 40**. NPC: “This heartstone radiates unbearable heat, glowing faintly with the breath of the Rift itself. The surface scorches at…”

???+ note "Stage 45: 1 route"

    1. walking into a blocked passage on [undertell_10](../maps/undertell_10.md) → the conversation leads here automatically — **conditions:** NOT reached stage 40 of [Lost treasures](../quests/nocmar.md#stage-40); NOT reached stage 45 of [Lost treasures](../quests/nocmar.md#stage-45) → **stage 45**; also gives 1× [Heartstone](../items/heartstone_unrefined.md). NPC: “Its size and presence leave little doubt - this must be what you came for.”

???+ note "Stage 48: 2 routes"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Actually, I found two. [extend your hands, one stone in each]” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20); carry 1× [Heartstone](../items/heartstone_unrefined.md); carry 1× [Heartstone](../items/heartstone.md) → **stage 48**. NPC: “Return it back where you found it, it will continue drawing heat and pressure from the Rift, hardening over years. But…”
    2. Talk to [Nocmar](../monsters/nocmar.md) → choose “Yes, at last I found it.” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20); carry 1× [Heartstone](../items/heartstone_unrefined.md); NOT carry 1× [Heartstone](../items/heartstone.md) → **stage 48**. NPC: “Well, I can tell from here that it is unrefined. Still forming. No heartsteel can be forged from this. If you tried,…”

???+ note "Stage 50: 1 route"

    1. Talk to [Unnmir](../monsters/unnmir.md) → choose “Yes and I am really hoping that you can help me! I found the heartstone, but it burns to the touch. I cannot…” — **conditions:** reached stage 40 of [Lost treasures](../quests/nocmar.md#stage-40); NOT reached stage 50 of [Lost treasures](../quests/nocmar.md#stage-50) → **stage 50**. NPC: “Climbing to that height is no small task, and the beasts there guard it jealously. But if you truly want to see…”

???+ note "Stage 60: 1 route"

    1. walking into a blocked passage on [undertell_10](../maps/undertell_10.md) → the conversation leads here automatically — **conditions:** carry 1× [Heartstone](../items/heartstone_unrefined.md); hand over 1× [Heartstone](../items/heartstone_unrefined.md) → **stage 60**; also applies condition fear. NPC: “You flinch and the heartstone slips from your hands and shatters across the ground.”

???+ note "Stage 70: 1 route"

    1. walking into a blocked passage on [undertell_3_lava_01](../maps/undertell_3_lava_01.md) → choose “OK, it's time to see if Unnmir is right! [place the block of Galmore ice on the stone]” — **conditions:** NOT reached stage 70 of [Lost treasures](../quests/nocmar.md#stage-70); reached stage 50 of [Lost treasures](../quests/nocmar.md#stage-50); hand over 1× [Galmore ice](../items/galmore_ice.md) → **stage 70**; also gives 1× [Heartstone](../items/heartstone.md). NPC: “You set the block of Galmore ice onto the blazing heartstone. At once, a violent hiss erupts, filling the chamber with…”

???+ note "Stage 80: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Oh, no!” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20); reached stage 10 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-10) → **stage 80**. NPC: “But no, I cannot work it here. Too many eyes, too many whispers. If I were caught forging heartsteel in this shop, it…”

???+ note "Stage 90: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “What will you do now?” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60) → **stage 90**; also removes monsters from fallhaven_nocmar. NPC: “Meet me at the white house south of town. The lock will no longer bar your entry. I must prepare the forge and make…”

???+ note "Stage 100: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “That explains the glow under the door?” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-90) is 90; NOT reached stage 100 of [Lost treasures](../quests/nocmar.md#stage-100) → **stage 100**. NPC: “Now, you brought one cooled heartstone. We can forge only one item from it.”

???+ note "Stage 110: 2 routes"

    1. walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md) → choose “I chose not to have a weapon forged.” — **conditions:** reached stage 38 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-38); NOT reached stage 110 of [Lost treasures](../quests/nocmar.md#stage-110) → **stage 110**; also gives 1× [Heartfire pendant of Kazaul](../items/heartfire_pendant.md). NPC: “The dragon lowers a claw and nudges a small trinket toward you. It gleams faintly, warm but not burning. Take it, and…”
    2. stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) → choose “I chose not to have a weapon forged.” — **conditions:** reached stage 45 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-45); NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50); reached stage 38 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-38); NOT reached stage 110 of [Lost treasures](../quests/nocmar.md#stage-110) → **stage 110**; also gives 1× [Heartfire pendant of Kazaul](../items/heartfire_pendant.md). NPC: “The dragon lowers a claw and nudges a small trinket toward you. It gleams faintly, warm but not burning. Take it, and…”

???+ note "Stage 200: 9 routes"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Carry on.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 37 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-37) → **stage 200**; also gives 1× [Heartsteel blade breaker](../items/heartstone_blade_breaker.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    2. Talk to [Nocmar](../monsters/nocmar.md) → choose “I will wait.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 30 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-30) → **stage 200**; also gives 1× [Heartsteel claymore](../items/heartstone_2h_sword.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it. And…”
    3. Talk to [Nocmar](../monsters/nocmar.md) → choose “Very well.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 32 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-32) → **stage 200**; also gives 1× [Heartsteel dagger](../items/heartstone_dagger.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    4. Talk to [Nocmar](../monsters/nocmar.md) → choose “Proceed.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 33 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-33) → **stage 200**; also gives 1× [Heartsteel trident](../items/heartstone_glaive.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    5. Talk to [Nocmar](../monsters/nocmar.md) → choose “Do it.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 34 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-34) → **stage 200**; also gives 1× [Heartsteel greataxe](../items/heartstone_greataxe.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    6. Talk to [Nocmar](../monsters/nocmar.md) → choose “Good.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 35 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-35) → **stage 200**; also gives 1× [Heartsteel handaxe](../items/heartstone_handaxe.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    7. Talk to [Nocmar](../monsters/nocmar.md) → choose “Carry on.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 36 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-36) → **stage 200**; also gives 1× [Heartsteel mace](../items/heartstone_mace.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”
    8. Talk to [Nocmar](../monsters/nocmar.md) → choose “Yeah, I'm sure. Thanks anyway.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 25 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-25); NOT reached stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39) → **stage 200**; also sets stage 38 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-38), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39). NPC: “Okay.”
    9. Talk to [Nocmar](../monsters/nocmar.md) → choose “Make it so.” — **conditions:** latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100; reached stage 31 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-31) → **stage 200**; also gives 1× [Heartsteel warblade](../items/heartstone_1h_sword.md). NPC: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

**Completability:** From v0.7.0 to v0.8.17, this quest could not be completed: its final step needed Heartstone, which could not be obtained anywhere. It became completable in [v0.8.18](../versions/0.8.18.md).

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Nice. I'll give you a hint, kid. *snickering*. Go see Nocmar over by …” → “Nice. I'll give you a hint, kid. *snickering* Go see Nocmar over by t…” |
| [v0.8.5](../versions/0.8.5.md) | stage 20 journal text changed |
| [v0.8.14](../versions/0.8.14.md) | stages added: 30, 35; stage 20 journal text changed<br>Dialogue: 2 lines added |
| [v0.8.18](../versions/0.8.18.md) | stages added: 40, 45, 48, 50, 60, 70, 80, 90, 100, 110; stage 30 journal text changed; stage 35 journal text changed; stage 200 journal text changed; stage 200 XP 1200 → 10036<br>Dialogue: 21 lines added, 2 lines changed<br>· text: “Quick. Let's get these old heartsteel weapons glowing again.” → “But no, I cannot work it here. Too many eyes, too many whispers. If I…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nocmar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nocmar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nocmar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nocmar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nocmar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `nocmar` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 45, 48, 50, 60, 70, 80, 90, 100, 110, 200 |
    | Dialogue nodes setting stages | 10: `unnmir_11`, 20: `nocmar_quest`, 30: `nocmar_quest_4a`, 35: `mg_myrelis_undertell_30`, 35: `mg_myrelis_barricades_10`, 40: `heartstone_discovery_10`, 45: `unrefined_heartstone_discovery_20`, 48: `nocmar_two_stones_11`, 48: `nocmar_unrefined_stone_10`, 50: `unnmir_hs_30`, 60: `unrefined_heartstone_return_20`, 70: `heartstone_ice_10`, 80: `nocmar_complete_3`, 90: `nocmar_deed_receive_10`, 100: `nocmar_dragon_reveal_20`, 110: `dragon_give_token_10`, 200: `nocmar_bladeBreaker_20`, 200: `nocmar_claymore_20`, 200: `nocmar_dagger_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
