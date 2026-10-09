---
description: "A familiar shadow is a quest in Andor's Trail, started by walking into a blocked passage on galmore_32. 8 stages, 6,548 XP in total. In the devastated lands south of Stoutford, I found an ominous stone etched with strange symbols."
---

# A familiar shadow

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `familiar_shadow` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 70) |
| **Started by** | walking into a blocked passage on [Galmore 32](../maps/galmore_32.md) |
| **NPCs involved** | [Leta](../monsters/leta.md), [Mikhail](../monsters/mikhail.md), [Old Leta](../monsters/old_leta.md), [Old Oromir](../monsters/old_oromir.md) |
| **Locations** | [Crossglen farmhouse](../maps/crossglen_farmhouse.md), [Home](../maps/home.md), [Waytogalmore 0](../maps/waytogalmore0.md) |
| **Total XP** | 6,548 |
| **Related quests** | 5 |

</div>

## Overview

> In the devastated lands south of Stoutford, I found an ominous stone etched with strange symbols.

## Prerequisites to start

Start with walking into a blocked passage on [Galmore 32](../maps/galmore_32.md). Required:

- NOT reached stage 10 of [A familiar shadow](../quests/familiar_shadow.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Thief apprentice](Thieves01.md#stage-60) | stage 60 reached, for stage 10 here |
| Requires | [Missing husband](leta.md#stage-100) | stage 100 reached, for stage 10 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [You're the postman](postman.md#stage-10) | stage 10 reached, for stage 10 here |
| Blocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-1) | reaching stage 50 here closes stage 1 there |
| Blocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-2) | reaching stage 50 here closes stage 2 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">In the devastated lands south of Stoutford, I found an ominous stone… ▸</span><span class="l">▴ less</span></summary>In the devastated lands south of Stoutford, I found an ominous stone etched with strange symbols.</details> | walking into a blocked passage on [Galmore 32](../maps/galmore_32.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">As I touched its glowing mark, an unnatural chill ran through me,… ▸</span><span class="l">▴ less</span></summary>As I touched its glowing mark, an unnatural chill ran through me, and I heard a voice in my mind, calling out for help. It spoke of torment and told me to return to Crossglen to find answers.</details><br><span class="qnote">🔒 An area on [Galmore 32](../maps/galmore_32.md) becomes blocked off.</span> | walking into a blocked passage on [Galmore 32](../maps/galmore_32.md) | applies condition pull_of_the_mark, applies condition fear, removes monsters from galmore_32, removes monsters from galmore_32 |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The presence of the mark grows unbearable. I feel an overwhelming… ▸</span><span class="l">▴ less</span></summary>The presence of the mark grows unbearable. I feel an overwhelming pull to return to Crossglen. There is something wrong, and I sense it's tied to my father. I must hurry to see what's happening.</details><br><span class="qnote">🔒 An area on [Crossglen](../maps/crossglen.md) becomes blocked off.</span> | walking into a blocked passage on [Galmore 32](../maps/galmore_32.md) | spawns monsters on galmore_32, spawns monsters on galmore_32 |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I spoke to father. He assured me he's fine, but mentioned Leta… ▸</span><span class="l">▴ less</span></summary>I spoke to father. He assured me he's fine, but mentioned Leta hasn't been herself lately. She's been pacing her home and muttering to herself. I should check on her and see what's going on.</details> | [Mikhail](../monsters/mikhail.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">When I confronted Leta, she seemed different--angrier, more… ▸</span><span class="l">▴ less</span></summary>When I confronted Leta, she seemed different--angrier, more agitated. As I pressed her, a dark spirit suddenly manifested before me and attacked.</details> | [Leta](../monsters/leta.md) | spawns monsters on crossglen_farmhouse, removes monsters from crossglen_farmhouse, removes monsters from crossglen_farmhouse_basement, removes monsters from crossglen, removes monsters from crossglen_farmhouse_basement |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I defeated the Dark spirit, but it didn't feel like the end. The… ▸</span><span class="l">▴ less</span></summary>I defeated the Dark spirit, but it didn't feel like the end. The Dark spirit trapped inside Leta has fled back to the devastated lands south of Stoutford, where its power can grow stronger. I need to return there and finish what I started.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [Crossglen](../maps/crossglen.md) | spawns monsters on galmore_32 |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">In the depths of the devastated lands south of Stoutford, I found… ▸</span><span class="l">▴ less</span></summary>In the depths of the devastated lands south of Stoutford, I found the dark spirit waiting for me. It was stronger this time, but I defeated it once and for all. Whatever bond it had with me and Leta is broken. I should check-up on Leta again.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 32](../maps/galmore_32.md).</span> | stepping on a trigger on [Galmore 32](../maps/galmore_32.md) | spawns monsters on crossglen_farmhouse, spawns monsters on crossglen_farmhouse_basement, applies condition pull_of_the_mark, removes monsters from galmore_32, removes monsters from galmore_32, removes monsters from galmore_32 |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I returned to Crossglen to find everything changed. Leta has aged… ▸</span><span class="l">▴ less</span></summary>I returned to Crossglen to find everything changed. Leta has aged decades in an instant. Her child is now fully grown, and her timid husband, Oromir, seems like a different man entirely. They remember nothing of what happened. The spirit may be gone, but its curse has left a permanent mark on the lives it touched.</details> **(ends quest)** | [Old Leta](../monsters/old_leta.md), [Old Oromir](../monsters/old_oromir.md) | 6,548 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-5"></span>

??? note "Stage 5 · walking into a blocked passage on galmore_32 · 1 way"

    **Way 1:** Walking into a blocked passage on [Galmore 32](../maps/galmore_32.md)

    - **Needs:** not yet stage 10


<span id="route-10"></span>

??? note "Stage 10 · walking into a blocked passage on galmore_32 · 1 way"

    **Way 1:** Walking into a blocked passage on [Galmore 32](../maps/galmore_32.md), choose “[Touch the stone.]”

    - **Needs:** not yet stage 10; reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60); reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 10 of [You're the postman](../quests/postman.md#stage-10)
    - **Gives:** applies condition pull_of_the_mark, applies condition fear, removes monsters from galmore_32, removes monsters from galmore_32
    - *“The moment your hand meets the mark, an icy jolt shoots through your body. A voice echoes in your mind, low and venomous, yet pleading:…”*


<span id="route-20"></span>

??? note "Stage 20 · walking into a blocked passage on galmore_32 · 1 way"

    **Way 1:** Walking into a blocked passage on [Galmore 32](../maps/galmore_32.md)

    - **Gives:** spawns monsters on galmore_32, spawns monsters on galmore_32
    - *“The weight of the mark grows heavier on your mind. A strange, oppressive feeling claws at your chest, urging you to leave this place and…”*


<span id="route-30"></span>

??? note "Stage 30 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “I don't know...something feels wrong. I thought maybe you were in danger.”

    - **Needs:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-20) is 20
    - *“What's gotten into you? I'm fine, but the same can't be said for Leta. I've seen her pacing in that house of hers, muttering to herself…”*


<span id="route-40"></span>

??? note "Stage 40 · Leta · 1 way"

    **Way 1:** Talk to [Leta](../monsters/leta.md), choose “Leta, talk to me. What's going on?”

    - **Needs:** stage 30
    - **Gives:** spawns monsters on crossglen_farmhouse, removes monsters from crossglen_farmhouse, removes monsters from crossglen_farmhouse_basement, removes monsters from crossglen, removes monsters from crossglen_farmhouse_basement
    - *“A dark aura surrounds Leta as a spirit begins its manifestation. Leta lets out a cry and vanishes as the spirit rises.”*


<span id="route-50"></span>

??? note "Stage 50 · stepping on a trigger on crossglen · 1 way"

    **Way 1:** Stepping on a trigger on [Crossglen](../maps/crossglen.md)

    - **Needs:** not yet stage 50; killed 1× [Dark spirit](../monsters/crossglen_dark_spirit.md)
    - **Gives:** spawns monsters on galmore_32
    - *“The Dark spirit has been defeated, but you feel as if this issue is unresolved. Something is telling you that it has fled back to the…”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on galmore_32 · 1 way"

    **Way 1:** Stepping on a trigger on [Galmore 32](../maps/galmore_32.md)

    - **Needs:** not yet stage 60; killed 1× [Dark spirit](../monsters/crossglen_dark_spirit.md#v-undertell_dark_spirit)
    - **Gives:** spawns monsters on crossglen_farmhouse, spawns monsters on crossglen_farmhouse_basement, applies condition pull_of_the_mark, removes monsters from galmore_32, removes monsters from galmore_32, removes monsters from galmore_32
    - *“As the dark spirit fades, the suffocating darkness that had plagued this place begins to lift. The air feels lighter, though the…”*


<span id="route-70"></span>

??? note "Stage 70 · Old Leta, Old Oromir · 2 ways"

    **Way 1:** Talk to [Old Leta](../monsters/old_leta.md), choose “I didn't do this to you. This doesn't feel right. What happened after the spirit was defeated?”

    - **Needs:** latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-60) is 60
    - *“While looking between Leta and Oromir, you are unsettled by their calm acceptance. The house feels peaceful, but the air is heavy with…”*

    **Way 2:** Talk to [Old Oromir](../monsters/old_oromir.md), choose “I didn't do this to you. This doesn't feel right. What happened after the spirit was defeated?”

    - **Needs:** latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-60) is 60
    - *“While looking between Leta and Oromir, you are unsettled by their calm acceptance. The house feels peaceful, but the air is heavy with…”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `familiar_shadow` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 30, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 5: `galmore_marked_stone_key`, 10: `galmore_marked_stone_10`, 20: `galmore_marked_stone_20`, 30: `galmore_marked_stone_mikhail`, 40: `galmore_marked_stone_leta_narrator`, 50: `crossglen_dark_spirit_defeated_1`, 60: `galmore_dark_spirit_defeated_10`, 70: `old_oromir_and_leta_narrator_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
