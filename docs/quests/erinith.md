---
description: "Deep wound is a quest in Andor's Trail, started by Erinith (wild0). 9 stages, 1,200 XP in total. Just northeast of Crossglen village, I met Erinith that has set up camp. Apparently, he was attacked during the night and lost a book."
---

# Deep wound

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `erinith` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 50) |
| **Started by** | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) |
| **NPCs involved** | [Erinith](../monsters/erinith.md) |
| **Locations** | [wild0](../maps/wild0.md) |
| **Total XP** | 1,200 |

</div>

## Overview

> Just northeast of Crossglen village, I met Erinith that has set up camp. Apparently, he was attacked during the night and lost a book.

## Prerequisites to start

None: talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Just northeast of Crossglen village, I met Erinith that has set up camp. Apparently, he was attacked during the night and lost a book. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | – | – |
| <span id="stage-20"></span>20 | I have agreed to help Erinith find his book. He told me he threw it among some trees to the north of his camp. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | – | – |
| <span id="stage-21"></span>21 | I have agreed to help Erinith find his book in return for 200 gold. He told me he threw it among some trees to the north of his camp. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | – | – |
| <span id="stage-30"></span>30 | I have returned the book to Erinith. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | hand over 1× [Erinith's book](../items/erinith_book.md), stage 20 | 500 XP |
| <span id="stage-31"></span>31 | He also needs help with his wound that doesn't seem to be healing. Either I should bring him one potion of major health, or four regular potions of health. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | stage 30 | – |
| <span id="stage-40"></span>40 | I gave Erinith a bonemeal potion to heal his wound. He was a bit scared to use it since they are prohibited by Lord Geomyr. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | hand over 1× [Bonemeal potion](../items/bonemeal_potion.md), stage 30 | – |
| <span id="stage-41"></span>41 | I gave Erinith a potion of a major health to heal his wound. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | hand over 1× [Major potion of health](../items/health_major2.md), stage 30 | – |
| <span id="stage-42"></span>42 | I gave Erinith four regular potions of health to heal his wound. | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | hand over 4× [Regular potion of health](../items/health.md), stage 30 | – |
| <span id="stage-50"></span>50 | The wound healed completely and Erinith thanked me for all the help. **(completes quest)** | [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) | stage 40 | 700 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “What's wrong?” → **stage 10**. NPC: “I was setting up camp here during the night, and was attacked by some bandits while asleep.”

???+ note "Stage 20: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “I could help you find that book if you want.” → **stage 20**. NPC: “You would? Oh thank you.”

???+ note "Stage 21: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “200 gold it is then. I'll go look for your book.” → **stage 21**. NPC: “Make it quick.”

???+ note "Stage 30: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “Yes, here is your book.” — **conditions:** reached stage 20 of [Deep wound](../quests/erinith.md#stage-20); hand over 1× [Erinith's book](../items/erinith_book.md) → **stage 30**

???+ note "Stage 31: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Deep wound](../quests/erinith.md#stage-30) → **stage 31**. NPC: “One of those would surely do. Otherwise, I think four regular potions of health would be enough.”

???+ note "Stage 40: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “Here, take this bonemeal potion instead. It's very potent in healing deep wounds.” — **conditions:** reached stage 30 of [Deep wound](../quests/erinith.md#stage-30); hand over 1× [Bonemeal potion](../items/bonemeal_potion.md) → **stage 40**. NPC: “Bonemeal potion? But ... but ... we are not allowed to use them since they are prohibited by Lord Geomyr.”

???+ note "Stage 41: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “Here, take this major potion of health.” — **conditions:** reached stage 30 of [Deep wound](../quests/erinith.md#stage-30); hand over 1× [Major potion of health](../items/health_major2.md) → **stage 41**. NPC: “Thank you for bringing me one. [Drinks potion]”

???+ note "Stage 42: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → choose “Here, take these four regular potions of health.” — **conditions:** reached stage 30 of [Deep wound](../quests/erinith.md#stage-30); hand over 4× [Regular potion of health](../items/health.md) → **stage 42**. NPC: “Thank you for bringing them to me. [Drinks all four potions]”

???+ note "Stage 50: 1 route"

    1. Talk to [Erinith](../monsters/erinith.md) ([wild0](../maps/wild0.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Deep wound](../quests/erinith.md#stage-40) → **stage 50**. NPC: “Thank you my friend for your help. My book is safe and my wound is healing. I hope our paths will cross again.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “Bonemeal potion? But.. but.. We are not allowed to use them since the…” → “Bonemeal potion? But ... but ... we are not allowed to use them since…”<br>· text: “Thank you for bringing me one. *drinks potion*” → “Thank you for bringing me one. [Drinks potion]” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=erinith.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=erinith.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=erinith.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=erinith.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=erinith.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `erinith` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 31, 40, 41, 42, 50 |
    | Dialogue nodes setting stages | 10: `erinith_story_1`, 20: `erinith_story_7`, 21: `erinith_story_gold_2`, 30: `erinith_needsbook_2`, 31: `erinith_needspotions_6`, 40: `erinith_gavepotion_bm_1`, 41: `erinith_gavepotion_major_1`, 42: `erinith_gavepotion_reg_1`, 50: `erinith_givenpotion_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
