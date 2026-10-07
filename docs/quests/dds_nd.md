---
description: "Darkness in the Daylight and Shadows story flags is a hidden quest in Andor's Trail, started by stepping on a trigger on crossroads. 8 stages. 1=Miri spawned at Crossroads"
---

# Darkness in the Daylight and Shadows story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `dds_nd` |
| **In journal** | No (hidden flag) |
| **Stages** | 8 |
| **Started by** | stepping on a trigger on [Crossroads](../maps/crossroads.md) |
| **NPCs involved** | [Borvis](../monsters/dds_borvis.md), [Mikhail](../monsters/mikhail.md), [Miri](../monsters/dds_miri.md) |
| **Locations** | [Galmore 41](../maps/galmore_41.md), [Galmore 45](../maps/galmore_45.md), [Home](../maps/home.md), [Houseatcrossroads 0](../maps/houseatcrossroads0.md) |
| **Related quests** | 3 |

</div>

## Overview

> 1=Miri spawned at Crossroads

## Prerequisites to start

Start with stepping on a trigger on [Crossroads](../maps/crossroads.md). Required:

- NOT reached stage 1 of [Darkness in the Daylight and Shadows story flags (hidden flag)](../quests/dds_nd.md#stage-1)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Darkness in the Daylight](darkness_in_daylight.md#stage-50) | stage 50 reached, for stage 3 here |
| Requires | [Darkness in the Daylight](darkness_in_daylight.md#stage-150) | stage 150 reached, for stage 2 here |
| Requires | [Darkness in the Daylight](darkness_in_daylight.md#stage-260) | stage 260 reached, for stage 6 here |
| Requires | [Darkness in the Daylight](darkness_in_daylight.md#stage-310) | stage 310 reached, for stage 20 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stage 20 here |
| Requires | [Shadows](shadows.md#stage-40) | stage 40 reached, for stage 3 here |
| Requires | [Shadows](shadows.md#stage-240) | stage 240 reached, for stage 6 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | 1=Miri spawned at Crossroads<br><span class="qnote">⚡ A scripted event can now trigger on [Houseatcrossroads 0](../maps/houseatcrossroads0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span> | stepping on a trigger on [Crossroads](../maps/crossroads.md) | spawns monsters on houseatcrossroads0 |
| <span id="stage-2"></span>[2](#route-2) | 2=Miri spawned 2<br><span class="qnote">⚡ A scripted event can now trigger on [Houseatcrossroads 0](../maps/houseatcrossroads0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span> | stepping on a trigger on [Crossroads](../maps/crossroads.md) | spawns monsters on houseatcrossroads0 |
| <span id="stage-3"></span>[3](#route-3) | 3=Dark shield active<br><span class="qnote">🔒 An area on [Galmore 45](../maps/galmore_45.md) becomes blocked off.</span><br><span class="qnote">🗺️ Part of [Galmore 45](../maps/galmore_45.md) visibly changes.</span> | [Borvis](../monsters/dds_borvis.md), [Miri](../monsters/dds_miri.md) | varies by route (see below) |
| <span id="stage-4"></span>4 | 4=Miri spawned 3 | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-5"></span>5 | 5=Dark priest killed | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-6"></span>[6](#route-6) | 6=Andor spawned at Rosmara/Alynndir | [Borvis](../monsters/dds_borvis.md), [Miri](../monsters/dds_miri.md) | varies by route (see below) |
| <span id="stage-11"></span>[11](#route-11) | 11=Borvis spawned near Alynndir's hut<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Cabin norcity road 1](../maps/cabin_norcity_road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road 4](../maps/road4.md).</span> | stepping on a trigger on [Cabin norcity road 1](../maps/cabin_norcity_road1.md) | spawns monsters on road5 |
| <span id="stage-20"></span>[20](#route-20) | 20=Told Mikhail about meeting Andor in Miri's or Borvis' quest | [Mikhail](../monsters/mikhail.md) | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · stepping on a trigger on crossroads · 1 way"

    **Way 1:** Stepping on a trigger on [Crossroads](../maps/crossroads.md)

    - **Needs:** not yet stage 1
    - **Gives:** spawns monsters on houseatcrossroads0


<span id="route-2"></span>

??? note "Stage 2 · stepping on a trigger on crossroads · 1 way"

    **Way 1:** Stepping on a trigger on [Crossroads](../maps/crossroads.md)

    - **Needs:** not yet stage 2; reached stage 150 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-150); 5 rounds passed since timer “dds_miri”
    - **Gives:** spawns monsters on houseatcrossroads0


<span id="route-3"></span>

??? note "Stage 3 · Borvis, Miri · 2 ways"

    **Way 1:** Talk to [Borvis](../monsters/dds_borvis.md), automatic

    - **Needs:** reached stage 40 of [Shadows](../quests/shadows.md#stage-40)
    - **Gives:** sets stage 40 of [Shadows](../quests/shadows.md#stage-40), spawns monsters on galmore_45, spawns monsters on galmore_45
    - *“Journey to the south of Stoutford, into the forests there. See what that Shadow priest is doing there, and stop him from doing it.”*

    **Way 2:** Talk to [Miri](../monsters/dds_miri.md), automatic

    - **Needs:** reached stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50)
    - **Gives:** sets stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50), spawns monsters on galmore_45, spawns monsters on galmore_45
    - *“Journey to the south of Stoutford, into the weird lands there. Investigate what's going on in the Purple Hills.”*


<span id="route-6"></span>

??? note "Stage 6 · Borvis, Miri · 2 ways"

    **Way 1:** Talk to [Borvis](../monsters/dds_borvis.md), choose “Really? Tell me!”

    - **Needs:** reached stage 240 of [Shadows](../quests/shadows.md#stage-240); killed 1× [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest_monster)
    - **Gives:** sets stage 260 of [Shadows](../quests/shadows.md#stage-260), removes monsters from galmore_41, spawns monsters on road5, spawns monsters on road5_house
    - *“Andor is going to visit Alynndir to refill his travel supplies.”*

    **Way 2:** Talk to [Miri](../monsters/dds_miri.md), choose “Really? Tell me!”

    - **Needs:** reached stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260); killed 1× [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest_monster)
    - **Gives:** sets stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280), removes monsters from galmore_41, spawns monsters on houseatcrossroads0, spawns monsters on wayto_feygard_duleian_2
    - *“Andor is going to visit Rosmara to refill his travel supplies.”*


<span id="route-11"></span>

??? note "Stage 11 · stepping on a trigger on cabin_norcity_road1 · 1 way"

    **Way 1:** Stepping on a trigger on [Cabin norcity road 1](../maps/cabin_norcity_road1.md)

    - **Needs:** not yet stage 11
    - **Gives:** spawns monsters on road5


<span id="route-20"></span>

??? note "Stage 20 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “He just said that he couldn't come now. Then he ran away before I could ask him what he was up to.”

    - **Needs:** not yet stage 20; reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 310 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-310)
    - *“Mikhail! Don't you dare talk to our child like that!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `dds_nd` |
    | Name in game data | `Darkness in the Daylight and Shadows - Non displayed` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 11, 20 |
    | Dialogue nodes setting stages | 1: `dds_miri_spawn_10`, 2: `dds_miri_spawn_20`, 3: `dds_borvis_100`, 3: `dds_miri_110`, 6: `dds_borvis_590`, 6: `dds_miri_590`, 11: `dds_borvis_spawn_10`, 20: `mikhail_news_64` |
    | Dialogue nodes clearing stages | 3: `dds_dark_shadow_52`, 3: `dds_dark_shadow_152` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
