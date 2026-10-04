# Where is Norry?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `hettar_dog` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 80, 90) |
| **Started by** | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) |
| **NPCs involved** | [Little Hettar](../monsters/hettar.md), [Wolfhound](../monsters/hettar_dog.md) |
| **Locations** | [blackwater_mountain55](../maps/blackwater_mountain55.md) |
| **Total XP** | 2,200 |
| **Related quests** | 1 |

</div>

## Overview

> I found Hettar, a tough boy about my age, on top of Blackwater mountain. He kept calling for a certain Norry.

## Prerequisites to start

None: talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [hettar_dog_nd (hidden flag)](hettar_dog_nd.md#stage-2) | stage 2 reached, for stage 40 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I found Hettar, a tough boy about my age, on top of Blackwater mountain. He kept calling for a certain Norry. | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | – |
| <span id="stage-20"></span>20 | Hettar's little dog Norry has run away. He was very anxious to find him. I promised to get Norry back. | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | removes monsters from blackwater_mountain55<br>spawns monsters on blackwater_mountain55 |
| <span id="stage-30"></span>30 | Hettar has given me a piece of Norry's favorite food. | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 20 | gives 1× [Wyrm meat](../items/hettar_bone.md) |
| <span id="stage-40"></span>40 | I have offered Hettar's piece of Wyrm meat to Norry, who took it eagerly. | [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | hand over 1× [Wyrm meat](../items/hettar_bone.md) | sets stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2) |
| <span id="stage-50"></span>50 | Norry ran off to reunite with Hettar. | [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 40 | removes monsters from blackwater_mountain55<br>spawns monsters on blackwater_mountain55 |
| <span id="stage-80"></span>80 | Hettar thanked me a thousand times for my help in finding Norry. **(completes quest)** | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 50 | 2,000 XP |
| <span id="stage-90"></span>90 | I explained to Hettar that I killed Norry. Hettar broke down on the floor in agony. **(completes quest)** | [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | stage 30 | 200 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Who is Norry?” → **stage 10**. NPC: “Norry is my little doggie. He fell down the steep slope and has not found his way back yet.”

???+ note "Stage 20: 1 route"

    1. Talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “OK, I'll do it.” — **conditions:** reached stage 20 of [Where is Norry?](../quests/hettar_dog.md#stage-20); NOT killed 1× [Wolfhound](../monsters/hettar_dog3.md) → **stage 20**; also removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55. NPC: “Great! Go immediately, as long as he might be alive still.”

???+ note "Stage 30: 1 route"

    1. Talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “I hope he will follow me.” — **conditions:** reached stage 20 of [Where is Norry?](../quests/hettar_dog.md#stage-20); NOT killed 1× [Wolfhound](../monsters/hettar_dog3.md); NOT reached stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30) → **stage 30**; also gives 1× [Wyrm meat](../items/hettar_bone.md). NPC: “Good that you have mentioned it. I'll give you a nice raw piece of Wyrm meat that I have as food for Norry. He loves…”

???+ note "Stage 40: 1 route"

    1. Talk to [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Hey Norry, look here! I have some much better food for you from Hettar.” — **conditions:** hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2) → **stage 40**; also sets stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2). NPC: “The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.”

???+ note "Stage 50: 1 route"

    1. Talk to [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Now run to Hettar! He is waiting for you.” — **conditions:** reached stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40) → **stage 50**; also removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55. NPC: “A moment later the huge wolfhound was gone.”

???+ note "Stage 80: 1 route"

    1. Talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Now guess who had persuaded him to do so? He was absorbed by a pile of monster bones.” — **conditions:** reached stage 50 of [Where is Norry?](../quests/hettar_dog.md#stage-50) → **stage 80**. NPC: “Oh. Thank you then.”

???+ note "Stage 90: 1 route"

    1. Talk to [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “This brute attacked me, so I had to kill it.” — **conditions:** reached stage 30 of [Where is Norry?](../quests/hettar_dog.md#stage-30); killed 1× [Wolfhound](../monsters/hettar_dog3.md) → **stage 90**. NPC: “[Hettar fell on the floor] Nooo! What did you do?!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 7 lines added |
| [v0.7.15](../versions/0.7.15.md) | stage 30 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `hettar_dog` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 80, 90 |
    | Dialogue nodes setting stages | 10: `hettar_1_2`, 20: `hettar_20_10`, 30: `hettar_20_30`, 40: `hettar_dog_10`, 50: `hettar_dog_20`, 80: `hettar_50_10`, 90: `hettar_10_6` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
