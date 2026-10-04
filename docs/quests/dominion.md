# Dominion

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `dominion` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 90) |
| **Started by** | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) |
| **NPCs involved** | [Saki](../monsters/saki.md), [Ysrine](../monsters/ysrine.md) |
| **Locations** | [undertell_1_1](../maps/undertell_1_1.md), [undertell_exit](../maps/undertell_exit.md) |
| **Total XP** | 9,000 |
| **Related quests** | 3 |

</div>

## Overview

> Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that the Kha'zaan were destroyed, Saki wanted me to help revive his Elytharan colleagues. They had become incorporeal during the war, and their souls became soul pearls.

## Prerequisites to start

Start with [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)). Required:

- reached stage 450 of [Devotion](../quests/devotion.md#stage-450)
- NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Devotion](devotion.md#stage-450) | stage 450 reached, for stages 10, 20, 30, 70 here |
| Requires | [The fifth master](fifth_master.md#stage-10) | stage 10 reached, for stage 50 here |
| Blocked by | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-7) | stage 7 must NOT be reached, for stage 50 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that the Kha'zaan were destroyed, Saki wanted me to help revive his Elytharan colleagues. They had become incorporeal during the war, and their souls became soul pearls. | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | – | spawns monsters on undertell_1_1 |
| <span id="stage-20"></span>20 | Saki wanted me to defeat the liches who had picked up the soul pearls, and get back all five of them. | [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md))<br>[Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 10 | spawns monsters on undertell_21<br>spawns monsters on undertell_3_lava_01<br>spawns monsters on undertell_4_01<br>spawns monsters on undertell_7_10<br>spawns monsters on undertell_5 |
| <span id="stage-30"></span>30 | I returned to Saki with all five soul pearls. He took them in haste and disappeared. | [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md))<br>[Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | hand over 5× [Soul pearl](../items/soul_pearl.md), stage 20 | 1,500 XP<br>removes monsters from undertell_1_1 |
| <span id="stage-50"></span>50 | Ysrine told me that Saki's behavior had confirmed her suspicions that Saki was a Kazaul mage and wanted to absorb the Elytharan mage souls to make himself stronger. | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 30 | – |
| <span id="stage-60"></span>60 | Ysrine told me that Saki was trying to flee Undertell. I was to find him, defeat him, and get the soul pearls back. | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 50 | spawns monsters on undertell_exit |
| <span id="stage-70"></span>70 | Prevented from escaping Undertell by Shannal, I found Saki at the passage to Undertell. | [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md))<br>[Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 60 | – |
| <span id="stage-90"></span>90 | Ysrine thanked me and told me to keep the soul pearls safe. **(completes quest)** | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | carry 5× [Soul pearl](../items/soul_pearl.md) | 7,500 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → the conversation leads here automatically — **conditions:** reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10) → **stage 10**; also spawns monsters on undertell_1_1. NPC: “Here, on my left.”

???+ note "Stage 20: 2 routes"

    1. Talk to [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “So I must destroy the liches and recover the pearls.” — **conditions:** latest stage of [Dominion](../quests/dominion.md#stage-10) is 10; reached stage 450 of [Devotion](../quests/devotion.md#stage-450) → **stage 20**; also spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5. NPC: “They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.”
    2. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “So I must destroy the liches and recover the pearls.” — **conditions:** reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10); latest stage of [Dominion](../quests/dominion.md#stage-10) is 10 → **stage 20**; also spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5. NPC: “They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.”

???+ note "Stage 30: 2 routes"

    1. Talk to [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “Yeah, here they are.” — **conditions:** reached stage 20 of [Dominion](../quests/dominion.md#stage-20); NOT reached stage 30 of [Dominion](../quests/dominion.md#stage-30); hand over 5× [Soul pearl](../items/soul_pearl.md) → **stage 30**; also removes monsters from undertell_1_1. NPC: “Thank you for these powerful artifacts!”
    2. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “Yeah, here they are.” — **conditions:** reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10); reached stage 20 of [Dominion](../quests/dominion.md#stage-20); NOT reached stage 30 of [Dominion](../quests/dominion.md#stage-30); hand over 5× [Soul pearl](../items/soul_pearl.md) → **stage 30**; also removes monsters from undertell_1_1. NPC: “Thank you for these powerful artifacts!”

???+ note "Stage 50: 1 route"

    1. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “Wrong how?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7); reached stage 30 of [Dominion](../quests/dominion.md#stage-30); NOT reached stage 50 of [Dominion](../quests/dominion.md#stage-50) → **stage 50**. NPC: “Saki was no follower of Elythara. He sought to absorb the spirits of the Elytharan mages and draw power from them. I…”

???+ note "Stage 60: 1 route"

    1. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Dominion](../quests/dominion.md#stage-50); NOT reached stage 60 of [Dominion](../quests/dominion.md#stage-60) → **stage 60**; also spawns monsters on undertell_exit. NPC: “Saki is trying to flee Undertell. Find him, defeat him, and recover the soul pearls and anything else he carries.…”

???+ note "Stage 70: 2 routes"

    1. Talk to [Saki](../monsters/saki.md) ([undertell_1_1](../maps/undertell_1_1.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Dominion](../quests/dominion.md#stage-60) → **stage 70**. NPC: “My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername,…”
    2. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → the conversation leads here automatically — **conditions:** reached stage 450 of [Devotion](../quests/devotion.md#stage-450); NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10); reached stage 60 of [Dominion](../quests/dominion.md#stage-60) → **stage 70**. NPC: “My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername,…”

???+ note "Stage 90: 1 route"

    1. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “What do I do with the Soul pearls?” — **conditions:** killed 1× [Saki](../monsters/saki.md); NOT reached stage 90 of [Dominion](../quests/dominion.md#stage-90); carry 5× [Soul pearl](../items/soul_pearl.md) → **stage 90**. NPC: “Besides keeping them away from those Kazaul Masters? I do not know yet. Powerful they are - they could perhaps bring…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `dominion` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 50, 60, 70, 90 |
    | Dialogue nodes setting stages | 10: `ysrine_start_devotion_15`, 20: `saki_dominion_100`, 30: `saki_pearls_20`, 50: `ysrine_dominion_saki_fleed_40`, 60: `ysrine_dominion_saki_fleed_60`, 70: `saki_trapped_20`, 90: `ysrine_saki_killed_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
