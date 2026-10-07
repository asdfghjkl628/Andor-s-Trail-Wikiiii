---
description: "gardenGuard blocks is a hidden quest in Andor's Trail, started by Guynmart guard (guynmart). 1 stages. 1=unblocked"
---

# gardenGuard blocks

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_quest_gguard` |
| **In journal** | No (hidden flag) |
| **Stages** | 1 |
| **Started by** | [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) |
| **NPCs involved** | [Guynmart guard](../monsters/guynmart_gguard.md) |
| **Locations** | [guynmart](../maps/guynmart.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1=unblocked

## Prerequisites to start

Start with [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)). Required:

- reached stage 30 of [Roses](../quests/guynmart.md#stage-30)
- pay 100 gold


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Roses](guynmart.md#stage-30) | stage 30 reached, for stage 1 here |
| Requires | [Roses](guynmart.md#stage-70) | stage 70 reached, for stage 82 here |
| Blocked by | [Roses](guynmart.md#stage-100) | stage 100 must NOT be reached, for stage 82 here |
| Blocked by | [Roses](guynmart.md#stage-132) | stage 132 must NOT be reached, for stage 82 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=unblocked<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart](../maps/guynmart.md).</span> | [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) | pay 100 gold | sets stage 30 of [Roses](../quests/guynmart.md#stage-30) |
| <span id="stage-82"></span>82 |  | [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) | have 100 gold, pay 100 gold | gives [Rose](../items/guynmart_rose.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) → choose “Here is 100 gold.” — **conditions:** reached stage 30 of [Roses](../quests/guynmart.md#stage-30); pay 100 gold → **stage 1**; also sets stage 30 of [Roses](../quests/guynmart.md#stage-30)

???+ note "Stage 82: 1 route"

    1. Talk to [Guynmart guard](../monsters/guynmart_gguard.md) ([guynmart](../maps/guynmart.md)) → choose “I understand. Here, 100 gold.” — **conditions:** reached stage 70 of [Roses](../quests/guynmart.md#stage-70); NOT carry 1× [Rose](../items/guynmart_rose.md); NOT reached stage 100 of [Roses](../quests/guynmart.md#stage-100); NOT reached stage 132 of [Roses](../quests/guynmart.md#stage-132); have 100 gold; pay 100 gold → **stage 82**; also gives [Rose](../items/guynmart_rose.md). NPC: “And here is the rose. Don't tell anybody that you got it from me.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_gguard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_gguard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_gguard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_gguard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_quest_gguard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_quest_gguard` |
    | showInLog | 0 |
    | Stage IDs | 1, 82 |
    | Dialogue nodes setting stages | 1: `guynmart_gguard_900`, 82: `guynmart_gguard_380` |
    | Dialogue nodes clearing stages | 1: `guynmart_sRpl_main_3a`, 1: `guynmart_sRpl_main_3b` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
