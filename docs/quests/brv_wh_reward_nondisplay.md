# Gold and Exp reward for Inventory quest completed - nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_wh_reward_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 3 |
| **Started by** | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) |
| **NPCs involved** | [Facutloni](../monsters/brv_wh_boss.md) |
| **Locations** | [brimhaven_warehouse](../maps/brimhaven_warehouse.md) |
| **Related quests** | 3 |

</div>

## Overview

> Not yet done.

## Prerequisites to start

None: talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Inventory](brv_wh.md#stage-10) | stage 10 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-100) | stage 100 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-101) | stage 101 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-102) | stage 102 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-103) | stage 103 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-104) | stage 104 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-105) | stage 105 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-106) | stage 106 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-107) | stage 107 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-108) | stage 108 reached, for stage 2 here |
| Requires | [Inventory](brv_wh.md#stage-109) | stage 109 reached, for stage 2 here |
| Unlocks | [Inventory](brv_wh.md#stage-900) | stage 900 there needs stage 2 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-10) | stage 10 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-20) | stage 20 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-30) | stage 30 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-40) | stage 40 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-50) | stage 50 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-60) | stage 60 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-70) | stage 70 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-80) | stage 80 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-90) | stage 90 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-100) | stage 100 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-110) | stage 110 there needs stage 3 here |
| Unlocks | [Delivery](brv_wh_delivery.md#stage-120) | stage 120 there needs stage 3 here |
| Unlocks | [Gold and Exp reward for Delivery quest completed - nondisplay (hidden flag)](brv_wh_delivery_reward_nondisplay.md#stage-1) | stage 1 there needs stage 3 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | Not yet done. | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | sets stage 10 of [Inventory](../quests/brv_wh.md#stage-10) |
| <span id="stage-2"></span>2 | Done. But haven't received gold and exp reward yet. | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | hand over 2× [Chandelier](../items/brv_wh_item_04.md), hand over 2× [Crystal globe](../items/brv_wh_item_00.md), hand over 2× [Dusty old book](../items/brv_wh_item_09.md), hand over 2× [Lyre](../items/brv_wh_item_02.md), hand over 2× [Mysterious green something](../items/brv_wh_item_05.md), hand over 2× [Old, worn cape](../items/brv_wh_item_06.md), hand over 2× [Plush pillow](../items/brv_wh_item_01.md), hand over 2× [Pretty porcelain figure](../items/brv_wh_item_07.md), hand over 2× [Striped hammer](../items/brv_wh_item_08.md), hand over 2× [Yellow boot](../items/brv_wh_item_03.md) | sets stage 900 of [Inventory](../quests/brv_wh.md#stage-900) |
| <span id="stage-3"></span>3 | Done. I received gold and exp reward. Old scrooge. | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | stage 2 | gives 100× [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 1 route"

    1. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → choose “Do you need any help?” → **stage 1**; also sets stage 10 of [Inventory](../quests/brv_wh.md#stage-10). NPC: “Come back to me when you found all the pairs and tell me how many there are.”

???+ note "Stage 2: 1 route"

    1. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → choose “I found 10 pairs of each item.” — **conditions:** reached stage 10 of [Inventory](../quests/brv_wh.md#stage-10); reached stage 100 of [Inventory](../quests/brv_wh.md#stage-100); reached stage 101 of [Inventory](../quests/brv_wh.md#stage-101); reached stage 102 of [Inventory](../quests/brv_wh.md#stage-102); reached stage 103 of [Inventory](../quests/brv_wh.md#stage-103); reached stage 104 of [Inventory](../quests/brv_wh.md#stage-104); reached stage 105 of [Inventory](../quests/brv_wh.md#stage-105); reached stage 106 of [Inventory](../quests/brv_wh.md#stage-106); reached stage 107 of [Inventory](../quests/brv_wh.md#stage-107); reached stage 108 of [Inventory](../quests/brv_wh.md#stage-108); reached stage 109 of [Inventory](../quests/brv_wh.md#stage-109); hand over 2× [Crystal globe](../items/brv_wh_item_00.md); hand over 2× [Plush pillow](../items/brv_wh_item_01.md); hand over 2× [Lyre](../items/brv_wh_item_02.md); hand over 2× [Yellow boot](../items/brv_wh_item_03.md); hand over 2× [Chandelier](../items/brv_wh_item_04.md); hand over 2× [Mysterious green something](../items/brv_wh_item_05.md); hand over 2× [Old, worn cape](../items/brv_wh_item_06.md); hand over 2× [Pretty porcelain figure](../items/brv_wh_item_07.md); hand over 2× [Striped hammer](../items/brv_wh_item_08.md); hand over 2× [Dusty old book](../items/brv_wh_item_09.md) → **stage 2**; also sets stage 900 of [Inventory](../quests/brv_wh.md#stage-900). NPC: “10 pairs - that is correct. So everything is in order.”

???+ note "Stage 3: 1 route"

    1. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → choose “I am glad. How much do I actually get for this work?” — **conditions:** reached stage 2 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2) → **stage 3**; also gives 100× [Gold coins](../items/gold.md). NPC: “Good work gives good wages! Here is 100 gold.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 3 lines added |
| [v0.7.17](../versions/0.7.17.md) | Added<br>Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_reward_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_reward_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_reward_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_reward_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_reward_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_wh_reward_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3 |
    | Dialogue nodes setting stages | 1: `brv_wh_boss_30`, 2: `brv_wh_boss_10_30`, 3: `brv_wh_boss_10_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
