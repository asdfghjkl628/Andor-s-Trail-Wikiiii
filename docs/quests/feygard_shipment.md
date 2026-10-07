---
description: "Feygard errands is a quest in Andor's Trail, started by Gandoren. 15 stages, 1,000 XP in total. I met Gandoren, the guard captain at the Crossroads guardhouse. He told me about some trouble up in Loneford, that have forced the guards to be even more alert than usual. Because of this, they can't d…"
---

# Feygard errands

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_shipment` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 80, 82) |
| **Started by** | [Gandoren](../monsters/gandoren.md) |
| **NPCs involved** | [Ailshara](../monsters/ailshara.md), [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Gandoren](../monsters/gandoren.md), [Vilegard smith](../monsters/vilegard_smith.md) |
| **Locations** | [Foaming flask](../maps/foaming_flask.md), [Houseatcrossroads 0](../maps/houseatcrossroads0.md), [Vilegard smith](../maps/vilegard_smith.md) |
| **Total XP** | 1,000 |
| **Related quests** | 5 |

</div>

## Overview

> I met Gandoren, the guard captain at the Crossroads guardhouse. He told me about some trouble up in Loneford, that have forced the guards to be even more alert than usual. Because of this, they can't do their regular errands themselves but need help with some basic things.

## Prerequisites to start

Start with [Gandoren](../monsters/gandoren.md). Required:

- reached stage 10 of [Feygard errands](../quests/feygard_shipment.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Darkness in the Daylight](darkness_in_daylight.md#stage-20) | stage 20 there needs stage 82 here |
| Unlocks | [Flows through the veins](loneford.md#stage-10) | stage 10 there needs stage 25 here |
| Unlocks | [Flows through the veins](loneford.md#stage-11) | stage 11 there needs stage 25 here |
| Unlocks | [Flows through the veins](loneford.md#stage-21) | stage 21 there needs stage 25 here |
| Unlocks | [General story flags (hidden flag)](nondisplay.md#stage-18) | stage 18 there needs stage 81 here |
| Unlocks | [A creeping fear](xulviir.md#stage-20) | stage 20 there needs stage 56 here |
| Unlocks | [A creeping fear](xulviir.md#stage-30) | stage 30 there needs stage 56 here |
| Blocks | [Shadows](shadows.md#stage-10) | reaching stage 82 here closes stage 10 there |
| Blocks | [Shadows](shadows.md#stage-20) | reaching stage 82 here closes stage 20 there |
| Blocks | [Shadows](shadows.md#stage-30) | reaching stage 82 here closes stage 30 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I met Gandoren, the guard captain at the Crossroads guardhouse. He… ▸</span><span class="l">▴ less</span></summary>I met Gandoren, the guard captain at the Crossroads guardhouse. He told me about some trouble up in Loneford, that have forced the guards to be even more alert than usual. Because of this, they can't do their regular errands themselves but need help with some basic things.</details> | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Gandoren wants me to help him transport a shipment of 10 iron swords… ▸</span><span class="l">▴ less</span></summary>Gandoren wants me to help him transport a shipment of 10 iron swords to another guard post to the south.</details> | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-21"></span>[21](#route-21) | I have agreed to help Gandoren transport the shipment, as a service for Feygard. | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-22"></span>[22](#route-22) | I have grudgingly agreed to help Gandoren transport the shipment. | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-25"></span>[25](#route-25) | <details class="jt"><summary><span class="s">I should deliver the shipment to the Feygard patrol captain… ▸</span><span class="l">▴ less</span></summary>I should deliver the shipment to the Feygard patrol captain stationed in the Foaming Flask tavern.</details> | [Gandoren](../monsters/gandoren.md) | [Feygard iron sword](../items/fg_ironsword.md) |
| <span id="stage-26"></span>[26](#route-26) | <details class="jt"><summary><span class="s">Gandoren tells me that Ailshara has expressed some interest in the… ▸</span><span class="l">▴ less</span></summary>Gandoren tells me that Ailshara has expressed some interest in the Feygard shipments, and urges me to stay away from her.</details> | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Ailshara is indeed interested in the shipment, and wants me to help… ▸</span><span class="l">▴ less</span></summary>Ailshara is indeed interested in the shipment, and wants me to help Nor City with the supplies instead.</details> | [Ailshara](../monsters/ailshara.md) | – |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">If I want to help Ailshara and Nor City, I should deliver the… ▸</span><span class="l">▴ less</span></summary>If I want to help Ailshara and Nor City, I should deliver the shipment to the smith in Vilegard instead.</details> | [Ailshara](../monsters/ailshara.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I have delivered the shipment to the Feygard patrol captain in the… ▸</span><span class="l">▴ less</span></summary>I have delivered the shipment to the Feygard patrol captain in the Foaming Flask tavern. I should go tell Gandoren in the Crossroads guardhouse that the shipment is delivered.</details> | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) | – |
| <span id="stage-55"></span>[55](#route-55) | I have delivered the shipment to the smith in Vilegard. | [Vilegard smith](../monsters/vilegard_smith.md) | – |
| <span id="stage-56"></span>[56](#route-56) | <details class="jt"><summary><span class="s">The Vilegard smith gave me a shipment of degraded items that I… ▸</span><span class="l">▴ less</span></summary>The Vilegard smith gave me a shipment of degraded items that I should deliver to the Feygard patrol captain in the Foaming Flask tavern instead of the normal ones.</details> | [Vilegard smith](../monsters/vilegard_smith.md) | [Degraded Feygard iron sword](../items/fg_ironsword_d.md) |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I have delivered the shipment of degraded items to the Feygard… ▸</span><span class="l">▴ less</span></summary>I have delivered the shipment of degraded items to the Feygard patrol captain in the Foaming Flask tavern. I should go tell Gandoren in the Crossroads guardhouse that the shipment is delivered.</details> | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) | – |
| <span id="stage-80"></span>[80](#route-80) | Gandoren thanked me for helping him deliver the shipment. **(ends quest)** | [Gandoren](../monsters/gandoren.md) | 500 XP |
| <span id="stage-81"></span>[81](#route-81) | <details class="jt"><summary><span class="s">Gandoren thanked me for helping him deliver the shipment. He never… ▸</span><span class="l">▴ less</span></summary>Gandoren thanked me for helping him deliver the shipment. He never suspected anything. I should also report back to Ailshara.</details> | [Gandoren](../monsters/gandoren.md) | – |
| <span id="stage-82"></span>[82](#route-82) | I have reported back to Ailshara. **(ends quest)** | [Ailshara](../monsters/ailshara.md) | 500 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “Can you tell me again what you told me before about recent events?”

    - **Needs:** stage 10
    - *“This also means that we cannot focus as much on our usual tasks as we normally do, but instead need help with doing basic tasks just to…”*


<span id="route-20"></span>

??? note "Stage 20 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “What is the task?”

    - **Needs:** stage 20
    - *“Take this shipment of 10 iron swords to the guard captain stationed in a tavern called 'The Foaming Flask', near a village called Vilegard.”*


<span id="route-21"></span>

??? note "Stage 21 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “No problem. Anything for the glory of Feygard.”

    - **Needs:** stage 20
    - *“Excellent.”*


<span id="route-22"></span>

??? note "Stage 22 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “Fine, whatever. I will carry your stupid swords. I still hope there will be some reward for this.”

    - **Needs:** stage 20
    - *“OK then.”*


<span id="route-25"></span>

??? note "Stage 25 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), automatic

    - **Needs:** stage 22
    - **Gives:** [Feygard iron sword](../items/fg_ironsword.md)
    - *“Here is the shipment that I want you to transport.”*


<span id="route-26"></span>

??? note "Stage 26 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “I am still working on transporting that shipment.”

    - **Needs:** stage 25
    - *“I would urge you to stay away from her at all costs. Whatever you do, do not speak to her about your mission with the shipment.”*


<span id="route-30"></span>

??? note "Stage 30 · Ailshara · 1 way"

    **Way 1:** Talk to [Ailshara](../monsters/ailshara.md), choose “Can you tell me again what I was supposed to do?”

    - **Needs:** stage 35
    - *“Any help we can bring to Nor City in this matter is welcome. These items that Gandoren gave you would be useful to our people in the…”*


<span id="route-35"></span>

??? note "Stage 35 · Ailshara · 1 way"

    **Way 1:** Talk to [Ailshara](../monsters/ailshara.md), choose “Can you tell me again what I was supposed to do?”

    - **Needs:** stage 35
    - *“If you indeed are walking in the Shadow, then deliver these items to the smith in Vilegard. He will be able to make good use of them. He…”*


<span id="route-50"></span>

??? note "Stage 50 · Feygard patrol captain · 1 way"

    **Way 1:** Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md), choose “I have a shipment of iron swords from Gandoren for you.”

    - **Needs:** stage 25; hand over 10× [Feygard iron sword](../items/fg_ironsword.md)


<span id="route-55"></span>

??? note "Stage 55 · Vilegard smith · 1 way"

    **Way 1:** Talk to [Vilegard smith](../monsters/vilegard_smith.md), choose “I have a shipment of Feygard items for you.”

    - **Needs:** stage 35, 56; hand over 10× [Feygard iron sword](../items/fg_ironsword.md)
    - *“Oh, this is most unexpected but very welcome. I will not question how you acquired these items, but instead express my gratitude for…”*


<span id="route-56"></span>

??? note "Stage 56 · Vilegard smith · 1 way"

    **Way 1:** Talk to [Vilegard smith](../monsters/vilegard_smith.md), choose “I was sent to deliver these items to a Feygard patrol stationed in the Foaming Flask tavern.”

    - **Needs:** stage 55
    - **Gives:** [Degraded Feygard iron sword](../items/fg_ironsword_d.md)
    - *“Take these items and deliver them to wherever you were supposed to deliver the items you gave me.”*


<span id="route-60"></span>

??? note "Stage 60 · Feygard patrol captain · 1 way"

    **Way 1:** Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md), choose “I have a shipment of iron swords from Gandoren for you.”

    - **Needs:** stage 56; hand over 10× [Degraded Feygard iron sword](../items/fg_ironsword_d.md)


<span id="route-80"></span>

??? note "Stage 80 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “Yes. I have delivered them as you ordered.”

    - **Needs:** stage 25, 50
    - *“Splendid! Feygard is in debt to you.”*


<span id="route-81"></span>

??? note "Stage 81 · Gandoren · 1 way"

    **Way 1:** Talk to [Gandoren](../monsters/gandoren.md), choose “Yes. I have delivered them.”

    - **Needs:** stage 25, 60
    - *“Splendid! Feygard is in debt to you.”*


<span id="route-82"></span>

??? note "Stage 82 · Ailshara · 1 way"

    **Way 1:** Talk to [Ailshara](../monsters/ailshara.md), choose “Yes, it is done.”

    - **Needs:** stage 35, 55, 81
    - *“Excellent! You do indeed walk with the Shadow my friend. I am glad to hear that there are at least a few decent folk still around.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Ok then.” → “OK then.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_shipment` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 22, 25, 26, 30, 35, 50, 55, 56, 60, 80, 81, 82 |
    | Dialogue nodes setting stages | 10: `gandoren_5`, 20: `gandoren_13`, 21: `gandoren_17`, 22: `gandoren_19`, 25: `gandoren_20`, 26: `gandoren_24`, 30: `ailshara_interested_5`, 35: `ailshara_interested_8`, 50: `ff_captain_fg_items_1`, 55: `vilegard_smith_fg_1`, 56: `vilegard_smith_fg_7`, 60: `ff_captain_vg_items_1`, 80: `gandoren_deliver_y_1`, 81: `gandoren_deliver_n_1`, 82: `ailshara_deliver_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
