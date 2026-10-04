# Inventory

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_wh` |
| **In journal** | Yes |
| **Stages** | 12 (completes at 900) |
| **Started by** | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) |
| **NPCs involved** | [Facutloni](../monsters/brv_wh_boss.md), [brv_wh_item_00](../monsters/brv_wh_item_00.md), [brv_wh_item_01](../monsters/brv_wh_item_01.md), [brv_wh_item_02](../monsters/brv_wh_item_02.md), [brv_wh_item_03](../monsters/brv_wh_item_03.md), [brv_wh_item_04](../monsters/brv_wh_item_04.md) +15 |
| **Locations** | [brimhaven_warehouse](../maps/brimhaven_warehouse.md) |
| **Total XP** | 2,000 |
| **Related quests** | 1 |

</div>

## Overview

> Facutloni asked me to help him check the storage. I should check if there is a pair of every item.

## Prerequisites to start

None: talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) to begin.

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](brv_wh_reward_nondisplay.md#stage-2) | stage 2 reached, for stage 900 here |
| Unlocks | [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](brv_wh_reward_nondisplay.md#stage-2) | stage 2 there needs stages 10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Facutloni asked me to help him check the storage. I should check if there is a pair of every item.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven warehouse](../maps/brimhaven_warehouse.md).</span> | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | sets stage 1 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-1) |
| <span id="stage-100"></span>100 | I have found a pair of crystal globes. | [brv_wh_item_00](../monsters/brv_wh_item_00.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_20](../monsters/brv_wh_item_20.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Crystal globe](../items/brv_wh_item_00.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-101"></span>101 | I have found a pair of plush pillows. | [brv_wh_item_01](../monsters/brv_wh_item_01.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_21](../monsters/brv_wh_item_21.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Plush pillow](../items/brv_wh_item_01.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-102"></span>102 | I have found a pair of lyras. | [brv_wh_item_02](../monsters/brv_wh_item_02.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_22](../monsters/brv_wh_item_22.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Lyre](../items/brv_wh_item_02.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-103"></span>103 | I have found a pair of boots. | [brv_wh_item_03](../monsters/brv_wh_item_03.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_23](../monsters/brv_wh_item_23.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Yellow boot](../items/brv_wh_item_03.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-104"></span>104 | I have found a pair of chandeliers. | [brv_wh_item_04](../monsters/brv_wh_item_04.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_24](../monsters/brv_wh_item_24.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Chandelier](../items/brv_wh_item_04.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-105"></span>105 | I have found a pair of mysterious green somethings. | [brv_wh_item_05](../monsters/brv_wh_item_05.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_25](../monsters/brv_wh_item_25.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Mysterious green something](../items/brv_wh_item_05.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-106"></span>106 | I have found a pair of old, worn capes. | [brv_wh_item_06](../monsters/brv_wh_item_06.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_26](../monsters/brv_wh_item_26.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Old, worn cape](../items/brv_wh_item_06.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-107"></span>107 | I have found a pair of pretty porcelain figures. | [brv_wh_item_07](../monsters/brv_wh_item_07.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_27](../monsters/brv_wh_item_27.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Pretty porcelain figure](../items/brv_wh_item_07.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-108"></span>108 | I have found a pair of striped hammers. | [brv_wh_item_08](../monsters/brv_wh_item_08.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_28](../monsters/brv_wh_item_28.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Striped hammer](../items/brv_wh_item_08.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-109"></span>109 | I have found a pair of dusty old books. | [brv_wh_item_09](../monsters/brv_wh_item_09.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md))<br>[brv_wh_item_29](../monsters/brv_wh_item_29.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | – | gives 2× [Dusty old book](../items/brv_wh_item_09.md)<br>faction “brv_wh_aln” set to 0<br>removes monsters from brimhaven_warehouse |
| <span id="stage-900"></span>900 | I found all the 10 pairs. Facutloni is very happy. **(completes quest)** | [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) | hand over 2× [Chandelier](../items/brv_wh_item_04.md), hand over 2× [Crystal globe](../items/brv_wh_item_00.md), hand over 2× [Dusty old book](../items/brv_wh_item_09.md), hand over 2× [Lyre](../items/brv_wh_item_02.md), hand over 2× [Mysterious green something](../items/brv_wh_item_05.md), hand over 2× [Old, worn cape](../items/brv_wh_item_06.md), hand over 2× [Plush pillow](../items/brv_wh_item_01.md), hand over 2× [Pretty porcelain figure](../items/brv_wh_item_07.md), hand over 2× [Striped hammer](../items/brv_wh_item_08.md), hand over 2× [Yellow boot](../items/brv_wh_item_03.md), stage 10, stage 100, stage 101, stage 102, stage 103, stage 104, stage 105, stage 106, stage 107, stage 108, stage 109 | 2,000 XP<br>sets stage 2 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → choose “Do you need any help?” → **stage 10**; also sets stage 1 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-1). NPC: “Come back to me when you found all the pairs and tell me how many there are.”

???+ note "Stage 100: 2 routes"

    1. Talk to [brv_wh_item_00](../monsters/brv_wh_item_00.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 120 → **stage 100**; also gives 2× [Crystal globe](../items/brv_wh_item_00.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second crystal globe. Now that's a pair!”
    2. Talk to [brv_wh_item_20](../monsters/brv_wh_item_20.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 100 → **stage 100**; also gives 2× [Crystal globe](../items/brv_wh_item_00.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second crystal globe. Now that's a pair!”

???+ note "Stage 101: 2 routes"

    1. Talk to [brv_wh_item_01](../monsters/brv_wh_item_01.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 121 → **stage 101**; also gives 2× [Plush pillow](../items/brv_wh_item_01.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second plush pillow!”
    2. Talk to [brv_wh_item_21](../monsters/brv_wh_item_21.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 101 → **stage 101**; also gives 2× [Plush pillow](../items/brv_wh_item_01.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second plush pillow!”

???+ note "Stage 102: 2 routes"

    1. Talk to [brv_wh_item_02](../monsters/brv_wh_item_02.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 122 → **stage 102**; also gives 2× [Lyre](../items/brv_wh_item_02.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “Great! You have found the second lyre and put it into your bag.”
    2. Talk to [brv_wh_item_22](../monsters/brv_wh_item_22.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 102 → **stage 102**; also gives 2× [Lyre](../items/brv_wh_item_02.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “Great! You have found the second lyre and put it into your bag.”

???+ note "Stage 103: 2 routes"

    1. Talk to [brv_wh_item_03](../monsters/brv_wh_item_03.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 123 → **stage 103**; also gives 2× [Yellow boot](../items/brv_wh_item_03.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the yellow boot!”
    2. Talk to [brv_wh_item_23](../monsters/brv_wh_item_23.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 103 → **stage 103**; also gives 2× [Yellow boot](../items/brv_wh_item_03.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the yellow boot!”

???+ note "Stage 104: 2 routes"

    1. Talk to [brv_wh_item_04](../monsters/brv_wh_item_04.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 124 → **stage 104**; also gives 2× [Chandelier](../items/brv_wh_item_04.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second chandelier!”
    2. Talk to [brv_wh_item_24](../monsters/brv_wh_item_24.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 104 → **stage 104**; also gives 2× [Chandelier](../items/brv_wh_item_04.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second chandelier!”

???+ note "Stage 105: 2 routes"

    1. Talk to [brv_wh_item_05](../monsters/brv_wh_item_05.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 125 → **stage 105**; also gives 2× [Mysterious green something](../items/brv_wh_item_05.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second mysterious green something!”
    2. Talk to [brv_wh_item_25](../monsters/brv_wh_item_25.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 105 → **stage 105**; also gives 2× [Mysterious green something](../items/brv_wh_item_05.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second mysterious green something!”

???+ note "Stage 106: 2 routes"

    1. Talk to [brv_wh_item_06](../monsters/brv_wh_item_06.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 126 → **stage 106**; also gives 2× [Old, worn cape](../items/brv_wh_item_06.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second old, worn cape!”
    2. Talk to [brv_wh_item_26](../monsters/brv_wh_item_26.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 106 → **stage 106**; also gives 2× [Old, worn cape](../items/brv_wh_item_06.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second old, worn cape!”

???+ note "Stage 107: 2 routes"

    1. Talk to [brv_wh_item_07](../monsters/brv_wh_item_07.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 127 → **stage 107**; also gives 2× [Pretty porcelain figure](../items/brv_wh_item_07.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second pretty porcelain figure!”
    2. Talk to [brv_wh_item_27](../monsters/brv_wh_item_27.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 107 → **stage 107**; also gives 2× [Pretty porcelain figure](../items/brv_wh_item_07.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second pretty porcelain figure!”

???+ note "Stage 108: 2 routes"

    1. Talk to [brv_wh_item_08](../monsters/brv_wh_item_08.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 128 → **stage 108**; also gives 2× [Striped hammer](../items/brv_wh_item_08.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second striped hammer!”
    2. Talk to [brv_wh_item_28](../monsters/brv_wh_item_28.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 108 → **stage 108**; also gives 2× [Striped hammer](../items/brv_wh_item_08.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second striped hammer!”

???+ note "Stage 109: 2 routes"

    1. Talk to [brv_wh_item_09](../monsters/brv_wh_item_09.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 129 → **stage 109**; also gives 2× [Dusty old book](../items/brv_wh_item_09.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second dusty old book!”
    2. Talk to [brv_wh_item_29](../monsters/brv_wh_item_29.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** faction “brv_wh_aln” = 109 → **stage 109**; also gives 2× [Dusty old book](../items/brv_wh_item_09.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse. NPC: “You have found the second dusty old book!”

???+ note "Stage 900: 2 routes"

    1. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → choose “I found 10 pairs of each item.” — **conditions:** reached stage 10 of [Inventory](../quests/brv_wh.md#stage-10); reached stage 100 of [Inventory](../quests/brv_wh.md#stage-100); reached stage 101 of [Inventory](../quests/brv_wh.md#stage-101); reached stage 102 of [Inventory](../quests/brv_wh.md#stage-102); reached stage 103 of [Inventory](../quests/brv_wh.md#stage-103); reached stage 104 of [Inventory](../quests/brv_wh.md#stage-104); reached stage 105 of [Inventory](../quests/brv_wh.md#stage-105); reached stage 106 of [Inventory](../quests/brv_wh.md#stage-106); reached stage 107 of [Inventory](../quests/brv_wh.md#stage-107); reached stage 108 of [Inventory](../quests/brv_wh.md#stage-108); reached stage 109 of [Inventory](../quests/brv_wh.md#stage-109); hand over 2× [Crystal globe](../items/brv_wh_item_00.md); hand over 2× [Plush pillow](../items/brv_wh_item_01.md); hand over 2× [Lyre](../items/brv_wh_item_02.md); hand over 2× [Yellow boot](../items/brv_wh_item_03.md); hand over 2× [Chandelier](../items/brv_wh_item_04.md); hand over 2× [Mysterious green something](../items/brv_wh_item_05.md); hand over 2× [Old, worn cape](../items/brv_wh_item_06.md); hand over 2× [Pretty porcelain figure](../items/brv_wh_item_07.md); hand over 2× [Striped hammer](../items/brv_wh_item_08.md); hand over 2× [Dusty old book](../items/brv_wh_item_09.md) → **stage 900**; also sets stage 2 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2). NPC: “10 pairs - that is correct. So everything is in order.”
    2. Talk to [Facutloni](../monsters/brv_wh_boss.md) ([brimhaven_warehouse](../maps/brimhaven_warehouse.md)) → the conversation leads here automatically — **conditions:** reached stage 2 of [Gold and Exp reward for Inventory quest completed - nondisplay (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2) → **stage 900**. NPC: “Good work! I am very pleased with you.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_wh` |
    | showInLog | 1 |
    | Stage IDs | 10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 900 |
    | Dialogue nodes setting stages | 10: `brv_wh_boss_30`, 100: `brv_wh_item_00_1`, 101: `brv_wh_item_01_1`, 102: `brv_wh_item_02_1`, 103: `brv_wh_item_03_1`, 104: `brv_wh_item_04_1`, 105: `brv_wh_item_05_1`, 106: `brv_wh_item_06_1`, 107: `brv_wh_item_07_1`, 108: `brv_wh_item_08_1`, 109: `brv_wh_item_09_1`, 900: `brv_wh_boss_10_30`, 900: `brv_wh_boss_10_32` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
