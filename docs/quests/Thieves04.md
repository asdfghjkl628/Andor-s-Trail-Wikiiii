---
description: "Another ruthless Crackshot is a quest in Andor's Trail, started by Umar (fallhaven_derelict2). 10 stages, 35,000 XP in total. Umar told me to visit Defy in Sullengard to instruct him to give the villagers their share."
---

# Another ruthless Crackshot

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves04` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 80) |
| **Started by** | [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Defy](../monsters/g04_defy.md), [Matpat](../monsters/sullengard_matpat.md), [Mayor Ale](../monsters/sullengard_mayor.md), [Umar](../monsters/umar.md) |
| **Locations** | [Fallhaven derelict 2](../maps/fallhaven_derelict2.md), [Fallhaven derelict 2 t](../maps/fallhaven_derelict2_t.md), [Sullengard 1 northeast house](../maps/sullengard1_northeast_house.md), [Sullengard 1 townhall](../maps/sullengard1_townhall.md) |
| **Total XP** | 35,000 |
| **Related quests** | 4 |

</div>

## Overview

> Umar told me to visit Defy in Sullengard to instruct him to give the villagers their share.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
- latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stages 10, 30, 40, 60, 70, 80 here |
| Requires | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-30) | stage 30 reached, for stage 80 here |
| Mutually exclusive | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-30) | stage 30 must NOT be reached, for stage 70 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-20) | stage 20 there needs stage 10 here |
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-28) | stage 28 there needs stage 70 here |
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-37) | stage 37 there needs stage 75 here |
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-39) | stage 39 there needs stage 80 here |
| Unlocks | [Sullengard story flags (hidden flag)](sullengard_hidden.md#stage-42) | stage 42 there needs stage 80 here |
| Unlocks | [Troubling times](troubling_times.md#stage-110) | stage 110 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-130) | stage 130 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-140) | stage 140 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-320) | stage 320 there needs stage 75 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Umar told me to visit Defy in Sullengard to instruct him to give the… ▸</span><span class="l">▴ less</span></summary>Umar told me to visit Defy in Sullengard to instruct him to give the villagers their share.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Defy told me that there will be a delay in giving the villagers of… ▸</span><span class="l">▴ less</span></summary>Defy told me that there will be a delay in giving the villagers of Sullengard their fair share for some unknown reason. I must report this to Umar at once.</details> | [Defy](../monsters/g04_defy.md) | – |
| <span id="stage-30"></span>[30](#route-30) | Umar instructed me to talk to Defy once more. | [Umar](../monsters/umar.md) | removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement |
| <span id="stage-35"></span>[35](#route-35) | Defy and his friends have vanished! Back to Umar ...<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard tavern basement](../maps/sullengard_tavern_basement.md).</span> | stepping on a trigger on [Sullengard tavern basement](../maps/sullengard_tavern_basement.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I told Umar about the disappearance of Defy and his men. But Umar… ▸</span><span class="l">▴ less</span></summary>I told Umar about the disappearance of Defy and his men. But Umar didn't believe me and he even sent me back to find them. I better ask the villagers there.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">There was a distressed man, whom just had his first child, who… ▸</span><span class="l">▴ less</span></summary>There was a distressed man, whom just had his first child, who hinted to me of wherabouts of Defy and his men. I must report this to Umar once more.</details> | [Matpat](../monsters/sullengard_matpat.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">With Sullengard running into financial trouble, Umar is enraged by… ▸</span><span class="l">▴ less</span></summary>With Sullengard running into financial trouble, Umar is enraged by Defy's traitorous way.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">Umar gave me a task to give the mayor at least 50000 gold coins as… ▸</span><span class="l">▴ less</span></summary>Umar gave me a task to give the mayor at least 50000 gold coins as the promised share for their living. After that, I'm instructed to report back to him.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-75"></span>[75](#route-75) | <details class="jt"><summary><span class="s">Sullengard has been given their share of the gold and now it's time… ▸</span><span class="l">▴ less</span></summary>Sullengard has been given their share of the gold and now it's time to revisit Umar.</details><br><span class="qnote">🗺️ Part of [Lake shore road 9](../maps/lake_shore_road_9.md) visibly changes.</span> | [Mayor Ale](../monsters/sullengard_mayor.md) | – |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">At last, Sullengard can now sleep calmly and eat sufficiently with… ▸</span><span class="l">▴ less</span></summary>At last, Sullengard can now sleep calmly and eat sufficiently with their finances restored.</details> **(ends quest)** | [Umar](../monsters/umar.md) | 35,000 XP, faction “ThievesGuild” +10, 1× [Blade of the protector](../items/blade_protector.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “You can count on me.”

    - **Needs:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10
    - *“Hurry now. There's no time to waste.”*


<span id="route-20"></span>

??? note "Stage 20 · Defy · 1 way"

    **Way 1:** Talk to [Defy](../monsters/g04_defy.md), choose “Umar told me that it is time to give their share to the bootleg brewers.”

    - **Needs:** latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10
    - *“The time of sharing? If that's so, then tell him that there will be a delay.”*


<span id="route-30"></span>

??? note "Stage 30 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “I don't know.”

    - **Needs:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-20) is 20
    - **Gives:** removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement
    - *“Sigh. He may be stubborn sometimes but he is a great supervisor. You should ask him once he is calm.”*


<span id="route-35"></span>

??? note "Stage 35 · stepping on a trigger on sullengard_tavern_basement · 1 way"

    **Way 1:** Stepping on a trigger on [Sullengard tavern basement](../maps/sullengard_tavern_basement.md)

    - **Needs:** latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-30) is 30
    - *“Strange. Defy and his men are gone. Maybe they talked with the bootleg brewers here and reported back to Umar?”*


<span id="route-40"></span>

??? note "Stage 40 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Defy and his men have left Sullengard.”

    - **Needs:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-35) is 35
    - *“He can't be gone without our share from the bootleg brewers.”*


<span id="route-50"></span>

??? note "Stage 50 · Matpat · 1 way"

    **Way 1:** Talk to [Matpat](../monsters/sullengard_matpat.md), choose “Calm down. I will find a way to help you.”

    - **Needs:** stage 40
    - *“Thank you. You are my only hope here. I don't trust those unlawful Feygard soldiers. You should talk to the head of the Thieves' Guild…”*


<span id="route-60"></span>

??? note "Stage 60 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Matpat told me that Defy and his men left Sullengard.”

    - **Needs:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-50) is 50
    - *“This is madness! He betrayed us just like Crackshot did.”*


<span id="route-70"></span>

??? note "Stage 70 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “How can we earn that large amount of gold?”

    - **Needs:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70) is 70; not reached stage 30 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-30)
    - *“I trust that you will find a way. In the meantime, go back to Sullengard and give them the share we promised them so they can go on with…”*


<span id="route-75"></span>

??? note "Stage 75 · Mayor Ale · 1 way"

    **Way 1:** Talk to [Mayor Ale](../monsters/sullengard_mayor.md), automatic

    - **Needs:** faction “gold_contribute” ≥ 50000
    - <small>Also: sets stage 30 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-30)</small>
    - *“Thank you so much again, kid. You are just like your brother Andor. After we are done speaking, you really should speak with my assistant,…”*


<span id="route-80"></span>

??? note "Stage 80 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “I have given them our promised share.”

    - **Needs:** not yet stage 80; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 30 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-30)
    - **Gives:** faction “ThievesGuild” +10, 1× [Blade of the protector](../items/blade_protector.md)
    - *“Good job, kid! I knew I could count on you. Here, take this blade. It used to be your brother's.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.8.2](../versions/0.8.2.md) | Renamed “Honor and plunder” → “Another ruthless Crackshot”<br>Journal visibility changed<br>Stages added: 10, 20, 30, 35, 40, 50, 60, 70, 80<br>Stages removed: 5<br>Dialogue: 10 lines added |
| [v0.8.4](../versions/0.8.4.md) | Stages added: 75<br>Stage 70 journal text changed<br>Dialogue: 3 lines changed<br>· text: “[Strange. Defy and his men are gone. Maybe they talked with the bootl…” → “Strange. Defy and his men are gone. Maybe they talked with the bootle…” |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “Thank you so much again, kid. You are just like your brother Andor.” → “Thank you so much again, kid. You are just like your brother Andor. A…” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed<br>· text: “Thank you. You are my only hope here. I don't trust those unlawful Fe…” → “Thank you. You are my only hope here. I don't trust those unlawful Fe…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `Thieves04` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 60, 70, 75, 80 |
    | Dialogue nodes setting stages | 10: `umar_guild04_14`, 20: `guild04_defy_4`, 30: `umar_guild04_16`, 35: `guild04_defy_gone_script_grant`, 40: `umar_guild04_17`, 50: `sullengard_matpat_6`, 60: `umar_guild04_19`, 70: `umar_guild04_27`, 75: `sullengard_mayor_5`, 80: `umar_guild04_29` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
