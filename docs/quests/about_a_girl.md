---
description: "About a girl is a quest in Andor's Trail, started by Liberated Elytharan ghost (undertell_3_00). 9 stages, 10,207 XP in total. Two Elytharan slave ghosts spoke quietly of another who has not joined them at the table. They said she still hides east of them, afraid the Shades might return."
---

# About a girl

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `about_a_girl` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 90) |
| **Started by** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([Undertell 3 00](../maps/undertell_3_00.md)) |
| **NPCs involved** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), [Thalen](../monsters/thalen.md) |
| **Locations** | [Undertell 3 00](../maps/undertell_3_00.md), [Undertell 3 lava 00](../maps/undertell_3_lava_00.md) |
| **Total XP** | 10,207 |
| **Related quests** | 2 |

</div>

## Overview

> Two Elytharan slave ghosts spoke quietly of another who has not joined them at the table. They said she still hides east of them, afraid the Shades might return.

## Prerequisites to start

Start with [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([Undertell 3 00](../maps/undertell_3_00.md)). Required:

- reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10)
- NOT reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The fifth master](fifth_master.md#stage-90) | stage 90 reached, for stage 50 here |
| Requires | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-85) | stage 85 reached, for stage 80 here |
| Unlocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-85) | stage 85 there needs stage 70 here |
| Unlocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-90) | stage 90 there needs stage 40 here |
| Blocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-85) | reaching stage 80 here closes stage 85 there |
| Blocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-90) | reaching stage 70 here closes stage 90 there |
| Blocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-95) | reaching stage 50 here closes stage 95 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Two Elytharan slave ghosts spoke quietly of another who has not… ▸</span><span class="l">▴ less</span></summary>Two Elytharan slave ghosts spoke quietly of another who has not joined them at the table. They said she still hides east of them, afraid the Shades might return.</details> | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The ghosts said the girl believed she could protect herself with a… ▸</span><span class="l">▴ less</span></summary>The ghosts said the girl believed she could protect herself with a folded copper talisman she made long ago, but she lost it before she could hide it away from the evil of Undertell.</details> | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">They remembered that such objects were sometimes taken during… ▸</span><span class="l">▴ less</span></summary>They remembered that such objects were sometimes taken during inspections, gathered with other personal effects and carried upward to the Masters.</details> | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I was told that one of the Masters may still possess the folded… ▸</span><span class="l">▴ less</span></summary>I was told that one of the Masters may still possess the folded copper talisman, kept not for protection, but for understanding.</details> | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) | spawns monsters on undertell_3_12 |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">A Master acknowledged the talisman when I asked about it. He spoke… ▸</span><span class="l">▴ less</span></summary>A Master acknowledged the talisman when I asked about it. He spoke of fear made solid, and said such fear was useful to those who taught the Shadow obedience rather than faith. It can be found in the "lower records", whatever that means.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Undertell 4 00](../maps/undertell_4_00.md).</span> | [Thalen](../monsters/thalen.md) | – |
| <span id="stage-60"></span>[60](#route-60) | In the Undertell archival room, I found the folded coin talisman. | walking into a blocked passage on [Undertell archive 2](../maps/undertell_archive2.md) | 1× [Folded copper talisman](../items/folded_copper_talisman.md) |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I found the terrified girl hiding behind a collapsed rock wall. She… ▸</span><span class="l">▴ less</span></summary>I found the terrified girl hiding behind a collapsed rock wall. She would not approach me, nor leave her hiding place.</details> | walking into a blocked passage on [Undertell 3 12](../maps/undertell_3_12.md) | – |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">I tossed the folded copper talisman to her. Only then did she step… ▸</span><span class="l">▴ less</span></summary>I tossed the folded copper talisman to her. Only then did she step forward, no longer clinging to the corner she had claimed as safety.</details> | walking into a blocked passage on [Undertell 3 12](../maps/undertell_3_12.md) | removes monsters from undertell_3_12, spawns monsters on undertell_3_00 |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">The girl rejoined the others at the table. The Elytharan ghosts… ▸</span><span class="l">▴ less</span></summary>The girl rejoined the others at the table. The Elytharan ghosts spoke her name softly, as if afraid to lose her again.</details> **(ends quest)** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) | 10,207 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Liberated Elytharan ghost · 1 way"

    **Way 1:** Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), automatic

    - **Needs:** stage 10; not yet stage 20
    - *“There is another. A girl. She never came back here when the shades fell. Instead, she hides east of here. Probably in a corner somewhere.”*


<span id="route-20"></span>

??? note "Stage 20 · Liberated Elytharan ghost · 1 way"

    **Way 1:** Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), choose “What did she make?”

    - **Needs:** stage 10; not yet stage 20
    - *“A folded coin. Copper. She believed evil could be trapped if it could not breathe.”*


<span id="route-30"></span>

??? note "Stage 30 · Liberated Elytharan ghost · 1 way"

    **Way 1:** Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), choose “I am still trying to understand what happened to the talisman.”

    - **Needs:** stage 20; not yet stage 30
    - *“They used to gather our things. Count them. Decide what mattered.”*


<span id="route-40"></span>

??? note "Stage 40 · Liberated Elytharan ghost · 1 way"

    **Way 1:** Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), choose “Then where should I look?”

    - **Needs:** latest stage of [About a girl](../quests/about_a_girl.md#stage-30) is 30
    - **Gives:** spawns monsters on undertell_3_12
    - *“With those who believed fear could be shaped. Go to the Masters.”*


<span id="route-50"></span>

??? note "Stage 50 · Thalen · 1 way"

    **Way 1:** Talk to [Thalen](../monsters/thalen.md), choose “Where do I find it?”

    - **Needs:** stage 40; not yet stage 50; reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90)
    - *“In the lower records. Where discarded faith is kept for study, not mercy.”*


<span id="route-60"></span>

??? note "Stage 60 · walking into a blocked passage on undertell_archive2 · 1 way"

    **Way 1:** Walking into a blocked passage on [Undertell archive 2](../maps/undertell_archive2.md), choose “[Take the folded copper piece.]”

    - **Needs:** not yet stage 60
    - **Gives:** 1× [Folded copper talisman](../items/folded_copper_talisman.md)
    - *“You grab the coin off the shelf.”*


<span id="route-70"></span>

??? note "Stage 70 · walking into a blocked passage on undertell_3_12 · 1 way"

    **Way 1:** Walking into a blocked passage on [Undertell 3 12](../maps/undertell_3_12.md)

    - **Needs:** stage 40; not yet stage 70
    - *“THIS PERSON IS TRYING TO DESTROY ME!”*


<span id="route-80"></span>

??? note "Stage 80 · walking into a blocked passage on undertell_3_12 · 1 way"

    **Way 1:** Walking into a blocked passage on [Undertell 3 12](../maps/undertell_3_12.md), choose “I will meet you there.”

    - **Needs:** stage 70; not yet stage 80; reached stage 85 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-85)
    - **Gives:** removes monsters from undertell_3_12, spawns monsters on undertell_3_00
    - *“My name is Syrra. Thank you for bringing it back.”*


<span id="route-90"></span>

??? note "Stage 90 · Liberated Elytharan ghost · 1 way"

    **Way 1:** Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), choose “Then this is enough.”

    - **Needs:** stage 80; not yet stage 90
    - *“It is.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `about_a_girl` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `elytharan_liberated_ghost_about_girl_10`, 20: `elytharan_liberated_ghost_about_girl_10c`, 30: `elytharan_liberated_ghost_about_girl_20b`, 40: `elytharan_liberated_ghost_about_girl_30b`, 50: `master_thalen_about_girl_90`, 60: `folded_coin_25`, 70: `about_girl_meet_10`, 80: `about_girl_meet_90`, 90: `about_girl_syrra_90c` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
