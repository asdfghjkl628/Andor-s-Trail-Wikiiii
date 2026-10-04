# Night visit

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `farrik` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 70, 90) |
| **Started by** | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Farrik](../monsters/farrik.md), [Guard captain](../monsters/warden.md), [Thieves guild cook](../monsters/thieves_guild_cook.md) |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md), [fallhaven_prison](../maps/fallhaven_prison.md) |
| **Total XP** | 3,200 |
| **Related quests** | 4 |

</div>

## Overview

> Farrik in the Fallhaven Thieves' Guild told me of a plan to help a fellow thief escape from the Fallhaven jail.

## Prerequisites to start

None: talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) to begin.

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Beer Bootlegging](beer_bootlegging.md#stage-50) | stage 50 there needs stage 70 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-17) | stage 17 there needs stage 90 here |
| Unlocks | [A path to the Duleian Road](pathway_fallhaven.md#stage-20) | stage 20 there needs stage 60 here |
| Unlocks | [Rumblings](rumblings.md#stage-25) | stage 25 there needs stage 70 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Farrik in the Fallhaven Thieves' Guild told me of a plan to help a fellow thief escape from the Fallhaven jail. | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-20"></span>20 | Farrik in the Fallhaven Thieves' Guild told me the details of the plan, and I accepted the task of helping him. The guard captain apparently has a drinking problem. The plan is that I get a prepared mead from the cook in the Thieves' Guild that will knock out the guard captain in the jail. I might be required to bribe the guard captain. | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-25"></span>25 | I got the prepared mead from the cook in the Thieves' Guild. | [Thieves guild cook](../monsters/thieves_guild_cook.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 20 | gives [Prepared sleepy mead](../items/sleepingmead.md) |
| <span id="stage-30"></span>30 | I told Farrik that I don't fully agree with their plan. I might tell the guard captain about their shady plan. | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-32"></span>32 | I have given the prepared mead to the guard captain. | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | hand over 1× [Prepared sleepy mead](../items/sleepingmead.md), stage 20, stage 25 | – |
| <span id="stage-40"></span>40 | I have told the guard captain of the plan that the thieves have to release their friend. | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | The guard captain wants me to tell the thieves that the security will be lowered for tonight. We might be able to catch some of the thieves. | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | – | – |
| <span id="stage-60"></span>60 | I managed to bribe the guard captain into drinking the prepared mead. He should be out during the night allowing the thieves to break their friend free. | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | pay 500 gold, stage 32 | – |
| <span id="stage-70"></span>70 | Farrik rewarded me for helping the Thieves' Guild. **(completes quest)** | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 20, stage 60 | 1,500 XP<br>removes monsters from fallhaven_prison |
| <span id="stage-80"></span>80 | I have told Farrik that the security will be lowered tonight. | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 30, stage 50 | – |
| <span id="stage-90"></span>90 | The guard captain thanked me for helping him plan to catch the thieves. He said he will also tell other guards that I helped him. **(completes quest)** | [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) | stage 50, stage 80 | 1,700 XP<br>gives [Gold coins](../items/gold.md) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “What did he do?” → **stage 10**. NPC: “I guess I can trust you with this secret. We are planning a mission tonight to help him out of jail.”

???+ note "Stage 20: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I am not done yet, but I am working on it.” — **conditions:** reached stage 20 of [Night visit](../quests/farrik.md#stage-20); NOT reached stage 30 of [Night visit](../quests/farrik.md#stage-30) → **stage 20**. NPC: “Good. Report back to me when you have gotten the guard captain to drink that special mead.”

???+ note "Stage 25: 1 route"

    1. Talk to [Thieves guild cook](../monsters/thieves_guild_cook.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Farrik said you can prepare me a round of special mead.” — **conditions:** reached stage 20 of [Night visit](../quests/farrik.md#stage-20) → **stage 25**; also gives [Prepared sleepy mead](../items/sleepingmead.md). NPC: “There. This should do it. Here you go.”

???+ note "Stage 30: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Maybe I should tell the guards that you are planning to get him out?” — **conditions:** NOT reached stage 20 of [Night visit](../quests/farrik.md#stage-20) → **stage 30**. NPC: “Whatever, they wouldn't believe you anyway.”

???+ note "Stage 32: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “I brought some with me if you would like to have a sip.” — **conditions:** reached stage 20 of [Night visit](../quests/farrik.md#stage-20); reached stage 25 of [Night visit](../quests/farrik.md#stage-25); hand over 1× [Prepared sleepy mead](../items/sleepingmead.md) → **stage 32**. NPC: “Oh sweet drinks of joy. I really shouldn't have this while on duty though.”

???+ note "Stage 40: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “I heard they are planning his escape tonight.” — **conditions:** reached stage 30 of [Night visit](../quests/farrik.md#stage-30) → **stage 40**. NPC: “Tonight? Thank you for this information. We will make sure to increase the security tonight then, but in such a way…”

???+ note "Stage 50: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “No, not yet. I'm working on it.” — **conditions:** reached stage 50 of [Night visit](../quests/farrik.md#stage-50) → **stage 50**. NPC: “Good. Report back to me when you have told them.”

???+ note "Stage 60: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “I have 500 gold right here that you could have.” — **conditions:** reached stage 32 of [Night visit](../quests/farrik.md#stage-32); pay 500 gold → **stage 60**. NPC: “Wow, that much gold? I'm sure I could even get away with this without being fined. Then I could have the gold AND a…”

???+ note "Stage 70: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “It is done. He should be no problem during the night.” — **conditions:** reached stage 20 of [Night visit](../quests/farrik.md#stage-20); NOT reached stage 30 of [Night visit](../quests/farrik.md#stage-30); reached stage 60 of [Night visit](../quests/farrik.md#stage-60) → **stage 70**; also removes monsters from fallhaven_prison. NPC: “That is good news! Now we should be able to get our friend out from jail tonight.”

???+ note "Stage 80: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “[Lie]. No. I went there, but I overheard the guard captain saying there was no real threat, so they will…” — **conditions:** reached stage 30 of [Night visit](../quests/farrik.md#stage-30); NOT reached stage 20 of [Night visit](../quests/farrik.md#stage-20); reached stage 50 of [Night visit](../quests/farrik.md#stage-50) → **stage 80**. NPC: “That's very useful information. Well done. You have my thanks, friend.”

???+ note "Stage 90: 1 route"

    1. Talk to [Guard captain](../monsters/warden.md) ([fallhaven_prison](../maps/fallhaven_prison.md)) → choose “Yes, they won't expect a thing.” — **conditions:** reached stage 50 of [Night visit](../quests/farrik.md#stage-50); reached stage 80 of [Night visit](../quests/farrik.md#stage-80) → **stage 90**; also gives [Gold coins](../items/gold.md). NPC: “Great. Thank you for your help. Here, take these coins as a token of our appreciation.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=farrik.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `farrik` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 32, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `farrik_11`, 20: `farrik_23`, 25: `thievesguild_cook_8`, 30: `farrik_15`, 32: `fallhaven_warden_4`, 40: `fallhaven_warden_21`, 50: `fallhaven_warden_25`, 60: `fallhaven_warden_9`, 70: `farrik_24`, 80: `farrik_26`, 90: `fallhaven_warden_31` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
