---
description: "Undertell: What was not written is a quest in Andor's Trail, started by stepping on a trigger on undertell_exit. 8 stages, 6,666 XP in total. I found the skeletal remains of an adventurer near the mining rails in Undertell. Among the remains were a history book titled \"Undertell: Its Ghosts and H…"
---

# Undertell: What was not written

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `undertell_book` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90) |
| **Started by** | stepping on a trigger on [Undertell exit](../maps/undertell_exit.md) |
| **NPCs involved** | [Arcir](../monsters/arcir.md), [Brenor](../monsters/brenor.md), [Elytharan cooker slave](../monsters/elytharan_cook_slave.md), [Ysrine](../monsters/ysrine.md) |
| **Locations** | [Undertell 1 0](../maps/undertell_1_0.md), [Undertell 1 1](../maps/undertell_1_1.md) |
| **Total XP** | 6,666 |
| **Related quests** | 2 |

</div>

## Overview

> I found the skeletal remains of an adventurer near the mining rails in Undertell. Among the remains were a history book titled "Undertell: Its Ghosts and History" and a necklace marked "Jewel of Fallhaven", which made me wonder if this man was from Fallhaven.

## Prerequisites to start

Start with stepping on a trigger on [Undertell exit](../maps/undertell_exit.md). Required:

- NOT reached stage 10 of [Undertell: What was not written](../quests/undertell_book.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The fifth master](fifth_master.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-75) | stage 75 reached, for stage 70 here |
| Blocked by | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-7) | stage 7 must NOT be reached, for stage 30 here |
| Unlocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-70) | stage 70 there needs stage 40 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I found the skeletal remains of an adventurer near the mining rails… ▸</span><span class="l">▴ less</span></summary>I found the skeletal remains of an adventurer near the mining rails in Undertell. Among the remains were a history book titled "Undertell: Its Ghosts and History" and a necklace marked "Jewel of Fallhaven", which made me wonder if this man was from Fallhaven.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell exit](../maps/undertell_exit.md).</span> | stepping on a trigger on [Undertell exit](../maps/undertell_exit.md) | 1× [Undertell: Its Ghosts and History](../items/undertell_book.md), 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md) |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Ysrine suggested that the history of Undertell records what could be… ▸</span><span class="l">▴ less</span></summary>Ysrine suggested that the history of Undertell records what could be measured, but avoids the voices of those who suffered here.</details> | [Ysrine](../monsters/ysrine.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I brought the book to Fallhaven. Arcir recognized it as a deliberate… ▸</span><span class="l">▴ less</span></summary>I brought the book to Fallhaven. Arcir recognized it as a deliberate account of Undertell's past and asked me to return and listen for what the book omits.</details> | [Arcir](../monsters/arcir.md) | spawns monsters on undertell_1_1 |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">In Undertell, I spoke with Brenor, an Elytharan ghost who still… ▸</span><span class="l">▴ less</span></summary>In Undertell, I spoke with Brenor, an Elytharan ghost who still remembers himself and the weight of the mines.</details> | [Brenor](../monsters/brenor.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I encountered an Elytharan cooker slave who spoke only of labor and… ▸</span><span class="l">▴ less</span></summary>I encountered an Elytharan cooker slave who spoke only of labor and routine, remembering work but not belief.</details> | [Elytharan cooker slave](../monsters/elytharan_cook_slave.md) | – |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I earned the trust of a shy Elytharan ghost named Cora, who would… ▸</span><span class="l">▴ less</span></summary>I earned the trust of a shy Elytharan ghost named Cora, who would only remain when I approached in silence.</details> | walking into a blocked passage on [Undertell 1 1](../maps/undertell_1_1.md) | spawns monsters on undertell_01 |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">The Elytharan ghosts each revealed a different truth: identity,… ▸</span><span class="l">▴ less</span></summary>The Elytharan ghosts each revealed a different truth: identity, labor and silence. I think Arcir would like to hear about this.</details> | [Brenor](../monsters/brenor.md), walking into a blocked passage on [Undertell 1 1](../maps/undertell_1_1.md) +1 | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">I returned to Arcir with what I learned about the Elytharan dead and… ▸</span><span class="l">▴ less</span></summary>I returned to Arcir with what I learned about the Elytharan dead and the omissions in the history of Undertell.</details> **(ends quest)** | [Arcir](../monsters/arcir.md) | 6,666 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on undertell_exit · 1 way"

    **Way 1:** Stepping on a trigger on [Undertell exit](../maps/undertell_exit.md), choose “Search the remains.”

    - **Needs:** not yet stage 10
    - **Gives:** 1× [Undertell: Its Ghosts and History](../items/undertell_book.md), 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md)
    - *“A book is lodged near the ribcage, its oilcloth wrapping stiff and darkened with blood. Despite the damage, the title remains readable:…”*


<span id="route-30"></span>

??? note "Stage 30 · Ysrine · 1 way"

    **Way 1:** Talk to [Ysrine](../monsters/ysrine.md), choose “What do you mean?”

    - **Needs:** stage 40; not yet stage 90; reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); not reached stage 7 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-7); carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md)
    - *“The dead are accustomed to being spoken for. Few think to listen instead. Undertell remembers those who do.”*


<span id="route-40"></span>

??? note "Stage 40 · Arcir · 1 way"

    **Way 1:** Talk to [Arcir](../monsters/arcir.md), choose “What is it leaving out?”

    - **Needs:** not yet stage 40; carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md)
    - **Gives:** spawns monsters on undertell_1_1
    - *“The Elytharan followers sent into those mines did not vanish. They were made unrecordable. If even one of them still remembers themselves,…”*


<span id="route-50"></span>

??? note "Stage 50 · Brenor · 1 way"

    **Way 1:** Talk to [Brenor](../monsters/brenor.md), choose “Who are you?”

    - **Needs:** stage 40; not carry 1× [Heartstone](../items/heartstone.md)
    - *“My name was Brenor. I came from the lands ruled by Feygard, back when its people still followed Elythara. I was taken during the rise of…”*


<span id="route-60"></span>

??? note "Stage 60 · Elytharan cooker slave · 1 way"

    **Way 1:** Talk to [Elytharan cooker slave](../monsters/elytharan_cook_slave.md), choose “Who do you cook for?”

    - **Needs:** stage 40; not yet stage 60
    - *“Those who work, eat. Those who eat return to work. The bell decides.”*


<span id="route-70"></span>

??? note "Stage 70 · walking into a blocked passage on undertell_1_1 · 1 way"

    **Way 1:** Walking into a blocked passage on [Undertell 1 1](../maps/undertell_1_1.md)

    - **Needs:** not yet stage 70; reached stage 75 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-75)
    - **Gives:** spawns monsters on undertell_01
    - *“You say nothing.”*


<span id="route-80"></span>

??? note "Stage 80 · Brenor, walking into a blocked passage on undertell_1_1, Ely · 3 ways"

    **Way 1:** Talk to [Brenor](../monsters/brenor.md), choose “I must continue my search.”

    - **Needs:** stage 50, 60, 70; not yet stage 80; not carry 1× [Heartstone](../items/heartstone.md)
    - *“Sure, you do that.”*

    **Way 2:** Walking into a blocked passage on [Undertell 1 1](../maps/undertell_1_1.md)

    - **Needs:** stage 50, 60, 70; not yet stage 80
    - *“The silence is so rewarding.”*

    **Way 3:** Talk to [Elytharan cooker slave](../monsters/elytharan_cook_slave.md), choose “I see, but...”

    - **Needs:** stage 50, 60, 70; not yet stage 80
    - *“When the bell rings, the bowls are filled.”*


<span id="route-90"></span>

??? note "Stage 90 · Arcir · 1 way"

    **Way 1:** Talk to [Arcir](../monsters/arcir.md), choose “The Elytharan ghosts remember different things.”

    - **Needs:** stage 80; not yet stage 90
    - *“Of course they do. History records stone and steel, but memory lives in people even after death. You have given voice to what was buried.…”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `undertell_book` |
    | showInLog | 1 |
    | Stage IDs | 10, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `undertell_book_search_20`, 30: `ysrine_undertell_quiet_road`, 40: `arcir_undertell_20`, 50: `brenor_who_20`, 60: `elytharan_cooker_loop_60`, 70: `cora_pit_return_20`, 80: `brenor_reward_qs80`, 80: `cora_reward_qs80`, 80: `elytharan_cooker_reward_qs80`, 90: `arcir_undertell_complete_npc` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
