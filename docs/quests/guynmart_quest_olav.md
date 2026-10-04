# Guest tour

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_quest_olav` |
| **In journal** | No (hidden flag) |
| **Stages** | 3 |
| **Started by** | stepping on a trigger on [guynmart](../maps/guynmart.md) |
| **NPCs involved** | [Hannah](../monsters/guynmart_hannah.md), [Hannah](../monsters/guynmart_hannah3.md) |
| **Locations** | [guynmart](../maps/guynmart.md), [guynmart_main_1](../maps/guynmart_main_1.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1

## Prerequisites to start

None: talk to stepping on a trigger on [guynmart](../maps/guynmart.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Roses](guynmart.md#stage-80) | stage 80 reached, for stage 7 here |
| Blocked by | [Roses](guynmart.md#stage-81) | stage 81 must NOT be reached, for stage 7 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | – | clears stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7) |
| <span id="stage-7"></span>7 | 7 olav-<br><span class="qnote">⚡ A scripted event can now trigger on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md)<br>[Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) | stage 1 | clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1)<br>spawns monsters on guynmart<br>clears stage 71 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-71)<br>clears stage 11 of [guynmart lake (hidden flag)](../quests/guynmart_r_lake.md#stage-11)<br>sets stage 70 of [Roses](../quests/guynmart.md#stage-70) |
| <span id="stage-71"></span>71 | 71 wall<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | – | applies condition stunned<br>applies condition bone_fracture |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 1**; also clears stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7)

???+ note "Stage 7: 2 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 80 of [Roses](../quests/guynmart.md#stage-80); NOT reached stage 81 of [Roses](../quests/guynmart.md#stage-81); reached stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1) → **stage 7**; also spawns monsters on guynmart, clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), clears stage 71 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-71), clears stage 11 of [guynmart lake (hidden flag)](../quests/guynmart_r_lake.md#stage-11). NPC: “Yoo-Hoo! You again - fine! I'm coming...”
    2. Talk to [Hannah](../monsters/guynmart_hannah.md) ([guynmart](../maps/guynmart.md)) → the conversation leads here automatically → **stage 7**; also sets stage 70 of [Roses](../quests/guynmart.md#stage-70), spawns monsters on guynmart, clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1). NPC: “I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...”

???+ note "Stage 71: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 71**; also applies condition stunned, applies condition bone_fracture


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_olav.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_quest_olav` |
    | showInLog | 0 |
    | Stage IDs | 1, 7, 71 |
    | Dialogue nodes setting stages | 1: `guynmart_sRpl_main_74`, 7: `guynmart_sRpl_main_72`, 7: `guynmart_sRpl_main_3a_10`, 7: `guynmart_hannah_20`, 71: `guynmart_sRpl_main_olav_2` |
    | Dialogue nodes clearing stages | 7: `guynmart_sRpl_main_olav_3`, 7: `guynmart_sRpl_main_74`, 7: `guynmart_sRpl_main_78`, 71: `guynmart_sRpl_main_1`, 71: `guynmart_sRpl_main_76`, 71: `guynmart_sRpl_main_3a_10`, 1: `guynmart_sRpl_main_72`, 1: `guynmart_sRpl_main_3a_10`, 1: `guynmart_hannah_20` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
