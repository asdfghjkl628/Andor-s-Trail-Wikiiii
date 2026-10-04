# Delivery - nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_wh_delivery_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 10 |
| **Started by** | [Arcir](../monsters/arcir.md) |
| **NPCs involved** | [Arcir](../monsters/arcir.md), [Arghes](../monsters/arghes.md), [Edrin](../monsters/brv_metalsmith.md), [Mikhail](../monsters/mikhail.md), [Odirath](../monsters/stoutford_armorer.md), [Pangitain](../monsters/brv_fortune_teller.md) +4 |
| **Locations** | [blackwater_mountain54](../maps/blackwater_mountain54.md), [brimhaven2_laundry](../maps/brimhaven2_laundry.md), [brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md), [brimhaven_metalsmith](../maps/brimhaven_metalsmith.md) |
| **Total XP** | 1,975 |
| **Related quests** | 3 |

</div>

## Overview

> I delivered 'Dusty Old book'

## Prerequisites to start

Start with [Arcir](../monsters/arcir.md). Required:

- hand over 1× [Dusty old book](../items/brv_wh_item_09.md)
- reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10)
- reached stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Delivery](brv_wh_delivery.md#stage-10) | stage 10 reached, for stages 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-20) | stage 20 reached, for stage 10 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-30) | stage 30 reached, for stage 20 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-40) | stage 40 reached, for stage 30 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-50) | stage 50 reached, for stage 40 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-60) | stage 60 reached, for stage 50 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-70) | stage 70 reached, for stage 60 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-80) | stage 80 reached, for stage 70 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-90) | stage 90 reached, for stage 80 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-100) | stage 100 reached, for stage 90 here |
| Requires | [Delivery](brv_wh_delivery.md#stage-110) | stage 110 reached, for stage 100 here |
| Requires | [The silver scale](mermaid_scale.md#stage-200) | stage 200 reached, for stage 50 here |
| Requires | [Uncertain cause](wrye.md#stage-90) | stage 90 reached, for stage 80 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I delivered 'Dusty Old book' | [Arcir](../monsters/arcir.md) | hand over 1× [Dusty old book](../items/brv_wh_item_09.md) | 75 XP<br>clears stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20)<br>gives 20× [Gold coins](../items/gold.md) |
| <span id="stage-20"></span>20 | I delivered 'Striped Hammer' | [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) | hand over 1× [Striped hammer](../items/brv_wh_item_08.md) | 50 XP<br>clears stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30)<br>gives 10× [Gold coins](../items/gold.md) |
| <span id="stage-30"></span>30 | I delivered 'Pretty Porcelain Figure' | [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) | hand over 1× [Pretty porcelain figure](../items/brv_wh_item_07.md) | 250 XP<br>clears stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40)<br>gives 30× [Gold coins](../items/gold.md) |
| <span id="stage-40"></span>40 | I delivered 'Old, worn cape' | [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) | hand over 1× [Old, worn cape](../items/brv_wh_item_06.md) | 50 XP<br>clears stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50)<br>gives 10× [Gold coins](../items/gold.md) |
| <span id="stage-50"></span>50 | I delivered 'Mysterious green something' | [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) | hand over 1× [Mysterious green something](../items/brv_wh_item_05.md) | 500 XP<br>clears stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60)<br>gives 50× [Gold coins](../items/gold.md) |
| <span id="stage-60"></span>60 | I delivered 'Chandelier' | [Servant](../monsters/guynmart_servant.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) | hand over 1× [Chandelier](../items/brv_wh_item_04.md) | 250 XP<br>clears stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70)<br>gives 40× [Gold coins](../items/gold.md) |
| <span id="stage-70"></span>70 | I delivered 'Yellow boots' | [Arghes](../monsters/arghes.md) ([remgard_tavern0](../maps/remgard_tavern0.md)) | hand over 1× [Yellow boot](../items/brv_wh_item_03.md) | 500 XP<br>clears stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80)<br>gives 50× [Gold coins](../items/gold.md) |
| <span id="stage-80"></span>80 | I delivered 'Lyre' | [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) | hand over 1× [Lyre](../items/brv_wh_item_02.md) | 150 XP<br>clears stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90) |
| <span id="stage-90"></span>90 | I delivered 'Plush Pillow' | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) | hand over 1× [Plush pillow](../items/brv_wh_item_01.md) | 100 XP<br>clears stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100) |
| <span id="stage-100"></span>100 | I delivered 'Crystal Globe' | [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) | hand over 1× [Crystal globe](../items/brv_wh_item_00.md) | 50 XP<br>clears stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110)<br>gives 100× [Gold coins](../items/gold.md) |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Arcir](../monsters/arcir.md) → choose “And I'm your delivery kid. Did you order a 'Dusty old book'?” — **conditions:** hand over 1× [Dusty old book](../items/brv_wh_item_09.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20) → **stage 10**; also clears stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20), gives 20× [Gold coins](../items/gold.md). NPC: “Yes, an old but useful book, but you should have wiped it off first. Anyway, here's my delivery fee.”

???+ note "Stage 20: 1 route"

    1. Talk to [Edrin](../monsters/brv_metalsmith.md) ([brimhaven_metalsmith](../maps/brimhaven_metalsmith.md)) → choose “Hello, did you order a 'Striped Hammer'?” — **conditions:** hand over 1× [Striped hammer](../items/brv_wh_item_08.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30) → **stage 20**; also clears stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30), gives 10× [Gold coins](../items/gold.md). NPC: “Ah, yes, a striped hammer. Don't look so impatient. Here's my delivery charge, and now you can leave!”

???+ note "Stage 30: 1 route"

    1. Talk to [Odirath](../monsters/stoutford_armorer.md) ([stoutford_armorer](../maps/stoutford_armorer.md)) → choose “Did you really order such an ugly porcelain figure? Oops, sorry I didn't mean to offend you.” — **conditions:** hand over 1× [Pretty porcelain figure](../items/brv_wh_item_07.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40) → **stage 30**; also clears stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40), gives 30× [Gold coins](../items/gold.md). NPC: “Yes, indeed. A gift for my beautiful daughter... but why did it take so long? Sigh, here's my delivery fee.”

???+ note "Stage 40: 1 route"

    1. Talk to [Venanra](../monsters/brv_laundry_boss.md) ([brimhaven2_laundry](../maps/brimhaven2_laundry.md)) → choose “Did you order an 'Old, worn cape'?” — **conditions:** hand over 1× [Old, worn cape](../items/brv_wh_item_06.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50) → **stage 40**; also clears stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50), gives 10× [Gold coins](../items/gold.md). NPC: “Yes I did, kid. Incredibly, it has become the latest fashion to buy new capes with holes. Here's my delivery fee.”

???+ note "Stage 50: 1 route"

    1. Talk to [Tjure](../monsters/tjure.md) ([blackwater_mountain54](../maps/blackwater_mountain54.md)) → choose “Indeed. By the way, did you order a 'Mysterious green something'?” — **conditions:** reached stage 200 of [The silver scale](../quests/mermaid_scale.md#stage-200); hand over 1× [Mysterious green something](../items/brv_wh_item_05.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60) → **stage 50**; also clears stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60), gives 50× [Gold coins](../items/gold.md). NPC: “What?! My lucky clover...but why now? Anyway, I'll no longer run out of luck. Here's my delivery fee.”

???+ note "Stage 60: 1 route"

    1. Talk to [Servant](../monsters/guynmart_servant.md) ([guynmart_main_3](../maps/guynmart_main_3.md)) → choose “I'm here to give you your ordered item. You don't want it?” — **conditions:** hand over 1× [Chandelier](../items/brv_wh_item_04.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70) → **stage 60**; also clears stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70), gives 40× [Gold coins](../items/gold.md). NPC: “Finally, I'm no longer afraid of that room every time my lord turns off the lights to scare me. Here's my delivery fee.”

???+ note "Stage 70: 1 route"

    1. Talk to [Arghes](../monsters/arghes.md) ([remgard_tavern0](../maps/remgard_tavern0.md)) → choose “And how interesting that you ordered a pair of 'Yellow boots'. Did you really order this?” — **conditions:** reached stage 51 of [andor (hidden flag)](../quests/andor.md#stage-51); hand over 1× [Yellow boot](../items/brv_wh_item_03.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80) → **stage 70**; also clears stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80), gives 50× [Gold coins](../items/gold.md). NPC: “Yes kid, thank you. Here, take this gold for them.”

???+ note "Stage 80: 1 route"

    1. Talk to [Wrye](../monsters/wrye.md) ([vilegard_wrye](../maps/vilegard_wrye.md)) → choose “Yes, I came back to deliver your order of a 'Lyre'. You must be good at playing it?” — **conditions:** reached stage 90 of [Uncertain cause](../quests/wrye.md#stage-90); hand over 1× [Lyre](../items/brv_wh_item_02.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90) → **stage 80**; also clears stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90). NPC: “Yes, I'm longing for it just like how I'm longing for my son. But now I can mourn as I play his favorite song until I…”

???+ note "Stage 90: 1 route"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Yes, I'm here to deliver the order for a 'Plush Pillow'. But what for?” — **conditions:** reached stage 10 of [mikhail_bread (hidden flag)](../quests/mikhail_bread.md#stage-10); hand over 1× [Plush pillow](../items/brv_wh_item_01.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100) → **stage 90**; also clears stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100). NPC: “Oh wow! Finally, your brother's gift has arrived and we only have to wait for his arrival.”

???+ note "Stage 100: 1 route"

    1. Talk to [Pangitain](../monsters/brv_fortune_teller.md) ([brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md)) → choose “So you are the one who ordered a 'Crystal Globe'?” — **conditions:** hand over 1× [Crystal globe](../items/brv_wh_item_00.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110) → **stage 100**; also clears stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110), gives 100× [Gold coins](../items/gold.md). NPC: “Ah yes, I need a new one. My current crystal globe has become a bit cloudy - otherwise I would of course have seen…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_delivery_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_delivery_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_delivery_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_delivery_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_wh_delivery_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_wh_delivery_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 |
    | Dialogue nodes setting stages | 10: `brv_wh_delivery_arcir`, 20: `brv_wh_delivery_edrin`, 30: `brv_wh_delivery_odirath`, 40: `brv_wh_delivery_venanra`, 50: `brv_wh_delivery_tjure`, 60: `brv_wh_delivery_servant`, 70: `brv_wh_delivery_arghes`, 80: `brv_wh_delivery_wyre`, 90: `brv_wh_delivery_mikhail`, 100: `brv_wh_delivery_brv_fortune` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
