---
description: "The last lord of Laeroth is a quest in Andor's Trail, started by stepping on a trigger on laerothbasement1. 8 stages, 1,001 XP in total. Before I leave Laeroth, perhaps I should try to find out where the last Lord went. Maybe there are clues somewhere in the manor."
---

# The last lord of Laeroth

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `last_lord` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 15, 70) |
| **Started by** | stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md), stepping on a trigger on [Laerothisland 1](../maps/laerothisland1.md) |
| **Total XP** | 1,001 |
| **Related quests** | 2 |

</div>

## Overview

> Before I leave Laeroth, perhaps I should try to find out where the last Lord went. Maybe there are clues somewhere in the manor.

## Prerequisites to start

Start with stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md). Required:

- NOT reached stage 10 of [The last lord of Laeroth](../quests/last_lord.md#stage-10)
- NOT reached stage 15 of [The last lord of Laeroth](../quests/last_lord.md#stage-15)
- reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-180) | stage 180 reached, for stages 10, 15 here |
| Unlocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-140) | stage 140 there needs stage 40 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Before I leave Laeroth, perhaps I should try to find out where the… ▸</span><span class="l">▴ less</span></summary>Before I leave Laeroth, perhaps I should try to find out where the last Lord went. Maybe there are clues somewhere in the manor.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 1](../maps/laerothbasement1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothisland 1](../maps/laerothisland1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 0](../maps/laerothmanor0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 3](../maps/laerothmanor3.md).</span> | stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">I didn't really care about where the last lord went. I left this… ▸</span><span class="l">▴ less</span></summary>I didn't really care about where the last lord went. I left this place, and whatever happened to him didn't make any difference to me.</details> **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 1](../maps/laerothbasement1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothisland 1](../maps/laerothisland1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 0](../maps/laerothmanor0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 3](../maps/laerothmanor3.md).</span> | stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md) | 1 XP |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I searched the caretakers room, and found a letter from "Adakin". It… ▸</span><span class="l">▴ less</span></summary>I searched the caretakers room, and found a letter from "Adakin". It says he is leaving to explore his future, but little more than that except that it mentions a chest that contains a diary and other things he could not take with him. I should look for this chest.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I have found a chest, with an inscription "Adakin" on the top. It is… ▸</span><span class="l">▴ less</span></summary>I have found a chest, with an inscription "Adakin" on the top. It is locked though, so I need to find the key. Hopefully he did not take it with him.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 0](../maps/laerothbasement0.md).</span> | stepping on a trigger on [Laerothbasement 0](../maps/laerothbasement0.md) | – |
| <span id="stage-40"></span>[40](#route-40) | I have found a key that looks like it should fit Adakin's chest.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 0](../maps/laerothmanor0.md).</span> | stepping on a trigger on [Laerothmanor 0](../maps/laerothmanor0.md) | 1× [Key for Adakin's chest](../items/adakin_chest_key.md) |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I have opened Adakin's chest. There are some useful items in here,… ▸</span><span class="l">▴ less</span></summary>I have opened Adakin's chest. There are some useful items in here, as well as his diary. The diary has a lock though, so it seems I must find a small key that fits this lock.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement 0](../maps/laerothbasement0.md).</span> | stepping on a trigger on [Laerothbasement 0](../maps/laerothbasement0.md) | 1× [Adakin's diary](../items/adakin_diary.md) |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I have found a jeweled key that looks like it might be for the… ▸</span><span class="l">▴ less</span></summary>I have found a jeweled key that looks like it might be for the diary. Time to try it.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md) | 1× [Key for Adakin's diary](../items/adakin_diary_key.md) |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">The key unlocked the diary. The final entry did not really give an… ▸</span><span class="l">▴ less</span></summary>The key unlocked the diary. The final entry did not really give an answer, except that he intended to go to either Nor City or Feygard, but had yet to decide which. Perhaps I will meet him some day.</details> **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor 1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md) | 1,000 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on laerothbasement1 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md), choose “Perhaps I should try to find out more.”

    - **Needs:** not yet stage 10, 15; reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180)
    - *“I will look around. The main quarters are probably a good place to start.”*


<span id="route-15"></span>

??? note "Stage 15 · stepping on a trigger on laerothbasement1 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 1](../maps/laerothbasement1.md), choose “I am just wasting time here. Time to leave.”

    - **Needs:** not yet stage 10, 15; reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180)
    - *“It doesn't matter where the last lord went.”*


<span id="route-20"></span>

??? note "Stage 20 · stepping on a trigger on laerothmanor1 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md)

    - **Needs:** stage 10; not yet stage 30
    - *“There is a chest here that contains what the caretaker left behind. Maybe there is something here about the last lord. There is a letter…”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on laerothbasement0 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 0](../maps/laerothbasement0.md)

    - **Needs:** stage 20; not yet stage 30
    - *“There is a chest here with "Adakin" written on the top. It is locked though. I need the key.”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on laerothmanor0 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothmanor 0](../maps/laerothmanor0.md)

    - **Needs:** stage 30; not yet stage 40
    - **Gives:** 1× [Key for Adakin's chest](../items/adakin_chest_key.md)
    - *“This small chest looks like it might contain something useful. Yes! A key that looks about the right size for Adakin's chest!”*


<span id="route-50"></span>

??? note "Stage 50 · stepping on a trigger on laerothbasement0 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothbasement 0](../maps/laerothbasement0.md)

    - **Needs:** stage 40; hand over 1× [Key for Adakin's chest](../items/adakin_chest_key.md)
    - **Gives:** 1× [Adakin's diary](../items/adakin_diary.md)
    - *“The key works, and the chest is open! Here is his diary. It has its own lock though, so now I need a key for this! There's some other nice…”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on laerothmanor1 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md)

    - **Needs:** stage 50; not yet stage 60
    - **Gives:** 1× [Key for Adakin's diary](../items/adakin_diary_key.md)
    - *“I have found a smalled jeweled key that looks like it will fit Adakin's diary.”*


<span id="route-70"></span>

??? note "Stage 70 · stepping on a trigger on laerothmanor1 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothmanor 1](../maps/laerothmanor1.md)

    - **Needs:** stage 60; not yet stage 70; hand over 1× [Key for Adakin's diary](../items/adakin_diary_key.md); hand over 1× [Adakin's diary](../items/adakin_diary.md)
    - *“It reads: "I need to go and find my destiny. It is not here at the manor, so I must strike out and find what lies ahead for me. I will go…”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `last_lord` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 10: `laeroth_exit_1c`, 15: `laeroth_exit_1b`, 20: `caretaker_chest_1`, 30: `adakin_chest_1`, 40: `adakin_key_search_1`, 50: `adakin_chest_2`, 60: `nightstand_search_2`, 70: `last_lord_final_0b` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
