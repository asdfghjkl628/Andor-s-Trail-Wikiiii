# The thorns of vengeance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `thorns_vengeance` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 32, 76, 90) |
| **Started by** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) |
| **NPCs involved** | [Aryfora](../monsters/stoutford_widow.md), [Blornvale](../monsters/stoutford_alchemist.md), [Blornvale](../monsters/stoutford_alchemist2.md), [Tahalendor](../monsters/tahalendor.md), [Tahalendor](../monsters/tahalendor2.md) |
| **Locations** | [stoutford_church](../maps/stoutford_church.md), [stoutford_gate](../maps/stoutford_gate.md), [stoutford_potion](../maps/stoutford_potion.md) |
| **Total XP** | 6,005 |
| **Related quests** | 3 |

</div>

## Overview

> Aryfora in Stoutford needs my help to prove her uncle, Blornvale, Stoutford's alchemist, killed her father.

## Prerequisites to start

Start with [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)). Required:

- reached stage 45 of [The roots of love](../quests/roots_love.md#stage-45)
- used 1× [Potion of deftness](../items/potion_deftness.md)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The roots of love](roots_love.md#stage-45) | stage 45 reached, for stage 10 here |
| Requires | [Rumblings](rumblings.md#stage-106) | stage 106 reached, for stage 65 here |
| Unlocks | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-202) | stage 202 there needs stage 20 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Aryfora in Stoutford needs my help to prove her uncle, Blornvale, Stoutford's alchemist, killed her father. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | – | – |
| <span id="stage-20"></span>20 | She needs me to purchase three potions of the brave from Blornvale and return to her. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 10 | spawns monsters on stoutford_sw |
| <span id="stage-30"></span>30 | I have returned with the three potions, and gave them to her. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | hand over 3× [Potion of the brave](../items/potion_brave.md), stage 20 | – |
| <span id="stage-32"></span>32 | I decided not to help Aryfora any further. **(completes quest)** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | carry 3× [Potion of the brave](../items/potion_brave.md), stage 20 | 500 XP |
| <span id="stage-40"></span>40 | She gave me a potion of truth. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 30 | gives 1× [Potion of truth](../items/potion_truth.md) |
| <span id="stage-50"></span>50 | She wants me to give that potion to Blornvale, and make him confess his crimes. I should have Tahalendor as a witness. | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | I agreed to make Blornvale drink that potion. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-65"></span>65 | Tahalendor agreed to go with me to the alchemist's house to hear Blornvale's confession. | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 50 | – |
| <span id="stage-70"></span>70 | Blornvale drank the potion. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) | carry 1× [Potion of truth](../items/potion_truth.md), hand over 1× [Potion of truth](../items/potion_truth.md) | 1,500 XP |
| <span id="stage-71"></span>71 | Tahalendor came to hear Blornvale's confession. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) | – | spawns monsters on stoutford_potion |
| <span id="stage-72"></span>72 | Blornvale confessed to killing Aryfora's father. Unfortunately there is no witness. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) | stage 70 | – |
| <span id="stage-74"></span>74 | Blornvale now understands what I was trying to do. I will no longer be able to help Aryfora get back her shop. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) | carry 1× [Potion of truth](../items/potion_truth.md), stage 72 | – |
| <span id="stage-75"></span>75 | Tahalendor wouldn't believe my story. I will no longer be able to help Aryfora get back her shop. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md))<br>[Tahalendor](../monsters/tahalendor2.md) ([stoutford_potion](../maps/stoutford_potion.md)) | stage 72 | – |
| <span id="stage-76"></span>76 | It's all my fault that Aryfora is crying now. **(completes quest)** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | – | 5 XP |
| <span id="stage-80"></span>80 | Blornvale confessed to killing Aryfora's father in the presence of Tahalendor. | [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md))<br>[Tahalendor](../monsters/tahalendor2.md) ([stoutford_potion](../maps/stoutford_potion.md)) | stage 71 | removes monsters from stoutford_potion |
| <span id="stage-90"></span>90 | Aryfora regained her father's shop. **(completes quest)** | [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) | stage 80 | 4,000 XP<br>removes monsters from stoutford_gate<br>spawns monsters on stoutford_potion |

<span id="untraced"></span>*No trigger*: nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “I can do it!” — **conditions:** reached stage 45 of [The roots of love](../quests/roots_love.md#stage-45); used 1× [Potion of deftness](../items/potion_deftness.md) → **stage 10**. NPC: “Then it's settled.”

???+ note "Stage 20: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “What will you do with them?” — **conditions:** reached stage 10 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-10) → **stage 20**; also spawns monsters on stoutford_sw. NPC: “That is why you must get the potions of the brave from Blornvale. Oh how I hate that name! Be quick.”

???+ note "Stage 30: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “Yes, here they are.” — **conditions:** reached stage 20 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-20); hand over 3× [Potion of the brave](../items/potion_brave.md) → **stage 30**. NPC: “Great! This will finally break him.”

???+ note "Stage 32: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “I don't quit think so. He is an honest person.” — **conditions:** reached stage 20 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-20); carry 3× [Potion of the brave](../items/potion_brave.md) → **stage 32**. NPC: “I would not have expected that from you!”

???+ note "Stage 40: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-30) → **stage 40**; also gives 1× [Potion of truth](../items/potion_truth.md). NPC: “Now I take three potions of the brave *chanting* ... add my prepared ingredients *chanting* ... shake it *chanting*…”

???+ note "Stage 50: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “But who would believe me, a stranger?” — **conditions:** reached stage 40 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-40) → **stage 50**. NPC: “Best would be Tahalendor himself. Yes, you must persuade the priest to be present when Blornvale tells the whole story.”

???+ note "Stage 65: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Would you come with me to talk to Blornvale? He wants to confess something important.” — **conditions:** reached stage 106 of [Rumblings](../quests/rumblings.md#stage-106); reached stage 50 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-50); NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65); NOT reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74) → **stage 65**. NPC: “If I must. Well, go ahead, I'll be there when you get there.”

???+ note "Stage 70: 1 route"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → choose “Yes, here. I still have one bottle of your potion of the brave.” — **conditions:** carry 1× [Potion of truth](../items/potion_truth.md); NOT reached stage 200 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-200); hand over 1× [Potion of truth](../items/potion_truth.md) → **stage 70**. NPC: “Do you see me drinking? Yes? Anything wrong? No - this potion is just perfect!”

???+ note "Stage 71: 1 route"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically — **conditions:** reached stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71) → **stage 71**; also spawns monsters on stoutford_potion

???+ note "Stage 72: 1 route"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → choose “How did you kill Aryfora's father, your own brother?” — **conditions:** reached stage 70 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-70); NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65) → **stage 72**. NPC: “He was naive enough to take a potion from me. I poisoned him with the potion of Quick Death.”

???+ note "Stage 74: 2 routes"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → choose “No, I poured all the rest away.” — **conditions:** carry 1× [Potion of truth](../items/potion_truth.md); NOT reached stage 200 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-200) → **stage 74**. NPC: “Then you can never prove it. That's good. Out now, leave my shop, you scum!”
    2. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically — **conditions:** reached stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72) → **stage 74**. NPC: “That was - a potion of truth! How dare you! Did you think I wouldn't recognize it?”

???+ note "Stage 75: 2 routes"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically — **conditions:** reached stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75) → **stage 75**. NPC: “And you child, go away now and tell no more fairy tales.”
    2. Talk to [Tahalendor](../monsters/tahalendor2.md) ([stoutford_potion](../maps/stoutford_potion.md)) → choose “He lies. Can't you see?” — **conditions:** reached stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72) → **stage 75**. NPC: “And you child, go away now and tell no more fairy tales.”

???+ note "Stage 76: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → the conversation leads here automatically — **conditions:** reached stage 76 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-76) → **stage 76**. NPC: “Oh no! Now I will never get justice!”

???+ note "Stage 80: 2 routes"

    1. Talk to [Blornvale](../monsters/stoutford_alchemist.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically — **conditions:** reached stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71) → **stage 80**; also removes monsters from stoutford_potion, removes monsters from stoutford_potion. NPC: “I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.”
    2. Talk to [Tahalendor](../monsters/tahalendor2.md) ([stoutford_potion](../maps/stoutford_potion.md)) → the conversation leads here automatically — **conditions:** reached stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71) → **stage 80**; also removes monsters from stoutford_potion, removes monsters from stoutford_potion. NPC: “I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.”

???+ note "Stage 90: 1 route"

    1. Talk to [Aryfora](../monsters/stoutford_widow.md) ([stoutford_gate](../maps/stoutford_gate.md)) → choose “Oh, that was just a trifle.” — **conditions:** reached stage 80 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-80) → **stage 90**; also removes monsters from stoutford_gate, spawns monsters on stoutford_potion. NPC: “Now I can move back into my father's house and create potions again. I will leave at once. Please come and visit me at…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thorns_vengeance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `thorns_vengeance` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 32, 40, 50, 60, 65, 70, 71, 72, 74, 75, 76, 80, 90 |
    | Dialogue nodes setting stages | 10: `stoutford_widow_roots4045_20`, 20: `stoutford_widow_thorns10_2`, 30: `stoutford_widow_thorns20_1`, 32: `stoutford_widow_thorns20_4`, 40: `stoutford_widow_thorns30_0`, 50: `stoutford_widow_thorns40_2`, 65: `tahalendor_thorns50`, 70: `blornvale_thorns50_30`, 71: `blornvale_thorns70_20`, 72: `blornvale_thorns70_12`, 74: `blornvale_thorns50_22`, 74: `blornvale_thorns72_10`, 75: `blornvale_thorns72_90`, 76: `stoutford_widow_thorns74_1`, 80: `blornvale_thorns70_30`, 90: `stoutford_widow_thorns80_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
