# A familiar shadow

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `familiar_shadow` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 70) |
| **Started by** | walking into a blocked passage on [galmore_32](../maps/galmore_32.md) |
| **NPCs involved** | [Leta](../monsters/leta.md), [Mikhail](../monsters/mikhail.md), [Old Leta](../monsters/old_leta.md), [Old Oromir](../monsters/old_oromir.md) |
| **Locations** | [crossglen_farmhouse](../maps/crossglen_farmhouse.md), [home](../maps/home.md), [waytogalmore0](../maps/waytogalmore0.md) |
| **Total XP** | 6,548 |
| **Related quests** | 5 |

</div>

## Overview

> In the devastated lands south of Stoutford, I found an ominous stone etched with strange symbols.

## Prerequisites to start

Start with walking into a blocked passage on [galmore_32](../maps/galmore_32.md). Required:

- NOT reached stage 10 of [A familiar shadow](../quests/familiar_shadow.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Thief apprentice](Thieves01.md#stage-60) | stage 60 reached, for stage 10 here |
| Requires | [Missing husband](leta.md#stage-100) | stage 100 reached, for stage 10 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [You're the postman](postman.md#stage-10) | stage 10 reached, for stage 10 here |
| Blocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-1) | reaching stage 50 here closes stage 1 there |
| Blocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-2) | reaching stage 50 here closes stage 2 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | In the devastated lands south of Stoutford, I found an ominous stone etched with strange symbols. | walking into a blocked passage on [galmore_32](../maps/galmore_32.md) | – | – |
| <span id="stage-10"></span>10 | As I touched its glowing mark, an unnatural chill ran through me, and I heard a voice in my mind, calling out for help. It spoke of torment and told me to return to Crossglen to find answers.<br><span class="qnote">🔒 An area on [Galmore 32](../maps/galmore_32.md) becomes blocked off.</span> | walking into a blocked passage on [galmore_32](../maps/galmore_32.md) | – | applies condition pull_of_the_mark<br>applies condition fear<br>removes monsters from galmore_32 |
| <span id="stage-20"></span>20 | The presence of the mark grows unbearable. I feel an overwhelming pull to return to Crossglen. There is something wrong, and I sense it's tied to my father. I must hurry to see what's happening.<br><span class="qnote">🔒 An area on [Crossglen](../maps/crossglen.md) becomes blocked off.</span> | walking into a blocked passage on [galmore_32](../maps/galmore_32.md) | – | spawns monsters on galmore_32 |
| <span id="stage-30"></span>30 | I spoke to father. He assured me he's fine, but mentioned Leta hasn't been herself lately. She's been pacing her home and muttering to herself. I should check on her and see what's going on. | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | When I confronted Leta, she seemed different--angrier, more agitated. As I pressed her, a dark spirit suddenly manifested before me and attacked. | [Leta](../monsters/leta.md) | stage 30 | spawns monsters on crossglen_farmhouse<br>removes monsters from crossglen_farmhouse<br>removes monsters from crossglen_farmhouse_basement<br>removes monsters from crossglen |
| <span id="stage-50"></span>50 | I defeated the Dark spirit, but it didn't feel like the end. The Dark spirit trapped inside Leta has fled back to the devastated lands south of Stoutford, where its power can grow stronger. I need to return there and finish what I started.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [crossglen](../maps/crossglen.md) | – | spawns monsters on galmore_32 |
| <span id="stage-60"></span>60 | In the depths of the devastated lands south of Stoutford, I found the dark spirit waiting for me. It was stronger this time, but I defeated it once and for all. Whatever bond it had with me and Leta is broken. I should check-up on Leta again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Galmore 32](../maps/galmore_32.md).</span> | stepping on a trigger on [galmore_32](../maps/galmore_32.md) | – | spawns monsters on crossglen_farmhouse<br>spawns monsters on crossglen_farmhouse_basement<br>applies condition pull_of_the_mark<br>removes monsters from galmore_32 |
| <span id="stage-70"></span>70 | I returned to Crossglen to find everything changed. Leta has aged decades in an instant. Her child is now fully grown, and her timid husband, Oromir, seems like a different man entirely. They remember nothing of what happened. The spirit may be gone, but its curse has left a permanent mark on the lives it touched. **(completes quest)** | [Old Leta](../monsters/old_leta.md) ([crossglen_farmhouse](../maps/crossglen_farmhouse.md))<br>[Old Oromir](../monsters/old_oromir.md) ([crossglen_farmhouse](../maps/crossglen_farmhouse.md)) | stage 60 | 6,548 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 5: 1 route"

    1. walking into a blocked passage on [galmore_32](../maps/galmore_32.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [A familiar shadow](../quests/familiar_shadow.md#stage-10) → **stage 5**

???+ note "Stage 10: 1 route"

    1. walking into a blocked passage on [galmore_32](../maps/galmore_32.md) → choose “[Touch the stone.]” — **conditions:** NOT reached stage 10 of [A familiar shadow](../quests/familiar_shadow.md#stage-10); reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60); reached stage 100 of [Missing husband](../quests/leta.md#stage-100); reached stage 10 of [You're the postman](../quests/postman.md#stage-10) → **stage 10**; also applies condition pull_of_the_mark, applies condition fear, removes monsters from galmore_32, removes monsters from galmore_32. NPC: “The moment your hand meets the mark, an icy jolt shoots through your body. A voice echoes in your mind, low and…”

???+ note "Stage 20: 1 route"

    1. walking into a blocked passage on [galmore_32](../maps/galmore_32.md) → the conversation leads here automatically → **stage 20**; also spawns monsters on galmore_32, spawns monsters on galmore_32. NPC: “The weight of the mark grows heavier on your mind. A strange, oppressive feeling claws at your chest, urging you to…”

???+ note "Stage 30: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “I don't know...something feels wrong. I thought maybe you were in danger.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-20) is 20 → **stage 30**. NPC: “What's gotten into you? I'm fine, but the same can't be said for Leta. I've seen her pacing in that house of hers,…”

???+ note "Stage 40: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “Leta, talk to me. What's going on?” — **conditions:** reached stage 30 of [A familiar shadow](../quests/familiar_shadow.md#stage-30) → **stage 40**; also spawns monsters on crossglen_farmhouse, removes monsters from crossglen_farmhouse, removes monsters from crossglen_farmhouse_basement, removes monsters from crossglen, removes monsters from crossglen_farmhouse_basement. NPC: “A dark aura surrounds Leta as a spirit begins its manifestation. Leta lets out a cry and vanishes as the spirit rises.”

???+ note "Stage 50: 1 route"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** killed 1× [Dark spirit](../monsters/crossglen_dark_spirit.md); NOT reached stage 50 of [A familiar shadow](../quests/familiar_shadow.md#stage-50) → **stage 50**; also spawns monsters on galmore_32. NPC: “The Dark spirit has been defeated, but you feel as if this issue is unresolved. Something is telling you that it has…”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [galmore_32](../maps/galmore_32.md) → the conversation leads here automatically — **conditions:** killed 1× [Dark spirit](../monsters/undertell_dark_spirit.md); NOT reached stage 60 of [A familiar shadow](../quests/familiar_shadow.md#stage-60) → **stage 60**; also spawns monsters on crossglen_farmhouse, spawns monsters on crossglen_farmhouse_basement, applies condition pull_of_the_mark, removes monsters from galmore_32, removes monsters from galmore_32, removes monsters from galmore_32. NPC: “As the dark spirit fades, the suffocating darkness that had plagued this place begins to lift. The air feels lighter,…”

???+ note "Stage 70: 2 routes"

    1. Talk to [Old Leta](../monsters/old_leta.md) ([crossglen_farmhouse](../maps/crossglen_farmhouse.md)) → choose “I didn't do this to you. This doesn't feel right. What happened after the spirit was defeated?” — **conditions:** latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-60) is 60 → **stage 70**. NPC: “While looking between Leta and Oromir, you are unsettled by their calm acceptance. The house feels peaceful, but the…”
    2. Talk to [Old Oromir](../monsters/old_oromir.md) ([crossglen_farmhouse](../maps/crossglen_farmhouse.md)) → choose “I didn't do this to you. This doesn't feel right. What happened after the spirit was defeated?” — **conditions:** latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-60) is 60 → **stage 70**. NPC: “While looking between Leta and Oromir, you are unsettled by their calm acceptance. The house feels peaceful, but the…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=familiar_shadow.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `familiar_shadow` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 30, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 5: `galmore_marked_stone_key`, 10: `galmore_marked_stone_10`, 20: `galmore_marked_stone_20`, 30: `galmore_marked_stone_mikhail`, 40: `galmore_marked_stone_leta_narrator`, 50: `crossglen_dark_spirit_defeated_1`, 60: `galmore_dark_spirit_defeated_10`, 70: `old_oromir_and_leta_narrator_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
