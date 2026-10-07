---
description: "Quick glance: statue found is a hidden quest in Andor's Trail, started by walking into a blocked passage on basiliskcave2. 6 stages. Found Statue"
---

# Quick glance: statue found

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance_hidden_found_statue` |
| **In journal** | No (hidden flag) |
| **Stages** | 6 |
| **Started by** | walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md) |
| **NPCs involved** | [Fangwurm](../monsters/fangwurm.md) |
| **Locations** | [Brimhaven church](../maps/brimhaven_church.md) |
| **Related quests** | 1 |

</div>

## Overview

> Found Statue

## Prerequisites to start

None: talk to walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md) to begin.


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

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | Found Statue | walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md) | – |
| <span id="stage-20"></span>[20](#route-20) | Removed Statue<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave 2](../maps/basiliskcave2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Basiliskcave 2](../maps/basiliskcave2.md).</span><br><span class="qnote">🗺️ Part of [Basiliskcave 2](../maps/basiliskcave2.md) visibly changes.</span> | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) | sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85), spawns monsters on brimhaven_anakis_house |
| <span id="stage-30"></span>[30](#route-30) | Decided what to do with the Basilisks blood<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave 2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) | varies by route (see below) |
| <span id="stage-40"></span>40 | Killed Basilisk and left the room | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-50"></span>[50](#route-50) | Told Fangwurm about keeping the blood for myself | [Fangwurm](../monsters/fangwurm.md) | – |
| <span id="stage-60"></span>[60](#route-60) | Told Fangwurm about killling the Basilisk | [Fangwurm](../monsters/fangwurm.md) | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · walking into a blocked passage on basiliskcave2 · 1 way"

    **Way 1:** Walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md)

    - *“This stone statue looks almost like a real woman.”*


<span id="route-20"></span>

??? note "Stage 20 · stepping on a trigger on basiliskcave2 · 1 way"

    **Way 1:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md), choose “I use the crystal vial and pour the blood over the stone statue.”

    - **Needs:** not yet stage 30; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md)
    - **Gives:** sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85), spawns monsters on brimhaven_anakis_house
    - *“Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she thanks you and tells you…”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on basiliskcave2 · 2 ways"

    **Way 1:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md), choose “I use the crystal vial and pour the blood over the stone statue.”

    - **Needs:** not yet stage 30; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md)
    - **Gives:** sets stage 85 of [A quick glance](../quests/quick_glance.md#stage-85), spawns monsters on brimhaven_anakis_house
    - *“Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she thanks you and tells you…”*

    **Way 2:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md), choose “I keep the blood for myself using the empty crystal vial.”

    - **Needs:** not yet stage 30; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); hand over 1× [Empty crystal vial](../items/empty_crystal_vial.md)
    - **Gives:** 1× [Basilisk blood](../items/basilisk_blood.md)


<span id="route-50"></span>

??? note "Stage 50 · Fangwurm · 1 way"

    **Way 1:** Talk to [Fangwurm](../monsters/fangwurm.md), automatic

    - **Needs:** stage 50
    - *“I am sad that you took the blood for yourself instead of trying to help Anakis' sister. Please leave now.”*


<span id="route-60"></span>

??? note "Stage 60 · Fangwurm · 1 way"

    **Way 1:** Talk to [Fangwurm](../monsters/fangwurm.md), automatic

    - **Needs:** stage 60
    - *“Thank you for killing the Basilisk, but it would be better if you had talked to me before killing it, because its magical blood is now…”*



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
    | Name in game data | `quick_glance_hidden_found_statue` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `sister_statue`, 20: `basiliskcave2_decided_to_heal`, 30: `basiliskcave2_decided_to_heal`, 30: `basiliskcave2_keep_blood`, 50: `fangwurm_angry`, 60: `fangwurm_thank_killing_basilisk` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
