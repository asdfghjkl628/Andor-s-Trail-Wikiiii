# The path is clear to me

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `rogorn` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 60) |
| **Started by** | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) |
| **NPCs involved** | [Minarra](../monsters/minarra.md), [Rogorn](../monsters/rogorn.md) |
| **Locations** | [houseatcrossroads4](../maps/houseatcrossroads4.md), [roadtocarntower2](../maps/roadtocarntower2.md) |
| **Related quests** | 2 |

</div>

## Overview

> Minarra up in the tower at the Crossroads guardhouse has seen a band of rogues heading west from the guardhouse, towards Carn Tower. Minarra was sure they matched the description of some men whose heads have a bounty on them from the Feygard patrol. If these are the men that Minarra thinks, they are supposedly led by particularly ruthless savage named Rogorn.

## Prerequisites to start

Start with [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)). Required:

- reached stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Flows through the veins](loneford.md#stage-10) | stage 10 there needs stage 20 here |
| Unlocks | [Flows through the veins](loneford.md#stage-11) | stage 11 there needs stage 20 here |
| Unlocks | [Flows through the veins](loneford.md#stage-21) | stage 21 there needs stage 20 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-18) | stage 18 there needs stage 60 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Minarra up in the tower at the Crossroads guardhouse has seen a band of rogues heading west from the guardhouse, towards Carn Tower. Minarra was sure they matched the description of some men whose heads have a bounty on them from the Feygard patrol. If these are the men that Minarra thinks, they are supposedly led by particularly ruthless savage named Rogorn. | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | – | – |
| <span id="stage-20"></span>20 | I am helping Minarra find the band of rogues. I should travel the road west from the Crossroads guardhouse towards Carn Tower and look for them. They have supposedly stolen three pieces of a valuable painting and are wanted dead for their crimes. | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | stage 10 | – |
| <span id="stage-21"></span>21 | Minarra also tells me that I should not trust anything I hear from them. In particular, anything from Rogorn should be viewed with great suspicion. | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | I have found the band of rogues on the road west towards Carn Tower, led by Rogorn. | [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) | stage 20 | – |
| <span id="stage-35"></span>35 | Rogorn tells me that they are wrongly accused of murder and theft in Feygard, while they themselves have never even been to Feygard. | [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) | – | – |
| <span id="stage-40"></span>40 | I have decided to attack Rogorn and his band of rogues. I should return to Minarra with the three pieces of the painting once they are dead. | [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) | – | – |
| <span id="stage-45"></span>45 | I have decided not to attack Rogorn and his band of rogues, but instead report back to Minarra that she must have mistaken the men she saw for someone else. | [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) | – | – |
| <span id="stage-50"></span>50 | Minarra thanked me for dealing with the thieves, and told me that my services to Feygard will be appreciated. | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | hand over 3× [Piece of painting](../items/rogorn_qitem.md), stage 20, stage 40 | – |
| <span id="stage-55"></span>55 | After telling Minarra that she must have mistaken the men for someone else, she seemed a bit suspicious, but thanked me for helping her look into the matter. | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | stage 20, stage 45 | – |
| <span id="stage-60"></span>60 | I have helped Minarra with her task. **(completes quest)** | [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | stage 55 | – |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “Can you tell me again about those men you saw?” — **conditions:** reached stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10) → **stage 10**. NPC: “I am sure that those were the men. If we were to catch and kill them, the people of Feygard would be much safer.”

???+ note "Stage 20: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I could go look for them if you want.” — **conditions:** reached stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10) → **stage 20**. NPC: “They have stolen three pieces of a very valuable painting from Feygard, from the report that I have read. For their…”

???+ note "Stage 21: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I will be back once they are dead. Anything else?” — **conditions:** reached stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10) → **stage 21**. NPC: “I urge you not to listen to their lies. Their crimes must be punished in order to uphold the law.”

???+ note "Stage 30: 1 route"

    1. Talk to [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) → choose “I am looking for a group of men led by someone by the name of Rogorn. Are you him?” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20) → **stage 30**. NPC: “That depends, why do you want to know?”

???+ note "Stage 35: 1 route"

    1. Talk to [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) → choose “Can you tell me your side of the story again?” — **conditions:** reached stage 35 of [The path is clear to me](../quests/rogorn.md#stage-35) → **stage 35**. NPC: “However, something must have upset the guards there anyway. Now we hear that we are accused of murder and theft in…”

???+ note "Stage 40: 1 route"

    1. Talk to [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40) → **stage 40**. NPC: “I had hoped it would not come to this. For the Shadow!”

???+ note "Stage 45: 1 route"

    1. Talk to [Rogorn](../monsters/rogorn.md) ([roadtocarntower2](../maps/roadtocarntower2.md)) → choose “What now? I was sent here to find you by some guards in the Crossroads guardhouse.” — **conditions:** reached stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45) → **stage 45**. NPC: “You tell those guards that you searched for us, but did not find anyone.”

???+ note "Stage 50: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “Yes, I killed them and recovered the three pieces of the painting.” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20); reached stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40); hand over 3× [Piece of painting](../items/rogorn_qitem.md) → **stage 50**. NPC: “That is excellent news indeed! I knew that we could trust you.”

???+ note "Stage 55: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I travelled west and found a travelling group of men, but they did not match the men you described.” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20); reached stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45) → **stage 55**. NPC: “I guess I will have to take your word for it.”

???+ note "Stage 60: 1 route"

    1. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → the conversation leads here automatically — **conditions:** reached stage 55 of [The path is clear to me](../quests/rogorn.md#stage-55) → **stage 60**. NPC: “Thank you for helping me investigate this matter.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rogorn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rogorn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rogorn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rogorn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rogorn.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `rogorn` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 35, 40, 45, 50, 55, 60 |
    | Dialogue nodes setting stages | 10: `minarra_story_6`, 20: `minarra_story_10`, 21: `minarra_story_13`, 30: `rogorn_story_1`, 35: `rogorn_story_r_6`, 40: `rogorn_attack_1`, 45: `rogorn_story_r_10`, 50: `minarra_look_3`, 55: `minarra_look_6`, 60: `minarra_completing_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
