# The silver scale

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `mermaid_scale` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90, 210) |
| **Started by** | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) |
| **NPCs involved** | [Tjure](../monsters/tjure.md) |
| **Locations** | [blackwater_mountain54](../maps/blackwater_mountain54.md) |
| **Total XP** | 4,000 |
| **Related quests** | 2 |

</div>

## Overview

> In a clearing, you met Tjure, who desperately asked for your help. He had once found a mermaid asleep on the beach at the river. The colorful tail attracted him so much that he pulled out a dazzling scale and ran away.

## Prerequisites to start

Start with [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)). Required:

- reached stage 10 of [The silver scale](../quests/mermaid_scale.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Delivery - nondisplay (hidden flag)](brv_wh_delivery_nondisplay.md#stage-50) | stage 50 there needs stage 200 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-10) | stage 10 there needs stage 220 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-11) | stage 11 there needs stage 220 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In a clearing, you met Tjure, who desperately asked for your help. He had once found a mermaid asleep on the beach at the river. The colorful tail attracted him so much that he pulled out a dazzling scale and ran away. | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | – | – |
| <span id="stage-20"></span>20 | Crying and mourning, the mermaid called after him. Finally she cursed him. Since then, Tjure has never been happy. He just wanted to get rid of the scale. Nevertheless, he never ventured back to the vicinity of the river. | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | – | – |
| <span id="stage-30"></span>30 | A wise woman told Tjure that he could neither throw away nor destroy the scale. His only salvation would be to give it back or to have someone buy it from him. But who would ever want to incur the wrath of a mermaid? | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | – | – |
| <span id="stage-90"></span>90 | You decided not to help Tjure. **(completes quest)** | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | – | 500 XP |
| <span id="stage-100"></span>100 | As soon as you held the scale in your hands, a great sluggishness and dispair came over you. | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | pay 1 gold, stage 30 | applies condition mermaid_scale |
| <span id="stage-200"></span>200 | You put the scale on the mark on the ground.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower2](../maps/roadtocarntower2.md).</span> | stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) | stage 100 | applies condition mermaid_scale |
| <span id="stage-210"></span>210 | There rang out a beautiful song of gratitude. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower2](../maps/roadtocarntower2.md).</span><br><span class="qnote">🗺️ Part of [Roadtocarntower2](../maps/roadtocarntower2.md) visibly changes.</span> | stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) | stage 200 | 3,500 XP |
| <span id="stage-220"></span>220 | You found a heavy bag of gold.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Roadtocarntower2](../maps/roadtocarntower2.md).</span> | stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) | stage 210 | gives 1000× [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [The silver scale](../quests/mermaid_scale.md#stage-10) → **stage 10**. NPC: “I pulled out one of her shimmering, dazzling scales, and ran away.”

???+ note "Stage 20: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [The silver scale](../quests/mermaid_scale.md#stage-20) → **stage 20**. NPC: “Crying and sobbing, the mermaid called after me. Finally, she screamed at me that I would never find peace, and that I…”

???+ note "Stage 30: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [The silver scale](../quests/mermaid_scale.md#stage-30) → **stage 30**. NPC: “She told me that my only other option was to find some kind-hearted person to buy it from me, but then they take on…”

???+ note "Stage 90: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → the conversation leads here automatically — **conditions:** reached stage 90 of [The silver scale](../quests/mermaid_scale.md#stage-90) → **stage 90**. NPC: “*Sigh* You were my last hope. Leave me now.”

???+ note "Stage 100: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → choose “No problem, here, take the gold.” — **conditions:** reached stage 30 of [The silver scale](../quests/mermaid_scale.md#stage-30); pay 1 gold → **stage 100**; also applies condition mermaid_scale. NPC: “(As soon as you take the scale in your hands, a great sluggishness and a feeling of despair come over you.)”

???+ note "Stage 200: 1 route"

    1. stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) → choose “* Put the scale on the ground *” — **conditions:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-100) is 100 → **stage 200**; also applies condition mermaid_scale. NPC: “What a relief! You suddenly feel lighthearted again.”

???+ note "Stage 210: 1 route"

    1. stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) → the conversation leads here automatically — **conditions:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-200) is 200 → **stage 210**. NPC: “You never heard such a beautiful sound before.”

???+ note "Stage 220: 1 route"

    1. stepping on a trigger on [roadtocarntower2](../maps/roadtocarntower2.md) → the conversation leads here automatically — **conditions:** latest stage of [The silver scale](../quests/mermaid_scale.md#stage-210) is 210 → **stage 220**; also gives 1000× [Gold coins](../items/gold.md). NPC: “You found a heavy bag of gold. 1,000 shining pieces of gold!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “You found a heavy bag of gold. 1000 shining pieces of gold!” → “You found a heavy bag of gold. {1000} shining pieces of gold!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=mermaid_scale.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `mermaid_scale` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 90, 100, 200, 210, 220 |
    | Dialogue nodes setting stages | 10: `tjure_10`, 20: `tjure_20`, 30: `tjure_30_34`, 90: `tjure_90`, 100: `tjure_30_92`, 200: `watermark_script_100_10`, 210: `watermark_script_200_10`, 220: `watermark_script_210` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
