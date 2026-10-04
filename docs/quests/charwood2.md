# Trial by fire

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `charwood2` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 50) |
| **Started by** | [Kantya](../monsters/kantya.md) ([tradehouse0](../maps/tradehouse0.md)) |
| **NPCs involved** | [Kantya](../monsters/kantya.md), [Maevalia](../monsters/maevalia.md), [Thukuzun](../monsters/thukuzun.md) |
| **Locations** | [lostmine11](../maps/lostmine11.md), [tradehouse0](../maps/tradehouse0.md) |
| **Total XP** | 7,000 |
| **Related quests** | 3 |

</div>

## Overview

> I've heard a story that the whole reason for the Charwood hills being invaded by the monsters in the first place was that something had been awoken deep in the Charwood mine. The people in the Charwood cabin say that the miners uncovered some sort of marking on the ground in a cave, with strange noises coming from below it. When they finally broke through the ground around the markings, all the…

## Prerequisites to start

Start with [Kantya](../monsters/kantya.md) ([tradehouse0](../maps/tradehouse0.md)). Required:

- reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Destined for great things](charwood1.md#stage-50) | stage 50 reached, for stage 10 here |
| Unlocks | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-10) | stage 10 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-15) | stage 15 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-20) | stage 20 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-25) | stage 25 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-30) | stage 30 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-35) | stage 35 there needs stage 50 here |
| Blocks | [Just the beginning](waterwayacave.md#stage-12) | reaching stage 50 here closes stage 12 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I've heard a story that the whole reason for the Charwood hills being invaded by the monsters in the first place was that something had been awoken deep in the Charwood mine. The people in the Charwood cabin say that the miners uncovered some sort of marking on the ground in a cave, with strange noises coming from below it. When they finally broke through the ground around the markings, all the troubles started. I should talk to Maevalia again. | [Kantya](../monsters/kantya.md) ([tradehouse0](../maps/tradehouse0.md)) | – | – |
| <span id="stage-15"></span>15 | I've promised Maevalia to investigate the deeper parts of the Charwood mine. I should be on the lookout for the dangerous monsters that inhabit the mine.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Lostmine0](../maps/lostmine0.md).</span> | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | – | – |
| <span id="stage-20"></span>20 | I've reached the part of the mine that was broken into. The air around here seems to get hotter as I get deeper into the mine. | reading a sign on [lostmine4](../maps/lostmine4.md) | – | – |
| <span id="stage-30"></span>30 | Among the fires in the lower parts of the mine, I've encountered some type of dragon-like creature. I guess this is the source of all the chaos in the mine. I should attempt to kill it and then venture back to Maevalia to tell her about it once I'm victorious. | [Thukuzun](../monsters/thukuzun.md) ([lostmine11](../maps/lostmine11.md)) | – | – |
| <span id="stage-40"></span>40 | I have presented one of the bones from the corpse of the Thukuzun to Maevalia. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | – | – |
| <span id="stage-50"></span>50 | Maevalia was happy to hear that I killed the source of the monster invasion. **(completes quest)** | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | stage 40 | 7,000 XP<br>gives [Gold coins](../items/gold.md)<br>gives [Worn iron boots](../items/hboot_wirn.md), [Ring of surehit](../items/ring_atkch1.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Kantya](../monsters/kantya.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “Is there anything I can do?” — **conditions:** reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50) → **stage 10**. NPC: “You've helped us this far. Talk to Maevalia again, she might have something else for you.”

???+ note "Stage 15: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “I'll go down into the Charwood mine and investigate.” — **conditions:** reached stage 15 of [Trial by fire](../quests/charwood2.md#stage-15) → **stage 15**. NPC: “Thank you.”

???+ note "Stage 20: 1 route"

    1. reading a sign on [lostmine4](../maps/lostmine4.md) → the conversation leads here automatically → **stage 20**. NPC: “The air around here is much hotter around the hole in the ground here than in the rest of this room. This must be…”

???+ note "Stage 30: 1 route"

    1. Talk to [Thukuzun](../monsters/thukuzun.md) ([lostmine11](../maps/lostmine11.md)) → the conversation leads here automatically → **stage 30**. NPC: “Ah, another mortal that has come to bow before the might of Thukuzun.”

???+ note "Stage 40: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Trial by fire](../quests/charwood2.md#stage-40) → **stage 40**. NPC: “You actually killed it?”

???+ note "Stage 50: 3 routes"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “I'm just happy to help.” — **conditions:** reached stage 40 of [Trial by fire](../quests/charwood2.md#stage-40) → **stage 50**. NPC: “You are truly our hero. Thank you yet again.”
    2. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “How about some gold for all my troubles?” — **conditions:** reached stage 40 of [Trial by fire](../quests/charwood2.md#stage-40) → **stage 50**; also gives [Gold coins](../items/gold.md). NPC: “Certainly. Here is what we can spare. Thank you yet again.”
    3. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “I think that one of your most precious items will suffice as payment.” — **conditions:** reached stage 40 of [Trial by fire](../quests/charwood2.md#stage-40) → **stage 50**; also gives [Worn iron boots](../items/hboot_wirn.md), [Ring of surehit](../items/ring_atkch1.md). NPC: “I guess we have no choice but to agree. Here, take these. They used to belong to my mother.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `charwood2` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `kantya23`, 15: `maevalia_d10`, 20: `sign_lostmine4`, 30: `thukuzun`, 40: `maevalia_h5`, 50: `maevalia_h9`, 50: `maevalia_h10`, 50: `maevalia_h12` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
