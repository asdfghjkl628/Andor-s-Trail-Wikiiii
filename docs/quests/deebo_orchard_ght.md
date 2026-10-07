---
description: "Getting home on time is a quest in Andor's Trail, started by Hadena (sullengard_ravine_cabin). 7 stages, 5,000 XP in total. Hadena needed my help to get her husband Ainsley home on time."
---

# Getting home on time

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `deebo_orchard_ght` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 60) |
| **Started by** | [Hadena](../monsters/sullengard_cabin_wife.md) ([Sullengard ravine cabin](../maps/sullengard_ravine_cabin.md)) |
| **NPCs involved** | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md), [Hadena](../monsters/sullengard_cabin_wife.md), [Throthaus](../monsters/throthaus.md) |
| **Locations** | [Loneford 15](../maps/loneford15.md), [Sullengard apple farm west](../maps/sullengard_apple_farm_west.md), [Sullengard ravine cabin](../maps/sullengard_ravine_cabin.md) |
| **Total XP** | 5,000 |
| **Related quests** | 1 |

</div>

## Overview

> Hadena needed my help to get her husband Ainsley home on time.

## Prerequisites to start

Start with [Hadena](../monsters/sullengard_cabin_wife.md) ([Sullengard ravine cabin](../maps/sullengard_ravine_cabin.md)). Required:

- NOT reached stage 10 of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-100) | stage 100 there needs stage 30 here |
| Blocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-16) | reaching stage 10 here closes stage 16 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | Hadena needed my help to get her husband Ainsley home on time. | [Hadena](../monsters/sullengard_cabin_wife.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I agreed to help Hadena with getting her husband Ainsley home on… ▸</span><span class="l">▴ less</span></summary>I agreed to help Hadena with getting her husband Ainsley home on time. He was working at Deebo's Orchard located southwest of their cabin.</details> | [Hadena](../monsters/sullengard_cabin_wife.md) | – |
| <span id="stage-25"></span>[25](#route-25) | <details class="jt"><summary><span class="s">Due to the vast distance to Loneford and the monsters that he would… ▸</span><span class="l">▴ less</span></summary>Due to the vast distance to Loneford and the monsters that he would encounter along the way, Ainsley has asked me to go to Loneford and get him a new pitchfork.</details> | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Throthaus wanted me to pull out his pitchfork from the haystack to… ▸</span><span class="l">▴ less</span></summary>Throthaus wanted me to pull out his pitchfork from the haystack to prove that I'm a son of a farmer.</details> | [Throthaus](../monsters/throthaus.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I successfully pulled out the pitchfork. It's time to visit Ainsley… ▸</span><span class="l">▴ less</span></summary>I successfully pulled out the pitchfork. It's time to visit Ainsley again who's working on Deebo's Orchard.</details> | walking into a blocked passage on [Loneford 13](../maps/loneford13.md) | 1× [Farmer's pitchfork](../items/farmer_pitchfork.md), applies condition fatigue4 |
| <span id="stage-50"></span>[50](#route-50) | I gave Ainsley the new pitchfork. I should tell Hadena about this. | [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md) | – |
| <span id="stage-60"></span>[60](#route-60) | Hadena was so grateful to me for helping them. **(ends quest)** | [Hadena](../monsters/sullengard_cabin_wife.md) | 5,000 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Hadena · 1 way"

    **Way 1:** Talk to [Hadena](../monsters/sullengard_cabin_wife.md), choose “So, my brother Andor was here as well? I'm $playername and you are?”

    - **Needs:** not yet stage 10
    - *“Oh, I'm sorry. My name is Hadena. Andor used to visit here but I don't know why he doesn't anymore. Anyways, I really need your…”*


<span id="route-20"></span>

??? note "Stage 20 · Hadena · 1 way"

    **Way 1:** Talk to [Hadena](../monsters/sullengard_cabin_wife.md), choose “I'm sorry because I was only half listening to you earlier, so I am a little fuzzy on the details. But can…”

    - **Needs:** not yet stage 10; latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-10) is 10
    - *“He is working at Deebo's Orchard located southwest of here. Please go there and help him.”*


<span id="route-25"></span>

??? note "Stage 25 · Ainsley · 1 way"

    **Way 1:** Talk to [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md), choose “Especially for a farmer. Trust me, I know.”

    - **Needs:** not yet stage 50; latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-20) is 20
    - *“Anyways, I would really appreciate it if you would go to Loneford and get the pitchfork.”*


<span id="route-30"></span>

??? note "Stage 30 · Throthaus · 1 way"

    **Way 1:** Talk to [Throthaus](../monsters/throthaus.md), choose “No. But I'm a child of an ordinary farmer in a small settlement called Crossglen.”

    - **Needs:** latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-25) is 25
    - *“If you are able to pull it out from the haystack, then it will be yours.”*


<span id="route-40"></span>

??? note "Stage 40 · walking into a blocked passage on loneford13 · 1 way"

    **Way 1:** Walking into a blocked passage on [Loneford 13](../maps/loneford13.md), choose “Time to prove that I'm the child of farmer!”

    - **Needs:** stage 30
    - **Gives:** 1× [Farmer's pitchfork](../items/farmer_pitchfork.md), applies condition fatigue4
    - <small>Also: sets stage 100 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-100)</small>
    - *“After several minutes of intense pulling you finally pull out the new pitchfork from the haystack.”*


<span id="route-50"></span>

??? note "Stage 50 · Ainsley · 1 way"

    **Way 1:** Talk to [Ainsley](../monsters/deebo_orchard_farmer_ainsley.md), automatic

    - *“Thank you so much, kid. Tell my wife Hadena I can come home on time today.”*


<span id="route-60"></span>

??? note "Stage 60 · Hadena · 1 way"

    **Way 1:** Talk to [Hadena](../monsters/sullengard_cabin_wife.md), choose “It is done. Ainsley will be home on time today.”

    - **Needs:** not yet stage 60; latest stage of [Getting home on time](../quests/deebo_orchard_ght.md#stage-50) is 50
    - *“Thank you so much for helping us. You are just like your brother.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.4](../versions/0.8.4.md) | Stage 40 journal text changed |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_ght.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
