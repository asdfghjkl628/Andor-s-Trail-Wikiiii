# Rare delicacies

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_wise` |
| **In journal** | Yes |
| **Stages** | 4 (completes at 90) |
| **Started by** | [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) |
| **NPCs involved** | [Old man](../monsters/guynmart_wise.md) |
| **Locations** | [guynmart_wood_10](../maps/guynmart_wood_10.md) |
| **Total XP** | 2,000 |
| **Related quests** | 1 |

</div>

## Overview

> I met an old man living in seclusion on a hill top. He yearned for a meal of bread and cheese, together with wine.

## Prerequisites to start

Start with [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)). Required:

- reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35)
- hand over 2× [Bread](../items/bread.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [guynmart nondisplay (hidden flag)](guynmart_nondisplay.md#stage-35) | stage 35 reached, for stages 10, 20, 30, 90 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met an old man living in seclusion on a hill top. He yearned for a meal of bread and cheese, together with wine. | [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | hand over 2× [Bread](../items/bread.md) | – |
| <span id="stage-20"></span>20 | I brought him bread, cheese and wine. He is very happy. | [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | hand over 1× [Cheese](../items/cheese.md), hand over 1× [Wine](../items/guynmart_wine.md), hand over 2× [Bread](../items/bread.md), stage 10 | gives 1× [Old man's ring of bone](../items/guynmart_bonering.md) |
| <span id="stage-30"></span>30 | He would be even happier if the cheese was cheddar from Charwood. You can only get the cheddar there if you explicitly ask for it. | [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | stage 20 | – |
| <span id="stage-90"></span>90 | I got bread, cheddar and wine for him. He started feasting happily. **(completes quest)** | [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | hand over 1× [Charwood cheddar](../items/charwood_cheddar.md), hand over 1× [Wine](../items/guynmart_wine.md), hand over 2× [Bread](../items/bread.md), stage 30 | 2,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “Just say what you would like. What can I do for you?” — **conditions:** reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35); hand over 2× [Bread](../items/bread.md) → **stage 10**. NPC: “I long for a meal with bread and cheese and a good bottle of wine. Oh, what would I give for that?”

???+ note "Stage 20: 1 route"

    1. Talk to [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “Yes, here you are. Enjoy it!” — **conditions:** reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35); reached stage 10 of [Rare delicacies](../quests/guynmart_wise.md#stage-10); hand over 2× [Bread](../items/bread.md); hand over 1× [Cheese](../items/cheese.md); hand over 1× [Wine](../items/guynmart_wine.md) → **stage 20**; also gives 1× [Old man's ring of bone](../items/guynmart_bonering.md). NPC: “So take this ring as a token of my gratitude. Certain beings in the cellars of Guynmart Castle will not harm you if…”

???+ note "Stage 30: 1 route"

    1. Talk to [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “Oh?” — **conditions:** reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35); reached stage 20 of [Rare delicacies](../quests/guynmart_wise.md#stage-20) → **stage 30**. NPC: “Their Cheddar is a dream! But they sell it only when you explicitly ask for it.”

???+ note "Stage 90: 1 route"

    1. Talk to [Old man](../monsters/guynmart_wise.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “Yes, finally I got it. I hope the cheddar is still fresh after the long journey.” — **conditions:** reached stage 35 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-35); reached stage 30 of [Rare delicacies](../quests/guynmart_wise.md#stage-30); hand over 2× [Bread](../items/bread.md); hand over 1× [Charwood cheddar](../items/charwood_cheddar.md); hand over 1× [Wine](../items/guynmart_wine.md) → **stage 90**. NPC: “Cheddar! I can't believe it!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Cheddar! I can't belive it!” → “Cheddar! I can't believe it!” |
| [v0.7.13](../versions/0.7.13.md) | stage 10 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_wise.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_wise.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_wise.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_wise.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_wise.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_wise` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 90 |
    | Dialogue nodes setting stages | 10: `guynmart_wise_130`, 20: `guynmart_wise_160`, 30: `guynmart_wise_182`, 90: `guynmart_wise_200` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
