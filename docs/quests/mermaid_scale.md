---
description: "The silver scale is a quest in Andor's Trail, started by Tjure (blackwater_mountain54). 8 stages, 4,000 XP in total. In a clearing, you met Tjure, who desperately asked for your help. He had once found a mermaid asleep on the beach at the river. The colorful tail attracted him so much that he pul…"
---

# The silver scale

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `mermaid_scale` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90, 210) |
| **Started by** | [Tjure](../monsters/tjure.md) ([Blackwater mountain 54](../maps/blackwater_mountain54.md)) |
| **NPCs involved** | [Tjure](../monsters/tjure.md) |
| **Locations** | [Blackwater mountain 54](../maps/blackwater_mountain54.md) |
| **Total XP** | 4,000 |
| **Related quests** | 2 |

</div>

## Overview

> In a clearing, you met Tjure, who desperately asked for your help. He had once found a mermaid asleep on the beach at the river. The colorful tail attracted him so much that he pulled out a dazzling scale and ran away.

## Prerequisites to start

Start with [Tjure](../monsters/tjure.md) ([Blackwater mountain 54](../maps/blackwater_mountain54.md)). Required:

- reached stage 10 of [The silver scale](../quests/mermaid_scale.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Brimhaven warehouse delivery (hidden flag)](brv_wh_delivery_nondisplay.md#stage-50) | stage 50 there needs stage 200 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-10) | stage 10 there needs stage 220 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-11) | stage 11 there needs stage 220 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">In a clearing, you met Tjure, who desperately asked for your help.… ▸</span><span class="l">▴ less</span></summary>In a clearing, you met Tjure, who desperately asked for your help. He had once found a mermaid asleep on the beach at the river. The colorful tail attracted him so much that he pulled out a dazzling scale and ran away.</details> | [Tjure](../monsters/tjure.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Crying and mourning, the mermaid called after him. Finally she… ▸</span><span class="l">▴ less</span></summary>Crying and mourning, the mermaid called after him. Finally she cursed him. Since then, Tjure has never been happy. He just wanted to get rid of the scale. Nevertheless, he never ventured back to the vicinity of the river.</details> | [Tjure](../monsters/tjure.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">A wise woman told Tjure that he could neither throw away nor destroy… ▸</span><span class="l">▴ less</span></summary>A wise woman told Tjure that he could neither throw away nor destroy the scale. His only salvation would be to give it back or to have someone buy it from him. But who would ever want to incur the wrath of a mermaid?</details> | [Tjure](../monsters/tjure.md) | – |
| <span id="stage-90"></span>[90](#route-90) | You decided not to help Tjure. **(ends quest)** | [Tjure](../monsters/tjure.md) | 500 XP |
| <span id="stage-100"></span>[100](#route-100) | <details class="jt"><summary><span class="s">As soon as you held the scale in your hands, a great sluggishness… ▸</span><span class="l">▴ less</span></summary>As soon as you held the scale in your hands, a great sluggishness and dispair came over you.</details> | [Tjure](../monsters/tjure.md) | applies condition mermaid_scale |
| <span id="stage-200"></span>[200](#route-200) | You put the scale on the mark on the ground.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower 2](../maps/roadtocarntower2.md).</span> | stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md) | applies condition mermaid_scale |
| <span id="stage-210"></span>[210](#route-210) | There rang out a beautiful song of gratitude. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower 2](../maps/roadtocarntower2.md).</span><br><span class="qnote">🗺️ Part of [Roadtocarntower 2](../maps/roadtocarntower2.md) visibly changes.</span> | stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md) | 3,500 XP |
| <span id="stage-220"></span>[220](#route-220) | You found a heavy bag of gold.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower 2](../maps/roadtocarntower2.md).</span> | stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md) | 1000× [Gold coins](../items/gold.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Tjure · 1 way"

    **Way 1:** Talk to [Tjure](../monsters/tjure.md), automatic

    - **Needs:** stage 10
    - *“I pulled out one of her shimmering, dazzling scales, and ran away.”*


<span id="route-20"></span>

??? note "Stage 20 · Tjure · 1 way"

    **Way 1:** Talk to [Tjure](../monsters/tjure.md), automatic

    - **Needs:** stage 20
    - *“Crying and sobbing, the mermaid called after me. Finally, she screamed at me that I would never find peace, and that I would never want to…”*


<span id="route-30"></span>

??? note "Stage 30 · Tjure · 1 way"

    **Way 1:** Talk to [Tjure](../monsters/tjure.md), automatic

    - **Needs:** stage 30
    - *“She told me that my only other option was to find some kind-hearted person to buy it from me, but then they take on the curse.”*


<span id="route-90"></span>

??? note "Stage 90 · Tjure · 1 way"

    **Way 1:** Talk to [Tjure](../monsters/tjure.md), automatic

    - **Needs:** stage 90
    - *“*Sigh* You were my last hope. Leave me now.”*


<span id="route-100"></span>

??? note "Stage 100 · Tjure · 1 way"

    **Way 1:** Talk to [Tjure](../monsters/tjure.md), choose “No problem, here, take the gold.”

    - **Needs:** stage 30; pay 1 gold
    - **Gives:** applies condition mermaid_scale
    - *“(As soon as you take the scale in your hands, a great sluggishness and a feeling of despair come over you.)”*


<span id="route-200"></span>

??? note "Stage 200 · stepping on a trigger on roadtocarntower2 · 1 way"

    **Way 1:** Stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md), choose “* Put the scale on the ground *”

    - **Needs:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-100) is 100
    - **Gives:** applies condition mermaid_scale
    - *“What a relief! You suddenly feel lighthearted again.”*


<span id="route-210"></span>

??? note "Stage 210 · stepping on a trigger on roadtocarntower2 · 1 way"

    **Way 1:** Stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md)

    - **Needs:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-200) is 200
    - *“You never heard such a beautiful sound before.”*


<span id="route-220"></span>

??? note "Stage 220 · stepping on a trigger on roadtocarntower2 · 1 way"

    **Way 1:** Stepping on a trigger on [Roadtocarntower 2](../maps/roadtocarntower2.md)

    - **Needs:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-210) is 210
    - **Gives:** 1000× [Gold coins](../items/gold.md)
    - *“You found a heavy bag of gold. 1,000 shining pieces of gold!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “You found a heavy bag of gold. 1000 shining pieces of gold!” → “You found a heavy bag of gold. {1000} shining pieces of gold!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `mermaid_scale` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 90, 100, 200, 210, 220 |
    | Dialogue nodes setting stages | 10: `tjure_10`, 20: `tjure_20`, 30: `tjure_30_34`, 90: `tjure_90`, 100: `tjure_30_92`, 200: `watermark_script_100_10`, 210: `watermark_script_200_10`, 220: `watermark_script_210` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
