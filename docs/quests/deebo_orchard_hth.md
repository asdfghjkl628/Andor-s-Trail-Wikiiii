# Hunting the hunter

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `deebo_orchard_hth` |
| **In journal** | Yes |
| **Stages** | 4 (completes at 50) |
| **Started by** | [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) |
| **NPCs involved** | [Deebo](../monsters/deebo_orchard_deebo.md) |
| **Locations** | [sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md) |
| **Total XP** | 10,000 |
| **Related quests** | 1 |

</div>

## Overview

> Deebo, the apple orchard farmer northeast of Sullengard informed me of a Golden jackal that is wreaking havoc in his orchard.

## Prerequisites to start

Start with [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)). Required:

- NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50)
- latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Mutually exclusive | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-4) | stage 4 must NOT be reached, for stage 10 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-4) | stage 4 there needs stage 0 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-0"></span>0 | Deebo, the apple orchard farmer northeast of Sullengard informed me of a Golden jackal that is wreaking havoc in his orchard. | [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) | – | – |
| <span id="stage-10"></span>10 | I accepted the challenge of tracking down the Golden jackal and bringing back proof to Deebo that I have killed it. | [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) | stage 0 | sets stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4) |
| <span id="stage-40"></span>40 | I killed the Golden jackal. I need to return to Deebo with the Golden jackal's fur as proof that I've killed it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard west ravine](../maps/sullengard_west_ravine.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods gj1](../maps/sullengard_woods_gj1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods12](../maps/sullengard_woods12.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods4](../maps/sullengard_woods4.md).</span> | stepping on a trigger on [sullengard_west_ravine](../maps/sullengard_west_ravine.md) | – | – |
| <span id="stage-50"></span>50 | I returned to Deebo with the killed the Golden jackal's fur as proof that I had killed it. He was now willing to trade with me. **(completes quest)** | [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) | hand over 1× [Golden jackal fur](../items/golden_jackal_fur.md), stage 40 | 10,000 XP<br>gives 1× [Golden jackal fur](../items/golden_jackal_fur.md) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 0: 1 route"

    1. Talk to [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) → choose “I want to hunt down and kill that Golden jackal for you.” — **conditions:** NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0 → **stage 0**. NPC: “That's great to hear! When can you start?”

???+ note "Stage 10: 2 routes"

    1. Talk to [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) → choose “I am ready! No more talking.” — **conditions:** NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0; NOT reached stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4); random chance (30%) → **stage 10**; also sets stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4). NPC: “The Golden jackal was last seen heading back into the "Sullengard forest" just to the west of my orchard. Return to me…”
    2. Talk to [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) → choose “I am ready! No more talking.” — **conditions:** NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0; NOT reached stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4) → **stage 10**

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [sullengard_west_ravine](../maps/sullengard_west_ravine.md) → the conversation leads here automatically — **conditions:** killed 1× [Golden jackal](../monsters/golden_jackal.md); NOT reached stage 40 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-40) → **stage 40**. NPC: “[The Golden jackal has perished.]”

???+ note "Stage 50: 1 route"

    1. Talk to [Deebo](../monsters/deebo_orchard_deebo.md) ([sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)) → choose “I have killed the Golden jackal and I have the requested proof.” — **conditions:** NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50); hand over 1× [Golden jackal fur](../items/golden_jackal_fur.md); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-40) is 40 → **stage 50**; also gives 1× [Golden jackal fur](../items/golden_jackal_fur.md). NPC: “Wonderful. Let me have it. [You hand over the Golden jackal's fur] Ah yes, this is indeed proof it is dead.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `deebo_orchard_hth` |
    | showInLog | 1 |
    | Stage IDs | 0, 10, 40, 50 |
    | Dialogue nodes setting stages | 0: `deebo_orchard_deebo_50`, 10: `deebo_orchard_deebo_80`, 10: `deebo_orchard_deebo_spawn_gj`, 40: `jackal_defeted_script_20`, 50: `deebo_orchard_deebo_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
