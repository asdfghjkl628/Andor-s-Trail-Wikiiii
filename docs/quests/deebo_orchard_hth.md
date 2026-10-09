---
description: "Hunting the hunter is a quest in Andor's Trail, started by Deebo (sullengard_apple_farm_east). 4 stages, 10,000 XP in total. Deebo, the apple orchard farmer northeast of Sullengard informed me of a Golden jackal that is wreaking havoc in his orchard."
---

# Hunting the hunter

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `deebo_orchard_hth` |
| **In journal** | Yes |
| **Stages** | 4 (completes at 50) |
| **Started by** | [Deebo](../monsters/deebo_orchard_deebo.md) ([Sullengard apple farm east](../maps/sullengard_apple_farm_east.md)) |
| **NPCs involved** | [Deebo](../monsters/deebo_orchard_deebo.md) |
| **Locations** | [Sullengard apple farm east](../maps/sullengard_apple_farm_east.md) |
| **Total XP** | 10,000 |
| **Related quests** | 1 |

</div>

## Overview

> Deebo, the apple orchard farmer northeast of Sullengard informed me of a Golden jackal that is wreaking havoc in his orchard.

## Prerequisites to start

Start with [Deebo](../monsters/deebo_orchard_deebo.md) ([Sullengard apple farm east](../maps/sullengard_apple_farm_east.md)). Required:

- NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50)
- latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Mutually exclusive | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-4) | stage 4 must NOT be reached, for stage 10 here |
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-4) | stage 4 there needs stage 0 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-0"></span>[0](#route-0) | <details class="jt"><summary><span class="s">Deebo, the apple orchard farmer northeast of Sullengard informed me… ▸</span><span class="l">▴ less</span></summary>Deebo, the apple orchard farmer northeast of Sullengard informed me of a Golden jackal that is wreaking havoc in his orchard.</details> | [Deebo](../monsters/deebo_orchard_deebo.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I accepted the challenge of tracking down the Golden jackal and… ▸</span><span class="l">▴ less</span></summary>I accepted the challenge of tracking down the Golden jackal and bringing back proof to Deebo that I have killed it.</details> | [Deebo](../monsters/deebo_orchard_deebo.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I killed the Golden jackal. I need to return to Deebo with the… ▸</span><span class="l">▴ less</span></summary>I killed the Golden jackal. I need to return to Deebo with the Golden jackal's fur as proof that I've killed it.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard west ravine](../maps/sullengard_west_ravine.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods 12](../maps/sullengard_woods12.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods 4](../maps/sullengard_woods4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods gj 1](../maps/sullengard_woods_gj1.md).</span> | stepping on a trigger on [Sullengard west ravine](../maps/sullengard_west_ravine.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I returned to Deebo with the killed the Golden jackal's fur as proof… ▸</span><span class="l">▴ less</span></summary>I returned to Deebo with the killed the Golden jackal's fur as proof that I had killed it. He was now willing to trade with me.</details> **(ends quest)** | [Deebo](../monsters/deebo_orchard_deebo.md) | 10,000 XP, 1× [Golden jackal fur](../items/golden_jackal_fur.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-0"></span>

??? note "Stage 0 · Deebo · 1 way"

    **Way 1:** Talk to [Deebo](../monsters/deebo_orchard_deebo.md), choose “I want to hunt down and kill that Golden jackal for you.”

    - **Needs:** not yet stage 50; latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0
    - *“That's great to hear! When can you start?”*


<span id="route-10"></span>

??? note "Stage 10 · Deebo · 2 ways"

    **Way 1:** Talk to [Deebo](../monsters/deebo_orchard_deebo.md), choose “I am ready! No more talking.”

    - **Needs:** not yet stage 50; latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0; not reached stage 4 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-4); random chance (30%)
    - <small>Also: sets stage 4 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-4)</small>
    - *“The Golden jackal was last seen heading back into the "Sullengard forest" just to the west of my orchard. Return to me with proof of it's…”*

    **Way 2:** Talk to [Deebo](../monsters/deebo_orchard_deebo.md), choose “I am ready! No more talking.”

    - **Needs:** not yet stage 50; latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0; not reached stage 4 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-4)


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on sullengard_west_ravine · 1 way"

    **Way 1:** Stepping on a trigger on [Sullengard west ravine](../maps/sullengard_west_ravine.md)

    - **Needs:** not yet stage 40; killed 1× [Golden jackal](../monsters/golden_jackal.md)
    - *“[The Golden jackal has perished.]”*


<span id="route-50"></span>

??? note "Stage 50 · Deebo · 1 way"

    **Way 1:** Talk to [Deebo](../monsters/deebo_orchard_deebo.md), choose “I have killed the Golden jackal and I have the requested proof.”

    - **Needs:** not yet stage 50; hand over 1× [Golden jackal fur](../items/golden_jackal_fur.md); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-40) is 40
    - **Gives:** 1× [Golden jackal fur](../items/golden_jackal_fur.md)
    - *“Wonderful. Let me have it. [You hand over the Golden jackal's fur] Ah yes, this is indeed proof it is dead.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=deebo_orchard_hth.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `deebo_orchard_hth` |
    | showInLog | 1 |
    | Stage IDs | 0, 10, 40, 50 |
    | Dialogue nodes setting stages | 0: `deebo_orchard_deebo_50`, 10: `deebo_orchard_deebo_80`, 10: `deebo_orchard_deebo_spawn_gj`, 40: `jackal_defeted_script_20`, 50: `deebo_orchard_deebo_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
