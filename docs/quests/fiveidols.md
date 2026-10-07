---
description: "The five idols is a quest in Andor's Trail, started by Algangror (lonelyhouse0). 20 stages, 21,000 XP in total. Algangror wants me to help her with a task. She cannot describe the nature of the task, or the reasoning behind it. If I help her, she has promised to give me her enchanted necklace, th…"
---

# The five idols

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fiveidols` |
| **In journal** | Yes |
| **Stages** | 20 (completes at 70, 100) |
| **Started by** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) |
| **NPCs involved** | [Algangror](../monsters/algangror.md) |
| **Locations** | [lonelyhouse0](../maps/lonelyhouse0.md) |
| **Total XP** | 21,000 |
| **Related quests** | 3 |

</div>

## Overview

> Algangror wants me to help her with a task. She cannot describe the nature of the task, or the reasoning behind it. If I help her, she has promised to give me her enchanted necklace, that apparently is worth a lot.

## Prerequisites to start

Start with [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)). Required:

- reached stage 21 of [Of mice and men](../quests/algangror.md#stage-21)
- reached stage 75 of [Everything in order](../quests/remgard.md#stage-75)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Of mice and men](algangror.md#stage-15) | stage 15 reached, for stage 100 here |
| Requires | [Of mice and men](algangror.md#stage-21) | stage 21 reached, for stages 10, 20 here |
| Requires | [Of mice and men](algangror.md#stage-100) | stage 100 reached, for stage 100 here |
| Requires | [Everything in order](remgard.md#stage-75) | stage 75 reached, for stages 10, 20 here |
| Requires | [What is that stench?](remgard2.md#stage-21) | stage 21 reached, for stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Algangror wants me to help her with a task. She cannot describe the nature of the task, or the reasoning behind it. If I help her, she has promised to give me her enchanted necklace, that apparently is worth a lot. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-20"></span>20 | I have agreed to help Algangror with her task. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-30"></span>30 | Algangror wants me to place five idols near five different people in Remgard. The idols should be placed near the beds of these five people, and must be hidden so that they are not found easily. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-31"></span>31 | The first person is Jhaeld, the village elder that can be found in the Remgard tavern. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-32"></span>32 | Second, I should place an idol by the bed of Larni the farmer, that lives in one of the northern cabins in Remgard. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-33"></span>33 | The third person is Arnal the weapon-smith, that lives in the northwest of Remgard. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-34"></span>34 | Fourth is Emerei, that can be found to the southeast of Remgard. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-35"></span>35 | The fifth person is Carthe. Carthe lives on the eastern shore of Remgard, near the tavern. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37 | – |
| <span id="stage-37"></span>37 | I must not tell anyone of my task, or of the placement of the idols. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | gives [Small idol](../items/algangror_idol.md) |
| <span id="stage-41"></span>41 | I have placed an idol by Jhaeld's bed. | reading a sign on [remgard_tavern1](../maps/remgard_tavern1.md) | hand over 1× [Small idol](../items/algangror_idol.md), stage 31 | – |
| <span id="stage-42"></span>42 | I have placed an idol by Larni the farmer's bed. | reading a sign on [remgard_farmer1](../maps/remgard_farmer1.md) | hand over 1× [Small idol](../items/algangror_idol.md), stage 32 | – |
| <span id="stage-43"></span>43 | I have placed an idol by Arnal's bed. | reading a sign on [remgard_weapon](../maps/remgard_weapon.md) | hand over 1× [Small idol](../items/algangror_idol.md), stage 33 | – |
| <span id="stage-44"></span>44 | I have placed an idol by Emerei's bed. | reading a sign on [remgard_villager3](../maps/remgard_villager3.md) | hand over 1× [Small idol](../items/algangror_idol.md), stage 34 | – |
| <span id="stage-45"></span>45 | I have placed an idol by Carthe's bed. | reading a sign on [remgard_farmer2](../maps/remgard_farmer2.md) | hand over 1× [Small idol](../items/algangror_idol.md), stage 35 | – |
| <span id="stage-50"></span>50 | All the idols have been placed by the beds of the people that Algangror told me to visit. I should return to Algangror. | reading a sign on [remgard_tavern1](../maps/remgard_tavern1.md)<br>reading a sign on [remgard_farmer1](../maps/remgard_farmer1.md)<br>reading a sign on [remgard_weapon](../maps/remgard_weapon.md)<br>+2 more | hand over 1× [Small idol](../items/algangror_idol.md), stage 31, stage 32, stage 33, stage 34, stage 35, stage 41, stage 42, stage 43, stage 44, stage 45 | – |
| <span id="stage-51"></span>51 | Algangror thanked me for helping her. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 37, stage 50 | – |
| <span id="stage-60"></span>60 | She told me her story, with how she used to live in the city, but was persecuted for her beliefs. According to her, the persecution was totally unjustified since she does no harm to people. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 51 | – |
| <span id="stage-61"></span>61 | To take revenge on the city of Remgard, she managed to lure some people into her cabin and turn them into rats. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 51 | – |
| <span id="stage-70"></span>70 | For helping her with the tasks that she could not perform herself, Algangror gave me her enchanted necklace, 'Marrowtaint'. **(completes quest)** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 61 | 21,000 XP<br>gives [Marrowtaint](../items/marrowtaint.md) |
| <span id="stage-100"></span>100 | I have decided not to help Algangror with her task. **(completes quest)** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 10, stage 37 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Depends on the task.” — **conditions:** reached stage 21 of [Of mice and men](../quests/algangror.md#stage-21); reached stage 75 of [Everything in order](../quests/remgard.md#stage-75) → **stage 10**. NPC: “The world around you seems to move a bit slower when you wear it.”

???+ note "Stage 20: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “OK. I will help you with your task.” — **conditions:** reached stage 21 of [Of mice and men](../quests/algangror.md#stage-21); reached stage 75 of [Everything in order](../quests/remgard.md#stage-75) → **stage 20**. NPC: “Good, good.”

???+ note "Stage 30: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Can you repeat what you wanted me to do?” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 30**. NPC: “Remember, it is of utmost importance that you be as discreet as possible about this. The idols must not be found once…”

???+ note "Stage 31: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Go on.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 31**. NPC: “So, the first person that I want you to visit is Jhaeld. I hear that he spends most of his time in the Remgard tavern…”

???+ note "Stage 32: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Go on.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 32**. NPC: “Secondly, I want you to visit one of the farmers named Larni. He lives with his wife Caeda here in Remgard in one of…”

???+ note "Stage 33: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Go on.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 33**. NPC: “The third person is Arnal the weapon-smith, that lives in the northwest of Remgard.”

???+ note "Stage 34: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Go on.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 34**. NPC: “Fourth is Emerei, that can probably be found in his house to the southeast of Remgard.”

???+ note "Stage 35: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Go on.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 35**. NPC: “The fifth person is the farmer Carthe. Carthe lives on the eastern shore of Remgard, near the tavern.”

???+ note "Stage 37: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “I understand.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 37**; also gives [Small idol](../items/algangror_idol.md). NPC: “Here are the idols.”

???+ note "Stage 41: 1 route"

    1. reading a sign on [remgard_tavern1](../maps/remgard_tavern1.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 31 of [The five idols](../quests/fiveidols.md#stage-31); hand over 1× [Small idol](../items/algangror_idol.md) → **stage 41**

???+ note "Stage 42: 1 route"

    1. reading a sign on [remgard_farmer1](../maps/remgard_farmer1.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 32 of [The five idols](../quests/fiveidols.md#stage-32); hand over 1× [Small idol](../items/algangror_idol.md) → **stage 42**

???+ note "Stage 43: 1 route"

    1. reading a sign on [remgard_weapon](../maps/remgard_weapon.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 33 of [The five idols](../quests/fiveidols.md#stage-33); hand over 1× [Small idol](../items/algangror_idol.md) → **stage 43**

???+ note "Stage 44: 1 route"

    1. reading a sign on [remgard_villager3](../maps/remgard_villager3.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 34 of [The five idols](../quests/fiveidols.md#stage-34); hand over 1× [Small idol](../items/algangror_idol.md) → **stage 44**

???+ note "Stage 45: 1 route"

    1. reading a sign on [remgard_farmer2](../maps/remgard_farmer2.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 35 of [The five idols](../quests/fiveidols.md#stage-35); hand over 1× [Small idol](../items/algangror_idol.md) → **stage 45**

???+ note "Stage 50: 5 routes"

    1. reading a sign on [remgard_tavern1](../maps/remgard_tavern1.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 31 of [The five idols](../quests/fiveidols.md#stage-31); hand over 1× [Small idol](../items/algangror_idol.md); reached stage 42 of [The five idols](../quests/fiveidols.md#stage-42); reached stage 43 of [The five idols](../quests/fiveidols.md#stage-43); reached stage 44 of [The five idols](../quests/fiveidols.md#stage-44); reached stage 45 of [The five idols](../quests/fiveidols.md#stage-45) → **stage 50**
    2. reading a sign on [remgard_farmer1](../maps/remgard_farmer1.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 32 of [The five idols](../quests/fiveidols.md#stage-32); hand over 1× [Small idol](../items/algangror_idol.md); reached stage 41 of [The five idols](../quests/fiveidols.md#stage-41); reached stage 43 of [The five idols](../quests/fiveidols.md#stage-43); reached stage 44 of [The five idols](../quests/fiveidols.md#stage-44); reached stage 45 of [The five idols](../quests/fiveidols.md#stage-45) → **stage 50**
    3. reading a sign on [remgard_weapon](../maps/remgard_weapon.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 33 of [The five idols](../quests/fiveidols.md#stage-33); hand over 1× [Small idol](../items/algangror_idol.md); reached stage 41 of [The five idols](../quests/fiveidols.md#stage-41); reached stage 42 of [The five idols](../quests/fiveidols.md#stage-42); reached stage 44 of [The five idols](../quests/fiveidols.md#stage-44); reached stage 45 of [The five idols](../quests/fiveidols.md#stage-45) → **stage 50**
    4. reading a sign on [remgard_villager3](../maps/remgard_villager3.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 34 of [The five idols](../quests/fiveidols.md#stage-34); hand over 1× [Small idol](../items/algangror_idol.md); reached stage 41 of [The five idols](../quests/fiveidols.md#stage-41); reached stage 42 of [The five idols](../quests/fiveidols.md#stage-42); reached stage 43 of [The five idols](../quests/fiveidols.md#stage-43); reached stage 45 of [The five idols](../quests/fiveidols.md#stage-45) → **stage 50**
    5. reading a sign on [remgard_farmer2](../maps/remgard_farmer2.md) → choose “Hide one of the idols under the bed.” — **conditions:** reached stage 35 of [The five idols](../quests/fiveidols.md#stage-35); hand over 1× [Small idol](../items/algangror_idol.md); reached stage 41 of [The five idols](../quests/fiveidols.md#stage-41); reached stage 42 of [The five idols](../quests/fiveidols.md#stage-42); reached stage 43 of [The five idols](../quests/fiveidols.md#stage-43); reached stage 44 of [The five idols](../quests/fiveidols.md#stage-44) → **stage 50**

???+ note "Stage 51: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “No, I hid the idols as you instructed.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37); reached stage 50 of [The five idols](../quests/fiveidols.md#stage-50) → **stage 51**. NPC: “Good. Thank you again for helping me.”

???+ note "Stage 60: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “So what happened?” — **conditions:** reached stage 51 of [The five idols](../quests/fiveidols.md#stage-51) → **stage 60**. NPC: “I had little chance to argue, however. The guards led me out of the city. They did not even let me gather my things.…”

???+ note "Stage 61: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Wait, does this mean that those rats I killed for you were...” — **conditions:** reached stage 51 of [The five idols](../quests/fiveidols.md#stage-51) → **stage 61**. NPC: “So, that's my story. Thank you for listening to it.”

???+ note "Stage 70: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 61 of [The five idols](../quests/fiveidols.md#stage-61) → **stage 70**; also gives [Marrowtaint](../items/marrowtaint.md). NPC: “Here you go.”

???+ note "Stage 100: 2 routes"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “I am sent by Jhaeld to end whatever it is you do to the people of Remgard.” — **conditions:** reached stage 15 of [Of mice and men](../quests/algangror.md#stage-15); reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21); reached stage 100 of [Of mice and men](../quests/algangror.md#stage-100); reached stage 10 of [The five idols](../quests/fiveidols.md#stage-10) → **stage 100**
    2. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “I won't do your stupid task.” — **conditions:** reached stage 37 of [The five idols](../quests/fiveidols.md#stage-37) → **stage 100**. NPC: “Ah yes. After all, you are just a child and I can understand that all of this must be too much for you. Hee hee.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed<br>· text: “Ah yes. After all, you are just a child and I can understand that all…” → “Ah yes. After all, you are just a child and I can understand that all…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fiveidols.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fiveidols.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fiveidols.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fiveidols.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fiveidols.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fiveidols` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 31, 32, 33, 34, 35, 37, 41, 42, 43, 44, 45, 50, 51, 60, 61, 70, 100 |
    | Dialogue nodes setting stages | 10: `algangror_task2_4`, 20: `algangror_task2_6`, 30: `algangror_task2_10`, 31: `algangror_task2_11`, 32: `algangror_task2_12`, 33: `algangror_task2_13`, 34: `algangror_task2_14`, 35: `algangror_task2_15`, 37: `algangror_task2_18`, 41: `jhaeld_bed_4s1`, 42: `larni_bed_4s1`, 43: `arnal_bed_4s1`, 44: `emerei_bed_4s1`, 45: `carthe_bed_4s1`, 50: `jhaeld_bed_4s5`, 50: `larni_bed_4s5`, 50: `arnal_bed_4s5`, 51: `algangror_task2_done3`, 60: `algangror_story19`, 61: `algangror_story28`, 70: `algangror_cmp3`, 100: `algangror_fight_2a`, 100: `algangror_task2_n` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
