---
description: "Spies in the foam is a quest in Andor's Trail, started by Jolnor (vilegard_chapel). 4 stages, 630 XP in total. Jolnor in Vilegard chapel tells me of a guard outside of the Foaming Flask tavern, that he thinks is a spy for the Feygard royal guard. He wants me to make the guard disappear, in any wa…"
---

# Spies in the foam

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `jolnor` |
| **In journal** | Yes |
| **Stages** | 4 (completes at 30) |
| **Started by** | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) |
| **NPCs involved** | [Feygard patrol watch](../monsters/feygard_patrol_watch.md), [Jolnor](../monsters/jolnor.md) |
| **Locations** | [road1](../maps/road1.md), [vilegard_chapel](../maps/vilegard_chapel.md) |
| **Total XP** | 630 |
| **Related quests** | 1 |

</div>

## Overview

> Jolnor in Vilegard chapel tells me of a guard outside of the Foaming Flask tavern, that he thinks is a spy for the Feygard royal guard. He wants me to make the guard disappear, in any way that I see fit. The tavern should be just north of Vilegard.

## Prerequisites to start

Start with [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)). Required:

- reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Trusting an outsider](vilegard.md#stage-10) | stage 10 reached, for stage 10 here |
| Requires | [Trusting an outsider](vilegard.md#stage-20) | stage 20 reached, for stage 30 here |
| Unlocks | [Trusting an outsider](vilegard.md#stage-30) | stage 30 there needs stage 30 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Jolnor in Vilegard chapel tells me of a guard outside of the Foaming Flask tavern, that he thinks is a spy for the Feygard royal guard. He wants me to make the guard disappear, in any way that I see fit. The tavern should be just north of Vilegard. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | – | – |
| <span id="stage-20"></span>20 | I have convinced the guard outside the Foaming Flask tavern to leave after his shift ends. | [Feygard patrol watch](../monsters/feygard_patrol_watch.md) ([road1](../maps/road1.md)) | – | – |
| <span id="stage-21"></span>21 | I have started a fight with the guard outside the Foaming Flask tavern. I should bring his Feygard royal guard ring to Jolnor once he is dead to show Jolnor that he has disappeared. | [Feygard patrol watch](../monsters/feygard_patrol_watch.md) ([road1](../maps/road1.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | I have told Jolnor that the guard is now gone. **(completes quest)** | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | stage 20 | 630 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “What do you want me to do?” — **conditions:** reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10) → **stage 10**. NPC: “I want you to make sure the guard disappears somehow. How you do that is purely up to you.”

???+ note "Stage 20: 1 route"

    1. Talk to [Feygard patrol watch](../monsters/feygard_patrol_watch.md) ([road1](../maps/road1.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20) → **stage 20**. NPC: “I will go inside in a minute. Will you stand watch while I go inside?”

???+ note "Stage 21: 1 route"

    1. Talk to [Feygard patrol watch](../monsters/feygard_patrol_watch.md) ([road1](../maps/road1.md)) → choose “Good. I have been waiting for a fight!” — **conditions:** reached stage 10 of [Spies in the foam](../quests/jolnor.md#stage-10) → **stage 21**

???+ note "Stage 30: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “Yes, he will leave his post as soon as this shift is over.” — **conditions:** reached stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20); reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20) → **stage 30**. NPC: “Very good. Thank you for your help.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=jolnor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=jolnor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=jolnor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=jolnor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=jolnor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `jolnor` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30 |
    | Dialogue nodes setting stages | 10: `jolnor_gaintrust_12`, 20: `ff_outsideguard_trouble_24`, 21: `ff_outsideguard_shadow_5`, 30: `jolnor_guard_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
