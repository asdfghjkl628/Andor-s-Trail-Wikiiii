# Recovering stolen property

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `sullengard_recover_items` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 70) |
| **Started by** | [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) |
| **NPCs involved** | [Gaelian](../monsters/sullengard_gaelian.md), [Lost traveler](../monsters/sullengard_inn_traveler.md), [Prowling Arantxa](../monsters/sullengard_arantxa.md), [Zaccheria](../monsters/sullengard_zaccheria.md) |
| **Locations** | [sullengard2_armory](../maps/sullengard2_armory.md), [sullengard_inn](../maps/sullengard_inn.md), [sullengard_tavern_basement](../maps/sullengard_tavern_basement.md) |
| **Total XP** | 3,800 |
| **Related quests** | 1 |

</div>

## Overview

> I've agreed to help the armour shop owner, Zaccheria investigate the theft of his shop's entire inventory.

## Prerequisites to start

Start with [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)). Required:

- NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60
- NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70) is 70


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-23) | stage 23 reached, for stage 40 here |
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-24) | stage 24 reached, for stage 40 here |
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-25) | stage 25 reached, for stage 40 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-23) | stage 23 there needs stage 30 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-24) | stage 24 there needs stage 30 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-25) | stage 25 there needs stage 30 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-39) | stage 39 there needs stage 70 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-42) | stage 42 there needs stage 70 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I've agreed to help the armour shop owner, Zaccheria investigate the theft of his shop's entire inventory. | [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) | – | – |
| <span id="stage-20"></span>20 | Zaccheria suggested that I should start my investigation by speaking with Gaelian from the Briwerra family. | [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) | – | – |
| <span id="stage-30"></span>30 | I spoke with Gaelian from the Briwerra family and I suspect that he had nothing to do with this crime. | [Gaelian](../monsters/sullengard_gaelian.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I spoke with Prowling Arantxa, a thief in the Sullengard tavern basement and she informed me that the 'lost traveler' recently tried to sell her some items that she recgonized as belonging to Zaccheria. I should speak with the 'lost traveler'. | [Prowling Arantxa](../monsters/sullengard_arantxa.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | I had paid the 'lost traveler' in exchange for the location of Zaccheria's stolen items. He told me that he had hidden them on the eastern boundaries of town. | [Lost traveler](../monsters/sullengard_inn_traveler.md) ([sullengard_inn](../maps/sullengard_inn.md)) | pay 10,000 gold, stage 40 | removes monsters from sullengard_inn |
| <span id="stage-60"></span>60 | I found the stolen items and should return to Zaccheria with them.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Sullengard woods9](../maps/sullengard_woods9.md).</span> | stepping on a trigger on [sullengard_woods9](../maps/sullengard_woods9.md) | stage 50 | gives 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md) |
| <span id="stage-70"></span>70 | Zaccheria was very happy that I was able to return his items to him. He paid me a very nice reward in gold. **(completes quest)** | [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) | carry 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md), hand over 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md), stage 60 | 3,800 XP<br>gives 15000× [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) → choose “I'll take it, but can you give me some more details?” — **conditions:** NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60; NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70) is 70 → **stage 10**. NPC: “Sure. You see, I was at the tavern last night enjoying a couple "Southernhaze" beers like I almost always do after…”

???+ note "Stage 20: 1 route"

    1. Talk to [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) → choose “Why is that?” — **conditions:** NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60; NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70) is 70 → **stage 20**. NPC: “Anyways, I think you should start there, but I suspect others too.”

???+ note "Stage 30: 1 route"

    1. Talk to [Gaelian](../monsters/sullengard_gaelian.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) → choose “I was told that maybe you know some information about these crimes.” — **conditions:** latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-20) is 20; NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30 → **stage 30**. NPC: “I know nothing except that Zaccheria deserved it.”

???+ note "Stage 40: 1 route"

    1. Talk to [Prowling Arantxa](../monsters/sullengard_arantxa.md) ([sullengard_tavern_basement](../maps/sullengard_tavern_basement.md)) → choose “Well, let's be honest. You are a thief after all.” — **conditions:** latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30; reached stage 23 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-23); reached stage 24 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-24); reached stage 25 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-25) → **stage 40**. NPC: “You see kid, here in Sullengard, we have a working agreement with the townspeople. They pay us for our services and we…”

???+ note "Stage 50: 1 route"

    1. Talk to [Lost traveler](../monsters/sullengard_inn_traveler.md) ([sullengard_inn](../maps/sullengard_inn.md)) → choose “Whatever. I can spare it.” — **conditions:** latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40) is 40; pay 10,000 gold → **stage 50**; also removes monsters from sullengard_inn. NPC: “Excellent. Nice doing 'business' with you. I hid them somewhere east of town. Close by, but I doubt you can find it…”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [sullengard_woods9](../maps/sullengard_woods9.md) → choose “Oh yeah! I've come this far already. There's no reason to stop.” — **conditions:** latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-50) is 50 → **stage 60**; also gives 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md). NPC: “You have successfully removed an extremely heavy sack. This must be Zaccheria stolen inventory.”

???+ note "Stage 70: 1 route"

    1. Talk to [Zaccheria](../monsters/sullengard_zaccheria.md) ([sullengard2_armory](../maps/sullengard2_armory.md)) → choose “I wish I knew. After he told me where to find your stuff, he took off and I was unable to see in what…” — **conditions:** latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60; carry 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md); hand over 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md) → **stage 70**; also gives 15000× [Gold coins](../items/gold.md). NPC: “Well that's unfortunate that we cannot punish this individual. But very fortunate that you worked hard to recover my…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed<br>· text: “[You have successfully removed an extreamly heavy sack. This must be …” → “[You have successfully removed an extremely heavy sack. This must be …” |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “[You have successfully removed an extremely heavy sack. This must be …” → “You have successfully removed an extremely heavy sack. This must be Z…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Well that's unfortunate that we cannot punish this individual. But ve…” → “Well that's unfortunate that we cannot punish this individual. But ve…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_recover_items.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_recover_items.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_recover_items.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_recover_items.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sullengard_recover_items.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `sullengard_recover_items` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 10: `sullengard_zaccheria_40`, 20: `sullengard_zaccheria_70`, 30: `sullengard_gaelian_40`, 40: `sullengard_arantxa_60`, 50: `sullengard_inn_traveler_130`, 60: `sullengard_hidden_inventory_20`, 70: `sullengard_zaccheria_100` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
