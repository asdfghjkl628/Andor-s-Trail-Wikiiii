---
description: "Where is Norry? is a quest in Andor's Trail, started by Little Hettar (blackwater_mountain55). 7 stages, 2,200 XP in total. I found Hettar, a tough boy about my age, on top of Blackwater mountain. He kept calling for a certain Norry."
---

# Where is Norry?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `hettar_dog` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 80, 90) |
| **Started by** | [Little Hettar](../monsters/hettar.md) ([Blackwater mountain 55](../maps/blackwater_mountain55.md)) |
| **NPCs involved** | [Little Hettar](../monsters/hettar.md), [Wolfhound](../monsters/hettar_dog.md) |
| **Locations** | [Blackwater mountain 55](../maps/blackwater_mountain55.md) |
| **Total XP** | 2,200 |
| **Related quests** | 1 |

</div>

## Overview

> I found Hettar, a tough boy about my age, on top of Blackwater mountain. He kept calling for a certain Norry.

## Prerequisites to start

None: talk to [Little Hettar](../monsters/hettar.md) ([Blackwater mountain 55](../maps/blackwater_mountain55.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Hettar dog story flags (hidden flag)](hettar_dog_nd.md#stage-2) | stage 2 reached, for stage 40 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I found Hettar, a tough boy about my age, on top of Blackwater… ▸</span><span class="l">▴ less</span></summary>I found Hettar, a tough boy about my age, on top of Blackwater mountain. He kept calling for a certain Norry.</details> | [Little Hettar](../monsters/hettar.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Hettar's little dog Norry has run away. He was very anxious to find… ▸</span><span class="l">▴ less</span></summary>Hettar's little dog Norry has run away. He was very anxious to find him. I promised to get Norry back.</details> | [Little Hettar](../monsters/hettar.md) | removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55 |
| <span id="stage-30"></span>[30](#route-30) | Hettar has given me a piece of Norry's favorite food. | [Little Hettar](../monsters/hettar.md) | 1× [Wyrm meat](../items/hettar_bone.md) |
| <span id="stage-40"></span>[40](#route-40) | I have offered Hettar's piece of Wyrm meat to Norry, who took it eagerly. | [Wolfhound](../monsters/hettar_dog.md) | – |
| <span id="stage-50"></span>[50](#route-50) | Norry ran off to reunite with Hettar. | [Wolfhound](../monsters/hettar_dog.md) | removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55 |
| <span id="stage-80"></span>[80](#route-80) | Hettar thanked me a thousand times for my help in finding Norry. **(ends quest)** | [Little Hettar](../monsters/hettar.md) | 2,000 XP |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">I explained to Hettar that I killed Norry. Hettar broke down on the… ▸</span><span class="l">▴ less</span></summary>I explained to Hettar that I killed Norry. Hettar broke down on the floor in agony.</details> **(ends quest)** | [Little Hettar](../monsters/hettar.md) | 200 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Little Hettar · 1 way"

    **Way 1:** Talk to [Little Hettar](../monsters/hettar.md), choose “Who is Norry?”

    - *“Norry is my little doggie. He fell down the steep slope and has not found his way back yet.”*


<span id="route-20"></span>

??? note "Stage 20 · Little Hettar · 1 way"

    **Way 1:** Talk to [Little Hettar](../monsters/hettar.md), choose “OK, I'll do it.”

    - **Needs:** stage 20; not killed 1× [Wolfhound](../monsters/hettar_dog.md#v-hettar_dog3)
    - **Gives:** removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55
    - *“Great! Go immediately, as long as he might be alive still.”*


<span id="route-30"></span>

??? note "Stage 30 · Little Hettar · 1 way"

    **Way 1:** Talk to [Little Hettar](../monsters/hettar.md), choose “I hope he will follow me.”

    - **Needs:** stage 20; not yet stage 30; not killed 1× [Wolfhound](../monsters/hettar_dog.md#v-hettar_dog3)
    - **Gives:** 1× [Wyrm meat](../items/hettar_bone.md)
    - *“Good that you have mentioned it. I'll give you a nice raw piece of Wyrm meat that I have as food for Norry. He loves them.”*


<span id="route-40"></span>

??? note "Stage 40 · Wolfhound · 1 way"

    **Way 1:** Talk to [Wolfhound](../monsters/hettar_dog.md), choose “Hey Norry, look here! I have some much better food for you from Hettar.”

    - **Needs:** hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-2)
    - <small>Also: sets stage 2 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-2)</small>
    - *“The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.”*


<span id="route-50"></span>

??? note "Stage 50 · Wolfhound · 1 way"

    **Way 1:** Talk to [Wolfhound](../monsters/hettar_dog.md), choose “Now run to Hettar! He is waiting for you.”

    - **Needs:** stage 40
    - **Gives:** removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55
    - *“A moment later the huge wolfhound was gone.”*


<span id="route-80"></span>

??? note "Stage 80 · Little Hettar · 1 way"

    **Way 1:** Talk to [Little Hettar](../monsters/hettar.md), choose “Now guess who had persuaded him to do so? He was absorbed by a pile of monster bones.”

    - **Needs:** stage 50
    - *“Oh. Thank you then.”*


<span id="route-90"></span>

??? note "Stage 90 · Little Hettar · 1 way"

    **Way 1:** Talk to [Little Hettar](../monsters/hettar.md), choose “This brute attacked me, so I had to kill it.”

    - **Needs:** stage 30; killed 1× [Wolfhound](../monsters/hettar_dog.md#v-hettar_dog3)
    - *“[Hettar fell on the floor] Nooo! What did you do?!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 7 lines added |
| [v0.7.15](../versions/0.7.15.md) | Stage 30 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `hettar_dog` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 80, 90 |
    | Dialogue nodes setting stages | 10: `hettar_1_2`, 20: `hettar_20_10`, 30: `hettar_20_30`, 40: `hettar_dog_10`, 50: `hettar_dog_20`, 80: `hettar_50_10`, 90: `hettar_10_6` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
