# bwmfill_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bwmfill_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 5 |
| **Started by** | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md), stepping on a trigger on [crossroads](../maps/crossroads.md) |
| **NPCs involved** | [Tunlon](../monsters/tunlon.md) |
| **Locations** | [bwmfill3](../maps/bwmfill3.md) |
| **Related quests** | 3 |

</div>

## Overview

> Guard Burhczyd active

## Prerequisites to start

Start with stepping on a trigger on [brimhaven4](../maps/brimhaven4.md). Required:

- NOT reached stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41)
- reached stage 80 of [Young merchant](../quests/quest_burhczyd.md#stage-80)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Young merchant](quest_burhczyd.md#stage-80) | stage 80 reached, for stages 40, 41 here |
| Blocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-142) | reaching stage 41 here closes stage 142 there |
| Blocks | [It makes no fence](tunlon_fence.md#stage-12) | reaching stage 44 here closes stage 12 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-40"></span>40 | Guard Burhczyd active<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | – | sets stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142) |
| <span id="stage-41"></span>41 | Guard Burhczyd used<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | – | sets stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142) |
| <span id="stage-42"></span>42 | BMP box<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | carry 1× [Andor's bonemeal box](../items/guynmart_bonemealbox.md), carry 1× [Bonemeal potion](../items/bonemeal_potion.md) | – |
| <span id="stage-43"></span>43 | BMP box with normal BMP<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven4](../maps/brimhaven4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossroads](../maps/crossroads.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fields6](../maps/fields6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road1](../maps/road1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads2](../maps/roadbeforecrossroads2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads6](../maps/roadbeforecrossroads6.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6](../maps/wild6.md).</span> | stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) | carry 1× [Andor's bonemeal box](../items/guynmart_bonemealbox.md), carry 1× [Bonemeal potion](../items/bonemeal_potion.md) | – |
| <span id="stage-44"></span>44 | Killed Tunlon's sheep detected<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Bwmfill3](../maps/bwmfill3.md).</span> | stepping on a trigger on [bwmfill3](../maps/bwmfill3.md)<br>[Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) | – | removes monsters from bwmfill3<br>spawns monsters on bwmfill3 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41); reached stage 80 of [Young merchant](../quests/quest_burhczyd.md#stage-80) → **stage 40**; also sets stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142)

???+ note "Stage 41: 1 route"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 41 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-41); reached stage 80 of [Young merchant](../quests/quest_burhczyd.md#stage-80) → **stage 41**; also sets stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142)

???+ note "Stage 42: 2 routes"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** carry 1× [Bonemeal potion](../items/bonemeal_potion.md); carry 1× [Andor's bonemeal box](../items/guynmart_bonemealbox.md) → **stage 42**
    2. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** carry 1× [Andor's bonemeal box](../items/guynmart_bonemealbox.md) → **stage 42**

???+ note "Stage 43: 1 route"

    1. stepping on a trigger on [brimhaven4](../maps/brimhaven4.md) → the conversation leads here automatically — **conditions:** carry 1× [Bonemeal potion](../items/bonemeal_potion.md); carry 1× [Andor's bonemeal box](../items/guynmart_bonemealbox.md) → **stage 43**

???+ note "Stage 44: 2 routes"

    1. stepping on a trigger on [bwmfill3](../maps/bwmfill3.md) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); NOT reached stage 44 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44) → **stage 44**; also removes monsters from bwmfill3, spawns monsters on bwmfill3. NPC: “You filthy MURDERER!!”
    2. Talk to [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) → the conversation leads here automatically — **conditions:** killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); NOT reached stage 44 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-44) → **stage 44**; also removes monsters from bwmfill3, spawns monsters on bwmfill3. NPC: “You filthy MURDERER!!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line added |
| [v0.8.10](../versions/0.8.10.md) | Added<br>Dialogue: 4 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwmfill_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwmfill_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwmfill_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwmfill_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwmfill_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bwmfill_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 40, 41, 42, 43, 44 |
    | Dialogue nodes setting stages | 40: `brv_patrol_stop_hero_bur`, 41: `brv_patrol_stop_hero_bur`, 42: `brv_patrol_stop_hero_box1`, 42: `brv_patrol_stop_hero_box2`, 43: `brv_patrol_stop_hero_box1`, 44: `bwmfill_killsheep_20` |
    | Dialogue nodes clearing stages | 40: `brv_patrol_check_stop_hero`, 42: `brv_patrol_check_stop_hero`, 43: `brv_patrol_check_stop_hero` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
