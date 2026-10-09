---
description: "Brimhaven dagger story flags is a hidden quest in Andor's Trail, started by stepping on a trigger on brimhaven_inn_east. 4 stages. Purchased gem"
---

# Brimhaven dagger story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_dagger_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 4 |
| **Started by** | stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md), stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) |
| **NPCs involved** | [Pixtumn](../monsters/quiet_thief.md) |
| **Locations** | [Brimhaven inn east](../maps/brimhaven_inn_east.md) |
| **Related quests** | 1 |

</div>

## Overview

> Purchased gem

## Prerequisites to start

**Route 1** (stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)):

- carry 1× [A strange-looking gem](../items/strange_gem.md)

**Route 2** (stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)):

- carry 1× [A strange looking dagger](../items/strange_dagger.md)
- carry 1× [A strange-looking gem](../items/strange_gem.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A strange looking dagger](brv_dagger.md#stage-30) | stage 30 reached, for stage 30 here |
| Requires | [A strange looking dagger](brv_dagger.md#stage-40) | stage 40 reached, for stage 40 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [A strange looking dagger](brv_dagger.md#stage-40) | stage 40 there needs stage 20 here |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-30) | reaching stages 20, 30 here closes stage 30 there |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-40) | reaching stages 10, 40 here closes stage 40 there |
| Blocks | [A strange looking dagger](brv_dagger.md#stage-90) | reaching stages 30, 40 here closes stage 90 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | Purchased gem<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – |
| <span id="stage-20"></span>[20](#route-20) | Purchased knife<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – |
| <span id="stage-30"></span>[30](#route-30) | purchased knife the hard way. | [Pixtumn](../monsters/quiet_thief.md) | 1× [A strange looking dagger](../items/strange_dagger.md) |
| <span id="stage-40"></span>[40](#route-40) | purchased gem the hard way. | [Pixtumn](../monsters/quiet_thief.md) | 1× [A strange-looking gem](../items/strange_gem.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on brimhaven_inn_east · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)

    - **Needs:** carry 1× [A strange-looking gem](../items/strange_gem.md)

    **Way 2:** Stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)

    - **Needs:** carry 1× [A strange looking dagger](../items/strange_dagger.md); carry 1× [A strange-looking gem](../items/strange_gem.md)


<span id="route-20"></span>

??? note "Stage 20 · stepping on a trigger on brimhaven_inn_east · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)

    - **Needs:** carry 1× [A strange looking dagger](../items/strange_dagger.md)

    **Way 2:** Stepping on a trigger on [Brimhaven inn east](../maps/brimhaven_inn_east.md)

    - **Needs:** carry 1× [A strange-looking gem](../items/strange_gem.md); carry 1× [A strange looking dagger](../items/strange_dagger.md)


<span id="route-30"></span>

??? note "Stage 30 · Pixtumn · 1 way"

    **Way 1:** Talk to [Pixtumn](../monsters/quiet_thief.md), choose “I don't think it's fair, but I'll pay it.”

    - **Needs:** stage 10; not yet stage 20, 30; reached stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30); pay 1,000 gold
    - **Gives:** 1× [A strange looking dagger](../items/strange_dagger.md)
    - *“Here you go kid.”*


<span id="route-40"></span>

??? note "Stage 40 · Pixtumn · 1 way"

    **Way 1:** Talk to [Pixtumn](../monsters/quiet_thief.md), choose “I don't think it's fair, but I'll pay it.”

    - **Needs:** stage 20; not yet stage 10, 40; reached stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40); pay 1,500 gold
    - **Gives:** 1× [A strange-looking gem](../items/strange_gem.md)
    - *“Here you go kid”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_dagger_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_dagger_nondisplay` |
    | Name in game data | `brv_dagger_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40 |
    | Dialogue nodes setting stages | 10: `brv_thief_1`, 10: `brv_thief_2a`, 20: `brv_thief_2`, 20: `brv_thief_1a`, 30: `quiet_thief_2_4`, 40: `quiet_thief_3_4` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
