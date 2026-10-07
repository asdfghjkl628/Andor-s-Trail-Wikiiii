# Fungi Panic - non displayed

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fungi_panic_nondisplayed` |
| **In journal** | No (hidden flag) |
| **Stages** | 9 |
| **Started by** | stepping on a trigger on [mushroom_m3_1](../maps/mushroom_m3_1.md) |
| **NPCs involved** | [Undina Bogsten](../monsters/bogsten_granny1.md), [Undina Bogsten](../monsters/bogsten_granny.md) |
| **Locations** | [mushroom_m2_4](../maps/mushroom_m2_4.md) |

</div>

## Overview

> 10=Chains.

## Prerequisites to start

None: talk to stepping on a trigger on [mushroom_m3_1](../maps/mushroom_m3_1.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | 10=Chains.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mushroom m3 1](../maps/mushroom_m3_1.md).</span><br><span class="qnote">🔒 An area on [Mushroom m3 1](../maps/mushroom_m3_1.md) becomes blocked off.</span> | stepping on a trigger on [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | starts timer “mushroom_m3_1_chains”<br>applies condition fear |
| <span id="stage-20"></span>20 | 20=Algore grave<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Woodsettlement0](../maps/woodsettlement0.md).</span><br><span class="qnote">🗺️ Part of [Woodsettlement0](../maps/woodsettlement0.md) visibly changes.</span> | stepping on a trigger on [woodsettlement0](../maps/woodsettlement0.md) | – | – |
| <span id="stage-35"></span>35 | 35=I opened Bogsten's backyard door.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bogsten1](../maps/bogsten1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Bogsten1](../maps/bogsten1.md).</span> | stepping on a trigger on [bogsten1](../maps/bogsten1.md) | hand over 1× [Bogsten's key](../items/bogsten_key.md) | – |
| <span id="stage-60"></span>60 | 60=Cave wall open<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bogsten3](../maps/bogsten3.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bogsten4](../maps/bogsten4.md).</span><br><span class="qnote">🗺️ Part of [Bogsten3](../maps/bogsten3.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Bogsten4](../maps/bogsten4.md) visibly changes.</span> | stepping on a trigger on [bogsten3](../maps/bogsten3.md) | wearing [Bogsten's necklace](../items/bogsten_necklace.md) | – |
| <span id="stage-90"></span>90 | 90=killed fungi<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mushroom m3 2](../maps/mushroom_m3_2.md).</span> | stepping on a trigger on [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | spawns monsters on mushroom_m3_2 |
| <span id="stage-100"></span>100 | 100=Granny despawn.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mushroom m2 4](../maps/mushroom_m2_4.md).</span> | stepping on a trigger on [mushroom_m2_4](../maps/mushroom_m2_4.md) | – | removes monsters from mushroom_m2_4 |
| <span id="stage-110"></span>110 | 110=Gardener gloves worn<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain32](../maps/blackwater_mountain32.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gapfiller2](../maps/gapfiller2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 11](../maps/guynmart_wood_11.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lodar19](../maps/lodar19.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lodar21](../maps/lodar21.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake7](../maps/mountainlake7.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Way to sullengard east8](../maps/way_to_sullengard_east8.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytolake10](../maps/waytolake10.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild9](../maps/wild9.md).</span> | stepping on a trigger on [blackwater_mountain32](../maps/blackwater_mountain32.md) | wearing [Gardener's gloves](../items/gardener_gloves.md) | spawns monsters on gapfiller2<br>spawns monsters on wild9<br>spawns monsters on guynmart_wood_8<br>spawns monsters on guynmart_wood_10<br>spawns monsters on guynmart_wood_11<br>spawns monsters on blackwater_mountain32<br>spawns monsters on waytolake10<br>spawns monsters on waytolake11<br>spawns monsters on lodar19<br>spawns monsters on lodar21<br>spawns monsters on mountainlake7<br>spawns monsters on mountainlake8<br>spawns monsters on way_to_sullengard_east7<br>spawns monsters on way_to_sullengard_east8 |
| <span id="stage-200"></span>200 | Bogsten's grand grand grandmother invited me to their family tomb.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Mushroom m2 4](../maps/mushroom_m2_4.md).</span><br><span class="qnote">🗺️ Part of [Mushroom m2 4](../maps/mushroom_m2_4.md) visibly changes.</span> | [Undina Bogsten](../monsters/bogsten_granny.md) ([mushroom_m2_4](../maps/mushroom_m2_4.md)) | – | removes monsters from mushroom_m2_4<br>spawns monsters on mushroom_m2_4 |
| <span id="stage-210"></span>210 | You found a hidden way downstairs.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mushroom m2 4](../maps/mushroom_m2_4.md).</span><br><span class="qnote">🗺️ Part of [Mushroom m2 4](../maps/mushroom_m2_4.md) visibly changes.</span> | stepping on a trigger on [mushroom_m2_4](../maps/mushroom_m2_4.md) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [mushroom_m3_1](../maps/mushroom_m3_1.md) → the conversation leads here automatically → **stage 10**; also starts timer “mushroom_m3_1_chains”, applies condition fear. NPC: “[You hear a sudden sharp click.] What is this? Help!”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [woodsettlement0](../maps/woodsettlement0.md) → the conversation leads here automatically — **conditions:** killed 1× [Hagale](../monsters/algore.md) → **stage 20**

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [bogsten1](../maps/bogsten1.md) → the conversation leads here automatically — **conditions:** hand over 1× [Bogsten's key](../items/bogsten_key.md) → **stage 35**

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [bogsten3](../maps/bogsten3.md) → the conversation leads here automatically — **conditions:** wearing [Bogsten's necklace](../items/bogsten_necklace.md) → **stage 60**

???+ note "Stage 90: 1 route"

    1. stepping on a trigger on [mushroom_m3_2](../maps/mushroom_m3_2.md) → the conversation leads here automatically — **conditions:** killed 1× [Great fungi](../monsters/boss_fungi.md); NOT reached stage 90 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-90) → **stage 90**; also spawns monsters on mushroom_m3_2, spawns monsters on mushroom_m3_2, spawns monsters on mushroom_m3_2. NPC: “On your final blow, the great mushroom explodes. Suddenly, the mushroom pieces spring back to life!”

???+ note "Stage 100: 1 route"

    1. stepping on a trigger on [mushroom_m2_4](../maps/mushroom_m2_4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 100 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-100) → **stage 100**; also removes monsters from mushroom_m2_4

???+ note "Stage 110: 1 route"

    1. stepping on a trigger on [blackwater_mountain32](../maps/blackwater_mountain32.md) → the conversation leads here automatically — **conditions:** wearing [Gardener's gloves](../items/gardener_gloves.md); NOT reached stage 110 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-110) → **stage 110**; also spawns monsters on gapfiller2, spawns monsters on wild9, spawns monsters on wild9, spawns monsters on guynmart_wood_8, spawns monsters on guynmart_wood_8, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_11, spawns monsters on guynmart_wood_11, spawns monsters on blackwater_mountain32, spawns monsters on blackwater_mountain32, spawns monsters on waytolake10, spawns monsters on waytolake10, spawns monsters on waytolake11, spawns monsters on waytolake11, spawns monsters on lodar19, spawns monsters on lodar19, spawns monsters on lodar21, spawns monsters on lodar21, spawns monsters on mountainlake7, spawns monsters on mountainlake7, spawns monsters on mountainlake8, spawns monsters on way_to_sullengard_east7, spawns monsters on way_to_sullengard_east7, spawns monsters on way_to_sullengard_east7, spawns monsters on way_to_sullengard_east8

???+ note "Stage 200: 1 route"

    1. Talk to [Undina Bogsten](../monsters/bogsten_granny.md) ([mushroom_m2_4](../maps/mushroom_m2_4.md)) → choose “Oh, you don't have to!” → **stage 200**; also removes monsters from mushroom_m2_4, spawns monsters on mushroom_m2_4. NPC: “Go ye into our family tomb. You may pick something from our treasures.”

???+ note "Stage 210: 1 route"

    1. stepping on a trigger on [mushroom_m2_4](../maps/mushroom_m2_4.md) → choose “. . . . . . N” — **conditions:** NOT reached stage 210 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-210); faction “bogsten_tomb_pw” = 3; faction “bogsten_tomb_pw” = 2; faction “bogsten_tomb_pw” = 5; faction “bogsten_tomb_pw” = 1 → **stage 210**. NPC: “The tombstone silently glides back into the wall.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 12 lines added |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fungi_panic_nondisplayed.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fungi_panic_nondisplayed` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 35, 60, 90, 100, 110, 200, 210 |
    | Dialogue nodes setting stages | 10: `mushroom_m3_1_chains`, 20: `algore_killed_10`, 35: `fungi_panic_check_key_10`, 60: `bogsten_check_necklace_10`, 90: `boss_fungi_killed_10`, 100: `bogsten_granny_switch_10`, 110: `chk_wild_berry_10`, 200: `bogsten_granny_80`, 210: `bogsten_tomb_pw_x1` |
    | Dialogue nodes clearing stages | 60: `bogsten_check_necklace_20`, 10: `mushroom_m3_1_chains_30`, 110: `chk_wild_berry_20` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
