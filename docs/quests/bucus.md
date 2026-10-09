---
description: "Key of Luthor is a quest in Andor's Trail, started by Bucus. 6 stages, 2,850 XP in total. Bucus in Fallhaven might know something about Andor. He wants me to bring him the key of Luthor from the catacombs beneath Fallhaven church."
---

# Key of Luthor

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bucus` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 100) |
| **Started by** | [Bucus](../monsters/bucus.md) |
| **NPCs involved** | [Athamyr](../monsters/athamyr.md), [Bucus](../monsters/bucus.md), [Thoronir](../monsters/thoronir.md) |
| **Locations** | [Fallhaven church](../maps/fallhaven_church.md) |
| **Total XP** | 2,850 |
| **Related quests** | 4 |

</div>

## Overview

> Bucus in Fallhaven might know something about Andor. He wants me to bring him the key of Luthor from the catacombs beneath Fallhaven church.

## Prerequisites to start

Start with [Bucus](../monsters/bucus.md). Required:

- reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Score counters (hidden flag)](scores.md#stage-18) | stage 18 reached, for stage 20 here |
| Unlocks | [Thief apprentice](Thieves01.md#stage-5) | stage 5 there needs stage 100 here |
| Unlocks | [Search for Andor](andor.md#stage-50) | stage 50 there needs stage 100 here |
| Unlocks | [Feygard story flags (hidden flag)](feygard_nondisplayed.md#stage-60) | stage 60 there needs stage 100 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Bucus in Fallhaven might know something about Andor. He wants me to… ▸</span><span class="l">▴ less</span></summary>Bucus in Fallhaven might know something about Andor. He wants me to bring him the key of Luthor from the catacombs beneath Fallhaven church.</details> | [Bucus](../monsters/bucus.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The catacombs beneath Fallhaven church are closed off. Athamyr is… ▸</span><span class="l">▴ less</span></summary>The catacombs beneath Fallhaven church are closed off. Athamyr is the only one with both permission and the bravery to enter them. I should go see him in his house southwest of the church.</details> | [Thoronir](../monsters/thoronir.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Athamyr wants me to bring him some cooked meat, then maybe he will… ▸</span><span class="l">▴ less</span></summary>Athamyr wants me to bring him some cooked meat, then maybe he will want to talk more.</details> | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-40"></span>[40](#route-40) | I brought some cooked meat to Athamyr. | [Athamyr](../monsters/athamyr.md) | 700 XP |
| <span id="stage-50"></span>[50](#route-50) | Athamyr has given me permission to enter the catacombs beneath Fallhaven church.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven church](../maps/fallhaven_church.md).</span> | [Athamyr](../monsters/athamyr.md) | – |
| <span id="stage-100"></span>[100](#route-100) | I brought Bucus the key of Luthor. **(ends quest)** | [Bucus](../monsters/bucus.md) | 2,150 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Bucus · 1 way"

    **Way 1:** Talk to [Bucus](../monsters/bucus.md), choose “What was I supposed to do again?”

    - **Needs:** stage 10
    - *“Bring me the key of Luthor and we can talk more. I don't know anything about the key itself, but rumor has it that it is located somewhere…”*


<span id="route-20"></span>

??? note "Stage 20 · Thoronir · 1 way"

    **Way 1:** Talk to [Thoronir](../monsters/thoronir.md), choose “Has anyone entered the catacombs?”

    - **Needs:** stage 10; reached stage 18 of [Score counters (hidden flag)](../quests/scores.md#stage-18)
    - *“No one is allowed down in the catacombs, except for Athamyr, my apprentice. He is the only one that has been down there for years.”*


<span id="route-30"></span>

??? note "Stage 30 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “How can I get permission to go down there?”

    - **Needs:** stage 20; not yet stage 100
    - *“Bring me some of that delicious cooked meat from the tavern and I will give you my permission to enter the catacombs of Fallhaven Church.”*


<span id="route-40"></span>

??? note "Stage 40 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Here, I have cooked meat for you.”

    - **Needs:** stage 20; not yet stage 100; hand over 1× [Cooked meat](../items/meat_cooked.md)
    - *“Thanks, this will do nicely.”*


<span id="route-50"></span>

??? note "Stage 50 · Athamyr · 1 way"

    **Way 1:** Talk to [Athamyr](../monsters/athamyr.md), choose “Have you been down in the catacombs?”

    - **Needs:** stage 20, 40; not yet stage 100
    - *“You have my permission to enter the catacombs of Fallhaven Church.”*


<span id="route-100"></span>

??? note "Stage 100 · Bucus · 1 way"

    **Way 1:** Talk to [Bucus](../monsters/bucus.md), choose “Here, I have it. The key of Luthor.”

    - **Needs:** stage 10; hand over 1× [Key of Luthor](../items/key_luthor.md)
    - *“Wow, you actually got the key of Luthor? I didn't think you would make it out of there.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bucus` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 100 |
    | Dialogue nodes setting stages | 10: `bucus_thieves_4`, 20: `thoronir_church_4`, 30: `athamyr_4`, 40: `athamyr_complete`, 50: `athamyr_complete_2`, 100: `bucus_thieves_complete_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
