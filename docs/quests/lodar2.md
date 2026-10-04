# Searching for madness

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lodar2` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 60) |
| **Started by** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) |
| **NPCs involved** | [Hira'zinn](../monsters/hirazinn.md), [Lodar](../monsters/lodar.md) |
| **Locations** | [lodarcave4a](../maps/lodarcave4a.md), [lodarhouse1](../maps/lodarhouse1.md) |
| **Total XP** | 1,000 |
| **Related quests** | 7 |

</div>

## Overview

> The potion-maker Lodar seems to be obsessed with something called the Hira'zinn.

## Prerequisites to start

Start with [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)). Required:

- reached stage 110 of [A lost potion](../quests/lodar.md#stage-110)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A lost potion](lodar.md#stage-100) | stage 100 reached, for stage 30 here |
| Requires | [A lost potion](lodar.md#stage-110) | stage 110 reached, for stages 10, 15, 20 here |
| Unlocks | [Search for Andor](andor.md#stage-70) | stage 70 there needs stage 60 here |
| Unlocks | [Search for Andor](andor.md#stage-71) | stage 71 there needs stage 60 here |
| Unlocks | [Search for Andor](andor.md#stage-72) | stage 72 there needs stage 60 here |
| Unlocks | [Search for Andor](andor.md#stage-80) | stage 80 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-10) | stage 10 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-30) | stage 30 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-40) | stage 40 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-41) | stage 41 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-42) | stage 42 there needs stage 60 here |
| Unlocks | [Lodar's potions](lodar_pots.md#stage-43) | stage 43 there needs stage 60 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 there needs stage 60 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-2) | stage 2 there needs stage 60 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 there needs stage 60 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-10) | stage 10 there needs stage 60 here |
| Unlocks | [The way out is through](shortcut_lodar.md#stage-10) | stage 10 there needs stage 60 here |
| Unlocks | [The way out is through](shortcut_lodar.md#stage-22) | stage 22 there needs stage 50 here |
| Unlocks | [The way out is through](shortcut_lodar.md#stage-30) | stage 30 there needs stage 60 here |
| Unlocks | [A creeping fear](xulviir.md#stage-10) | stage 10 there needs stage 60 here |
| Blocks | [The way out is through](shortcut_lodar.md#stage-20) | reaching stage 50 here closes stage 20 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | The potion-maker Lodar seems to be obsessed with something called the Hira'zinn. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | – |
| <span id="stage-15"></span>15 | Apparently, it relates to something that has started to happen recently. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | – |
| <span id="stage-20"></span>20 | Lodar gave me a glowing stone, that he said would allow me to enter some sort of tomb. He did not say which tomb, where the tomb is located, or how to reach it - only that it's somewhere 'below'. Below what, I wonder? | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | gives [Gatekeeper stone](../items/lodarstone.md) |
| <span id="stage-30"></span>30 | In the cave leading to Lodar's Hideaway, I reached what looks like a tomb. Could this be the one Lodar was referring to? | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 20 | – |
| <span id="stage-35"></span>35 | The glowing stone that Lodar gave me, crumbled to dust as I got near the tomb. However, it seems that I am now able to enter.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Lodarcave4a](../maps/lodarcave4a.md).</span> | walking into a blocked passage on [lodarcave4a](../maps/lodarcave4a.md) | hand over 1× [Gatekeeper stone](../items/lodarstone.md) | – |
| <span id="stage-40"></span>40 | I have encountered a foul creature inside the tomb. I assume this is the Hira'zinn that Lodar was referring to. I should kill it and then tell Lodar. | [Hira'zinn](../monsters/hirazinn.md) ([lodarcave4a](../maps/lodarcave4a.md)) | – | – |
| <span id="stage-50"></span>50 | I have presented the heart of the Hira'zinn to Lodar.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar0](../maps/shortcut_lodar0.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Shortcut lodar4](../maps/shortcut_lodar4.md).</span> | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | hand over 1× [Heart of the Hira'zinn](../items/hirazinn.md), stage 20 | 1,000 XP |
| <span id="stage-51"></span>51 | As soon as I presented the heart of the Hira'zinn to Lodar, he seemed to snap out of his previous state of mind. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 50 | – |
| <span id="stage-60"></span>60 | Lodar thanked me for defeating the Hira'zinn. In return, he promised to help me in any way he can. He has a large selection of potent potions available for me to purchase at a discount. **(completes quest)** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “The Hira'zinn?” — **conditions:** reached stage 110 of [A lost potion](../quests/lodar.md#stage-110) → **stage 10**. NPC: “Yes yes, the Hira'zinn. As I said, I must find the correct mixture before it moves again.”

???+ note "Stage 15: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “You are still not making any sense to me. What is this Hira'zinn that you keep mentioning?” — **conditions:** reached stage 110 of [A lost potion](../quests/lodar.md#stage-110) → **stage 15**. NPC: “It never used to be like this, or did it? I can't remember.”

???+ note "Stage 20: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “I'm up for it! What do you need help with?” — **conditions:** reached stage 110 of [A lost potion](../quests/lodar.md#stage-110) → **stage 20**; also gives [Gatekeeper stone](../items/lodarstone.md). NPC: “[Lodar hands you an odd looking stone that seems to be glowing from within] Good. Take this stone, it will allow you…”

???+ note "Stage 30: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “Fine. I still don't understand, but I'll try to do as you ask.” — **conditions:** reached stage 20 of [Searching for madness](../quests/lodar2.md#stage-20); reached stage 100 of [A lost potion](../quests/lodar.md#stage-100) → **stage 30**

???+ note "Stage 35: 1 route"

    1. walking into a blocked passage on [lodarcave4a](../maps/lodarcave4a.md) → the conversation leads here automatically — **conditions:** hand over 1× [Gatekeeper stone](../items/lodarstone.md) → **stage 35**. NPC: “From the stone that Lodar gave you, you start hearing cracking noises.”

???+ note "Stage 40: 1 route"

    1. Talk to [Hira'zinn](../monsters/hirazinn.md) ([lodarcave4a](../maps/lodarcave4a.md)) → the conversation leads here automatically → **stage 40**. NPC: “[You also feel a strong urge to leave this place]”

???+ note "Stage 50: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “I have defeated the Hira'zinn in the tomb below. Here is its heart.” — **conditions:** reached stage 20 of [Searching for madness](../quests/lodar2.md#stage-20); hand over 1× [Heart of the Hira'zinn](../items/hirazinn.md) → **stage 50**. NPC: “Give me that. Oh, yes ... yes!”

???+ note "Stage 51: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “Yes, we spoke before, but you seemed to be obsessed with the Hira'zinn and did not make much sense.” — **conditions:** reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50) → **stage 51**. NPC: “Well, I feel much better now.”

???+ note "Stage 60: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60) → **stage 60**. NPC: “Again, thank you for your help.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Good. Take this stone, it will allow you to enter the tomb. Go below.…” → “[Lodar hands you an odd looking stone that seems to be glowing from w…”<br>· text: “Give me that. Oh, yes.. Yes!” → “Give me that. Oh, yes ... yes!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lodar2` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 35, 40, 50, 51, 60 |
    | Dialogue nodes setting stages | 10: `lodar_3`, 15: `lodar_8`, 20: `lodar_12`, 30: `lodar_13a`, 35: `sign_lodarcave4a3`, 40: `hirazinn_2`, 50: `lodar_find1`, 51: `lodar_find4`, 60: `lodar_d1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
