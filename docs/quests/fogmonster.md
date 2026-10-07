---
description: "Fog in the woods is a quest in Andor's Trail, started by stepping on a trigger on guynmart_wood_13. 8 stages, 3,000 XP in total. You had entered a very unnatural looking fog and decided to find the source of it. Maybe you could lift the fog?"
---

# Fog in the woods

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fogmonster` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 70, 80, 90) |
| **Started by** | stepping on a trigger on [guynmart_wood_13](../maps/guynmart_wood_13.md), stepping on a trigger on [swamp2](../maps/swamp2.md) |
| **NPCs involved** | [Madame Mim](../monsters/swamp_witch.md), [Shiny Foggerlump](../monsters/feygard_fogmonster9.md) |
| **Locations** | [swamp3](../maps/swamp3.md), [swamp_hut](../maps/swamp_hut.md) |
| **Total XP** | 3,000 |
| **Related quests** | 1 |

</div>

## Overview

> You had entered a very unnatural looking fog and decided to find the source of it. Maybe you could lift the fog?

## Prerequisites to start

Start with stepping on a trigger on [guynmart_wood_13](../maps/guynmart_wood_13.md). Required:

- NOT reached stage 5 of [Fog in the woods](../quests/fogmonster.md#stage-5)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [feygard fog (hidden flag)](feygard_fog.md#stage-1) | stage 1 reached, for stage 20 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-1) | stage 1 must NOT be reached, for stage 10 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-2) | stage 2 must NOT be reached, for stage 10 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-3) | stage 3 must NOT be reached, for stage 10 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-4) | stage 4 must NOT be reached, for stage 10 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-5) | stage 5 must NOT be reached, for stage 10 here |
| Blocked by | [feygard fog (hidden flag)](feygard_fog.md#stage-9) | stage 9 must NOT be reached, for stage 70 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | You had entered a very unnatural looking fog and decided to find the source of it. Maybe you could lift the fog?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 13](../maps/guynmart_wood_13.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp2](../maps/swamp2.md).</span> | stepping on a trigger on [guynmart_wood_13](../maps/guynmart_wood_13.md) | – | – |
| <span id="stage-10"></span>10 | After you chased away a fog monster, the fog suddenly dissipated.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 14](../maps/guynmart_wood_14.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp2](../maps/swamp2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp4](../maps/swamp4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp5](../maps/swamp5.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp6](../maps/swamp6.md).</span> | stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md)<br>stepping on a trigger on [swamp2](../maps/swamp2.md)<br>stepping on a trigger on [swamp4](../maps/swamp4.md)<br>+2 more | – | starts timer “feygard_fogmonster1”<br>sets stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>changes map guynmart_wood_13<br>starts timer “feygard_fogmonster2”<br>sets stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2)<br>starts timer “feygard_fogmonster3”<br>sets stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3)<br>starts timer “feygard_fogmonster4”<br>sets stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4)<br>starts timer “feygard_fogmonster5”<br>sets stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5) |
| <span id="stage-20"></span>20 | Another fog monster guarded the footbridge to the hut. As long as there was still fog somewhere around the hut, you couldn't drive it away. | [Shiny Foggerlump](../monsters/feygard_fogmonster9.md) ([swamp3](../maps/swamp3.md)) | – | – |
| <span id="stage-30"></span>30 | In the hut you encountered a terrifying looking witch. | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | – |
| <span id="stage-70"></span>70 | You defeated the old witch in battle, so she can't create a new fog. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp hut](../maps/swamp_hut.md).</span> | stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) | – | sets stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9)<br>gives 1× [Quarterstaff](../items/swampwitch_staff.md) |
| <span id="stage-80"></span>80 | You were able to convince the witch Mim to keep the road clear of fog. **(completes quest)** | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | 1,000 XP<br>sets stage 8 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-8)<br>sets stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>spawns monsters on guynmart_wood_14 |
| <span id="stage-90"></span>90 | You convinced the witch Mim to replace the fog with a distraction spell. **(completes quest)** | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | 1,000 XP<br>sets stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>sets stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2)<br>sets stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3)<br>sets stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4)<br>sets stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13 |
| <span id="stage-92"></span>92 | Madame Mim gave you a bottle of her swamp water. | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | 1,000 XP<br>gives 1× [Madame Mim's Medicine](../items/swampwitch_health.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. stepping on a trigger on [guynmart_wood_13](../maps/guynmart_wood_13.md) → the conversation leads here automatically — **conditions:** NOT reached stage 5 of [Fog in the woods](../quests/fogmonster.md#stage-5) → **stage 5**. NPC: “This fog seems to be very unnatural.”

???+ note "Stage 10: 5 routes"

    1. stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md) → the conversation leads here automatically — **conditions:** NOT reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1) → **stage 10**; also starts timer “feygard_fogmonster1”, sets stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), changes map guynmart_wood_13. NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. stepping on a trigger on [swamp2](../maps/swamp2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2) → **stage 10**; also starts timer “feygard_fogmonster2”, sets stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2). NPC: “The fog vanishes completely as soon as you touch its heart.”
    3. stepping on a trigger on [swamp4](../maps/swamp4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3) → **stage 10**; also starts timer “feygard_fogmonster3”, sets stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3). NPC: “The fog vanishes completely as soon as you touch its heart.”
    4. stepping on a trigger on [swamp5](../maps/swamp5.md) → the conversation leads here automatically — **conditions:** NOT reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4) → **stage 10**; also starts timer “feygard_fogmonster4”, sets stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4). NPC: “The fog vanishes completely as soon as you touch its heart.”
    5. stepping on a trigger on [swamp6](../maps/swamp6.md) → the conversation leads here automatically — **conditions:** NOT reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5) → **stage 10**; also starts timer “feygard_fogmonster5”, sets stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5). NPC: “The fog vanishes completely as soon as you touch its heart.”

???+ note "Stage 20: 1 route"

    1. Talk to [Shiny Foggerlump](../monsters/feygard_fogmonster9.md) ([swamp3](../maps/swamp3.md)) → choose “Not for long, some of your brothers have all left the area already. Attack!” — **conditions:** reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1) → **stage 20**. NPC: “You can't defeat me as long as my brothers stand their ground.”

???+ note "Stage 30: 1 route"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → the conversation leads here automatically → **stage 30**. NPC: “Who dares disturb my solitude? Be gone, or face my wrath!”

???+ note "Stage 70: 1 route"

    1. stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) → the conversation leads here automatically — **conditions:** NOT reached stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9); killed 1× [Madame Mim](../monsters/swamp_witch.md) → **stage 70**; also sets stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9), gives 1× [Quarterstaff](../items/swampwitch_staff.md). NPC: “This area will never be bullied by the old witch again. You take the witch's staff - maybe it will find a good use as…”

???+ note "Stage 80: 1 route"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “People have trouble that the way to Feygard goes through your fog. If you make your fog a little smaller in…” → **stage 80**; also sets stage 8 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-8), sets stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), spawns monsters on guynmart_wood_14. NPC: “Agreed. Here child, take these sweets and now begone!”

???+ note "Stage 90: 1 route"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 90**; also sets stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), sets stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2), sets stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3), sets stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4), sets stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 92: 1 route"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Everlasting thankfulness” → **stage 92**; also gives 1× [Madame Mim's Medicine](../items/swampwitch_health.md). NPC: “You have it. And now go and finally leave me alone. Otherwise I'll turn you into a frog. [Muttering] Here, take this…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fogmonster.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fogmonster.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fogmonster.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fogmonster.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fogmonster.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fogmonster` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 30, 70, 80, 90, 92 |
    | Dialogue nodes setting stages | 5: `feygard_fogmonster_startquest_10`, 10: `feygard_fogmonster1_heart_10`, 10: `feygard_fogmonster2_heart_10`, 10: `feygard_fogmonster3_heart_10`, 20: `feygard_fogmonster9_20`, 30: `swamp_witch_20`, 70: `swamp_witch_checkkill_10`, 80: `swamp_witch_20_134`, 90: `swamp_witch_20_160`, 92: `swamp_witch_20_190` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
