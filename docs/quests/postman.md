---
description: "You're the postman is a quest in Andor's Trail, started by Gorwath (crossglen). 5 stages, 50 XP in total. Gorwath would like me to give a letter to Arensia, in Fallhaven."
---

# You're the postman

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `postman` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 12, 30) |
| **Started by** | [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) |
| **NPCs involved** | [Arensia](../monsters/arensia.md), [Gorwath](../monsters/gorwath.md) |
| **Locations** | [crossglen](../maps/crossglen.md), [fallhaven_sw](../maps/fallhaven_sw.md) |
| **Total XP** | 50 |
| **Related quests** | 1 |

</div>

## Overview

> Gorwath would like me to give a letter to Arensia, in Fallhaven.

## Prerequisites to start

Start with [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)). Required:

- reached stage 10 of [You're the postman](../quests/postman.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [A familiar shadow](familiar_shadow.md#stage-10) | stage 10 there needs stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Gorwath would like me to give a letter to Arensia, in Fallhaven. | [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) | – | – |
| <span id="stage-12"></span>12 | But I decided not to help him with that. **(completes quest)** | [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) | stage 10 | removes monsters from crossglen |
| <span id="stage-15"></span>15 | He gave me the letter. | [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) | stage 10 | gives 1× [Gorwath's letter](../items/gorwath_letter.md) |
| <span id="stage-20"></span>20 | I gave the letter to Arensia, who was visibly happy about it. Gorwath needs to hear that. | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | carry 1× [Gorwath's letter](../items/gorwath_letter.md), hand over 1× [Gorwath's letter](../items/gorwath_letter.md) | – |
| <span id="stage-30"></span>30 | I told Gorwath that I gave the letter to Arensia. He's happy too. **(completes quest)** | [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) | stage 20 | 50 XP<br>gives 30× [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [You're the postman](../quests/postman.md#stage-10) → **stage 10**. NPC: “Would you be so kind to give her my letter?”

???+ note "Stage 12: 1 route"

    1. Talk to [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) → choose “Sorry, but I have no time. I have to find my brother now.” — **conditions:** reached stage 10 of [You're the postman](../quests/postman.md#stage-10) → **stage 12**; also removes monsters from crossglen. NPC: “Good by then. I will not disturb you anymore. * Sob *”

???+ note "Stage 15: 1 route"

    1. Talk to [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) → choose “Yeah sure, why not?” — **conditions:** reached stage 10 of [You're the postman](../quests/postman.md#stage-10) → **stage 15**; also gives 1× [Gorwath's letter](../items/gorwath_letter.md). NPC: “Thanks a lot. Here's the letter. Go to Fallhaven and look for Arensia.”

???+ note "Stage 20: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Here it is.” — **conditions:** carry 1× [Gorwath's letter](../items/gorwath_letter.md); hand over 1× [Gorwath's letter](../items/gorwath_letter.md) → **stage 20**. NPC: “[Reading] Oh that's cute. Tell Gorwath I love him too.”

???+ note "Stage 30: 1 route"

    1. Talk to [Gorwath](../monsters/gorwath.md) ([crossglen](../maps/crossglen.md)) → choose “Yes. I gave her the letter and she asked me to tell you that she loves you too.” — **conditions:** reached stage 20 of [You're the postman](../quests/postman.md#stage-20) → **stage 30**; also gives 30× [Gold coins](../items/gold.md). NPC: “You have truly earned these gold pieces.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=postman.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=postman.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=postman.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=postman.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=postman.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `postman` |
    | showInLog | 1 |
    | Stage IDs | 10, 12, 15, 20, 30 |
    | Dialogue nodes setting stages | 10: `gorwath_letter_20`, 12: `gorwath_letter_24`, 15: `gorwath_letter_50`, 20: `arensia_letter_20`, 30: `gorwath_love_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
