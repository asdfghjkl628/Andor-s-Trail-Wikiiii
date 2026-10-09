---
description: "The thorns of vengeance is a quest in Andor's Trail, started by Aryfora (stoutford_gate). 16 stages, 6,005 XP in total. Aryfora in Stoutford needs my help to prove her uncle, Blornvale, Stoutford's alchemist, killed her father."
---

# The thorns of vengeance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `thorns_vengeance` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 32, 76, 90) |
| **Started by** | [Aryfora](../monsters/stoutford_widow.md) ([Stoutford gate](../maps/stoutford_gate.md)) |
| **NPCs involved** | [Aryfora](../monsters/stoutford_widow.md), [Blornvale](../monsters/stoutford_alchemist.md#v-stoutford_alchemist2), [Blornvale](../monsters/stoutford_alchemist.md), [Tahalendor](../monsters/tahalendor.md#v-tahalendor2), [Tahalendor](../monsters/tahalendor.md) |
| **Locations** | [Stoutford church](../maps/stoutford_church.md), [Stoutford gate](../maps/stoutford_gate.md), [Stoutford potion](../maps/stoutford_potion.md) |
| **Total XP** | 6,005 |
| **Related quests** | 3 |

</div>

## Overview

> Aryfora in Stoutford needs my help to prove her uncle, Blornvale, Stoutford's alchemist, killed her father.

## Prerequisites to start

Start with [Aryfora](../monsters/stoutford_widow.md) ([Stoutford gate](../maps/stoutford_gate.md)). Required:

- reached stage 45 of [The roots of love](../quests/roots_love.md#stage-45)
- used 1× [Potion of deftness](../items/potion_deftness.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The roots of love](roots_love.md#stage-45) | stage 45 reached, for stage 10 here |
| Requires | [Rumblings](rumblings.md#stage-106) | stage 106 reached, for stage 65 here |
| Unlocks | [Stoutford story flags (hidden flag)](stn_nondisplay.md#stage-202) | stage 202 there needs stage 20 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Aryfora in Stoutford needs my help to prove her uncle, Blornvale,… ▸</span><span class="l">▴ less</span></summary>Aryfora in Stoutford needs my help to prove her uncle, Blornvale, Stoutford's alchemist, killed her father.</details> | [Aryfora](../monsters/stoutford_widow.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">She needs me to purchase three potions of the brave from Blornvale… ▸</span><span class="l">▴ less</span></summary>She needs me to purchase three potions of the brave from Blornvale and return to her.</details> | [Aryfora](../monsters/stoutford_widow.md) | spawns monsters on stoutford_sw |
| <span id="stage-30"></span>[30](#route-30) | I have returned with the three potions, and gave them to her. | [Aryfora](../monsters/stoutford_widow.md) | – |
| <span id="stage-32"></span>[32](#route-32) | I decided not to help Aryfora any further. **(ends quest)** | [Aryfora](../monsters/stoutford_widow.md) | 500 XP |
| <span id="stage-40"></span>[40](#route-40) | She gave me a potion of truth. | [Aryfora](../monsters/stoutford_widow.md) | 1× [Potion of truth](../items/potion_truth.md) |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">She wants me to give that potion to Blornvale, and make him confess… ▸</span><span class="l">▴ less</span></summary>She wants me to give that potion to Blornvale, and make him confess his crimes. I should have Tahalendor as a witness.</details> | [Aryfora](../monsters/stoutford_widow.md) | – |
| <span id="stage-60"></span>60 | I agreed to make Blornvale drink that potion. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-65"></span>[65](#route-65) | <details class="jt"><summary><span class="s">Tahalendor agreed to go with me to the alchemist's house to hear… ▸</span><span class="l">▴ less</span></summary>Tahalendor agreed to go with me to the alchemist's house to hear Blornvale's confession.</details> | [Tahalendor](../monsters/tahalendor.md) | – |
| <span id="stage-70"></span>[70](#route-70) | Blornvale drank the potion. | [Blornvale](../monsters/stoutford_alchemist.md) | 1,500 XP |
| <span id="stage-71"></span>[71](#route-71) | Tahalendor came to hear Blornvale's confession. | [Blornvale](../monsters/stoutford_alchemist.md) | spawns monsters on stoutford_potion |
| <span id="stage-72"></span>[72](#route-72) | <details class="jt"><summary><span class="s">Blornvale confessed to killing Aryfora's father. Unfortunately there… ▸</span><span class="l">▴ less</span></summary>Blornvale confessed to killing Aryfora's father. Unfortunately there is no witness.</details> | [Blornvale](../monsters/stoutford_alchemist.md) | – |
| <span id="stage-74"></span>[74](#route-74) | <details class="jt"><summary><span class="s">Blornvale now understands what I was trying to do. I will no longer… ▸</span><span class="l">▴ less</span></summary>Blornvale now understands what I was trying to do. I will no longer be able to help Aryfora get back her shop.</details> | [Blornvale](../monsters/stoutford_alchemist.md) | – |
| <span id="stage-75"></span>[75](#route-75) | <details class="jt"><summary><span class="s">Tahalendor wouldn't believe my story. I will no longer be able to… ▸</span><span class="l">▴ less</span></summary>Tahalendor wouldn't believe my story. I will no longer be able to help Aryfora get back her shop.</details> | [Blornvale](../monsters/stoutford_alchemist.md), [Tahalendor](../monsters/tahalendor.md#v-tahalendor2) | – |
| <span id="stage-76"></span>[76](#route-76) | It's all my fault that Aryfora is crying now. **(ends quest)** | [Aryfora](../monsters/stoutford_widow.md) | 5 XP |
| <span id="stage-80"></span>[80](#route-80) | Blornvale confessed to killing Aryfora's father in the presence of Tahalendor. | [Blornvale](../monsters/stoutford_alchemist.md), [Tahalendor](../monsters/tahalendor.md#v-tahalendor2) | removes monsters from stoutford_potion, removes monsters from stoutford_potion |
| <span id="stage-90"></span>[90](#route-90) | Aryfora regained her father's shop. **(ends quest)** | [Aryfora](../monsters/stoutford_widow.md) | 4,000 XP, removes monsters from stoutford_gate, spawns monsters on stoutford_potion |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “I can do it!”

    - **Needs:** reached stage 45 of [The roots of love](../quests/roots_love.md#stage-45); used 1× [Potion of deftness](../items/potion_deftness.md)
    - *“Then it's settled.”*


<span id="route-20"></span>

??? note "Stage 20 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “What will you do with them?”

    - **Needs:** stage 10
    - **Gives:** spawns monsters on stoutford_sw
    - *“That is why you must get the potions of the brave from Blornvale. Oh how I hate that name! Be quick.”*


<span id="route-30"></span>

??? note "Stage 30 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “Yes, here they are.”

    - **Needs:** stage 20; hand over 3× [Potion of the brave](../items/potion_brave.md)
    - *“Great! This will finally break him.”*


<span id="route-32"></span>

??? note "Stage 32 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “I don't quit think so. He is an honest person.”

    - **Needs:** stage 20; carry 3× [Potion of the brave](../items/potion_brave.md)
    - *“I would not have expected that from you!”*


<span id="route-40"></span>

??? note "Stage 40 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), automatic

    - **Needs:** stage 30
    - **Gives:** 1× [Potion of truth](../items/potion_truth.md)
    - *“Now I take three potions of the brave *chanting* ... add my prepared ingredients *chanting* ... shake it *chanting* ... shake it - ready.…”*


<span id="route-50"></span>

??? note "Stage 50 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “But who would believe me, a stranger?”

    - **Needs:** stage 40
    - *“Best would be Tahalendor himself. Yes, you must persuade the priest to be present when Blornvale tells the whole story.”*


<span id="route-65"></span>

??? note "Stage 65 · Tahalendor · 1 way"

    **Way 1:** Talk to [Tahalendor](../monsters/tahalendor.md), choose “Would you come with me to talk to Blornvale? He wants to confess something important.”

    - **Needs:** stage 50; not yet stage 65, 74; reached stage 106 of [Rumblings](../quests/rumblings.md#stage-106)
    - *“If I must. Well, go ahead, I'll be there when you get there.”*


<span id="route-70"></span>

??? note "Stage 70 · Blornvale · 1 way"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), choose “Yes, here. I still have one bottle of your potion of the brave.”

    - **Needs:** not yet stage 200; carry 1× [Potion of truth](../items/potion_truth.md); hand over 1× [Potion of truth](../items/potion_truth.md)
    - *“Do you see me drinking? Yes? Anything wrong? No - this potion is just perfect!”*


<span id="route-71"></span>

??? note "Stage 71 · Blornvale · 1 way"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), automatic

    - **Needs:** stage 71
    - **Gives:** spawns monsters on stoutford_potion


<span id="route-72"></span>

??? note "Stage 72 · Blornvale · 1 way"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), choose “How did you kill Aryfora's father, your own brother?”

    - **Needs:** stage 70; not yet stage 65
    - *“He was naive enough to take a potion from me. I poisoned him with the potion of Quick Death.”*


<span id="route-74"></span>

??? note "Stage 74 · Blornvale · 2 ways"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), choose “No, I poured all the rest away.”

    - **Needs:** not yet stage 200; carry 1× [Potion of truth](../items/potion_truth.md)
    - *“Then you can never prove it. That's good. Out now, leave my shop, you scum!”*

    **Way 2:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), automatic

    - **Needs:** stage 72
    - *“That was - a potion of truth! How dare you! Did you think I wouldn't recognize it?”*


<span id="route-75"></span>

??? note "Stage 75 · Blornvale, Tahalendor · 2 ways"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), automatic

    - **Needs:** stage 75
    - *“And you child, go away now and tell no more fairy tales.”*

    **Way 2:** Talk to [Tahalendor](../monsters/tahalendor.md#v-tahalendor2), choose “He lies. Can't you see?”

    - **Needs:** stage 72
    - *“And you child, go away now and tell no more fairy tales.”*


<span id="route-76"></span>

??? note "Stage 76 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), automatic

    - **Needs:** stage 76
    - *“Oh no! Now I will never get justice!”*


<span id="route-80"></span>

??? note "Stage 80 · Blornvale, Tahalendor · 2 ways"

    **Way 1:** Talk to [Blornvale](../monsters/stoutford_alchemist.md), automatic

    - **Needs:** stage 71
    - **Gives:** removes monsters from stoutford_potion, removes monsters from stoutford_potion
    - *“I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.”*

    **Way 2:** Talk to [Tahalendor](../monsters/tahalendor.md#v-tahalendor2), automatic

    - **Needs:** stage 71
    - **Gives:** removes monsters from stoutford_potion, removes monsters from stoutford_potion
    - *“I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.”*


<span id="route-90"></span>

??? note "Stage 90 · Aryfora · 1 way"

    **Way 1:** Talk to [Aryfora](../monsters/stoutford_widow.md), choose “Oh, that was just a trifle.”

    - **Needs:** stage 80
    - **Gives:** removes monsters from stoutford_gate, spawns monsters on stoutford_potion
    - *“Now I can move back into my father's house and create potions again. I will leave at once. Please come and visit me at any time.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 16 lines added |
| [v0.7.4](../versions/0.7.4.md) | Stage 71 journal text changed<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `thorns_vengeance` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 32, 40, 50, 60, 65, 70, 71, 72, 74, 75, 76, 80, 90 |
    | Dialogue nodes setting stages | 10: `stoutford_widow_roots4045_20`, 20: `stoutford_widow_thorns10_2`, 30: `stoutford_widow_thorns20_1`, 32: `stoutford_widow_thorns20_4`, 40: `stoutford_widow_thorns30_0`, 50: `stoutford_widow_thorns40_2`, 65: `tahalendor_thorns50`, 70: `blornvale_thorns50_30`, 71: `blornvale_thorns70_20`, 72: `blornvale_thorns70_12`, 74: `blornvale_thorns50_22`, 74: `blornvale_thorns72_10`, 75: `blornvale_thorns72_90`, 76: `stoutford_widow_thorns74_1`, 80: `blornvale_thorns70_30`, 90: `stoutford_widow_thorns80_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
