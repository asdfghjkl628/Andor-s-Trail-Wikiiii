---
description: "Final cave is a hidden quest in Andor's Trail, started by walking into a blocked passage on final_cave1. 12 stages. key 1 set - sw"
---

# Final cave

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `final_cave` |
| **In journal** | No (hidden flag) |
| **Stages** | 12 |
| **Started by** | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) |
| **NPCs involved** | [Algangror](../monsters/algangror.md#v-lae_algangror1), [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1) |
| **Locations** | [Island 4 cave 1](../maps/island_4_cave1.md) |
| **Related quests** | 1 |

</div>

## Overview

> key 1 set - sw

## Prerequisites to start

**Route 1** (walking into a blocked passage on [Final cave 1](../maps/final_cave1.md)):

- hand over 1× [Scroll of fire](../items/final_cave_f.md)

**Route 2** (walking into a blocked passage on [Final cave 1](../maps/final_cave1.md)):

- hand over 1× [Scroll of water](../items/final_cave_w.md)

**Route 3** (walking into a blocked passage on [Final cave 1](../maps/final_cave1.md)):

- hand over 1× [Scroll of earth](../items/final_cave_e.md)

**Route 4** (walking into a blocked passage on [Final cave 1](../maps/final_cave1.md)):

- hand over 1× [Scroll of wind](../items/final_cave_a.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Mutually exclusive | [Not Pony Island](lae_centaurs.md#stage-150) | stage 150 must NOT be reached, for stage 11 here |
| Mutually exclusive | [Not Pony Island](lae_centaurs.md#stage-210) | stage 210 must NOT be reached, for stage 9 here |
| Unlocks | [Not Pony Island](lae_centaurs.md#stage-140) | stage 140 there needs stage 11 here |
| Unlocks | [Not Pony Island](lae_centaurs.md#stage-150) | stage 150 there needs stages 1, 2, 3, 4, 5, 6, 7, 10 here |
| Unlocks | [Not Pony Island](lae_centaurs.md#stage-190) | stage 190 there needs stage 10 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | key 1 set - sw<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-2"></span>[2](#route-2) | key 2 set - w<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-3"></span>[3](#route-3) | key 3 set - nw<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-4"></span>[4](#route-4) | key 4 set - n<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-5"></span>[5](#route-5) | key 5 set - ne<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-6"></span>[6](#route-6) | key 6 set - e<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-7"></span>[7](#route-7) | key 7 set - se<br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md) | varies by route (see below) |
| <span id="stage-9"></span>[9](#route-9) | 9: wall down<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 2](../maps/final_cave2.md).</span><br><span class="qnote">🗺️ Part of [Final cave 1](../maps/final_cave1.md) visibly changes.</span> | walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), stepping on a trigger on [Final cave 1](../maps/final_cave1.md) +2 | varies by route (see below) |
| <span id="stage-10"></span>[10](#route-10) | 10: 0=Algangror 1=Jhaeld<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Island 4](../maps/island4.md).</span> | stepping on a trigger on [Island 4](../maps/island4.md) | spawns monsters on island_4_cave1 |
| <span id="stage-11"></span>[11](#route-11) | 11: Andor talk<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Final cave 1](../maps/final_cave1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Island 1](../maps/island1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Island 2](../maps/island2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Island 3](../maps/island3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Island 4](../maps/island4.md).</span> | stepping on a trigger on [Final cave 1](../maps/final_cave1.md) | sets stage 130 of [Not Pony Island](../quests/lae_centaurs.md#stage-130), removes monsters from island_4_cave1, removes monsters from island_4_cave1 |
| <span id="stage-12"></span>[12](#route-12) | 12: Algangror/Jhaeld talk<br><span class="qnote">🔓 You can finally access a previously blocked area on [Island 4 cave 1](../maps/island_4_cave1.md).</span> | [Algangror](../monsters/algangror.md#v-lae_algangror1), [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1) | – |
| <span id="stage-99"></span>99 | x | *no trigger found* <sup>[?](#untraced)</sup> | – |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · walking into a blocked passage on final_cave1 · 4 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_f” set to 1

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of water”

    - **Needs:** hand over 1× [Scroll of water](../items/final_cave_w.md)
    - **Gives:** faction “final_cave_w” set to 1

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of earth”

    - **Needs:** hand over 1× [Scroll of earth](../items/final_cave_e.md)
    - **Gives:** faction “final_cave_e” set to 1

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of wind”

    - **Needs:** hand over 1× [Scroll of wind](../items/final_cave_a.md)
    - **Gives:** faction “final_cave_a” set to 1


<span id="route-2"></span>

??? note "Stage 2 · walking into a blocked passage on final_cave1 · 3 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The red globe”

    - **Needs:** hand over 1× [Red globe of the elements](../items/final_cave_r.md)
    - **Gives:** faction “final_cave_r” set to 2

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The green globe”

    - **Needs:** hand over 1× [Green globe of the elements](../items/final_cave_g.md)
    - **Gives:** faction “final_cave_g” set to 2

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The blue globe”

    - **Needs:** hand over 1× [Blue globe of the elements](../items/final_cave_b.md)
    - **Gives:** faction “final_cave_b” set to 2


<span id="route-3"></span>

??? note "Stage 3 · walking into a blocked passage on final_cave1 · 4 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_f” set to 3

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of water”

    - **Needs:** hand over 1× [Scroll of water](../items/final_cave_w.md)
    - **Gives:** faction “final_cave_w” set to 3

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of earth”

    - **Needs:** hand over 1× [Scroll of earth](../items/final_cave_e.md)
    - **Gives:** faction “final_cave_e” set to 3

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of wind”

    - **Needs:** hand over 1× [Scroll of wind](../items/final_cave_a.md)
    - **Gives:** faction “final_cave_a” set to 3


<span id="route-4"></span>

??? note "Stage 4 · walking into a blocked passage on final_cave1 · 3 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The red globe”

    - **Needs:** hand over 1× [Red globe of the elements](../items/final_cave_r.md)
    - **Gives:** faction “final_cave_r” set to 4

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The green globe”

    - **Needs:** hand over 1× [Green globe of the elements](../items/final_cave_g.md)
    - **Gives:** faction “final_cave_g” set to 4

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The blue globe”

    - **Needs:** hand over 1× [Blue globe of the elements](../items/final_cave_b.md)
    - **Gives:** faction “final_cave_b” set to 4


<span id="route-5"></span>

??? note "Stage 5 · walking into a blocked passage on final_cave1 · 4 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_f” set to 5

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of water”

    - **Needs:** hand over 1× [Scroll of water](../items/final_cave_w.md)
    - **Gives:** faction “final_cave_w” set to 5

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of earth”

    - **Needs:** hand over 1× [Scroll of earth](../items/final_cave_e.md)
    - **Gives:** faction “final_cave_e” set to 5

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of wind”

    - **Needs:** hand over 1× [Scroll of wind](../items/final_cave_a.md)
    - **Gives:** faction “final_cave_a” set to 5


<span id="route-6"></span>

??? note "Stage 6 · walking into a blocked passage on final_cave1 · 3 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The red globe”

    - **Needs:** hand over 1× [Red globe of the elements](../items/final_cave_r.md)
    - **Gives:** faction “final_cave_r” set to 6

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The green globe”

    - **Needs:** hand over 1× [Green globe of the elements](../items/final_cave_g.md)
    - **Gives:** faction “final_cave_g” set to 6

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The blue globe”

    - **Needs:** hand over 1× [Blue globe of the elements](../items/final_cave_b.md)
    - **Gives:** faction “final_cave_b” set to 6


<span id="route-7"></span>

??? note "Stage 7 · walking into a blocked passage on final_cave1 · 4 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_f” set to 7

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of water”

    - **Needs:** hand over 1× [Scroll of water](../items/final_cave_w.md)
    - **Gives:** faction “final_cave_w” set to 7

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of earth”

    - **Needs:** hand over 1× [Scroll of earth](../items/final_cave_e.md)
    - **Gives:** faction “final_cave_e” set to 7

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “The scroll of wind”

    - **Needs:** hand over 1× [Scroll of wind](../items/final_cave_a.md)
    - **Gives:** faction “final_cave_a” set to 7


<span id="route-9"></span>

??? note "Stage 9 · walking into a blocked passage on final_cave1, stepping on a · 10 ways"

    **Way 1:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** stage 1; not yet stage 9; faction “final_cave_f” = 1; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 2:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** stage 2; not yet stage 9; faction “final_cave_r” = 2; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 3:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** stage 3; not yet stage 9; faction “final_cave_f” = 3; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 4:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** stage 4; not yet stage 9; faction “final_cave_r” = 4; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 5:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** stage 5; not yet stage 9; faction “final_cave_f” = 5; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 6:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my red globe.”

    - **Needs:** stage 6; not yet stage 9; faction “final_cave_r” = 6; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 7:** Walking into a blocked passage on [Final cave 1](../maps/final_cave1.md), choose “I take back my scroll of fire.”

    - **Needs:** stage 7; not yet stage 9; faction “final_cave_f” = 7; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 8:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md)

    - **Needs:** stage 10; not yet stage 9; faction “final_cave_e” = 1; faction “final_cave_g” = 2; faction “final_cave_f” = 3; faction “final_cave_b” = 4; faction “final_cave_a” = 5; faction “final_cave_r” = 6; faction “final_cave_w” = 7
    - **Gives:** sets stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150), faction “final_cave_hint” set to 999
    - *“A loud rumbling fills the air!”*

    **Way 9:** Walking into a blocked passage on [Final cave 2](../maps/final_cave2.md), choose “The scroll of fire”

    - **Needs:** hand over 1× [Scroll of fire](../items/final_cave_f.md)
    - **Gives:** faction “final_cave_e” set to 0, faction “final_cave_g” set to 0, faction “final_cave_f” set to 0, faction “final_cave_b” set to 0, faction “final_cave_a” set to 0, faction “final_cave_r” set to 0, faction “final_cave_w” set to 0, sets stage 210 of [Not Pony Island](../quests/lae_centaurs.md#stage-210), faction “final_cave_hint” set to 999, applies condition bleeding_wound
    - <small>Also: clears stage 1 of [Final cave (hidden flag)](../quests/final_cave.md#stage-1), clears stage 2 of [Final cave (hidden flag)](../quests/final_cave.md#stage-2), clears stage 3 of [Final cave (hidden flag)](../quests/final_cave.md#stage-3), clears stage 4 of [Final cave (hidden flag)](../quests/final_cave.md#stage-4), clears stage 5 of [Final cave (hidden flag)](../quests/final_cave.md#stage-5), clears stage 6 of [Final cave (hidden flag)](../quests/final_cave.md#stage-6), clears stage 7 of [Final cave (hidden flag)](../quests/final_cave.md#stage-7)</small>
    - *“A loud rumbling fills the air! - At the same time the scroll of fire explodes.”*

    **Way 10:** Stepping on a trigger on [Final cave 2](../maps/final_cave2.md)

    - **Needs:** killed 123× [Dorhantarh](../monsters/lae_island_boss.md); not reached stage 210 of [Not Pony Island](../quests/lae_centaurs.md#stage-210)
    - **Gives:** sets stage 210 of [Not Pony Island](../quests/lae_centaurs.md#stage-210), faction “final_cave_hint” set to 999
    - *“You hear a loud rumbling from above. Seems to be the walls are opened up again.”*


<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on island4 · 1 way"

    **Way 1:** Stepping on a trigger on [Island 4](../maps/island4.md)

    - **Needs:** killed 1× [Algangror](../monsters/algangror.md)
    - **Gives:** spawns monsters on island_4_cave1


<span id="route-11"></span>

??? note "Stage 11 · stepping on a trigger on final_cave1 · 1 way"

    **Way 1:** Stepping on a trigger on [Final cave 1](../maps/final_cave1.md), choose “What?!”

    - **Needs:** not yet stage 11; not reached stage 150 of [Not Pony Island](../quests/lae_centaurs.md#stage-150); random chance (25%)
    - **Gives:** sets stage 130 of [Not Pony Island](../quests/lae_centaurs.md#stage-130), removes monsters from island_4_cave1, removes monsters from island_4_cave1
    - *“I entered this room to find a powerful weapon against the enemy, when suddenly the walls closed around me.”*


<span id="route-12"></span>

??? note "Stage 12 · Algangror, Jhaeld · 2 ways"

    **Way 1:** Talk to [Algangror](../monsters/algangror.md#v-lae_algangror1), choose “Of course I'm happy to help.”

    - *“To free him I would need to go for some items all over the isle. But these nasty centaurs wouldn't let me.”*

    **Way 2:** Talk to [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld1), choose “Of course I'm happy to help.”

    - *“To free him I would need to go for some items all over the isle. But these nasty centaurs wouldn't let me.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 60 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=final_cave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=final_cave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=final_cave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=final_cave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=final_cave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `final_cave` |
    | Name in game data | `final_cave` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 99 |
    | Dialogue nodes setting stages | 1: `final_cave_k1_10_f`, 1: `final_cave_k1_10_w`, 1: `final_cave_k1_10_e`, 2: `final_cave_k2_10_r`, 2: `final_cave_k2_10_g`, 2: `final_cave_k2_10_b`, 3: `final_cave_k3_10_f`, 3: `final_cave_k3_10_w`, 3: `final_cave_k3_10_e`, 4: `final_cave_k4_10_r`, 4: `final_cave_k4_10_g`, 4: `final_cave_k4_10_b`, 5: `final_cave_k5_10_f`, 5: `final_cave_k5_10_w`, 5: `final_cave_k5_10_e`, 6: `final_cave_k6_10_r`, 6: `final_cave_k6_10_g`, 6: `final_cave_k6_10_b`, 7: `final_cave_k7_10_f`, 7: `final_cave_k7_10_w`, 7: `final_cave_k7_10_e`, 9: `final_cave_kx_open`, 9: `final_cave2_k1_10_f`, 9: `lae_fc2_s1_6`, 10: `final_cave_init_j`, 11: `lae_andor1_42`, 12: `lae_algangror1_30` |
    | Dialogue nodes clearing stages | 1: `final_cave_k1_20_f`, 1: `final_cave_k1_20_w`, 1: `final_cave_k1_20_e`, 1: `final_cave_k1_20_a`, 1: `final_cave_s9`, 1: `lae_andor1_999_maybe_obsolete`, 1: `final_cave2_k1_10_f`, 2: `final_cave_k2_20_r`, 2: `final_cave_k2_20_g`, 2: `final_cave_k2_20_b` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
