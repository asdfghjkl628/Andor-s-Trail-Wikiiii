---
description: "Cheap cuts is a quest in Andor's Trail, started by Benbyr (crossroads). 5 stages, 900 XP in total. I have met Benbyr outside the Crossroads guardhouse. He wants to get revenge on an old 'business partner' of his - Tinlyn. Benbyr wants me to kill all Tinlyn's sheep."
---

# Cheap cuts

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `benbyr` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 30, 60) |
| **Started by** | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) |
| **NPCs involved** | [Benbyr](../monsters/benbyr.md), [Sheep](../monsters/sheep1.md#v-lostsheep2), [Sheep](../monsters/sheep1.md#v-lostsheep4), [Sheep](../monsters/sheep1.md#v-lostsheep3), [Sheep](../monsters/sheep1.md), [Sheep](../monsters/sheep1.md#v-lostsheep1) |
| **Locations** | [crossroads](../maps/crossroads.md), [fields1](../maps/fields1.md), [fields2](../maps/fields2.md), [fields3](../maps/fields3.md) |
| **Total XP** | 900 |
| **Related quests** | 2 |

</div>

## Overview

> I have met Benbyr outside the Crossroads guardhouse. He wants to get revenge on an old 'business partner' of his - Tinlyn. Benbyr wants me to kill all Tinlyn's sheep.

## Prerequisites to start

Start with [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)). Required:

- reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Lost sheep](tinlyn.md#stage-20) | stage 20 reached, for stage 21 here |
| Requires | [Lost sheep](tinlyn.md#stage-21) | stage 21 reached, for stage 21 here |
| Requires | [Lost sheep](tinlyn.md#stage-22) | stage 22 reached, for stage 21 here |
| Requires | [Lost sheep](tinlyn.md#stage-23) | stage 23 reached, for stage 21 here |
| Unlocks | [Lost sheep](tinlyn.md#stage-60) | stage 60 there needs stages 20, 21 here |
| Unlocks | [It makes no fence](tunlon_fence.md#stage-40) | stage 40 there needs stage 21 here |
| Unlocks | [It makes no fence](tunlon_fence.md#stage-110) | stage 110 there needs stage 21 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I have met Benbyr outside the Crossroads guardhouse. He wants to get revenge on an old 'business partner' of his - Tinlyn. Benbyr wants me to kill all Tinlyn's sheep. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 20 | – |
| <span id="stage-20"></span>20 | I have agreed to help Benbyr find Tinlyn's sheep and kill all eight of them. I should go look for them in the fields northwest of the Crossroads guardhouse. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | – | – |
| <span id="stage-21"></span>21 | I have started attacking the sheep. I should return to Benbyr once I have killed all eight of them. | [Sheep](../monsters/sheep1.md#v-lostsheep1) ([fields1](../maps/fields1.md))<br>[Sheep](../monsters/sheep1.md#v-lostsheep2) ([fields2](../maps/fields2.md))<br>[Sheep](../monsters/sheep1.md#v-lostsheep3) ([fields3](../maps/fields3.md))<br>+2 more | stage 20 | – |
| <span id="stage-30"></span>30 | Benbyr was thrilled to hear that all of Tinlyn's sheep are dead. **(completes quest)** | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | hand over 8× [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md), stage 20 | 900 XP |
| <span id="stage-60"></span>60 | I declined to help Benbyr kill the sheep. **(completes quest)** | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 20 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Can you tell me your story again?” — **conditions:** reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 10**. NPC: “Do this, and I will have avenged that fool Tinlyn.”

???+ note "Stage 20: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Sounds like just my type of thing. I'll do it!” — **conditions:** reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 20**. NPC: “Splendid!”

???+ note "Stage 21: 5 routes"

    1. Talk to [Sheep](../monsters/sheep1.md#v-lostsheep1) ([fields1](../maps/fields1.md)) → choose “[Attack]” — **conditions:** reached stage 20 of [Lost sheep](../quests/tinlyn.md#stage-20); reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 21**
    2. Talk to [Sheep](../monsters/sheep1.md#v-lostsheep2) ([fields2](../maps/fields2.md)) → choose “[Attack]” — **conditions:** reached stage 21 of [Lost sheep](../quests/tinlyn.md#stage-21); reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 21**
    3. Talk to [Sheep](../monsters/sheep1.md#v-lostsheep3) ([fields3](../maps/fields3.md)) → choose “[Attack]” — **conditions:** reached stage 22 of [Lost sheep](../quests/tinlyn.md#stage-22); reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 21**
    4. Talk to [Sheep](../monsters/sheep1.md#v-lostsheep4) ([loneford1](../maps/loneford1.md)) → choose “[Attack]” — **conditions:** reached stage 23 of [Lost sheep](../quests/tinlyn.md#stage-23); reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 21**
    5. Talk to [Sheep](../monsters/sheep1.md) ([fields6](../maps/fields6.md)) → choose “[Attack]” — **conditions:** reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 21**

???+ note "Stage 30: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “I have slain all eight of Tinlyn's sheep for you.” — **conditions:** reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20); hand over 8× [Meat from Tinlyn's sheep](../items/tinlyn_sheep_meat.md) → **stage 30**. NPC: “Ha ha! That fool Tinlyn must be in tears. The Shadow surely walks with you my friend.”

???+ note "Stage 60: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “No way, killing innocent sheep is beneath me. I will never do your task.” — **conditions:** reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20) → **stage 60**. NPC: “Very well, but remember that I have my eyes on you ... adventurer.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | stage 20 journal text changed<br>Dialogue: 1 line changed<br>· text: “Very well, but remember that I have my eyes on you.. adventurer.” → “Very well, but remember that I have my eyes on you ... adventurer.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=benbyr.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=benbyr.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=benbyr.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=benbyr.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=benbyr.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `benbyr` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 60 |
    | Dialogue nodes setting stages | 10: `benbyr_story_13`, 20: `benbyr_accept_1`, 21: `tinlyn_sheep_atk`, 30: `benbyr_mission_2`, 60: `benbyr_decline_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
