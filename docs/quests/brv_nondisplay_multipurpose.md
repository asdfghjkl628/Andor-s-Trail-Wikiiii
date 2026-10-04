# brv_nondisplay_multipurpose

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_nondisplay_multipurpose` |
| **In journal** | No (hidden flag) |
| **Stages** | 7 |
| **Started by** | [Worker](../monsters/brv_laundry_worker.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)), [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Ito](../monsters/brv_guard_deputy.md), [Mikhail](../monsters/mikhail.md), [Venanra](../monsters/brv_laundry_boss.md), [Worker](../monsters/brv_laundry_worker.md) |
| **Locations** | [brimhaven2](../maps/brimhaven2.md), [brimhaven2_laundry](../maps/brimhaven2_laundry.md), [brimhaven_general1](../maps/brimhaven_general1.md), [home](../maps/home.md) |
| **Related quests** | 4 |

</div>

## Overview

> Knows about laundry offering upgrades

## Prerequisites to start

**Route 1** ([Worker](../monsters/brv_laundry_worker.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md))):

- nothing

**Route 2** ([Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md))):

- NOT reached stage 10 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Search for Andor](andor.md#stage-30) | stage 30 reached, for stage 40 here |
| Requires | [Search for Andor](andor.md#stage-55) | stage 55 reached, for stage 40 here |
| Requires | [Search for Andor](andor.md#stage-80) | stage 80 reached, for stage 40 here |
| Requires | [A strange looking dagger](brv_dagger.md#stage-110) | stage 110 reached, for stage 50 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stage 40 here |
| Blocked by | [Search for Andor](andor.md#stage-30) | stage 30 must NOT be reached, for stage 40 here |
| Blocked by | [Search for Andor](andor.md#stage-55) | stage 55 must NOT be reached, for stage 40 here |
| Mutually exclusive | [A strange looking dagger](brv_dagger.md#stage-115) | stage 115 must NOT be reached, for stage 50 here |
| Mutually exclusive | [A strange looking dagger](brv_dagger.md#stage-120) | stage 120 must NOT be reached, for stage 50 here |
| Mutually exclusive | [A strange looking dagger](brv_dagger.md#stage-200) | stage 200 must NOT be reached, for stage 50 here |
| Mutually exclusive | [A strange looking dagger](brv_dagger.md#stage-220) | stage 220 must NOT be reached, for stage 60 here |
| Mutually exclusive | [A strange looking dagger](brv_dagger.md#stage-230) | stage 230 must NOT be reached, for stage 50 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-120) | stage 120 there needs stage 50 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-130) | stage 130 there needs stage 50 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-220) | stage 220 there needs stage 60 here |
| Unlocks | [Honor your parents](brv_present.md#stage-40) | stage 40 there needs stage 40 here |
| Unlocks | [Honor your parents](brv_present.md#stage-50) | stage 50 there needs stage 40 here |
| Unlocks | [Honor your parents](brv_present.md#stage-60) | stage 60 there needs stage 40 here |
| Blocks | [Honor your parents](brv_present.md#stage-30) | reaching stage 40 here closes stage 30 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Knows about laundry offering upgrades | [Worker](../monsters/brv_laundry_worker.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md))<br>[Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) | – | – |
| <span id="stage-15"></span>15 | Knows about dresses | [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) | – | – |
| <span id="stage-20"></span>20 | brother2_door_opened<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven3](../maps/brimhaven3.md).</span><br><span class="qnote">🗺️ Part of [Brimhaven3](../maps/brimhaven3.md) visibly changes.</span> | walking into a blocked passage on [brimhaven3](../maps/brimhaven3.md) | carry 1× [Key (found in run-down house East Brimhaven)](../items/brv_key_brother2.md) | – |
| <span id="stage-30"></span>30 | never true<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven brother1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-40"></span>40 | told father about andor | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | – | – |
| <span id="stage-50"></span>50 | Arlish took the dagger | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | hand over 1× [Assassin's blade](../items/dagger_assassin.md) | – |
| <span id="stage-60"></span>60 | Gave Ito the glove | [Ito](../monsters/brv_guard_deputy.md) ([brimhaven2](../maps/brimhaven2.md)) | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 2 routes"

    1. Talk to [Worker](../monsters/brv_laundry_worker.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) → choose “What are you working on?” → **stage 10**. NPC: “Currently I am coloring some cloth, but we do everything related to cloth, like repairing, custom tailoring, or…”
    2. Talk to [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) → choose “Can you sell me something?” — **conditions:** NOT reached stage 10 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10) → **stage 10**. NPC: “We are working on some nice green dresses. We can also repair and improve your clothes.”

???+ note "Stage 15: 1 route"

    1. Talk to [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) → choose “Can you sell me something?” — **conditions:** NOT reached stage 10 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10) → **stage 15**. NPC: “We are working on some nice green dresses. We can also repair and improve your clothes.”

???+ note "Stage 20: 1 route"

    1. walking into a blocked passage on [brimhaven3](../maps/brimhaven3.md) → choose “I try to use the key that I found in the house nearby to open the door.” — **conditions:** carry 1× [Key (found in run-down house East Brimhaven)](../items/brv_key_brother2.md) → **stage 20**. NPC: “The key opens the door.”

???+ note "Stage 40: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “I met a man called Lodar and he told me that Andor probably went to Nor City.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); NOT reached stage 30 of [Search for Andor](../quests/andor.md#stage-30); NOT reached stage 55 of [Search for Andor](../quests/andor.md#stage-55); reached stage 80 of [Search for Andor](../quests/andor.md#stage-80) → **stage 40**. NPC: “Did you go to Nor City?”
    2. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Someone in Fallhaven told me that he met Andor and that he was searching for a man called Lodar.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); NOT reached stage 30 of [Search for Andor](../quests/andor.md#stage-30); reached stage 55 of [Search for Andor](../quests/andor.md#stage-55) → **stage 40**. NPC: “Did you find this Lodar?”
    3. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “I asked around in Crossglen and they sent me to Fallhaven.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 30 of [Search for Andor](../quests/andor.md#stage-30) → **stage 40**. NPC: “Did you go the dangerous way to Fallhaven?”

???+ note "Stage 50: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “Well, I have it right here.” — **conditions:** reached stage 110 of [A strange looking dagger](../quests/brv_dagger.md#stage-110); NOT reached stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115); NOT reached stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230); hand over 1× [Assassin's blade](../items/dagger_assassin.md) → **stage 50**. NPC: “Arlish takes the dagger and examines it while you continue to talk.”

???+ note "Stage 60: 1 route"

    1. Talk to [Ito](../monsters/brv_guard_deputy.md) ([brimhaven2](../maps/brimhaven2.md)) → choose “I want to discuss Ogea again.” — **conditions:** reached stage 60 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-60); NOT reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220) → **stage 60**. NPC: “Wow. You did a great job! Do you want a job on our team?”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |
| [v0.7.12](../versions/0.7.12.md) | stages added: 15, 50, 60<br>Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay_multipurpose.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay_multipurpose.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay_multipurpose.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay_multipurpose.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay_multipurpose.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_nondisplay_multipurpose` |
    | showInLog | 0 |
    | Stage IDs | 10, 15, 20, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `brv_laundry_worker_2`, 10: `brv_laundry_boss_1`, 15: `brv_laundry_boss_1`, 20: `brv_brother2_door2`, 40: `mikhail_news_40`, 40: `mikhail_news_30`, 40: `mikhail_news_20`, 50: `arlish_asd_20`, 60: `brv_guard_deputy_asd_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
