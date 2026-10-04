# The Dead are Walking

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `dead_walking` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 70) |
| **Started by** | [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) |
| **NPCs involved** | [Gabriel](../monsters/gabriel.md) |
| **Locations** | [vilegard_s](../maps/vilegard_s.md) |
| **Total XP** | 7,000 |

</div>

## Overview

> Gabriel, the acolyte in Vilegard has asked me to investigate the sounds that only he is hearing.

## Prerequisites to start

Start with [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)). Required:

- NOT reached stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0)

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-0"></span>0 | Gabriel, the acolyte in Vilegard has asked me to investigate the sounds that only he is hearing.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Way to sullengard east1](../maps/way_to_sullengard_east1.md).</span> | [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) | – | – |
| <span id="stage-10"></span>10 | Off of the Duleian road, just east of Vilegard, I noticed that the moaning sounds seem just a little bit louder.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road2](../maps/road2.md).</span> | stepping on a trigger on [road2](../maps/road2.md) | stage 0 | 500 XP |
| <span id="stage-20"></span>20 | Off of the Duleian road, just south of Alynndir's cabin, I noticed that the moaning sounds seem just a little bit louder.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Road5](../maps/road5.md).</span> | stepping on a trigger on [road5](../maps/road5.md) | stage 0 | 500 XP |
| <span id="stage-40"></span>40 | I discovered the 'Haunted forest' and suspect that this may be the source of the sounds heard by Gabriel in Vilegard.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Haunted forest1](../maps/haunted_forest1.md).</span> | stepping on a trigger on [haunted_forest1](../maps/haunted_forest1.md) | – | – |
| <span id="stage-50"></span>50 | In the haunted house's basement, I discovered Benzimos (and he discovered me) while chanting some kind of ritual. He must be stopped.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Haunted house basement](../maps/haunted_house_basement.md).</span> | stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) | – | applies condition fear |
| <span id="stage-60"></span>60 | Now that Benzimos is "dead" again, I should return to Vilegard and speak with Gabriel.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Haunted house basement](../maps/haunted_house_basement.md).</span> | stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) | – | – |
| <span id="stage-70"></span>70 | Gabriel was eternally grateful that I was able to prevent Benzimos' pack of undead from their potential attack on Vilegard. **(completes quest)** | [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) | stage 60 | 6,000 XP<br>gives [Gold coins](../items/gold.md)<br>faction “factionCountShadow” set to 2 |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 0: 1 route"

    1. Talk to [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) → choose “Of course. Anything for the Shadow.” — **conditions:** NOT reached stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0) → **stage 0**. NPC: “Outstanding. Report back to me when you are done.”

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [road2](../maps/road2.md) → choose “What an eerie sound ...” — **conditions:** reached stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0); NOT reached stage 40 of [The Dead are Walking](../quests/dead_walking.md#stage-40) → **stage 10**. NPC: “Now you notice that the moaning heard by Gabriel is a little louder here.”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [road5](../maps/road5.md) → choose “I should stick around a little bit longer.” — **conditions:** reached stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0); NOT reached stage 20 of [The Dead are Walking](../quests/dead_walking.md#stage-20) → **stage 20**. NPC: “Now you begin to notice that the moaning heard by Gabriel is a little louder here.”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [haunted_forest1](../maps/haunted_forest1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 40 of [The Dead are Walking](../quests/dead_walking.md#stage-40) → **stage 40**. NPC: “As you enter this dark place, you suspect that you are getting closer to the sounds heard by Gabriel as the moaning is…”

???+ note "Stage 50: 1 route"

    1. stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) → the conversation leads here automatically — **conditions:** NOT reached stage 50 of [The Dead are Walking](../quests/dead_walking.md#stage-50) → **stage 50**; also applies condition fear. NPC: “Again, yelling in a language that you do not understand. You begin to tremble in fear.”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) → the conversation leads here automatically — **conditions:** killed 1× [Benzimos](../monsters/haunted_benzimos.md); NOT reached stage 60 of [The Dead are Walking](../quests/dead_walking.md#stage-60) → **stage 60**. NPC: “Benzimos is now dead ... again.”

???+ note "Stage 70: 2 routes"

    1. Talk to [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) → choose “How 'grateful' are you?” — **conditions:** latest stage of [The Dead are Walking](../quests/dead_walking.md#stage-60) is 60 → **stage 70**; also gives [Gold coins](../items/gold.md). NPC: “Very! In fact, here are 3,000 gold pieces for all your trouble.”
    2. Talk to [Gabriel](../monsters/gabriel.md) ([vilegard_s](../maps/vilegard_s.md)) → choose “I will do anything for the Shadow.” — **conditions:** latest stage of [The Dead are Walking](../quests/dead_walking.md#stage-60) is 60 → **stage 70**; also faction “factionCountShadow” set to 2. NPC: “Walk with the Shadow, my child.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dead_walking.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dead_walking.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dead_walking.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dead_walking.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=dead_walking.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `dead_walking` |
    | showInLog | 1 |
    | Stage IDs | 0, 10, 20, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 0: `gabriel_daw_100`, 10: `road2_daw_20`, 20: `road5_daw_20`, 40: `haunted_forest_discovery_script_10`, 50: `haunted_house_basement_script_30`, 60: `haunted_benzimos_death_10`, 70: `gabriel_daw_complete_50`, 70: `gabriel_daw_complete_49` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
