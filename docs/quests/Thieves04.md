# Another ruthless Crackshot

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves04` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 80) |
| **Started by** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Defy](../monsters/g04_defy.md), [Matpat](../monsters/sullengard_matpat.md), [Mayor Ale](../monsters/sullengard_mayor.md), [Umar](../monsters/umar.md) |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md), [sullengard1_northeast_house](../maps/sullengard1_northeast_house.md), [sullengard1_townhall](../maps/sullengard1_townhall.md) |
| **Total XP** | 35,000 |
| **Related quests** | 3 |

</div>

## Overview

> Umar told me to visit Defy in Sullengard to instruct him to give the villagers their share.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51)
- latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-30) | stage 30 reached, for stage 80 here |
| Mutually exclusive | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-30) | stage 30 must NOT be reached, for stage 70 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-20) | stage 20 there needs stage 10 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-28) | stage 28 there needs stage 70 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-37) | stage 37 there needs stage 75 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-39) | stage 39 there needs stage 80 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-42) | stage 42 there needs stage 80 here |
| Unlocks | [Troubling times](troubling_times.md#stage-110) | stage 110 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-130) | stage 130 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-140) | stage 140 there needs stage 75 here |
| Unlocks | [Troubling times](troubling_times.md#stage-320) | stage 320 there needs stage 75 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Umar told me to visit Defy in Sullengard to instruct him to give the villagers their share. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-20"></span>20 | Defy told me that there will be a delay in giving the villagers of Sullengard their fair share for some unknown reason. I must report this to Umar at once. | [Defy](../monsters/g04_defy.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | Umar instructed me to talk to Defy once more. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 20 | removes monsters from sullengard_tavern_basement |
| <span id="stage-35"></span>35 | Defy and his friends have vanished! Back to Umar ...<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard tavern basement](../maps/sullengard_tavern_basement.md).</span> | stepping on a trigger on [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md) | stage 30 | – |
| <span id="stage-40"></span>40 | I told Umar about the disappearance of Defy and his men. But Umar didn't believe me and he even sent me back to find them. I better ask the villagers there. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 35 | – |
| <span id="stage-50"></span>50 | There was a distressed man, whom just had his first child, who hinted to me of wherabouts of Defy and his men. I must report this to Umar once more. | [Matpat](../monsters/sullengard_matpat.md) ([sullengard1_northeast_house](../maps/sullengard1_northeast_house.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | With Sullengard running into financial trouble, Umar is enraged by Defy's traitorous way. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 50 | – |
| <span id="stage-70"></span>70 | Umar gave me a task to give the mayor at least 50000 gold coins as the promised share for their living. After that, I'm instructed to report back to him. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-75"></span>75 | Sullengard has been given their share of the gold and now it's time to revisit Umar.<br><span class="qnote">🗺️ Part of [Lake shore road 9](../maps/lake_shore_road_9.md) visibly changes.</span> | [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) | – | sets stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30) |
| <span id="stage-80"></span>80 | At last, Sullengard can now sleep calmly and eat sufficiently with their finances restored. **(completes quest)** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | 35,000 XP<br>faction “ThievesGuild” +10<br>gives 1× [Blade of the protector](../items/blade_protector.md) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “You can count on me.” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10 → **stage 10**. NPC: “Hurry now. There's no time to waste.”

???+ note "Stage 20: 1 route"

    1. Talk to [Defy](../monsters/g04_defy.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) → choose “Umar told me that it is time to give their share to the bootleg brewers.” — **conditions:** latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-10) is 10 → **stage 20**. NPC: “The time of sharing? If that's so, then tell him that there will be a delay.”

???+ note "Stage 30: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I don't know.” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-20) is 20 → **stage 30**; also removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement, removes monsters from sullengard_tavern_basement. NPC: “Sigh. He may be stubborn sometimes but he is a great supervisor. You should ask him once he is calm.”

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md) → the conversation leads here automatically — **conditions:** latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-30) is 30 → **stage 35**. NPC: “Strange. Defy and his men are gone. Maybe they talked with the bootleg brewers here and reported back to Umar?”

???+ note "Stage 40: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Defy and his men have left Sullengard.” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-35) is 35 → **stage 40**. NPC: “He can't be gone without our share from the bootleg brewers.”

???+ note "Stage 50: 1 route"

    1. Talk to [Matpat](../monsters/sullengard_matpat.md) ([sullengard1_northeast_house](../maps/sullengard1_northeast_house.md)) → choose “Calm down. I will find a way to help you.” — **conditions:** reached stage 40 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-40) → **stage 50**. NPC: “Thank you. You are my only hope here. I don't trust those unlawful Feygard soldiers. You should talk to the head of…”

???+ note "Stage 60: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Matpat told me that Defy and his men left Sullengard.” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-50) is 50 → **stage 60**. NPC: “This is madness! He betrayed us just like Crackshot did.”

???+ note "Stage 70: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “How can we earn that large amount of gold?” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); latest stage of [Another ruthless Crackshot](../quests/Thieves04.md#stage-70) is 70; NOT reached stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30) → **stage 70**. NPC: “I trust that you will find a way. In the meantime, go back to Sullengard and give them the share we promised them so…”

???+ note "Stage 75: 1 route"

    1. Talk to [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) → the conversation leads here automatically — **conditions:** faction “gold_contribute” ≥ 50000 → **stage 75**; also sets stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30). NPC: “Thank you so much again, kid. You are just like your brother Andor. After we are done speaking, you really should…”

???+ note "Stage 80: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I have given them our promised share.” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); NOT reached stage 80 of [Another ruthless Crackshot](../quests/Thieves04.md#stage-80); reached stage 30 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-30) → **stage 80**; also faction “ThievesGuild” +10, gives 1× [Blade of the protector](../items/blade_protector.md). NPC: “Good job, kid! I knew I could count on you. Here, take this blade. It used to be your brother's.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves04.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `Thieves04` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 60, 70, 75, 80 |
    | Dialogue nodes setting stages | 10: `umar_guild04_14`, 20: `guild04_defy_4`, 30: `umar_guild04_16`, 35: `guild04_defy_gone_script_grant`, 40: `umar_guild04_17`, 50: `sullengard_matpat_6`, 60: `umar_guild04_19`, 70: `umar_guild04_27`, 75: `sullengard_mayor_5`, 80: `umar_guild04_29` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
