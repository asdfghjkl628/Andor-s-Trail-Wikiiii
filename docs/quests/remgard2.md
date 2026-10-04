# What is that stench?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `remgard2` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 45) |
| **Started by** | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) |
| **NPCs involved** | [Algangror](../monsters/algangror.md), [Ervelyn](../monsters/ervelyn.md), [Jhaeld](../monsters/jhaeld.md) |
| **Locations** | [lonelyhouse0](../maps/lonelyhouse0.md), [remgard_clothes](../maps/remgard_clothes.md), [remgard_tavern1](../maps/remgard_tavern1.md) |
| **Total XP** | 21,000 |
| **Related quests** | 4 |

</div>

## Overview

> I have told Jhaeld, the village elder in Remgard, about the woman named Algangror that lives in the abandoned house to the east along the northern shore of the lake outside Remgard.

## Prerequisites to start

Start with [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)). Required:

- reached stage 10 of [What is that stench?](../quests/remgard2.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Of mice and men](algangror.md#stage-101) | stage 101 there needs stages 10, 21 here |
| Unlocks | [The five idols](fiveidols.md#stage-100) | stage 100 there needs stage 21 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-21) | stage 21 there needs stage 45 here |
| Unlocks | [A difference of opinion](sisterfight.md#stage-10) | stage 10 there needs stage 45 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I have told Jhaeld, the village elder in Remgard, about the woman named Algangror that lives in the abandoned house to the east along the northern shore of the lake outside Remgard. | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-20"></span>20 | Jhaeld told me that he would rather not deal with her, since he believes she is very dangerous. For the sake of his guards, he will not risk going against her since he is afraid of what might happen to all of them. | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 21 | – |
| <span id="stage-21"></span>21 | If I want to help Jhaeld and the people of Remgard, I should find a way to make Algangror disappear. He also warns me to be extremely careful. | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-30"></span>30 | Algangror admitted to me that she had made some people disappear from Remgard. She would not tell me what happened to them though. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-35"></span>35 | I have started attacking Algangror. I should return to Jhaeld with proof of defeating her when she is dead. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-40"></span>40 | I have told Jhaeld that I defeated Algangror. | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | hand over 1× [Algangror's ring](../items/algangror_ring.md), stage 21, stage 35 | – |
| <span id="stage-41"></span>41 | Jhaeld was very pleased to hear the good news. The people of Remgard should now be safe, and the town can be opened to outsiders again. | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-45"></span>45 | For helping the people of Remgard find the cause of the disappearing people, Jhaeld told me to talk to Rothses. He might be able to improve some of my equipment. **(completes quest)** | [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 41 | 21,000 XP |
| <span id="stage-46"></span>46 | Ervelyn, the Remgard tailor, gave me a feathered hat as thanks for helping the people of Remgard find out what happened to the missing people. | [Ervelyn](../monsters/ervelyn.md) ([remgard_clothes](../maps/remgard_clothes.md)) | stage 45 | gives [Woodcutter's feathered hat](../items/hat_crit.md) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [What is that stench?](../quests/remgard2.md#stage-10) → **stage 10**. NPC: “If Algangror is here, this is grim news indeed.”

???+ note "Stage 20: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “So, what then?” — **conditions:** reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21) → **stage 20**. NPC: “If I were to choose, I would rather not deal with it, and just seal the town bridge as safely as possible, to prevent…”

???+ note "Stage 21: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “I am still trying to find a way to make Algangror disappear.” — **conditions:** reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21) → **stage 21**. NPC: “Remember, please be careful! I would not want to be responsible for another person disappearing.”

???+ note "Stage 30: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [What is that stench?](../quests/remgard2.md#stage-30) → **stage 30**. NPC: “Jhaeld, the fool. He hides behind his guards and his stone walls. Such a pitiful man he is. Yes, I made those people…”

???+ note "Stage 35: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 35 of [What is that stench?](../quests/remgard2.md#stage-35) → **stage 35**

???+ note "Stage 40: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “I have brought you her ring as proof that what I say is true.” — **conditions:** reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21); reached stage 35 of [What is that stench?](../quests/remgard2.md#stage-35); hand over 1× [Algangror's ring](../items/algangror_ring.md) → **stage 40**. NPC: “I can hardly believe it! Yes, this is indeed her ring.”

???+ note "Stage 41: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 41 of [What is that stench?](../quests/remgard2.md#stage-41) → **stage 41**. NPC: “This means that the people of Remgard are now safe from her, and it is all thanks to you! Who would have thought.”

???+ note "Stage 45: 1 route"

    1. Talk to [Jhaeld](../monsters/jhaeld.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “You are most welcome.” — **conditions:** reached stage 41 of [What is that stench?](../quests/remgard2.md#stage-41) → **stage 45**. NPC: “Go talk to Rothses over at the west side of town. He should be able to help you improve some of your equipment.”

???+ note "Stage 46: 1 route"

    1. Talk to [Ervelyn](../monsters/ervelyn.md) ([remgard_clothes](../maps/remgard_clothes.md)) → the conversation leads here automatically — **conditions:** reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45) → **stage 46**; also gives [Woodcutter's feathered hat](../items/hat_crit.md). NPC: “As a token of my appreciation, please accept this hat that I made. May it guide you through the blinding light.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=remgard2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=remgard2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=remgard2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=remgard2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=remgard2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `remgard2` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 35, 40, 41, 45, 46 |
    | Dialogue nodes setting stages | 10: `jhaeld_alg_3`, 20: `jhaeld_alg_20`, 21: `jhaeld_alg_26`, 30: `algangror_fight_3`, 35: `algangror_fight_6`, 40: `jhaeld_killalg_1b`, 41: `jhaeld_killalg_3`, 45: `jhaeld_killalg_6`, 46: `ervelyn_give2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
