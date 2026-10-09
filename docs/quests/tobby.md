---
description: "Sobby's Trail is a quest in Andor's Trail, started by Tobby (guynmart_wood_19). 10 stages, 1,560 XP in total. On the road to Feygard I have met a boy named Tobby. He is looking for his brother Sobby."
---

# Sobby's Trail

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `tobby` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 30, 40) |
| **Started by** | [Tobby](../monsters/tobby.md) ([Guynmart wood 19](../maps/guynmart_wood_19.md)) |
| **NPCs involved** | [Tobby](../monsters/tobby.md#v-tobby5), [Tobby](../monsters/tobby.md), [Tobby](../monsters/tobby.md#v-tobby3), [Tobby](../monsters/tobby.md#v-tobby6), [Tobby](../monsters/tobby.md#v-tobby4b), [Tobby](../monsters/tobby.md#v-tobby2) +1 |
| **Locations** | [Guynmart wood 17](../maps/guynmart_wood_17.md), [Guynmart wood 17b](../maps/guynmart_wood_17b.md), [Guynmart wood 18](../maps/guynmart_wood_18.md), [Guynmart wood 19](../maps/guynmart_wood_19.md) |
| **Total XP** | 1,560 |

</div>

## Overview

> On the road to Feygard I have met a boy named Tobby. He is looking for his brother Sobby.

## Prerequisites to start

None: talk to [Tobby](../monsters/tobby.md) ([Guynmart wood 19](../maps/guynmart_wood_19.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">On the road to Feygard I have met a boy named Tobby. He is looking… ▸</span><span class="l">▴ less</span></summary>On the road to Feygard I have met a boy named Tobby. He is looking for his brother Sobby.</details> | [Tobby](../monsters/tobby.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I have promised to help Tobby get past the kobolds to the south. | [Tobby](../monsters/tobby.md) | – |
| <span id="stage-21"></span>[21](#route-21) | I have killed the rat in Tobby's garden. | [Tobby](../monsters/tobby.md) | 30 XP |
| <span id="stage-22"></span>[22](#route-22) | I gave Tobby a loaf of bread for his father. | [Tobby](../monsters/tobby.md) | 30 XP |
| <span id="stage-23"></span>[23](#route-23) | Tobby has followed me to the beginning of the ravine with the kobolds.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span> | stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md) | removes monsters from guynmart_wood_19, spawns monsters on guynmart_wood_18 |
| <span id="stage-24"></span>[24](#route-24) | Tobby has made it through the ravine.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17b](../maps/guynmart_wood_17b.md).</span> | stepping on a trigger on [Guynmart wood 17b](../maps/guynmart_wood_17b.md) | removes monsters from guynmart_wood_18, spawns monsters on guynmart_wood_17b |
| <span id="stage-25"></span>[25](#route-25) | Tobby followed me further to the south.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span> | stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md) | removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b, spawns monsters on guynmart_wood_17 |
| <span id="stage-30"></span>[30](#route-30) | I have attacked poor Tobby, but he ran away. Now he will never find his brother. **(ends quest)** | [Tobby](../monsters/tobby.md#v-tobby2) | removes monsters from guynmart_wood_19, removes monsters from guynmart_wood_18, removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b |
| <span id="stage-40"></span>[40](#route-40) | We have parted. Tobby was sure now to find his brother. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span> | stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md), [Tobby](../monsters/tobby.md#v-tobby5) | 1,500 XP, removes monsters from guynmart_wood_17, spawns monsters on woodhouse1 |
| <span id="stage-50"></span>[50](#route-50) | I have met Tobby again, together with Sobby in the little village in the woods. | [Tobby](../monsters/tobby.md#v-tobby6) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md), choose “I am $playername. What can I do for you?”

    - *“I can't seem to find my brother, Sobby. He hasn't been back since he left last year.”*


<span id="route-20"></span>

??? note "Stage 20 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md), automatic

    - **Needs:** stage 20
    - *“I am glad you want to help me.”*


<span id="route-21"></span>

??? note "Stage 21 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md), choose “OK. And tell your father that his rat problem is solved.”

    - **Needs:** stage 20; killed 1× [Tiny rat](../monsters/tiny_rat.md#v-tobby_trainingrat)
    - *“Oh, how did you know?”*


<span id="route-22"></span>

??? note "Stage 22 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md), choose “OK. And bring your father this loaf of bread.”

    - **Needs:** stage 20; not killed 1× [Tiny rat](../monsters/tiny_rat.md#v-tobby_trainingrat); hand over 1× [Bread](../items/bread.md)
    - *“Now I'm speechless - thank you!”*


<span id="route-23"></span>

??? note "Stage 23 · stepping on a trigger on guynmart_wood_18 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 18](../maps/guynmart_wood_18.md)

    - **Needs:** stage 20; not yet stage 23, 30
    - **Gives:** removes monsters from guynmart_wood_19, spawns monsters on guynmart_wood_18


<span id="route-24"></span>

??? note "Stage 24 · stepping on a trigger on guynmart_wood_17b · 2 ways"

    **Way 1:** Stepping on a trigger on [Guynmart wood 17b](../maps/guynmart_wood_17b.md)

    - **Needs:** stage 23; not yet stage 24, 30
    - **Gives:** removes monsters from guynmart_wood_18, spawns monsters on guynmart_wood_17b

    **Way 2:** Stepping on a trigger on [Guynmart wood 17b](../maps/guynmart_wood_17b.md)

    - **Needs:** stage 23; not yet stage 24, 30
    - **Gives:** removes monsters from guynmart_wood_18, spawns monsters on guynmart_wood_17b


<span id="route-25"></span>

??? note "Stage 25 · stepping on a trigger on guynmart_wood_17 · 1 way"

    **Way 1:** Stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md)

    - **Needs:** stage 24; not yet stage 25, 30
    - **Gives:** removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b, spawns monsters on guynmart_wood_17


<span id="route-30"></span>

??? note "Stage 30 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md#v-tobby2), choose “I'll show you - attack!”

    - **Gives:** removes monsters from guynmart_wood_19, removes monsters from guynmart_wood_18, removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b
    - *“Tobby cried out aloud and ran away like the wind. You monster!”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on guynmart_wood_17, Tobby · 2 ways"

    **Way 1:** Stepping on a trigger on [Guynmart wood 17](../maps/guynmart_wood_17.md), choose “Was it? I have got used to such things by now.”

    - **Needs:** stage 25; not yet stage 40
    - **Gives:** removes monsters from guynmart_wood_17, spawns monsters on woodhouse1
    - *“I think that I'll find Sobby by myself now. Thank you - hope we'll meet again!”*

    **Way 2:** Talk to [Tobby](../monsters/tobby.md#v-tobby5), choose “Was it? I have got used to such things by now.”

    - **Gives:** removes monsters from guynmart_wood_17, spawns monsters on woodhouse1
    - *“I think that I'll find Sobby by myself now. Thank you - hope we'll meet again!”*


<span id="route-50"></span>

??? note "Stage 50 · Tobby · 1 way"

    **Way 1:** Talk to [Tobby](../monsters/tobby.md#v-tobby6), choose “Tobby? What are you doing here?”

    - *“Thanks to you I have found my brother Sobby.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `tobby` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 22, 23, 24, 25, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `tobby_3`, 20: `tobby_20`, 21: `tobby_30`, 22: `tobby_32`, 23: `tobby2_mce_1`, 24: `tobby3_mcea_1`, 24: `tobby3_mceb_1`, 25: `tobby4_mce_1`, 30: `tobby2_2`, 40: `tobby5_10`, 50: `tobby6_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
