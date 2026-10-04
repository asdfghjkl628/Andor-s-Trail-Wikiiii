# Lost girl looking for lost things

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `stn_quest_gyra` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 170, 199) |
| **Started by** | walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) |
| **NPCs involved** | [Gyra](../monsters/stn_gyra.md), [Lord Berbane](../monsters/berbane.md), [Odirath](../monsters/stoutford_armorer.md) |
| **Locations** | [stoutford_armorer](../maps/stoutford_armorer.md), [stoutford_castle1](../maps/stoutford_castle1.md), [stoutford_tavern](../maps/stoutford_tavern.md) |
| **Total XP** | 5,000 |
| **Related quests** | 2 |

</div>

## Overview

> The mechanism of the south gate seemed to be broken. Maybe someone in Stoutford could repair it?

## Prerequisites to start

None: talk to walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-13) | stage 13 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-17) | stage 17 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-19) | stage 19 reached, for stage 60 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-21) | stage 21 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-41) | stage 41 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-42) | stage 42 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-43) | stage 43 reached, for stage 50 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-44) | stage 44 reached, for stages 92, 99, 199 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-149) | stage 149 there needs stage 70 here |
| Unlocks | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-9) | stage 9 there needs stage 5 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | The mechanism of the south gate seemed to be broken. Maybe someone in Stoutford could repair it? | walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) | – | – |
| <span id="stage-10"></span>10 | The little daughter of Odirath the armorer has been missing for several days now. You offered to help search for her. | [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) | – | – |
| <span id="stage-20"></span>20 | Odirath's daughter Gyra was hidden in the storeroom of the main house of the castle. She was surprised by the raid on the castle and no longer dared to leave her hiding place. She was looking for Lord Berbane's helmet, which he had forgotten somewhere in the castle. | [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md)) | – | – |
| <span id="stage-30"></span>30 | You offered Gyra to lead her back home safely. | [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md)) | – | sets stage 11 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-11)<br>starts timer “stn_gyra_hint”<br>removes monsters from stoutford_castle1<br>spawns monsters on stoutford_castle1 |
| <span id="stage-40"></span>40 | Gyra has the feeling that the helmet is very close. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-50"></span>50 | You found the helmet.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack1](../maps/stoutford_castle_barrack1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower1](../maps/stoutford_castle_tower1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle2](../maps/stoutford_castle2.md).</span> | stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md)<br>stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md)<br>stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) | – | gives 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) |
| <span id="stage-60"></span>60 | Once back in Stoutford Gyra knew the way and ran to her father Odirath.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild19](../maps/wild19.md).</span> | stepping on a trigger on [wild19](../maps/wild19.md) | stage 50 | clears stage 19 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-19)<br>clears stage 29 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-29)<br>removes monsters from wild19<br>applies condition fatigue_minor |
| <span id="stage-70"></span>70 | Odirath thanks you many thousand times. | [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) | stage 60 | 2,300 XP |
| <span id="stage-80"></span>80 | Odirath had repaired the mechanism of the southern castle gate. | walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) | – | – |
| <span id="stage-90"></span>90 | Lord Berbane slowly took his helmet. Nevertheless, he remained sitting at the table. He probably needs a few more hours without drinks before he can get back to work. If ever. | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | carry 1× [Stoutford chief's helmet](../items/stoutford_helmet.md), hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md), stage 70 | sets stage 149 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-149) |
| <span id="stage-92"></span>92 | Lord Berbane took his helmet. But somehow that does not really satisfy you. | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) | sets stage 149 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-149) |
| <span id="stage-99"></span>99 | Lord Berbane is singing merrily about his pretended heroic deeds. What a boaster. | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) | – |
| <span id="stage-170"></span>170 | Odirath thanked you many thousands of times. **(completes quest)** | [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) | stage 60, stage 99 | 2,500 XP |
| <span id="stage-199"></span>199 | Lord Berbane is singing merrily about his pretended heroic deeds. What a boaster. **(completes quest)** | [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md), stage 70 | 200 XP |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically → **stage 5**. NPC: “The mechanism doesn't move. It seems to be broken. Maybe someone can fix it for me?”

???+ note "Stage 10: 1 route"

    1. Talk to [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) → choose “I'm not afraid. I could have a look in the castle.” — **conditions:** NOT reached stage 10 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-10); NOT reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60) → **stage 10**. NPC: “You would do that for me? I can hardly accept your offer.”

???+ note "Stage 20: 1 route"

    1. Talk to [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md)) → choose “What is your problem, my little one?” → **stage 20**. NPC: “I was looking for Lord Bourbon's helmet, when I was surprised by these monsters.”

???+ note "Stage 30: 1 route"

    1. Talk to [Gyra](../monsters/stn_gyra.md) ([stoutford_castle1](../maps/stoutford_castle1.md)) → choose “Of course I will help you. Just follow me.” → **stage 30**; also sets stage 11 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-11), starts timer “stn_gyra_hint”, removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1. NPC: “I started to look in the main house, but maybe we have to search the whole castle.”

???+ note "Stage 50: 3 routes"

    1. stepping on a trigger on [stoutford_castle2](../maps/stoutford_castle2.md) → choose “Yes, there it is!” — **conditions:** reached stage 13 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-13); NOT reached stage 50 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-50); reached stage 41 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-41) → **stage 50**; also gives 1× [Stoutford chief's helmet](../items/stoutford_helmet.md). NPC: “And now back home quickly!”
    2. stepping on a trigger on [stoutford_castle_barrack1](../maps/stoutford_castle_barrack1.md) → choose “Yes, there it is!” — **conditions:** reached stage 21 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-21); NOT reached stage 50 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-50); reached stage 42 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-42) → **stage 50**; also gives 1× [Stoutford chief's helmet](../items/stoutford_helmet.md). NPC: “And now back home quickly!”
    3. stepping on a trigger on [stoutford_castle_tower1](../maps/stoutford_castle_tower1.md) → choose “Yes, there it is!” — **conditions:** reached stage 17 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-17); NOT reached stage 50 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-50); reached stage 43 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-43) → **stage 50**; also gives 1× [Stoutford chief's helmet](../items/stoutford_helmet.md). NPC: “And now back home quickly!”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [wild19](../maps/wild19.md) → the conversation leads here automatically — **conditions:** reached stage 19 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-19); reached stage 50 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-50) → **stage 60**; also clears stage 19 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-19), clears stage 29 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-29), removes monsters from wild19, applies condition fatigue_minor. NPC: “Now I know the way. I run to my dad and tell him the whole story.”

???+ note "Stage 70: 1 route"

    1. Talk to [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) → choose “You look happy again.” — **conditions:** reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60) → **stage 70**

???+ note "Stage 80: 1 route"

    1. walking into a blocked passage on [waytogalmore1](../maps/waytogalmore1.md) → the conversation leads here automatically — **conditions:** reached stage 80 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-80) → **stage 80**. NPC: “Oh, cool, Odirath seems to have repaired the mechanism already.”

???+ note "Stage 90: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “Will you make the songs a reality now?” — **conditions:** reached stage 70 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-70); carry 1× [Stoutford chief's helmet](../items/stoutford_helmet.md); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) → **stage 90**; also sets stage 149 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-149). NPC: “He sighs and slowly takes the helmet.”

???+ note "Stage 92: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “No, I have...” — **conditions:** reached stage 44 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) → **stage 92**; also sets stage 149 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-149). NPC: “[Loud voice] Yes, he has carried my magical helmet for me. I will take it back now.”

???+ note "Stage 99: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “I give up.” — **conditions:** reached stage 44 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) → **stage 99**

???+ note "Stage 170: 1 route"

    1. Talk to [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) → choose “You look happy again.” — **conditions:** reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60); reached stage 99 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-99) → **stage 170**

???+ note "Stage 199: 1 route"

    1. Talk to [Lord Berbane](../monsters/berbane.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “I give up.” — **conditions:** reached stage 44 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md); reached stage 70 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-70) → **stage 199**


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.14](../versions/0.8.14.md) | stages added: 5, 80; stage 170 journal text changed<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `stn_quest_gyra` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 92, 99, 170, 199 |
    | Dialogue nodes setting stages | 5: `stn_southgate_10a`, 10: `odirath_2_3`, 20: `stn_gyra_init_12`, 30: `stn_gyra_init_52`, 50: `stn_gyra_hlm1b_found_10`, 60: `stn_gyra_110`, 70: `odirath_3_1`, 80: `stn_southgate_10b`, 90: `berbane_32`, 92: `berbane_132`, 99: `berbane_142`, 170: `odirath_3_2`, 199: `berbane_144` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
