---
description: "Brimhaven blackjack story flags is a hidden quest in Andor's Trail, started by Dealer (brimhaven_tavern_west_back). 10 stages. Bet 1"
---

# Brimhaven blackjack story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_blackjack_hidden` |
| **In journal** | No (hidden flag) |
| **Stages** | 10 |
| **Started by** | [Dealer](../monsters/brv_blackjack_dealer.md) ([Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) |
| **NPCs involved** | [Dealer](../monsters/brv_blackjack_dealer.md), [Guard](../monsters/guard.md#v-brv_tavern_west_guard), [Zimsko](../monsters/zimsko.md) |
| **Locations** | [Brimhaven tavern west](../maps/brimhaven_tavern_west.md), [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) |
| **Related quests** | 2 |

</div>

## Overview

> Bet 1

## Prerequisites to start

**Route 1** ([Dealer](../monsters/brv_blackjack_dealer.md) ([Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md))):

- pay 1 gold

**Route 2** (stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)):

- NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50)
- pay 1 gold


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Fair play?](brv_blackjack.md#stage-40) | stage 40 reached, for stage 150 here |
| Requires | [Fair play?](brv_blackjack.md#stage-50) | stage 50 reached, for stage 150 here |
| Requires | [Fair play?](brv_blackjack.md#stage-60) | stage 60 reached, for stage 150 here |
| Requires | [A place to forge](place_to_forge.md#stage-40) | stage 40 reached, for stage 150 here |
| Blocked by | [Fair play?](brv_blackjack.md#stage-50) | stage 50 must NOT be reached, for stages 1, 10, 20, 30, 140 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-20) | stage 20 there needs stage 110 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-30) | stage 30 there needs stage 110 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-31) | stage 31 there needs stage 110 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-60) | stage 60 there needs stage 150 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-70) | stage 70 there needs stages 110, 140 here |
| Unlocks | [Fair play?](brv_blackjack.md#stage-80) | stage 80 there needs stages 110, 140 here |
| Blocks | [A place to forge](place_to_forge.md#stage-45) | reaching stage 100 here closes stage 45 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | Bet 1 | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-10"></span>[10](#route-10) | Bet 2 | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-20"></span>[20](#route-20) | Bet 5 | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-30"></span>[30](#route-30) | Bet 10<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-100"></span>[100](#route-100) | Seat taken<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-110"></span>[110](#route-110) | Started talking to Zimsko | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-120"></span>[120](#route-120) | Bought Zimsko beer | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-130"></span>[130](#route-130) | Zimsko talked about loosing money | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-140"></span>[140](#route-140) | Played blackjack for higher amounts<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – |
| <span id="stage-150"></span>[150](#route-150) | Allowed to enter backroom<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span> | [Guard](../monsters/guard.md#v-brv_tavern_west_guard), stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) | varies by route (see below) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “1 Gold”

    - **Needs:** pay 1 gold

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “1 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 1 gold


<span id="route-10"></span>

??? note "Stage 10 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “2 Gold”

    - **Needs:** pay 2 gold

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “2 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 2 gold


<span id="route-20"></span>

??? note "Stage 20 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “5 Gold”

    - **Needs:** pay 5 gold; faction “brv_blackjack_won” ≥ 3

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “5 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 5 gold; faction “brv_blackjack_won” ≥ 3


<span id="route-30"></span>

??? note "Stage 30 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “10 Gold”

    - **Needs:** pay 10 gold; faction “brv_blackjack_won” ≥ 3

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “10 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 10 gold; faction “brv_blackjack_won” ≥ 3


<span id="route-100"></span>

??? note "Stage 100 · stepping on a trigger on brimhaven_tavern_west_back · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)



<span id="route-110"></span>

??? note "Stage 110 · Zimsko · 1 way"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), automatic

    - *“What do you want from me?”*


<span id="route-120"></span>

??? note "Stage 120 · Zimsko · 1 way"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “Let's drink a beer together. I will pay. [Pay 2 gold]”

    - **Needs:** pay 2 gold


<span id="route-130"></span>

??? note "Stage 130 · Zimsko · 1 way"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “I want to join you for a beer.”

    - *“I lost all my money gambling and can't afford a beer.”*


<span id="route-140"></span>

??? note "Stage 140 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 4 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “5 Gold”

    - **Needs:** pay 5 gold; faction “brv_blackjack_won” ≥ 3

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “5 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 5 gold; faction “brv_blackjack_won” ≥ 3

    **Way 3:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “10 Gold”

    - **Needs:** pay 10 gold; faction “brv_blackjack_won” ≥ 3

    **Way 4:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “10 Gold”

    - **Needs:** not reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 10 gold; faction “brv_blackjack_won” ≥ 3


<span id="route-150"></span>

??? note "Stage 150 · Guard, stepping on a trigger on brimhaven_tavern_west · 3 ways"

    **Way 1:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), automatic

    - **Needs:** reached stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40)
    - **Gives:** sets stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40)
    - *“I wish you good luck. [Laughs]”*

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md), choose “Sure I am. I'm on official Alkapoan business.”

    - **Needs:** stage 150; reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler2_evil); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler1_evil); killed 1× [Dealer](../monsters/brv_blackjack_dealer.md#v-brv_blackjack_dealer_evil); latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40
    - **Gives:** spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back
    - *“Oh, sorry. Please don't tell Alkapoan that I hassled you.”*

    **Way 3:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), choose “Sure I am. I'm on official Alkapoan business.”

    - **Needs:** reached stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60); latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40
    - **Gives:** spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back
    - *“Oh, sorry. Please don't tell Alkapoan that I hassled you.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 12 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_blackjack_hidden` |
    | Name in game data | `brv_blackjack_hidden` |
    | showInLog | 0 |
    | Stage IDs | 1, 10, 20, 30, 100, 110, 120, 130, 140, 150 |
    | Dialogue nodes setting stages | 1: `blackjack_bet_1`, 10: `blackjack_bet_2`, 20: `blackjack_bet_5`, 30: `blackjack_bet_10`, 100: `blackjack_seat`, 110: `brv_zimsko_10`, 120: `brv_zimsko_20`, 130: `brv_zimsko_10_2`, 140: `blackjack_bet_5`, 140: `blackjack_bet_10`, 150: `brv_tavern_west_guard_20`, 150: `brv_tavern_west_guard_alkapaon_business_10` |
    | Dialogue nodes clearing stages | 100: `blackjack_left_seat`, 150: `brv_tavern_west_guard_90`, 1: `blackjack_bet`, 10: `blackjack_bet`, 20: `blackjack_bet`, 30: `blackjack_bet` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
