---
description: "Quick glance: position is a hidden quest in Andor's Trail, started by stepping on a trigger on basiliskcave2. 2 stages. Anakis left"
---

# Quick glance: position

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance_hidden_position` |
| **In journal** | No (hidden flag) |
| **Stages** | 2 |
| **Started by** | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md), stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) |
| **Related quests** | 1 |

</div>

## Overview

> Anakis left

## Prerequisites to start

**Route 1** (stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)):

- NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
- NOT wearing [Hand mirror](../items/hand_mirror.md)
- NOT affected by turn_to_stone
- NOT reached stage 15 of [A quick glance](../quests/quick_glance.md#stage-15)
- NOT reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20)

**Route 2** (stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)):

- NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
- NOT wearing [Hand mirror](../items/hand_mirror.md)
- NOT affected by turn_to_stone

**Route 3** (stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)):

- reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20)
- NOT reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A quick glance](quick_glance.md#stage-20) | stage 20 reached, for stage 110 here |
| Blocked by | [A quick glance](quick_glance.md#stage-15) | stage 15 must NOT be reached, for stage 110 here |
| Blocked by | [A quick glance](quick_glance.md#stage-20) | stage 20 must NOT be reached, for stage 110 here |
| Blocked by | [A quick glance](quick_glance.md#stage-50) | stage 50 must NOT be reached, for stage 110 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-100"></span>100 | Anakis left | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-110"></span>[110](#route-110) | Basilisk blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave 2](../maps/basiliskcave2.md).</span><br><span class="qnote">🔒 An area on [Basiliskcave 2](../maps/basiliskcave2.md) becomes blocked off.</span> | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) | varies by route (see below) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-110"></span>

??? note "Stage 110 · stepping on a trigger on basiliskcave2 · 3 ways"

    **Way 1:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)

    - **Needs:** not killed 1× [Ancient basilisk](../monsters/old_basilisk.md); not wearing [Hand mirror](../items/hand_mirror.md); not affected by turn_to_stone; not reached stage 15 of [A quick glance](../quests/quick_glance.md#stage-15); not reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20)
    - **Gives:** applies condition turn_to_stone
    - *“You see an old Basilisk at the end of the room that glances at you. With a feeling of deadly danger your movements get slower the nearer…”*

    **Way 2:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)

    - **Needs:** not killed 1× [Ancient basilisk](../monsters/old_basilisk.md); not wearing [Hand mirror](../items/hand_mirror.md); not affected by turn_to_stone
    - **Gives:** applies condition turn_to_stone
    - *“You see an old Basilisk at the end of the room that glances at you. With a feeling of deadly danger your movements get slower the nearer…”*

    **Way 3:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)

    - **Needs:** reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20); not reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50)



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `quick_glance_hidden_position` |
    | Name in game data | `quick_glance_hidden_position` |
    | showInLog | 0 |
    | Stage IDs | 100, 110 |
    | Dialogue nodes setting stages | 110: `basiliskcave2_warn`, 110: `basiliskcave2_warn_hint`, 110: `basiliskcave2_check_turntostone_20` |
    | Dialogue nodes clearing stages | 110: `basiliskcave2_remove_turntostone` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
