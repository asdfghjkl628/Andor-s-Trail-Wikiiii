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
| **Started by** | [Lodar](../monsters/lodar.md) ([Lodarhouse 1](../maps/lodarhouse1.md)) |
| **NPCs involved** | [Lodar](../monsters/lodar.md) |
| **Locations** | [Lodarhouse 1](../maps/lodarhouse1.md) |
| **Related quests** | 1 |

</div>

## Overview

> I talked with Lodar about a possible shortcut to the outside world. He said I should check the cave under the former cave of the Hira'zinn.

## Prerequisites to start

Start with [Lodar](../monsters/lodar.md) ([Lodarhouse 1](../maps/lodarhouse1.md)). Required:

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

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I talked with Lodar about a possible shortcut to the outside world.… ▸</span><span class="l">▴ less</span></summary>I talked with Lodar about a possible shortcut to the outside world. He said I should check the cave under the former cave of the Hira'zinn.</details> | [Lodar](../monsters/lodar.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I've found the cave but the way is blocked by rocks and water. Why can't I swim? | reading a sign on [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – |
| <span id="stage-22"></span>[22](#route-22) | <details class="jt"><summary><span class="s">The rock formations are not the only thing that changed here. There… ▸</span><span class="l">▴ less</span></summary>The rock formations are not the only thing that changed here. There is now a path through the water.</details> | reading a sign on [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – |
| <span id="stage-26"></span>[26](#route-26) | <details class="jt"><summary><span class="s">I notice a torch burning with a strange purple hue. It's definitely… ▸</span><span class="l">▴ less</span></summary>I notice a torch burning with a strange purple hue. It's definitely a magical item. I should ask Lodar about this torch.</details> | walking into a blocked passage on [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Upon telling Lodar about the purple fire he gave me a green vial,… ▸</span><span class="l">▴ less</span></summary>Upon telling Lodar about the purple fire he gave me a green vial, and told me to pour it over the torch to see what happens.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar 0](../maps/shortcut_lodar0.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar 4](../maps/shortcut_lodar4.md).</span> | [Lodar](../monsters/lodar.md) | 1× [Lodar's activation vial](../items/vial_activation.md) |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I poured the vial over the purple fire and then it turned green.… ▸</span><span class="l">▴ less</span></summary>I poured the vial over the purple fire and then it turned green. When approaching it I was teleported into another room of the cave with more purple torches. I was able to activate them as well. Finally, I have got my shortcut and can travel to Lodar a lot faster!</details> **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Shortcut lodar 0](../maps/shortcut_lodar0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Shortcut lodar 4](../maps/shortcut_lodar4.md).</span> | stepping on a trigger on [Shortcut lodar 0](../maps/shortcut_lodar0.md) | – |
| <span id="stage-50"></span>50 | I told Lodar about the new shortcut. He asked me to keep it a secret. | *no trigger found* <sup>[?](#untraced)</sup> | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Lodar · 1 way"

    **Way 1:** Talk to [Lodar](../monsters/lodar.md), choose “The way to come here is a real maze and the path is tricky to find. I think I've lost my way a hundred…”

    - **Needs:** not yet stage 10, 30; reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
    - *“Hmm, I remember seeing a cave under the former cave of the Hira'zinn. I don't know where it leads to but maybe you could give it a try and…”*


<span id="route-20"></span>

??? note "Stage 20 · reading a sign on shortcut_lodar0 · 1 way"

    **Way 1:** Reading a sign on [Shortcut lodar 0](../maps/shortcut_lodar0.md)

    - **Needs:** stage 10; not reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50)
    - *“There is no way to go further. Maybe this has something to do with the stones?”*


<span id="route-22"></span>

??? note "Stage 22 · reading a sign on shortcut_lodar0 · 1 way"

    **Way 1:** Reading a sign on [Shortcut lodar 0](../maps/shortcut_lodar0.md)

    - **Needs:** stage 20; not yet stage 22; reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50)
    - *“Rocks have emerged here. I can walk further down this path.”*


<span id="route-26"></span>

??? note "Stage 26 · walking into a blocked passage on shortcut_lodar0 · 1 way"

    **Way 1:** Walking into a blocked passage on [Shortcut lodar 0](../maps/shortcut_lodar0.md)

    - *“In front of me, I see a torch burning with a purple glow. I can feel the force coming from this item. I shouldn't get closer until I tell…”*


<span id="route-30"></span>

??? note "Stage 30 · Lodar · 1 way"

    **Way 1:** Talk to [Lodar](../monsters/lodar.md), choose “I found the cave you mentioned but unfortunately the path doesn't go anywhere. I noticed a weird torch…”

    - **Needs:** stage 10, 26; not yet stage 30; reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
    - **Gives:** 1× [Lodar's activation vial](../items/vial_activation.md)
    - *“Hmm, this is interesting. I have heard of such artifacts being teleporters but have never seen one myself. Here, take this vial and pour…”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on shortcut_lodar0 · 1 way"

    **Way 1:** Stepping on a trigger on [Shortcut lodar 0](../maps/shortcut_lodar0.md)

    - **Needs:** not yet stage 40
    - *“When pouring the vial's liquid over the torch, it suddenly burns a lot brighter and changes its color to green. I should approach this…”*



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
