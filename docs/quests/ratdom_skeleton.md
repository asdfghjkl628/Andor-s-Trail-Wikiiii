---
description: "Skeleton brothers is a quest in Andor's Trail, started by Roskelt (ratdom_maze_415). 9 stages, 1,000 XP in total. Roskelt, the leader of a gang of skeletons, claimed to be king of the caves. He demanded that I would seek out his brother and bring him a message: if he came and surrendered, then he…"
---

# Skeleton brothers

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ratdom_skeleton` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 90) |
| **Started by** | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) |
| **NPCs involved** | [Bloskelt](../monsters/ratdom_skeleton_boss2.md), [Roskelt](../monsters/ratdom_skeleton_boss1.md) |
| **Locations** | [ratdom_maze_415](../maps/ratdom_maze_415.md), [ratdom_maze_416](../maps/ratdom_maze_416.md) |
| **Total XP** | 1,000 |
| **Related quests** | 1 |

</div>

## Overview

> Roskelt, the leader of a gang of skeletons, claimed to be king of the caves. He demanded that I would seek out his brother and bring him a message: if he came and surrendered, then he would have the grace of a quick, almost painless death.

## Prerequisites to start

Start with [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)). Required:

- NOT reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62)
- NOT reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Yellow is it](ratdom_quest.md#stage-37) | stage 37 there needs stages 61, 62, 71, 72 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-41"></span>41 | Roskelt, the leader of a gang of skeletons, claimed to be king of the caves. He demanded that I would seek out his brother and bring him a message: if he came and surrendered, then he would have the grace of a quick, almost painless death. | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) | – | – |
| <span id="stage-42"></span>42 | Bloskelt, the leader of a gang of skeletons, claimed to be king of the caves. He demanded that I would seek out his brother and bring him a message: if he came and surrendered, then he would have the grace of a quick, almost painless death. | [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) | – | – |
| <span id="stage-51"></span>51 | Bloskelt, a leader of another gang of skeletons, also had claimed to be king of the caves. I delivered Roskelt's message, but earned nothing but laughter. | [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) | stage 41 | – |
| <span id="stage-52"></span>52 | Roskelt, a leader of another gang of skeletons, also had claimed to be king of the caves. I delivered Bloskelt's message, but earned nothing but laughter. | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) | stage 42 | – |
| <span id="stage-61"></span>61 | Roskelt asked me to kill his brother. | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) | stage 51 | – |
| <span id="stage-62"></span>62 | Bloskelt asked me to kill his brother. | [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) | stage 52 | – |
| <span id="stage-71"></span>71 | I have killed Bloskelt.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 416](../maps/ratdom_maze_416.md).</span> | stepping on a trigger on [ratdom_maze_416](../maps/ratdom_maze_416.md) | – | – |
| <span id="stage-72"></span>72 | I have killed Roskelt.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Ratdom maze 415](../maps/ratdom_maze_415.md).</span> | stepping on a trigger on [ratdom_maze_415](../maps/ratdom_maze_415.md) | – | – |
| <span id="stage-90"></span>90 | For all my efforts, I've got a pretty poor reward. **(completes quest)** | [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md))<br>[Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) | stage 61, stage 62, stage 71, stage 72 | 1,000 XP<br>gives 18× [Gold coins](../items/gold.md)<br>gives 2× [Glass gem](../items/gem1.md)<br>sets stage 37 of [Yellow is it](../quests/ratdom_quest.md#stage-37)<br>gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 41: 1 route"

    1. Talk to [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) → choose “Aha.” — **conditions:** NOT reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62); NOT reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42) → **stage 41**. NPC: “You go and find Bloskelt! Tell him that he shall come to me to surrender! He would receive the grace of a quick,…”

???+ note "Stage 42: 1 route"

    1. Talk to [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) → choose “Aha.” — **conditions:** NOT reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61); NOT reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41) → **stage 42**. NPC: “You go and find Roskelt! Tell him that he shall come to me to surrender! He would receive the grace of a quick, almost…”

???+ note "Stage 51: 1 route"

    1. Talk to [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) → choose “Eh, yes. How did you know?” — **conditions:** NOT reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61); reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41) → **stage 51**. NPC: “HAHAHA! I will not give up and surrender to him! Never! Tell him that. HAHAHAHA!”

???+ note "Stage 52: 1 route"

    1. Talk to [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) → choose “Eh, yes. How did you know?” — **conditions:** NOT reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62); reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42) → **stage 52**. NPC: “HAHAHA! I will not give up and surrender to him! Never! Tell him that. HAHAHAHA!”

???+ note "Stage 61: 1 route"

    1. Talk to [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) → choose “I delivered your message, but Bloskelt was just laughing.” — **conditions:** reached stage 51 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-51) → **stage 61**. NPC: “Then go again. And kill him.”

???+ note "Stage 62: 1 route"

    1. Talk to [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) → choose “I delivered your message, but Roskelt was just laughing.” — **conditions:** reached stage 52 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-52) → **stage 62**. NPC: “Then go again. And kill him.”

???+ note "Stage 71: 1 route"

    1. stepping on a trigger on [ratdom_maze_416](../maps/ratdom_maze_416.md) → the conversation leads here automatically — **conditions:** killed 1× [Bloskelt](../monsters/ratdom_skeleton_boss2.md); NOT reached stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90) → **stage 71**

???+ note "Stage 72: 1 route"

    1. stepping on a trigger on [ratdom_maze_415](../maps/ratdom_maze_415.md) → the conversation leads here automatically — **conditions:** killed 1× [Roskelt](../monsters/ratdom_skeleton_boss1.md); NOT reached stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90) → **stage 72**

???+ note "Stage 90: 2 routes"

    1. Talk to [Roskelt](../monsters/ratdom_skeleton_boss1.md) ([ratdom_maze_415](../maps/ratdom_maze_415.md)) → choose “Yes. Your brother is dead.” — **conditions:** reached stage 71 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-71); reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61) → **stage 90**; also gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), sets stage 37 of [Yellow is it](../quests/ratdom_quest.md#stage-37), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md). NPC: “Good. I will shower you with gold, jewels and bones.”
    2. Talk to [Bloskelt](../monsters/ratdom_skeleton_boss2.md) ([ratdom_maze_416](../maps/ratdom_maze_416.md)) → choose “Yes. Your brother is dead.” — **conditions:** reached stage 72 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-72); reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62) → **stage 90**; also gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), sets stage 37 of [Yellow is it](../quests/ratdom_quest.md#stage-37), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md). NPC: “Good. I will shower you with gold, jewels and bones.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 9 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | stage 41 journal text changed; stage 42 journal text changed; stage 51 journal text changed; stage 52 journal text changed; stage 61 journal text changed; stage 62 journal text changed (+3 more) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_skeleton.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_skeleton.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_skeleton.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_skeleton.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_skeleton.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ratdom_skeleton` |
    | showInLog | 1 |
    | Stage IDs | 41, 42, 51, 52, 61, 62, 71, 72, 90 |
    | Dialogue nodes setting stages | 41: `ratdom_skeleton_boss_11_42`, 42: `ratdom_skeleton_boss_12_42`, 51: `ratdom_skeleton_boss_12_52`, 52: `ratdom_skeleton_boss_11_52`, 61: `ratdom_skeleton_boss_51_10`, 62: `ratdom_skeleton_boss_52_10`, 71: `ratdom_skeleton_boss2_check_10`, 72: `ratdom_skeleton_boss1_check_10`, 90: `ratdom_skeleton_boss_70_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
