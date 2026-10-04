# Pond safety

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `sullengard_pond_safety` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 50) |
| **Started by** | [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) |
| **NPCs involved** | [Kealwea](../monsters/sullengard_priest.md), [Nanette](../monsters/sullengard_nanette.md) |
| **Locations** | [sullengard2_northwest_house](../maps/sullengard2_northwest_house.md), [sullengard_church](../maps/sullengard_church.md) |
| **Total XP** | 2,000 |
| **Related quests** | 1 |

</div>

## Overview

> Nanette was troubled that her pond is unsafe because of the monsters that emerged in the pond.

## Prerequisites to start

Start with [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)). Required:

- latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [mg2_exploded_star_nd (hidden flag)](mg2_exploded_star_nd.md#stage-91) | stage 91 reached, for stage 40 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Nanette was troubled that her pond is unsafe because of the monsters that emerged in the pond.  | [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) | – | – |
| <span id="stage-20"></span>20 | I accepted her request to clear out the monsters in her pond area so that she could enjoy the pond again. | [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | I have now cleared the pond area. Nanette told me that I should talk to Kaelwea, the priest of Sullengard, to see if he has some information about the cause of the monster's appearance in the pond area. | [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | The priest Kaelwea told me a story about his strange experience same as Nanette's experience in the pond area. I should better tell her the moral of the story. | [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | I told Nanette the moral of the story. She had already learned from her mistake and she promised never to do it again just to release her anger issue against the unfair taxes of Feygard. **(completes quest)** | [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) | stage 40 | 2,000 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) → the conversation leads here automatically — **conditions:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10 → **stage 10**. NPC: “[Sigh]. Please help me. For I'm longing to enjoy my pond again.”

???+ note "Stage 20: 1 route"

    1. Talk to [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) → choose “Fine. I'm going now.” — **conditions:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10 → **stage 20**. NPC: “Remember. It is just southeast from here.”

???+ note "Stage 30: 1 route"

    1. Talk to [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) → choose “Yes, your pond is safe again. May I know the cause of it?” — **conditions:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-20) is 20; killed 26× [Sullengard snapper](../monsters/sullengard_snapper.md) → **stage 30**. NPC: “I...I still don't know what's the cause of it. You should talk to Kealwea the priest about it.”

???+ note "Stage 40: 1 route"

    1. Talk to [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) → choose “I will listen to your story.” — **conditions:** reached stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91); reached stage 30 of [Pond safety](../quests/sullengard_pond_safety.md#stage-30); NOT reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40) → **stage 40**. NPC: “The moral of my story is to never again to throw rocks there, be it small or large. Thank you for listening. Please…”

???+ note "Stage 50: 1 route"

    1. Talk to [Nanette](../monsters/sullengard_nanette.md) ([sullengard2_northwest_house](../maps/sullengard2_northwest_house.md)) → choose “Don't throw pebbles into the pond. You might disturb whatever lies beneath the surface.” — **conditions:** reached stage 40 of [Pond safety](../quests/sullengard_pond_safety.md#stage-40) → **stage 50**. NPC: “Oh. I remember now. I kept throwing pebbles on the pond to relieve my anger issues caused by the unfair taxes of…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `sullengard_pond_safety` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `sullengard_nanette_4`, 20: `sullengard_nanette_5`, 30: `sullengard_nanette_8`, 40: `sullengard_kealwea_pond_safety_6`, 50: `sullengard_nanette_11` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
