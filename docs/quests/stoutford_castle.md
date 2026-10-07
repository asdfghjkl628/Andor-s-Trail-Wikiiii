---
description: "Stoutford's old castle is a quest in Andor's Trail, started by stepping on a trigger on stoutford_castle0. 11 stages, 6,550 XP in total. I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help..."
---

# Stoutford's old castle

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `stoutford_castle` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 50, 60, 70) |
| **Started by** | stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) |
| **NPCs involved** | [Tahalendor](../monsters/tahalendor.md), [Yolgen](../monsters/yolgen.md) |
| **Locations** | [Stoutford church](../maps/stoutford_church.md) |
| **Total XP** | 6,550 |
| **Related quests** | 3 |

</div>

## Overview

> I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help...

## Prerequisites to start

Start with stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md). Required:

- killed 1× [Lord Erwyn](../monsters/erwyn.md)
- reached stage 48 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-48)
- NOT reached stage 49 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-49)
- killed 2× [Lord Erwyn](../monsters/erwyn.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [General story flags 2 (hidden flag)](nondisplay_2.md#stage-180) | stage 180 reached, for stages 10, 12 here |
| Requires | [General story flags 2 (hidden flag)](nondisplay_2.md#stage-190) | stage 190 reached, for stages 10, 12 here |
| Requires | [Rumblings](rumblings.md#stage-80) | stage 80 reached, for stages 10, 12, 20, 30, 42, 50, 60, 70 here |
| Requires | [Rumblings](rumblings.md#stage-106) | stage 106 reached, for stage 14 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-46) | stage 46 reached, for stages 20, 30 here |
| Requires | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-48) | stage 48 reached, for stages 5, 16 here |
| Blocked by | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-49) | stage 49 must NOT be reached, for stage 5 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">I tried to free this castle from the undead Lord Erwyn. But whenever… ▸</span><span class="l">▴ less</span></summary>I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help...</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle 0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I talked to Yolgen, the Shadow priest of Stoutford, and he told me… ▸</span><span class="l">▴ less</span></summary>I talked to Yolgen, the Shadow priest of Stoutford, and he told me that the mighty Lord Erwyn used to reside here, but Lord Erwyn and his army were crushed during a war, the castle was sacked and the house extinguished. But recently Erwyn's knights have risen from the dead. Yolgen asked me to rid Stoutford of these undead once and for all.</details> | [Yolgen](../monsters/yolgen.md) | – |
| <span id="stage-12"></span>[12](#route-12) | <details class="jt"><summary><span class="s">I should ask Tahalendor for some special artifact that I can use to… ▸</span><span class="l">▴ less</span></summary>I should ask Tahalendor for some special artifact that I can use to defeat powerful undead.</details> | [Yolgen](../monsters/yolgen.md) | – |
| <span id="stage-14"></span>[14](#route-14) | <details class="jt"><summary><span class="s">Tahalendor gave me a pair of special coins that I can use to defeat… ▸</span><span class="l">▴ less</span></summary>Tahalendor gave me a pair of special coins that I can use to defeat powerful undead.</details> | [Tahalendor](../monsters/tahalendor.md) | 2× [Gold coins](../items/erwyn_coin.md) |
| <span id="stage-16"></span>[16](#route-16) | I slew Lord Erwyn himself and ensured that he remains dead now.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle 0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md) | 500 XP, removes monsters from stoutford_castle0 |
| <span id="stage-20"></span>[20](#route-20) | I slew all the undead knights. | [Yolgen](../monsters/yolgen.md) | 2,000 XP |
| <span id="stage-30"></span>[30](#route-30) | I slew Lord Erwyn's commander. | [Yolgen](../monsters/yolgen.md) | 1,000 XP |
| <span id="stage-42"></span>[42](#route-42) | Among his remains I found a strange ring. I should show it to Yolgen. | [Yolgen](../monsters/yolgen.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">Yolgen examined the ring thoroughly. He suspects it has somehow come… ▸</span><span class="l">▴ less</span></summary>Yolgen examined the ring thoroughly. He suspects it has somehow come from Mt. Galmore and reanimated the long dead soldiers. I should be wary of the evil grasp of Mt. Galmore and whatever lurks there...</details> **(ends quest)** | [Yolgen](../monsters/yolgen.md) | 2,050 XP |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I kept the ring for myself, which upset Yolgen. I should keep… ▸</span><span class="l">▴ less</span></summary>I kept the ring for myself, which upset Yolgen. I should keep looking for its previous owner.</details> **(ends quest)** | [Yolgen](../monsters/yolgen.md) | 500 XP |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I kept the ring for myself and didn't tell Yolgen about it. He was… ▸</span><span class="l">▴ less</span></summary>I kept the ring for myself and didn't tell Yolgen about it. He was suspicious but couldn't do anything about it. I should keep looking for its previous owner.</details> **(ends quest)** | [Yolgen](../monsters/yolgen.md) | 500 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-5"></span>

??? note "Stage 5 · stepping on a trigger on stoutford_castle0 · 1 way"

    **Way 1:** Stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md)

    - **Needs:** killed 1× [Lord Erwyn](../monsters/erwyn.md); reached stage 48 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-48); not reached stage 49 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-49); killed 2× [Lord Erwyn](../monsters/erwyn.md)
    - *“I'm not dead, so you can't kill me. Haha. You don't know much about the undead, do you kid? You can't destroy me!”*


<span id="route-10"></span>

??? note "Stage 10 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “No problem. They are already as good as dead.”

    - **Needs:** not yet stage 10; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 180 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-190); not reached stage 10 of stoutford reinforcements (flag not defined in the game data); reached stage 10 of not yet realized (flag not defined in the game data)
    - *“Before you leave, go to Tahalendor. He might give you something that helps against undead.”*


<span id="route-12"></span>

??? note "Stage 12 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “No problem. They are already as good as dead.”

    - **Needs:** not yet stage 10; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 180 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-190); not reached stage 10 of stoutford reinforcements (flag not defined in the game data); reached stage 10 of not yet realized (flag not defined in the game data)
    - *“Before you leave, go to Tahalendor. He might give you something that helps against undead.”*


<span id="route-14"></span>

??? note "Stage 14 · Tahalendor · 1 way"

    **Way 1:** Talk to [Tahalendor](../monsters/tahalendor.md), choose “OK.”

    - **Needs:** stage 12; not yet stage 14; reached stage 106 of [Rumblings](../quests/rumblings.md#stage-106); killed 1× [Lord Erwyn](../monsters/erwyn.md); pay 2 gold
    - **Gives:** 2× [Gold coins](../items/erwyn_coin.md)
    - *“Here you go. As soon as the undead lord appears to be destroyed, place one coin on each eye. This will prevent him from rising again, and…”*


<span id="route-16"></span>

??? note "Stage 16 · stepping on a trigger on stoutford_castle0 · 1 way"

    **Way 1:** Stepping on a trigger on [Stoutford castle 0](../maps/stoutford_castle0.md)

    - **Needs:** killed 1× [Lord Erwyn](../monsters/erwyn.md#v-erwyn2); reached stage 48 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-48)
    - **Gives:** removes monsters from stoutford_castle0
    - <small>Also: clears stage 48 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-48)</small>
    - *“I followed Tahalendor's advice, and placed one coin in each eye socket. Not long after, Lord Erwyn's remains crumbled to dust. He is gone…”*


<span id="route-20"></span>

??? note "Stage 20 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “I have dealt with Erwyn's army.”

    - **Needs:** stage 10; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 46 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-46)
    - *“Let me see... OK, you killed all of the undead knights and soldiers who had worn Lord Erwyn's tattered banner.”*


<span id="route-30"></span>

??? note "Stage 30 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “I have dealt with Erwyn's army.”

    - **Needs:** stage 10; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 46 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-46); killed 1× [Karth the Unbowed](../monsters/erwyn_commander.md)
    - *“And you slew Lord Erwyn's commander.”*


<span id="route-42"></span>

??? note "Stage 42 · Yolgen · 2 ways"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “Sure. I found this ring among his remains.”

    - **Needs:** stage 10, 40; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md)
    - *“I am very pleased to hear this. A ring you say? Let me take a look.”*

    **Way 2:** Talk to [Yolgen](../monsters/yolgen.md), choose “Sure. I found this ring among his remains.”

    - **Needs:** stage 10, 40; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md)
    - *“Hmm. This looks most interesting. I suspected something like this. It is certainly some magical item and seems to have the powers to…”*


<span id="route-50"></span>

??? note "Stage 50 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “Sounds fine to me. Anything for the safety of the people of Stoutford.”

    - **Needs:** stage 10, 40; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md); hand over 1× [Lord Erwyn's ring](../items/erwyn_ring.md)
    - *“That is it. The ring is destroyed. I wonder where it came from. Maybe from the depths of Mt. Galmore, or some mischievous traveller put it…”*


<span id="route-60"></span>

??? note "Stage 60 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “No, I don't think so. I wonder who had owned the ring before Erwyn?”

    - **Needs:** stage 10, 40; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80)
    - *“Do not play with ancient forces that are beyond your power.”*


<span id="route-70"></span>

??? note "Stage 70 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “[Lie] Yes, but I found nothing worth having.”

    - **Needs:** stage 10, 40; not yet stage 50, 60, 70; reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80)
    - *“If you say so. I suspect Lord Erwyn had a ring, and if you find it you must bring it to me. It is dangerous.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.7.11](../versions/0.7.11.md) | Stage 12 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `stoutford_castle` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 12, 14, 16, 20, 30, 42, 50, 60, 70 |
    | Dialogue nodes setting stages | 5: `check_erwyn_2b`, 10: `yolgen_castle_0_1`, 12: `yolgen_castle_0_1`, 14: `tahalendor_erwyn_6`, 16: `check_erwyn_1`, 20: `yolgen_castle_1_1a`, 30: `yolgen_castle_1_2a`, 42: `yolgen_castle_3`, 42: `yolgen_castle_4`, 50: `yolgen_castle_6`, 60: `yolgen_castle_13`, 70: `yolgen_castle_11` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
