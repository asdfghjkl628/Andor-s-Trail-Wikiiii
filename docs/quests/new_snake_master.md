---
description: "Perception is not reality is a quest in Andor's Trail, started by Ewmondold (wild2). 5 stages, 700 XP in total. A traveler named Ewmondold had asked me to venture into the Snake Cave to retrieve his map."
---

# Perception is not reality

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `new_snake_master` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 30) |
| **Started by** | [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) ([Wild 2](../maps/wild2.md)) |
| **NPCs involved** | [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) |
| **Locations** | [Wild 2](../maps/wild2.md) |
| **Total XP** | 700 |

</div>

## Overview

> A traveler named Ewmondold had asked me to venture into the Snake Cave to retrieve his map.

## Prerequisites to start

Start with [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) ([Wild 2](../maps/wild2.md)). Required:

- NOT killed 1× [Snake master](../monsters/snake_master.md)
- NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">A traveler named Ewmondold had asked me to venture into the Snake… ▸</span><span class="l">▴ less</span></summary>A traveler named Ewmondold had asked me to venture into the Snake Cave to retrieve his map.</details> | [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Ewmondold had thanked me for killing the Snake master, and that his… ▸</span><span class="l">▴ less</span></summary>Ewmondold had thanked me for killing the Snake master, and that his way to rule would be free. I should find him.</details> | [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) | removes monsters from wild2, spawns monsters on snakecave3 |
| <span id="stage-20"></span>[20](#route-20) | I've returned Ewmondold's map to him. | [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) | 450 XP |
| <span id="stage-25"></span>25 | I must stop Ewmondold from getting stronger. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I've destroyed Ewmondold and eliminated his threat to Crossglen and… ▸</span><span class="l">▴ less</span></summary>I've destroyed Ewmondold and eliminated his threat to Crossglen and the surrounding area.</details> **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Snakecave 3](../maps/snakecave3.md).</span> | stepping on a trigger on [Snakecave 3](../maps/snakecave3.md) | 250 XP, [Gold coins](../items/gold.md) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-5"></span>

??? note "Stage 5 · Ewmondold · 1 way"

    **Way 1:** Talk to [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master), choose “I could retrieve the map for you.”

    - **Needs:** not yet stage 5; not killed 1× [Snake master](../monsters/snake_master.md)
    - *“Please do and hurry back to me.”*


<span id="route-10"></span>

??? note "Stage 10 · Ewmondold · 1 way"

    **Way 1:** Talk to [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master), automatic

    - **Needs:** not yet stage 5; killed 1× [Snake master](../monsters/snake_master.md)
    - **Gives:** removes monsters from wild2, spawns monsters on snakecave3
    - *“Thanks for killing the Snake master, sucker - the way for me to rule is now free...”*


<span id="route-20"></span>

??? note "Stage 20 · Ewmondold · 1 way"

    **Way 1:** Talk to [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master), automatic

    - **Needs:** stage 5; killed 1× [Snake master](../monsters/snake_master.md); hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md)
    - *“Ah, my 'map'. Good!”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on snakecave3 · 1 way"

    **Way 1:** Stepping on a trigger on [Snakecave 3](../maps/snakecave3.md)

    - **Needs:** not yet stage 30; killed 1× [Ewmondold](../monsters/ewmondold_snake_master.md)
    - **Gives:** [Gold coins](../items/gold.md)
    - *“You've destroyed Ewmondold and eliminated his threat to Crossglen and the surrounding area.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.13](../versions/0.7.13.md) | Stage 10 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `new_snake_master` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 25, 30 |
    | Dialogue nodes setting stages | 5: `inspiring_snake_master_70`, 10: `inspiring_snake_master_20`, 20: `inspiring_snake_master_80`, 30: `ewmondold_snake_master_defeted_script_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
