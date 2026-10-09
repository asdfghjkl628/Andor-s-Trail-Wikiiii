---
description: "Mine for the taking is a quest in Andor's Trail, started by stepping on a trigger on graveyard0. 13 stages, 5,500 XP in total. I stumbled across a treasure chest in a clearing south of the Waterway house but the chest is protected by some form of magic and cannot be opened."
---

# Mine for the taking

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `graveyard_quest` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 90, 95, 100, 105) |
| **Started by** | stepping on a trigger on [Graveyard 0](../maps/graveyard0.md) |
| **NPCs involved** | [Graveyard king](../monsters/graveyardking.md), [Hagale](../monsters/algore.md), [Waterway traveler](../monsters/graveyard_traveler.md) |
| **Locations** | [Graveyard 0](../maps/graveyard0.md), [Graveyard 1](../maps/graveyard1.md), [Woodsettlement 0](../maps/woodsettlement0.md) |
| **Total XP** | 5,500 |

</div>

## Overview

> I stumbled across a treasure chest in a clearing south of the Waterway house but the chest is protected by some form of magic and cannot be opened.

## Prerequisites to start

Start with stepping on a trigger on [Graveyard 0](../maps/graveyard0.md). Required:

- NOT reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80)
- NOT reached stage 70 of [Mine for the taking](../quests/graveyard_quest.md#stage-70)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I stumbled across a treasure chest in a clearing south of the… ▸</span><span class="l">▴ less</span></summary>I stumbled across a treasure chest in a clearing south of the Waterway house but the chest is protected by some form of magic and cannot be opened.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard 0](../maps/graveyard0.md).</span> | stepping on a trigger on [Graveyard 0](../maps/graveyard0.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I encountered a traveler a short distance from the treasure chest.… ▸</span><span class="l">▴ less</span></summary>I encountered a traveler a short distance from the treasure chest. He told me there is a legend that the key to the chest is held by one of the undead that roam the cemetery to the south of the chest. However, the entrance to the cemetery is sealed by a magical force.</details> | [Waterway traveler](../monsters/graveyard_traveler.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">The traveler told me that Hagale in the Wood settlement might know… ▸</span><span class="l">▴ less</span></summary>The traveler told me that Hagale in the Wood settlement might know how to enter the cemetery.</details> | [Waterway traveler](../monsters/graveyard_traveler.md) | – |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">I went to the Wood settlement and found Hagale. He was a drunk mess… ▸</span><span class="l">▴ less</span></summary>I went to the Wood settlement and found Hagale. He was a drunk mess and would not speak to me unless I brought him two Lowyna's special brew.</details> | [Hagale](../monsters/algore.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">Hagale said that the entrance to the cemetery was also sealed with… ▸</span><span class="l">▴ less</span></summary>Hagale said that the entrance to the cemetery was also sealed with magic to safeguard the key to the chest. The seal can only be broken by defeating the undead monster. However, Hagale found an ancient text that allows the holder to temporarily enter the cemetery. Hagale gave me the text.</details> | [Hagale](../monsters/algore.md) | 1× [Ancient text](../items/graveyardtext.md) |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I returned to the cemetery and was able to enter it using the… ▸</span><span class="l">▴ less</span></summary>I returned to the cemetery and was able to enter it using the ancient text just as Hagale had claimed.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Graveyard 1](../maps/graveyard1.md).</span> | walking into a blocked passage on [Graveyard 1](../maps/graveyard1.md) | 500 XP, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1 |
| <span id="stage-60"></span>[60](#route-60) | I hacked through a horde of undead until I encountered one wearing a key. | [Graveyard king](../monsters/graveyardking.md) | – |
| <span id="stage-70"></span>[70](#route-70) | I killed the undead and took the key.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard 1](../maps/graveyard1.md).</span> | stepping on a trigger on [Graveyard 1](../maps/graveyard1.md) | – |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">I opened the chest, which contained a powerful sword. Next time I'm… ▸</span><span class="l">▴ less</span></summary>I opened the chest, which contained a powerful sword. Next time I'm in the Wood settlement I should see if Hagale is still around.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard 0](../maps/graveyard0.md).</span> | stepping on a trigger on [Graveyard 0](../maps/graveyard0.md) | 2,500 XP, 1× [LifeTaker](../items/lifetaker.md) |
| <span id="stage-90"></span>[90](#route-90) | Hagale tried to rob me and take the sword, but I killed him and took it back. **(ends quest)** | [Hagale](../monsters/algore.md) | – |
| <span id="stage-95"></span>[95](#route-95) | <details class="jt"><summary><span class="s">Hagale tried to rob me and take the sword. He lost his wife and… ▸</span><span class="l">▴ less</span></summary>Hagale tried to rob me and take the sword. He lost his wife and daughter and wasn't thinking straight. I gave him the sword without a fight.</details> **(ends quest)** | [Hagale](../monsters/algore.md) | 1,500 XP |
| <span id="stage-100"></span>[100](#route-100) | <details class="jt"><summary><span class="s">Hagale wanted some of the gold I got from selling the sword. It… ▸</span><span class="l">▴ less</span></summary>Hagale wanted some of the gold I got from selling the sword. It seemed fair to give him a share.</details> **(ends quest)** | [Hagale](../monsters/algore.md) | 1,000 XP |
| <span id="stage-105"></span>[105](#route-105) | <details class="jt"><summary><span class="s">Hagale tried to rob me of the gold I got from selling the sword. I… ▸</span><span class="l">▴ less</span></summary>Hagale tried to rob me of the gold I got from selling the sword. I had no choice but to kill him.</details> **(ends quest)** | [Hagale](../monsters/algore.md) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · stepping on a trigger on graveyard0 · 1 way"

    **Way 1:** Stepping on a trigger on [Graveyard 0](../maps/graveyard0.md), choose “Nothing my weapon couldn't handle.”

    - **Needs:** not yet stage 70, 80
    - *“Multiple strikes from your weapon do not damage the chest. The chest is protected by some form of magic.”*


<span id="route-20"></span>

??? note "Stage 20 · Waterway traveler · 1 way"

    **Way 1:** Talk to [Waterway traveler](../monsters/graveyard_traveler.md), choose “Yes.”

    - **Needs:** stage 10; not yet stage 40
    - *“That chest is something of a local legend. Been there for generations. They say it is sealed with magic and can only be opened with a…”*


<span id="route-30"></span>

??? note "Stage 30 · Waterway traveler · 1 way"

    **Way 1:** Talk to [Waterway traveler](../monsters/graveyard_traveler.md), choose “Interesting. Is there anything else you can tell me about the chest or cemetery?”

    - **Needs:** stage 10; not yet stage 40
    - *“That is all I know ... Come to think of it ... Hagale from the Wood Settlement was out here a few weeks ago asking about the chest.…”*


<span id="route-35"></span>

??? note "Stage 35 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “I heard you were interested in that unattended treasure chest by the Waterway house.”

    - **Needs:** stage 30; not yet stage 40
    - *“Oh yeah? What's it to you kid? ... BURP ... If you want to know, it will cost you two bottles of Lowyna's special brew.”*


<span id="route-40"></span>

??? note "Stage 40 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “I'm sorry for your losses. You have suffered a lot. I want to finish what you started. Do you still have…”

    - **Needs:** stage 35; not yet stage 40; hand over 2× [Lowyna's special brew](../items/drink_lowyn2.md)
    - **Gives:** 1× [Ancient text](../items/graveyardtext.md)
    - *“[Hagale finishes the second bottle of Lowyna's special brew] Sure do. I hope you know what you're doing kid.”*


<span id="route-50"></span>

??? note "Stage 50 · walking into a blocked passage on graveyard1 · 1 way"

    **Way 1:** Walking into a blocked passage on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** stage 40; not yet stage 70; carry 1× [Ancient text](../items/graveyardtext.md)
    - **Gives:** spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1
    - *“The text begins to radiate light. The ground begins to shake as darkness fills the sky. A loud cracking sound is followed by a rush of…”*


<span id="route-60"></span>

??? note "Stage 60 · Graveyard king · 1 way"

    **Way 1:** Talk to [Graveyard king](../monsters/graveyardking.md), automatic

    - *“[You notice this undead is wearing a key around its neck]”*


<span id="route-70"></span>

??? note "Stage 70 · stepping on a trigger on graveyard1 · 1 way"

    **Way 1:** Stepping on a trigger on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** killed 1× [Graveyard king](../monsters/graveyardking.md)


<span id="route-80"></span>

??? note "Stage 80 · stepping on a trigger on graveyard0 · 1 way"

    **Way 1:** Stepping on a trigger on [Graveyard 0](../maps/graveyard0.md), choose “I have the key right here.”

    - **Needs:** stage 70; not yet stage 80; hand over 1× [Graveyard key](../items/graveyardkey.md)
    - **Gives:** 1× [LifeTaker](../items/lifetaker.md)
    - *“You open the chest and discover a powerful sword infused with unholy magic.”*


<span id="route-90"></span>

??? note "Stage 90 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “I went through hell to get this sword. I won't give it to you without a fight.”

    - **Needs:** stage 80; not yet stage 90, 95, 100, 105; carry 1× [LifeTaker](../items/lifetaker.md)
    - *“Let's go.”*


<span id="route-95"></span>

??? note "Stage 95 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “I went through a lot to get this sword ... but you suffered more than me. I won't fight you. If you want it…”

    - **Needs:** stage 80; not yet stage 90, 95, 100, 105; hand over 1× [LifeTaker](../items/lifetaker.md)
    - *“Alright hand it over. Be quick about it.”*


<span id="route-100"></span>

??? note "Stage 100 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “OK, OK. I guess it's fair that you should get a share. Here's 1,000 gold.”

    - **Needs:** stage 80; not yet stage 90, 95, 100, 105; not carry 1× [LifeTaker](../items/lifetaker.md); not wearing [LifeTaker](../items/lifetaker.md); pay 1,000 gold
    - *“Thanks kid. It's good to see you have some honor.”*


<span id="route-105"></span>

??? note "Stage 105 · Hagale · 1 way"

    **Way 1:** Talk to [Hagale](../monsters/algore.md), choose “No way! I fought to get the sword, and the profit is mine!”

    - **Needs:** stage 80; not yet stage 90, 95, 100, 105; not carry 1× [LifeTaker](../items/lifetaker.md); not wearing [LifeTaker](../items/lifetaker.md)
    - *“We'll see about that.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 14 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 2 lines changed<br>· text: “Lets go.” → “Let's go.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `graveyard_quest` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 60, 70, 80, 90, 95, 100, 105 |
    | Dialogue nodes setting stages | 10: `graveyard_quest4`, 20: `graveyardtraveler_20`, 30: `graveyardtraveler_50`, 35: `algore_10`, 40: `algore_87`, 50: `graveyardwall_2`, 60: `graveyardking_1`, 70: `graveyardbosskill_20`, 80: `graveyard_quest_end`, 90: `algore_99a`, 95: `algore_99b`, 100: `algore_99g`, 100: `algore_99h`, 105: `algore_99i` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
