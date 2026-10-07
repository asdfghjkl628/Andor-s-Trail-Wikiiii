---
description: "brv_dagger_nondisplay is a hidden quest in Andor's Trail, started by stepping on a trigger on brimhaven_inn_east. 4 stages. Purchased gem"
---

# brv_dagger_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_dagger_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 4 |
| **Started by** | stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md), stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) |
| **NPCs involved** | [Pixtumn](../monsters/quiet_thief.md) |
| **Locations** | [brimhaven_inn_east](../maps/brimhaven_inn_east.md) |
| **Related quests** | 1 |

</div>

## Overview

> Purchased gem

## Prerequisites to start

**Route 1** (stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md)):

- carry 1× [A strange-looking gem](../items/strange_gem.md)

**Route 2** (stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md)):

- carry 1× [A strange looking dagger](../items/strange_dagger.md)
- carry 1× [A strange-looking gem](../items/strange_gem.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A strange looking dagger](brv_dagger.md#stage-30) | stage 30 reached, for stage 30 here |
| Requires | [A strange looking dagger](brv_dagger.md#stage-40) | stage 40 reached, for stage 40 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-40) | stage 40 there needs stage 20 here |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-30) | reaching stages 20, 30 here closes stage 30 there |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-40) | reaching stages 10, 40 here closes stage 40 there |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-90) | reaching stages 30, 40 here closes stage 90 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Purchased gem<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md) | – |
| <span id="stage-20"></span>20 | Purchased knife<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) | carry 1× [A strange looking dagger](../items/strange_dagger.md), carry 1× [A strange-looking gem](../items/strange_gem.md) | – |
| <span id="stage-30"></span>30 | purchased knife the hard way. | [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) | pay 1,000 gold, stage 10 | gives 1× [A strange looking dagger](../items/strange_dagger.md) |
| <span id="stage-40"></span>40 | purchased gem the hard way. | [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) | pay 1,500 gold, stage 20 | gives 1× [A strange-looking gem](../items/strange_gem.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 2 routes"

    1. stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) → the conversation leads here automatically — **conditions:** carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 10**
    2. stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) → the conversation leads here automatically — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md) → **stage 10**

???+ note "Stage 20: 2 routes"

    1. stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) → the conversation leads here automatically — **conditions:** carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 20**
    2. stepping on a trigger on [brimhaven_inn_east](../maps/brimhaven_inn_east.md) → the conversation leads here automatically — **conditions:** carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md) → **stage 20**

???+ note "Stage 30: 1 route"

    1. Talk to [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) → choose “I don't think it's fair, but I'll pay it.” — **conditions:** NOT reached stage 30 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); reached stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30); reached stage 10 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 20 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); pay 1,000 gold → **stage 30**; also gives 1× [A strange looking dagger](../items/strange_dagger.md). NPC: “Here you go kid.”

???+ note "Stage 40: 1 route"

    1. Talk to [Pixtumn](../monsters/quiet_thief.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) → choose “I don't think it's fair, but I'll pay it.” — **conditions:** NOT reached stage 40 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40); reached stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40); reached stage 20 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 10 of [brv_dagger_nondisplay (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); pay 1,500 gold → **stage 40**; also gives 1× [A strange-looking gem](../items/strange_gem.md). NPC: “Here you go kid”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_dagger_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40 |
    | Dialogue nodes setting stages | 10: `brv_thief_1`, 10: `brv_thief_2a`, 20: `brv_thief_2`, 20: `brv_thief_1a`, 30: `quiet_thief_2_4`, 40: `quiet_thief_3_4` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
