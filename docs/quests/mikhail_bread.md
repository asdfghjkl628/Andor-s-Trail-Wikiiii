# Breakfast bread

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `mikhail_bread` |
| **In journal** | Yes |
| **Stages** | 2 (completes at 100) |
| **Started by** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) |
| **NPCs involved** | [Mikhail](../monsters/mikhail.md) |
| **Locations** | [home](../maps/home.md), [waytogalmore0](../maps/waytogalmore0.md) |
| **Total XP** | 30 |
| **Related quests** | 9 |

</div>

## Overview

> Mikhail wants me to go buy a loaf of bread from Mara at the town hall.

## Prerequisites to start

Start with [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)). Required:

- reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10)
- NOT reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100)
- reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Rats!](mikhail_rats.md#stage-100) | stage 100 reached, for stage 10 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-1) | stage 1 there needs stages 10, 100 here |
| Unlocks | [Search for Andor](andor.md#stage-1) | stage 1 there needs stage 100 here |
| Unlocks | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-40) | stage 40 there needs stage 10 here |
| Unlocks | [Honor your parents](brv_present.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [Honor your parents](brv_present.md#stage-40) | stage 40 there needs stage 10 here |
| Unlocks | [Honor your parents](brv_present.md#stage-50) | stage 50 there needs stage 10 here |
| Unlocks | [Honor your parents](brv_present.md#stage-60) | stage 60 there needs stage 10 here |
| Unlocks | [Delivery - nondisplay (hidden flag)](brv_wh_delivery_nondisplay.md#stage-90) | stage 90 there needs stage 10 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-20) | stage 20 there needs stage 10 here |
| Unlocks | [A familiar shadow](familiar_shadow.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [Rats!](mikhail_rats.md#stage-10) | stage 10 there needs stages 10, 100 here |
| Unlocks | [Rats!](mikhail_rats.md#stage-100) | stage 100 there needs stage 100 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-1) | stage 1 there needs stages 10, 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Mikhail wants me to go buy a loaf of bread from Mara at the town hall. | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | – | – |
| <span id="stage-100"></span>100 | I have brought the bread to Mikhail. **(completes quest)** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | hand over 1× [Bread](../items/bread.md), stage 10 | 30 XP<br>gives [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “What about the bread?” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); NOT reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100) → **stage 10**. NPC: “Oh, I almost forgot. If you have time, please go see Mara at the town hall and buy me some more bread.”

???+ note "Stage 100: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Yes, here you go.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); hand over 1× [Bread](../items/bread.md) → **stage 100**; also gives [Gold coins](../items/gold.md). NPC: “Thanks a lot, now I can make my breakfast. Here, take these coins for your help.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | stage 100 XP 0 → 30<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mikhail_bread.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mikhail_bread.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mikhail_bread.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mikhail_bread.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mikhail_bread.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `mikhail_bread` |
    | showInLog | 1 |
    | Stage IDs | 10, 100 |
    | Dialogue nodes setting stages | 10: `mikhail_bread_start`, 100: `mikhail_bread_complete` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
