# Undertell: What was not written

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `undertell_book` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 90) |
| **Started by** | stepping on a trigger on [undertell_exit](../maps/undertell_exit.md) |
| **NPCs involved** | [Arcir](../monsters/arcir.md), [Brenor](../monsters/brenor.md), [Elytharan cooker slave](../monsters/elytharan_cook_slave.md), [Ysrine](../monsters/ysrine.md) |
| **Locations** | [undertell_1_0](../maps/undertell_1_0.md), [undertell_1_1](../maps/undertell_1_1.md) |
| **Total XP** | 6,666 |
| **Related quests** | 2 |

</div>

## Overview

> I found the skeletal remains of an adventurer near the mining rails in Undertell. Among the remains were a history book titled "Undertell: Its Ghosts and History" and a necklace marked "Jewel of Fallhaven", which made me wonder if this man was from Fallhaven.

## Prerequisites to start

Start with stepping on a trigger on [undertell_exit](../maps/undertell_exit.md). Required:

- NOT reached stage 10 of [Undertell: What was not written](../quests/undertell_book.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The fifth master](fifth_master.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-75) | stage 75 reached, for stage 70 here |
| Blocked by | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-7) | stage 7 must NOT be reached, for stage 30 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-70) | stage 70 there needs stage 40 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I found the skeletal remains of an adventurer near the mining rails in Undertell. Among the remains were a history book titled "Undertell: Its Ghosts and History" and a necklace marked "Jewel of Fallhaven", which made me wonder if this man was from Fallhaven.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Undertell exit](../maps/undertell_exit.md).</span> | stepping on a trigger on [undertell_exit](../maps/undertell_exit.md) | – | gives 1× [Undertell: Its Ghosts and History](../items/undertell_book.md)<br>gives 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md) |
| <span id="stage-30"></span>30 | Ysrine suggested that the history of Undertell records what could be measured, but avoids the voices of those who suffered here. | [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) | carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md), stage 40 | – |
| <span id="stage-40"></span>40 | I brought the book to Fallhaven. Arcir recognized it as a deliberate account of Undertell's past and asked me to return and listen for what the book omits. | [Arcir](../monsters/arcir.md) | carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md) | spawns monsters on undertell_1_1 |
| <span id="stage-50"></span>50 | In Undertell, I spoke with Brenor, an Elytharan ghost who still remembers himself and the weight of the mines. | [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | I encountered an Elytharan cooker slave who spoke only of labor and routine, remembering work but not belief. | [Elytharan cooker slave](../monsters/elytharan_cook_slave.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 40 | – |
| <span id="stage-70"></span>70 | I earned the trust of a shy Elytharan ghost named Cora, who would only remain when I approached in silence. | walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md) | – | spawns monsters on undertell_01 |
| <span id="stage-80"></span>80 | The Elytharan ghosts each revealed a different truth: identity, labor and silence. I think Arcir would like to hear about this. | [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md))<br>walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md)<br>[Elytharan cooker slave](../monsters/elytharan_cook_slave.md) ([undertell_1_1](../maps/undertell_1_1.md)) | stage 50, stage 60, stage 70 | – |
| <span id="stage-90"></span>90 | I returned to Arcir with what I learned about the Elytharan dead and the omissions in the history of Undertell. **(completes quest)** | [Arcir](../monsters/arcir.md) | stage 80 | 6,666 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [undertell_exit](../maps/undertell_exit.md) → choose “Search the remains.” — **conditions:** NOT reached stage 10 of [Undertell: What was not written](../quests/undertell_book.md#stage-10) → **stage 10**; also gives 1× [Undertell: Its Ghosts and History](../items/undertell_book.md), gives 1× [Jewel of Fallhaven](../items/jewel_fallhaven.md). NPC: “A book is lodged near the ribcage, its oilcloth wrapping stiff and darkened with blood. Despite the damage, the title…”

???+ note "Stage 30: 1 route"

    1. Talk to [Ysrine](../monsters/ysrine.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “What do you mean?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7); carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md); NOT reached stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90); reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40) → **stage 30**. NPC: “The dead are accustomed to being spoken for. Few think to listen instead. Undertell remembers those who do.”

???+ note "Stage 40: 1 route"

    1. Talk to [Arcir](../monsters/arcir.md) → choose “What is it leaving out?” — **conditions:** NOT reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md) → **stage 40**; also spawns monsters on undertell_1_1. NPC: “The Elytharan followers sent into those mines did not vanish. They were made unrecordable. If even one of them still…”

???+ note "Stage 50: 1 route"

    1. Talk to [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md)) → choose “Who are you?” — **conditions:** NOT carry 1× [Heartstone](../items/heartstone.md); reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40) → **stage 50**. NPC: “My name was Brenor. I came from the lands ruled by Feygard, back when its people still followed Elythara. I was taken…”

???+ note "Stage 60: 1 route"

    1. Talk to [Elytharan cooker slave](../monsters/elytharan_cook_slave.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “Who do you cook for?” — **conditions:** reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60) → **stage 60**. NPC: “Those who work, eat. Those who eat return to work. The bell decides.”

???+ note "Stage 70: 1 route"

    1. walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); reached stage 75 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-75) → **stage 70**; also spawns monsters on undertell_01. NPC: “You say nothing.”

???+ note "Stage 80: 3 routes"

    1. Talk to [Brenor](../monsters/brenor.md) ([undertell_1_0](../maps/undertell_1_0.md)) → choose “I must continue my search.” — **conditions:** NOT carry 1× [Heartstone](../items/heartstone.md); reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80) → **stage 80**. NPC: “Sure, you do that.”
    2. walking into a blocked passage on [undertell_1_1](../maps/undertell_1_1.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80) → **stage 80**. NPC: “The silence is so rewarding.”
    3. Talk to [Elytharan cooker slave](../monsters/elytharan_cook_slave.md) ([undertell_1_1](../maps/undertell_1_1.md)) → choose “I see, but...” — **conditions:** reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80) → **stage 80**. NPC: “When the bell rings, the bowls are filled.”

???+ note "Stage 90: 1 route"

    1. Talk to [Arcir](../monsters/arcir.md) → choose “The Elytharan ghosts remember different things.” — **conditions:** reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80); NOT reached stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90) → **stage 90**. NPC: “Of course they do. History records stone and steel, but memory lives in people even after death. You have given voice…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_book.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `undertell_book` |
    | showInLog | 1 |
    | Stage IDs | 10, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `undertell_book_search_20`, 30: `ysrine_undertell_quiet_road`, 40: `arcir_undertell_20`, 50: `brenor_who_20`, 60: `elytharan_cooker_loop_60`, 70: `cora_pit_return_20`, 80: `brenor_reward_qs80`, 80: `cora_reward_qs80`, 80: `elytharan_cooker_reward_qs80`, 90: `arcir_undertell_complete_npc` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
