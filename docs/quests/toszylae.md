# An involuntary carrier

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `toszylae` |
| **In journal** | Yes |
| **Stages** | 12 (completes at 70) |
| **Started by** | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) |
| **NPCs involved** | [Radiant guardian](../monsters/toszylae_guard.md), [Toszylae](../monsters/toszylae.md), [Ulirfendor](../monsters/ulirfendor.md) |
| **Locations** | [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md), [waytobrimhavencave4](../maps/waytobrimhavencave4.md) |
| **Total XP** | 27,000 |
| **Related quests** | 2 |

</div>

## Overview

> On the road between Loneford and Brimhaven, I found a dried up lake-bed with a major cavern below. Deep inside the cavern, I met Ulirfendor - a priest of the Shadow from Brimhaven. Ulirfendor is trying to translate the inscriptions on a shrine of Kazaul, and has determined that it speaks of the 'Dark protector', but he is unsure what that refers to. Whatever it means, he is determined that it…

## Prerequisites to start

Start with [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)). Required:

- reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The dark protector](darkprotector.md#stage-10) | stage 10 reached, for stage 70 here |
| Unlocks | [I have it in me](maggots.md#stage-20) | stage 20 there needs stage 60 here |
| Unlocks | [I have it in me](maggots.md#stage-21) | stage 21 there needs stages 60, 70 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | On the road between Loneford and Brimhaven, I found a dried up lake-bed with a major cavern below. Deep inside the cavern, I met Ulirfendor - a priest of the Shadow from Brimhaven. Ulirfendor is trying to translate the inscriptions on a shrine of Kazaul, and has determined that it speaks of the 'Dark protector', but he is unsure what that refers to. Whatever it means, he is determined that it must be stopped. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 15 | – |
| <span id="stage-11"></span>11 | Ulirfendor needs help with figuring out what some of the missing parts on the shrine says. The inscription reads 'Kulauil hamar urum Kazaul'te', but the next parts have been completely eroded from the rock. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 15 | – |
| <span id="stage-15"></span>15 | I have agreed to help Ulirfendor find out what the missing parts of the inscription might be. Ulirfendor believes the shrine speaks of a powerful creature that lives deeper inside the dungeon. Maybe that could provide some clue as to what the missing parts are. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-20"></span>20 | Deep inside the dungeon, I encountered a radiant guardian, guarding some other being. The guardian uttered the phrases 'Kulauil hamar urum Kazaul'te. Kazaul hamat urul'. This must be what Ulirfendor was looking for. I should return to him at once. | [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | stage 15 | – |
| <span id="stage-21"></span>21 | I tried to attack the guardian, but was unable to even reach it. Some powerful force held me back. Maybe Ulirfendor knows more. | [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | stage 32 | – |
| <span id="stage-30"></span>30 | Ulirfendor was very pleased to hear that I uncovered the missing parts of the inscription. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 15, stage 20 | 2,000 XP |
| <span id="stage-32"></span>32 | He also told me the continuation of the inscription, but did not know what it means. I should go back to the guardian and speak the words that Ulirfendor told me. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-42"></span>42 | I have spoken the words to the guardian. | [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | stage 32 | 5,000 XP |
| <span id="stage-45"></span>45 | The guardian gave off a chilling laughter, and started attacking me. | [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | – | – |
| <span id="stage-50"></span>50 | I defeated the guardian and reached the lich 'Toszylae'. The lich managed to infect me with something. I must kill the lich and return to Ulirfendor. | [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) | – | applies condition rotworm<br>sets stage 10 of [I have it in me](../quests/maggots.md#stage-10) |
| <span id="stage-60"></span>60 | Ulirfendor told me that he had managed to translate the parts of the inscription that I told the guardian. Apparently, what I told the guardian roughly means 'My body for Kazaul'. Ulirfendor was very concerned about what this means for me, and was very regretful that he had made me speak the words. | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | – | – |
| <span id="stage-70"></span>70 | Ulirfendor was very happy to hear that I managed to defeat the lich. With the lich defeated, the people in the surrounding areas should be safe now. **(completes quest)** | [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) | stage 60 | 20,000 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “What have you translated so far?” — **conditions:** reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15) → **stage 10**. NPC: “Regardless, it must be stopped, whatever it means. Maybe it refers to something deeper down this cave? I have not…”

???+ note "Stage 11: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “What have you translated so far?” — **conditions:** reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15) → **stage 11**. NPC: “The last part of this piece has been eroded from the rock. It begins with 'Kulauil hamar urum Kazaul'te'. But what is…”

???+ note "Stage 15: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “No, I have not found any clues yet.” — **conditions:** reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15) → **stage 15**. NPC: “Also, I should warn you that I believe the shrine talks of a powerful creature somewhere in this cave. Maybe if you…”

???+ note "Stage 20: 1 route"

    1. Talk to [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → the conversation leads here automatically — **conditions:** reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15) → **stage 20**. NPC: “Kulauil hamar urum Kazaul'te. Kazaul hamat urul.”

???+ note "Stage 21: 1 route"

    1. Talk to [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → choose “[Attack]” — **conditions:** reached stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32) → **stage 21**. NPC: “[As you try to make your attack against the guardian, your arms are held back by an enormous force]”

???+ note "Stage 30: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “Yes, the creature also spoke the words 'Kazaul hamat urul', maybe that is part of the missing piece?” — **conditions:** reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15); reached stage 20 of [An involuntary carrier](../quests/toszylae.md#stage-20) → **stage 30**. NPC: “Excellent work my friend! Now I just need to translate it.”

???+ note "Stage 32: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “No, not yet. But I am working on it.” — **conditions:** reached stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32) → **stage 32**. NPC: “Good. Please return as soon as possible.”

???+ note "Stage 42: 1 route"

    1. Talk to [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → choose “Klatam ur turum Kazaul'te” — **conditions:** reached stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32) → **stage 42**. NPC: “Kulum Kazaul.”

???+ note "Stage 45: 1 route"

    1. Talk to [Radiant guardian](../monsters/toszylae_guard.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → the conversation leads here automatically — **conditions:** reached stage 45 of [An involuntary carrier](../quests/toszylae.md#stage-45) → **stage 45**. NPC: “[It raises its claw-like hands above its head, looking to get ready to strike at you]”

???+ note "Stage 50: 1 route"

    1. Talk to [Toszylae](../monsters/toszylae.md) ([waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)) → the conversation leads here automatically → **stage 50**; also applies condition rotworm, sets stage 10 of [I have it in me](../quests/maggots.md#stage-10). NPC: “[As if having swallowed a thousand needles, you are suddenly stricken with a cascading series of spikes of pain…”

???+ note "Stage 60: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60) → **stage 60**. NPC: “Oh, what have I done? I made you say it, and now you are touched by its vile essence.”

???+ note "Stage 70: 1 route"

    1. Talk to [Ulirfendor](../monsters/ulirfendor.md) ([waytobrimhavencave4](../maps/waytobrimhavencave4.md)) → choose “I at least defeated the lich that infected me with this thing.” — **conditions:** reached stage 60 of [An involuntary carrier](../quests/toszylae.md#stage-60); reached stage 10 of [The dark protector](../quests/darkprotector.md#stage-10) → **stage 70**. NPC: “Oh, that is good news indeed. A lich you say? With your help, the people of the surrounding towns should be safe from…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=toszylae.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=toszylae.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=toszylae.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=toszylae.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=toszylae.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `toszylae` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 15, 20, 21, 30, 32, 42, 45, 50, 60, 70 |
    | Dialogue nodes setting stages | 10: `ulirfendor_16`, 11: `ulirfendor_19`, 15: `ulirfendor_22`, 20: `toszylae_guard_2_1`, 21: `toszylae_guard_2_n2`, 30: `ulirfendor_findparts_5`, 32: `ulirfendor_findparts_9`, 42: `toszylae_guard_4`, 45: `toszylae_guard_8`, 50: `toszylae_6`, 60: `ulirfendor_infected_8`, 70: `ulirfendor_demon_d1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
