# Feygard errands

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_shipment` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 80, 82) |
| **Started by** | [Gandoren](../monsters/gandoren.md) |
| **NPCs involved** | [Ailshara](../monsters/ailshara.md), [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Gandoren](../monsters/gandoren.md), [Vilegard smith](../monsters/vilegard_smith.md) |
| **Locations** | [foaming_flask](../maps/foaming_flask.md), [houseatcrossroads0](../maps/houseatcrossroads0.md), [vilegard_smith](../maps/vilegard_smith.md) |
| **Total XP** | 1,000 |
| **Related quests** | 5 |

</div>

## Overview

> I met Gandoren, the guard captain at the Crossroads guardhouse. He told me about some trouble up in Loneford, that have forced the guards to be even more alert than usual. Because of this, they can't do their regular errands themselves but need help with some basic things.

## Prerequisites to start

Start with [Gandoren](../monsters/gandoren.md). Required:

- reached stage 10 of [Feygard errands](../quests/feygard_shipment.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Darkness in the Daylight](darkness_in_daylight.md#stage-20) | stage 20 there needs stage 82 here |
| Unlocks | [Flows through the veins](loneford.md#stage-10) | stage 10 there needs stage 25 here |
| Unlocks | [Flows through the veins](loneford.md#stage-11) | stage 11 there needs stage 25 here |
| Unlocks | [Flows through the veins](loneford.md#stage-21) | stage 21 there needs stage 25 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-18) | stage 18 there needs stage 81 here |
| Unlocks | [A creeping fear](xulviir.md#stage-20) | stage 20 there needs stage 56 here |
| Unlocks | [A creeping fear](xulviir.md#stage-30) | stage 30 there needs stage 56 here |
| Blocks | [Shadows](shadows.md#stage-10) | reaching stage 82 here closes stage 10 there |
| Blocks | [Shadows](shadows.md#stage-20) | reaching stage 82 here closes stage 20 there |
| Blocks | [Shadows](shadows.md#stage-30) | reaching stage 82 here closes stage 30 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met Gandoren, the guard captain at the Crossroads guardhouse. He told me about some trouble up in Loneford, that have forced the guards to be even more alert than usual. Because of this, they can't do their regular errands themselves but need help with some basic things. | [Gandoren](../monsters/gandoren.md) | – | – |
| <span id="stage-20"></span>20 | Gandoren wants me to help him transport a shipment of 10 iron swords to another guard post to the south. | [Gandoren](../monsters/gandoren.md) | – | – |
| <span id="stage-21"></span>21 | I have agreed to help Gandoren transport the shipment, as a service for Feygard. | [Gandoren](../monsters/gandoren.md) | stage 20 | – |
| <span id="stage-22"></span>22 | I have grudgingly agreed to help Gandoren transport the shipment. | [Gandoren](../monsters/gandoren.md) | stage 20 | – |
| <span id="stage-25"></span>25 | I should deliver the shipment to the Feygard patrol captain stationed in the Foaming Flask tavern. | [Gandoren](../monsters/gandoren.md) | stage 22 | gives [Feygard iron sword](../items/fg_ironsword.md) |
| <span id="stage-26"></span>26 | Gandoren tells me that Ailshara has expressed some interest in the Feygard shipments, and urges me to stay away from her. | [Gandoren](../monsters/gandoren.md) | stage 25 | – |
| <span id="stage-30"></span>30 | Ailshara is indeed interested in the shipment, and wants me to help Nor City with the supplies instead. | [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) | stage 35 | – |
| <span id="stage-35"></span>35 | If I want to help Ailshara and Nor City, I should deliver the shipment to the smith in Vilegard instead. | [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) | – | – |
| <span id="stage-50"></span>50 | I have delivered the shipment to the Feygard patrol captain in the Foaming Flask tavern. I should go tell Gandoren in the Crossroads guardhouse that the shipment is delivered. | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | hand over 10× [Feygard iron sword](../items/fg_ironsword.md), stage 25 | – |
| <span id="stage-55"></span>55 | I have delivered the shipment to the smith in Vilegard. | [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) | hand over 10× [Feygard iron sword](../items/fg_ironsword.md), stage 35, stage 56 | – |
| <span id="stage-56"></span>56 | The Vilegard smith gave me a shipment of degraded items that I should deliver to the Feygard patrol captain in the Foaming Flask tavern instead of the normal ones. | [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) | stage 55 | gives [Degraded Feygard iron sword](../items/fg_ironsword_d.md) |
| <span id="stage-60"></span>60 | I have delivered the shipment of degraded items to the Feygard patrol captain in the Foaming Flask tavern. I should go tell Gandoren in the Crossroads guardhouse that the shipment is delivered. | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | hand over 10× [Degraded Feygard iron sword](../items/fg_ironsword_d.md), stage 56 | – |
| <span id="stage-80"></span>80 | Gandoren thanked me for helping him deliver the shipment. **(completes quest)** | [Gandoren](../monsters/gandoren.md) | stage 25, stage 50 | 500 XP |
| <span id="stage-81"></span>81 | Gandoren thanked me for helping him deliver the shipment. He never suspected anything. I should also report back to Ailshara. | [Gandoren](../monsters/gandoren.md) | stage 25, stage 60 | – |
| <span id="stage-82"></span>82 | I have reported back to Ailshara. **(completes quest)** | [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) | stage 35, stage 55, stage 81 | 500 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “Can you tell me again what you told me before about recent events?” — **conditions:** reached stage 10 of [Feygard errands](../quests/feygard_shipment.md#stage-10) → **stage 10**. NPC: “This also means that we cannot focus as much on our usual tasks as we normally do, but instead need help with doing…”

???+ note "Stage 20: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “What is the task?” — **conditions:** reached stage 20 of [Feygard errands](../quests/feygard_shipment.md#stage-20) → **stage 20**. NPC: “Take this shipment of 10 iron swords to the guard captain stationed in a tavern called 'The Foaming Flask', near a…”

???+ note "Stage 21: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “No problem. Anything for the glory of Feygard.” — **conditions:** reached stage 20 of [Feygard errands](../quests/feygard_shipment.md#stage-20) → **stage 21**. NPC: “Excellent.”

???+ note "Stage 22: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “Fine, whatever. I will carry your stupid swords. I still hope there will be some reward for this.” — **conditions:** reached stage 20 of [Feygard errands](../quests/feygard_shipment.md#stage-20) → **stage 22**. NPC: “OK then.”

???+ note "Stage 25: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → the conversation leads here automatically — **conditions:** reached stage 22 of [Feygard errands](../quests/feygard_shipment.md#stage-22) → **stage 25**; also gives [Feygard iron sword](../items/fg_ironsword.md). NPC: “Here is the shipment that I want you to transport.”

???+ note "Stage 26: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “I am still working on transporting that shipment.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25) → **stage 26**. NPC: “I would urge you to stay away from her at all costs. Whatever you do, do not speak to her about your mission with the…”

???+ note "Stage 30: 1 route"

    1. Talk to [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) → choose “Can you tell me again what I was supposed to do?” — **conditions:** reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35) → **stage 30**. NPC: “Any help we can bring to Nor City in this matter is welcome. These items that Gandoren gave you would be useful to our…”

???+ note "Stage 35: 1 route"

    1. Talk to [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) → choose “Can you tell me again what I was supposed to do?” — **conditions:** reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35) → **stage 35**. NPC: “If you indeed are walking in the Shadow, then deliver these items to the smith in Vilegard. He will be able to make…”

???+ note "Stage 50: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “I have a shipment of iron swords from Gandoren for you.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); hand over 10× [Feygard iron sword](../items/fg_ironsword.md) → **stage 50**

???+ note "Stage 55: 1 route"

    1. Talk to [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) → choose “I have a shipment of Feygard items for you.” — **conditions:** reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56); reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35); hand over 10× [Feygard iron sword](../items/fg_ironsword.md) → **stage 55**. NPC: “Oh, this is most unexpected but very welcome. I will not question how you acquired these items, but instead express my…”

???+ note "Stage 56: 1 route"

    1. Talk to [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) → choose “I was sent to deliver these items to a Feygard patrol stationed in the Foaming Flask tavern.” — **conditions:** reached stage 55 of [Feygard errands](../quests/feygard_shipment.md#stage-55) → **stage 56**; also gives [Degraded Feygard iron sword](../items/fg_ironsword_d.md). NPC: “Take these items and deliver them to wherever you were supposed to deliver the items you gave me.”

???+ note "Stage 60: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “I have a shipment of iron swords from Gandoren for you.” — **conditions:** reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56); hand over 10× [Degraded Feygard iron sword](../items/fg_ironsword_d.md) → **stage 60**

???+ note "Stage 80: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “Yes. I have delivered them as you ordered.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); reached stage 50 of [Feygard errands](../quests/feygard_shipment.md#stage-50) → **stage 80**. NPC: “Splendid! Feygard is in debt to you.”

???+ note "Stage 81: 1 route"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “Yes. I have delivered them.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); reached stage 60 of [Feygard errands](../quests/feygard_shipment.md#stage-60) → **stage 81**. NPC: “Splendid! Feygard is in debt to you.”

???+ note "Stage 82: 1 route"

    1. Talk to [Ailshara](../monsters/ailshara.md) ([houseatcrossroads0](../maps/houseatcrossroads0.md)) → choose “Yes, it is done.” — **conditions:** reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35); reached stage 55 of [Feygard errands](../quests/feygard_shipment.md#stage-55); reached stage 81 of [Feygard errands](../quests/feygard_shipment.md#stage-81) → **stage 82**. NPC: “Excellent! You do indeed walk with the Shadow my friend. I am glad to hear that there are at least a few decent folk…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Ok then.” → “OK then.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_shipment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_shipment` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 22, 25, 26, 30, 35, 50, 55, 56, 60, 80, 81, 82 |
    | Dialogue nodes setting stages | 10: `gandoren_5`, 20: `gandoren_13`, 21: `gandoren_17`, 22: `gandoren_19`, 25: `gandoren_20`, 26: `gandoren_24`, 30: `ailshara_interested_5`, 35: `ailshara_interested_8`, 50: `ff_captain_fg_items_1`, 55: `vilegard_smith_fg_1`, 56: `vilegard_smith_fg_7`, 60: `ff_captain_vg_items_1`, 80: `gandoren_deliver_y_1`, 81: `gandoren_deliver_n_1`, 82: `ailshara_deliver_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
