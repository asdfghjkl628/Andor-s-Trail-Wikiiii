# guynmart Replace Walkable unten/oben

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_qRpl_main` |
| **In journal** | No (hidden flag) |
| **Stages** | 7 |
| **Started by** | stepping on a trigger on [guynmart](../maps/guynmart.md), stepping on a trigger on [guynmart](../maps/guynmart.md) |

</div>

## Overview

> 1=ground

## Prerequisites to start

None: talk to stepping on a trigger on [guynmart](../maps/guynmart.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=ground<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | – | removes monsters from guynmart |
| <span id="stage-2"></span>2 | 2=wall<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 1 | clears stage 31 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-31)<br>clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22)<br>clears stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21)<br>clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12)<br>clears stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11)<br>clears stage 1 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-1)<br>removes monsters from guynmart<br>clears stage 2 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-2) |
| <span id="stage-11"></span>11 | 11=ground2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 2 | clears stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2) |
| <span id="stage-12"></span>12 | 12=wall2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 11 | clears stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11) |
| <span id="stage-21"></span>21 | 21=ground2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 12 | clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12) |
| <span id="stage-22"></span>22 | 22=wall2<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 21 | clears stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21) |
| <span id="stage-31"></span>31 | 31=ground3<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart](../maps/guynmart.md).</span> | stepping on a trigger on [guynmart](../maps/guynmart.md) | stage 22 | clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22)<br>spawns monsters on guynmart |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 4 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 1**; also removes monsters from guynmart
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 1**; also removes monsters from guynmart
    3. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 1**; also removes monsters from guynmart
    4. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 1**; also removes monsters from guynmart

???+ note "Stage 2: 3 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 2**; also clears stage 31 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-31), clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), clears stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21), clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12), clears stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11), clears stage 1 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-1), removes monsters from guynmart, clears stage 2 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-2)
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically → **stage 2**; also clears stage 31 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-31), clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), clears stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21), clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12), clears stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11), clears stage 1 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-1), removes monsters from guynmart, clears stage 2 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-2)
    3. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-1) → **stage 2**; also clears stage 1 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-1)

???+ note "Stage 11: 4 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2) → **stage 11**; also clears stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2)
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2) → **stage 11**; also clears stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2)
    3. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2) → **stage 11**; also clears stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2)
    4. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2) → **stage 11**; also clears stage 2 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-2)

???+ note "Stage 12: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11) → **stage 12**; also clears stage 11 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-11)

???+ note "Stage 21: 4 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12) → **stage 21**; also clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12)
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12) → **stage 21**; also clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12)
    3. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12) → **stage 21**; also clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12)
    4. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12) → **stage 21**; also clears stage 12 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-12)

???+ note "Stage 22: 1 route"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21) → **stage 22**; also clears stage 21 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-21)

???+ note "Stage 31: 4 routes"

    1. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22) → **stage 31**; also clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), spawns monsters on guynmart
    2. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22) → **stage 31**; also clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), spawns monsters on guynmart
    3. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22) → **stage 31**; also clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), spawns monsters on guynmart
    4. stepping on a trigger on [guynmart](../maps/guynmart.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22) → **stage 31**; also clears stage 22 of [guynmart Replace Walkable unten/oben (hidden flag)](../quests/guynmart_qRpl_main.md#stage-22), spawns monsters on guynmart


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_qRpl_main.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_qRpl_main.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_qRpl_main.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_qRpl_main.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_qRpl_main.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_qRpl_main` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 11, 12, 21, 22, 31 |
    | Dialogue nodes setting stages | 1: `guynmart_sRpl_main_q01`, 2: `guynmart_sRpl_main_2c`, 2: `guynmart_sRpl_main_q02`, 11: `guynmart_sRpl_main_q11`, 12: `guynmart_sRpl_main_q12`, 21: `guynmart_sRpl_main_q21`, 22: `guynmart_sRpl_main_q22`, 31: `guynmart_sRpl_main_q31` |
    | Dialogue nodes clearing stages | 31: `guynmart_sRpl_main_2c`, 31: `guynmart_sRpl_main_1r`, 22: `guynmart_sRpl_main_2c`, 22: `guynmart_sRpl_main_1r`, 22: `guynmart_sRpl_main_q31`, 21: `guynmart_sRpl_main_2c`, 21: `guynmart_sRpl_main_1r`, 21: `guynmart_sRpl_main_q22`, 12: `guynmart_sRpl_main_2c`, 12: `guynmart_sRpl_main_1r` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
