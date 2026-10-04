# Uncertain cause

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `wrye` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90) |
| **Started by** | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) |
| **NPCs involved** | [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Jolnor](../monsters/jolnor.md), [Oluag](../monsters/oluag.md), [Wrye](../monsters/wrye.md) |
| **Locations** | [foaming_flask](../maps/foaming_flask.md), [vilegard_chapel](../maps/vilegard_chapel.md), [vilegard_wrye](../maps/vilegard_wrye.md), [wild14_clearing](../maps/wild14_clearing.md) |
| **Total XP** | 720 |
| **Related quests** | 2 |

</div>

## Overview

> Jolnor in Vilegard chapel wants me to talk to Wrye in northern Vilegard. She has apparently lost her son recently.

## Prerequisites to start

Start with [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)). Required:

- reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Trusting an outsider](vilegard.md#stage-10) | stage 10 reached, for stage 10 here |
| Unlocks | [Delivery - nondisplay (hidden flag)](brv_wh_delivery_nondisplay.md#stage-80) | stage 80 there needs stage 90 here |
| Unlocks | [Trusting an outsider](vilegard.md#stage-30) | stage 30 there needs stage 90 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Jolnor in Vilegard chapel wants me to talk to Wrye in northern Vilegard. She has apparently lost her son recently. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | – | – |
| <span id="stage-20"></span>20 | Wrye in northern Vilegard tells me that her son Rincel has gone missing. She thinks that he has died or gotten critically hurt. | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | stage 40 | – |
| <span id="stage-30"></span>30 | Wrye tells me that she thinks the royal guard from Feygard are involved in his disappearance, and that they have recruited him. | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | stage 40 | – |
| <span id="stage-40"></span>40 | Wrye wants me to go search for clues as to what has happened to her son. | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | – | – |
| <span id="stage-41"></span>41 | I should go look in the Vilegard tavern and the Foaming Flask tavern north of Vilegard. | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | stage 40 | 200 XP |
| <span id="stage-42"></span>42 | I heard of a boy being in the Foaming Flask tavern a while ago. Apparently he left to the west of the tavern somewhere. | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 41 | – |
| <span id="stage-80"></span>80 | To the northwest of Vilegard I found a man that had found Rincel fighting some monsters. Rincel had apparently left Vilegard by his own will to go see the city of Feygard. I should go tell Wrye in northern Vilegard what happened to her son. | [Oluag](../monsters/oluag.md) ([wild14_clearing](../maps/wild14_clearing.md)) | stage 40 | – |
| <span id="stage-90"></span>90 | I have told Wrye the truth about her son's disappearance. **(completes quest)** | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | stage 40, stage 80 | 520 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “OK. Talk to Kaori. Got it.” — **conditions:** reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10) → **stage 10**. NPC: “She recently lost her son in a tragic way. If you can gain her trust, you will have a strong ally here.”

???+ note "Stage 20: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “Can you tell me the story about what happened again?” — **conditions:** reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40) → **stage 20**. NPC: “I can feel it in me. The Shadow speaks to me. He is dead.”

???+ note "Stage 30: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “What now?” — **conditions:** reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40) → **stage 30**. NPC: “I fear he has died or got hurt somehow. Those bastards probably drove him into his own death.”

???+ note "Stage 40: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “What can I do to help?” — **conditions:** reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40) → **stage 40**. NPC: “If you want to help me, please find out what happened to my son, Rincel.”

???+ note "Stage 41: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “Any idea where I should look?” — **conditions:** reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40) → **stage 41**. NPC: “I guess you could ask in the tavern here in Vilegard, or the Foaming Flask tavern just north of here.”

???+ note "Stage 42: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “OK, that might be something worth checking anyway.” — **conditions:** reached stage 41 of [Uncertain cause](../quests/wrye.md#stage-41) → **stage 42**. NPC: “I noticed he left to the west heading out of the Foaming Flask tavern.”

???+ note "Stage 80: 1 route"

    1. Talk to [Oluag](../monsters/oluag.md) ([wild14_clearing](../maps/wild14_clearing.md)) → choose “Maybe he didn't dare tell Wrye?” — **conditions:** reached stage 80 of [Uncertain cause](../quests/wrye.md#stage-80); reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40) → **stage 80**. NPC: “So, anyway. Now he is buried over there. Rest in peace.”

???+ note "Stage 90: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “Yes, but not for long. He did not survive the wounds. He is now buried to the northwest of Vilegard.” — **conditions:** reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40); reached stage 80 of [Uncertain cause](../quests/wrye.md#stage-80) → **stage 90**. NPC: “Oh my poor boy. What have I done?”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wrye.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wrye.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wrye.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wrye.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wrye.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `wrye` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 41, 42, 80, 90 |
    | Dialogue nodes setting stages | 10: `jolnor_gaintrust_4`, 20: `wrye_mourn_7`, 30: `wrye_story_10`, 40: `wrye_story_13`, 41: `wrye_story_16`, 42: `ff_captain_rincel_3`, 80: `oluag_grave_15`, 90: `wrye_resolved_7` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
