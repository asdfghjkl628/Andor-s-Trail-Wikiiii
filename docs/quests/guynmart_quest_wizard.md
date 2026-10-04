# Ringmaker

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_quest_wizard` |
| **In journal** | No (hidden flag) |
| **Stages** | 5 |
| **Started by** | [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) |
| **NPCs involved** | [Rorthron](../monsters/guynmart_wizard.md) |
| **Locations** | [guynmart_tower_4](../maps/guynmart_tower_4.md) |
| **Total XP** | 1,000 |

</div>

## Overview

> 1=ROLS taken

## Prerequisites to start

Start with [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)). Required:

- reached stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12)
- carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md)
- hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=ROLS taken | [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) | carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md), hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md), stage 12 | gives [Ring of far lesser Shadow](../items/ring_shadow1.md) |
| <span id="stage-2"></span>2 | 2=Shutter down<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart tower 4](../maps/guynmart_tower_4.md).</span> | stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md)<br>[Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) | carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md), hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md), stage 100, stage 12 | gives [Ring of far lesser Shadow](../items/ring_shadow1.md) |
| <span id="stage-11"></span>11 | 11=inside<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart tower 4](../maps/guynmart_tower_4.md).</span> | stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md) | – | clears stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12) |
| <span id="stage-12"></span>12 | 12=outside<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart tower 4](../maps/guynmart_tower_4.md).</span> | stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md) | – | clears stage 11 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-11) |
| <span id="stage-100"></span>100 | 100=Shop closed | [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) | carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md), hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md), stage 12 | 1,000 XP<br>gives [Ring of far lesser Shadow](../items/ring_shadow1.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 1 route"

    1. Talk to [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) → choose “Thank you for your offer Rorthron. Here is the ring - be careful with it.” — **conditions:** reached stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12); carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md); hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md) → **stage 1**; also gives [Ring of far lesser Shadow](../items/ring_shadow1.md). NPC: “Oops!”

???+ note "Stage 2: 2 routes"

    1. stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-100) → **stage 2**
    2. Talk to [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) → choose “Thank you for your offer Rorthron. Here is the ring - be careful with it.” — **conditions:** reached stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12); carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md); hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md) → **stage 2**; also gives [Ring of far lesser Shadow](../items/ring_shadow1.md). NPC: “Oops!”

???+ note "Stage 11: 1 route"

    1. stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md) → the conversation leads here automatically → **stage 11**; also clears stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12)

???+ note "Stage 12: 1 route"

    1. stepping on a trigger on [guynmart_tower_4](../maps/guynmart_tower_4.md) → the conversation leads here automatically → **stage 12**; also clears stage 11 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-11)

???+ note "Stage 100: 1 route"

    1. Talk to [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) → choose “Thank you for your offer Rorthron. Here is the ring - be careful with it.” — **conditions:** reached stage 12 of [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-12); carry 1× [Ring of lesser Shadow](../items/ring_shadow0.md); hand over 1× [Ring of lesser Shadow](../items/ring_shadow0.md) → **stage 100**; also gives [Ring of far lesser Shadow](../items/ring_shadow1.md). NPC: “Oops!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_wizard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_wizard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_wizard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_wizard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_wizard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_quest_wizard` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 11, 12, 100 |
    | Dialogue nodes setting stages | 1: `guynmart_wizard_70`, 2: `guynmart_s_wizard_shutter_10`, 2: `guynmart_wizard_70`, 11: `guynmart_sign_wizard_in`, 12: `guynmart_sign_wizard_out`, 100: `guynmart_wizard_70` |
    | Dialogue nodes clearing stages | 12: `guynmart_sign_wizard_in`, 11: `guynmart_sign_wizard_out`, 2: `guynmart_sRpl_main_2c`, 1: `guynmart_lovis2_60`, 1: `guynmart_lovis2_460` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
