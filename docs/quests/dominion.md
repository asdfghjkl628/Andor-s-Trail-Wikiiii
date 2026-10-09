---
description: "Dominion is a quest in Andor's Trail, started by Ysrine (undertell_1_1). 7 stages, 9,000 XP in total. Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that the Kha'zaan were destroyed, Saki wanted me to help revive his Elytharan colleagues. They had become incorporeal during the war,…"
---

# Dominion

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `dominion` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 90) |
| **Started by** | [Ysrine](../monsters/ysrine.md) ([Undertell 1 1](../maps/undertell_1_1.md)) |
| **NPCs involved** | [Saki](../monsters/saki.md), [Ysrine](../monsters/ysrine.md) |
| **Locations** | [Undertell 1 1](../maps/undertell_1_1.md), [Undertell exit](../maps/undertell_exit.md) |
| **Total XP** | 9,000 |
| **Related quests** | 3 |

</div>

## Overview

> Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that the Kha'zaan were destroyed, Saki wanted me to help revive his Elytharan colleagues. They had become incorporeal during the war, and their souls became soul pearls.

## Prerequisites to start

Start with [Ysrine](../monsters/ysrine.md) ([Undertell 1 1](../maps/undertell_1_1.md)). Required:

- reached stage 450 of [Devotion](../quests/devotion.md#stage-450)
- NOT reached stage 10 of [Dominion](../quests/dominion.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Devotion](devotion.md#stage-450) | stage 450 reached, for stages 10, 20, 30, 70 here |
| Requires | [The fifth master](fifth_master.md#stage-10) | stage 10 reached, for stage 50 here |
| Blocked by | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-7) | stage 7 must NOT be reached, for stage 50 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that… ▸</span><span class="l">▴ less</span></summary>Ysrine introduced me to Saki, ghost of an Elytharan mage. Now that the Kha'zaan were destroyed, Saki wanted me to help revive his Elytharan colleagues. They had become incorporeal during the war, and their souls became soul pearls.</details> | [Ysrine](../monsters/ysrine.md) | spawns monsters on undertell_1_1 |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Saki wanted me to defeat the liches who had picked up the soul… ▸</span><span class="l">▴ less</span></summary>Saki wanted me to defeat the liches who had picked up the soul pearls, and get back all five of them.</details> | [Saki](../monsters/saki.md), [Ysrine](../monsters/ysrine.md) | spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5 |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I returned to Saki with all five soul pearls. He took them in haste… ▸</span><span class="l">▴ less</span></summary>I returned to Saki with all five soul pearls. He took them in haste and disappeared.</details> | [Saki](../monsters/saki.md), [Ysrine](../monsters/ysrine.md) | 1,500 XP, removes monsters from undertell_1_1 |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">Ysrine told me that Saki's behavior had confirmed her suspicions… ▸</span><span class="l">▴ less</span></summary>Ysrine told me that Saki's behavior had confirmed her suspicions that Saki was a Kazaul mage and wanted to absorb the Elytharan mage souls to make himself stronger.</details> | [Ysrine](../monsters/ysrine.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">Ysrine told me that Saki was trying to flee Undertell. I was to find… ▸</span><span class="l">▴ less</span></summary>Ysrine told me that Saki was trying to flee Undertell. I was to find him, defeat him, and get the soul pearls back.</details> | [Ysrine](../monsters/ysrine.md) | spawns monsters on undertell_exit |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">Prevented from escaping Undertell by Shannal, I found Saki at the… ▸</span><span class="l">▴ less</span></summary>Prevented from escaping Undertell by Shannal, I found Saki at the passage to Undertell.</details> | [Saki](../monsters/saki.md), [Ysrine](../monsters/ysrine.md) | – |
| <span id="stage-90"></span>[90](#route-90) | Ysrine thanked me and told me to keep the soul pearls safe. **(ends quest)** | [Ysrine](../monsters/ysrine.md) | 7,500 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Ysrine · 1 way"

    **Way 1:** Talk to [Ysrine](../monsters/ysrine.md), automatic

    - **Needs:** not yet stage 10; reached stage 450 of [Devotion](../quests/devotion.md#stage-450)
    - **Gives:** spawns monsters on undertell_1_1
    - *“Here, on my left.”*


<span id="route-20"></span>

??? note "Stage 20 · Saki, Ysrine · 2 ways"

    **Way 1:** Talk to [Saki](../monsters/saki.md), choose “So I must destroy the liches and recover the pearls.”

    - **Needs:** latest stage of [Dominion](../quests/dominion.md#stage-10) is 10; reached stage 450 of [Devotion](../quests/devotion.md#stage-450)
    - **Gives:** spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5
    - *“They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.”*

    **Way 2:** Talk to [Ysrine](../monsters/ysrine.md), choose “So I must destroy the liches and recover the pearls.”

    - **Needs:** not yet stage 10; reached stage 450 of [Devotion](../quests/devotion.md#stage-450); latest stage of [Dominion](../quests/dominion.md#stage-10) is 10
    - **Gives:** spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5
    - *“They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.”*


<span id="route-30"></span>

??? note "Stage 30 · Saki, Ysrine · 2 ways"

    **Way 1:** Talk to [Saki](../monsters/saki.md), choose “Yeah, here they are.”

    - **Needs:** stage 20; not yet stage 30; hand over 5× [Soul pearl](../items/soul_pearl.md)
    - **Gives:** removes monsters from undertell_1_1
    - *“Thank you for these powerful artifacts!”*

    **Way 2:** Talk to [Ysrine](../monsters/ysrine.md), choose “Yeah, here they are.”

    - **Needs:** stage 20; not yet stage 10, 30; reached stage 450 of [Devotion](../quests/devotion.md#stage-450); hand over 5× [Soul pearl](../items/soul_pearl.md)
    - **Gives:** removes monsters from undertell_1_1
    - *“Thank you for these powerful artifacts!”*


<span id="route-50"></span>

??? note "Stage 50 · Ysrine · 1 way"

    **Way 1:** Talk to [Ysrine](../monsters/ysrine.md), choose “Wrong how?”

    - **Needs:** stage 30; not yet stage 50; reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); not reached stage 7 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-7)
    - *“Saki was no follower of Elythara. He sought to absorb the spirits of the Elytharan mages and draw power from them. I fear he serves the…”*


<span id="route-60"></span>

??? note "Stage 60 · Ysrine · 1 way"

    **Way 1:** Talk to [Ysrine](../monsters/ysrine.md), automatic

    - **Needs:** stage 50; not yet stage 60
    - **Gives:** spawns monsters on undertell_exit
    - *“Saki is trying to flee Undertell. Find him, defeat him, and recover the soul pearls and anything else he carries. Bring them back here.”*


<span id="route-70"></span>

??? note "Stage 70 · Saki, Ysrine · 2 ways"

    **Way 1:** Talk to [Saki](../monsters/saki.md), automatic

    - **Needs:** stage 60
    - *“My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername, get this guy!”*

    **Way 2:** Talk to [Ysrine](../monsters/ysrine.md), automatic

    - **Needs:** stage 60; not yet stage 10; reached stage 450 of [Devotion](../quests/devotion.md#stage-450)
    - *“My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername, get this guy!”*


<span id="route-90"></span>

??? note "Stage 90 · Ysrine · 1 way"

    **Way 1:** Talk to [Ysrine](../monsters/ysrine.md), choose “What do I do with the Soul pearls?”

    - **Needs:** not yet stage 90; killed 1× [Saki](../monsters/saki.md); carry 5× [Soul pearl](../items/soul_pearl.md)
    - *“Besides keeping them away from those Kazaul Masters? I do not know yet. Powerful they are - they could perhaps bring Elythara back, help…”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dominion.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `dominion` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 50, 60, 70, 90 |
    | Dialogue nodes setting stages | 10: `ysrine_start_devotion_15`, 20: `saki_dominion_100`, 30: `saki_pearls_20`, 50: `ysrine_dominion_saki_fleed_40`, 60: `ysrine_dominion_saki_fleed_60`, 70: `saki_trapped_20`, 90: `ysrine_saki_killed_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
