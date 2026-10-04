# Rat infestation

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `odair` |
| **In journal** | Yes |
| **Stages** | 2 (completes at 100) |
| **Started by** | [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)) |
| **NPCs involved** | [Odair](../monsters/odair.md) |
| **Locations** | [crossglen](../maps/crossglen.md) |
| **Total XP** | 400 |
| **Related quests** | 2 |

</div>

## Overview

> Odair wants me to clear the supply cave in Crossglen village of rats. In particular, I should kill the large rat and return to Odair.

## Prerequisites to start

Start with [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)). Required:

- reached stage 10 of [Rat infestation](../quests/odair.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 there needs stage 100 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-2) | stage 2 there needs stage 100 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 there needs stage 100 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-10) | stage 10 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Odair wants me to clear the supply cave in Crossglen village of rats. In particular, I should kill the large rat and return to Odair. | [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)) | – | – |
| <span id="stage-100"></span>100 | I have helped Odair clear out the rats in the supply cave in Crossglen village. **(completes quest)** | [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)) | hand over 1× [Cave rat tail](../items/tail_caverat.md), stage 10 | 400 XP<br>gives [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 10 of [Rat infestation](../quests/odair.md#stage-10) → **stage 10**. NPC: “I need you to get into that cave and kill the large rat, that way maybe we can stop the rat infestation in the cave…”

???+ note "Stage 100: 1 route"

    1. Talk to [Odair](../monsters/odair.md) ([crossglen](../maps/crossglen.md)) → choose “Yes, I have killed the large rat.” — **conditions:** reached stage 10 of [Rat infestation](../quests/odair.md#stage-10); hand over 1× [Cave rat tail](../items/tail_caverat.md) → **stage 100**; also gives [Gold coins](../items/gold.md). NPC: “Thanks a lot for your help kid! Maybe you and that brother of yours aren't as cowardly as I thought. Here, take these…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |
| [v0.7.10](../versions/0.7.10.md) | stage 100 XP 300 → 400<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odair.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odair.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odair.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odair.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=odair.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `odair` |
    | showInLog | 1 |
    | Stage IDs | 10, 100 |
    | Dialogue nodes setting stages | 10: `odair5`, 100: `odair_complete` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
