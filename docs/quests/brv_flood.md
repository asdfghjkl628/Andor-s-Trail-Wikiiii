# Much water

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_flood` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 200) |
| **Started by** | walking into a blocked passage on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Alvies](../monsters/brv_alvies.md), [Attohead](../monsters/brv_attohead.md), [Guard](../monsters/brv_exit_guard.md), [Mustura](../monsters/brv_guard_captain.md) |
| **Locations** | [brimhaven3](../maps/brimhaven3.md), [brimhaven4](../maps/brimhaven4.md), [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md), [brimhaven_house1](../maps/brimhaven_house1.md) |
| **Total XP** | 1,500 |
| **Related quests** | 5 |

</div>

## Overview

> I found two not very bright brothers in a cellar of their house. They seemed to be talking about some sinister plan.

## Prerequisites to start

None: talk to walking into a blocked passage on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-100) | stage 100 reached, for stages 100, 110 here |
| Unlocks | [Search for Andor](andor.md#stage-65) | stage 65 there needs stages 120, 130 here |
| Unlocks | [Search for Andor](andor.md#stage-910) | stage 910 there needs stage 200 here |
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-71) | stage 71 there needs stages 52, 70 here |
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-81) | stage 81 there needs stages 52, 70 here |
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-100) | stage 100 there needs stages 52, 70 here |
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-110) | stage 110 there needs stage 200 here |
| Unlocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-120) | stage 120 there needs stage 200 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-20) | stage 20 there needs stage 200 here |
| Unlocks | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-21) | stage 21 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-20) | stage 20 there needs stage 130 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-30) | stage 30 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-35) | stage 35 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-40) | stage 40 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-50) | stage 50 there needs stage 200 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-15) | stage 15 there needs stage 200 here |
| Blocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-71) | reaching stages 54, 70, 80 here closes stage 71 there |
| Blocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-81) | reaching stages 54, 70, 80 here closes stage 81 there |
| Blocks | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-100) | reaching stages 54, 70, 80 here closes stage 100 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I found two not very bright brothers in a cellar of their house. They seemed to be talking about some sinister plan.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven brother1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | walking into a blocked passage on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) | – | – |
| <span id="stage-20"></span>20 | They were planning to destroy the great dam of Brimhaven. They just could not agree how they would do it. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | – | – |
| <span id="stage-30"></span>30 | They asked me to help them. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | – | removes monsters from brimhaven1 |
| <span id="stage-50"></span>50 | I have agreed to destroy the dam for them. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | stage 30 | gives 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-52"></span>52 | The brothers gave me a hand axe that could weaken the dam in a vulnerable place. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | stage 30 | gives 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-53"></span>53 | I took another hand axe. This time I shouldn't lose it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven brother1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | stepping on a trigger on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) | – | gives 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-54"></span>54 | I found the weak spot in the dam and started hacking at the wood.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 52, wearing [Hand Axe](../items/hand_axe.md) | 500 XP<br>sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71)<br>sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)<br>sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4 |
| <span id="stage-56"></span>56 | Water came pouring through the hole in the dam. A lot of water!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 52, wearing [Hand Axe](../items/hand_axe.md) | sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71)<br>sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)<br>sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4 |
| <span id="stage-70"></span>70 | I refused to destroy the dam for the brothers. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | stage 30 | faction “brv_brothers” set to -1 |
| <span id="stage-72"></span>72 | Given what I overheard, I was not allowed to leave. The two brothers attacked me. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | stage 30 | faction “brv_brothers” set to -1 |
| <span id="stage-75"></span>75 | <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven brother1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | stepping on a trigger on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) | carry 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md) | – |
| <span id="stage-80"></span>80 | Someone else destroyed the dam and water came pouring through a hole in the dam. A lot of water!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven1](../maps/brimhaven1.md).</span> | stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) | stage 70 | sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71)<br>sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81)<br>sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100)<br>spawns monsters on brimhaven3<br>spawns monsters on brimhaven4 |
| <span id="stage-100"></span>100 | The Brimhaven guards have informed me that I may not leave the town until they have investigated who destroyed the dam. | [Guard](../monsters/brv_exit_guard.md) ([brimhaven3](../maps/brimhaven3.md))<br>[Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) | stage 110 | – |
| <span id="stage-110"></span>110 | I have promised to track down the real perpetrators. However, I still cannot leave the town. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) | – | – |
| <span id="stage-120"></span>120 | The two brothers did not know their boss's name, but he seemed to have a lot of gold. | [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) | stage 110, stage 56 | – |
| <span id="stage-130"></span>130 | The rich man living up on the hill of Brimhaven seemed to know more than he admitted. | [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | stage 110, stage 120 | – |
| <span id="stage-150"></span>150 | The rich man boasted that he had been bribed by an important man in Loneford to sabotage the dam. | [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | stage 120, stage 130 | gives 1× [Alkapoans's letters](../items/alkapoans_letters.md)<br>sets stage 65 of [Search for Andor](../quests/andor.md#stage-65) |
| <span id="stage-200"></span>200 | I gave the letters as a piece of evidence to the captain of the guard. Now it is up to them to deal with the rich man. **(completes quest)** | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) | hand over 1× [Alkapoans's letters](../items/alkapoans_letters.md), stage 110 | 1,000 XP<br>clears stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100)<br>removes monsters from brimhaven4<br>removes monsters from brimhaven3<br>removes monsters from brimhaven_house1<br>spawns monsters on brimhaven1<br>spawns monsters on brimhaven_house1 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. walking into a blocked passage on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) → the conversation leads here automatically → **stage 10**. NPC: “[You eavesdrop on the middle of the conversation. ] ... have to make sure no one finds out what we are going to do.”

???+ note "Stage 20: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → the conversation leads here automatically → **stage 20**. NPC: “[It seems they still have not seen you, because they have their backs turned to you.] Your way of destroying the dam…”

???+ note "Stage 30: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Much water](../quests/brv_flood.md#stage-30) → **stage 30**; also removes monsters from brimhaven1. NPC: “Would you assist us in destroying the dam?”

???+ note "Stage 50: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → choose “OK, I would like to help you destroy the dam.” — **conditions:** reached stage 30 of [Much water](../quests/brv_flood.md#stage-30) → **stage 50**; also gives 1× [Hand Axe](../items/hand_axe.md). NPC: “To not attract attention the best way to destroy the dam would be to take this small axe. Use it at the weak point of…”

???+ note "Stage 52: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → choose “OK, I would like to help you destroy the dam.” — **conditions:** reached stage 30 of [Much water](../quests/brv_flood.md#stage-30) → **stage 52**; also gives 1× [Hand Axe](../items/hand_axe.md). NPC: “To not attract attention the best way to destroy the dam would be to take this small axe. Use it at the weak point of…”

???+ note "Stage 53: 1 route"

    1. stepping on a trigger on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) → the conversation leads here automatically → **stage 53**; also gives 1× [Hand Axe](../items/hand_axe.md). NPC: “So lucky! Another small hand axe lies here.”

???+ note "Stage 54: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Start hacking on the wood.” — **conditions:** NOT reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); NOT reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md) → **stage 54**; also sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through the hole in the dam. A lot of water!”

???+ note "Stage 56: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → choose “Start hacking on the wood.” — **conditions:** NOT reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); reached stage 52 of [Much water](../quests/brv_flood.md#stage-52); NOT reached stage 54 of [Much water](../quests/brv_flood.md#stage-54); wearing [Hand Axe](../items/hand_axe.md) → **stage 56**; also sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through the hole in the dam. A lot of water!”

???+ note "Stage 70: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → choose “No, I will never do that!” — **conditions:** reached stage 30 of [Much water](../quests/brv_flood.md#stage-30) → **stage 70**; also faction “brv_brothers” set to -1. NPC: “Then we have to shut you up and do it ourselves.”

???+ note "Stage 72: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → choose “No, I will never do that!” — **conditions:** reached stage 30 of [Much water](../quests/brv_flood.md#stage-30) → **stage 72**; also faction “brv_brothers” set to -1. NPC: “Then we have to shut you up and do it ourselves.”

???+ note "Stage 75: 1 route"

    1. stepping on a trigger on [brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md) → the conversation leads here automatically — **conditions:** carry 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md) → **stage 75**

???+ note "Stage 80: 1 route"

    1. stepping on a trigger on [brimhaven1](../maps/brimhaven1.md) → the conversation leads here automatically — **conditions:** reached stage 70 of [Much water](../quests/brv_flood.md#stage-70); NOT reached stage 80 of [Much water](../quests/brv_flood.md#stage-80) → **stage 80**; also sets stage 71 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100), spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4. NPC: “Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”

???+ note "Stage 100: 3 routes"

    1. Talk to [Guard](../monsters/brv_exit_guard.md) ([brimhaven3](../maps/brimhaven3.md)) → the conversation leads here automatically → **stage 100**. NPC: “Stop! All foreigners have to stay in town until we have investigated who destroyed the great dam.”
    2. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “[Lie] I have no idea, but I will try to help you.” — **conditions:** reached stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100) → **stage 100**. NPC: “Thank you. But be aware that you are not allowed to leave the town until we have found out how the dam was destroyed.”
    3. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “No, not yet, but I will try to help you.” — **conditions:** reached stage 110 of [Much water](../quests/brv_flood.md#stage-110) → **stage 100**. NPC: “Come back when you have a proof, and until then stop accusing people. In the meantime, you are not allowed to leave…”

???+ note "Stage 110: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “[Lie] I have no idea, but I will try to help you.” — **conditions:** reached stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100) → **stage 110**. NPC: “Thank you. But be aware that you are not allowed to leave the town until we have found out how the dam was destroyed.”
    2. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “No, not yet, but I will try to help you.” — **conditions:** reached stage 110 of [Much water](../quests/brv_flood.md#stage-110) → **stage 110**. NPC: “Come back when you have a proof, and until then stop accusing people. In the meantime, you are not allowed to leave…”

???+ note "Stage 120: 1 route"

    1. Talk to [Alvies](../monsters/brv_alvies.md) ([brimhaven_brother1_to_2](../maps/brimhaven_brother1_to_2.md)) → choose “Can you tell me who is your boss?” — **conditions:** reached stage 56 of [Much water](../quests/brv_flood.md#stage-56); reached stage 110 of [Much water](../quests/brv_flood.md#stage-110) → **stage 120**. NPC: “We don't know him by name. He looked very rich and I think he lives in the western town alone in a big house.”

???+ note "Stage 130: 1 route"

    1. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “Are you sure?” — **conditions:** reached stage 110 of [Much water](../quests/brv_flood.md#stage-110); NOT reached stage 150 of [Much water](../quests/brv_flood.md#stage-150); reached stage 120 of [Much water](../quests/brv_flood.md#stage-120) → **stage 130**. NPC: “I... I.... know nothing. Really, it is the truth!”

???+ note "Stage 150: 1 route"

    1. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “I don't believe a word you say. [Half-lie] The two brothers told me that you paid them for destroying the dam.” — **conditions:** reached stage 130 of [Much water](../quests/brv_flood.md#stage-130); reached stage 120 of [Much water](../quests/brv_flood.md#stage-120) → **stage 150**; also gives 1× [Alkapoans's letters](../items/alkapoans_letters.md), sets stage 65 of [Search for Andor](../quests/andor.md#stage-65). NPC: “[Breaks down] I was bribed by the people of Loneford to sabotage the dam. Here are some letters I exchanged with them,…”

???+ note "Stage 200: 1 route"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Alkapoan was behind it. Here are letters proving his guilt. He is waiting at his home for you to arrest him.” — **conditions:** reached stage 110 of [Much water](../quests/brv_flood.md#stage-110); hand over 1× [Alkapoans's letters](../items/alkapoans_letters.md) → **stage 200**; also clears stage 100 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-100), removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven3, removes monsters from brimhaven_house1, spawns monsters on brimhaven1, spawns monsters on brimhaven_house1, spawns monsters on brimhaven_house1. NPC: “We will check this and if it is true then you can leave the town.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.12](../versions/0.7.12.md) | stage 10 journal text changed; stage 30 journal text changed; stage 50 journal text changed; stage 52 journal text changed; stage 54 journal text changed; stage 70 journal text changed (+4 more) |
| [v0.7.13](../versions/0.7.13.md) | stages added: 53<br>Dialogue: 1 line added, 1 line changed<br>· text: “[Breaks down] I was bribed by the people of Loneford to sabotage the …” → “[Breaks down] I was bribed by the people of Loneford to sabotage the …” |
| [v0.8.14](../versions/0.8.14.md) | stage 100 journal text changed; stage 110 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_flood` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 50, 52, 53, 54, 56, 70, 72, 75, 80, 100, 110, 120, 130, 150, 200 |
    | Dialogue nodes setting stages | 10: `brv_brothers_0`, 20: `brv_brothers_6`, 30: `brv_brothers_10`, 50: `brv_brothers_12`, 52: `brv_brothers_12`, 53: `brv_brothers_another_axe_10`, 54: `brv_flood_0_10`, 56: `brv_flood_0_10`, 70: `brv_brothers_11`, 72: `brv_brothers_11`, 75: `brv_brothers_found_coin_bag`, 80: `brv_flood_20_10`, 100: `brv_exit_forbidden_10`, 100: `brv_guard_captain_40`, 100: `brv_guard_captain_23`, 110: `brv_guard_captain_40`, 110: `brv_guard_captain_23`, 120: `brv_brothers_15`, 130: `brv_richman_10`, 150: `brv_richman_20`, 200: `brv_guard_captain_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
