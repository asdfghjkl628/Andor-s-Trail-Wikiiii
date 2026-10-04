# It's knot funny

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fallhaven_lytwings` |
| **In journal** | Yes |
| **Stages** | 19 (completes at 101, 102, 103) |
| **Started by** | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) |
| **NPCs involved** | [Arensia](../monsters/arensia.md), [Lytwing](../monsters/lytwing_fallhaven.md), [Rigmor](../monsters/rigmor.md) |
| **Locations** | [fallhaven_sw](../maps/fallhaven_sw.md), [gapfiller2](../maps/gapfiller2.md) |
| **Total XP** | 300 |

</div>

## Overview

> I met Arensia in Fallhaven. She is being taunted by lytwings while she slumbers. I agreed to help get rid of the mischevious creatures. I should talk to Rigmor to find out more, she lives north of the tavern.

## Prerequisites to start

Start with [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)). Required:

- NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1)
- NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12)
- latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | I met Arensia in Fallhaven. She is being taunted by lytwings while she slumbers. I agreed to help get rid of the mischevious creatures. I should talk to Rigmor to find out more, she lives north of the tavern. | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | – | – |
| <span id="stage-10"></span>10 | Rigmor told me that lytwings live near large rings of mushroom growth, I should look for these in the forest surrounding Fallhaven.<br><span class="qnote">⚡ A scripted event can now trigger on [Gapfiller2](../maps/gapfiller2.md).</span> | [Rigmor](../monsters/rigmor.md) | stage 1 | – |
| <span id="stage-11"></span>11 | I have to take a gift of two red apples and two strawberries before I can talk to the lytwings. They cast some kind of spell on me for not bringing them these fruit, it made me feel very tired. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | – | applies condition fatigue_minor |
| <span id="stage-12"></span>12 | The lytwings accepted my gift, and I can now talk with them. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | hand over 2× [Red apple](../items/apple_red.md), hand over 2× [Strawberry](../items/strawberry.md) | – |
| <span id="stage-13"></span>13 | I offered my help to the lytwings in exchange for leaving Arensia alone. They are considering my request. I should check in with them shortly, to hear their decision. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | stage 12 | starts timer “lytwing_fallhaven_timer” |
| <span id="stage-20"></span>20 | The lytwings asked that I chop down a gnarly old tree that is inside their mushroom ring. They insisted that I use an iron axe because the cursed bark of the tree cannot be cut by other tools. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | – | – |
| <span id="stage-21"></span>21 | I was about to swing my axe, when the lytwings stopped me. They have changed their minds about chopping down the tree. I am beginning to think they are indecisive on purpose. | reading a sign on [gapfiller2](../maps/gapfiller2.md) | carry 1× [Iron axe](../items/axe2.md), stage 20 | – |
| <span id="stage-30"></span>30 | The lytwings want four bottles of mead. I can probably find some at the Fallhaven tavern. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | stage 21 | – |
| <span id="stage-31"></span>31 | They took the mead, and turned around saying they want something else. I can now see why Rigmor said they are full of mischief! But I have no other choice but to continue this fool's errand if I want to help Arensia. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | hand over 4× [Mead](../items/mead.md), stage 30 | – |
| <span id="stage-40"></span>40 | I have to find twelve wild flowers for the lytwings. I wonder where I could find those. Perhaps Arensia will know.<br><span class="qnote">⚡ A scripted event can now trigger on [Wild10](../maps/wild10.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Wild11](../maps/wild11.md).</span> | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | stage 31 | – |
| <span id="stage-41"></span>41 | They accepted the flowers, and as expected, said they want something else! How many more times will they make me run around? | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | hand over 12× [Wild Flower](../items/wild_flower.md), stage 40 | – |
| <span id="stage-90"></span>90 | The lytwings want a token of Arensia's promise that she will not to pick their mushrooms again. I sense they are not playing another prank this time, they seemed intent about this task. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | stage 41 | – |
| <span id="stage-91"></span>91 | Arensia made a promise to her mother's ring, and then she gave it to me. I should take it to the lytwings at once. | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 90 | gives 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md) |
| <span id="stage-92"></span>92 | I gave Arensia's ring to the lytwings. Just when I thought it was done, they said they need something else! I am waiting on their decision. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | hand over 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md), stage 90 | – |
| <span id="stage-99"></span>99 | The lytwings have agreed to stop taunting Arensia. I should go tell her. | [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) | stage 92 | gives 1× [Arensia's Ring of Promise](../items/ring_of_promise.md) |
| <span id="stage-100"></span>100 | Arensia was elated to hear that the lytwings will no longer taunt her. | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | – | 300 XP |
| <span id="stage-101"></span>101 | I could not take the absurd errands any more. I am no longer helping Arensia with her lytwing problem. **(completes quest)** | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 40 | – |
| <span id="stage-102"></span>102 | I lied to Arensia's and kept her mother's ring for myself. **(completes quest)** | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 100 | – |
| <span id="stage-103"></span>103 | Arensia gave me her magical promise ring as reward for helping her. **(completes quest)** | [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 100 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Not yet. I still need to go talk with Rigmor to find out more.” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12); latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1 → **stage 1**. NPC: “You should talk to Rigmor, as she knows more about the lytwings than I do. She lives here in Fallhaven, just go north…”

???+ note "Stage 10: 1 route"

    1. Talk to [Rigmor](../monsters/rigmor.md) → choose “Where can I find lytwings?” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1 → **stage 10**. NPC: “Lytwings gather near fairy rings. I suggest that you look for large mushroom patches in the woodland surrounding…”

???+ note "Stage 11: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “I did not, sorry.” — **conditions:** NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12) → **stage 11**; also applies condition fatigue_minor. NPC: “Bring us two red apples and two strawberries. Since you came without a gift, we cast on you a mystical Lytwing spell!”

???+ note "Stage 12: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Yes, here are two red apples and two strawberries.” — **conditions:** NOT reached stage 12 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12); hand over 2× [Red apple](../items/apple_red.md); hand over 2× [Strawberry](../items/strawberry.md) → **stage 12**. NPC: “Wonderful! These strawberries are so sweet. You may stay!”

???+ note "Stage 13: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Don't be mad, I am just trying to help. Is there anything I can do to make this right?” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-12) is 12 → **stage 13**; also starts timer “lytwing_fallhaven_timer”. NPC: “Hmmm, let us discuss this amongst ourselves. Can you give us a minute alone?”

???+ note "Stage 20: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → the conversation leads here automatically — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20) is 20 → **stage 20**. NPC: “Please chop down this gnarly old tree inside our fairy circle. Can you do that for us?”

???+ note "Stage 21: 1 route"

    1. reading a sign on [gapfiller2](../maps/gapfiller2.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-20); carry 1× [Iron axe](../items/axe2.md); NOT reached stage 30 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30) → **stage 21**. NPC: “Hey wait! We changed our minds. We like that tree and want to keep it.”

???+ note "Stage 30: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → the conversation leads here automatically — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-21) is 21 → **stage 30**. NPC: “We are having a celebration, please get us four bottles of mead. [giggle]”

???+ note "Stage 31: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Yes, here is your mead.” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-30) is 30; hand over 4× [Mead](../items/mead.md) → **stage 31**. NPC: “Wonderful!”

???+ note "Stage 40: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → the conversation leads here automatically — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-31) is 31 → **stage 40**. NPC: “For our celebrations, we would like a dozen wild flowers.”

???+ note "Stage 41: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Yes, here are your flowers.” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40; hand over 12× [Wild Flower](../items/wild_flower.md) → **stage 41**. NPC: “These are perfect. Thank you!”

???+ note "Stage 90: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “OK?” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-41) is 41 → **stage 90**. NPC: “We want Arensia to promise not to pick our mushrooms again. And we want proof!”

???+ note "Stage 91: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “I hope this works.” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); NOT reached stage 99 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-99); latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90 → **stage 91**; also gives 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md). NPC: “I made a promise to the ring, here take it to the lytwings!”

???+ note "Stage 92: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Yes, here is her promise ring.” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-90) is 90; hand over 1× [Arensia's Ring of Promise](../items/ring_of_promise_quest.md) → **stage 92**. NPC: “This will do just fine, thank you $playername.”

???+ note "Stage 99: 1 route"

    1. Talk to [Lytwing](../monsters/lytwing_fallhaven.md) ([gapfiller2](../maps/gapfiller2.md)) → choose “Oh how wonderful. Thank you forest lytwings!” — **conditions:** latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-92) is 92 → **stage 99**; also gives 1× [Arensia's Ring of Promise](../items/ring_of_promise.md). NPC: “However, we have no need for a human ring. We embued it with our magical powers. Please take this ring back to Arensia.”

???+ note "Stage 100: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “You seem tired. Is everything alright?” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); NOT reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102) → **stage 100**. NPC: “I cannot thank you enough, $playername. You have saved my sanity!”

???+ note "Stage 101: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Yes, I want to quit.” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); NOT reached stage 99 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-99); latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-40) is 40 → **stage 101**. NPC: “I appreciate your help either way.”

???+ note "Stage 102: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Unfortunately they kept your mother's ring (Lie).” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); NOT reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102) → **stage 102**. NPC: “That is okay. I did not expect to get it back.”

???+ note "Stage 103: 1 route"

    1. Talk to [Arensia](../monsters/arensia.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “They used their magic on your ring, and asked that I give it back to you.” — **conditions:** NOT reached stage 1 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1); reached stage 100 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-100); NOT reached stage 102 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-102) → **stage 103**. NPC: “After everything you have done for me ... I want you to keep it. Please, I insist!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 19 lines added |
| [v0.8.13](../versions/0.8.13.md) | stage 21 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fallhaven_lytwings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fallhaven_lytwings` |
    | showInLog | 1 |
    | Stage IDs | 1, 10, 11, 12, 13, 20, 21, 30, 31, 40, 41, 90, 91, 92, 99, 100, 101, 102, 103 |
    | Dialogue nodes setting stages | 1: `arensia_lytwing_33`, 10: `rigmor_lytwing_5`, 11: `lytwing_fallhaven_4`, 12: `lytwing_fallhaven_5`, 13: `lytwing_fallhaven_9`, 20: `lytwing_fallhaven_14`, 21: `lytwing_fallhaven_16`, 30: `lytwing_fallhaven_17`, 31: `lytwing_fallhaven_19`, 40: `lytwing_fallhaven_22`, 41: `lytwing_fallhaven_24`, 90: `lytwing_fallhaven_28`, 91: `arensia_lytwing_21`, 92: `lytwing_fallhaven_32`, 99: `lytwing_fallhaven_37`, 100: `arensia_lytwing_24`, 101: `arensia_lytwing_17`, 102: `arensia_lytwing_25`, 103: `arensia_lytwing_26` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
