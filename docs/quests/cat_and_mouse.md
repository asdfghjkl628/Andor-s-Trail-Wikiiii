---
description: "A cat and mouse game is a quest in Andor's Trail, started by Seviron (brimhaven_church). 9 stages, 2,500 XP in total. I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks."
---

# A cat and mouse game

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `cat_and_mouse` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 70, 90) |
| **Started by** | [Seviron](../monsters/brv_churchman.md) ([Brimhaven church](../maps/brimhaven_church.md)) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Seviron](../monsters/brv_churchman.md) |
| **Locations** | [Brimhaven church](../maps/brimhaven_church.md), [Brimhaven church upstairs](../maps/brimhaven_church_upstairs.md), [Brimhaven general 1](../maps/brimhaven_general1.md) |
| **Total XP** | 2,500 |
| **Related quests** | 1 |

</div>

## Overview

> I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks.

## Prerequisites to start

Start with [Seviron](../monsters/brv_churchman.md) ([Brimhaven church](../maps/brimhaven_church.md)). Required:

- NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10)
- NOT reached stage 30 of nondisplay bhvt (flag not defined in the game data)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Brimhaven story flags 2 (hidden flag)](brv_nondisplay2.md#stage-60) | stage 60 there needs stage 60 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I agreed to help Seviron trap the mouse that the cat cannot catch. I… ▸</span><span class="l">▴ less</span></summary>I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks.</details> | [Seviron](../monsters/brv_churchman.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I have given Seviron the rocks. | [Seviron](../monsters/brv_churchman.md) | – |
| <span id="stage-30"></span>[30](#route-30) | I have given Seviron the cheese. | [Seviron](../monsters/brv_churchman.md) | – |
| <span id="stage-40"></span>[40](#route-40) | I obtained a suitable bottle from Arlish. | [Arlish](../monsters/arlish.md) | [Large empty bottle](../items/large_bottle.md) |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I have given Seviron the bottle. Seviron will set the trap, but it… ▸</span><span class="l">▴ less</span></summary>I have given Seviron the bottle. Seviron will set the trap, but it may take some time to catch the mouse. I should come back later.</details> | [Seviron](../monsters/brv_churchman.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">The mouse has been caught! Seviron gave it to me in the bottle. He… ▸</span><span class="l">▴ less</span></summary>The mouse has been caught! Seviron gave it to me in the bottle. He said I can decide what to do with it.</details> | [Seviron](../monsters/brv_churchman.md) | [Trapped mouse](../items/trapped_mouse.md), [Gold coins](../items/gold.md) |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">I decided to give the mouse to the cat. The cat would have… ▸</span><span class="l">▴ less</span></summary>I decided to give the mouse to the cat. The cat would have eventually killed it anyway.</details> **(ends quest)** | [Seviron](../monsters/brv_churchman.md) | 1,000 XP, [Large empty bottle](../items/large_bottle.md) |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">I decided to release the mouse outside. Seviron told me to do that… ▸</span><span class="l">▴ less</span></summary>I decided to release the mouse outside. Seviron told me to do that outside the town.</details> | [Seviron](../monsters/brv_churchman.md) | – |
| <span id="stage-90"></span>[90](#route-90) | I released the mouse. **(ends quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 7](../maps/brimhaven7.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven exit](../maps/brimhaven_exit.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterway 12](../maps/waterway12.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 3](../maps/waytobrimhaven3.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven 6](../maps/waytobrimhaven6.md).</span> | stepping on a trigger on [Brimhaven 7](../maps/brimhaven7.md) | 1,500 XP, [Large empty bottle](../items/large_bottle.md) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Seviron · 1 way"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “OK. I'll help.”

    - **Needs:** not yet stage 10; not reached stage 30 of nondisplay bhvt (flag not defined in the game data)
    - *“Thanks. Just bring me the items. I think three rocks should be enough.”*


<span id="route-20"></span>

??? note "Stage 20 · Seviron · 2 ways"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I have the rocks.”

    - **Needs:** stage 10, 20; not yet stage 20, 30; hand over 3× [Small rock](../items/rock.md); not carry 1× [Cheese](../items/cheese.md)
    - *“Thanks. Now we just need the cheese and the bottle.”*

    **Way 2:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I have the rocks.”

    - **Needs:** stage 10, 20, 30; not yet stage 20, 30; hand over 3× [Small rock](../items/rock.md)
    - *“Thanks. Now we just need the bottle. You should ask around town. Someone must have one.”*


<span id="route-30"></span>

??? note "Stage 30 · Seviron · 2 ways"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I have the cheese.”

    - **Needs:** stage 10, 20; not yet stage 20, 30; hand over 1× [Cheese](../items/cheese.md); not carry 3× [Small rock](../items/rock.md)
    - *“Thanks. Now we just need the rocks and the bottle.”*

    **Way 2:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I have the rocks.”

    - **Needs:** stage 10, 20, 30; not yet stage 20, 30; hand over 3× [Small rock](../items/rock.md)
    - *“Thanks. Now we just need the bottle. You should ask around town. Someone must have one.”*


<span id="route-40"></span>

??? note "Stage 40 · Arlish · 1 way"

    **Way 1:** Talk to [Arlish](../monsters/arlish.md), choose “Seviron at the church needs it. I'm just helping out.”

    - **Needs:** stage 20, 30; not yet stage 40
    - **Gives:** [Large empty bottle](../items/large_bottle.md)
    - *“Well, I do happen to have one. I don't display it as shop inventory because I've never been asked for such a thing before. Since it's for…”*


<span id="route-50"></span>

??? note "Stage 50 · Seviron · 1 way"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “Yes. Here it is.”

    - **Needs:** stage 20, 30; not yet stage 50; hand over 1× [Large empty bottle](../items/large_bottle.md)
    - <small>Also: starts timer “mouse_trap”</small>
    - *“Excellent. I'll set the trap. This will require some patience though, so you should come back later to see if it worked.”*


<span id="route-60"></span>

??? note "Stage 60 · Seviron · 1 way"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), automatic

    - **Needs:** stage 50; not yet stage 60; reached stage 40 of nondisplay bhvt (flag not defined in the game data)
    - **Gives:** [Trapped mouse](../items/trapped_mouse.md), [Gold coins](../items/gold.md)
    - *“We caught the mouse! Here it is, in the bottle. You can decide what to do with it. And here's a little gold for your help.”*


<span id="route-70"></span>

??? note "Stage 70 · Seviron · 1 way"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I'll give it to the cat. That should solve the problem.”

    - **Needs:** stage 60; not yet stage 70, 80, 90; carry 1× [Trapped mouse](../items/trapped_mouse.md); hand over 1× [Trapped mouse](../items/trapped_mouse.md)
    - **Gives:** [Large empty bottle](../items/large_bottle.md)
    - *“Hmm. I'm sure the cat will be happy, but I doubt the mouse will!”*


<span id="route-80"></span>

??? note "Stage 80 · Seviron · 1 way"

    **Way 1:** Talk to [Seviron](../monsters/brv_churchman.md), choose “I'll release it outside.”

    - **Needs:** stage 60; not yet stage 70, 80, 90; carry 1× [Trapped mouse](../items/trapped_mouse.md)
    - *“Well, don't release it in the town. It will just go into another building.”*


<span id="route-90"></span>

??? note "Stage 90 · stepping on a trigger on brimhaven7 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 7](../maps/brimhaven7.md), choose “[Open the bottle]”

    - **Needs:** carry 1× [Trapped mouse](../items/trapped_mouse.md); hand over 1× [Trapped mouse](../items/trapped_mouse.md)
    - **Gives:** [Large empty bottle](../items/large_bottle.md)
    - *“You look after as it disappears quickly.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `cat_and_mouse` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `brv_churchman_08`, 20: `brv_churchman_09a`, 20: `brv_churchman_09c`, 30: `brv_churchman_09b`, 30: `brv_churchman_09c`, 40: `arlish_bottle_2`, 50: `brv_churchman_b2`, 60: `brv_churchman_trap2`, 70: `brv_churchman_trap3a`, 80: `brv_churchman_trap3b`, 90: `release_mouse1a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
