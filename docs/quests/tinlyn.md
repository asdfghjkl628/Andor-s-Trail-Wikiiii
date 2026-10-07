---
description: "Lost sheep is a quest in Andor's Trail, started by Tinlyn (fields6). 10 stages, 800 XP in total. On the road to Feygard, near the Feygard bridge, I met a shepherd named Tinlyn. Tinlyn told me that four of his sheep have wandered away and that he won't dare leave the remaining sheep to go look for…"
---

# Lost sheep

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `tinlyn` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 30, 31, 60) |
| **Started by** | [Tinlyn](../monsters/tinlyn.md) ([Fields 6](../maps/fields6.md)) |
| **NPCs involved** | [Sheep](../monsters/sheep1.md#v-lostsheep2), [Sheep](../monsters/sheep1.md#v-lostsheep1), [Sheep](../monsters/sheep1.md#v-lostsheep4), [Sheep](../monsters/sheep1.md), [Sheep](../monsters/sheep1.md#v-lostsheep3), [Tinlyn](../monsters/tinlyn.md) |
| **Locations** | [Fields 1](../maps/fields1.md), [Fields 2](../maps/fields2.md), [Fields 3](../maps/fields3.md), [Fields 6](../maps/fields6.md) |
| **Total XP** | 800 |
| **Related quests** | 2 |

</div>

## Overview

> On the road to Feygard, near the Feygard bridge, I met a shepherd named Tinlyn. Tinlyn told me that four of his sheep have wandered away and that he won't dare leave the remaining sheep to go look for them.

## Prerequisites to start

Start with [Tinlyn](../monsters/tinlyn.md) ([Fields 6](../maps/fields6.md)). Required:

- reached stage 15 of [Lost sheep](../quests/tinlyn.md#stage-15)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Cheap cuts](benbyr.md#stage-20) | stage 20 reached, for stage 60 here |
| Requires | [Cheap cuts](benbyr.md#stage-21) | stage 21 reached, for stage 60 here |
| Unlocks | [Cheap cuts](benbyr.md#stage-21) | stage 21 there needs stages 20, 21, 22, 23 here |
| Unlocks | [It makes no fence](tunlon_fence.md#stage-100) | stage 100 there needs stage 31 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">On the road to Feygard, near the Feygard bridge, I met a shepherd… ▸</span><span class="l">▴ less</span></summary>On the road to Feygard, near the Feygard bridge, I met a shepherd named Tinlyn. Tinlyn told me that four of his sheep have wandered away and that he won't dare leave the remaining sheep to go look for them.</details> | [Tinlyn](../monsters/tinlyn.md) | – |
| <span id="stage-15"></span>[15](#route-15) | I have agreed to help Tinlyn find his four lost sheep. | [Tinlyn](../monsters/tinlyn.md) | [Tinlyn's sheep bell](../items/tinlyn_bells.md) |
| <span id="stage-20"></span>[20](#route-20) | I have found one of Tinlyn's lost sheep. | [Sheep](../monsters/sheep1.md#v-lostsheep1) | – |
| <span id="stage-21"></span>[21](#route-21) | I have found one of Tinlyn's lost sheep. | [Sheep](../monsters/sheep1.md#v-lostsheep2) | – |
| <span id="stage-22"></span>[22](#route-22) | I have found one of Tinlyn's lost sheep. | [Sheep](../monsters/sheep1.md#v-lostsheep3) | – |
| <span id="stage-23"></span>[23](#route-23) | I have found one of Tinlyn's lost sheep. | [Sheep](../monsters/sheep1.md#v-lostsheep4) | – |
| <span id="stage-25"></span>[25](#route-25) | I have found all four of Tinlyn's lost sheep. | [Sheep](../monsters/sheep1.md#v-lostsheep1), [Sheep](../monsters/sheep1.md#v-lostsheep2) +2 | – |
| <span id="stage-30"></span>[30](#route-30) | Tinlyn thanked me for finding his lost sheep. **(ends quest)** | [Tinlyn](../monsters/tinlyn.md) | 300 XP |
| <span id="stage-31"></span>[31](#route-31) | Tinlyn thanked me for finding his lost sheep, but he had no reward to give me. **(ends quest)** | [Tinlyn](../monsters/tinlyn.md) | 500 XP |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I have attacked at least one of Tinlyn's lost sheep and I am… ▸</span><span class="l">▴ less</span></summary>I have attacked at least one of Tinlyn's lost sheep and I am therefore unable to return them all to Tinlyn.</details> **(ends quest)** | [Tinlyn](../monsters/tinlyn.md), [Sheep](../monsters/sheep1.md#v-lostsheep1) +4 | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Tinlyn · 1 way"

    **Way 1:** Talk to [Tinlyn](../monsters/tinlyn.md), choose “What was I supposed to do?”

    - **Needs:** stage 15
    - *“The thing is, I have lost four of them. Now I won't dare leave the ones I still have in my sight to go look for the lost ones.”*


<span id="route-15"></span>

??? note "Stage 15 · Tinlyn · 1 way"

    **Way 1:** Talk to [Tinlyn](../monsters/tinlyn.md), choose “Absolutely, it would be my honor to assist you in locating your missing sheep.”

    - **Needs:** stage 15
    - **Gives:** [Tinlyn's sheep bell](../items/tinlyn_bells.md)
    - *“Good, thank you. Please put these bells around their necks so I can hear them.”*


<span id="route-20"></span>

??? note "Stage 20 · Sheep · 1 way"

    **Way 1:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep1), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)


<span id="route-21"></span>

??? note "Stage 21 · Sheep · 1 way"

    **Way 1:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep2), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)


<span id="route-22"></span>

??? note "Stage 22 · Sheep · 1 way"

    **Way 1:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep3), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)


<span id="route-23"></span>

??? note "Stage 23 · Sheep · 1 way"

    **Way 1:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep4), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)


<span id="route-25"></span>

??? note "Stage 25 · Sheep · 4 ways"

    **Way 1:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep1), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** stage 20, 21, 22, 23; hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)

    **Way 2:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep2), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** stage 20, 21, 22, 23; hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)

    **Way 3:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep3), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** stage 20, 21, 22, 23; hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)

    **Way 4:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep4), choose “[Place Tinlyn's bell around the neck of the sheep]”

    - **Needs:** stage 20, 21, 22, 23; hand over 1× [Tinlyn's sheep bell](../items/tinlyn_bells.md)


<span id="route-30"></span>

??? note "Stage 30 · Tinlyn · 1 way"

    **Way 1:** Talk to [Tinlyn](../monsters/tinlyn.md), choose “I am happy to help.”

    - **Needs:** stage 15, 25
    - *“Thank you for helping me.”*


<span id="route-31"></span>

??? note "Stage 31 · Tinlyn · 1 way"

    **Way 1:** Talk to [Tinlyn](../monsters/tinlyn.md), choose “That was some hard work. What about a reward?”

    - **Needs:** stage 15, 25
    - *“I am sorry, but I am a simple shepherd. I have no wealth or magical trinkets to give you.”*


<span id="route-60"></span>

??? note "Stage 60 · Tinlyn, Sheep · 6 ways"

    **Way 1:** Talk to [Tinlyn](../monsters/tinlyn.md), automatic

    - **Needs:** stage 10; reached stage 21 of [Cheap cuts](../quests/benbyr.md#stage-21)

    **Way 2:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep1), choose “[Attack]”

    - **Needs:** stage 10, 20; reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)

    **Way 3:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep2), choose “[Attack]”

    - **Needs:** stage 10, 21; reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)

    **Way 4:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep3), choose “[Attack]”

    - **Needs:** stage 10, 22; reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)

    **Way 5:** Talk to [Sheep](../monsters/sheep1.md#v-lostsheep4), choose “[Attack]”

    - **Needs:** stage 10, 23; reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)

    **Way 6:** Talk to [Sheep](../monsters/sheep1.md), choose “[Attack]”

    - **Needs:** stage 10; reached stage 20 of [Cheap cuts](../quests/benbyr.md#stage-20)



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Good, thank you. Please put these bells around their necks so I can h…” → “Good, thank you. Please put these bells around their necks so I can h…” |
| [v0.8.7](../versions/0.8.7.md) | Stage 60 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tinlyn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tinlyn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tinlyn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tinlyn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tinlyn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `tinlyn` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 21, 22, 23, 25, 30, 31, 60 |
    | Dialogue nodes setting stages | 10: `tinlyn_story_3`, 15: `tinlyn_story_5`, 20: `tinlyn_lostsheep1_place`, 21: `tinlyn_lostsheep2_place`, 22: `tinlyn_lostsheep3_place`, 23: `tinlyn_lostsheep4_place`, 25: `tinlyn_lostsheep_placed_1`, 30: `tinlyn_found_3`, 31: `tinlyn_found_2`, 60: `tinlyn_killedsheep_0_1`, 60: `tinlyn_lostsheep_atk1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
