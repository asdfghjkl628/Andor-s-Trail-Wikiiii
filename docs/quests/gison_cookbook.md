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
| **Started by** | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) |
| **NPCs involved** | [Gison](../monsters/gison.md), [Thief](../monsters/gison_thief1.md) |
| **Locations** | [mywild20_houseleft](../maps/mywild20_houseleft.md), [mywildcave4](../maps/mywildcave4.md) |
| **Related quests** | 1 |

</div>

## Overview

> Gison, the man with the mushroom soup in the forest south of Fallhaven, got raided. Only his cookbook was stolen and he asked me to bring it back to him.

## Prerequisites to start

Start with [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)). Required:

- reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100)
- killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Delicious soup](gison_soup.md#stage-100) | stage 100 reached, for stages 10, 15 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Gison, the man with the mushroom soup in the forest south of Fallhaven, got raided. Only his cookbook was stolen and he asked me to bring it back to him. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | – | – |
| <span id="stage-15"></span>15 | I agreed to help him. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | – | – |
| <span id="stage-20"></span>20 | Gison said the thieves came from the south. I should begin my search there. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 15 | – |
| <span id="stage-30"></span>30 | I discovered a hidden cave. The thieves may be hiding there.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Mywildcave](../maps/mywildcave.md).</span> | walking into a blocked passage on [mywildcave](../maps/mywildcave.md) | stage 20 | – |
| <span id="stage-40"></span>40 | I found the thieves. Their leader was performing some kind of ritual when I came into the cave. | [Thief](../monsters/gison_thief1.md) ([mywildcave4](../maps/mywildcave4.md)) | – | – |
| <span id="stage-60"></span>60 | I brought the cookbook back to Gison. The thieves were working for Zuul'khan, the fungi sorcerer. They made a second copy of the book without the strange writing, which Gison gladly accepted. Gison can now cook his mushroom soup again. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | carry 1× [Fabulous cookings (copy)](../items/gison_cookbook_2.md), stage 40 | – |
| <span id="stage-62"></span>62 | I told Gison that I found the thieves, but that they had destroyed the cookbook. **(completes quest)**<br><span class="qnote">🔒 An area on [Mywildcave4](../maps/mywildcave4.md) becomes blocked off.</span> | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 40 | changes map mywildcave4 |
| <span id="stage-70"></span>70 | Gison will give me mushroom soup in thanks if I bring him 50 gold, 2 of Bogsten's mushrooms and an empty bottle. **(completes quest)** | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → the conversation leads here automatically — **conditions:** reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9) → **stage 10**. NPC: “Strangely they only took my old cookbook with them. Please help me get back my book, otherwise I cannot make my…”

???+ note "Stage 15: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Sure thing. I'll search for your book.” — **conditions:** reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-zuul_khan9) → **stage 15**. NPC: “I really thank you.”

???+ note "Stage 20: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → the conversation leads here automatically — **conditions:** reached stage 15 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-15) → **stage 20**. NPC: “The robbers came from the south. Maybe you should start your search in that direction. Take care!”

???+ note "Stage 30: 1 route"

    1. walking into a blocked passage on [mywildcave](../maps/mywildcave.md) → choose “Examine it more closely.” — **conditions:** reached stage 20 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-20) → **stage 30**. NPC: “You examine the wall more closely and discover an entrance hidden beneath moss and leaves.”

???+ note "Stage 40: 1 route"

    1. Talk to [Thief](../monsters/gison_thief1.md) ([mywildcave4](../maps/mywildcave4.md)) → the conversation leads here automatically → **stage 40**. NPC: “Let's pretend that you have not seen my master over there, practicing dark magic with the old spell in this book we…”

???+ note "Stage 60: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes, the robbers have made a complete copy of the book, just without the spell.” — **conditions:** reached stage 40 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-40); carry 1× [Fabulous cookings (copy)](../items/gison_cookbook_2.md) → **stage 60**. NPC: “Then give me the copy. I don't want to be raided again.”

???+ note "Stage 62: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “[Lie] I found the robbers, but they had destroyed the book.” — **conditions:** reached stage 40 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-40); NOT killed 1× [Zuul'khan](../monsters/zuul_khan.md#v-gison_thiefboss) → **stage 62**; also changes map mywildcave4. NPC: “Noo!”

???+ note "Stage 70: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Oh yes.” — **conditions:** reached stage 70 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-70) → **stage 70**. NPC: “Give me 2 of Bogsten's mushrooms and an empty bottle, then I could sell you a portion for only 50 gold.”


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
