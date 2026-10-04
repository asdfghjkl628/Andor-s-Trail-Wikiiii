# Taste is everything

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `antifoodp` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 40) |
| **Started by** | [Tharal](../monsters/tharal.md) |
| **NPCs involved** | [Potion merchant](../monsters/potion_merchant.md), [Tharal](../monsters/tharal.md) |
| **Locations** | [fallhaven_potions](../maps/fallhaven_potions.md) |
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

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I should visit the potion-maker in Fallhaven and ask for something to help against food poisoning. | [Tharal](../monsters/tharal.md) | – | – |
| <span id="stage-15"></span>15 | The potion-maker in Fallhaven can create potions that help against food-poisoning. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | – | – |
| <span id="stage-20"></span>20 | I should bring him a poison gland, two pieces of animal hair and 50 gold pieces, and he'll create a potion for me. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | stage 40 | – |
| <span id="stage-30"></span>30 | I have brought the ingredients for the potion. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | hand over 1× [Poison gland](../items/gland.md), hand over 2× [Animal hair](../items/hair.md), pay 50 gold, stage 40 | 200 XP |
| <span id="stage-35"></span>35 | I received a potion of antidote, that should help me if I get food-poisoning. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | hand over 1× [Poison gland](../items/gland.md), hand over 2× [Animal hair](../items/hair.md), pay 50 gold, stage 40 | gives [Antidote](../items/antifoodp.md) |
| <span id="stage-40"></span>40 | I can bring him more ingredients if I want him to create more antidote potions in the future. **(completes quest)** | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | stage 35 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Tharal](../monsters/tharal.md) → choose “Do you have anything to help against food-poisoning?” → **stage 10**. NPC: “You should go see him and ask if he has anything to help against that. He can probably help you.”

???+ note "Stage 15: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “Do you have anything to help against food-poisoning?” → **stage 15**. NPC: “Oh yes, I have a recipe for a mixture that helps against food poisoning. If you want, I could create some of that for…”

???+ note "Stage 20: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “Do you have anything to help against food-poisoning?” — **conditions:** reached stage 40 of [Taste is everything](../quests/antifoodp.md#stage-40) → **stage 20**. NPC: “To make the potion against food-poisoning, I would need one poison gland and two pieces of animal hair. I will also…”

???+ note "Stage 30: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “I have those ingredients for you.” — **conditions:** reached stage 40 of [Taste is everything](../quests/antifoodp.md#stage-40); hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold; NOT reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35) → **stage 30**. NPC: “Good. Give me a minute to prepare that antidote for you.”

???+ note "Stage 35: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “I have those ingredients for you.” — **conditions:** reached stage 40 of [Taste is everything](../quests/antifoodp.md#stage-40); hand over 1× [Poison gland](../items/gland.md); hand over 2× [Animal hair](../items/hair.md); pay 50 gold; reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35) → **stage 35**; also gives [Antidote](../items/antifoodp.md). NPC: “There. One potion against food-poisoning for you.”

???+ note "Stage 40: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “Do you have anything to help against food-poisoning?” — **conditions:** reached stage 35 of [Taste is everything](../quests/antifoodp.md#stage-35) → **stage 40**. NPC: “I can create more of those potions if you want. You'll have to bring me more of those ingredients then.”


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

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=antifoodp.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
