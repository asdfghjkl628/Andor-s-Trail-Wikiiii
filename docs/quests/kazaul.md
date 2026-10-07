---
description: "Lights in the dark is a quest in Andor's Trail, started by Throdna (blackwater_mountain50). 15 stages, 6,800 XP in total. I have made my way into the inner chamber in the Blackwater mountain settlement and found a group of mages led by a man named Throdna."
---

# Lights in the dark

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `kazaul` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 100) |
| **Started by** | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) |
| **NPCs involved** | [Kazaul guardian](../monsters/kazaul_guardian.md), [Throdna](../monsters/throdna.md) |
| **Locations** | [blackwater_mountain42](../maps/blackwater_mountain42.md), [blackwater_mountain50](../maps/blackwater_mountain50.md) |
| **Total XP** | 6,800 |
| **Related quests** | 1 |

</div>

## Overview

> I have made my way into the inner chamber in the Blackwater mountain settlement and found a group of mages led by a man named Throdna.

## Prerequisites to start

None: talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Vines in bwm_17 (hidden flag)](bwm17_vine.md#stage-3) | stage 3 there needs stage 9 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-8"></span>8 | I have made my way into the inner chamber in the Blackwater mountain settlement and found a group of mages led by a man named Throdna. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | – | – |
| <span id="stage-9"></span>9 | Throdna seems very interested in someone (or something) called Kazaul, and in particular a ritual performed in its name. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 10 | – |
| <span id="stage-10"></span>10 | I have agreed to help Throdna find out more about the ritual itself, by looking for pieces of the ritual that apparently are scattered across the mountain. I should go look for the parts of the Kazaul ritual on the mountain path down from Blackwater mountain to Prim. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | – | – |
| <span id="stage-11"></span>11 | I need to find the two parts of the chant and the three pieces describing the ritual itself, and return to Throdna once I have found them all. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 10 | – |
| <span id="stage-21"></span>21 | I have found the first half of the chant for the Kazaul ritual. | reading a sign on [blackwater_mountain30](../maps/blackwater_mountain30.md) | stage 10 | – |
| <span id="stage-22"></span>22 | I have found the second half of the chant for the Kazaul ritual. | reading a sign on [blackwater_mountain16](../maps/blackwater_mountain16.md) | stage 10 | – |
| <span id="stage-25"></span>25 | I have found the first piece of the Kazaul ritual. | reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) | stage 10 | – |
| <span id="stage-26"></span>26 | I have found the second piece of the Kazaul ritual. | reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) | stage 10 | – |
| <span id="stage-27"></span>27 | I have found the third piece of the Kazaul ritual. | reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) | stage 10 | – |
| <span id="stage-30"></span>30 | Throdna thanked me for finding all the pieces of the ritual. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | – | 3,600 XP |
| <span id="stage-40"></span>40 | Throdna wants me to put an end to the Kazaul spawn uprising that has taken place near the Blackwater mountain. There is a shrine at the base of the mountain that i should investigate closer. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 41 | – |
| <span id="stage-41"></span>41 | I have been given a vial of purifying spirit that Throdna wants me to apply to the shrine of Kazaul. I should return to Throdna when I have found and purified the shrine. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | – | gives [Vial of purifying spirit](../items/q_kazaul_vial.md) |
| <span id="stage-50"></span>50 | In the shrine at the base of Blackwater mountain, I met a guardian of Kazaul. By reciting the verses of the ritual chant, I was able to make the guardian attack me. | [Kazaul guardian](../monsters/kazaul_guardian.md) ([blackwater_mountain42](../maps/blackwater_mountain42.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | I have purified the shrine of Kazaul. | reading a sign on [blackwater_mountain42](../maps/blackwater_mountain42.md) | hand over 1× [Vial of purifying spirit](../items/q_kazaul_vial.md) | 3,200 XP |
| <span id="stage-100"></span>100 | I had expected some form of appreciation from Throdna for helping him learn more about the ritual and for purifying the shrine. But he seemed more occupied with rambling on about Kazaul. I could not make out anything sane from his ramblings. **(completes quest)** | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 41, stage 60 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 8: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “What was that you talked about when I arrived, Kazaul?” → **stage 8**. NPC: “Kazaul, the Shadow spawn of red marrow.”

???+ note "Stage 9: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 9**. NPC: “As I said, we want to learn more about the ritual itself.”

???+ note "Stage 10: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “I would be glad to help.” — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 10**. NPC: “OK. Find me the pieces of the ritual that the former messenger carried on him. They should be found somewhere on the…”

???+ note "Stage 11: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “I will return with your parts of the ritual.” — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 11**. NPC: “Yes, you will.”

???+ note "Stage 21: 1 route"

    1. reading a sign on [blackwater_mountain30](../maps/blackwater_mountain30.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 21**. NPC: “You find a piece of paper partially frozen in the snow. You can barely make out the phrase 'Kazaul, defiler of the…”

???+ note "Stage 22: 1 route"

    1. reading a sign on [blackwater_mountain16](../maps/blackwater_mountain16.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 22**. NPC: “You find a piece of torn paper stuck in the thick bush. You can barely make out the phrase 'Kazaul, destroyer of…”

???+ note "Stage 25: 1 route"

    1. reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 25**. NPC: “You find a piece of paper describing the beginnings of some form of ritual. This must be the first part of the Kazaul…”

???+ note "Stage 26: 1 route"

    1. reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 26**. NPC: “You find a piece of paper describing the main part of the Kazaul ritual. This must be the second part of the Kazaul…”

???+ note "Stage 27: 1 route"

    1. reading a sign on [blackwater_mountain38](../maps/blackwater_mountain38.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [Lights in the dark](../quests/kazaul.md#stage-10) → **stage 27**. NPC: “You find a piece of paper describing the end of the Kazaul ritual. This must be the third part of the Kazaul ritual.”

???+ note "Stage 30: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Lights in the dark](../quests/kazaul.md#stage-30) → **stage 30**. NPC: “You actually found all five pieces? I suppose I should thank you. Well then. Thank you.”

???+ note "Stage 40: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41) → **stage 40**. NPC: “Second, we need you to take a vial of purifying spirit and apply it to the shrine.”

???+ note "Stage 41: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “Sounds easy. I'll do it.” — **conditions:** reached stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41) → **stage 41**; also gives [Vial of purifying spirit](../items/q_kazaul_vial.md). NPC: “Good, here is the vial. Now hurry.”

???+ note "Stage 50: 1 route"

    1. Talk to [Kazaul guardian](../monsters/kazaul_guardian.md) ([blackwater_mountain42](../maps/blackwater_mountain42.md)) → choose “Kazaul, defiler of the Elytharan Temple.” — **conditions:** reached stage 40 of [Lights in the dark](../quests/kazaul.md#stage-40) → **stage 50**. NPC: “[You see the burning eyes of the guardian instantly turn into a dark red haze]”

???+ note "Stage 60: 1 route"

    1. reading a sign on [blackwater_mountain42](../maps/blackwater_mountain42.md) → choose “Apply the vial of purifying spirit on the formation.” — **conditions:** hand over 1× [Vial of purifying spirit](../items/q_kazaul_vial.md) → **stage 60**. NPC: “You gently pour the contents of the vial onto the formation.”

???+ note "Stage 100: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “Yes, it is done.” — **conditions:** reached stage 41 of [Lights in the dark](../quests/kazaul.md#stage-41); reached stage 60 of [Lights in the dark](../quests/kazaul.md#stage-60) → **stage 100**. NPC: “Good. We must hurry to continue our research on Kazaul.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | stage 8 journal text changed; stage 10 journal text changed; stage 40 journal text changed; stage 50 journal text changed<br>Dialogue: 2 lines changed<br>· text: “Ok. Find me the pieces of the ritual that the former messenger carrie…” → “OK. Find me the pieces of the ritual that the former messenger carrie…”<br>· text: “(You see the burning eyes of the guardian instantly turn into a dark …” → “[You see the burning eyes of the guardian instantly turn into a dark …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kazaul.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kazaul.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kazaul.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kazaul.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kazaul.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `kazaul` |
    | showInLog | 1 |
    | Stage IDs | 8, 9, 10, 11, 21, 22, 25, 26, 27, 30, 40, 41, 50, 60, 100 |
    | Dialogue nodes setting stages | 8: `throdna_8`, 9: `throdna_12`, 10: `throdna_19`, 11: `throdna_20`, 21: `sign_blackwater30_qstarted`, 22: `sign_blackwater16_qstarted`, 25: `sign_blackwater38_1_qstarted`, 26: `sign_blackwater38_2_qstarted`, 27: `sign_blackwater38_3_qstarted`, 30: `throdna_return_3`, 40: `throdna_return_10`, 41: `throdna_return_12`, 50: `kazaul_guardian_3`, 60: `sign_kazaul_5`, 100: `throdna_purify_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
