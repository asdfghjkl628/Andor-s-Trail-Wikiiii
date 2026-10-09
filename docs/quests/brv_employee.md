---
description: "Work for debts is a quest in Andor's Trail, started by Stebbarik (brimhaven_employee). 9 stages, 1,000 XP in total. The dam is very important to Brimhaven. It should be repaired."
---

# Work for debts

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_employee` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 90) |
| **Started by** | [Stebbarik](../monsters/brv_employee.md) ([Brimhaven employee](../maps/brimhaven_employee.md)) |
| **NPCs involved** | [Gnossath](../monsters/brv_employer.md), [Stebbarik](../monsters/brv_employee.md) |
| **Locations** | [Brimhaven 1](../maps/brimhaven1.md), [Brimhaven employee](../maps/brimhaven_employee.md) |
| **Total XP** | 1,000 |
| **Related quests** | 1 |

</div>

## Overview

> The dam is very important to Brimhaven. It should be repaired.

## Prerequisites to start

None: talk to [Stebbarik](../monsters/brv_employee.md) ([Brimhaven employee](../maps/brimhaven_employee.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-11) | stage 11 there needs stage 1 here |
| Blocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-89) | reaching stage 90 here closes stage 89 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>1 | The dam is very important to Brimhaven. It should be repaired. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Stebbarik was ill at home in bed. He could not work and feared that… ▸</span><span class="l">▴ less</span></summary>Stebbarik was ill at home in bed. He could not work and feared that he would lose his job. Because of his high debts, he feared that Gnossath would then take his house away. I have offered to do the work for Stebbarik.</details> | [Stebbarik](../monsters/brv_employee.md) | – |
| <span id="stage-30"></span>[30](#route-30) | Gnossath has asked me to carry 25 heavy boulders from the stock to the dam. | [Gnossath](../monsters/brv_employer.md) | changes map brimhaven1 |
| <span id="stage-40"></span>[40](#route-40) | I have carried the first boulder to the dam.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-41"></span>[41](#route-41) | I have carried 5 boulders to the dam.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-42"></span>[42](#route-42) | I have moved 10 boulders.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-43"></span>[43](#route-43) | I have moved 15 boulders. This work is exhausting!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-44"></span>[44](#route-44) | Only a few to go...<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | – |
| <span id="stage-90"></span>[90](#route-90) | Finally - that was the last boulder! Gnossath was very pleased with my work. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | 1,000 XP, removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, changes map brimhaven1, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1 |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Stebbarik · 1 way"

    **Way 1:** Talk to [Stebbarik](../monsters/brv_employee.md), choose “Maybe I could help you? I could do your work.”

    - *“You would do that? Oh, thank you! Thank you!”*


<span id="route-30"></span>

??? note "Stage 30 · Gnossath · 1 way"

    **Way 1:** Talk to [Gnossath](../monsters/brv_employer.md), choose “Sounds easy. Let me try it.”

    - **Needs:** stage 10
    - **Gives:** changes map brimhaven1
    - *“OK. Try, if you want. The pile of boulders is just next to the wooden logs over there.”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** hand over 4× [Boulder](../items/brv_boulder.md)


<span id="route-41"></span>

??? note "Stage 41 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** not yet stage 41; hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 6
    - *“You have brought already more than 5 boulders.”*


<span id="route-42"></span>

??? note "Stage 42 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** not yet stage 42; hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 11
    - *“Over 10 boulders.”*


<span id="route-43"></span>

??? note "Stage 43 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** not yet stage 43; hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 16
    - *“At least 15 boulders now.”*


<span id="route-44"></span>

??? note "Stage 44 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** not yet stage 44; hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 21
    - *“Only a few boulders left.”*


<span id="route-90"></span>

??? note "Stage 90 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Uff. They somehow seem to get heavier and heavier.”

    - **Needs:** not yet stage 90; hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 25
    - **Gives:** removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, changes map brimhaven1, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1
    - <small>Also: clears stage 83 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-83), sets stage 89 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-89)</small>
    - *“Wow, you got it.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.12](../versions/0.7.12.md) | Stage 10 journal text changed<br>Stage 30 journal text changed<br>Stage 40 journal text changed<br>Stage 41 journal text changed<br>Stage 42 journal text changed<br>Stage 43 journal text changed<br>Stage 90 journal text changed |
| [v0.7.13](../versions/0.7.13.md) | Stage 90 XP 0 → 1000 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_employee` |
    | showInLog | 1 |
    | Stage IDs | 1, 10, 30, 40, 41, 42, 43, 44, 90 |
    | Dialogue nodes setting stages | 10: `brv_employee_06`, 30: `brv_employer_10_30`, 40: `brv_employer_put_boulder_10`, 41: `brv_employer_put_boulder_21`, 42: `brv_employer_put_boulder_22`, 43: `brv_employer_put_boulder_23`, 44: `brv_employer_put_boulder_24`, 90: `brv_employer_put_boulder_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
