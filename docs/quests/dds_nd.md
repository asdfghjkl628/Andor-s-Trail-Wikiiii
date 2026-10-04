# Darkness in the Daylight and Shadows - Non displayed

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `dds_nd` |
| **In journal** | No (hidden flag) |
| **Stages** | 8 |
| **Started by** | stepping on a trigger on [crossroads](../maps/crossroads.md) |
| **NPCs involved** | [Borvis](../monsters/dds_borvis.md), [Mikhail](../monsters/mikhail.md), [Miri](../monsters/dds_miri.md) |
| **Locations** | [galmore_41](../maps/galmore_41.md), [galmore_45](../maps/galmore_45.md), [home](../maps/home.md), [houseatcrossroads0](../maps/houseatcrossroads0.md) |
| **Related quests** | 3 |

</div>

## Overview

> 1=Miri spawned at Crossroads

## Prerequisites to start

Start with stepping on a trigger on [crossroads](../maps/crossroads.md). Required:

- NOT reached stage 1 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-1)


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

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=Miri spawned at Crossroads<br><span class="qnote">⚡ A scripted event can now trigger on [Houseatcrossroads0](../maps/houseatcrossroads0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span> | stepping on a trigger on [crossroads](../maps/crossroads.md) | – | spawns monsters on houseatcrossroads0 |
| <span id="stage-2"></span>2 | 2=Miri spawned 2<br><span class="qnote">⚡ A scripted event can now trigger on [Houseatcrossroads0](../maps/houseatcrossroads0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span> | stepping on a trigger on [crossroads](../maps/crossroads.md) | – | spawns monsters on houseatcrossroads0 |
| <span id="stage-3"></span>3 | 3=Dark shield active<br><span class="qnote">🔒 An area on [Galmore 45](../maps/galmore_45.md) becomes blocked off.</span><br><span class="qnote">🗺️ Part of [Galmore 45](../maps/galmore_45.md) visibly changes.</span> | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | sets stage 40 of [Shadows](../quests/shadows.md#stage-40)<br>spawns monsters on galmore_45<br>sets stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50) |
| <span id="stage-4"></span>4 | 4=Miri spawned 3 | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-5"></span>5 | 5=Dark priest killed | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-6"></span>6 | 6=Andor spawned at Rosmara/Alynndir | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | sets stage 260 of [Shadows](../quests/shadows.md#stage-260)<br>removes monsters from galmore_41<br>spawns monsters on road5<br>spawns monsters on road5_house<br>sets stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280)<br>spawns monsters on houseatcrossroads0<br>spawns monsters on wayto_feygard_duleian_2 |
| <span id="stage-11"></span>11 | 11=Borvis spawned near Alynndir's hut<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Cabin norcity road1](../maps/cabin_norcity_road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road4](../maps/road4.md).</span> | stepping on a trigger on [cabin_norcity_road1](../maps/cabin_norcity_road1.md) | – | spawns monsters on road5 |
| <span id="stage-20"></span>20 | 20=Told Mikhail about meeting Andor in Miri's or Borvis' quest | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [crossroads](../maps/crossroads.md) → the conversation leads here automatically — **conditions:** NOT reached stage 1 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-1) → **stage 1**; also spawns monsters on houseatcrossroads0

???+ note "Stage 2: 1 route"

    1. stepping on a trigger on [crossroads](../maps/crossroads.md) → the conversation leads here automatically — **conditions:** NOT reached stage 2 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-2); reached stage 150 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-150); 5 rounds passed since timer “dds_miri” → **stage 2**; also spawns monsters on houseatcrossroads0

???+ note "Stage 3: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Shadows](../quests/shadows.md#stage-40) → **stage 3**; also sets stage 40 of [Shadows](../quests/shadows.md#stage-40), spawns monsters on galmore_45, spawns monsters on galmore_45. NPC: “Journey to the south of Stoutford, into the forests there. See what that Shadow priest is doing there, and stop him…”
    2. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50) → **stage 3**; also sets stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50), spawns monsters on galmore_45, spawns monsters on galmore_45. NPC: “Journey to the south of Stoutford, into the weird lands there. Investigate what's going on in the Purple Hills.”

???+ note "Stage 6: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Really? Tell me!” — **conditions:** reached stage 240 of [Shadows](../quests/shadows.md#stage-240); killed 1× [Dark priest](../monsters/dds_dark_priest_monster.md) → **stage 6**; also sets stage 260 of [Shadows](../quests/shadows.md#stage-260), removes monsters from galmore_41, spawns monsters on road5, spawns monsters on road5_house. NPC: “Andor is going to visit Alynndir to refill his travel supplies.”
    2. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Really? Tell me!” — **conditions:** reached stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260); killed 1× [Dark priest](../monsters/dds_dark_priest_monster.md) → **stage 6**; also sets stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280), removes monsters from galmore_41, spawns monsters on houseatcrossroads0, spawns monsters on wayto_feygard_duleian_2. NPC: “Andor is going to visit Rosmara to refill his travel supplies.”

???+ note "Stage 11: 1 route"

    1. stepping on a trigger on [cabin_norcity_road1](../maps/cabin_norcity_road1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 11 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-11) → **stage 11**; also spawns monsters on road5

???+ note "Stage 20: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “He just said that he couldn't come now. Then he ran away before I could ask him what he was up to.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 310 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-310); NOT reached stage 20 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-20) → **stage 20**. NPC: “Mikhail! Don't you dare talk to our child like that!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dds_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `dds_nd` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 11, 20 |
    | Dialogue nodes setting stages | 1: `dds_miri_spawn_10`, 2: `dds_miri_spawn_20`, 3: `dds_borvis_100`, 3: `dds_miri_110`, 6: `dds_borvis_590`, 6: `dds_miri_590`, 11: `dds_borvis_spawn_10`, 20: `mikhail_news_64` |
    | Dialogue nodes clearing stages | 3: `dds_dark_shadow_52`, 3: `dds_dark_shadow_152` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
