---
description: "Well rested is a quest in Andor's Trail, started by Prim cook (blackwater_mountain21). 5 stages, 500 XP in total. I talked to the cook in Prim, at the base of Blackwater mountain. There is a back room available for rent, but it is currently rented out to Arghest. I should go talk to Arghest to se…"
---

# Well rested

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `prim_innquest` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 50) |
| **Started by** | [Prim cook](../monsters/prim_cook.md) ([Blackwater mountain 21](../maps/blackwater_mountain21.md)) |
| **NPCs involved** | [Arghest](../monsters/arghest.md), [Prim cook](../monsters/prim_cook.md) |
| **Locations** | [Blackwater mountain 13](../maps/blackwater_mountain13.md), [Blackwater mountain 21](../maps/blackwater_mountain21.md) |
| **Total XP** | 500 |

</div>

## Overview

> I talked to the cook in Prim, at the base of Blackwater mountain. There is a back room available for rent, but it is currently rented out to Arghest. I should go talk to Arghest to see whether he still wants to rent the room. The cook pointed me towards the southwest of Prim.

## Prerequisites to start

Start with [Prim cook](../monsters/prim_cook.md) ([Blackwater mountain 21](../maps/blackwater_mountain21.md)). Required:

- reached stage 10 of [Well rested](../quests/prim_innquest.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I talked to the cook in Prim, at the base of Blackwater mountain.… ▸</span><span class="l">▴ less</span></summary>I talked to the cook in Prim, at the base of Blackwater mountain. There is a back room available for rent, but it is currently rented out to Arghest. I should go talk to Arghest to see whether he still wants to rent the room. The cook pointed me towards the southwest of Prim.</details> | [Prim cook](../monsters/prim_cook.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I talked to Arghest about the back room at the inn. He is still… ▸</span><span class="l">▴ less</span></summary>I talked to Arghest about the back room at the inn. He is still interested in having it as an option to rest at. But he told me he could probably be persuaded to let me use it if I compensate him sufficiently.</details> | [Arghest](../monsters/arghest.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Arghest wants me to bring him 5 bottles of milk. I can probably find… ▸</span><span class="l">▴ less</span></summary>Arghest wants me to bring him 5 bottles of milk. I can probably find some milk in any of the larger villages.</details> | [Arghest](../monsters/arghest.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I have brought the milk to Arghest. He agreed to let me use the back… ▸</span><span class="l">▴ less</span></summary>I have brought the milk to Arghest. He agreed to let me use the back room at the Prim inn. I should be able to rest there now. I should go talk to the cook at the inn.</details> | [Arghest](../monsters/arghest.md) | 500 XP |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I have explained to the cook that I have permission by Arghest to… ▸</span><span class="l">▴ less</span></summary>I have explained to the cook that I have permission by Arghest to use the back room.</details> **(ends quest)**<br><span class="qnote">🔓 You can finally access a previously blocked area on [Blackwater mountain 21](../maps/blackwater_mountain21.md).</span> | [Prim cook](../monsters/prim_cook.md) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Prim cook · 1 way"

    **Way 1:** Talk to [Prim cook](../monsters/prim_cook.md), choose “Any idea where he might be?”

    - **Needs:** stage 10
    - *“I don't know where he is now, but I do know that he used to be part of the mining effort in our mine to the southwest.”*


<span id="route-20"></span>

??? note "Stage 20 · Arghest · 1 way"

    **Way 1:** Talk to [Arghest](../monsters/arghest.md), choose “Mind if I use the room at the inn to rest in?”

    - **Needs:** stage 10
    - *“Well, I would like to still keep the option of using it. But I guess someone else could rest there now that I'm not actively using it.”*


<span id="route-30"></span>

??? note "Stage 30 · Arghest · 1 way"

    **Way 1:** Talk to [Arghest](../monsters/arghest.md), choose “Sure, no problem. I'll get you your bottles of milk. How much do you need?”

    - **Needs:** stage 10
    - *“Bring me 5 bottles of milk. That should be enough.”*


<span id="route-40"></span>

??? note "Stage 40 · Arghest · 1 way"

    **Way 1:** Talk to [Arghest](../monsters/arghest.md), choose “Yes, here you go, enjoy!”

    - **Needs:** stage 30; hand over 5× [Milk](../items/milk.md)
    - *“Thank you my friend! Now I can restock my supply.”*


<span id="route-50"></span>

??? note "Stage 50 · Prim cook · 1 way"

    **Way 1:** Talk to [Prim cook](../monsters/prim_cook.md), choose “Yes, he gave me permission to use the back room whenever I wish.”

    - **Needs:** stage 10, 40
    - *“Really, he did? Well then, go ahead. I'm just glad the back room is being used.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Stage 10 journal text changed<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_innquest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_innquest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_innquest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_innquest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_innquest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `prim_innquest` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `prim_cook_6`, 20: `arghest_11`, 30: `arghest_14`, 40: `arghest_return_4`, 50: `prim_cook_return_6` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
