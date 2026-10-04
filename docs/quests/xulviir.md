# A creeping fear

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `xulviir` |
| **In journal** | Yes |
| **Stages** | 3 (completes at 20, 30) |
| **Started by** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) |
| **NPCs involved** | [Lodar](../monsters/lodar.md), [Vilegard smith](../monsters/vilegard_smith.md) |
| **Locations** | [lodarhouse1](../maps/lodarhouse1.md), [vilegard_smith](../maps/vilegard_smith.md) |
| **Total XP** | 4,000 |
| **Related quests** | 2 |

</div>

## Overview

> I was told that the broken sword that I found on the body of the Hira'zinn should be taken to the smith in Vilegard.

## Prerequisites to start

Start with [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)). Required:

- reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)
- carry 1× [Broken sword](../items/xulviir0.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Feygard errands](feygard_shipment.md#stage-56) | stage 56 reached, for stages 20, 30 here |
| Requires | [Searching for madness](lodar2.md#stage-60) | stage 60 reached, for stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I was told that the broken sword that I found on the body of the Hira'zinn should be taken to the smith in Vilegard. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | carry 1× [Broken sword](../items/xulviir0.md) | – |
| <span id="stage-20"></span>20 | I have restored the Xul'viir. I had to threaten the smith in Vilegard to get it restored. **(completes quest)** | [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) | carry 1× [Broken sword](../items/xulviir0.md), carry 3× [Oegyth crystal](../items/oegyth.md), hand over 1× [Broken sword](../items/xulviir0.md), hand over 3× [Oegyth crystal](../items/oegyth.md) | 2,000 XP<br>gives [Xul'viir](../items/xulviir.md) |
| <span id="stage-30"></span>30 | I have destroyed the Xul'viir. **(completes quest)** | [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) | carry 1× [Broken sword](../items/xulviir0.md), hand over 1× [Broken sword](../items/xulviir0.md) | 2,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “Vilegard?” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); carry 1× [Broken sword](../items/xulviir0.md) → **stage 10**. NPC: “Vilegard - yes, that's the place. You should go see the smith there. He might be able to guide you further.”

???+ note "Stage 20: 1 route"

    1. Talk to [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) → choose “I'm sure. Here is the sword and three of those crystals. Restore it to how it once was.” — **conditions:** reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56); carry 1× [Broken sword](../items/xulviir0.md); carry 3× [Oegyth crystal](../items/oegyth.md); hand over 3× [Oegyth crystal](../items/oegyth.md); hand over 1× [Broken sword](../items/xulviir0.md) → **stage 20**; also gives [Xul'viir](../items/xulviir.md). NPC: “Sigh. OK, whatever you say. We just need to fit these into there, and sharpen up this bit here. There. It should be…”

???+ note "Stage 30: 1 route"

    1. Talk to [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) → choose “Here it is. We had better get rid of it.” — **conditions:** reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56); carry 1× [Broken sword](../items/xulviir0.md); hand over 1× [Broken sword](../items/xulviir0.md) → **stage 30**. NPC: “Into the smelting pit with it. Good. See how it bubbles and flares? That's the lives of countless people thanking you…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Sigh. Ok, whatever you say. We just need to fit these into there, and…” → “Sigh. OK, whatever you say. We just need to fit these into there, and…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=xulviir.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=xulviir.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=xulviir.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=xulviir.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=xulviir.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `xulviir` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30 |
    | Dialogue nodes setting stages | 10: `lodar_xul3`, 20: `vilegard_smith_xul_19`, 30: `vilegard_smith_xul_8` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
