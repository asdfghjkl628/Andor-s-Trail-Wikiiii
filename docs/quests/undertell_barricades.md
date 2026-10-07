---
description: "You shall pass is a quest in Andor's Trail, started by Myrelis (galmore_58). 14 stages, 7,204 XP in total. I asked Myrelis how to get the barricades to Undertell removed and he told me to meet his friend Shannal inside the beach-scene house."
---

# You shall pass

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `undertell_barricades` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 160) |
| **Started by** | [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) |
| **NPCs involved** | [Bela](../monsters/bela.md), [Bela](../monsters/bela.md#v-bela_2), [Benbyr](../monsters/benbyr.md), [Drunkard](../monsters/drunkard.md), [Myrelis](../monsters/mg_myrelis.md), [Shannal](../monsters/shannal.md) |
| **Locations** | [crossroads](../maps/crossroads.md), [fallhaven_nw](../maps/fallhaven_nw.md), [galmore_58](../maps/galmore_58.md), [mt_galmore_railhouse](../maps/mt_galmore_railhouse.md) |
| **Total XP** | 7,204 |
| **Related quests** | 4 |

</div>

## Overview

> I asked Myrelis how to get the barricades to Undertell removed and he told me to meet his friend Shannal inside the beach-scene house.

## Prerequisites to start

Start with [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)). Required:

- reached stage 9 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-9)
- latest stage of [Lost treasures](../quests/nocmar.md#stage-35) is 35
- NOT reached stage 20 of [You shall pass](../quests/undertell_barricades.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A giant snake](bela_gsnake.md#stage-90) | stage 90 reached, for stage 150 here |
| Requires | [galmore_nondisplayed (hidden flag)](galmore_nondisplayed.md#stage-9) | stage 9 reached, for stage 10 here |
| Requires | [Lost treasures](nocmar.md#stage-35) | stage 35 reached, for stage 10 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-55) | stage 55 reached, for stage 130 here |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-55) | reaching stage 130 here closes stage 55 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I asked Myrelis how to get the barricades to Undertell removed and he told me to meet his friend Shannal inside the beach-scene house. | [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) | – | spawns monsters on mt_galmore_railhouse |
| <span id="stage-20"></span>20 | I met Shannal and she said I had to prove myself before she would remove the barriers. She feared that I am not ready to enter Undertell. | [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) | – | – |
| <span id="stage-40"></span>40 | Shannal gave me a special Traders' Guild bronze coin and asked me to show it to Benbyr north of Fallhaven. | [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) | stage 20 | gives 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md) |
| <span id="stage-60"></span>60 | A frightened Benbyr told me these coins were payments his ancestor received for kidnapping people to work in the mines of Undertell. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | carry 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md), stage 40 | – |
| <span id="stage-70"></span>70 | Benbyr asked me to help save him from Shannal. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | carry 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md), stage 40 | – |
| <span id="stage-80"></span>80 | Shannal told me she did not want to kill Benbyr. She wanted him to pay toward helping her descendant, the drunkard named Rain who sleeps outside the Fallhaven Tavern. | [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) | stage 70 | – |
| <span id="stage-90"></span>90 | Shannal asked me to help cure Rain by giving him one of Lodar's Potion of Heightened Senses and whatever I can get of value from Benbyr. But I should visit Benbyr first. | [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) | stage 70 | – |
| <span id="stage-100"></span>100 | Benbyr offered me fifty gold to keep the matter quiet. I refused. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 90 | – |
| <span id="stage-110"></span>110 | Benbyr then offered 500 gold. I still refused. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 90 | – |
| <span id="stage-120"></span>120 | Benbyr became terrified and handed over 5000 gold. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 90 | gives 5000× [Gold coins](../items/gold.md) |
| <span id="stage-130"></span>130 | I gave one of Lodar's Potion of Heightened Senses to drunkard outside the Fallhaven tavern, and he remembered his time in Undertell. | [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) | have 5,000 gold | – |
| <span id="stage-140"></span>140 | I assured Rain that Shannal was at peace and gave him the 5000 gold Benbyr had given me. He told me to keep the money safe with Bela until his hangover passed. | [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) | pay 5,000 gold, stage 130 | gives 4850× [Gold coins](../items/gold.md) |
| <span id="stage-150"></span>150 | I entrusted 4850 gold to Bela for safekeeping. She agreed to hold it. | [Bela](../monsters/bela.md#v-bela_2)<br>[Bela](../monsters/bela.md) | pay 4,850 gold, stage 140 | removes monsters from fallhaven_nw<br>spawns monsters on fallhaven_nw |
| <span id="stage-160"></span>160 | Shannal thanked me for helping Rain and warned me to be careful. She removed the barricades in front of the entrance to Undertell. **(completes quest)**<br><span class="qnote">🔓 You can finally access a previously blocked area on [Galmore 58](../maps/galmore_58.md).</span><br><span class="qnote">🗺️ Part of [Galmore 58](../maps/galmore_58.md) visibly changes.</span> | [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) | stage 150 | 7,204 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Myrelis](../monsters/mg_myrelis.md) ([galmore_58](../maps/galmore_58.md)) → choose “How do I get past those barricades?” — **conditions:** reached stage 9 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-9); latest stage of [Lost treasures](../quests/nocmar.md#stage-35) is 35; NOT reached stage 20 of [You shall pass](../quests/undertell_barricades.md#stage-20) → **stage 10**; also spawns monsters on mt_galmore_railhouse. NPC: “To enter Undertell, you need to talk to my friend Shannal, she has just come to spend a day at the beach. Shannal is…”

???+ note "Stage 20: 1 route"

    1. Talk to [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) → the conversation leads here automatically — **conditions:** latest stage of [You shall pass](../quests/undertell_barricades.md#stage-20) is 20 → **stage 20**. NPC: “If you want to get into Undertell, you shall have to prove your capability to go inside. There are plenty of ghosts…”

???+ note "Stage 40: 1 route"

    1. Talk to [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) → choose “So, what do you want from me?” — **conditions:** latest stage of [You shall pass](../quests/undertell_barricades.md#stage-20) is 20 → **stage 40**; also gives 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md). NPC: “Here, take this bronze coin. It is a 'Traders' Guild Bronze coin' and the only one I have left, so don't lose it. Now,…”

???+ note "Stage 60: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Why is that?” — **conditions:** reached stage 40 of [You shall pass](../quests/undertell_barricades.md#stage-40); carry 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md); NOT reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70) → **stage 60**. NPC: “Oh well, we're not proud of it. My ancestor was one of those who would force or capture people to work in the mines of…”

???+ note "Stage 70: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Old sins cast long shadows. However, perhaps I could talk to her, ask her to spare you?” — **conditions:** reached stage 40 of [You shall pass](../quests/undertell_barricades.md#stage-40); carry 1× [Trader's Guild bronze coin](../items/trader_guild-coins.md); NOT reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70) → **stage 70**. NPC: “W-w-will you? T-t-t-thank you! P-p-p-please help me.”

???+ note "Stage 80: 1 route"

    1. Talk to [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) → choose “Do you intend to kill him?” — **conditions:** reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70); NOT reached stage 100 of [You shall pass](../quests/undertell_barricades.md#stage-100) → **stage 80**. NPC: “Benbyr? No, if I wanted, I could have harmed his predecessors. But I seek your help. Benbyr has to make restitution.”

???+ note "Stage 90: 1 route"

    1. Talk to [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) → choose “Poor guy.” — **conditions:** reached stage 70 of [You shall pass](../quests/undertell_barricades.md#stage-70); NOT reached stage 100 of [You shall pass](../quests/undertell_barricades.md#stage-100) → **stage 90**. NPC: “[sternly] And don't keep any gold from Benbyr for yourself, else you'll not get into Undertell!”

???+ note "Stage 100: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Well, that's not my problem.” — **conditions:** reached stage 90 of [You shall pass](../quests/undertell_barricades.md#stage-90); NOT reached stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120) → **stage 100**. NPC: “All I have is fifty gold, I swear of it.”

???+ note "Stage 110: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Are you kidding me? Let me call the ghost - she must be nearby...” — **conditions:** reached stage 90 of [You shall pass](../quests/undertell_barricades.md#stage-90); NOT reached stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120) → **stage 110**. NPC: “N-n-no, I found some more in my other pocket. I have 500 gold.”

???+ note "Stage 120: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Old sins cast long shadows. Try harder.” — **conditions:** reached stage 90 of [You shall pass](../quests/undertell_barricades.md#stage-90); NOT reached stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120) → **stage 120**; also gives 5000× [Gold coins](../items/gold.md). NPC: “You'll bankrupt me! Well, here's 5000. It's all my savings I secreted away before I was arrested and put in a Feygard…”

???+ note "Stage 130: 1 route"

    1. Talk to [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) → choose “Just drink the potion.” — **conditions:** reached stage 55 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-55); NOT reached stage 130 of [You shall pass](../quests/undertell_barricades.md#stage-130); have 5,000 gold → **stage 130**. NPC: “Now I remember; it was horrible. [weeping]”

???+ note "Stage 140: 1 route"

    1. Talk to [Drunkard](../monsters/drunkard.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) → choose “Worry not, as restitution, Shannal made the kidnapper's descendant, Benbyr pay up. Here's 5,000 gold. Keep…” — **conditions:** latest stage of [You shall pass](../quests/undertell_barricades.md#stage-130) is 130; pay 5,000 gold → **stage 140**; also gives 4850× [Gold coins](../items/gold.md). NPC: “Thank you! Please ask Bela to keep them safe till Rain, oh by the way, that's my name, gets over this hangover. I need…”

???+ note "Stage 150: 2 routes"

    1. Talk to [Bela](../monsters/bela.md#v-bela_2) → choose “Please keep these 4,850 gold coins for safekeeping. Rain asked for you until he gets over his hangover,…” — **conditions:** latest stage of [You shall pass](../quests/undertell_barricades.md#stage-140) is 140; pay 4,850 gold → **stage 150**; also removes monsters from fallhaven_nw, spawns monsters on fallhaven_nw. NPC: “Definitely. Count on me. Glad you could help him, the poor sod.”
    2. Talk to [Bela](../monsters/bela.md) → choose “Please keep these 4,850 gold coins for safekeeping. Rain asked for you until he gets over his hangover,…” — **conditions:** reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90); latest stage of [You shall pass](../quests/undertell_barricades.md#stage-140) is 140; pay 4,850 gold → **stage 150**; also removes monsters from fallhaven_nw, spawns monsters on fallhaven_nw. NPC: “Definitely. Count on me. Glad you could help him, the poor sod.”

???+ note "Stage 160: 1 route"

    1. Talk to [Shannal](../monsters/shannal.md) ([mt_galmore_railhouse](../maps/mt_galmore_railhouse.md)) → the conversation leads here automatically — **conditions:** latest stage of [You shall pass](../quests/undertell_barricades.md#stage-150) is 150 → **stage 160**. NPC: “You may now pass. The path to Undertell is open. Fare the well, wanderer.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_barricades.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_barricades.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_barricades.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_barricades.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=undertell_barricades.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `undertell_barricades` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160 |
    | Dialogue nodes setting stages | 10: `mg_myrelis_shannal_10`, 20: `shannal_welcome_30`, 40: `shannal_benbyr_10`, 60: `benbyr_shannal_40`, 70: `benbyr_shannal_70`, 80: `shannal_benbyr_50`, 90: `shannal_benbyr_95`, 100: `benbyr_restitution_40`, 110: `benbyr_restitution_50`, 120: `benbyr_restitution_70`, 130: `fallhaven_drunk_remember_10`, 140: `fallhaven_drunk_remember_40`, 150: `bela_rain`, 160: `shannal_removes_barricades_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
