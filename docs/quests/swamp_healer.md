# The swamp healer

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `swamp_healer` |
| **In journal** | Yes |
| **Stages** | 3 (completes at 30) |
| **Started by** | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) |
| **NPCs involved** | [Vaelric](../monsters/vaelric.md) |
| **Locations** | [galmore_17_house](../maps/galmore_17_house.md) |
| **Total XP** | 2,449 |
| **Related quests** | 2 |

</div>

## Overview

> I encountered Vaelric, a reclusive healer living in the swamp between Mt. Galmore and Stoutford. He refused to help me unless I dealt with a dangerous creature corrupting his medicinal pools.

## Prerequisites to start

Start with [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)). Required:

- NOT reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Blocked by | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-59) | stage 59 must NOT be reached, for stage 30 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-10) | stage 10 there needs stage 10 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-59) | stage 59 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-10) | stage 10 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-20) | stage 20 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-63) | stage 63 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-70) | stage 70 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-80) | stage 80 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-95) | stage 95 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-97) | stage 97 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-115) | stage 115 there needs stage 30 here |
| Unlocks | [Restless in the grave](mg_restless_grave.md#stage-120) | stage 120 there needs stage 30 here |
| Blocks | [Restless in the grave](mg_restless_grave.md#stage-15) | reaching stage 30 here closes stage 15 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I encountered Vaelric, a reclusive healer living in the swamp between Mt. Galmore and Stoutford. He refused to help me unless I dealt with a dangerous creature corrupting his medicinal pools. | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | – | spawns monsters on galmore_28 |
| <span id="stage-20"></span>20 | I defeated the monstrous creature that I found on Vaelric's land. This creature was enormous and venomous, feeding on the lifeblood of the swamp.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 28](../maps/galmore_28.md).</span> | stepping on a trigger on [galmore_28](../maps/galmore_28.md) | – | – |
| <span id="stage-30"></span>30 | Vaelric rewarded me for my efforts by teaching me how to use leeches to heal bleeding wounds. He warned me to save them for dire situations and respect their power. **(completes quest)** | [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) | – | 2,449 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “What kind of creature?” — **conditions:** NOT reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10) → **stage 10**; also spawns monsters on galmore_28. NPC: “A swamp creature, but far from the kind you'd expect to see. This one is massive, venomous, and ravenous. It's…”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [galmore_28](../maps/galmore_28.md) → the conversation leads here automatically — **conditions:** killed 1× [Venomous swamp creature](../monsters/venomous_swamp_creature.md); NOT reached stage 20 of [The swamp healer](../quests/swamp_healer.md#stage-20) → **stage 20**. NPC: “It's time to revisit Vaelric.”

???+ note "Stage 30: 1 route"

    1. Talk to [Vaelric](../monsters/vaelric.md) ([galmore_17_house](../maps/galmore_17_house.md)) → choose “Can you teach me?” — **conditions:** reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); NOT reached stage 59 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59) → **stage 30**. NPC: “See how the leech attaches itself? It draws out the bad humors, cleansing the blood. Placement is everything. Here,…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=swamp_healer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=swamp_healer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=swamp_healer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=swamp_healer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=swamp_healer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `swamp_healer` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30 |
    | Dialogue nodes setting stages | 10: `vaelric_alone_40`, 20: `galmore_swamp_creature_defeated_10`, 30: `vaelric_creature_killed_40` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
