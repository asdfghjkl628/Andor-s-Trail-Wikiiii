---
description: "A raid for a cookbook is a quest in Andor's Trail, started by Gison (mywild20_houseleft). 8 stages. Gison, the man with the mushroom soup in the forest south of Fallhaven, got raided. Only his cookbook was stolen and he asked me to bring it back to him."
---

# A raid for a cookbook

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `gison_cookbook` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 62, 70) |
| **Started by** | [Gison](../monsters/gison.md) ([Mywild 20 houseleft](../maps/mywild20_houseleft.md)) |
| **NPCs involved** | [Gison](../monsters/gison.md), [Thief](../monsters/gison_thief1.md) |
| **Locations** | [Mywild 20 houseleft](../maps/mywild20_houseleft.md), [Mywildcave 4](../maps/mywildcave4.md) |
| **Related quests** | 1 |

</div>

## Overview

> Gison, the man with the mushroom soup in the forest south of Fallhaven, got raided. Only his cookbook was stolen and he asked me to bring it back to him.

## Prerequisites to start

Start with [Gison](../monsters/gison.md) ([Mywild 20 houseleft](../maps/mywild20_houseleft.md)). Required:

- reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100)
- killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Delicious soup](gison_soup.md#stage-100) | stage 100 reached, for stages 10, 15 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Gison, the man with the mushroom soup in the forest south of… ▸</span><span class="l">▴ less</span></summary>Gison, the man with the mushroom soup in the forest south of Fallhaven, got raided. Only his cookbook was stolen and he asked me to bring it back to him.</details> | [Gison](../monsters/gison.md) | – |
| <span id="stage-15"></span>[15](#route-15) | I agreed to help him. | [Gison](../monsters/gison.md) | – |
| <span id="stage-20"></span>[20](#route-20) | Gison said the thieves came from the south. I should begin my search there. | [Gison](../monsters/gison.md) | – |
| <span id="stage-30"></span>[30](#route-30) | I discovered a hidden cave. The thieves may be hiding there.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Mywildcave](../maps/mywildcave.md).</span> | walking into a blocked passage on [Mywildcave](../maps/mywildcave.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I found the thieves. Their leader was performing some kind of ritual… ▸</span><span class="l">▴ less</span></summary>I found the thieves. Their leader was performing some kind of ritual when I came into the cave.</details> | [Thief](../monsters/gison_thief1.md) | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I brought the cookbook back to Gison. The thieves were working for… ▸</span><span class="l">▴ less</span></summary>I brought the cookbook back to Gison. The thieves were working for Zuul'khan, the fungi sorcerer. They made a second copy of the book without the strange writing, which Gison gladly accepted. Gison can now cook his mushroom soup again.</details> | [Gison](../monsters/gison.md) | – |
| <span id="stage-62"></span>[62](#route-62) | I told Gison that I found the thieves, but that they had destroyed the cookbook. **(ends quest)**<br><span class="qnote">🔒 An area on [Mywildcave 4](../maps/mywildcave4.md) becomes blocked off.</span> | [Gison](../monsters/gison.md) | changes map mywildcave4 |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">Gison will give me mushroom soup in thanks if I bring him 50 gold, 2… ▸</span><span class="l">▴ less</span></summary>Gison will give me mushroom soup in thanks if I bring him 50 gold, 2 of Bogsten's mushrooms and an empty bottle.</details> **(ends quest)** | [Gison](../monsters/gison.md) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), automatic

    - **Needs:** reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9)
    - *“Strangely they only took my old cookbook with them. Please help me get back my book, otherwise I cannot make my delicious mushroom soup.”*


<span id="route-15"></span>

??? note "Stage 15 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), choose “Sure thing. I'll search for your book.”

    - **Needs:** reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9)
    - *“I really thank you.”*


<span id="route-20"></span>

??? note "Stage 20 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), automatic

    - **Needs:** stage 15
    - *“The robbers came from the south. Maybe you should start your search in that direction. Take care!”*


<span id="route-30"></span>

??? note "Stage 30 · walking into a blocked passage on mywildcave · 1 way"

    **Way 1:** Walking into a blocked passage on [Mywildcave](../maps/mywildcave.md), choose “Examine it more closely.”

    - **Needs:** stage 20
    - *“You examine the wall more closely and discover an entrance hidden beneath moss and leaves.”*


<span id="route-40"></span>

??? note "Stage 40 · Thief · 1 way"

    **Way 1:** Talk to [Thief](../monsters/gison_thief1.md), automatic

    - *“Let's pretend that you have not seen my master over there, practicing dark magic with the old spell in this book we have stolen. Go away!”*


<span id="route-60"></span>

??? note "Stage 60 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), choose “Yes, the robbers have made a complete copy of the book, just without the spell.”

    - **Needs:** stage 40; carry 1× [Fabulous cookings (copy)](../items/gison_cookbook_2.md)
    - *“Then give me the copy. I don't want to be raided again.”*


<span id="route-62"></span>

??? note "Stage 62 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), choose “[Lie] I found the robbers, but they had destroyed the book.”

    - **Needs:** stage 40; not killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-gison_thiefboss)
    - **Gives:** changes map mywildcave4
    - *“Noo!”*


<span id="route-70"></span>

??? note "Stage 70 · Gison · 1 way"

    **Way 1:** Talk to [Gison](../monsters/gison.md), choose “Oh yes.”

    - **Needs:** stage 70
    - *“Give me 2 of Bogsten's mushrooms and an empty bottle, then I could sell you a portion for only 50 gold.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_cookbook.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_cookbook.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_cookbook.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_cookbook.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_cookbook.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `gison_cookbook` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 60, 62, 70 |
    | Dialogue nodes setting stages | 10: `gison_p1_40_2`, 15: `gison_p2_10_11`, 20: `gison_p2_15`, 30: `gison_cavekey_unlock`, 40: `gison_thief1_10`, 60: `gison_p2_50_3`, 62: `gison_p2_50_5`, 70: `gison_p2_70_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
