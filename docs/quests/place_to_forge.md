---
description: "A place to forge is a quest in Andor's Trail, started by Nocmar. 8 stages, 8,975 XP in total. Nocmar refused to forge heartsteel in his shop, fearing discovery by Geomyr's men. He revealed that he once owned a glowing white house south of Fallhaven, where a special forge still burns. That forge w…"
---

# A place to forge

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `place_to_forge` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 60) |
| **Started by** | [Nocmar](../monsters/nocmar.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Dealer](../monsters/brv_blackjack_dealer.md), [Mustura](../monsters/brv_guard_captain.md), [Nocmar](../monsters/nocmar.md) |
| **Locations** | [Brimhaven 4](../maps/brimhaven4.md), [Brimhaven house 1](../maps/brimhaven_house1.md), [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) |
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
| Requires | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-15) | stage 15 reached, for stages 30, 35, 40, 50 here |
| Blocked by | [Fair play?](brv_blackjack.md#stage-50) | stage 50 must NOT be reached, for stage 45 here |
| Blocked by | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-100) | stage 100 must NOT be reached, for stage 45 here |
| Mutually exclusive | [Lost treasures](nocmar.md#stage-90) | stage 90 must NOT be reached, for stages 10, 20, 60 here |
| Unlocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 there needs stage 40 here |
| Unlocks | [Lost treasures](nocmar.md#stage-90) | stage 90 there needs stage 60 here |
| Blocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-10) | reaching stage 60 here closes stage 10 there |
| Blocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-15) | reaching stage 50 here closes stage 15 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Nocmar refused to forge heartsteel in his shop, fearing discovery by… ▸</span><span class="l">▴ less</span></summary>Nocmar refused to forge heartsteel in his shop, fearing discovery by Geomyr's men. He revealed that he once owned a glowing white house south of Fallhaven, where a special forge still burns. That forge was the only place he ever worked heartsteel. But after falling into debt, he lost the house to Alkapoan. If Nocmar is to forge again, I must help him regain it.</details> | [Nocmar](../monsters/nocmar.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Nocmar told me that Alkapoan holds the deed and key to the glowing… ▸</span><span class="l">▴ less</span></summary>Nocmar told me that Alkapoan holds the deed and key to the glowing white house. He said the forge within never dies, always blazing, ready for work. If I can reclaim the deed and key from Alkapoan, Nocmar will finally have his forge back.</details> | [Nocmar](../monsters/nocmar.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Alkapoan scoffed when I mentioned Nocmar. He said the only way to… ▸</span><span class="l">▴ less</span></summary>Alkapoan scoffed when I mentioned Nocmar. He said the only way to reclaim the glowing white house is to pay him fifty thousand gold. Nothing else will satisfy him.</details> | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">I told Alkapoan I wanted the glowing white house for myself. He… ▸</span><span class="l">▴ less</span></summary>I told Alkapoan I wanted the glowing white house for myself. He agreed to sell it for forty thousand gold, but only if I first complete a task for him to prove my worth.</details> | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">Alkapoan asked me to collect an overdue 'operation tax' of five… ▸</span><span class="l">▴ less</span></summary>Alkapoan asked me to collect an overdue 'operation tax' of five thousand gold from a card dealer in the back room of Brimhaven's tavern. I'll need to go there and retrieve the gold for Alkapoan before he will sell me the deed to the white house for forty thousand.</details> | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-45"></span>[45](#route-45) | <details class="jt"><summary><span class="s">I was able to collect the overdue 'operation tax' from the dealer… ▸</span><span class="l">▴ less</span></summary>I was able to collect the overdue 'operation tax' from the dealer and now I should return to Alkapoan.</details> | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | varies by route (see below) |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">After I paid Alkapoan, he gave me the deed and the key to the white… ▸</span><span class="l">▴ less</span></summary>After I paid Alkapoan, he gave me the deed and the key to the white house south of Fallhaven. I should bring them back to Nocmar.</details> | [Mustura](../monsters/brv_guard_captain.md), [Alkapoan](../monsters/brv_richman.md) | 1× [White house deed](../items/white_house_deed.md), 1× [White house key](../items/white_house_key.md) |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I was able to finally give Nocmar back what was rightfully… ▸</span><span class="l">▴ less</span></summary>I was able to finally give Nocmar back what was rightfully his...possession of his forge house.</details> **(ends quest)** | [Nocmar](../monsters/nocmar.md) | 8,975 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Nocmar · 1 way"

    **Way 1:** Talk to [Nocmar](../monsters/nocmar.md), choose “Unnmir sent me.”

    - **Needs:** not yet stage 60; not reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80)
    - *“There was a time, before all this, when I had a place. A house. Not just any house...a white house on the edge of Fallhaven, glowing as if…”*


<span id="route-20"></span>

??? note "Stage 20 · Nocmar · 1 way"

    **Way 1:** Talk to [Nocmar](../monsters/nocmar.md), choose “That's a lot to lose, indeed.”

    - **Needs:** not yet stage 50, 60; not reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80); reached stage 130 of [Much water](../quests/brv_flood.md#stage-130)
    - *“If I am to work again, I must have that house returned to me. Speak to Alkapoan. Persuade him, pay him, bargain with him. Do what must be…”*


<span id="route-30"></span>

??? note "Stage 30 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “Nocmar has sent me to get back what was once his.”

    - **Needs:** not yet stage 35, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“Ah...so this is for Nocmar? The man who couldn't pay his debt and lost everything. And now you want me to just hand it back? Hah! If he…”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “Nocmar has sent me to get back what was once his.”

    - **Needs:** not yet stage 35, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“Ah...so this is for Nocmar? The man who couldn't pay his debt and lost everything. And now you want me to just hand it back? Hah! If he…”*


<span id="route-35"></span>

??? note "Stage 35 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “[lie] I want the glowing white house. I need a place to hide from my parents.”

    - **Needs:** not yet stage 30, 45, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“You want the house for yourself? Now that is interesting. Most people shy away from that cursed glow, but I can see ambition in your eyes.…”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “[lie] I want the glowing white house. I need a place to hide from my parents.”

    - **Needs:** not yet stage 30, 45, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“You want the house for yourself? Now that is interesting. Most people shy away from that cursed glow, but I can see ambition in your eyes.…”*


<span id="route-40"></span>

??? note "Stage 40 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “Okay?”

    - **Needs:** not yet stage 30, 45, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“He's late. Bring me what he owes, and don't let him wiggle out of it. I want every bit of the five thousand gold. When you return with the…”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “Okay?”

    - **Needs:** not yet stage 30, 45, 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15)
    - *“He's late. Bring me what he owes, and don't let him wiggle out of it. I want every bit of the five thousand gold. When you return with the…”*


<span id="route-45"></span>

??? note "Stage 45 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 4 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “Yes. He sent me to collect the operation tax.”

    - **Needs:** stage 40; not yet stage 45; not reached stage 100 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100)
    - **Gives:** 5000× [Gold coins](../items/gold.md)
    - *“[Grumbles] Always the same story. Alkapoan's cut, never mine. Fine, here. Take your five thousand gold and tell him I'm clear...until next…”*

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “Yes. He sent me to collect the operation tax.”

    - **Needs:** stage 40; not yet stage 45; not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); not reached stage 100 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100)
    - **Gives:** 5000× [Gold coins](../items/gold.md)
    - *“[Grumbles] Always the same story. Alkapoan's cut, never mine. Fine, here. Take your five thousand gold and tell him I'm clear...until next…”*

    **Way 3:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “[lie]Six thousand. Collector's fees, you understand.”

    - **Needs:** stage 40; not yet stage 45; not reached stage 100 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100)
    - **Gives:** 6000× [Gold coins](../items/gold.md)
    - *“Slams the table, six?! That greedy vulture...fine, here. Just get out before I change my mind.”*

    **Way 4:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “[lie]Six thousand. Collector's fees, you understand.”

    - **Needs:** stage 40; not yet stage 45; not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); not reached stage 100 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100)
    - **Gives:** 6000× [Gold coins](../items/gold.md)
    - *“Slams the table, six?! That greedy vulture...fine, here. Just get out before I change my mind.”*


<span id="route-50"></span>

??? note "Stage 50 · Mustura, Alkapoan · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “Here, take the fourty-five thousand and give me the deed and the key.”

    - **Needs:** not yet stage 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15); latest stage of [A place to forge](../quests/place_to_forge.md#stage-45) is 45; pay 45,000 gold
    - **Gives:** 1× [White house deed](../items/white_house_deed.md), 1× [White house key](../items/white_house_key.md)
    - *“A pleasure doing business with you.”*

    **Way 2:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “Here, take the fourty-five thousand and give me the deed and the key.”

    - **Needs:** not yet stage 50; reached stage 200 of [Much water](../quests/brv_flood.md#stage-200); reached stage 15 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-15); latest stage of [A place to forge](../quests/place_to_forge.md#stage-45) is 45; pay 45,000 gold
    - **Gives:** 1× [White house deed](../items/white_house_deed.md), 1× [White house key](../items/white_house_key.md)
    - *“A pleasure doing business with you.”*


<span id="route-60"></span>

??? note "Stage 60 · Nocmar · 1 way"

    **Way 1:** Talk to [Nocmar](../monsters/nocmar.md), choose “Well, that time has come back! I have the deed and the key to your forge house. [hand them to Nocmar]”

    - **Needs:** not yet stage 60; not reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90); reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80); latest stage of [A place to forge](../quests/place_to_forge.md#stage-50) is 50; hand over 1× [White house deed](../items/white_house_deed.md); hand over 1× [White house key](../items/white_house_key.md)
    - *“Ah, all these years and at last I have a chance to see it again.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 8 lines added, 1 line changed<br>· text: “Can you feel it? The heartsteel is glowing again.” → “There was a time, before all this, when I had a place. A house. Not j…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=place_to_forge.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
