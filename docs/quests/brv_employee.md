# Work for debts

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_employee` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 90) |
| **Started by** | [Stebbarik](../monsters/brv_employee.md) ([brimhaven_employee](../maps/brimhaven_employee.md)) |
| **NPCs involved** | [Gnossath](../monsters/brv_employer.md), [Stebbarik](../monsters/brv_employee.md) |
| **Locations** | [brimhaven1](../maps/brimhaven1.md), [brimhaven_employee](../maps/brimhaven_employee.md) |
| **Total XP** | 1,000 |
| **Related quests** | 1 |

</div>

## Overview

> The dam is very important to Brimhaven. It should be repaired.

## Prerequisites to start

None: talk to [Stebbarik](../monsters/brv_employee.md) ([brimhaven_employee](../maps/brimhaven_employee.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-11) | stage 11 there needs stage 1 here |
| Blocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-89) | reaching stage 90 here closes stage 89 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | The dam is very important to Brimhaven. It should be repaired. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-10"></span>10 | Stebbarik was ill at home in bed. He could not work and feared that he would lose his job. Because of his high debts, he feared that Gnossath would then take his house away. I have offered to do the work for Stebbarik. | [Stebbarik](../monsters/brv_employee.md) ([brimhaven_employee](../maps/brimhaven_employee.md)) | – | – |
| <span id="stage-30"></span>30 | Gnossath has asked me to carry 25 heavy boulders from the stock to the dam. | [Gnossath](../monsters/brv_employer.md) ([brimhaven1](../maps/brimhaven1.md)) | stage 10 | changes map brimhaven1 |
| <span id="stage-40"></span>40 | I have carried the first boulder to the dam.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | – |
| <span id="stage-41"></span>41 | I have carried 5 boulders to the dam.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | – |
| <span id="stage-42"></span>42 | I have moved 10 boulders.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | – |
| <span id="stage-43"></span>43 | I have moved 15 boulders. This work is exhausting!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | – |
| <span id="stage-44"></span>44 | Only a few to go...<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | – |
| <span id="stage-90"></span>90 | Finally - that was the last boulder! Gnossath was very pleased with my work. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | hand over 4× [Boulder](../items/brv_boulder.md) | 1,000 XP<br>removes monsters from brimhaven_tavern1<br>removes monsters from brimhaven_employee<br>changes map brimhaven1<br>spawns monsters on brimhaven_employee<br>spawns monsters on brimhaven_tavern1<br>clears stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83)<br>sets stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Stebbarik](../monsters/brv_employee.md) ([brimhaven_employee](../maps/brimhaven_employee.md)) → choose “Maybe I could help you? I could do your work.” → **stage 10**. NPC: “You would do that? Oh, thank you! Thank you!”

???+ note "Stage 30: 1 route"

    1. Talk to [Gnossath](../monsters/brv_employer.md) ([brimhaven1](../maps/brimhaven1.md)) → choose “Sounds easy. Let me try it.” — **conditions:** reached stage 10 of [Work for debts](../quests/brv_employee.md#stage-10) → **stage 30**; also changes map brimhaven1. NPC: “OK. Try, if you want. The pile of boulders is just next to the wooden logs over there.”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md) → **stage 40**

???+ note "Stage 41: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 6; NOT reached stage 41 of [Work for debts](../quests/brv_employee.md#stage-41) → **stage 41**. NPC: “You have brought already more than 5 boulders.”

???+ note "Stage 42: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 11; NOT reached stage 42 of [Work for debts](../quests/brv_employee.md#stage-42) → **stage 42**. NPC: “Over 10 boulders.”

???+ note "Stage 43: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 16; NOT reached stage 43 of [Work for debts](../quests/brv_employee.md#stage-43) → **stage 43**. NPC: “At least 15 boulders now.”

???+ note "Stage 44: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 21; NOT reached stage 44 of [Work for debts](../quests/brv_employee.md#stage-44) → **stage 44**. NPC: “Only a few boulders left.”

???+ note "Stage 90: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Uff. They somehow seem to get heavier and heavier.” — **conditions:** hand over 4× [Boulder](../items/brv_boulder.md); faction “brv_boulder_count” ≥ 25; NOT reached stage 90 of [Work for debts](../quests/brv_employee.md#stage-90) → **stage 90**; also removes monsters from brimhaven_tavern1, removes monsters from brimhaven_employee, changes map brimhaven1, spawns monsters on brimhaven_employee, spawns monsters on brimhaven_tavern1, clears stage 83 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-83), sets stage 89 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-89). NPC: “Wow, you got it.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.12](../versions/0.7.12.md) | stage 10 journal text changed; stage 30 journal text changed; stage 40 journal text changed; stage 41 journal text changed; stage 42 journal text changed; stage 43 journal text changed (+1 more) |
| [v0.7.13](../versions/0.7.13.md) | stage 90 XP 0 → 1000 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_employee.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_employee` |
    | showInLog | 1 |
    | Stage IDs | 1, 10, 30, 40, 41, 42, 43, 44, 90 |
    | Dialogue nodes setting stages | 10: `brv_employee_06`, 30: `brv_employer_10_30`, 40: `brv_employer_put_boulder_10`, 41: `brv_employer_put_boulder_21`, 42: `brv_employer_put_boulder_22`, 43: `brv_employer_put_boulder_23`, 44: `brv_employer_put_boulder_24`, 90: `brv_employer_put_boulder_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
