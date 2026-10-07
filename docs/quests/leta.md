---
description: "Missing husband is a quest in Andor's Trail, started by Leta. 13 stages, 520 XP in total. Leta in Crossglen village wants me to look for her husband Oromir."
---

# Missing husband

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `leta` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 100, 105) |
| **Started by** | [Leta](../monsters/leta.md), [Leta](../monsters/leta.md) |
| **NPCs involved** | [Leta](../monsters/leta.md), [Oromir](../monsters/oromir.md#v-oromir_behind_inn_help), [Oromir](../monsters/oromir.md#v-oromir_behind_haystack), [Oromir](../monsters/oromir.md#v-oromir_basement), [Oromir](../monsters/oromir.md#v-oromir_basement_help), [Oromir](../monsters/oromir.md#v-oromir_behind_inn) +2 |
| **Locations** | [crossglen](../maps/crossglen.md), [crossglen_farmhouse_basement](../maps/crossglen_farmhouse_basement.md) |
| **Total XP** | 520 |
| **Related quests** | 1 |

</div>

## Overview

> Leta in Crossglen village wants me to look for her husband Oromir.

## Prerequisites to start

**Route 1** ([Leta](../monsters/leta.md)):

- NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105)
- NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100)

**Route 2** ([Leta](../monsters/leta.md)):

- NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105)
- NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100)
- reached stage 25 of [Missing husband](../quests/leta.md#stage-25)
- NOT reached stage 35 of [Missing husband](../quests/leta.md#stage-35)
- NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45)

**Route 3** ([Leta](../monsters/leta.md)):

- NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105)
- NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100)
- reached stage 35 of [Missing husband](../quests/leta.md#stage-35)
- NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45)

**Route 4** ([Leta](../monsters/leta.md)):

- NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105)
- NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100)
- reached stage 45 of [Missing husband](../quests/leta.md#stage-45)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [A familiar shadow](familiar_shadow.md#stage-10) | stage 10 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Leta in Crossglen village wants me to look for her husband Oromir. | [Leta](../monsters/leta.md) | stage 25, stage 35, stage 45 | removes monsters from crossglen<br>spawns monsters on crossglen<br>spawns monsters on crossglen_farmhouse_basement |
| <span id="stage-20"></span>20 | I have found Oromir in Crossglen village, hiding from his wife Leta. | [Oromir](../monsters/oromir.md) ([crossglen](../maps/crossglen.md)) | – | – |
| <span id="stage-25"></span>25 | I have found Oromir in Crossglen village, hiding from his wife Leta, but I promised him that I would not tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md) ([crossglen](../maps/crossglen.md)) | – | 50 XP |
| <span id="stage-30"></span>30 | Leta asked me to tell Oromir to come home and help her with the housework. | [Leta](../monsters/leta.md) | stage 20 | 80 XP<br>removes monsters from crossglen<br>spawns monsters on crossglen |
| <span id="stage-35"></span>35 | I have found Oromir behind the Crossglen village inn, hiding from his wife Leta, but I promised him that I would not tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md#v-oromir_behind_inn_help) ([crossglen](../maps/crossglen.md)) | – | 50 XP |
| <span id="stage-40"></span>40 | I have found Oromir behind the Crossglen village inn, hiding from his wife Leta, but I should tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md#v-oromir_behind_inn) ([crossglen](../maps/crossglen.md)) | – | – |
| <span id="stage-45"></span>45 | I have found Oromir in Crossglen village behind a haystack, hiding from his wife Leta, but I promised him that I would not tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md#v-oromir_behind_haystack_help) ([crossglen](../maps/crossglen.md)) | – | 50 XP |
| <span id="stage-50"></span>50 | Leta asked me to tell Oromir to come home and help her with the housework. | [Leta](../monsters/leta.md) | stage 40 | 80 XP<br>removes monsters from crossglen<br>spawns monsters on crossglen |
| <span id="stage-60"></span>60 | I have found Oromir in Crossglen village behind a haystack, hiding from his wife Leta, I should tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md#v-oromir_behind_haystack) ([crossglen](../maps/crossglen.md)) | – | – |
| <span id="stage-70"></span>70 | Leta asked me to tell Oromir to come home and help her with the housework. | [Leta](../monsters/leta.md) | stage 60 | 80 XP<br>removes monsters from crossglen<br>spawns monsters on crossglen_farmhouse_basement |
| <span id="stage-80"></span>80 | I have found Oromir in the basement of his house, hiding from his wife Leta, I should tell Leta of his whereabouts. | [Oromir](../monsters/oromir.md#v-oromir_basement) ([crossglen_farmhouse_basement](../maps/crossglen_farmhouse_basement.md)) | – | – |
| <span id="stage-100"></span>100 | I have told Leta that Oromir is hiding in their basement. **(completes quest)** | [Leta](../monsters/leta.md) | stage 80 | 80 XP |
| <span id="stage-105"></span>105 | Even after all my help, Oromir was still brought back home to Leta. **(completes quest)** | [Oromir](../monsters/oromir.md#v-oromir_basement_help) ([crossglen_farmhouse_basement](../maps/crossglen_farmhouse_basement.md)) | stage 45 | 50 XP<br>gives 1× [Kid's boots](../items/kids_boots.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 4 routes"

    1. Talk to [Leta](../monsters/leta.md) → choose “I have no idea.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100) → **stage 10**. NPC: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!”
    2. Talk to [Leta](../monsters/leta.md) → choose “[Lie] I have no idea.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 25 of [Missing husband](../quests/leta.md#stage-25); NOT reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45) → **stage 10**; also removes monsters from crossglen, spawns monsters on crossglen. NPC: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!”
    3. Talk to [Leta](../monsters/leta.md) → choose “[Lie] I have no idea.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45) → **stage 10**; also removes monsters from crossglen, spawns monsters on crossglen. NPC: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!”
    4. Talk to [Leta](../monsters/leta.md) → choose “[Lie] I have no idea.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 45 of [Missing husband](../quests/leta.md#stage-45) → **stage 10**; also removes monsters from crossglen, spawns monsters on crossglen_farmhouse_basement. NPC: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!”

???+ note "Stage 20: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md) ([crossglen](../maps/crossglen.md)) → choose “Hello.” → **stage 20**. NPC: “I'm hiding here from my wife Leta. She is always getting angry at me for not helping out on the farm. Please don't…”

???+ note "Stage 25: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md) ([crossglen](../maps/crossglen.md)) → choose “Your secret is safe with me.” — **conditions:** NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100) → **stage 25**. NPC: “Thank you, friend.”

???+ note "Stage 30: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “Yes, I found him. He is hiding among some trees to the east.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 20 of [Missing husband](../quests/leta.md#stage-20); NOT reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45); NOT reached stage 40 of [Missing husband](../quests/leta.md#stage-40); NOT reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80); NOT reached stage 25 of [Missing husband](../quests/leta.md#stage-25) → **stage 30**; also removes monsters from crossglen, spawns monsters on crossglen. NPC: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.”

???+ note "Stage 35: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_behind_inn_help) ([crossglen](../maps/crossglen.md)) → choose “That's a wise move because she has asked me to inform her of your whereabouts. But I won't do so.” → **stage 35**. NPC: “Thank you, friend.”

???+ note "Stage 40: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_behind_inn) ([crossglen](../maps/crossglen.md)) → choose “You are needed at home.” → **stage 40**. NPC: “I see.”

???+ note "Stage 45: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_behind_haystack_help) ([crossglen](../maps/crossglen.md)) → choose “That's a wise move because she has asked me to inform her of your whereabouts. But I won't do so.” → **stage 45**. NPC: “Thank you, friend.”

???+ note "Stage 50: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “Tucked away between the back of the inn and the woods.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 40 of [Missing husband](../quests/leta.md#stage-40); NOT reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80) → **stage 50**; also removes monsters from crossglen, spawns monsters on crossglen. NPC: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.”

???+ note "Stage 60: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_behind_haystack) ([crossglen](../maps/crossglen.md)) → choose “A happy wife is a happy life. Go home.” → **stage 60**. NPC: “No thanks. I'm staying here.”

???+ note "Stage 70: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “Hiding behind a haystack.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80) → **stage 70**; also removes monsters from crossglen, spawns monsters on crossglen_farmhouse_basement. NPC: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.”

???+ note "Stage 80: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_basement) ([crossglen_farmhouse_basement](../maps/crossglen_farmhouse_basement.md)) → choose “I'm sorry, but I think that it's better if I'm on Leta's side.” → **stage 80**. NPC: “Yep. That's something that I've not learnt to do.”

???+ note "Stage 100: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “He's in your basement.” — **conditions:** NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 80 of [Missing husband](../quests/leta.md#stage-80) → **stage 100**. NPC: “What?! How? Oh, it doesn't matter. Thank you for finding him.”

???+ note "Stage 105: 1 route"

    1. Talk to [Oromir](../monsters/oromir.md#v-oromir_basement_help) ([crossglen_farmhouse_basement](../maps/crossglen_farmhouse_basement.md)) → choose “I'm sorry to hear that.” — **conditions:** reached stage 45 of [Missing husband](../quests/leta.md#stage-45); NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105) → **stage 105**; also gives 1× [Kid's boots](../items/kids_boots.md). NPC: “While cleaning, I found your kid brother's boots. Please take them as my gift to you for all of your help.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.10](../versions/0.7.10.md) | Stage 100 XP 50 → 80 |
| [v0.7.12](../versions/0.7.12.md) | Stages added: 25, 30, 35, 40, 45, 50, 60, 70, 80, 105<br>Stage 100 journal text changed<br>Dialogue: 14 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=leta.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=leta.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=leta.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=leta.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=leta.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `leta` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 105 |
    | Dialogue nodes setting stages | 10: `leta_oromir2`, 10: `leta_oromir1_trees_help`, 10: `leta_oromir1_behind_inn_help`, 20: `oromir2`, 25: `oromir_trees_help_10`, 30: `leta_oromir1_trees`, 35: `oromir_behind_inn_help_20`, 40: `oromir_behind_inn_20`, 45: `oromir_behind_haystack_help_20`, 50: `leta_oromir1_behind_inn_20`, 60: `oromir_behind_haystack_20`, 70: `leta_oromir1_behind_haystack_20`, 80: `oromir_basement_20`, 100: `leta_oromir_complete`, 100: `leta_oromir1_basement_10`, 105: `oromir_basement_help_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
