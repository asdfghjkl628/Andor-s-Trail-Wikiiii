# A place to forge

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `place_to_forge` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 60) |
| **Started by** | [Nocmar](../monsters/nocmar.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Dealer](../monsters/brv_blackjack_dealer.md), [Mustura](../monsters/brv_guard_captain.md), [Nocmar](../monsters/nocmar.md) |
| **Locations** | [brimhaven4](../maps/brimhaven4.md), [brimhaven_house1](../maps/brimhaven_house1.md), [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) |
| **Total XP** | 8,975 |
| **Related quests** | 5 |

</div>

## Overview

> Nocmar refused to forge heartsteel in his shop, fearing discovery by Geomyr's men. He revealed that he once owned a glowing white house south of Fallhaven, where a special forge still burns. That forge was the only place he ever worked heartsteel. But after falling into debt, he lost the house to Alkapoan. If Nocmar is to forge again, I must help him regain it.

## Prerequisites to start

Start with [Nocmar](../monsters/nocmar.md). Required:

- NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90)
- reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10)
- NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60)
- reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Much water](brv_flood.md#stage-130) | stage 130 reached, for stage 20 here |
| Requires | [Much water](brv_flood.md#stage-200) | stage 200 reached, for stages 30, 35, 40, 50 here |
| Requires | [Lost treasures](nocmar.md#stage-10) | stage 10 reached, for stages 10, 20, 60 here |
| Requires | [Lost treasures](nocmar.md#stage-80) | stage 80 reached, for stages 10, 20, 60 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-15) | stage 15 reached, for stages 30, 35, 40, 50 here |
| Blocked by | [Fair play?](brv_blackjack.md#stage-50) | stage 50 must NOT be reached, for stage 45 here |
| Blocked by | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-100) | stage 100 must NOT be reached, for stage 45 here |
| Mutually exclusive | [Lost treasures](nocmar.md#stage-90) | stage 90 must NOT be reached, for stages 10, 20, 60 here |
| Unlocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 there needs stage 40 here |
| Unlocks | [Lost treasures](nocmar.md#stage-90) | stage 90 there needs stage 60 here |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-10) | reaching stage 60 here closes stage 10 there |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-15) | reaching stage 50 here closes stage 15 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Nocmar refused to forge heartsteel in his shop, fearing discovery by Geomyr's men. He revealed that he once owned a glowing white house south of Fallhaven, where a special forge still burns. That forge was the only place he ever worked heartsteel. But after falling into debt, he lost the house to Alkapoan. If Nocmar is to forge again, I must help him regain it. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-20"></span>20 | Nocmar told me that Alkapoan holds the deed and key to the glowing white house. He said the forge within never dies, always blazing, ready for work. If I can reclaim the deed and key from Alkapoan, Nocmar will finally have his forge back. | [Nocmar](../monsters/nocmar.md) | – | – |
| <span id="stage-30"></span>30 | Alkapoan scoffed when I mentioned Nocmar. He said the only way to reclaim the glowing white house is to pay him fifty thousand gold. Nothing else will satisfy him. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | – | – |
| <span id="stage-35"></span>35 | I told Alkapoan I wanted the glowing white house for myself. He agreed to sell it for forty thousand gold, but only if I first complete a task for him to prove my worth. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | – | – |
| <span id="stage-40"></span>40 | Alkapoan asked me to collect an overdue 'operation tax' of five thousand gold from a card dealer in the back room of Brimhaven's tavern. I'll need to go there and retrieve the gold for Alkapoan before he will sell me the deed to the white house for forty thousand. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | – | – |
| <span id="stage-45"></span>45 | I was able to collect the overdue 'operation tax' from the dealer and now I should return to Alkapoan. | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | stage 40 | gives 5000× [Gold coins](../items/gold.md)<br>gives 6000× [Gold coins](../items/gold.md) |
| <span id="stage-50"></span>50 | After I paid Alkapoan, he gave me the deed and the key to the white house south of Fallhaven. I should bring them back to Nocmar. | [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md))<br>[Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) | pay 45,000 gold, stage 45 | gives 1× [White house deed](../items/white_house_deed.md)<br>gives 1× [White house key](../items/white_house_key.md) |
| <span id="stage-60"></span>60 | I was able to finally give Nocmar back what was rightfully his...possession of his forge house. **(completes quest)** | [Nocmar](../monsters/nocmar.md) | hand over 1× [White house deed](../items/white_house_deed.md), hand over 1× [White house key](../items/white_house_key.md), stage 50 | 8,975 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Unnmir sent me.” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80) → **stage 10**. NPC: “There was a time, before all this, when I had a place. A house. Not just any house...a white house on the edge of…”

???+ note "Stage 20: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “That's a lot to lose, indeed.” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); reached stage 130 of [Much water](../quests/brv_flood.md#stage-130) → **stage 20**. NPC: “If I am to work again, I must have that house returned to me. Speak to Alkapoan. Persuade him, pay him, bargain with…”

???+ note "Stage 30: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Nocmar has sent me to get back what was once his.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 35 of [A place to forge](../quests/place_to_forge.md#stage-35) → **stage 30**. NPC: “Ah...so this is for Nocmar? The man who couldn't pay his debt and lost everything. And now you want me to just hand it…”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “Nocmar has sent me to get back what was once his.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 35 of [A place to forge](../quests/place_to_forge.md#stage-35) → **stage 30**. NPC: “Ah...so this is for Nocmar? The man who couldn't pay his debt and lost everything. And now you want me to just hand it…”

???+ note "Stage 35: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “[lie] I want the glowing white house. I need a place to hide from my parents.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 35**. NPC: “You want the house for yourself? Now that is interesting. Most people shy away from that cursed glow, but I can see…”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “[lie] I want the glowing white house. I need a place to hide from my parents.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 35**. NPC: “You want the house for yourself? Now that is interesting. Most people shy away from that cursed glow, but I can see…”

???+ note "Stage 40: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Okay?” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 40**. NPC: “He's late. Bring me what he owes, and don't let him wiggle out of it. I want every bit of the five thousand gold. When…”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “Okay?” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); NOT reached stage 30 of [A place to forge](../quests/place_to_forge.md#stage-30); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 40**. NPC: “He's late. Bring me what he owes, and don't let him wiggle out of it. I want every bit of the five thousand gold. When…”

???+ note "Stage 45: 4 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “Yes. He sent me to collect the operation tax.” — **conditions:** NOT reached stage 100 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100); reached stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 45**; also gives 5000× [Gold coins](../items/gold.md). NPC: “[Grumbles] Always the same story. Alkapoan's cut, never mine. Fine, here. Take your five thousand gold and tell him…”
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “Yes. He sent me to collect the operation tax.” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); NOT reached stage 100 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100); reached stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 45**; also gives 5000× [Gold coins](../items/gold.md). NPC: “[Grumbles] Always the same story. Alkapoan's cut, never mine. Fine, here. Take your five thousand gold and tell him…”
    3. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “[lie]Six thousand. Collector's fees, you understand.” — **conditions:** NOT reached stage 100 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100); reached stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 45**; also gives 6000× [Gold coins](../items/gold.md). NPC: “Slams the table, six?! That greedy vulture...fine, here. Just get out before I change my mind.”
    4. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “[lie]Six thousand. Collector's fees, you understand.” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); NOT reached stage 100 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100); reached stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45) → **stage 45**; also gives 6000× [Gold coins](../items/gold.md). NPC: “Slams the table, six?! That greedy vulture...fine, here. Just get out before I change my mind.”

???+ note "Stage 50: 2 routes"

    1. Talk to [Mustura](../monsters/brv_guard_captain.md) ([brimhaven4](../maps/brimhaven4.md)) → choose “Here, take the fourty-five thousand and give me the deed and the key.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); latest stage of [A place to forge](../quests/place_to_forge.md#stage-45) is 45; pay 45,000 gold → **stage 50**; also gives 1× [White house deed](../items/white_house_deed.md), gives 1× [White house key](../items/white_house_key.md). NPC: “A pleasure doing business with you.”
    2. Talk to [Alkapoan](../monsters/brv_richman.md) ([brimhaven_house1](../maps/brimhaven_house1.md)) → choose “Here, take the fourty-five thousand and give me the deed and the key.” — **conditions:** reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-15); NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50); latest stage of [A place to forge](../quests/place_to_forge.md#stage-45) is 45; pay 45,000 gold → **stage 50**; also gives 1× [White house deed](../items/white_house_deed.md), gives 1× [White house key](../items/white_house_key.md). NPC: “A pleasure doing business with you.”

???+ note "Stage 60: 1 route"

    1. Talk to [Nocmar](../monsters/nocmar.md) → choose “Well, that time has come back! I have the deed and the key to your forge house. [hand them to Nocmar]” — **conditions:** NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80); latest stage of [A place to forge](../quests/place_to_forge.md#stage-50) is 50; hand over 1× [White house deed](../items/white_house_deed.md); hand over 1× [White house key](../items/white_house_key.md) → **stage 60**. NPC: “Ah, all these years and at last I have a chance to see it again.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 8 lines added, 1 line changed<br>· text: “Can you feel it? The heartsteel is glowing again.” → “There was a time, before all this, when I had a place. A house. Not j…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `place_to_forge` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 45, 50, 60 |
    | Dialogue nodes setting stages | 10: `nocmar_complete_5`, 20: `nocmar_white_house_20`, 30: `alkapoan_nocmar_wh_10`, 35: `alkapoan_lie_wh_10`, 40: `alkapoan_lie_wh_40`, 45: `blackjack_dealer_collect_tax_20`, 45: `blackjack_dealer_collect_tax_30`, 50: `alkapoan_nocmar_wh_give_deed`, 60: `nocmar_wh_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
