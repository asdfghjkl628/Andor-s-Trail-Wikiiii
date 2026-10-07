# Devastated land

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `hadracor` |
| **In journal** | Yes |
| **Stages** | 4 (completes at 30) |
| **Started by** | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) |
| **NPCs involved** | [Hadracor](../monsters/hadracor.md) |
| **Locations** | [roadtocarntower1](../maps/roadtocarntower1.md) |
| **Related quests** | 1 |

</div>

## Overview

> On the road to Carn Tower, west of the Crossroads guardhouse, I met a group of woodcutters led by Hadracor. Hadracor wants me to help him get revenge on some wasps that were attacking them while they were cutting down the forest. To help them get revenge, I should look for giant wasps near their encampment and bring him at least five giant wasp wings.

## Prerequisites to start

Start with [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)). Required:

- reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [It makes no fence](tunlon_fence.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [It makes no fence](tunlon_fence.md#stage-32) | stage 32 there needs stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | On the road to Carn Tower, west of the Crossroads guardhouse, I met a group of woodcutters led by Hadracor. Hadracor wants me to help him get revenge on some wasps that were attacking them while they were cutting down the forest. To help them get revenge, I should look for giant wasps near their encampment and bring him at least five giant wasp wings. | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | – | – |
| <span id="stage-20"></span>20 | I have brought five giant wasp wings to Hadracor. | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | hand over 5× [Giant wasp wing](../items/hadracor_waspwing.md), stage 10 | – |
| <span id="stage-21"></span>21 | I have brought six giant wasp wings to Hadracor. For helping him, he gave me a pair of gloves. | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | hand over 6× [Giant wasp wing](../items/hadracor_waspwing.md), stage 10 | gives [Woodcutter's gloves](../items/gloves_woodcutter.md) |
| <span id="stage-30"></span>30 | Hadracor thanked me for helping him and the other woodcutters get revenge on the wasps. In return, he offered me to trade for some of his items. **(completes quest)** | [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → choose “Not yet, but I am working on it.” — **conditions:** reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10) → **stage 10**. NPC: “Good, hurry back once you are done.”

???+ note "Stage 20: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → choose “Yes, I killed five of them.” — **conditions:** reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10); hand over 5× [Giant wasp wing](../items/hadracor_waspwing.md) → **stage 20**. NPC: “Wow, you actually killed those things?”

???+ note "Stage 21: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → choose “Yes, I killed six of them.” — **conditions:** reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10); hand over 6× [Giant wasp wing](../items/hadracor_waspwing.md) → **stage 21**; also gives [Woodcutter's gloves](../items/gloves_woodcutter.md). NPC: “Wow, you actually killed six of those things? I thought there were only five, so I guess I should be even more…”

???+ note "Stage 30: 1 route"

    1. Talk to [Hadracor](../monsters/hadracor.md) ([roadtocarntower1](../maps/roadtocarntower1.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Devastated land](../quests/hadracor.md#stage-30) → **stage 30**. NPC: “As a token of our appreciation, we are willing to trade some of our equipment with you if you want.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | stage 10 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hadracor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hadracor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hadracor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hadracor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hadracor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `hadracor` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30 |
    | Dialogue nodes setting stages | 10: `hadracor_accept_3`, 20: `hadracor_wantsitems_2`, 21: `hadracor_wantsitems_3`, 30: `hadracor_complete_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
