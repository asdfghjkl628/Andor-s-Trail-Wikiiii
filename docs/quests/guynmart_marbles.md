# Marble hunting

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_marbles` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90) |
| **Started by** | [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) |
| **NPCs involved** | [Golden marble](../monsters/guynmart_marble4.md), [Green marble](../monsters/guynmart_marble1.md), [Pearl white marble](../monsters/guynmart_marble5.md), [Pink marble](../monsters/guynmart_marble3.md), [Red marble](../monsters/guynmart_marble2.md), [Stuephant](../monsters/guynmart_child.md) |
| **Locations** | [guynmart_wood_10](../maps/guynmart_wood_10.md) |
| **Total XP** | 1,000 |

</div>

## Overview

> Little Stuephant was crying because he lost his marbles. You told him you would find them for him.

## Prerequisites to start

None: talk to [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) to begin.

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Little Stuephant was crying because he lost his marbles. You told him you would find them for him. | [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | spawns monsters on guynmart_wood_10 |
| <span id="stage-21"></span>21 | I found a green marble. | [Green marble](../monsters/guynmart_marble1.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | gives 1× [Stuephant's marble](../items/guynmart_marble.md)<br>removes monsters from guynmart_wood_10 |
| <span id="stage-22"></span>22 | I found a red marble. | [Red marble](../monsters/guynmart_marble2.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | gives 1× [Stuephant's marble](../items/guynmart_marble.md)<br>removes monsters from guynmart_wood_10 |
| <span id="stage-23"></span>23 | I found a pink marble. | [Pink marble](../monsters/guynmart_marble3.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | gives 1× [Stuephant's marble](../items/guynmart_marble.md)<br>removes monsters from guynmart_wood_10 |
| <span id="stage-24"></span>24 | I found a golden marble. | [Golden marble](../monsters/guynmart_marble4.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | gives 1× [Stuephant's marble](../items/guynmart_marble.md)<br>removes monsters from guynmart_wood_10 |
| <span id="stage-25"></span>25 | I found a pearl white marble. | [Pearl white marble](../monsters/guynmart_marble5.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | – | gives 1× [Stuephant's marble](../items/guynmart_marble.md)<br>removes monsters from guynmart_wood_10 |
| <span id="stage-30"></span>30 | That was all of them. I should give them to Stuephant now. | [Green marble](../monsters/guynmart_marble1.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md))<br>[Red marble](../monsters/guynmart_marble2.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md))<br>[Pink marble](../monsters/guynmart_marble3.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md))<br>+2 more | stage 21, stage 22, stage 23, stage 24, stage 25 | – |
| <span id="stage-90"></span>90 | Stuephant was happy again. **(completes quest)** | [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) | hand over 5× [Stuephant's marble](../items/guynmart_marble.md), stage 21, stage 22, stage 23, stage 24, stage 25 | 1,000 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → choose “Oh dear, That is all? I will find them for you.” → **stage 10**; also spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10. NPC: “I have lost them here in the yard or in the field over there.”

???+ note "Stage 21: 1 route"

    1. Talk to [Green marble](../monsters/guynmart_marble1.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically → **stage 21**; also gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10. NPC: “I found a green marble!”

???+ note "Stage 22: 1 route"

    1. Talk to [Red marble](../monsters/guynmart_marble2.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically → **stage 22**; also gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10. NPC: “I found a red marble!”

???+ note "Stage 23: 1 route"

    1. Talk to [Pink marble](../monsters/guynmart_marble3.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically → **stage 23**; also gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10. NPC: “I found a pink marble!”

???+ note "Stage 24: 1 route"

    1. Talk to [Golden marble](../monsters/guynmart_marble4.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically → **stage 24**; also gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10. NPC: “Wow - a golden marble!”

???+ note "Stage 25: 1 route"

    1. Talk to [Pearl white marble](../monsters/guynmart_marble5.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically → **stage 25**; also gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10. NPC: “I found a pearl white marble!”

???+ note "Stage 30: 5 routes"

    1. Talk to [Green marble](../monsters/guynmart_marble1.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25) → **stage 30**. NPC: “That was the last one. I have found them all. Stuephant will be happy.”
    2. Talk to [Red marble](../monsters/guynmart_marble2.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25) → **stage 30**. NPC: “That was the last one. I have found them all. Stuephant will be happy.”
    3. Talk to [Pink marble](../monsters/guynmart_marble3.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25) → **stage 30**. NPC: “That was the last one. I have found them all. Stuephant will be happy.”
    4. Talk to [Golden marble](../monsters/guynmart_marble4.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25) → **stage 30**. NPC: “That was the last one. I have found them all. Stuephant will be happy.”
    5. Talk to [Pearl white marble](../monsters/guynmart_marble5.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25) → **stage 30**. NPC: “That was the last one. I have found them all. Stuephant will be happy.”

???+ note "Stage 90: 1 route"

    1. Talk to [Stuephant](../monsters/guynmart_child.md) ([guynmart_wood_10](../maps/guynmart_wood_10.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25); hand over 5× [Stuephant's marble](../items/guynmart_marble.md) → **stage 90**. NPC: “My lost marbles! All five! Great, thank you! [Stuephant takes the marbles]”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_marbles.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_marbles.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_marbles.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_marbles.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_marbles.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_marbles` |
    | showInLog | 1 |
    | Stage IDs | 10, 21, 22, 23, 24, 25, 30, 90 |
    | Dialogue nodes setting stages | 10: `guynmart_child_30`, 21: `guynmart_marble1_10`, 22: `guynmart_marble2_10`, 23: `guynmart_marble3_10`, 24: `guynmart_marble4_10`, 25: `guynmart_marble5_10`, 30: `guynmart_marbles_20`, 90: `guynmart_child_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
