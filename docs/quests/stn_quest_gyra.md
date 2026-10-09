---
description: "Lost girl looking for lost things is a quest in Andor's Trail, started by walking into a blocked passage on waytogalmore1. 14 stages, 5,000 XP in total. The mechanism of the south gate seemed to be broken. Maybe someone in Stoutford could repair it?"
---

# Lost girl looking for lost things

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `stn_quest_gyra` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 170, 199) |
| **Started by** | walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md) |
| **NPCs involved** | [Gyra](../monsters/stn_gyra.md), [Lord Berbane](../monsters/berbane.md), [Odirath](../monsters/stoutford_armorer.md) |
| **Locations** | [Stoutford armorer](../maps/stoutford_armorer.md), [Stoutford castle 1](../maps/stoutford_castle1.md), [Stoutford tavern](../maps/stoutford_tavern.md) |
| **Total XP** | 5,000 |
| **Related quests** | 2 |

</div>

## Overview

> The mechanism of the south gate seemed to be broken. Maybe someone in Stoutford could repair it?

## Prerequisites to start

None: talk to walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-13) | stage 13 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-17) | stage 17 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-19) | stage 19 reached, for stage 60 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-21) | stage 21 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-41) | stage 41 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-42) | stage 42 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-43) | stage 43 reached, for stage 50 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-44) | stage 44 reached, for stages 92, 99, 199 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-149) | stage 149 there needs stage 70 here |
| Unlocks | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-9) | stage 9 there needs stage 5 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">The mechanism of the south gate seemed to be broken. Maybe someone… ▸</span><span class="l">▴ less</span></summary>The mechanism of the south gate seemed to be broken. Maybe someone in Stoutford could repair it?</details> | walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">The little daughter of Odirath the armorer has been missing for… ▸</span><span class="l">▴ less</span></summary>The little daughter of Odirath the armorer has been missing for several days now. You offered to help search for her.</details> | [Odirath](../monsters/stoutford_armorer.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Odirath's daughter Gyra was hidden in the storeroom of the main… ▸</span><span class="l">▴ less</span></summary>Odirath's daughter Gyra was hidden in the storeroom of the main house of the castle. She was surprised by the raid on the castle and no longer dared to leave her hiding place. She was looking for Lord Berbane's helmet, which he had forgotten somewhere in the castle.</details> | [Gyra](../monsters/stn_gyra.md) | – |
| <span id="stage-30"></span>[30](#route-30) | You offered Gyra to lead her back home safely. | [Gyra](../monsters/stn_gyra.md) | removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1 |
| <span id="stage-40"></span>40 | Gyra has the feeling that the helmet is very close. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-50"></span>[50](#route-50) | You found the helmet.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle 2](../maps/stoutford_castle2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle barrack 1](../maps/stoutford_castle_barrack1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle tower 1](../maps/stoutford_castle_tower1.md).</span> | stepping on a trigger on [Stoutford castle 2](../maps/stoutford_castle2.md), stepping on a trigger on [Stoutford castle barrack 1](../maps/stoutford_castle_barrack1.md) +1 | 1× [Stoutford chief's helmet](../items/stoutford_helmet.md) |
| <span id="stage-60"></span>[60](#route-60) | Once back in Stoutford Gyra knew the way and ran to her father Odirath.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild 19](../maps/wild19.md).</span> | stepping on a trigger on [Wild 19](../maps/wild19.md) | removes monsters from wild19, applies condition fatigue_minor |
| <span id="stage-70"></span>[70](#route-70) | Odirath thanks you many thousand times. | [Odirath](../monsters/stoutford_armorer.md) | 2,300 XP |
| <span id="stage-80"></span>[80](#route-80) | Odirath had repaired the mechanism of the southern castle gate. | walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md) | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">Lord Berbane slowly took his helmet. Nevertheless, he remained… ▸</span><span class="l">▴ less</span></summary>Lord Berbane slowly took his helmet. Nevertheless, he remained sitting at the table. He probably needs a few more hours without drinks before he can get back to work. If ever.</details> | [Lord Berbane](../monsters/berbane.md) | – |
| <span id="stage-92"></span>[92](#route-92) | Lord Berbane took his helmet. But somehow that does not really satisfy you. | [Lord Berbane](../monsters/berbane.md) | – |
| <span id="stage-99"></span>[99](#route-99) | <details class="jt"><summary><span class="s">Lord Berbane is singing merrily about his pretended heroic deeds.… ▸</span><span class="l">▴ less</span></summary>Lord Berbane is singing merrily about his pretended heroic deeds. What a boaster.</details> | [Lord Berbane](../monsters/berbane.md) | – |
| <span id="stage-170"></span>[170](#route-170) | Odirath thanked you many thousands of times. **(ends quest)** | [Odirath](../monsters/stoutford_armorer.md) | 2,500 XP |
| <span id="stage-199"></span>[199](#route-199) | <details class="jt"><summary><span class="s">Lord Berbane is singing merrily about his pretended heroic deeds.… ▸</span><span class="l">▴ less</span></summary>Lord Berbane is singing merrily about his pretended heroic deeds. What a boaster.</details> **(ends quest)** | [Lord Berbane](../monsters/berbane.md) | 200 XP |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-5"></span>

??? note "Stage 5 · walking into a blocked passage on waytogalmore1 · 1 way"

    **Way 1:** Walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md)

    - *“The mechanism doesn't move. It seems to be broken. Maybe someone can fix it for me?”*


<span id="route-10"></span>

??? note "Stage 10 · Odirath · 1 way"

    **Way 1:** Talk to [Odirath](../monsters/stoutford_armorer.md), choose “I'm not afraid. I could have a look in the castle.”

    - **Needs:** not yet stage 10, 60
    - *“You would do that for me? I can hardly accept your offer.”*


<span id="route-20"></span>

??? note "Stage 20 · Gyra · 1 way"

    **Way 1:** Talk to [Gyra](../monsters/stn_gyra.md), choose “What is your problem, my little one?”

    - *“I was looking for Lord Bourbon's helmet, when I was surprised by these monsters.”*


<span id="route-30"></span>

??? note "Stage 30 · Gyra · 1 way"

    **Way 1:** Talk to [Gyra](../monsters/stn_gyra.md), choose “Of course I will help you. Just follow me.”

    - **Gives:** removes monsters from stoutford_castle1, spawns monsters on stoutford_castle1
    - <small>Also: sets stage 11 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-11), starts timer “stn_gyra_hint”</small>
    - *“I started to look in the main house, but maybe we have to search the whole castle.”*


<span id="route-50"></span>

??? note "Stage 50 · stepping on a trigger on stoutford_castle2, stepping on a tr · 3 ways"

    **Way 1:** Stepping on a trigger on [Stoutford castle 2](../maps/stoutford_castle2.md), choose “Yes, there it is!”

    - **Needs:** not yet stage 50; reached stage 13 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-13); reached stage 41 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-41)
    - **Gives:** 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)
    - *“And now back home quickly!”*

    **Way 2:** Stepping on a trigger on [Stoutford castle barrack 1](../maps/stoutford_castle_barrack1.md), choose “Yes, there it is!”

    - **Needs:** not yet stage 50; reached stage 21 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-21); reached stage 42 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-42)
    - **Gives:** 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)
    - *“And now back home quickly!”*

    **Way 3:** Stepping on a trigger on [Stoutford castle tower 1](../maps/stoutford_castle_tower1.md), choose “Yes, there it is!”

    - **Needs:** not yet stage 50; reached stage 17 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-17); reached stage 43 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-43)
    - **Gives:** 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)
    - *“And now back home quickly!”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on wild19 · 1 way"

    **Way 1:** Stepping on a trigger on [Wild 19](../maps/wild19.md)

    - **Needs:** stage 50; reached stage 19 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-19)
    - **Gives:** removes monsters from wild19, applies condition fatigue_minor
    - <small>Also: clears stage 19 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-19), clears stage 29 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-29)</small>
    - *“Now I know the way. I run to my dad and tell him the whole story.”*


<span id="route-70"></span>

??? note "Stage 70 · Odirath · 1 way"

    **Way 1:** Talk to [Odirath](../monsters/stoutford_armorer.md), choose “You look happy again.”

    - **Needs:** stage 60


<span id="route-80"></span>

??? note "Stage 80 · walking into a blocked passage on waytogalmore1 · 1 way"

    **Way 1:** Walking into a blocked passage on [Waytogalmore 1](../maps/waytogalmore1.md)

    - **Needs:** stage 80
    - *“Oh, cool, Odirath seems to have repaired the mechanism already.”*


<span id="route-90"></span>

??? note "Stage 90 · Lord Berbane · 1 way"

    **Way 1:** Talk to [Lord Berbane](../monsters/berbane.md), choose “Will you make the songs a reality now?”

    - **Needs:** stage 70; carry 1× [Stoutford chief's helmet](../items/stoutford_helmet.md); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)
    - <small>Also: sets stage 149 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-149)</small>
    - *“He sighs and slowly takes the helmet.”*


<span id="route-92"></span>

??? note "Stage 92 · Lord Berbane · 1 way"

    **Way 1:** Talk to [Lord Berbane](../monsters/berbane.md), choose “No, I have...”

    - **Needs:** reached stage 44 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)
    - <small>Also: sets stage 149 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-149)</small>
    - *“[Loud voice] Yes, he has carried my magical helmet for me. I will take it back now.”*


<span id="route-99"></span>

??? note "Stage 99 · Lord Berbane · 1 way"

    **Way 1:** Talk to [Lord Berbane](../monsters/berbane.md), choose “I give up.”

    - **Needs:** reached stage 44 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)


<span id="route-170"></span>

??? note "Stage 170 · Odirath · 1 way"

    **Way 1:** Talk to [Odirath](../monsters/stoutford_armorer.md), choose “You look happy again.”

    - **Needs:** stage 60, 99


<span id="route-199"></span>

??? note "Stage 199 · Lord Berbane · 1 way"

    **Way 1:** Talk to [Lord Berbane](../monsters/berbane.md), choose “I give up.”

    - **Needs:** stage 70; reached stage 44 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-44); hand over 1× [Stoutford chief's helmet](../items/stoutford_helmet.md)



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.14](../versions/0.8.14.md) | Stages added: 5, 80<br>Stage 170 journal text changed<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stn_quest_gyra.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
