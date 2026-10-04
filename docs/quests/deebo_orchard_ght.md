# Getting home on time

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `deebo_orchard_ght` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 60) |
| **Started by** | [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) |
| **NPCs involved** | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md), [Hadena](../monsters/sullengard_cabin_wife.md), [Throthaus](../monsters/throthaus.md) |
| **Locations** | [loneford15](../maps/loneford15.md), [sullengard_apple_farm_west](../maps/sullengard_apple_farm_west.md), [sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md) |
| **Total XP** | 5,000 |
| **Related quests** | 1 |

</div>

## Overview

> Hadena needed my help to get her husband Ainsley home on time.

## Prerequisites to start

Start with [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)). Required:

- NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-100) | stage 100 there needs stage 30 here |
| Blocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-16) | reaching stage 10 here closes stage 16 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Hadena needed my help to get her husband Ainsley home on time. | [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) | – | – |
| <span id="stage-20"></span>20 | I agreed to help Hadena with getting her husband Ainsley home on time. He was working at Deebo's Orchard located southwest of their cabin. | [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) | stage 10 | – |
| <span id="stage-25"></span>25 | Due to the vast distance to Loneford and the monsters that he would encounter along the way, Ainsley has asked me to go to Loneford and get him a new pitchfork. | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) ([sullengard_apple_farm_west](../maps/sullengard_apple_farm_west.md)) | stage 20 | – |
| <span id="stage-30"></span>30 | Throthaus wanted me to pull out his pitchfork from the haystack to prove that I'm a son of a farmer. | [Throthaus](../monsters/throthaus.md) ([loneford15](../maps/loneford15.md)) | stage 25 | – |
| <span id="stage-40"></span>40 | I successfully pulled out the pitchfork. It's time to visit Ainsley again who's working on Deebo's Orchard. | walking into a blocked passage on [loneford13](../maps/loneford13.md) | stage 30 | sets stage 100 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-100)<br>gives 1× [Farmer's pitchfork](../items/farmer_pitchfork.md)<br>applies condition fatigue4 |
| <span id="stage-50"></span>50 | I gave Ainsley the new pitchfork. I should tell Hadena about this. | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) ([sullengard_apple_farm_west](../maps/sullengard_apple_farm_west.md)) | – | – |
| <span id="stage-60"></span>60 | Hadena was so grateful to me for helping them. **(completes quest)** | [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) | stage 50 | 5,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) → choose “So, my brother Andor was here as well? I'm $playername and you are?” — **conditions:** NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) → **stage 10**. NPC: “Oh, I'm sorry. My name is Hadena. Andor used to visit here but I don't know why he doesn't anymore. Anyways, I really…”

???+ note "Stage 20: 1 route"

    1. Talk to [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) → choose “I'm sorry because I was only half listening to you earlier, so I am a little fuzzy on the details. But can…” — **conditions:** NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10); latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10 → **stage 20**. NPC: “He is working at Deebo's Orchard located southwest of here. Please go there and help him.”

???+ note "Stage 25: 1 route"

    1. Talk to [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) ([sullengard_apple_farm_west](../maps/sullengard_apple_farm_west.md)) → choose “Especially for a farmer. Trust me, I know.” — **conditions:** NOT reached stage 50 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50); latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-20) is 20 → **stage 25**. NPC: “Anyways, I would really appreciate it if you would go to Loneford and get the pitchfork.”

???+ note "Stage 30: 1 route"

    1. Talk to [Throthaus](../monsters/throthaus.md) ([loneford15](../maps/loneford15.md)) → choose “No. But I'm a child of an ordinary farmer in a small settlement called Crossglen.” — **conditions:** latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-25) is 25 → **stage 30**. NPC: “If you are able to pull it out from the haystack, then it will be yours.”

???+ note "Stage 40: 1 route"

    1. walking into a blocked passage on [loneford13](../maps/loneford13.md) → choose “Time to prove that I'm the child of farmer!” — **conditions:** reached stage 30 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-30) → **stage 40**; also sets stage 100 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-100), gives 1× [Farmer's pitchfork](../items/farmer_pitchfork.md), applies condition fatigue4. NPC: “After several minutes of intense pulling you finally pull out the new pitchfork from the haystack.”

???+ note "Stage 50: 1 route"

    1. Talk to [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) ([sullengard_apple_farm_west](../maps/sullengard_apple_farm_west.md)) → the conversation leads here automatically → **stage 50**. NPC: “Thank you so much, kid. Tell my wife Hadena I can come home on time today.”

???+ note "Stage 60: 1 route"

    1. Talk to [Hadena](../monsters/sullengard_cabin_wife.md) ([sullengard_ravine_cabin](../maps/sullengard_ravine_cabin.md)) → choose “It is done. Ainsley will be home on time today.” — **conditions:** NOT reached stage 60 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-60); latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50) is 50 → **stage 60**. NPC: “Thank you so much for helping us. You are just like your brother.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.4](../versions/0.8.4.md) | stage 40 journal text changed |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `deebo_orchard_ght` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `sullengard_hadena_1`, 20: `sullengard_hadena_4`, 25: `ainsley_goto_loneford_40`, 30: `throthaus_6`, 40: `loneford13_pitchfork_success`, 50: `sullengard_ainsley_3`, 60: `sullengard_hadena_7` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
