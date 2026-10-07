---
description: "feygard fog is a hidden quest in Andor's Trail, started by stepping on a trigger on guynmart_wood_14. 10 stages. 1=Fog 1 has lifted"
---

# feygard fog

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_fog` |
| **In journal** | No (hidden flag) |
| **Stages** | 10 |
| **Started by** | stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md), [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) |
| **NPCs involved** | [Madame Mim](../monsters/swamp_witch.md) |
| **Locations** | [swamp_hut](../maps/swamp_hut.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1=Fog 1 has lifted

## Prerequisites to start

**Route 1** (stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md)):

- NOT reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)

**Route 2** ([Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Fog in the woods](fogmonster.md#stage-20) | stage 20 there needs stage 1 here |
| Blocks | [Fog in the woods](fogmonster.md#stage-10) | reaching stages 1, 2, 3, 4, 5 here closes stage 10 there |
| Blocks | [Fog in the woods](fogmonster.md#stage-70) | reaching stage 9 here closes stage 70 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=Fog 1 has lifted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 14](../maps/guynmart_wood_14.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart wood 13](../maps/guynmart_wood_13.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 13](../maps/guynmart_wood_13.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 14](../maps/guynmart_wood_14.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp3](../maps/swamp3.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | starts timer “feygard_fogmonster1”<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>changes map guynmart_wood_13<br>sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6 |
| <span id="stage-2"></span>2 | 2=Fog 2 has lifted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp2](../maps/swamp2.md).</span><br><span class="qnote">🗺️ Part of [Swamp2](../maps/swamp2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp3](../maps/swamp3.md) visibly changes.</span> | stepping on a trigger on [swamp2](../maps/swamp2.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | starts timer “feygard_fogmonster2”<br>sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13 |
| <span id="stage-3"></span>3 | 3=Fog 3 has lifted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp4](../maps/swamp4.md).</span><br><span class="qnote">🗺️ Part of [Swamp2](../maps/swamp2.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp3](../maps/swamp3.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp4](../maps/swamp4.md) visibly changes.</span> | stepping on a trigger on [swamp4](../maps/swamp4.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | starts timer “feygard_fogmonster3”<br>sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13 |
| <span id="stage-4"></span>4 | 4=Fog 4 has lifted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp5](../maps/swamp5.md).</span><br><span class="qnote">🗺️ Part of [Swamp3](../maps/swamp3.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp4](../maps/swamp4.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp5](../maps/swamp5.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp6](../maps/swamp6.md) visibly changes.</span> | stepping on a trigger on [swamp5](../maps/swamp5.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | starts timer “feygard_fogmonster4”<br>sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13 |
| <span id="stage-5"></span>5 | 5=Fog 5 has lifted<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp6](../maps/swamp6.md).</span><br><span class="qnote">🗺️ Part of [Swamp3](../maps/swamp3.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Swamp6](../maps/swamp6.md) visibly changes.</span> | stepping on a trigger on [swamp6](../maps/swamp6.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | starts timer “feygard_fogmonster5”<br>sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13 |
| <span id="stage-6"></span>6 | 6=Fog 1 normal<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp2](../maps/swamp2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp4](../maps/swamp4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp5](../maps/swamp5.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp6](../maps/swamp6.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 13](../maps/guynmart_wood_13.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 14](../maps/guynmart_wood_14.md) visibly changes.</span> | stepping on a trigger on [swamp2](../maps/swamp2.md) | stage 1 | clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7) |
| <span id="stage-7"></span>7 | 7=Fog 1 short<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp2](../maps/swamp2.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp4](../maps/swamp4.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp5](../maps/swamp5.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp6](../maps/swamp6.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 13](../maps/guynmart_wood_13.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 14](../maps/guynmart_wood_14.md) visibly changes.</span> | stepping on a trigger on [swamp2](../maps/swamp2.md)<br>[Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | stage 1, stage 8 | clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>sets stage 80 of [Fog in the woods](../quests/fogmonster.md#stage-80)<br>spawns monsters on guynmart_wood_14 |
| <span id="stage-8"></span>8 | 8=Fogs shortened | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) | – | sets stage 80 of [Fog in the woods](../quests/fogmonster.md#stage-80)<br>clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1)<br>clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>spawns monsters on guynmart_wood_14 |
| <span id="stage-9"></span>9 | 9=Fogs ended<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp hut](../maps/swamp_hut.md).</span> | [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md))<br>stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) | – | clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)<br>clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)<br>sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90)<br>removes monsters from guynmart_wood_14<br>removes monsters from swamp2<br>removes monsters from swamp4<br>removes monsters from swamp5<br>removes monsters from swamp6<br>changes map swamp2<br>changes map swamp4<br>changes map swamp6<br>changes map guynmart_wood_13<br>sets stage 70 of [Fog in the woods](../quests/fogmonster.md#stage-70)<br>gives 1× [Quarterstaff](../items/swampwitch_staff.md) |
| <span id="stage-10"></span>10 | 10=Board<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Swamp hut](../maps/swamp_hut.md).</span> | stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 2 routes"

    1. stepping on a trigger on [guynmart_wood_14](../maps/guynmart_wood_14.md) → the conversation leads here automatically — **conditions:** NOT reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1) → **stage 1**; also starts timer “feygard_fogmonster1”, clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), changes map guynmart_wood_13, sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10). NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 1**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 2: 2 routes"

    1. stepping on a trigger on [swamp2](../maps/swamp2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 2 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-2) → **stage 2**; also starts timer “feygard_fogmonster2”, sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10). NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 2**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 3: 2 routes"

    1. stepping on a trigger on [swamp4](../maps/swamp4.md) → the conversation leads here automatically — **conditions:** NOT reached stage 3 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-3) → **stage 3**; also starts timer “feygard_fogmonster3”, sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10). NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 3**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 4: 2 routes"

    1. stepping on a trigger on [swamp5](../maps/swamp5.md) → the conversation leads here automatically — **conditions:** NOT reached stage 4 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-4) → **stage 4**; also starts timer “feygard_fogmonster4”, sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10). NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 4**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 5: 2 routes"

    1. stepping on a trigger on [swamp6](../maps/swamp6.md) → the conversation leads here automatically — **conditions:** NOT reached stage 5 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-5) → **stage 5**; also starts timer “feygard_fogmonster5”, sets stage 10 of [Fog in the woods](../quests/fogmonster.md#stage-10). NPC: “The fog vanishes completely as soon as you touch its heart.”
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 5**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”

???+ note "Stage 6: 1 route"

    1. stepping on a trigger on [swamp2](../maps/swamp2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9); reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1); 75 rounds passed since timer “feygard_fogmonster1” → **stage 6**; also clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7)

???+ note "Stage 7: 2 routes"

    1. stepping on a trigger on [swamp2](../maps/swamp2.md) → the conversation leads here automatically — **conditions:** NOT reached stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9); reached stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1); 75 rounds passed since timer “feygard_fogmonster1”; reached stage 8 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-8) → **stage 7**; also clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6)
    2. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “People have trouble that the way to Feygard goes through your fog. If you make your fog a little smaller in…” → **stage 7**; also sets stage 80 of [Fog in the woods](../quests/fogmonster.md#stage-80), clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), spawns monsters on guynmart_wood_14. NPC: “Agreed. Here child, take these sweets and now begone!”

???+ note "Stage 8: 1 route"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “People have trouble that the way to Feygard goes through your fog. If you make your fog a little smaller in…” → **stage 8**; also sets stage 80 of [Fog in the woods](../quests/fogmonster.md#stage-80), clears stage 1 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-1), clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), spawns monsters on guynmart_wood_14. NPC: “Agreed. Here child, take these sweets and now begone!”

???+ note "Stage 9: 2 routes"

    1. Talk to [Madame Mim](../monsters/swamp_witch.md) ([swamp_hut](../maps/swamp_hut.md)) → choose “Uh, garden, I meant.” → **stage 9**; also clears stage 6 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-6), clears stage 7 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-7), sets stage 90 of [Fog in the woods](../quests/fogmonster.md#stage-90), removes monsters from guynmart_wood_14, removes monsters from swamp2, removes monsters from swamp4, removes monsters from swamp5, removes monsters from swamp6, changes map swamp2, changes map swamp4, changes map swamp6, changes map guynmart_wood_13. NPC: “Great. You deserve a reward for that. You may choose one thing from these:”
    2. stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) → the conversation leads here automatically — **conditions:** NOT reached stage 9 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-9); killed 1× [Madame Mim](../monsters/swamp_witch.md) → **stage 9**; also sets stage 70 of [Fog in the woods](../quests/fogmonster.md#stage-70), gives 1× [Quarterstaff](../items/swampwitch_staff.md). NPC: “This area will never be bullied by the old witch again. You take the witch's staff - maybe it will find a good use as…”

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [swamp_hut](../maps/swamp_hut.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [feygard fog (hidden flag)](../quests/feygard_fog.md#stage-10) → **stage 10**. NPC: “Oh what's this? How unusual!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 18 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_fog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_fog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_fog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_fog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_fog.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_fog` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
    | Dialogue nodes setting stages | 1: `feygard_fogmonster1_heart_10`, 1: `swamp_witch_20_160`, 1: `swamp_witch_t1`, 2: `feygard_fogmonster2_heart_10`, 2: `swamp_witch_20_160`, 2: `swamp_witch_t1`, 3: `feygard_fogmonster3_heart_10`, 3: `swamp_witch_20_160`, 3: `swamp_witch_t1`, 4: `feygard_fogmonster4_heart_10`, 4: `swamp_witch_20_160`, 4: `swamp_witch_t1`, 5: `feygard_fogmonster5_heart_10`, 5: `swamp_witch_20_160`, 5: `swamp_witch_t1`, 6: `feygard_fogmonster1_check_10_6`, 7: `feygard_fogmonster1_check_10_7`, 7: `swamp_witch_20_134`, 7: `swamp_witch_t2`, 8: `swamp_witch_20_134`, 8: `swamp_witch_t2`, 9: `swamp_witch_20_160`, 9: `swamp_witch_checkkill_10`, 9: `swamp_witch_t1`, 10: `swampwitch_board_note_10` |
    | Dialogue nodes clearing stages | 1: `feygard_fogmonster1_check_10_6`, 1: `feygard_fogmonster1_check_10_7`, 1: `swamp_witch_20_134`, 1: `swamp_witch_t2`, 1: `swamphut_oven_10`, 7: `feygard_fogmonster1_check_10_6`, 7: `feygard_fogmonster1_heart_10`, 7: `swamp_witch_20_160`, 7: `swamphut_oven_10`, 6: `feygard_fogmonster1_check_10_7` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
