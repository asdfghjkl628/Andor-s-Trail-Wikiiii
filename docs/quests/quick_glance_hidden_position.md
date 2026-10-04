# quick_glance_hidden_position

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance_hidden_position` |
| **In journal** | No (hidden flag) |
| **Stages** | 2 |
| **Started by** | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md), stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) |
| **Related quests** | 1 |

</div>

## Overview

> Anakis left

## Prerequisites to start

**Route 1** (stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md)):

- NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
- NOT wearing [Hand mirror](../items/hand_mirror.md)
- NOT affected by turn_to_stone
- NOT reached stage 15 of [A quick glance](../quests/quick_glance.md#stage-15)
- NOT reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20)

**Route 2** (stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md)):

- NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
- NOT wearing [Hand mirror](../items/hand_mirror.md)
- NOT affected by turn_to_stone

**Route 3** (stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md)):

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

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-100"></span>100 | Anakis left | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-110"></span>110 | Basilisk blocked<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave2](../maps/basiliskcave2.md).</span><br><span class="qnote">🔒 An area on [Basiliskcave2](../maps/basiliskcave2.md) becomes blocked off.</span> | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) | – | applies condition turn_to_stone |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 110: 3 routes"

    1. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically — **conditions:** NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT wearing [Hand mirror](../items/hand_mirror.md); NOT affected by turn_to_stone; NOT reached stage 15 of [A quick glance](../quests/quick_glance.md#stage-15); NOT reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20) → **stage 110**; also applies condition turn_to_stone. NPC: “You see an old Basilisk at the end of the room that glances at you. With a feeling of deadly danger your movements get…”
    2. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically — **conditions:** NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT wearing [Hand mirror](../items/hand_mirror.md); NOT affected by turn_to_stone → **stage 110**; also applies condition turn_to_stone. NPC: “You see an old Basilisk at the end of the room that glances at you. With a feeling of deadly danger your movements get…”
    3. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20); NOT reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50) → **stage 110**


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance_hidden_position.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `quick_glance_hidden_position` |
    | showInLog | 0 |
    | Stage IDs | 100, 110 |
    | Dialogue nodes setting stages | 110: `basiliskcave2_warn`, 110: `basiliskcave2_warn_hint`, 110: `basiliskcave2_check_turntostone_20` |
    | Dialogue nodes clearing stages | 110: `basiliskcave2_remove_turntostone` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
