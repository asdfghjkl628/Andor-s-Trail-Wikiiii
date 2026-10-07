---
description: "I have it in me is a quest in Andor's Trail, started by Toszylae (waytobrimhavencave3a). 11 stages, 30,000 XP in total. Deep inside a cavern, I encountered a lich of Kazaul. Somehow the lich managed to infect me with things that crawl around in my stomach! I must find some way to get rid of these…"
---

# I have it in me

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `maggots` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 51) |
| **Started by** | [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) |
| **NPCs involved** | [Talion](../monsters/talion.md), [Toszylae](../monsters/toszylae.md), [Ulirfendor](../monsters/ulirfendor.md) |
| **Locations** | [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md), [waytobrimhavencave4](../maps/waytobrimhavencave4.md) |
| **Total XP** | 30,000 |
| **Related quests** | 4 |

</div>

## Overview

> Deep inside a cavern, I encountered a lich of Kazaul. Somehow the lich managed to infect me with things that crawl around in my stomach! I must find some way to get rid of these things inside of me. I should go talk to Ulirfendor, or seek help in one of the chapels.

## Prerequisites to start

None: talk to [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [An involuntary carrier](toszylae.md#stage-60) | stage 60 reached, for stages 20, 21 here |
| Requires | [An involuntary carrier](toszylae.md#stage-70) | stage 70 reached, for stage 21 here |
| Unlocks | [Flows through the veins](loneford.md#stage-23) | stage 23 there needs stage 51 here |
| Unlocks | [Flows through the veins](loneford.md#stage-25) | stage 25 there needs stage 51 here |
| Unlocks | [Shadows](shadows.md#stage-90) | stage 90 there needs stage 51 here |
| Unlocks | [Shadows](shadows.md#stage-100) | stage 100 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-70) | stage 70 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-80) | stage 80 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-170) | stage 170 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-280) | stage 280 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-290) | stage 290 there needs stage 51 here |
| Unlocks | [Troubling times](troubling_times.md#stage-300) | stage 300 there needs stage 51 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Deep inside a cavern, I encountered a lich of Kazaul. Somehow the lich managed to infect me with things that crawl around in my stomach! I must find some way to get rid of these things inside of me. I should go talk to Ulirfendor, or seek help in one of the chapels. | [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | – | applies condition rotworm<br>sets stage 50 of [An involuntary carrier](../quests/toszylae.md#stage-50) |
| <span id="stage-20"></span>20 | Ulirfendor tells me that he read something long ago about rotworms that feed upon living tissue. They can have what he called 'unusual' effects on whoever carries them, and their eggs can slowly kill a person from the inside. I should seek help immediately, before it is too late. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-21"></span>21 | Ulirfendor says that one of the priests of the Shadow should be able help me. I should go visit Talion at the chapel in Loneford at once. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-30"></span>30 | Talion in Loneford told me that in order to be cured of my affliction, I will need to bring four parts to him. The parts that I will need are five bones, two pieces of animal hair, one irdegh poison gland and one empty vial. Bones and fur can probably be found on some animal in the wilderness, and the poison gland can be found on one of the irdeghs that have been spotted to the east. | [Talion](../monsters/talion.md) | – | – |
| <span id="stage-40"></span>40 | I have brought the five bones to Talion. | [Talion](../monsters/talion.md) | hand over 5× [Bone](../items/bone.md), stage 30 | – |
| <span id="stage-41"></span>41 | I have brought the two pieces of animal hair to Talion. | [Talion](../monsters/talion.md) | hand over 2× [Animal hair](../items/hair.md), stage 30 | – |
| <span id="stage-42"></span>42 | I have brought one irdegh poison gland to Talion. | [Talion](../monsters/talion.md) | hand over 1× [Irdegh poison gland](../items/irdegh.md), stage 30 | – |
| <span id="stage-43"></span>43 | I have brought an empty vial to Talion. | [Talion](../monsters/talion.md) | hand over 1× [Small empty vial](../items/vial_empty1.md), stage 30 | – |
| <span id="stage-45"></span>45 | I have now brought all pieces that Talion needs in order to cure me of these things. | [Talion](../monsters/talion.md) | stage 30, stage 40, stage 41, stage 42, stage 43 | – |
| <span id="stage-50"></span>50 | Talion has cured me of the Kazaul rotworms. I managed to get one of the rotworms into an empty vial, and Talion told me that it would be very valuable. I cannot imagine for what. | [Talion](../monsters/talion.md) | stage 45 | 30,000 XP<br>gives [Kazaul rotworm](../items/potion_rotworm.md)<br>applies condition rotworm |
| <span id="stage-51"></span>51 | Because of my former affliction, Talion has agreed to help me by placing blessings of the Shadow upon me whenever I wish, for a fee. **(completes quest)** | [Talion](../monsters/talion.md) | stage 50 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → the conversation leads here automatically → **stage 10**; also applies condition rotworm, sets stage 50 of [An involuntary carrier](../quests/toszylae.md#stage-50). NPC: “[As if having swallowed a thousand needles, you are suddenly stricken with a cascading series of spikes of pain…”

???+ note "Stage 20: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “What is?” — **conditions:** reached stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60) → **stage 20**. NPC: “Needless to say, you are in great danger, and you should seek help immediately.”

???+ note "Stage 21: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “I found a strange looking helmet among the remains of the lich that I defeated. Do you know anything about it?” — **conditions:** reached stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60); reached stage 70 of [An involuntary carrier](../quests/toszylae.md#stage-70) → **stage 21**. NPC: “You should hurry and seek help from one of the priests of the Shadow as quickly as possible. My dear friend Talion in…”

???+ note "Stage 30: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Got it. Anything else?” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30) → **stage 30**. NPC: “Bring me these things and I will be able to help you with your ... condition.”

???+ note "Stage 40: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Here you go.” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30); hand over 5× [Bone](../items/bone.md) → **stage 40**. NPC: “Thank you.”

???+ note "Stage 41: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Here you go.” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30); hand over 2× [Animal hair](../items/hair.md) → **stage 41**. NPC: “Thank you.”

???+ note "Stage 42: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Here you go.” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30); hand over 1× [Irdegh poison gland](../items/irdegh.md) → **stage 42**. NPC: “Thank you.”

???+ note "Stage 43: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Here you go, one small empty vial.” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30); hand over 1× [Small empty vial](../items/vial_empty1.md) → **stage 43**. NPC: “Thank you.”

???+ note "Stage 45: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “I brought five bones for you.” — **conditions:** reached stage 30 of [I have it in me](../quests/maggots.md#stage-30); reached stage 40 of [I have it in me](../quests/maggots.md#stage-40); reached stage 41 of [I have it in me](../quests/maggots.md#stage-41); reached stage 42 of [I have it in me](../quests/maggots.md#stage-42); reached stage 43 of [I have it in me](../quests/maggots.md#stage-43) → **stage 45**. NPC: “That's all I need to cure you. Good work.”

???+ note "Stage 50: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Drink the potion.” — **conditions:** reached stage 45 of [I have it in me](../quests/maggots.md#stage-45) → **stage 50**; also gives [Kazaul rotworm](../items/potion_rotworm.md), applies condition rotworm. NPC: “[The potion smells rancid, but you manage to drink it all down. The pain from the stomach decreases, and you feel one…”

???+ note "Stage 51: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “OK, I will hold on to it.” — **conditions:** reached stage 50 of [I have it in me](../quests/maggots.md#stage-50) → **stage 51**. NPC: “Seeing as you managed to pull through all of this, I would be willing to offer you the help of giving you blessings of…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Stage 30 journal text changed<br>Stage 42 journal text changed<br>Dialogue: 4 lines changed<br>· text: “(The potion smells rancid, but you manage to drink it all down. The p…” → “[The potion smells rancid, but you manage to drink it all down. The p…”<br>· text: “Bring me these things and I will be able to help you with your .. con…” → “Bring me these things and I will be able to help you with your ... co…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=maggots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=maggots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=maggots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=maggots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=maggots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `maggots` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 40, 41, 42, 43, 45, 50, 51 |
    | Dialogue nodes setting stages | 10: `toszylae_6`, 20: `ulirfendor_infected_15`, 21: `ulirfendor_infected_17`, 30: `talion_infect_19`, 40: `talion_bone_2`, 41: `talion_hair_2`, 42: `talion_irdegh_2`, 43: `talion_vial_2`, 45: `talion_cure_1`, 50: `talion_cure_7`, 51: `talion_cured_9` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
