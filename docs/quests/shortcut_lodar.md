---
description: "The way out is through is a quest in Andor's Trail, started by Lodar (lodarhouse1). 7 stages. I talked with Lodar about a possible shortcut to the outside world. He said I should check the cave under the former cave of the Hira'zinn."
---

# The way out is through

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `shortcut_lodar` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 40) |
| **Started by** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) |
| **NPCs involved** | [Lodar](../monsters/lodar.md) |
| **Locations** | [lodarhouse1](../maps/lodarhouse1.md) |
| **Related quests** | 1 |

</div>

## Overview

> I talked with Lodar about a possible shortcut to the outside world. He said I should check the cave under the former cave of the Hira'zinn.

## Prerequisites to start

Start with [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)). Required:

- reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
- NOT reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10)
- NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Searching for madness](lodar2.md#stage-50) | stage 50 reached, for stage 22 here |
| Requires | [Searching for madness](lodar2.md#stage-60) | stage 60 reached, for stages 10, 30 here |
| Blocked by | [Searching for madness](lodar2.md#stage-50) | stage 50 must NOT be reached, for stage 20 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I talked with Lodar about a possible shortcut to the outside world. He said I should check the cave under the former cave of the Hira'zinn. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | – |
| <span id="stage-20"></span>20 | I've found the cave but the way is blocked by rocks and water. Why can't I swim? | reading a sign on [shortcut_lodar0](../maps/shortcut_lodar0.md) | stage 10 | – |
| <span id="stage-22"></span>22 | The rock formations are not the only thing that changed here. There is now a path through the water. | reading a sign on [shortcut_lodar0](../maps/shortcut_lodar0.md) | stage 20 | – |
| <span id="stage-26"></span>26 | I notice a torch burning with a strange purple hue. It's definitely a magical item. I should ask Lodar about this torch. | walking into a blocked passage on [shortcut_lodar0](../maps/shortcut_lodar0.md) | – | – |
| <span id="stage-30"></span>30 | Upon telling Lodar about the purple fire he gave me a green vial, and told me to pour it over the torch to see what happens.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar0](../maps/shortcut_lodar0.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar4](../maps/shortcut_lodar4.md).</span> | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 10, stage 26 | gives 1× [Lodar's activation vial](../items/vial_activation.md) |
| <span id="stage-40"></span>40 | I poured the vial over the purple fire and then it turned green. When approaching it I was teleported into another room of the cave with more purple torches. I was able to activate them as well. Finally, I have got my shortcut and can travel to Lodar a lot faster! **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Shortcut lodar0](../maps/shortcut_lodar0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Shortcut lodar4](../maps/shortcut_lodar4.md).</span> | stepping on a trigger on [shortcut_lodar0](../maps/shortcut_lodar0.md) | – | – |
| <span id="stage-50"></span>50 | I told Lodar about the new shortcut. He asked me to keep it a secret. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “The way to come here is a real maze and the path is tricky to find. I think I've lost my way a hundred…” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); NOT reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10); NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30) → **stage 10**. NPC: “Hmm, I remember seeing a cave under the former cave of the Hira'zinn. I don't know where it leads to but maybe you…”

???+ note "Stage 20: 1 route"

    1. reading a sign on [shortcut_lodar0](../maps/shortcut_lodar0.md) → the conversation leads here automatically — **conditions:** NOT reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50); reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10) → **stage 20**. NPC: “There is no way to go further. Maybe this has something to do with the stones?”

???+ note "Stage 22: 1 route"

    1. reading a sign on [shortcut_lodar0](../maps/shortcut_lodar0.md) → the conversation leads here automatically — **conditions:** NOT reached stage 22 of [The way out is through](../quests/shortcut_lodar.md#stage-22); reached stage 20 of [The way out is through](../quests/shortcut_lodar.md#stage-20); reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50) → **stage 22**. NPC: “Rocks have emerged here. I can walk further down this path.”

???+ note "Stage 26: 1 route"

    1. walking into a blocked passage on [shortcut_lodar0](../maps/shortcut_lodar0.md) → the conversation leads here automatically → **stage 26**. NPC: “In front of me, I see a torch burning with a purple glow. I can feel the force coming from this item. I shouldn't get…”

???+ note "Stage 30: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “I found the cave you mentioned but unfortunately the path doesn't go anywhere. I noticed a weird torch…” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 26 of [The way out is through](../quests/shortcut_lodar.md#stage-26); reached stage 10 of [The way out is through](../quests/shortcut_lodar.md#stage-10); NOT reached stage 30 of [The way out is through](../quests/shortcut_lodar.md#stage-30) → **stage 30**; also gives 1× [Lodar's activation vial](../items/vial_activation.md). NPC: “Hmm, this is interesting. I have heard of such artifacts being teleporters but have never seen one myself. Here, take…”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [shortcut_lodar0](../maps/shortcut_lodar0.md) → the conversation leads here automatically — **conditions:** NOT reached stage 40 of [The way out is through](../quests/shortcut_lodar.md#stage-40) → **stage 40**. NPC: “When pouring the vial's liquid over the torch, it suddenly burns a lot brighter and changes its color to green. I…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shortcut_lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shortcut_lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shortcut_lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shortcut_lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shortcut_lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `shortcut_lodar` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 22, 26, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `lodar_shortcut_0`, 20: `sign_lodar_shortcut_2a`, 22: `sign_lodar_shortcut_2b`, 26: `sign_lodar_shortcut_4b`, 30: `shortcut_lodar_1`, 40: `sign_lodar_shortcut_5a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
