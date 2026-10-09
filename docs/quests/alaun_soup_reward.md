---
description: "Alaun soup rewards is a hidden quest in Andor's Trail, started by Alaun (fallhaven_alaun). 7 stages, 1,350 XP in total. 10 gold"
---

# Alaun soup rewards

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `alaun_soup_reward` |
| **In journal** | No (hidden flag) |
| **Stages** | 7 |
| **Started by** | [Alaun](../monsters/alaun.md) ([Fallhaven alaun](../maps/fallhaven_alaun.md)) |
| **NPCs involved** | [Alaun](../monsters/alaun.md) |
| **Locations** | [Fallhaven alaun](../maps/fallhaven_alaun.md) |
| **Total XP** | 1,350 |
| **Related quests** | 1 |

</div>

## Overview

> 10 gold

## Prerequisites to start

Start with [Alaun](../monsters/alaun.md) ([Fallhaven alaun](../maps/fallhaven_alaun.md)). Required:

- NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Delicious soup](gison_soup.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [Delicious soup](gison_soup.md#stage-20) | stage 20 reached, for stages 11, 16, 21 here |
| Requires | [Delicious soup](gison_soup.md#stage-50) | stage 50 reached, for stage 30 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-10) | stage 10 must NOT be reached, for stages 10, 15, 20 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-30) | stage 30 must NOT be reached, for stages 11, 16, 21 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-50) | stage 50 must NOT be reached, for stages 11, 16, 21 here |
| Unlocks | [Delicious soup](gison_soup.md#stage-30) | stage 30 there needs stages 10, 15, 20 here |
| Unlocks | [Delicious soup](gison_soup.md#stage-35) | stage 35 there needs stages 10, 15, 20 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | 10 gold | [Alaun](../monsters/alaun.md) | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-11"></span>[11](#route-11) |  | [Alaun](../monsters/alaun.md) | 500 XP, sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), 10× [Gold coins](../items/gold.md), 5× [Bread](../items/bread.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-15"></span>[15](#route-15) | 15 gold | [Alaun](../monsters/alaun.md) | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-16"></span>[16](#route-16) |  | [Alaun](../monsters/alaun.md) | 450 XP, 15× [Gold coins](../items/gold.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-20"></span>[20](#route-20) | 20 gold | [Alaun](../monsters/alaun.md) | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-21"></span>[21](#route-21) |  | [Alaun](../monsters/alaun.md) | 400 XP, sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), 20× [Gold coins](../items/gold.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-30"></span>[30](#route-30) | Failure | [Alaun](../monsters/alaun.md) | applies condition fear |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Sounds easy, I'll do it!”

    - **Needs:** not reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - **Gives:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - *“That's really nice of you.”*


<span id="route-11"></span>

??? note "Stage 11 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Gison gave me some of his soup.”

    - **Needs:** stage 10; reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); not reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); not reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); hand over 1× [Gison's mushroom soup](../items/gison_soup.md)
    - **Gives:** sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), 10× [Gold coins](../items/gold.md), 5× [Bread](../items/bread.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)
    - *“Here is the money I promised you. And as a bonus I will give you some of this bread. Next time I will buy Nimael's soup.”*


<span id="route-15"></span>

??? note "Stage 15 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Sounds good. I will do it.”

    - **Needs:** not reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - **Gives:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - *“That's nice of you.”*


<span id="route-16"></span>

??? note "Stage 16 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Gison gave me some of his soup.”

    - **Needs:** stage 15; reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); not reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); not reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); hand over 1× [Gison's mushroom soup](../items/gison_soup.md)
    - **Gives:** 15× [Gold coins](../items/gold.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)
    - *“Here is the money I promised you. Next time I will buy Nimael's soup.”*


<span id="route-20"></span>

??? note "Stage 20 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Sounds good. I will do it.”

    - **Needs:** not reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - **Gives:** sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)
    - *“OK, please bring it hot!”*


<span id="route-21"></span>

??? note "Stage 21 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “Gison gave me some of his soup.”

    - **Needs:** stage 20; reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); not reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); not reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); hand over 1× [Gison's mushroom soup](../items/gison_soup.md)
    - **Gives:** sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), 20× [Gold coins](../items/gold.md), 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35)
    - *“Here is the money I promised you. Next time I will buy Nimael's soup.”*


<span id="route-30"></span>

??? note "Stage 30 · Alaun · 1 way"

    **Way 1:** Talk to [Alaun](../monsters/alaun.md), choose “I was not able to bring you the soup.”

    - **Needs:** latest stage of [Delicious soup](../quests/gison_soup.md#stage-10) is 10; reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50)
    - **Gives:** applies condition fear
    - *“That can't be. Get out of here! [Alaun starts throwing things at you]”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `alaun_soup_reward` |
    | Name in game data | `Alaun soup rewards` |
    | showInLog | 0 |
    | Stage IDs | 10, 11, 15, 16, 20, 21, 30 |
    | Dialogue nodes setting stages | 10: `alaun_startquest10`, 11: `alaun_return10`, 15: `alaun_startquest15`, 16: `alaun_return15`, 20: `alaun_startquest20`, 21: `alaun_return20`, 30: `alaun_return_fail` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
