---
description: "More rats! is a quest in Andor's Trail, started by Mikhail (home). 10 stages, 1,200 XP in total. A huge rat called Gruiik told me that they drove all the people out of this village."
---

# More rats!

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ratdom_mikhail` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 90) |
| **Started by** | [Mikhail](../monsters/mikhail.md) ([Home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([Home](../maps/home.md)) |
| **NPCs involved** | [Gruiik](../monsters/ratdom_mikhail.md), [Mikhail](../monsters/mikhail.md) |
| **Locations** | [Home](../maps/home.md), [Waytogalmore 0](../maps/waytogalmore0.md) |
| **Total XP** | 1,200 |
| **Related quests** | 2 |

</div>

## Overview

> A huge rat called Gruiik told me that they drove all the people out of this village.

## Prerequisites to start

**Route 1** ([Mikhail](../monsters/mikhail.md) ([Home](../maps/home.md))):

- reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)

**Route 2** ([Gruiik](../monsters/ratdom_mikhail.md) ([Home](../maps/home.md))):

- nothing

**Route 3** (stepping on a trigger on [Home](../maps/home.md)):

- reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
- reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950)
- NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Ratdom story flags (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Requires | [Yellow is it](ratdom_quest.md#stage-950) | stage 950 reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Blocked by | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 must NOT be reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Unlocks | [Ratdom story flags (hidden flag)](ratdom_nondisplay.md#stage-13) | stage 13 there needs stage 90 here |
| Unlocks | [Ratdom story flags (hidden flag)](ratdom_nondisplay.md#stage-21) | stage 21 there needs stage 90 here |
| Unlocks | [Ratdom story flags (hidden flag)](ratdom_nondisplay.md#stage-22) | stage 22 there needs stage 90 here |
| Unlocks | [Ratdom story flags (hidden flag)](ratdom_nondisplay.md#stage-23) | stage 23 there needs stage 90 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-50) | stage 50 there needs stage 10 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-940) | stage 940 there needs stage 90 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 there needs stage 90 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">A huge rat called Gruiik told me that they drove all the people out… ▸</span><span class="l">▴ less</span></summary>A huge rat called Gruiik told me that they drove all the people out of this village.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | – |
| <span id="stage-20"></span>[20](#route-20) | Some two-legs were running around in the garden again. I should kill them.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | – |
| <span id="stage-30"></span>[30](#route-30) | I have killed Mara.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [Crossglen](../maps/crossglen.md) | removes monsters from crossglen_hall |
| <span id="stage-32"></span>[32](#route-32) | I have killed Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [Crossglen](../maps/crossglen.md) | removes monsters from crossglen_hall |
| <span id="stage-52"></span>[52](#route-52) | I told Gruiik that I have killed Mara and Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | 500 XP |
| <span id="stage-54"></span>[54](#route-54) | I lied to Gruiik that I have killed Mara and Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | 500 XP |
| <span id="stage-70"></span>[70](#route-70) | Gruiik was hungry and asked to bring him bread.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | – |
| <span id="stage-72"></span>[72](#route-72) | I found a bread in a bag hanging at the door of the Crossglen town hall. | walking into a blocked passage on [Crossglen](../maps/crossglen.md) | 1× [Bread](../items/bread.md) |
| <span id="stage-74"></span>[74](#route-74) | I gave a bread to Gruiik.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | 200 XP |
| <span id="stage-90"></span>[90](#route-90) | The huge rat ignored me after he had got the bread. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md), [Gruiik](../monsters/ratdom_mikhail.md) +1 | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “What are you doing in my house? Where is Mikhail?”

    - **Needs:** reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
    - *“We rats took over this village. I am Gruiik, their leader.”*

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “What are you doing in my house? Where is Mikhail?”

    - *“We rats took over this village. I am Gruiik, their leader.”*

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “What are you doing in my house? Where is Mikhail?”

    - **Needs:** reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
    - *“We rats took over this village. I am Gruiik, their leader.”*


<span id="route-20"></span>

??? note "Stage 20 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “What are you doing in my house? Where is Mikhail?”

    - **Needs:** reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
    - *“However, there are two-legs running around in my garden again. Go and kill them.”*

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “What are you doing in my house? Where is Mikhail?”

    - *“However, there are two-legs running around in my garden again. Go and kill them.”*

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “What are you doing in my house? Where is Mikhail?”

    - **Needs:** reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
    - *“However, there are two-legs running around in my garden again. Go and kill them.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on crossglen · 1 way"

    **Way 1:** Stepping on a trigger on [Crossglen](../maps/crossglen.md)

    - **Needs:** not yet stage 30; killed 1× [Mara](../monsters/mara.md#v-ratdom_mara)
    - **Gives:** removes monsters from crossglen_hall


<span id="route-32"></span>

??? note "Stage 32 · stepping on a trigger on crossglen · 1 way"

    **Way 1:** Stepping on a trigger on [Crossglen](../maps/crossglen.md)

    - **Needs:** not yet stage 32; killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)
    - **Gives:** removes monsters from crossglen_hall


<span id="route-52"></span>

??? note "Stage 52 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “Yes, I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “Yes, I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “Yes, I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)


<span id="route-54"></span>

??? note "Stage 54 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “(lie) I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); not killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “(lie) I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; not killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “(lie) I killed Mara and Tharal in the garden for you.”

    - **Needs:** stage 20; not yet stage 52, 54; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); not killed 1× [Mara](../monsters/mara.md#v-ratdom_mara); killed 1× [Tharal](../monsters/tharal.md#v-ratdom_tharal)


<span id="route-70"></span>

??? note "Stage 70 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), automatic

    - **Needs:** stage 20; not yet stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
    - *“And I am hungry. Go to the town hall and bring me some bread.”*

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), automatic

    - **Needs:** stage 20; not yet stage 70
    - *“And I am hungry. Go to the town hall and bring me some bread.”*

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “Oh. Hello Gruiik.”

    - **Needs:** stage 20; not yet stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
    - *“And I am hungry. Go to the town hall and bring me some bread.”*


<span id="route-72"></span>

??? note "Stage 72 · walking into a blocked passage on crossglen · 1 way"

    **Way 1:** Walking into a blocked passage on [Crossglen](../maps/crossglen.md), choose “Oh, what's this?”

    - **Needs:** not yet stage 72
    - **Gives:** 1× [Bread](../items/bread.md)
    - *“A bag of freshly baked bread is dangling at the door.”*


<span id="route-74"></span>

??? note "Stage 74 · Mikhail, Gruiik, stepping on a trigger on home · 6 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “Here I have some bread for you.”

    - **Needs:** stage 20; not yet stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); hand over 1× [Bread](../items/bread.md)
    - *“It's about time.”*

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “Here I have some bread for you.”

    - **Needs:** stage 20; not yet stage 70; hand over 1× [Bread](../items/bread.md)
    - *“It's about time.”*

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “Here I have some bread for you.”

    - **Needs:** stage 20; not yet stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); hand over 1× [Bread](../items/bread.md)
    - *“It's about time.”*

    **Way 4:** Talk to [Mikhail](../monsters/mikhail.md), choose “Here I have some bread for you.”

    - **Needs:** stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); hand over 1× [Bread](../items/bread.md)

    **Way 5:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “Here I have some bread for you.”

    - **Needs:** stage 70; hand over 1× [Bread](../items/bread.md)

    **Way 6:** Stepping on a trigger on [Home](../maps/home.md), choose “Here I have some bread for you.”

    - **Needs:** stage 70; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); hand over 1× [Bread](../items/bread.md)


<span id="route-90"></span>

??? note "Stage 90 · Mikhail, Gruiik, stepping on a trigger on home · 3 ways"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “Hey - I have brought some bread already.”

    - **Needs:** stage 70, 74; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
    - *“Good! Now I don't need you anymore!”*

    **Way 2:** Talk to [Gruiik](../monsters/ratdom_mikhail.md), choose “Hey - I have brought some bread already.”

    - **Needs:** stage 70, 74
    - *“Good! Now I don't need you anymore!”*

    **Way 3:** Stepping on a trigger on [Home](../maps/home.md), choose “Hey - I have brought some bread already.”

    - **Needs:** stage 70, 74; reached stage 1 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); not reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)
    - *“Good! Now I don't need you anymore!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.6.1](../versions/0.8.6.1.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Stage 10 journal text changed<br>Stage 20 journal text changed<br>Stage 30 journal text changed<br>Stage 32 journal text changed<br>Stage 52 journal text changed<br>Stage 54 journal text changed<br>Stage 72 journal text changed<br>Stage 74 journal text changed<br>Stage 90 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ratdom_mikhail` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 32, 52, 54, 70, 72, 74, 90 |
    | Dialogue nodes setting stages | 10: `ratdom_mikhail_04`, 20: `ratdom_mikhail_10`, 30: `ratdom_check_kills_mara`, 32: `ratdom_check_kills_tharal`, 52: `ratdom_mikhail_50_2`, 54: `ratdom_mikhail_50_4`, 70: `ratdom_mikhail_10_10`, 72: `crossglen_ratdom_key_3_20`, 74: `ratdom_mikhail_10_20`, 74: `ratdom_mikhail_74`, 90: `ratdom_mikhail_80` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
