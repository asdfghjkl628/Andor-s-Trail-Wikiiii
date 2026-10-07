---
description: "Beer Bootlegging is a quest in Andor's Trail, started by Feygard patrol captain (foaming_flask). 12 stages, 21,246 XP in total. I've agreed to help the Feygard patrol captain investigate why there is so much beer on the Foaming flask tavern property."
---

# Beer Bootlegging

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `beer_bootlegging` |
| **In journal** | Yes |
| **Stages** | 12 (completes at 90, 100, 110, 120) |
| **Started by** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) |
| **NPCs involved** | [Dunla](../monsters/dunla.md), [Farrik](../monsters/farrik.md), [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Kealwea](../monsters/sullengard_priest.md), [Mayor Ale](../monsters/sullengard_mayor.md), [Tharwyn](../monsters/tharwyn.md) +1 |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md), [foaming_flask](../maps/foaming_flask.md), [sullengard1_townhall](../maps/sullengard1_townhall.md) |
| **Total XP** | 21,246 |
| **Related quests** | 8 |

</div>

## Overview

> I've agreed to help the Feygard patrol captain investigate why there is so much beer on the Foaming flask tavern property.

## Prerequisites to start

Start with [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)). Required:

- NOT reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The ruthless Crackshot](Thieves03.md#stage-50) | stage 50 reached, for stage 40 here |
| Requires | [Night visit](farrik.md#stage-70) | stage 70 reached, for stage 50 here |
| Requires | [mg2_exploded_star_nd (hidden flag)](mg2_exploded_star_nd.md#stage-91) | stage 91 reached, for stage 70 here |
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-32) | stage 32 reached, for stage 30 here |
| Requires | [Trusting an outsider](vilegard.md#stage-30) | stage 30 reached, for stage 30 here |
| Unlocks | [Darkness in the Daylight](darkness_in_daylight.md#stage-30) | stage 30 there needs stage 120 here |
| Blocks | [The exploded star](mg2_exploded_star.md#stage-5) | reaching stage 80 here closes stage 5 there |
| Blocks | [Shadows](shadows.md#stage-10) | reaching stage 120 here closes stage 10 there |
| Blocks | [Shadows](shadows.md#stage-20) | reaching stage 120 here closes stage 20 there |
| Blocks | [Shadows](shadows.md#stage-30) | reaching stage 120 here closes stage 30 there |
| Blocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-32) | reaching stage 30 here closes stage 32 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I've agreed to help the Feygard patrol captain investigate why there is so much beer on the Foaming flask tavern property. | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | – | – |
| <span id="stage-20"></span>20 | After bribing Torilo, the owner of the Foaming flask, he stated that he and other tavern owners had a 'business agreement' with a group of 'distributors'. He suggested that I ask other tavern owners for more information. | [Torilo](../monsters/torilo.md) ([foaming_flask](../maps/foaming_flask.md)) | pay 10,000 gold, stage 10 | – |
| <span id="stage-30"></span>30 | After bribing Tharwyn, the owner of the Vilegard tavern, he stated as part of his 'business agreement', Dunla, the local thief, is one of his 'distributors'. He suggested that I talk to him. | [Tharwyn](../monsters/tharwyn.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) | – | – |
| <span id="stage-40"></span>40 | Dunla, the thief in Vilegard instructed me to speak with Farrick if I want to learn more about the tavern owner's 'business agreement' with their 'distributors'. | [Dunla](../monsters/dunla.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | Farrik told me that the beer is coming from Sullengard. I really should go there next. | [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | To earn his trust, Mayor Ale has asked that I deliver his letter to Kealwea, the Sullengard priest. | [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) | stage 50 | gives 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md) |
| <span id="stage-70"></span>70 | I have done what Mayor Ale has asked of me as I have delivered his letter. I should now return to him. | [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) | hand over 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md), stage 60 | – |
| <span id="stage-80"></span>80 | Mayor Ale has explained everything to me about the 'business agreement' with the Thieves guild. I should head back to the Foaming flask tavern and speak with the captain. | [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) | stage 70 | – |
| <span id="stage-90"></span>90 | I informed the guard captain at the Foaming flask tavern all about the beer bootlegging operation. **(completes quest)** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 10, stage 80 | 7,128 XP |
| <span id="stage-100"></span>100 | I informed the guard captain at the Foaming flask tavern that the beer was being distributed by the Thieves guild. **(completes quest)** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 10, stage 80 | 5,109 XP |
| <span id="stage-110"></span>110 | I informed the guard captain at the Foaming flask tavern that Sullengard was responsible for brewing the beer. **(completes quest)** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 10, stage 80 | 5,109 XP |
| <span id="stage-120"></span>120 | I lied to the guard captain at the Foaming flask tavern and told him nothing about the beer bootlegging operation. **(completes quest)** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 10, stage 80 | 3,900 XP<br>faction “factionCountShadow” set to 4<br>faction “factionCountThieves” set to 4<br>faction “factionCountFeygard” set to -4 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “Anything for the glorious Feygard.” — **conditions:** NOT reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10) → **stage 10**. NPC: “Great to hear. I need you to talk with the tavern owner and find out anything you can about the beer.”

???+ note "Stage 20: 1 route"

    1. Talk to [Torilo](../monsters/torilo.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “What does that mean?” — **conditions:** latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10) is 10; pay 10,000 gold → **stage 20**. NPC: “It means that that is all I will tell you and I suggest you talk to another tavern owner.”

???+ note "Stage 30: 1 route"

    1. Talk to [Tharwyn](../monsters/tharwyn.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) → choose “The thief?” — **conditions:** reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30); reached stage 32 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-32); NOT reached stage 30 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30) → **stage 30**. NPC: “That is Dunla. He gets me my beer. Go talk to him.”

???+ note "Stage 40: 1 route"

    1. Talk to [Dunla](../monsters/dunla.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) → choose “Is the Thieves guild the 'distributors'?” — **conditions:** latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30) is 30; reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50) → **stage 40**. NPC: “Yes, yes we are, but if you want to learn more, go talk to Farrik back at our guild house.”

???+ note "Stage 50: 1 route"

    1. Talk to [Farrik](../monsters/farrik.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Yes, it was 'silly' of you to do that.” — **conditions:** reached stage 70 of [Night visit](../quests/farrik.md#stage-70); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-40) is 40 → **stage 50**. NPC: “It is Sullengard, of course.”

???+ note "Stage 60: 1 route"

    1. Talk to [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) → choose “I guess you could say that.” — **conditions:** latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-50) is 50 → **stage 60**; also gives 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md). NPC: “But how can you prove it to me?...Uh, I know. You can deliver this letter for me. Here, take it to Kealwea and return…”

???+ note "Stage 70: 1 route"

    1. Talk to [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) → choose “Mayor Ale has asked me to give this letter to you.” — **conditions:** reached stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-60) is 60; hand over 1× [Mayor Ale's letter](../items/sullengard_mayor_letter.md) → **stage 70**. NPC: “Oh, I've been expecting this. Thank you.”

???+ note "Stage 80: 2 routes"

    1. Talk to [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) → choose “I can't argue with that logic.” — **conditions:** latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-70) is 70 → **stage 80**. NPC: “Please keep this information to yourself.”
    2. Talk to [Mayor Ale](../monsters/sullengard_mayor.md) ([sullengard1_townhall](../maps/sullengard1_townhall.md)) → choose “But you are breaking the laws of Feygard. Aren't you afraid you will get caught?” — **conditions:** latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-70) is 70 → **stage 80**. NPC: “Not as much as we fear not being able to make a living selling our beer. Plus, we have the support of the people of…”

???+ note "Stage 90: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “All that work, and the reward is just gold?” — **conditions:** reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10); NOT reached stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90); NOT reached stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100); NOT reached stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80 → **stage 90**. NPC: “Anyways, I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer…”

???+ note "Stage 100: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “Thanks and Shadow be with you.” — **conditions:** reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10); NOT reached stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90); NOT reached stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100); NOT reached stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80 → **stage 100**. NPC: “I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer…”

???+ note "Stage 110: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “Thanks!” — **conditions:** reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10); NOT reached stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90); NOT reached stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100); NOT reached stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80 → **stage 110**. NPC: “I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer…”

???+ note "Stage 120: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “That's the thing, I don't 'know' anything that I could prove.” — **conditions:** reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10); NOT reached stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90); NOT reached stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100); NOT reached stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120); latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80 → **stage 120**; also faction “factionCountShadow” set to 4, faction “factionCountThieves” set to 4, faction “factionCountFeygard” set to -4. NPC: “I knew that you would be a waste of my time. I'll reward you with nothing.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 13 lines added |
| [v0.8.3](../versions/0.8.3.md) | stage 20 journal text changed; stage 80 journal text changed; stage 90 journal text changed; stage 100 journal text changed; stage 110 journal text changed; stage 120 journal text changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=beer_bootlegging.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=beer_bootlegging.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=beer_bootlegging.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=beer_bootlegging.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=beer_bootlegging.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `beer_bootlegging` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 |
    | Dialogue nodes setting stages | 10: `ff_captain_beer_100`, 20: `torilo_beer_pay_10`, 30: `tharwyn_beer_70`, 40: `dunla_beer_30`, 50: `farrik_beer_town_10`, 60: `sullengard_mayor_beer_35`, 70: `sullengard_kealwea_letter`, 80: `sullengard_mayor_beer_115`, 80: `sullengard_mayor_beer_120`, 90: `ff_captain_beer_tell_everything_60`, 100: `ff_captain_beer_tell_sull_30`, 110: `ff_captain_beer_tell_thieves_20`, 120: `ff_captain_beer_tell_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
