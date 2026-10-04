# Of mice and men

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `algangror` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 21, 100, 101) |
| **Started by** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) |
| **NPCs involved** | [Algangror](../monsters/algangror.md) |
| **Locations** | [lonelyhouse0](../maps/lonelyhouse0.md) |
| **Total XP** | 5,000 |
| **Related quests** | 2 |

</div>

## Overview

> In a lonely house on a peninsula at the northern shore of lake Laeroth up in the mountains to the north-east, I met a woman called Algangror.

## Prerequisites to start

None: talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [What is that stench?](remgard2.md#stage-10) | stage 10 reached, for stage 101 here |
| Requires | [What is that stench?](remgard2.md#stage-21) | stage 21 reached, for stage 101 here |
| Unlocks | [The five idols](fiveidols.md#stage-10) | stage 10 there needs stage 21 here |
| Unlocks | [The five idols](fiveidols.md#stage-20) | stage 20 there needs stage 21 here |
| Unlocks | [The five idols](fiveidols.md#stage-100) | stage 100 there needs stages 15, 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In a lonely house on a peninsula at the northern shore of lake Laeroth up in the mountains to the north-east, I met a woman called Algangror. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-11"></span>11 | She has a rodent problem and needs help dealing with some of them that she has trapped in her basement. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-15"></span>15 | I have agreed to help Algangror deal with her rodent problem. I should return to her when I have killed all six rodents in her basement. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | – | – |
| <span id="stage-20"></span>20 | Algangror thanked me for helping her with her problem. | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | hand over 6× [Strange looking rat tail](../items/algangror_rat.md), stage 15 | 5,000 XP |
| <span id="stage-21"></span>21 | She also told me not to talk to anyone in Remgard about her whereabouts. Apparently, they are looking for her for some reason that she would not say. Under no circumstances should I tell anyone where she is. **(completes quest)** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 20 | – |
| <span id="stage-100"></span>100 | I will not help Algangror with her task. **(completes quest)** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 15 | – |
| <span id="stage-101"></span>101 | Algangror won't talk to me, and I will be unable to help her with her task. **(completes quest)** | [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) | stage 10, stage 15, stage 21 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → the conversation leads here automatically → **stage 10**. NPC: “Oh my, a child. He he, how nice. Tell me, what brings you here?”

???+ note "Stage 11: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Sure, what's the problem?” → **stage 11**. NPC: “That's where you come in. Would you be willing to ... ahem ... handle those rodents for me?”

???+ note "Stage 15: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Sure, some rodents, I can handle that.” → **stage 15**. NPC: “Splendid. Return to me with some proof that they have been dealt with.”

???+ note "Stage 20: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “Yes, they are all dead.” — **conditions:** reached stage 15 of [Of mice and men](../quests/algangror.md#stage-15); hand over 6× [Strange looking rat tail](../items/algangror_rat.md) → **stage 20**. NPC: “He he. I bet you sure showed them. Excellent. Thank you for ... ahem ... helping me.”

???+ note "Stage 21: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “OK.” — **conditions:** reached stage 20 of [Of mice and men](../quests/algangror.md#stage-20) → **stage 21**. NPC: “Under no circumstances.”

???+ note "Stage 100: 1 route"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “I won't do your stupid task, count me out.” — **conditions:** reached stage 15 of [Of mice and men](../quests/algangror.md#stage-15) → **stage 100**. NPC: “Ah yes. After all, you are just a child and I can understand such a task would be too much for you. He he.”

???+ note "Stage 101: 2 routes"

    1. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → choose “I am sent by Jhaeld to end whatever it is you do to the people of Remgard.” — **conditions:** reached stage 15 of [Of mice and men](../quests/algangror.md#stage-15); reached stage 21 of [What is that stench?](../quests/remgard2.md#stage-21); reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10) → **stage 101**
    2. Talk to [Algangror](../monsters/algangror.md) ([lonelyhouse0](../maps/lonelyhouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 21 of [Of mice and men](../quests/algangror.md#stage-21); reached stage 10 of [What is that stench?](../quests/remgard2.md#stage-10); reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10) → **stage 101**


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “He he. I bet you sure showed them. Excellent. Thank you for .. ahem .…” → “He he. I bet you sure showed them. Excellent. Thank you for ... ahem …”<br>· text: “That's where you come in. Would you be willing to .. ahem .. handle t…” → “That's where you come in. Would you be willing to ... ahem ... handle…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=algangror.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=algangror.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=algangror.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=algangror.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=algangror.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `algangror` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 15, 20, 21, 100, 101 |
    | Dialogue nodes setting stages | 10: `algangror_1`, 11: `algangror_8`, 15: `algangror_9`, 20: `algangror_return_2`, 21: `algangror_remgard_7`, 100: `algangror_decline_1`, 101: `algangror_fight_1a`, 101: `algangror_told_1a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
