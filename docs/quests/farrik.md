---
description: "Night visit is a quest in Andor's Trail, started by Farrik (fallhaven_derelict2). 11 stages, 3,200 XP in total. Farrik in the Fallhaven Thieves' Guild told me of a plan to help a fellow thief escape from the Fallhaven jail."
---

# Night visit

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `farrik` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 70, 90) |
| **Started by** | [Farrik](../monsters/farrik.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Farrik](../monsters/farrik.md), [Guard captain](../monsters/warden.md), [Thieves guild cook](../monsters/thieves_guild_cook.md) |
| **Locations** | [Fallhaven derelict 2](../maps/fallhaven_derelict2.md), [Fallhaven derelict 2 t](../maps/fallhaven_derelict2_t.md), [Fallhaven prison](../maps/fallhaven_prison.md) |
| **Total XP** | 3,200 |
| **Related quests** | 4 |

</div>

## Overview

> Farrik in the Fallhaven Thieves' Guild told me of a plan to help a fellow thief escape from the Fallhaven jail.

## Prerequisites to start

None: talk to [Farrik](../monsters/farrik.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Beer Bootlegging](beer_bootlegging.md#stage-50) | stage 50 there needs stage 70 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-17) | stage 17 there needs stage 90 here |
| Unlocks | [A path to the Duleian Road](pathway_fallhaven.md#stage-20) | stage 20 there needs stage 60 here |
| Unlocks | [Rumblings](rumblings.md#stage-25) | stage 25 there needs stage 70 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Farrik in the Fallhaven Thieves' Guild told me of a plan to help a… ▸</span><span class="l">▴ less</span></summary>Farrik in the Fallhaven Thieves' Guild told me of a plan to help a fellow thief escape from the Fallhaven jail.</details> | [Farrik](../monsters/farrik.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Farrik in the Fallhaven Thieves' Guild told me the details of the… ▸</span><span class="l">▴ less</span></summary>Farrik in the Fallhaven Thieves' Guild told me the details of the plan, and I accepted the task of helping him. The guard captain apparently has a drinking problem. The plan is that I get a prepared mead from the cook in the Thieves' Guild that will knock out the guard captain in the jail. I might be required to bribe the guard captain.</details> | [Farrik](../monsters/farrik.md) | – |
| <span id="stage-25"></span>[25](#route-25) | I got the prepared mead from the cook in the Thieves' Guild. | [Thieves guild cook](../monsters/thieves_guild_cook.md) | [Prepared sleepy mead](../items/sleepingmead.md) |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I told Farrik that I don't fully agree with their plan. I might tell… ▸</span><span class="l">▴ less</span></summary>I told Farrik that I don't fully agree with their plan. I might tell the guard captain about their shady plan.</details> | [Farrik](../monsters/farrik.md) | – |
| <span id="stage-32"></span>[32](#route-32) | I have given the prepared mead to the guard captain. | [Guard captain](../monsters/warden.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I have told the guard captain of the plan that the thieves have to… ▸</span><span class="l">▴ less</span></summary>I have told the guard captain of the plan that the thieves have to release their friend.</details> | [Guard captain](../monsters/warden.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">The guard captain wants me to tell the thieves that the security… ▸</span><span class="l">▴ less</span></summary>The guard captain wants me to tell the thieves that the security will be lowered for tonight. We might be able to catch some of the thieves.</details> | [Guard captain](../monsters/warden.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I managed to bribe the guard captain into drinking the prepared… ▸</span><span class="l">▴ less</span></summary>I managed to bribe the guard captain into drinking the prepared mead. He should be out during the night allowing the thieves to break their friend free.</details> | [Guard captain](../monsters/warden.md) | – |
| <span id="stage-70"></span>[70](#route-70) | Farrik rewarded me for helping the Thieves' Guild. **(ends quest)** | [Farrik](../monsters/farrik.md) | 1,500 XP, removes monsters from fallhaven_prison |
| <span id="stage-80"></span>[80](#route-80) | I have told Farrik that the security will be lowered tonight. | [Farrik](../monsters/farrik.md) | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">The guard captain thanked me for helping him plan to catch the… ▸</span><span class="l">▴ less</span></summary>The guard captain thanked me for helping him plan to catch the thieves. He said he will also tell other guards that I helped him.</details> **(ends quest)** | [Guard captain](../monsters/warden.md) | 1,700 XP, [Gold coins](../items/gold.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Farrik · 1 way"

    **Way 1:** Talk to [Farrik](../monsters/farrik.md), choose “What did he do?”

    - *“I guess I can trust you with this secret. We are planning a mission tonight to help him out of jail.”*


<span id="route-20"></span>

??? note "Stage 20 · Farrik · 1 way"

    **Way 1:** Talk to [Farrik](../monsters/farrik.md), choose “I am not done yet, but I am working on it.”

    - **Needs:** stage 20; not yet stage 30
    - *“Good. Report back to me when you have gotten the guard captain to drink that special mead.”*


<span id="route-25"></span>

??? note "Stage 25 · Thieves guild cook · 1 way"

    **Way 1:** Talk to [Thieves guild cook](../monsters/thieves_guild_cook.md), choose “Farrik said you can prepare me a round of special mead.”

    - **Needs:** stage 20
    - **Gives:** [Prepared sleepy mead](../items/sleepingmead.md)
    - *“There. This should do it. Here you go.”*


<span id="route-30"></span>

??? note "Stage 30 · Farrik · 1 way"

    **Way 1:** Talk to [Farrik](../monsters/farrik.md), choose “Maybe I should tell the guards that you are planning to get him out?”

    - **Needs:** not yet stage 20
    - *“Whatever, they wouldn't believe you anyway.”*


<span id="route-32"></span>

??? note "Stage 32 · Guard captain · 1 way"

    **Way 1:** Talk to [Guard captain](../monsters/warden.md), choose “I brought some with me if you would like to have a sip.”

    - **Needs:** stage 20, 25; hand over 1× [Prepared sleepy mead](../items/sleepingmead.md)
    - *“Oh sweet drinks of joy. I really shouldn't have this while on duty though.”*


<span id="route-40"></span>

??? note "Stage 40 · Guard captain · 1 way"

    **Way 1:** Talk to [Guard captain](../monsters/warden.md), choose “I heard they are planning his escape tonight.”

    - **Needs:** stage 30
    - *“Tonight? Thank you for this information. We will make sure to increase the security tonight then, but in such a way that they won't notice.”*


<span id="route-50"></span>

??? note "Stage 50 · Guard captain · 1 way"

    **Way 1:** Talk to [Guard captain](../monsters/warden.md), choose “No, not yet. I'm working on it.”

    - **Needs:** stage 50
    - *“Good. Report back to me when you have told them.”*


<span id="route-60"></span>

??? note "Stage 60 · Guard captain · 1 way"

    **Way 1:** Talk to [Guard captain](../monsters/warden.md), choose “I have 500 gold right here that you could have.”

    - **Needs:** stage 32; pay 500 gold
    - *“Wow, that much gold? I'm sure I could even get away with this without being fined. Then I could have the gold AND a nice drink of mead at…”*


<span id="route-70"></span>

??? note "Stage 70 · Farrik · 1 way"

    **Way 1:** Talk to [Farrik](../monsters/farrik.md), choose “It is done. He should be no problem during the night.”

    - **Needs:** stage 20, 60; not yet stage 30
    - **Gives:** removes monsters from fallhaven_prison
    - *“That is good news! Now we should be able to get our friend out from jail tonight.”*


<span id="route-80"></span>

??? note "Stage 80 · Farrik · 1 way"

    **Way 1:** Talk to [Farrik](../monsters/farrik.md), choose “[Lie]. No. I went there, but I overheard the guard captain saying there was no real threat, so they will…”

    - **Needs:** stage 30, 50; not yet stage 20
    - *“That's very useful information. Well done. You have my thanks, friend.”*


<span id="route-90"></span>

??? note "Stage 90 · Guard captain · 1 way"

    **Way 1:** Talk to [Guard captain](../monsters/warden.md), choose “Yes, they won't expect a thing.”

    - **Needs:** stage 50, 80
    - **Gives:** [Gold coins](../items/gold.md)
    - *“Great. Thank you for your help. Here, take these coins as a token of our appreciation.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Dialogue: 1 line changed |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Oh you did? Well done. You have my thanks, friend.” → “That's very useful information. Well done. You have my thanks, friend.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `farrik` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 32, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `farrik_11`, 20: `farrik_23`, 25: `thievesguild_cook_8`, 30: `farrik_15`, 32: `fallhaven_warden_4`, 40: `fallhaven_warden_21`, 50: `fallhaven_warden_25`, 60: `fallhaven_warden_9`, 70: `farrik_24`, 80: `farrik_26`, 90: `fallhaven_warden_31` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
