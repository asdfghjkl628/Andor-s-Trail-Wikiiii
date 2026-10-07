---
description: "Brutes is a quest in Andor's Trail, started by Bidro (mountainlake11). 6 stages, 2,000 XP in total. I have met Bidro, a fisherman on the long way to Remgard. He wondered why only few people come along nowadays."
---

# Brutes

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brute_creator` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 90) |
| **Started by** | [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) |
| **NPCs involved** | [Bidro](../monsters/brute_fisherman.md), [Os](../monsters/brute_creator.md) |
| **Locations** | [mountainlake11](../maps/mountainlake11.md), [mountainlake8_cave](../maps/mountainlake8_cave.md) |
| **Total XP** | 2,000 |

</div>

## Overview

> I have met Bidro, a fisherman on the long way to Remgard. He wondered why only few people come along nowadays.

## Prerequisites to start

Start with [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)). Required:

- reached stage 10 of [Brutes](../quests/brute_creator.md#stage-10)
- NOT reached stage 30 of [Brutes](../quests/brute_creator.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I have met Bidro, a fisherman on the long way to Remgard. He wondered why only few people come along nowadays. | [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) | – | – |
| <span id="stage-20"></span>20 | I told Bidro about the many nasty monsters along the way.<br><span class="qnote">🗺️ Part of [Mountainlake8](../maps/mountainlake8.md) visibly changes.</span> | [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) | – | – |
| <span id="stage-30"></span>30 | I have discovered a cave where brutes seem to pour out.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Mountainlake8 cave](../maps/mountainlake8_cave.md).</span> | stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) | – | faction “brute_creator_flash” set to 1<br>sets stage 201 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-201)<br>faction “brute_creator_flash” set to 2 |
| <span id="stage-35"></span>35 | Then I have told Bidro about this cave full of brutes. | [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) | stage 30 | – |
| <span id="stage-40"></span>40 | I have talked to Os, a scientist about brute matters. He has built up a brute production facility. | [Os](../monsters/brute_creator.md) ([mountainlake8_cave](../maps/mountainlake8_cave.md)) | – | – |
| <span id="stage-90"></span>90 | I told Bidro what I have learned from Os. He thanked me for this new story he could tell his wife. **(completes quest)** | [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) | stage 35, stage 40 | 2,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) → choose “About the few people who come this way ...” — **conditions:** reached stage 10 of [Brutes](../quests/brute_creator.md#stage-10); NOT reached stage 30 of [Brutes](../quests/brute_creator.md#stage-30) → **stage 10**. NPC: “So what's stopping people from using the route?”

???+ note "Stage 20: 1 route"

    1. Talk to [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) → choose “About the monsters along the way here ...” — **conditions:** reached stage 20 of [Brutes](../quests/brute_creator.md#stage-20); NOT reached stage 30 of [Brutes](../quests/brute_creator.md#stage-30) → **stage 20**. NPC: “Have you been able to find out why the path is rarely used anymore?”

???+ note "Stage 30: 2 routes"

    1. stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) → the conversation leads here automatically — **conditions:** random chance (3%) → **stage 30**; also faction “brute_creator_flash” set to 1, sets stage 201 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-201)
    2. stepping on a trigger on [mountainlake8_cave](../maps/mountainlake8_cave.md) → the conversation leads here automatically — **conditions:** random chance (5%) → **stage 30**; also faction “brute_creator_flash” set to 2, sets stage 201 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-201)

???+ note "Stage 35: 1 route"

    1. Talk to [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) → choose “I have discovered a cave where brutes seem to pour out.” — **conditions:** reached stage 30 of [Brutes](../quests/brute_creator.md#stage-30); NOT reached stage 35 of [Brutes](../quests/brute_creator.md#stage-35) → **stage 35**. NPC: “Oh interesting. What did you find in the cave?”

???+ note "Stage 40: 1 route"

    1. Talk to [Os](../monsters/brute_creator.md) ([mountainlake8_cave](../maps/mountainlake8_cave.md)) → choose “That is understandable.” → **stage 40**. NPC: “I'll just say that my brutes evolve from rats. There are too many of them anyway.”

???+ note "Stage 90: 1 route"

    1. Talk to [Bidro](../monsters/brute_fisherman.md) ([mountainlake11](../maps/mountainlake11.md)) → choose “There are several bake rooms where the animals take on an even more hideous appearance. Until they finally…” — **conditions:** reached stage 35 of [Brutes](../quests/brute_creator.md#stage-35); reached stage 40 of [Brutes](../quests/brute_creator.md#stage-40); NOT reached stage 90 of [Brutes](../quests/brute_creator.md#stage-90) → **stage 90**. NPC: “Wow, what a great story!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brute_creator.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brute_creator.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brute_creator.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brute_creator.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brute_creator.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brute_creator` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 90 |
    | Dialogue nodes setting stages | 10: `brute_fisherman_10`, 20: `brute_fisherman_20`, 30: `brute_creator_flash_1`, 30: `brute_creator_flash_2`, 35: `brute_fisherman_32`, 40: `brute_creator_30`, 90: `brute_fisherman_50` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
