---
description: "Guest tour is a hidden quest in Andor's Trail, started by stepping on a trigger on guynmart. 3 stages. 1"
---

# Guest tour

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_quest_olav` |
| **In journal** | No (hidden flag) |
| **Stages** | 3 |
| **Started by** | stepping on a trigger on [Guynmart](../maps/guynmart.md) |
| **NPCs involved** | [Hannah](../monsters/guynmart_hannah.md), [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah3) |
| **Locations** | [Guynmart](../maps/guynmart.md), [Guynmart main 1](../maps/guynmart_main_1.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1

## Prerequisites to start

None: talk to stepping on a trigger on [Guynmart](../maps/guynmart.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Roses](guynmart.md#stage-80) | stage 80 reached, for stage 7 here |
| Blocked by | [Roses](guynmart.md#stage-81) | stage 81 must NOT be reached, for stage 7 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | 1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart](../maps/guynmart.md) | – |
| <span id="stage-7"></span>[7](#route-7) | 7 olav-<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart](../maps/guynmart.md), [Hannah](../monsters/guynmart_hannah.md) | varies by route (see below) |
| <span id="stage-71"></span>[71](#route-71) | 71 wall<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [Guynmart](../maps/guynmart.md) | applies condition stunned, applies condition bone_fracture |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · stepping on a trigger on guynmart · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart](../maps/guynmart.md)

    - <small>Also: clears stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7)</small>


<span id="route-7"></span>

??? note "Stage 7 · stepping on a trigger on guynmart, Hannah · 2 ways"

    **Way 1:** Stepping on a trigger on [Guynmart](../maps/guynmart.md)

    - **Needs:** stage 1; reached stage 80 of [Roses](../quests/guynmart.md#stage-80); not reached stage 81 of [Roses](../quests/guynmart.md#stage-81)
    - **Gives:** spawns monsters on guynmart
    - <small>Also: clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), clears stage 71 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-71), clears stage 11 of [Guynmart lake (hidden flag)](../quests/guynmart_r_lake.md#stage-11)</small>
    - *“Yoo-Hoo! You again - fine! I'm coming...”*

    **Way 2:** Talk to [Hannah](../monsters/guynmart_hannah.md), automatic

    - **Gives:** sets stage 70 of [Roses](../quests/guynmart.md#stage-70), spawns monsters on guynmart
    - <small>Also: clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1)</small>
    - *“I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...”*


<span id="route-71"></span>

??? note "Stage 71 · stepping on a trigger on guynmart · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart](../maps/guynmart.md)

    - **Gives:** applies condition stunned, applies condition bone_fracture



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_quest_olav` |
    | Name in game data | `Guest tour` |
    | showInLog | 0 |
    | Stage IDs | 1, 7, 71 |
    | Dialogue nodes setting stages | 1: `guynmart_sRpl_main_74`, 7: `guynmart_sRpl_main_72`, 7: `guynmart_sRpl_main_3a_10`, 7: `guynmart_hannah_20`, 71: `guynmart_sRpl_main_olav_2` |
    | Dialogue nodes clearing stages | 7: `guynmart_sRpl_main_olav_3`, 7: `guynmart_sRpl_main_74`, 7: `guynmart_sRpl_main_78`, 71: `guynmart_sRpl_main_1`, 71: `guynmart_sRpl_main_76`, 71: `guynmart_sRpl_main_3a_10`, 1: `guynmart_sRpl_main_72`, 1: `guynmart_sRpl_main_3a_10`, 1: `guynmart_hannah_20` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
