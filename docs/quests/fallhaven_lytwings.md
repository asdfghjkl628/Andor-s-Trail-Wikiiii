---
description: "It's knot funny is a quest in Andor's Trail, started by Arensia (fallhaven_sw). 19 stages, 300 XP in total. I met Arensia in Fallhaven. She is being taunted by lytwings while she slumbers. I agreed to help get rid of the mischevious creatures. I should talk to Rigmor to find out more, she lives n…"
---

# It's knot funny

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fallhaven_lytwings` |
| **In journal** | Yes |
| **Stages** | 19 (completes at 101, 102, 103) |
| **Started by** | [Arensia](../monsters/arensia.md) ([Fallhaven south-west](../maps/fallhaven_sw.md)) |
| **NPCs involved** | [Arensia](../monsters/arensia.md), [Lytwing](../monsters/lytwing_fallhaven.md), [Rigmor](../monsters/rigmor.md) |
| **Locations** | [Fallhaven south-west](../maps/fallhaven_sw.md), [Gapfiller 2](../maps/gapfiller2.md) |
| **Total XP** | 300 |

</div>

## Overview

> I met Arensia in Fallhaven. She is being taunted by lytwings while she slumbers. I agreed to help get rid of the mischevious creatures. I should talk to Rigmor to find out more, she lives north of the tavern.

## Prerequisites to start

Start with [Arensia](../monsters/arensia.md) ([Fallhaven south-west](../maps/fallhaven_sw.md)). Required:

- NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1)
- NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12)
- latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | <details class="jt"><summary><span class="s">I met Arensia in Fallhaven. She is being taunted by lytwings while… ▸</span><span class="l">▴ less</span></summary>I met Arensia in Fallhaven. She is being taunted by lytwings while she slumbers. I agreed to help get rid of the mischevious creatures. I should talk to Rigmor to find out more, she lives north of the tavern.</details> | [Arensia](../monsters/arensia.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Rigmor told me that lytwings live near large rings of mushroom… ▸</span><span class="l">▴ less</span></summary>Rigmor told me that lytwings live near large rings of mushroom growth, I should look for these in the forest surrounding Fallhaven.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Gapfiller 2](../maps/gapfiller2.md).</span> | [Rigmor](../monsters/rigmor.md) | – |
| <span id="stage-11"></span>[11](#route-11) | <details class="jt"><summary><span class="s">I have to take a gift of two red apples and two strawberries before… ▸</span><span class="l">▴ less</span></summary>I have to take a gift of two red apples and two strawberries before I can talk to the lytwings. They cast some kind of spell on me for not bringing them these fruit, it made me feel very tired.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | applies condition fatigue_minor |
| <span id="stage-12"></span>[12](#route-12) | The lytwings accepted my gift, and I can now talk with them. | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-13"></span>[13](#route-13) | <details class="jt"><summary><span class="s">I offered my help to the lytwings in exchange for leaving Arensia… ▸</span><span class="l">▴ less</span></summary>I offered my help to the lytwings in exchange for leaving Arensia alone. They are considering my request. I should check in with them shortly, to hear their decision.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The lytwings asked that I chop down a gnarly old tree that is inside… ▸</span><span class="l">▴ less</span></summary>The lytwings asked that I chop down a gnarly old tree that is inside their mushroom ring. They insisted that I use an iron axe because the cursed bark of the tree cannot be cut by other tools.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-21"></span>[21](#route-21) | <details class="jt"><summary><span class="s">I was about to swing my axe, when the lytwings stopped me. They have… ▸</span><span class="l">▴ less</span></summary>I was about to swing my axe, when the lytwings stopped me. They have changed their minds about chopping down the tree. I am beginning to think they are indecisive on purpose.</details> | reading a sign on [Gapfiller 2](../maps/gapfiller2.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">The lytwings want four bottles of mead. I can probably find some at… ▸</span><span class="l">▴ less</span></summary>The lytwings want four bottles of mead. I can probably find some at the Fallhaven tavern.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-31"></span>[31](#route-31) | <details class="jt"><summary><span class="s">They took the mead, and turned around saying they want something… ▸</span><span class="l">▴ less</span></summary>They took the mead, and turned around saying they want something else. I can now see why Rigmor said they are full of mischief! But I have no other choice but to continue this fool's errand if I want to help Arensia.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I have to find twelve wild flowers for the lytwings. I wonder where… ▸</span><span class="l">▴ less</span></summary>I have to find twelve wild flowers for the lytwings. I wonder where I could find those. Perhaps Arensia will know.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Wild 10](../maps/wild10.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Wild 11](../maps/wild11.md).</span> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-41"></span>[41](#route-41) | <details class="jt"><summary><span class="s">They accepted the flowers, and as expected, said they want something… ▸</span><span class="l">▴ less</span></summary>They accepted the flowers, and as expected, said they want something else! How many more times will they make me run around?</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">The lytwings want a token of Arensia's promise that she will not to… ▸</span><span class="l">▴ less</span></summary>The lytwings want a token of Arensia's promise that she will not to pick their mushrooms again. I sense they are not playing another prank this time, they seemed intent about this task.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-91"></span>[91](#route-91) | <details class="jt"><summary><span class="s">Arensia made a promise to her mother's ring, and then she gave it to… ▸</span><span class="l">▴ less</span></summary>Arensia made a promise to her mother's ring, and then she gave it to me. I should take it to the lytwings at once.</details> | [Arensia](../monsters/arensia.md) | 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md) |
| <span id="stage-92"></span>[92](#route-92) | <details class="jt"><summary><span class="s">I gave Arensia's ring to the lytwings. Just when I thought it was… ▸</span><span class="l">▴ less</span></summary>I gave Arensia's ring to the lytwings. Just when I thought it was done, they said they need something else! I am waiting on their decision.</details> | [Lytwing](../monsters/lytwing_fallhaven.md) | – |
| <span id="stage-99"></span>[99](#route-99) | The lytwings have agreed to stop taunting Arensia. I should go tell her. | [Lytwing](../monsters/lytwing_fallhaven.md) | 1× [Arensia's Ring of Promise](../items/ring_of_promise.md) |
| <span id="stage-100"></span>[100](#route-100) | Arensia was elated to hear that the lytwings will no longer taunt her. | [Arensia](../monsters/arensia.md) | 300 XP |
| <span id="stage-101"></span>[101](#route-101) | <details class="jt"><summary><span class="s">I could not take the absurd errands any more. I am no longer helping… ▸</span><span class="l">▴ less</span></summary>I could not take the absurd errands any more. I am no longer helping Arensia with her lytwing problem.</details> **(ends quest)** | [Arensia](../monsters/arensia.md) | – |
| <span id="stage-102"></span>[102](#route-102) | I lied to Arensia's and kept her mother's ring for myself. **(ends quest)** | [Arensia](../monsters/arensia.md) | – |
| <span id="stage-103"></span>[103](#route-103) | Arensia gave me her magical promise ring as reward for helping her. **(ends quest)** | [Arensia](../monsters/arensia.md) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “Not yet. I still need to go talk with Rigmor to find out more.”

    - **Needs:** not yet stage 1, 12; latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1
    - *“You should talk to Rigmor, as she knows more about the lytwings than I do. She lives here in Fallhaven, just go north past the tavern.”*


<span id="route-10"></span>

??? note "Stage 10 · Rigmor · 1 way"

    **Way 1:** Talk to [Rigmor](../monsters/rigmor.md), choose “Where can I find lytwings?”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1
    - *“Lytwings gather near fairy rings. I suggest that you look for large mushroom patches in the woodland surrounding Fallhaven.”*


<span id="route-11"></span>

??? note "Stage 11 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “I did not, sorry.”

    - **Needs:** not yet stage 12
    - **Gives:** applies condition fatigue_minor
    - *“Bring us two red apples and two strawberries. Since you came without a gift, we cast on you a mystical Lytwing spell!”*


<span id="route-12"></span>

??? note "Stage 12 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Yes, here are two red apples and two strawberries.”

    - **Needs:** not yet stage 12; hand over 2× [Red apple](../items/apple_red.md); hand over 2× [Strawberry](../items/strawberry.md)
    - *“Wonderful! These strawberries are so sweet. You may stay!”*


<span id="route-13"></span>

??? note "Stage 13 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Don't be mad, I am just trying to help. Is there anything I can do to make this right?”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12) is 12
    - <small>Also: starts timer “lytwing_fallhaven_timer”</small>
    - *“Hmmm, let us discuss this amongst ourselves. Can you give us a minute alone?”*


<span id="route-20"></span>

??? note "Stage 20 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), automatic

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20) is 20
    - *“Please chop down this gnarly old tree inside our fairy circle. Can you do that for us?”*


<span id="route-21"></span>

??? note "Stage 21 · reading a sign on gapfiller2 · 1 way"

    **Way 1:** Reading a sign on [Gapfiller 2](../maps/gapfiller2.md)

    - **Needs:** stage 20; not yet stage 30; carry 1× [Iron axe](../items/axe2.md)
    - *“Hey wait! We changed our minds. We like that tree and want to keep it.”*


<span id="route-30"></span>

??? note "Stage 30 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), automatic

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-21) is 21
    - *“We are having a celebration, please get us four bottles of mead. [giggle]”*


<span id="route-31"></span>

??? note "Stage 31 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Yes, here is your mead.”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30) is 30; hand over 4× [Mead](../items/mead.md)
    - *“Wonderful!”*


<span id="route-40"></span>

??? note "Stage 40 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), automatic

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-31) is 31
    - *“For our celebrations, we would like a dozen wild flowers.”*


<span id="route-41"></span>

??? note "Stage 41 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Yes, here are your flowers.”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40; hand over 12× [Wild Flower](../items/wild_flower.md)
    - *“These are perfect. Thank you!”*


<span id="route-90"></span>

??? note "Stage 90 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “OK?”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-41) is 41
    - *“We want Arensia to promise not to pick our mushrooms again. And we want proof!”*


<span id="route-91"></span>

??? note "Stage 91 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “I hope this works.”

    - **Needs:** not yet stage 1, 99; latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90
    - **Gives:** 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md)
    - *“I made a promise to the ring, here take it to the lytwings!”*


<span id="route-92"></span>

??? note "Stage 92 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Yes, here is her promise ring.”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90; hand over 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md)
    - *“This will do just fine, thank you $playername.”*


<span id="route-99"></span>

??? note "Stage 99 · Lytwing · 1 way"

    **Way 1:** Talk to [Lytwing](../monsters/lytwing_fallhaven.md), choose “Oh how wonderful. Thank you forest lytwings!”

    - **Needs:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-92) is 92
    - **Gives:** 1× [Arensia's Ring of Promise](../items/ring_of_promise.md)
    - *“However, we have no need for a human ring. We embued it with our magical powers. Please take this ring back to Arensia.”*


<span id="route-100"></span>

??? note "Stage 100 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “You seem tired. Is everything alright?”

    - **Needs:** stage 100; not yet stage 1, 102
    - *“I cannot thank you enough, $playername. You have saved my sanity!”*


<span id="route-101"></span>

??? note "Stage 101 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “Yes, I want to quit.”

    - **Needs:** not yet stage 1, 99; latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40
    - *“I appreciate your help either way.”*


<span id="route-102"></span>

??? note "Stage 102 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “Unfortunately they kept your mother's ring (Lie).”

    - **Needs:** stage 100; not yet stage 1, 102
    - *“That is okay. I did not expect to get it back.”*


<span id="route-103"></span>

??? note "Stage 103 · Arensia · 1 way"

    **Way 1:** Talk to [Arensia](../monsters/arensia.md), choose “They used their magic on your ring, and asked that I give it back to you.”

    - **Needs:** stage 100; not yet stage 1, 102
    - *“After everything you have done for me ... I want you to keep it. Please, I insist!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 19 lines added |
| [v0.8.13](../versions/0.8.13.md) | Stage 21 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fallhaven_lytwings` |
    | showInLog | 1 |
    | Stage IDs | 1, 10, 11, 12, 13, 20, 21, 30, 31, 40, 41, 90, 91, 92, 99, 100, 101, 102, 103 |
    | Dialogue nodes setting stages | 1: `arensia_lytwing_33`, 10: `rigmor_lytwing_5`, 11: `lytwing_fallhaven_4`, 12: `lytwing_fallhaven_5`, 13: `lytwing_fallhaven_9`, 20: `lytwing_fallhaven_14`, 21: `lytwing_fallhaven_16`, 30: `lytwing_fallhaven_17`, 31: `lytwing_fallhaven_19`, 40: `lytwing_fallhaven_22`, 41: `lytwing_fallhaven_24`, 90: `lytwing_fallhaven_28`, 91: `arensia_lytwing_21`, 92: `lytwing_fallhaven_32`, 99: `lytwing_fallhaven_37`, 100: `arensia_lytwing_24`, 101: `arensia_lytwing_17`, 102: `arensia_lytwing_25`, 103: `arensia_lytwing_26` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
