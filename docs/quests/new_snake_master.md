# Perception is not reality

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `new_snake_master` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 30) |
| **Started by** | [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) |
| **NPCs involved** | [Ewmondold](../monsters/inspiring_snake_master.md) |
| **Locations** | [wild2](../maps/wild2.md) |
| **Total XP** | 700 |

</div>

## Overview

> A traveler named Ewmondold had asked me to venture into the Snake Cave to retrieve his map.

## Prerequisites to start

Start with [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)). Required:

- NOT killed 1× [Snake master](../monsters/snake_master.md)
- NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | A traveler named Ewmondold had asked me to venture into the Snake Cave to retrieve his map. | [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) | – | – |
| <span id="stage-10"></span>10 | Ewmondold had thanked me for killing the Snake master, and that his way to rule would be free. I should find him. | [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) | – | removes monsters from wild2<br>spawns monsters on snakecave3 |
| <span id="stage-20"></span>20 | I've returned Ewmondold's map to him. | [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) | hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md), stage 5 | 450 XP |
| <span id="stage-25"></span>25 | I must stop Ewmondold from getting stronger. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-30"></span>30 | I've destroyed Ewmondold and eliminated his threat to Crossglen and the surrounding area. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Snakecave3](../maps/snakecave3.md).</span> | stepping on a trigger on [snakecave3](../maps/snakecave3.md) | – | 250 XP<br>gives [Gold coins](../items/gold.md) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 5: 1 route"

    1. Talk to [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) → choose “I could retrieve the map for you.” — **conditions:** NOT killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5) → **stage 5**. NPC: “Please do and hurry back to me.”

???+ note "Stage 10: 1 route"

    1. Talk to [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) → the conversation leads here automatically — **conditions:** killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5) → **stage 10**; also removes monsters from wild2, spawns monsters on snakecave3. NPC: “Thanks for killing the Snake master, sucker - the way for me to rule is now free...”

???+ note "Stage 20: 1 route"

    1. Talk to [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) → the conversation leads here automatically — **conditions:** reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); killed 1× [Snake master](../monsters/snake_master.md); hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md) → **stage 20**. NPC: “Ah, my 'map'. Good!”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [snakecave3](../maps/snakecave3.md) → the conversation leads here automatically — **conditions:** killed 1× [Ewmondold](../monsters/ewmondold_snake_master.md); NOT reached stage 30 of [Perception is not reality](../quests/new_snake_master.md#stage-30) → **stage 30**; also gives [Gold coins](../items/gold.md). NPC: “You've destroyed Ewmondold and eliminated his threat to Crossglen and the surrounding area.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.13](../versions/0.7.13.md) | stage 10 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=new_snake_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `new_snake_master` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 25, 30 |
    | Dialogue nodes setting stages | 5: `inspiring_snake_master_70`, 10: `inspiring_snake_master_20`, 20: `inspiring_snake_master_80`, 30: `ewmondold_snake_master_defeted_script_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
