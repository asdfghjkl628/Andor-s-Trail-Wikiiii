---
description: "quick_glance_hidden_found_statue is a hidden quest in Andor's Trail, started by walking into a blocked passage on basiliskcave2. 6 stages. Found Statue"
---

# quick_glance_hidden_found_statue

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance_hidden_found_statue` |
| **In journal** | No (hidden flag) |
| **Stages** | 6 |
| **Started by** | walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) |
| **NPCs involved** | [Fangwurm](../monsters/fangwurm.md) |
| **Locations** | [brimhaven_church](../maps/brimhaven_church.md) |
| **Related quests** | 1 |

</div>

## Overview

> Found Statue

## Prerequisites to start

None: talk to walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A quick glance](quick_glance.md#stage-60) | stage 60 reached, for stages 20, 30 here |
| Unlocks | [A quick glance](quick_glance.md#stage-40) | stage 40 there needs stage 10 here |
| Unlocks | [A quick glance](quick_glance.md#stage-50) | stage 50 there needs stage 10 here |
| Unlocks | [A quick glance](quick_glance.md#stage-90) | stage 90 there needs stage 30 here |
| Blocks | [A quick glance](quick_glance.md#stage-20) | reaching stage 10 here closes stage 20 there |
| Blocks | [A quick glance](quick_glance.md#stage-80) | reaching stage 30 here closes stage 80 there |
| Blocks | [A quick glance](quick_glance.md#stage-85) | reaching stage 30 here closes stage 85 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Found Statue | walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) | – | – |
| <span id="stage-20"></span>20 | Removed Statue<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave2](../maps/basiliskcave2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Basiliskcave2](../maps/basiliskcave2.md).</span><br><span class="qnote">🗺️ Part of [Basiliskcave2](../maps/basiliskcave2.md) visibly changes.</span> | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) | carry 1× [Empty crystal vial](../items/empty_crystal_vial.md) | sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85)<br>spawns monsters on brimhaven_anakis_house |
| <span id="stage-30"></span>30 | Decided what to do with the Basilisks blood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) | carry 1× [Empty crystal vial](../items/empty_crystal_vial.md), hand over 1× [Empty crystal vial](../items/empty_crystal_vial.md) | sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85)<br>spawns monsters on brimhaven_anakis_house<br>gives 1× [Basilisk blood](../items/basilisk_blood.md) |
| <span id="stage-40"></span>40 | Killed Basilisk and left the room | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-50"></span>50 | Told Fangwurm about keeping the blood for myself | [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) | – | – |
| <span id="stage-60"></span>60 | Told Fangwurm about killling the Basilisk | [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) | – | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically → **stage 10**. NPC: “This stone statue looks almost like a real woman.”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → choose “I use the crystal vial and pour the blood over the stone statue.” — **conditions:** killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md) → **stage 20**; also sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85), spawns monsters on brimhaven_anakis_house. NPC: “Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she…”

???+ note "Stage 30: 2 routes"

    1. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → choose “I use the crystal vial and pour the blood over the stone statue.” — **conditions:** killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md) → **stage 30**; also sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85), spawns monsters on brimhaven_anakis_house. NPC: “Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she…”
    2. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → choose “I keep the blood for myself using the empty crystal vial.” — **conditions:** killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); hand over 1× [Empty crystal vial](../items/empty_crystal_vial.md) → **stage 30**; also gives 1× [Basilisk blood](../items/basilisk_blood.md)

???+ note "Stage 50: 1 route"

    1. Talk to [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-50) → **stage 50**. NPC: “I am sad that you took the blood for yourself instead of trying to help Anakis' sister. Please leave now.”

???+ note "Stage 60: 1 route"

    1. Talk to [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-60) → **stage 60**. NPC: “Thank you for killing the Basilisk, but it would be better if you had talked to me before killing it, because its…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_found_statue.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_found_statue.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_found_statue.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_found_statue.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_found_statue.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `quick_glance_hidden_found_statue` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `sister_statue`, 20: `basiliskcave2_decided_to_heal`, 30: `basiliskcave2_decided_to_heal`, 30: `basiliskcave2_keep_blood`, 50: `fangwurm_angry`, 60: `fangwurm_thank_killing_basilisk` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
