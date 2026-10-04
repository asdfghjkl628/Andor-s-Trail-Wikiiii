# The roots of love

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `roots_love` |
| **In journal** | Yes |
| **Stages** | 5 (completes at 40, 45) |
| **Started by** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) |
| **NPCs involved** | [Aryfora](../monsters/stoutford_widow.md), [Caeda](../monsters/caeda.md) |
| **Locations** | [lakecave2](../maps/lakecave2.md), [remgard0](../maps/remgard0.md), [stoutford_gate](../maps/stoutford_gate.md) |
| **Total XP** | 3,500 |
| **Related quests** | 2 |

</div>

## Overview

> Aryfora, a woman grieving in Stoutford's graveyard asked me to bring her some damerilias from Remgard for the grave of Noraed, her husband.

## Prerequisites to start

None: talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Blocked by | [A secret garden](secret_garden.md#stage-10) | stage 10 must NOT be reached, for stage 20 here |
| Unlocks | [A secret garden](secret_garden.md#stage-10) | stage 10 there needs stage 20 here |
| Unlocks | [A secret garden](secret_garden.md#stage-20) | stage 20 there needs stage 20 here |
| Unlocks | [The thorns of vengeance](thorns_vengeance.md#stage-10) | stage 10 there needs stage 45 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Aryfora, a woman grieving in Stoutford's graveyard asked me to bring her some damerilias from Remgard for the grave of Noraed, her husband. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | – | – |
| <span id="stage-20"></span>20 | Noraed's sister, Caeda, gave me some damerilias. I should bring them back to Stoutford. | [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) | stage 10 | gives 3× [Damerilias](../items/damerilias.md) |
| <span id="stage-30"></span>30 | I have brought the damerilias back to Aryfora. She thanked me with a potion she made. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | hand over 3× [Damerilias](../items/damerilias.md), stage 10 | 3,500 XP<br>gives 1× [Potion of deftness](../items/potion_deftness.md) |
| <span id="stage-40"></span>40 | I told her the flowers were from Noraed's sister, Caeda. **(completes quest)** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 30 | – |
| <span id="stage-45"></span>45 | I told her I found the flowers around Remgard, in the wild. **(completes quest)** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 30 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “Don't worry about me. I can handle myself.” → **stage 10**. NPC: “Really? If you manage to do it, I'll make sure to reward you with something only I can do, and that I haven't done in…”

???+ note "Stage 20: 1 route"

    1. Talk to [Caeda](../monsters/caeda.md) ([lakecave2](../maps/lakecave2.md)) → choose “Yes, Aryfora told me. She asked me to bring her some damerilias for Noraed's grave.” — **conditions:** reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10); NOT reached stage 20 of [The roots of love](../quests/roots_love.md#stage-20); NOT reached stage 10 of [A secret garden](../quests/secret_garden.md#stage-10) → **stage 20**; also gives 3× [Damerilias](../items/damerilias.md). NPC: “I still have some. Here, take these to her, and send her my condolences.”

???+ note "Stage 30: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “Yes. Here they are, three of the most beautiful damerilias.” — **conditions:** reached stage 10 of [The roots of love](../quests/roots_love.md#stage-10); hand over 3× [Damerilias](../items/damerilias.md) → **stage 30**; also gives 1× [Potion of deftness](../items/potion_deftness.md). NPC: “Oh. They're beautiful! Thank you! Here, take this potion as your reward.”

???+ note "Stage 40: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “Caeda, Noraed's sister, gave them to me. She sends you her condolences.” — **conditions:** reached stage 30 of [The roots of love](../quests/roots_love.md#stage-30) → **stage 40**. NPC: “Noraed had a sister? He never talked about his family. He said he had a happy childhood, but that's it. I think he…”

???+ note "Stage 45: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “I found them in the wild around Remgard.” — **conditions:** reached stage 30 of [The roots of love](../quests/roots_love.md#stage-30) → **stage 45**. NPC: “Is that so? Remgard must be a beautiful place to have such nice flowers growing in the wild.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 5 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “I still have some. Here, take these to her, and send her my condolanc…” → “I still have some. Here, take these to her, and send her my condolenc…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=roots_love.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=roots_love.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=roots_love.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=roots_love.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=roots_love.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `roots_love` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 45 |
    | Dialogue nodes setting stages | 10: `stoutford_widow_10`, 20: `caeda_root10_4`, 30: `stoutford_widow_roots10_2`, 40: `stoutford_widow_roots30_3`, 45: `stoutford_widow_roots30_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
