# A secret garden

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `secret_garden` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 20, 45, 60) |
| **Started by** | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) |
| **NPCs involved** | [Caeda](../monsters/caeda.md) |
| **Locations** | [lakecave2](../maps/lakecave2.md), [remgard0](../maps/remgard0.md) |
| **Total XP** | 4,000 |
| **Related quests** | 2 |

</div>

## Overview

> Caeda in Remgard told me I can find fresh damerilias in her family's glade, but the key was taken by monsters. If I can find the key in the cave north of Remgard, I can access that glade, but I have to return the key to Caeda.

## Prerequisites to start

Start with [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)). Required:

- reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20)
- NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The roots of love](roots_love.md#stage-20) | stage 20 reached, for stages 10, 20 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-211) | stage 211 reached, for stage 30 here |
| Mutually exclusive | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-212) | stage 212 must NOT be reached, for stage 30 here |
| Unlocks | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-203) | stage 203 there needs stage 10 here |
| Unlocks | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-205) | stage 205 there needs stage 60 here |
| Blocks | [The roots of love](roots_love.md#stage-20) | reaching stage 10 here closes stage 20 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Caeda in Remgard told me I can find fresh damerilias in her family's glade, but the key was taken by monsters. If I can find the key in the cave north of Remgard, I can access that glade, but I have to return the key to Caeda. | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | – | – |
| <span id="stage-20"></span>20 | Finding the key was not worth the trouble. The wilted damerilias Caeda gave me will be just fine. **(completes quest)** | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | – | – |
| <span id="stage-30"></span>30 | I killed some monsters and found the key to the glade.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lakecave2](../maps/lakecave2.md).</span> | stepping on a trigger on [lakecave2](../maps/lakecave2.md) | – | gives 1× [Key to the glade](../items/glade_key.md)<br>sets stage 212 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-212) |
| <span id="stage-40"></span>40 | I returned the key right away to Caeda. | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | – | 2,000 XP |
| <span id="stage-45"></span>45 | I kept the key for a while, but finally returned it to Caeda. **(completes quest)** | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | 2,000 XP |
| <span id="stage-50"></span>50 | Caeda asked for my help to clear out the monsters in the caves so that she can go back there and attend to the flowers. | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | stage 40 | spawns monsters on lakecave0 |
| <span id="stage-55"></span>55 | Many monsters are dead now. The rest will no longer dare to approach the statue.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lakecave0](../maps/lakecave0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Lakecave2](../maps/lakecave2.md).</span> | stepping on a trigger on [lakecave0](../maps/lakecave0.md) | stage 50 | removes monsters from lakecave0 |
| <span id="stage-60"></span>60 | I told Caeda, so that she can attend to the glade. **(completes quest)** | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | stage 50, stage 55 | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → choose “Had?” — **conditions:** reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20); NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10) → **stage 10**. NPC: “Suddenly there were trolls everywhere. I barely escaped, but I must have lost the key to our glade there. If only I…”

???+ note "Stage 20: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → choose “Eh, OK. This isn't worth the trouble. Fresh damerilias wouldn't look different after my travel back. Thank…” — **conditions:** reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20); NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10) → **stage 20**. NPC: “Farewell then. Give my greetings to my sister-in-law.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [lakecave2](../maps/lakecave2.md) → the conversation leads here automatically — **conditions:** reached stage 211 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-211); NOT reached stage 212 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-212) → **stage 30**; also gives 1× [Key to the glade](../items/glade_key.md), sets stage 212 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-212). NPC: “Hey, this looks like Caeda's lost key.”

???+ note "Stage 40: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [A secret garden](../quests/secret_garden.md#stage-40); NOT reached stage 50 of [A secret garden](../quests/secret_garden.md#stage-50) → **stage 40**. NPC: “You really found my key! Thank you - I can't believe it!”

???+ note "Stage 50: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [A secret garden](../quests/secret_garden.md#stage-40) → **stage 50**; also spawns monsters on lakecave0. NPC: “Would it be too much to ask if you could get rid of the trolls?”

???+ note "Stage 55: 1 route"

    1. stepping on a trigger on [lakecave0](../maps/lakecave0.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [A secret garden](../quests/secret_garden.md#stage-50); NOT reached stage 55 of [A secret garden](../quests/secret_garden.md#stage-55); NOT reached stage 60 of [A secret garden](../quests/secret_garden.md#stage-60); killed 7× [Strong cave troll](../monsters/cave_troll_2.md); killed 15× [Tough cave troll](../monsters/cave_troll_3.md); killed 7× [Cave troll shaman](../monsters/cave_troll_4.md) → **stage 55**; also removes monsters from lakecave0, removes monsters from lakecave0, removes monsters from lakecave0. NPC: “Many of the trolls are dead now. The rest will no longer dare to approach the statue.”

???+ note "Stage 60: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → choose “Yes, I have dealt with most of the trolls. They won't dare to bother you for a long time.” — **conditions:** reached stage 50 of [A secret garden](../quests/secret_garden.md#stage-50); reached stage 55 of [A secret garden](../quests/secret_garden.md#stage-55) → **stage 60**. NPC: “Thank you so much! I wish you safe travels back to Stoutford. If you want to go to the glade next time you are in…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Hey, this looks like Caedas lost key.” → “Hey, this looks like Caeda's lost key.” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=secret_garden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=secret_garden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=secret_garden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=secret_garden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=secret_garden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `secret_garden` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 45, 50, 55, 60 |
    | Dialogue nodes setting stages | 10: `caeda_root10_8`, 20: `caeda_root10_8a`, 30: `lakecave2_script_keycheck3a`, 40: `caeda_root30_1`, 50: `caeda_root40_2`, 55: `script_lakecave_cleared_1`, 60: `caeda_root50_4` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
