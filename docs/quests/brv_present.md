# Honor your parents

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_present` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 40, 50, 60) |
| **Started by** | [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) |
| **NPCs involved** | [Mikhail](../monsters/mikhail.md), [Shop Owner](../monsters/brv_shop_owner.md) |
| **Locations** | [brimhaven_shop](../maps/brimhaven_shop.md), [home](../maps/home.md), [waytogalmore0](../maps/waytogalmore0.md) |
| **Total XP** | 600 |
| **Related quests** | 3 |

</div>

## Overview

> I have decided to give a necklace to my father Mikhail, in our family colors of red, green, and white.

## Prerequisites to start

Start with [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)). Required:

- reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brv_nondisplay (hidden flag)](brv_nondisplay.md#stage-130) | stage 130 reached, for stages 10, 20 here |
| Requires | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-40) | stage 40 reached, for stages 40, 50, 60 here |
| Requires | [Breakfast bread](mikhail_bread.md#stage-10) | stage 10 reached, for stages 30, 40, 50, 60 here |
| Blocked by | [brv_nondisplay_multipurpose (hidden flag)](brv_nondisplay_multipurpose.md#stage-40) | stage 40 must NOT be reached, for stage 30 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I have decided to give a necklace to my father Mikhail, in our family colors of red, green, and white. | [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) | – | – |
| <span id="stage-20"></span>20 | I have purchased a necklace. | [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) | pay 5 gold, pay 50,000 gold, pay 500 gold | gives 1× [Necklace for father (expensive)](../items/necklace_for_father3.md)<br>gives 1× [Necklace for father](../items/necklace_for_father2.md)<br>gives 1× [Necklace for father (cheap)](../items/necklace_for_father1.md) |
| <span id="stage-30"></span>30 | Mikhail didn't want to take the necklace. He was angry because I didn't focus on finding Andor. | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | My father didn't seem very happy with the cheap necklace. **(completes quest)** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | hand over 1× [Necklace for father (cheap)](../items/necklace_for_father1.md), stage 20 | 50 XP |
| <span id="stage-50"></span>50 | My father was very happy with the nice necklace. **(completes quest)** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | hand over 1× [Necklace for father](../items/necklace_for_father2.md), stage 20 | 500 XP |
| <span id="stage-60"></span>60 | My father was disappointed with the pretentious necklace I bought. **(completes quest)** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | hand over 1× [Necklace for father (expensive)](../items/necklace_for_father3.md), stage 20 | 50 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) → the conversation leads here automatically — **conditions:** reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130) → **stage 10**. NPC: “How can I serve you, traveler?”

???+ note "Stage 20: 3 routes"

    1. Talk to [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) → choose “Give me a necklace for 50,000 gold coins.” — **conditions:** reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 50,000 gold → **stage 20**; also gives 1× [Necklace for father (expensive)](../items/necklace_for_father3.md). NPC: “Take this wonderful necklace. Your father will be very happy.”
    2. Talk to [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) → choose “Give me a necklace for 500 gold coins.” — **conditions:** reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 500 gold → **stage 20**; also gives 1× [Necklace for father](../items/necklace_for_father2.md). NPC: “Here is the necklace.”
    3. Talk to [Shop Owner](../monsters/brv_shop_owner.md) ([brimhaven_shop](../maps/brimhaven_shop.md)) → choose “Give me a necklace for 5 gold coins.” — **conditions:** reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130); pay 5 gold → **stage 20**; also gives 1× [Necklace for father (cheap)](../items/necklace_for_father1.md). NPC: “Take this... valuable necklace. Your father will be proud to wear it.”

???+ note "Stage 30: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “I have a present for you.” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); NOT reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40) → **stage 30**. NPC: “I asked you to search for your brother Andor and you did not find out anything and instead you are bringing me a…”

???+ note "Stage 40: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “[Give him the cheap necklace]” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father (cheap)](../items/necklace_for_father1.md) → **stage 40**. NPC: “Hm, thank you. Looks like you spent all your pocket money for this.”

???+ note "Stage 50: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “[Give him the necklace]” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father](../items/necklace_for_father2.md) → **stage 50**. NPC: “Thank you my child for this wonderful necklace. Oh and it is in our family colors!”

???+ note "Stage 60: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “[Give him the expensive necklace]” — **conditions:** reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10); reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40); hand over 1× [Necklace for father (expensive)](../items/necklace_for_father3.md) → **stage 60**. NPC: “Oh, where did you get the money to buy this? Maybe I don't want to know...”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 8 lines added |
| [v0.7.12](../versions/0.7.12.md) | stage 10 journal text changed; stage 20 journal text changed; stage 30 journal text changed; stage 40 journal text changed; stage 50 journal text changed; stage 60 journal text changed<br>Dialogue: 1 line changed<br>· text: “Thank you my son for this wonderful necklace. Oh and it is in our fam…” → “Thank you my child for this wonderful necklace. Oh and it is in our f…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “How can I serve you, Sir?” → “How can I serve you, traveler?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_present.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_present` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60 |
    | Dialogue nodes setting stages | 10: `brv_shop_owner_20`, 20: `brv_shop_owner_40_3`, 20: `brv_shop_owner_40_2`, 20: `brv_shop_owner_40_1`, 30: `mikhail_present_10`, 40: `mikhail_present_20_1`, 50: `mikhail_present_20_2`, 60: `mikhail_present_20_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
