# A path to the Duleian Road

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `pathway_fallhaven` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 60) |
| **Started by** | [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) |
| **NPCs involved** | [Guard captain](../monsters/warden.md), [Jakrar](../monsters/jakrar.md), [Watchman](../monsters/guard_pathway.md) |
| **Locations** | [fallhaven_ne](../maps/fallhaven_ne.md), [fallhaven_prison](../maps/fallhaven_prison.md), [fallhaven_sw](../maps/fallhaven_sw.md) |
| **Total XP** | 1,000 |
| **Related quests** | 2 |

</div>

## Overview

> I talked to a guard in the east of Fallhaven. He watches over the old passage to the Duleian Road, which is now blocked by fallen trees. If I want to help opening the path I should talk to his superior, the guard captain in the Fallhaven prison.

## Prerequisites to start

None: talk to [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Night visit](farrik.md#stage-60) | stage 60 reached, for stage 20 here |
| Unlocks | [It makes no fence](tunlon_fence.md#stage-20) | stage 20 there needs stage 50 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I talked to a guard in the east of Fallhaven. He watches over the old passage to the Duleian Road, which is now blocked by fallen trees. If I want to help opening the path I should talk to his superior, the guard captain in the Fallhaven prison. | [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) | – | – |
| <span id="stage-20"></span>20 | I talked to the guard captain. I wasn't able to convince him, but he advised me to talk to the woodcutter Jakrar, who lives just south of Fallhaven's prison. | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | I talked to Jakrar the woodcutter. He will only clear the trees away if I do him a favor. I should search for his favorite axe east of the Crossroads Guardhouse, located to the north of Fallhaven. I should keep my eyes open for an evil wolf pack.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Roadbeforecrossroads](../maps/roadbeforecrossroads.md).</span> | [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 20 | – |
| <span id="stage-35"></span>35 | <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadbeforecrossroads](../maps/roadbeforecrossroads.md).</span> | stepping on a trigger on [roadbeforecrossroads](../maps/roadbeforecrossroads.md) | – | – |
| <span id="stage-40"></span>40 | I showed Jakrar the axe I found and he recognized it immediately. | [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | hand over 1× [Jakrar's woodcutting axe](../items/jakrar_axe.md), stage 30 | – |
| <span id="stage-50"></span>50 | Jakrar was very happy to see his good old axe again. He expressed his gratitude, and started to clear away the trees immediately. | [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | Now the woodcutter has cleared away all the trees that blocked the path. Finally, the townsfolk have got back their shortcut to the Duleian Road! **(completes quest)** | [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) | stage 50 | 700 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) → choose “You're right, but I'd really love to be able to take this path.” → **stage 10**. NPC: “OK, maybe you can be of use. Talk to the guard captain. Maybe you can convince him to pay the woodcutter first. But I…”

???+ note "Stage 20: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “So where can I find him?” — **conditions:** reached stage 60 of [Night visit](../quests/farrik.md#stage-60); latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10) is 10 → **stage 20**. NPC: “He lives in his hut, immediately south of my prison. Don't you bother me again!”

???+ note "Stage 30: 1 route"

    1. Talk to [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “So I guess you want me to retrieve your axe?” — **conditions:** latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-20) is 20 → **stage 30**. NPC: “Yes exactly. If you would do me that favor I will gladly cut away the trees and receive payment afterwards. Just head…”

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [roadbeforecrossroads](../maps/roadbeforecrossroads.md) → the conversation leads here automatically — **conditions:** killed 1× [Korvan the leader of the wolves](../monsters/wolf_leader.md); NOT reached stage 35 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-35) → **stage 35**. NPC: “You have found Jakrar's axe next to the body of the beast.”

???+ note "Stage 40: 1 route"

    1. Talk to [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Hello again! I've finally found your axe!” — **conditions:** reached stage 30 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-30); hand over 1× [Jakrar's woodcutting axe](../items/jakrar_axe.md) → **stage 40**. NPC: “Let me see... Oh yes! This is my axe! I cannot thank you enough!”

???+ note "Stage 50: 1 route"

    1. Talk to [Jakrar](../monsters/jakrar.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “So will you cut away those trees that block the old pathway?” — **conditions:** reached stage 40 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-40); NOT reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50) → **stage 50**. NPC: “Sure! Already on my way! The work will be finished soon.”

???+ note "Stage 60: 1 route"

    1. Talk to [Watchman](../monsters/guard_pathway.md) ([fallhaven_ne](../maps/fallhaven_ne.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50) → **stage 60**. NPC: “Hello again. It seems like you have sorted things out. Now the passage isn't blocked anymore. You have my gratitude…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.7.15](../versions/0.7.15.md) | stage 10 journal text changed; stage 20 journal text changed<br>Dialogue: 2 lines changed<br>· text: “OK, maybe you can be of use. Talk to the warden. Maybe you can convin…” → “OK, maybe you can be of use. Talk to the guard captainn. Maybe you ca…” |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 1 line changed<br>· text: “OK, maybe you can be of use. Talk to the guard captainn. Maybe you ca…” → “OK, maybe you can be of use. Talk to the guard captain. Maybe you can…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=pathway_fallhaven.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=pathway_fallhaven.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=pathway_fallhaven.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=pathway_fallhaven.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=pathway_fallhaven.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `pathway_fallhaven` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `guard_pathway_4`, 20: `fallhaven_warden_pathway_3`, 30: `fallhaven_lumberjack_8`, 35: `sign_wolf_pack_jakrar_1`, 40: `fallhaven_lumberjack_10`, 50: `fallhaven_lumberjack_11`, 60: `guard_pathway_5` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
