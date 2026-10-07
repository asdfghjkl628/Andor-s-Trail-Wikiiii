---
description: "Honor your parents is a quest in Andor's Trail, started by Shop Owner (brimhaven_shop). 6 stages, 600 XP in total. I have decided to give a necklace to my father Mikhail, in our family colors of red, green, and white."
---

# Honor your parents

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_present` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 40, 50, 60) |
| **Started by** | [Shop Owner](../monsters/brv_shop_owner.md) ([Brimhaven shop](../maps/brimhaven_shop.md)) |
| **NPCs involved** | [Mikhail](../monsters/mikhail.md), [Shop Owner](../monsters/brv_shop_owner.md) |
| **Locations** | [Brimhaven shop](../maps/brimhaven_shop.md), [Home](../maps/home.md), [Waytogalmore 0](../maps/waytogalmore0.md) |
| **Total XP** | 600 |
| **Related quests** | 3 |

</div>

## Overview

> I have decided to give a necklace to my father Mikhail, in our family colors of red, green, and white.

## Prerequisites to start

Start with [Shop Owner](../monsters/brv_shop_owner.md) ([Brimhaven shop](../maps/brimhaven_shop.md)). Required:

- reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-130) | stage 130 reached, for stages 10, 20 here |
| Requires | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-40) | stage 40 reached, for stages 40, 50, 60 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stages 30, 40, 50, 60 here |
| Blocked by | [Brimhaven multipurpose story flags (hidden flag)](brv_nondisplay_multipurpose.md#stage-40) | stage 40 must NOT be reached, for stage 30 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I have decided to give a necklace to my father Mikhail, in our… ▸</span><span class="l">▴ less</span></summary>I have decided to give a necklace to my father Mikhail, in our family colors of red, green, and white.</details> | [Shop Owner](../monsters/brv_shop_owner.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I have purchased a necklace. | [Shop Owner](../monsters/brv_shop_owner.md) | varies by route (see below) |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Mikhail didn't want to take the necklace. He was angry because I… ▸</span><span class="l">▴ less</span></summary>Mikhail didn't want to take the necklace. He was angry because I didn't focus on finding Andor.</details> | [Mikhail](../monsters/mikhail.md) | – |
| <span id="stage-40"></span>[40](#route-40) | My father didn't seem very happy with the cheap necklace. **(ends quest)** | [Mikhail](../monsters/mikhail.md) | 50 XP |
| <span id="stage-50"></span>[50](#route-50) | My father was very happy with the nice necklace. **(ends quest)** | [Mikhail](../monsters/mikhail.md) | 500 XP |
| <span id="stage-60"></span>[60](#route-60) | My father was disappointed with the pretentious necklace I bought. **(ends quest)** | [Mikhail](../monsters/mikhail.md) | 50 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Shop Owner · 1 way"

    **Way 1:** Talk to [Shop Owner](../monsters/brv_shop_owner.md), automatic

    - **Needs:** reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130)
    - *“How can I serve you, traveler?”*


<span id="route-20"></span>

??? note "Stage 20 · Shop Owner · 3 ways"

    **Way 1:** Talk to [Shop Owner](../monsters/brv_shop_owner.md), choose “Give me a necklace for 50,000 gold coins.”

    - **Needs:** reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 50,000 gold
    - **Gives:** 1× [Necklace for father (expensive)](../items/necklace_for_father3.md)
    - *“Take this wonderful necklace. Your father will be very happy.”*

    **Way 2:** Talk to [Shop Owner](../monsters/brv_shop_owner.md), choose “Give me a necklace for 500 gold coins.”

    - **Needs:** reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 500 gold
    - **Gives:** 1× [Necklace for father](../items/necklace_for_father2.md)
    - *“Here is the necklace.”*

    **Way 3:** Talk to [Shop Owner](../monsters/brv_shop_owner.md), choose “Give me a necklace for 5 gold coins.”

    - **Needs:** reached stage 130 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 5 gold
    - **Gives:** 1× [Necklace for father (cheap)](../items/necklace_for_father1.md)
    - *“Take this... valuable necklace. Your father will be proud to wear it.”*


<span id="route-30"></span>

??? note "Stage 30 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “I have a present for you.”

    - **Needs:** stage 20; not yet stage 40, 50, 60; reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); not reached stage 40 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40)
    - *“I asked you to search for your brother Andor and you did not find out anything and instead you are bringing me a necklace? Go and search…”*


<span id="route-40"></span>

??? note "Stage 40 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “[Give him the cheap necklace]”

    - **Needs:** stage 20; not yet stage 40, 50, 60; reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 40 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father (cheap)](../items/necklace_for_father1.md)
    - *“Hm, thank you. Looks like you spent all your pocket money for this.”*


<span id="route-50"></span>

??? note "Stage 50 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “[Give him the necklace]”

    - **Needs:** stage 20; not yet stage 40, 50, 60; reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 40 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father](../items/necklace_for_father2.md)
    - *“Thank you my child for this wonderful necklace. Oh and it is in our family colors!”*


<span id="route-60"></span>

??? note "Stage 60 · Mikhail · 1 way"

    **Way 1:** Talk to [Mikhail](../monsters/mikhail.md), choose “[Give him the expensive necklace]”

    - **Needs:** stage 20; not yet stage 40, 50, 60; reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 40 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father (expensive)](../items/necklace_for_father3.md)
    - *“Oh, where did you get the money to buy this? Maybe I don't want to know...”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.12](../versions/0.7.12.md) | Stage 10 journal text changed<br>Stage 20 journal text changed<br>Stage 30 journal text changed<br>Stage 40 journal text changed<br>Stage 50 journal text changed<br>Stage 60 journal text changed<br>Dialogue: 1 line changed<br>· text: “Thank you my son for this wonderful necklace. Oh and it is in our fam…” → “Thank you my child for this wonderful necklace. Oh and it is in our f…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “How can I serve you, Sir?” → “How can I serve you, traveler?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_present` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `brv_shop_owner_20`, 20: `brv_shop_owner_40_3`, 20: `brv_shop_owner_40_2`, 20: `brv_shop_owner_40_1`, 30: `mikhail_present_10`, 40: `mikhail_present_20_1`, 50: `mikhail_present_20_2`, 60: `mikhail_present_20_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
