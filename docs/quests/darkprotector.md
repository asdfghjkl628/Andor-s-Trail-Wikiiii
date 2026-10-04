# The dark protector

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `darkprotector` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 40, 41, 70) |
| **Started by** | reading a sign on [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) |
| **NPCs involved** | [Ulirfendor](../monsters/ulirfendor.md) |
| **Locations** | [waytobrimhavencave4](../maps/waytobrimhavencave4.md) |
| **Total XP** | 55,000 |
| **Related quests** | 1 |

</div>

## Overview

> I have found a strange looking helmet from the lich 'Toszylae' that I defeated. I should go ask Ulirfendor if he knows anything about it.

## Prerequisites to start

None: talk to reading a sign on [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [An involuntary carrier](toszylae.md#stage-70) | stage 70 there needs stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I have found a strange looking helmet from the lich 'Toszylae' that I defeated. I should go ask Ulirfendor if he knows anything about it.<br><span class="qnote">⚡ A scripted event can now trigger on [Waytobrimhavencave3a](../maps/waytobrimhavencave3a.md).</span> | reading a sign on [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) | – | gives [Strange looking helmet](../items/helm_protector0.md) |
| <span id="stage-15"></span>15 | Ulirfendor in the same dungeon thinks this artifact is what the shrine speaks of, and that it will bring misery to the surroundings of whoever carries it. He wants me to help him destroy it immediately. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-26"></span>26 | To destroy the artifact, I would need give the helmet and the heart of the lich to Ulirfendor. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 15 | – |
| <span id="stage-30"></span>30 | I have given the helmet to Ulirfendor. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | hand over 1× [Demon heart](../items/toszylae_heart.md), hand over 1× [Strange looking helmet](../items/helm_protector0.md), stage 15 | – |
| <span id="stage-31"></span>31 | I have given the heart of the lich to Ulirfendor. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | hand over 1× [Demon heart](../items/toszylae_heart.md), hand over 1× [Strange looking helmet](../items/helm_protector0.md), stage 15 | – |
| <span id="stage-35"></span>35 | Ulirfendor has destroyed the artifact. The people of the surrounding towns are safe from whatever misery the helmet would have brought. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 31 | – |
| <span id="stage-40"></span>40 | For helping with both the lich and the helmet, Ulirfendor has given me the dark blessing of the Shadow. **(completes quest)** | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 35 | 15,000 XP<br>+1 [Dark blessing of the Shadow](../skills/shadowBless.md) |
| <span id="stage-41"></span>41 | For helping with both the lich and the helmet, Ulirfendor wanted to give me the dark blessing of the Shadow, but I declined. **(completes quest)** | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 35 | 35,000 XP |
| <span id="stage-50"></span>50 | I have decided to keep the helmet for myself. Who knows what power I could gain from it. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-51"></span>51 | Ulirfendor attacked me for keeping the helmet. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-55"></span>55 | I found a book by the shrine where Ulirfendor was. The book talks of a ritual that would restore the helmet to its true power. I should complete the ritual by the shrine if I want to use the helmet. | reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) | – | – |
| <span id="stage-60"></span>60 | I have started the Kazaul ritual. | reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) | – | – |
| <span id="stage-65"></span>65 | I have placed the helmet in front of the Kazaul shrine. | reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) | – | – |
| <span id="stage-66"></span>66 | I have placed the lich's heart in front of the Kazaul shrine. | reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) | hand over 1× [Demon heart](../items/toszylae_heart.md), stage 65 | – |
| <span id="stage-70"></span>70 | The ritual is complete, and I have restored the power of the helmet to its former glory. **(completes quest)** | reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) | stage 66 | 5,000 XP<br>gives [Dark protector](../items/helm_protector.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. reading a sign on [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md) → the conversation leads here automatically → **stage 10**; also gives [Strange looking helmet](../items/helm_protector0.md). NPC: “[On the shrine that was behind the lich 'Toszylae' that you defeated, you find a strange looking helmet]”

???+ note "Stage 15: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “What was that about destroying the helmet?” — **conditions:** reached stage 15 of [The dark protector](../quests/darkprotector.md#stage-15) → **stage 15**. NPC: “I say, we must destroy that item immediately to make sure that the Kazaul taint is forever cleansed from this place…”

???+ note "Stage 26: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “I managed to get the heart of the lich, would that do?” — **conditions:** reached stage 15 of [The dark protector](../quests/darkprotector.md#stage-15) → **stage 26**. NPC: “The heart? Oh yes, that would surely do.”

???+ note "Stage 30: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “Here is the helmet and the heart.” — **conditions:** reached stage 15 of [The dark protector](../quests/darkprotector.md#stage-15); hand over 1× [Strange looking helmet](../items/helm_protector0.md); hand over 1× [Demon heart](../items/toszylae_heart.md) → **stage 30**. NPC: “Excellent. I will begin the procedure immediately.”

???+ note "Stage 31: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “Here is the helmet and the heart.” — **conditions:** reached stage 15 of [The dark protector](../quests/darkprotector.md#stage-15); hand over 1× [Strange looking helmet](../items/helm_protector0.md); hand over 1× [Demon heart](../items/toszylae_heart.md) → **stage 31**. NPC: “Excellent. I will begin the procedure immediately.”

???+ note "Stage 35: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → the conversation leads here automatically — **conditions:** reached stage 31 of [The dark protector](../quests/darkprotector.md#stage-31) → **stage 35**. NPC: “[The helmet completely shatters, leaving nothing but a fine dust]”

???+ note "Stage 40: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “Thank you, please go ahead.” — **conditions:** reached stage 35 of [The dark protector](../quests/darkprotector.md#stage-35) → **stage 40**; also +1 [Dark blessing of the Shadow](../skills/shadowBless.md). NPC: “There. You now have the dark blessing of the Shadow upon you.”

???+ note "Stage 41: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “Thank you, but that will not be necessary. I am just happy to help.” — **conditions:** reached stage 35 of [The dark protector](../quests/darkprotector.md#stage-35) → **stage 41**. NPC: “You truly have a large heart.”

???+ note "Stage 50: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [The dark protector](../quests/darkprotector.md#stage-50) → **stage 50**. NPC: “What is this!? I knew there was something wrong about you the first time I saw you.”

???+ note "Stage 51: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → the conversation leads here automatically — **conditions:** reached stage 51 of [The dark protector](../quests/darkprotector.md#stage-51) → **stage 51**. NPC: “By the Shadow, I will stop you. Whatever it takes. You will not live to see the next day!”

???+ note "Stage 55: 1 route"

    1. reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) → the conversation leads here automatically → **stage 55**. NPC: “The ritual itself would require the heart of a lich, and from the text surrounding the ritual in the book, it could…”

???+ note "Stage 60: 1 route"

    1. reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) → choose “Begin the ritual.” → **stage 60**. NPC: “You place yourself in front of the shrine, kneeling like the drawings in the book show.”

???+ note "Stage 65: 1 route"

    1. reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) → the conversation leads here automatically — **conditions:** reached stage 65 of [The dark protector](../quests/darkprotector.md#stage-65) → **stage 65**. NPC: “You place the helmet on the ground in front of you, leaning it slightly against the shrine.”

???+ note "Stage 66: 1 route"

    1. reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) → choose “Place the heart of the lich in front of the shrine” — **conditions:** reached stage 65 of [The dark protector](../quests/darkprotector.md#stage-65); hand over 1× [Demon heart](../items/toszylae_heart.md) → **stage 66**. NPC: “You place the heart of the lich beside the helmet in front of the shrine.”

???+ note "Stage 70: 1 route"

    1. reading a sign on [waytobrimhavencave4](../maps/waytobrimhavencave4.md) → choose “Take the helmet” — **conditions:** reached stage 66 of [The dark protector](../quests/darkprotector.md#stage-66) → **stage 70**; also gives [Dark protector](../items/helm_protector.md). NPC: “You take the helmet, and examine it more closely.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “(The helmet completely shatters, leaving nothing but a fine dust.)” → “[The helmet completely shatters, leaving nothing but a fine dust]”<br>· text: “(Among the remains of the lich 'Toszylae' that you defeated, you find…” → “[On the shrine that was behind the lich 'Toszylae' that you defeated,…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkprotector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkprotector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkprotector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkprotector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkprotector.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `darkprotector` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 26, 30, 31, 35, 40, 41, 50, 51, 55, 60, 65, 66, 70 |
    | Dialogue nodes setting stages | 10: `sign_toszylae_1`, 15: `ulirfendor_helmet_8`, 26: `ulirfendor_helmet_n6`, 30: `ulirfendor_dp_proc_2`, 31: `ulirfendor_dp_proc_2`, 35: `ulirfendor_dp_proc_12`, 40: `ulirfendor_dp_bless_5`, 41: `ulirfendor_dp_bless_1`, 50: `ulirfendor_helmet_keep2`, 51: `ulirfendor_helmet_keep3`, 55: `sign_ulirfendor_4`, 60: `sign_ulirfendor_5`, 65: `sign_ulirfendor_6`, 66: `sign_ulirfendor_7`, 70: `sign_ulirfendor_14` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
