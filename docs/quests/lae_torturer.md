---
description: "Shadow of the torturer is a quest in Andor's Trail, started by Laeroth prisoner (laerothprison4). 16 stages. In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story."
---

# Shadow of the torturer

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lae_torturer` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 80, 130) |
| **Started by** | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([Laerothprison 4](../maps/laerothprison4.md)), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4a) |
| **NPCs involved** | [Dark watch](../monsters/lae_demon4.md#v-lae_demon4b), [Dark watch](../monsters/lae_demon4.md), [Dark watch](../monsters/lae_demon4.md#v-lae_demon9), [Kotheses](../monsters/kotheses.md), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4i), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) +1 |
| **Locations** | [Laerothprison 4](../maps/laerothprison4.md), [Laerothprison 7](../maps/laerothprison7.md) |
| **Related quests** | 1 |

</div>

## Overview

> In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story.

## Prerequisites to start

Start with [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([Laerothprison 4](../maps/laerothprison4.md)). Required:

- reached stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31)
- reached stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33)
- reached stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-31) | stage 31 reached, for stages 5, 10 here |
| Requires | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-33) | stage 33 reached, for stages 5, 10 here |
| Requires | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-34) | stage 34 reached, for stages 5, 10 here |
| Blocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-31) | reaching stage 110 here closes stage 31 there |
| Blocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-32) | reaching stage 110 here closes stage 32 there |
| Blocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-33) | reaching stage 110 here closes stage 33 there |
| Blocks | [Laeroth story flags (hidden flag)](laeroth_nondisplay.md#stage-34) | reaching stage 110 here closes stage 34 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">In the dungeon of the mansion I found some ghosts of prisoners. One… ▸</span><span class="l">▴ less</span></summary>In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison 4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) | changes map laerothprison4 |
| <span id="stage-10"></span>[10](#route-10) | I have agreed to help the spirits in the prison be free of the prison torturer. | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) | – |
| <span id="stage-20"></span>[20](#route-20) | I didn't want to help the spirits in the prison be free of the prison torturer.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison 4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md) | – |
| <span id="stage-25"></span>[25](#route-25) | <details class="jt"><summary><span class="s">Kotheses the torturer offered to teach me his art, as he had done… ▸</span><span class="l">▴ less</span></summary>Kotheses the torturer offered to teach me his art, as he had done for Andor before.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison 7](../maps/laerothprison7.md).</span> | [Kotheses](../monsters/kotheses.md) | removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4 |
| <span id="stage-30"></span>[30](#route-30) | I accepted his offer to apprentice with him.<br><span class="qnote">⚡ A scripted event can now trigger on [Laerothprison 7](../maps/laerothprison7.md).</span> | [Kotheses](../monsters/kotheses.md) | – |
| <span id="stage-35"></span>[35](#route-35) | Kotheses gave me an Oegyth crystal. | [Kotheses](../monsters/kotheses.md) | 1× [Oegyth crystal](../items/oegyth.md) |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">In order to imprison the released prisoners again, I should call the… ▸</span><span class="l">▴ less</span></summary>In order to imprison the released prisoners again, I should call the demon guard by throwing an Oegyth crystal into the abyss.</details> | [Kotheses](../monsters/kotheses.md) | – |
| <span id="stage-50"></span>[50](#route-50) | Kotheses scolded me because I killed his precious demons. | [Kotheses](../monsters/kotheses.md) | – |
| <span id="stage-60"></span>[60](#route-60) | I declined the offer to become his apprentice. | [Kotheses](../monsters/kotheses.md) | – |
| <span id="stage-70"></span>70 | Kotheses attacked me. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-80"></span>[80](#route-80) | I told the prisoners that I had killed their torturer. Now they could get peace. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison 4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md) | – |
| <span id="stage-100"></span>[100](#route-100) | I have thrown an Oegyth crystal down into the abyss to call for the dark watch.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison 7](../maps/laerothprison7.md).</span> | stepping on a trigger on [Laerothprison 7](../maps/laerothprison7.md) | spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7 |
| <span id="stage-110"></span>[110](#route-110) | I got back the Oegyth crystal from the chief of the Demon guard. | [Dark watch](../monsters/lae_demon4.md#v-lae_demon9) | 1× [Oegyth crystal](../items/oegyth.md), removes monsters from laerothprison7, spawns monsters on laerothprison7 |
| <span id="stage-114"></span>[114](#route-114) | I ordered the demons to watch over the prisoners. | [Dark watch](../monsters/lae_demon4.md) | removes monsters from laerothprison7, removes monsters from laerothprison7, spawns monsters on laerothprison4, spawns monsters on laerothprison4, changes map laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4 |
| <span id="stage-120"></span>[120](#route-120) | <details class="jt"><summary><span class="s">I took my leave from Kotheses, who, incidentally, forgot to reclaim… ▸</span><span class="l">▴ less</span></summary>I took my leave from Kotheses, who, incidentally, forgot to reclaim his Oegyth crystal.</details> | [Kotheses](../monsters/kotheses.md) | – |
| <span id="stage-130"></span>[130](#route-130) | <details class="jt"><summary><span class="s">Everything was in order when I left. The prisoners were back in… ▸</span><span class="l">▴ less</span></summary>Everything was in order when I left. The prisoners were back in their cells, and the Demon guard were on duty again.</details> **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison 4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md) | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-5"></span>

??? note "Stage 5 · Laeroth prisoner · 1 way"

    **Way 1:** Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), choose “What sort of help?”

    - **Needs:** reached stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)
    - **Gives:** changes map laerothprison4
    - *“It didn't work, because we had so little life left anyway.”*


<span id="route-10"></span>

??? note "Stage 10 · Laeroth prisoner · 1 way"

    **Way 1:** Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), choose “OK. I'll do it. I am not afraid of a few monsters!”

    - **Needs:** not yet stage 20; reached stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)
    - *“Thank you! But beware! He has guards that are like him. They may appear to be human at first glance, but they are not!”*


<span id="route-20"></span>

??? note "Stage 20 · Laeroth prisoner, stepping on a trigger on laerothprison4 · 2 ways"

    **Way 1:** Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), automatic

    - **Needs:** stage 25; not killed 1× [Kotheses](../monsters/kotheses.md)
    - *“Ohhh! What will become of us?”*

    **Way 2:** Stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md)

    - **Needs:** stage 25; not killed 1× [Kotheses](../monsters/kotheses.md)
    - *“Ohhh! What will become of us?”*


<span id="route-25"></span>

??? note "Stage 25 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), automatic

    - **Needs:** not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - **Gives:** removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4
    - *“Would you like to learn the trade of a torturer?”*


<span id="route-30"></span>

??? note "Stage 30 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), choose “Very gladly. I always like to learn new things.”

    - **Needs:** not yet stage 60; not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - *“OK, then let's get started. This is a very important job, you know?”*


<span id="route-35"></span>

??? note "Stage 35 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), choose “Sigh.”

    - **Needs:** not yet stage 35, 60; not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - **Gives:** 1× [Oegyth crystal](../items/oegyth.md)
    - *“Here take this Oegyth crystal.”*


<span id="route-40"></span>

??? note "Stage 40 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), choose “What?!”

    - **Needs:** stage 35; not yet stage 60; not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - *“Do it. Then run for your life back to me so that I can protect you from them.”*


<span id="route-50"></span>

??? note "Stage 50 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), automatic

    - *“Why do you kill my precious demons?! I told you to stay here beside me!”*


<span id="route-60"></span>

??? note "Stage 60 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), choose “That is no job for me.”

    - **Needs:** not yet stage 30; not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - *“What a pity. At least let me warn you about the prisoners above.”*


<span id="route-80"></span>

??? note "Stage 80 · Laeroth prisoner, stepping on a trigger on laerothprison4 · 2 ways"

    **Way 1:** Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), automatic

    - **Needs:** stage 25; killed 1× [Kotheses](../monsters/kotheses.md)
    - *“Ooooh! We are eternally grateful!”*

    **Way 2:** Stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md)

    - **Needs:** killed 1× [Kotheses](../monsters/kotheses.md)
    - *“Ooooh! We are eternally grateful!”*


<span id="route-100"></span>

??? note "Stage 100 · stepping on a trigger on laerothprison7 · 1 way"

    **Way 1:** Stepping on a trigger on [Laerothprison 7](../maps/laerothprison7.md), choose “Let's throw an oegyth crystal down there.”

    - **Needs:** not yet stage 100; hand over 1× [Oegyth crystal](../items/oegyth.md)
    - **Gives:** spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7
    - *“You hear an uproar from far away. But coming nearer and nearer.”*


<span id="route-110"></span>

??? note "Stage 110 · Dark watch · 1 way"

    **Way 1:** Talk to [Dark watch](../monsters/lae_demon4.md#v-lae_demon9), automatic

    - **Gives:** 1× [Oegyth crystal](../items/oegyth.md), removes monsters from laerothprison7, spawns monsters on laerothprison7
    - *“[hollow voice] Take back your glass ball, brave little human.”*


<span id="route-114"></span>

??? note "Stage 114 · Dark watch · 1 way"

    **Way 1:** Talk to [Dark watch](../monsters/lae_demon4.md), automatic

    - **Gives:** removes monsters from laerothprison7, removes monsters from laerothprison7, spawns monsters on laerothprison4, spawns monsters on laerothprison4, changes map laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4
    - <small>Also: clears stage 31 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-31), clears stage 32 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-32), clears stage 33 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-33), clears stage 34 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)</small>
    - *“Command us!”*


<span id="route-120"></span>

??? note "Stage 120 · Kotheses · 1 way"

    **Way 1:** Talk to [Kotheses](../monsters/kotheses.md), automatic

    - **Needs:** stage 110; not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); not killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); not killed 1× [Dark watch](../monsters/lae_demon4.md)
    - *“I see it in your eyes - you want to leave too. Like your brother.”*


<span id="route-130"></span>

??? note "Stage 130 · Laeroth prisoner, stepping on a trigger on laerothprison4 · 2 ways"

    **Way 1:** Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), automatic

    - **Needs:** stage 25, 114; not yet stage 130
    - *“Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.”*

    **Way 2:** Stepping on a trigger on [Laerothprison 4](../maps/laerothprison4.md)

    - **Needs:** stage 114; not yet stage 130
    - *“Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | Stage 40 journal text changed<br>Stage 100 journal text changed<br>Stage 130 journal text changed<br>Dialogue: 1 line changed<br>· text: “Okay, then let's get started. This is a very important job, you know?” → “OK, then let's get started. This is a very important job, you know?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lae_torturer` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 25, 30, 35, 40, 50, 60, 70, 80, 100, 110, 114, 120, 130 |
    | Dialogue nodes setting stages | 5: `lae_prison_02b`, 10: `lae_prison_03`, 20: `lae_prison_3a`, 25: `lae_torturer_10a`, 30: `lae_torturer_30`, 35: `lae_torturer_44`, 40: `lae_torturer_48`, 50: `lae_torturer_2`, 60: `lae_torturer_60`, 80: `lae_prison_end_20`, 100: `lae_demon_call_20`, 110: `lae_demon9`, 114: `lae_demon4`, 120: `lae_torturer_110`, 130: `lae_prison_end_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
