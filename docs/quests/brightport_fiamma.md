# Too hot to handle

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brightport_fiamma` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 45, 50) |
| **Started by** | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) |
| **NPCs involved** | [Fiamma](../monsters/brightportsmith.md) |
| **Locations** | [brightport_weapon](../maps/brightport_weapon.md) |
| **Related quests** | 1 |

</div>

## Overview

> Fiamma, the swordsmith of Brightport. Is willing to forge me a sword if I can bring him the materials.

## Prerequisites to start

Start with [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)). Required:

- reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87)
- NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-87) | stage 87 reached, for stages 5, 10, 15, 20 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-175) | stage 175 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-176) | stage 176 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-177) | stage 177 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-178) | stage 178 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-179) | stage 179 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-180) | stage 180 there needs stage 15 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-181) | stage 181 there needs stage 15 here |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-175) | reaching stage 25 here closes stage 175 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-176) | reaching stage 25 here closes stage 176 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-177) | reaching stage 25 here closes stage 177 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-178) | reaching stage 25 here closes stage 178 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-179) | reaching stage 25 here closes stage 179 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-180) | reaching stage 25 here closes stage 180 there |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-181) | reaching stage 25 here closes stage 181 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | Fiamma, the swordsmith of Brightport. Is willing to forge me a sword if I can bring him the materials. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | – |
| <span id="stage-10"></span>10 | In the mountains near the road to Remgard lies a dangerous area overrun by Arulirs, beasts with skin as tough as steel. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | – |
| <span id="stage-15"></span>15 | Fiamma has asked for a strip of Arulir skin, coveted for its durability and flexibility. He also requires 15 cold lava rocks from the mountain cave, which burn hotter than any ordinary coal. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | – |
| <span id="stage-20"></span>20 | The final material is a red crystal from a Gornaud, a ferocious beast that sometimes forms these rare crystals in its body. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | – |
| <span id="stage-25"></span>25 | I brought Fiamma the arulir skin and lava rocks. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | hand over 15× [Cold Lava Rock](../items/lava_rock_cold.md), hand over 1× [Arulir skin](../items/arulir_skin.md), stage 15, stage 20 | – |
| <span id="stage-30"></span>30 | I brought Fiamma the red crystal. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | hand over 1× [Red Crystals](../items/crystal_red.md), stage 20 | – |
| <span id="stage-35"></span>35 | I gave all the materials to Fiamma. He thanked me and told me to come back later when it's finished. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | stage 25, stage 30 | starts timer “fiamma_forge” |
| <span id="stage-40"></span>40 | To my surprise, the sword he forged heats up on contact with air and requires special gloves to handle. They are made of the Arulir skin I brought. | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | – |
| <span id="stage-45"></span>45 | I asked Fiamma to give me something else, and he gave me a very sharp glaive. **(completes quest)** | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | gives 1× [Glaive of Imeria](../items/glaive_butcher.md) |
| <span id="stage-50"></span>50 | I thanked Fiamma and went on my merry way. **(completes quest)** | [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) | – | gives 1× [Glaive of Imeria](../items/glaive_butcher.md)<br>gives 1× [Flaming greatsword](../items/brightportflamesword.md)<br>gives 1× [Salamander gloves](../items/brightport_glove.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 5: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “There is no task beyond my skill.” — **conditions:** reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87); NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 5**. NPC: “OK. First, we have to discuss the materials I have in mind. I presume you have heard of the town of Remgard?”

???+ note "Stage 10: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Yes I have heard of it.” — **conditions:** reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87); NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 10**. NPC: “Many travelers pass through Brightport on their way to and back from Remgard. The town lies high in the mountains, and…”

???+ note "Stage 15: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Yes I have heard of it.” — **conditions:** reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87); NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 15**. NPC: “First, if you can travel there, I want a strip of the arulir's skin - rumored to be tougher than steel but as flexible…”

???+ note "Stage 20: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Yes I have heard of it.” — **conditions:** reached stage 87 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-87); NOT reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 20**. NPC: “And lastly, the material from which I will forge a blade, a red crystal from a gornaud. This material, which their…”

???+ note "Stage 25: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “I have the cold lava rocks and arulir skin.” — **conditions:** hand over 15× [Cold Lava Rock](../items/lava_rock_cold.md); hand over 1× [Arulir skin](../items/arulir_skin.md); NOT reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25); reached stage 15 of [Too hot to handle](../quests/brightport_fiamma.md#stage-15); reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 25**. NPC: “Yes, those look good. Thanks!”

???+ note "Stage 30: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “I have the red crystal here.” — **conditions:** hand over 1× [Red Crystals](../items/crystal_red.md); NOT reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); reached stage 20 of [Too hot to handle](../quests/brightport_fiamma.md#stage-20) → **stage 30**. NPC: “Wow. It looks magnificent!”

???+ note "Stage 35: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → the conversation leads here automatically — **conditions:** reached stage 25 of [Too hot to handle](../quests/brightport_fiamma.md#stage-25); reached stage 30 of [Too hot to handle](../quests/brightport_fiamma.md#stage-30); NOT reached stage 35 of [Too hot to handle](../quests/brightport_fiamma.md#stage-35) → **stage 35**; also starts timer “fiamma_forge”. NPC: “With all these quality materials, I can forge you something magnificent enough to equal the legends. Come back to me…”

???+ note "Stage 40: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → the conversation leads here automatically — **conditions:** 6 rounds passed since timer “fiamma_forge”; NOT reached stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50) → **stage 40**. NPC: “I was hoping to keep the Arulir skin for a pair of forging gloves, but I ended up making these smaller, heat-resistant…”

???+ note "Stage 45: 1 route"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Yes, I would prefer that.” — **conditions:** 6 rounds passed since timer “fiamma_forge”; NOT reached stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50) → **stage 45**; also gives 1× [Glaive of Imeria](../items/glaive_butcher.md). NPC: “Take this glaive, it was given to me by my old master from Nor City. It was originally forged for nobility but after…”

???+ note "Stage 50: 2 routes"

    1. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Yes, I would prefer that.” — **conditions:** 6 rounds passed since timer “fiamma_forge”; NOT reached stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50) → **stage 50**; also gives 1× [Glaive of Imeria](../items/glaive_butcher.md). NPC: “Take this glaive, it was given to me by my old master from Nor City. It was originally forged for nobility but after…”
    2. Talk to [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) → choose “Sounds nice, I'll take it.” — **conditions:** 6 rounds passed since timer “fiamma_forge”; NOT reached stage 50 of [Too hot to handle](../quests/brightport_fiamma.md#stage-50) → **stage 50**; also gives 1× [Flaming greatsword](../items/brightportflamesword.md), gives 1× [Salamander gloves](../items/brightport_glove.md). NPC: “Well, usually I would have my reservations about giving someone as young as you something this dangerous. But you're…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_fiamma.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_fiamma.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_fiamma.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_fiamma.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_fiamma.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brightport_fiamma` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |
    | Dialogue nodes setting stages | 5: `brightport_fiamma3`, 10: `brightport_fiamma5`, 15: `brightport_fiamma7`, 20: `brightport_fiamma8`, 25: `brightport_fiamma9`, 30: `brightport_fiamma10`, 35: `brightport_fiamma11`, 40: `brightport_fiamma17`, 45: `brightport_fiamma21`, 50: `brightport_fiamma21`, 50: `brightport_fiamma20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
