---
description: "Awoken from slumber is a quest in Andor's Trail, started by Bjorgur (blackwater_mountain26). 8 stages, 3,000 XP in total. Bjorgur in Prim at the base of the Blackwater mountain thinks that something has disturbed the grave of his parents, to the southwest of Prim, just outside the Elm mine."
---

# Awoken from slumber

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bjorgur_grave` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 50, 60) |
| **Started by** | [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) |
| **NPCs involved** | [Bjorgur](../monsters/bjorgur.md), [Fulus](../monsters/fulus.md), [Graverobber](../monsters/graverobber.md) |
| **Locations** | [blackwater_mountain26](../maps/blackwater_mountain26.md), [blackwater_mountain28](../maps/blackwater_mountain28.md), [blackwater_mountain35](../maps/blackwater_mountain35.md) |
| **Total XP** | 3,000 |

</div>

## Overview

> Bjorgur in Prim at the base of the Blackwater mountain thinks that something has disturbed the grave of his parents, to the southwest of Prim, just outside the Elm mine.

## Prerequisites to start

Start with [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)). Required:

- reached stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Bjorgur in Prim at the base of the Blackwater mountain thinks that something has disturbed the grave of his parents, to the southwest of Prim, just outside the Elm mine. | [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) | stage 15 | – |
| <span id="stage-15"></span>15 | Bjorgur wants me to go check the grave, and make sure his family's dagger is still secure in the tomb. | [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) | – | – |
| <span id="stage-20"></span>20 | Fulus in Prim is interested in obtaining Bjorgur's family dagger that Bjorgur's grandfather used to possess. | [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) | – | – |
| <span id="stage-30"></span>30 | I met a man that wielded a strange looking dagger in the lower parts of a tomb to the southwest of Prim. He must have robbed this dagger from the grave. | [Graverobber](../monsters/graverobber.md) ([blackwater_mountain35](../maps/blackwater_mountain35.md)) | – | – |
| <span id="stage-40"></span>40 | I placed the dagger back into its place in the tomb. The restless undead seem much less restless now, strangely enough. | reading a sign on [blackwater_mountain35](../maps/blackwater_mountain35.md) | hand over 1× [Bjorgur's family dagger](../items/bjorgur_dagger.md) | 200 XP |
| <span id="stage-50"></span>50 | Bjorgur thanked me for my assistance. He told me I should also seek his relatives in Feygard. **(completes quest)** | [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) | stage 15, stage 40 | 1,100 XP |
| <span id="stage-51"></span>51 | I have told Fulus that I helped Bjorgur return his family dagger to its original place. | [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) | – | – |
| <span id="stage-60"></span>60 | I have given Bjorgur's family dagger to Fulus. He thanked me for bringing it to him, and rewarded me handsomely. **(completes quest)** | [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) | hand over 1× [Bjorgur's family dagger](../items/bjorgur_dagger.md), stage 20 | 1,700 XP<br>gives [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15) → **stage 10**. NPC: “Now I fear something has happened to the grave. I have not been sleeping well the last couple of nights, and I am sure…”

???+ note "Stage 15: 1 route"

    1. Talk to [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) → choose “Sure. I will go check on your parents grave.” — **conditions:** reached stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15) → **stage 15**. NPC: “Thank you. Please see if anything has happened to the grave, and what could be the cause of my nightly anxiety.”

???+ note "Stage 20: 1 route"

    1. Talk to [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) → choose “Sounds easy enough. I'll do it.” — **conditions:** reached stage 20 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-20) → **stage 20**. NPC: “Good. Return to me once you have it. Maybe you can talk to Bjorgur about directions to the tomb. His house is just…”

???+ note "Stage 30: 1 route"

    1. Talk to [Graverobber](../monsters/graverobber.md) ([blackwater_mountain35](../maps/blackwater_mountain35.md)) → the conversation leads here automatically → **stage 30**. NPC: “Hey you! You shouldn't be here. This dagger is mine. Get out!”

???+ note "Stage 40: 1 route"

    1. reading a sign on [blackwater_mountain35](../maps/blackwater_mountain35.md) → choose “Place the dagger back into its original place.” — **conditions:** hand over 1× [Bjorgur's family dagger](../items/bjorgur_dagger.md) → **stage 40**. NPC: “You place the dagger back among the equipment, where it looks like it used to be.”

???+ note "Stage 50: 1 route"

    1. Talk to [Bjorgur](../monsters/bjorgur.md) ([blackwater_mountain26](../maps/blackwater_mountain26.md)) → choose “Yes. I killed the intruder and restored the dagger to its original place.” — **conditions:** reached stage 15 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-15); reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40) → **stage 50**. NPC: “Thank you again. I'm afraid I can't give you anything except my gratitude. You should go see my relatives in Feygard…”

???+ note "Stage 51: 1 route"

    1. Talk to [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) → the conversation leads here automatically — **conditions:** reached stage 51 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-51) → **stage 51**. NPC: “What?! Sigh. Stupid kid. That dagger is worth a fortune. We could have been rich! Rich I tell you!”

???+ note "Stage 60: 1 route"

    1. Talk to [Fulus](../monsters/fulus.md) ([blackwater_mountain28](../maps/blackwater_mountain28.md)) → choose “Yes. Here it is.” — **conditions:** reached stage 20 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-20); hand over 1× [Bjorgur's family dagger](../items/bjorgur_dagger.md) → **stage 60**; also gives [Gold coins](../items/gold.md). NPC: “Oh wow, you actually managed to get the dagger? Thank you kid. This is worth a lot. Here, take these coins as…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Stage 10 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bjorgur_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bjorgur_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bjorgur_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bjorgur_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bjorgur_grave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bjorgur_grave` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 50, 51, 60 |
    | Dialogue nodes setting stages | 10: `bjorgur_6`, 15: `bjorgur_8`, 20: `fulus_10`, 30: `bjorgur_bandit`, 40: `sign_bwm35_3`, 50: `bjorgur_complete_3`, 51: `fulus_return_3`, 60: `fulus_complete_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
