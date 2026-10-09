---
description: "Taste is everything is a quest in Andor's Trail, started by Tharal. 6 stages, 200 XP in total. I should visit the potion-maker in Fallhaven and ask for something to help against food poisoning."
---

# Taste is everything

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `antifoodp` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 40) |
| **Started by** | [Tharal](../monsters/tharal.md) |
| **NPCs involved** | [Potion merchant](../monsters/potion_merchant.md), [Tharal](../monsters/tharal.md) |
| **Locations** | [Fallhaven potions](../maps/fallhaven_potions.md) |
| **Total XP** | 200 |

</div>

## Overview

> I should visit the potion-maker in Fallhaven and ask for something to help against food poisoning.

## Prerequisites to start

None: talk to [Tharal](../monsters/tharal.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I should visit the potion-maker in Fallhaven and ask for something… ▸</span><span class="l">▴ less</span></summary>I should visit the potion-maker in Fallhaven and ask for something to help against food poisoning.</details> | [Tharal](../monsters/tharal.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">The potion-maker in Fallhaven can create potions that help against… ▸</span><span class="l">▴ less</span></summary>The potion-maker in Fallhaven can create potions that help against food-poisoning.</details> | [Potion merchant](../monsters/potion_merchant.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I should bring him a poison gland, two pieces of animal hair and 50… ▸</span><span class="l">▴ less</span></summary>I should bring him a poison gland, two pieces of animal hair and 50 gold pieces, and he'll create a potion for me.</details> | [Potion merchant](../monsters/potion_merchant.md) | – |
| <span id="stage-30"></span>[30](#route-30) | I have brought the ingredients for the potion. | [Potion merchant](../monsters/potion_merchant.md) | 200 XP |
| <span id="stage-35"></span>[35](#route-35) | I received a potion of antidote, that should help me if I get food-poisoning. | [Potion merchant](../monsters/potion_merchant.md) | [Antidote](../items/antifoodp.md) |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I can bring him more ingredients if I want him to create more… ▸</span><span class="l">▴ less</span></summary>I can bring him more ingredients if I want him to create more antidote potions in the future.</details> **(ends quest)** | [Potion merchant](../monsters/potion_merchant.md) | – |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Tharal · 1 way"

    **Way 1:** Talk to [Tharal](../monsters/tharal.md), choose “Do you have anything to help against food-poisoning?”

    - *“You should go see him and ask if he has anything to help against that. He can probably help you.”*


<span id="route-15"></span>

??? note "Stage 15 · Potion merchant · 1 way"

    **Way 1:** Talk to [Potion merchant](../monsters/potion_merchant.md), choose “Do you have anything to help against food-poisoning?”

    - *“Oh yes, I have a recipe for a mixture that helps against food poisoning. If you want, I could create some of that for you.”*


<span id="route-20"></span>

??? note "Stage 20 · Potion merchant · 1 way"

    **Way 1:** Talk to [Potion merchant](../monsters/potion_merchant.md), choose “Do you have anything to help against food-poisoning?”

    - **Needs:** stage 40
    - *“To make the potion against food-poisoning, I would need one poison gland and two pieces of animal hair. I will also require 50 gold for…”*


<span id="route-30"></span>

??? note "Stage 30 · Potion merchant · 1 way"

    **Way 1:** Talk to [Potion merchant](../monsters/potion_merchant.md), choose “I have those ingredients for you.”

    - **Needs:** stage 40; not yet stage 35; hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold
    - *“Good. Give me a minute to prepare that antidote for you.”*


<span id="route-35"></span>

??? note "Stage 35 · Potion merchant · 1 way"

    **Way 1:** Talk to [Potion merchant](../monsters/potion_merchant.md), choose “I have those ingredients for you.”

    - **Needs:** stage 35, 40; hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold
    - **Gives:** [Antidote](../items/antifoodp.md)
    - *“There. One potion against food-poisoning for you.”*


<span id="route-40"></span>

??? note "Stage 40 · Potion merchant · 1 way"

    **Way 1:** Talk to [Potion merchant](../monsters/potion_merchant.md), choose “Do you have anything to help against food-poisoning?”

    - **Needs:** stage 35
    - *“I can create more of those potions if you want. You'll have to bring me more of those ingredients then.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `antifoodp` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 35, 40 |
    | Dialogue nodes setting stages | 10: `tharal_antifoodp2`, 15: `fallhaven_pot_antifoodp2`, 20: `fallhaven_pot_antifoodp5`, 30: `fallhaven_pot_antifp_q1`, 35: `fallhaven_pot_antifp_q3`, 40: `fallhaven_pot_antifp_q4` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
