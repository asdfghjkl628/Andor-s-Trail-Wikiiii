---
description: "Pond safety is a quest in Andor's Trail, started by Nanette (sullengard2_northwest_house). 5 stages, 2,000 XP in total. Nanette was troubled that her pond is unsafe because of the monsters that emerged in the pond."
---

# Pond safety

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `sullengard_pond_safety` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 50) |
| **Started by** | [Nanette](../monsters/sullengard_nanette.md) ([Sullengard 2 northwest house](../maps/sullengard2_northwest_house.md)) |
| **NPCs involved** | [Kealwea](../monsters/sullengard_priest.md), [Nanette](../monsters/sullengard_nanette.md) |
| **Locations** | [Sullengard 2 northwest house](../maps/sullengard2_northwest_house.md), [Sullengard church](../maps/sullengard_church.md) |
| **Total XP** | 2,000 |
| **Related quests** | 1 |

</div>

## Overview

> Nanette was troubled that her pond is unsafe because of the monsters that emerged in the pond.

## Prerequisites to start

Start with [Nanette](../monsters/sullengard_nanette.md) ([Sullengard 2 northwest house](../maps/sullengard2_northwest_house.md)). Required:

- latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Mt. Galmore exploded star (hidden flag)](mg2_exploded_star_nd.md#stage-91) | stage 91 reached, for stage 40 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Nanette was troubled that her pond is unsafe because of the monsters… ▸</span><span class="l">▴ less</span></summary>Nanette was troubled that her pond is unsafe because of the monsters that emerged in the pond.</details> | [Nanette](../monsters/sullengard_nanette.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I accepted her request to clear out the monsters in her pond area so… ▸</span><span class="l">▴ less</span></summary>I accepted her request to clear out the monsters in her pond area so that she could enjoy the pond again.</details> | [Nanette](../monsters/sullengard_nanette.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I have now cleared the pond area. Nanette told me that I should talk… ▸</span><span class="l">▴ less</span></summary>I have now cleared the pond area. Nanette told me that I should talk to Kaelwea, the priest of Sullengard, to see if he has some information about the cause of the monster's appearance in the pond area.</details> | [Nanette](../monsters/sullengard_nanette.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">The priest Kaelwea told me a story about his strange experience same… ▸</span><span class="l">▴ less</span></summary>The priest Kaelwea told me a story about his strange experience same as Nanette's experience in the pond area. I should better tell her the moral of the story.</details> | [Kealwea](../monsters/sullengard_priest.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I told Nanette the moral of the story. She had already learned from… ▸</span><span class="l">▴ less</span></summary>I told Nanette the moral of the story. She had already learned from her mistake and she promised never to do it again just to release her anger issue against the unfair taxes of Feygard.</details> **(ends quest)** | [Nanette](../monsters/sullengard_nanette.md) | 2,000 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Nanette · 1 way"

    **Way 1:** Talk to [Nanette](../monsters/sullengard_nanette.md), automatic

    - **Needs:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10
    - *“[Sigh]. Please help me. For I'm longing to enjoy my pond again.”*


<span id="route-20"></span>

??? note "Stage 20 · Nanette · 1 way"

    **Way 1:** Talk to [Nanette](../monsters/sullengard_nanette.md), choose “Fine. I'm going now.”

    - **Needs:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-10) is 10
    - *“Remember. It is just southeast from here.”*


<span id="route-30"></span>

??? note "Stage 30 · Nanette · 1 way"

    **Way 1:** Talk to [Nanette](../monsters/sullengard_nanette.md), choose “Yes, your pond is safe again. May I know the cause of it?”

    - **Needs:** latest stage of [Pond safety](../quests/sullengard_pond_safety.md#stage-20) is 20; killed 26× [Sullengard snapper](../monsters/sullengard_snapper.md)
    - *“I...I still don't know what's the cause of it. You should talk to Kealwea the priest about it.”*


<span id="route-40"></span>

??? note "Stage 40 · Kealwea · 1 way"

    **Way 1:** Talk to [Kealwea](../monsters/sullengard_priest.md), choose “I will listen to your story.”

    - **Needs:** stage 30; not yet stage 40; reached stage 91 of [Mt. Galmore exploded star (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91)
    - *“The moral of my story is to never again to throw rocks there, be it small or large. Thank you for listening. Please talk to Nanette about…”*


<span id="route-50"></span>

??? note "Stage 50 · Nanette · 1 way"

    **Way 1:** Talk to [Nanette](../monsters/sullengard_nanette.md), choose “Don't throw pebbles into the pond. You might disturb whatever lies beneath the surface.”

    - **Needs:** stage 40
    - *“Oh. I remember now. I kept throwing pebbles on the pond to relieve my anger issues caused by the unfair taxes of Feygard.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_pond_safety.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
