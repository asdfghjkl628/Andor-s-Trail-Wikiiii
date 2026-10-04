# Sutdove_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `sutdover_hidden` |
| **In journal** | No (hidden flag) |
| **Stages** | 5 |
| **Started by** | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)), [Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md)) |
| **NPCs involved** | [Bonicksa](../monsters/wicked_witch_third.md), [Emmeline](../monsters/captive_girl.md), [Rennik](../monsters/wild6_house_thief.md) |
| **Locations** | [lake_shore_road_1](../maps/lake_shore_road_1.md), [wild6_house](../maps/wild6_house.md), [witch_house](../maps/witch_house.md) |
| **Related quests** | 3 |

</div>

## Overview

> PC has completed enough of 'A Wicked witch' to enable mountain teleportation crystals.

## Prerequisites to start

**Route 1** ([Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md))):

- NOT reached stage 90 of [A Wicked witch](../quests/wicked_witch.md#stage-90)
- NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95)
- NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96)

**Route 2** ([Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md))):

- latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-65) is 65


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A Wicked witch](wicked_witch.md#stage-65) | stage 65 reached, for stage 1 here |
| Blocked by | [Wanted men](wanted_men.md#stage-57) | stage 57 must NOT be reached, for stage 2 here |
| Blocked by | [A Wicked witch](wicked_witch.md#stage-90) | stage 90 must NOT be reached, for stage 1 here |
| Blocked by | [A Wicked witch](wicked_witch.md#stage-95) | stage 95 must NOT be reached, for stage 1 here |
| Blocked by | [A Wicked witch](wicked_witch.md#stage-96) | stage 96 must NOT be reached, for stage 1 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-60) | stage 60 there needs stage 2 here |
| Unlocks | [Wanted men](wanted_men.md#stage-57) | stage 57 there needs stage 2 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | PC has completed enough of 'A Wicked witch' to enable mountain teleportation crystals.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Waytogalmore0](../maps/waytogalmore0.md).</span><br><span class="qnote">🗺️ Part of [Lake shore road 0](../maps/lake_shore_road_0.md) visibly changes.</span> | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md))<br>[Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md)) | – | sets stage 80 of [A Wicked witch](../quests/wicked_witch.md#stage-80)<br>spawns monsters on lake_shore_road_0<br>changes map lake_shore_road_0<br>sets stage 70 of [A Wicked witch](../quests/wicked_witch.md#stage-70) |
| <span id="stage-2"></span>2 | The PC has been rewarded by Rennik. | [Rennik](../monsters/wild6_house_thief.md) ([wild6_house](../maps/wild6_house.md)) | – | gives [Gold coins](../items/gold.md), [Nixite crystal](../items/nixite_crystal.md) |
| <span id="stage-3"></span>3 | Sly Seraphina has sold the Armored Helmet to the PC.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lake shore road 9](../maps/lake_shore_road_9.md).</span> | stepping on a trigger on [lake_shore_road_9](../maps/lake_shore_road_9.md) | – | – |
| <span id="stage-7"></span>7 | halloween<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span><br><span class="qnote">🗺️ Part of [Crossglen](../maps/crossglen.md) visibly changes.</span> | stepping on a trigger on [crossglen](../maps/crossglen.md)<br>stepping on a trigger on [home](../maps/home.md) | – | clears stage 8 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-8)<br>removes monsters from crossglen |
| <span id="stage-8"></span>8 | xmas<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span><br><span class="qnote">🗺️ Part of [Home](../maps/home.md) visibly changes.</span> | stepping on a trigger on [crossglen](../maps/crossglen.md)<br>stepping on a trigger on [home](../maps/home.md) | – | clears stage 7 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-7)<br>spawns monsters on crossglen |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 2 routes"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → choose “What ... do I know you? You're just a young girl?” — **conditions:** NOT reached stage 90 of [A Wicked witch](../quests/wicked_witch.md#stage-90); NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95); NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96) → **stage 1**; also sets stage 80 of [A Wicked witch](../quests/wicked_witch.md#stage-80), spawns monsters on lake_shore_road_0, changes map lake_shore_road_0. NPC: “Yes, I was under a spell that made me appear as the witch. She wanted to test your heart. I'm glad you proved kind.”
    2. Talk to [Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md)) → choose “[disgruntled] Is this some kind of sick game to you?” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-65) is 65 → **stage 1**; also sets stage 70 of [A Wicked witch](../quests/wicked_witch.md#stage-70), spawns monsters on lake_shore_road_0, changes map lake_shore_road_0. NPC: “[smirks] Perhaps. But remember, hero, life's full of surprises. You may have won this time, but who's to say what lies…”

???+ note "Stage 2: 1 route"

    1. Talk to [Rennik](../monsters/wild6_house_thief.md) ([wild6_house](../maps/wild6_house.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); NOT reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2) → **stage 2**; also gives [Gold coins](../items/gold.md), [Nixite crystal](../items/nixite_crystal.md). NPC: “Ah, $playername has finally returned. Please, take this crystal and some gold as our thanks to you.”

???+ note "Stage 3: 1 route"

    1. stepping on a trigger on [lake_shore_road_9](../maps/lake_shore_road_9.md) → the conversation leads here automatically — **conditions:** NOT reached stage 3 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-3); NOT carry 0× [Armored helmet](../items/armored_helmet.md) → **stage 3**

???+ note "Stage 7: 3 routes"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** date MMDD 1031; NOT date MMDD 1102 → **stage 7**; also clears stage 8 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-8), removes monsters from crossglen
    2. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** date MMDD 1031; NOT date MMDD 1102 → **stage 7**; also clears stage 8 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-8), removes monsters from crossglen
    3. stepping on a trigger on [home](../maps/home.md) → the conversation leads here automatically — **conditions:** date MMDD 1031; NOT date MMDD 1102 → **stage 7**; also clears stage 8 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-8), removes monsters from crossglen

???+ note "Stage 8: 3 routes"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** date MMDD 1224; NOT date MMDD 1228 → **stage 8**; also clears stage 7 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-7), spawns monsters on crossglen
    2. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** date MMDD 1224; NOT date MMDD 1228 → **stage 8**; also clears stage 7 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-7), spawns monsters on crossglen
    3. stepping on a trigger on [home](../maps/home.md) → the conversation leads here automatically — **conditions:** date MMDD 1224; NOT date MMDD 1228 → **stage 8**; also clears stage 7 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-7), spawns monsters on crossglen


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 6 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | stages added: 3<br>Dialogue: 1 line added, 3 lines changed |
| [v0.8.14](../versions/0.8.14.md) | stage 1 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sutdover_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sutdover_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sutdover_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sutdover_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sutdover_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `sutdover_hidden` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 7, 8 |
    | Dialogue nodes setting stages | 1: `captive_girl_20`, 1: `wicked_witch_third_30`, 2: `thief_rennik_10`, 3: `thief_seraphina_helmet_bought`, 7: `gal_chk_h3`, 8: `gal_chk_h4` |
    | Dialogue nodes clearing stages | 8: `gal_chk_h3`, 8: `gal_chk_h9`, 7: `gal_chk_h4`, 7: `gal_chk_h9` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
