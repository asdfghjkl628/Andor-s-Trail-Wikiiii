# brv_blackjack_hidden

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_blackjack_hidden` |
| **In journal** | No (hidden flag) |
| **Stages** | 10 |
| **Started by** | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)), stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) |
| **NPCs involved** | [Dealer](../monsters/brv_blackjack_dealer.md), [Guard](../monsters/brv_tavern_west_guard.md), [Zimsko](../monsters/zimsko.md) |
| **Locations** | [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md), [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) |
| **Related quests** | 2 |

</div>

## Overview

> Bet 1

## Prerequisites to start

**Route 1** ([Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))):

- pay 1 gold

**Route 2** (stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)):

- NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50)
- pay 1 gold

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

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | Bet 1 | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 1 gold | – |
| <span id="stage-10"></span>10 | Bet 2 | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 2 gold | – |
| <span id="stage-20"></span>20 | Bet 5 | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 5 gold | – |
| <span id="stage-30"></span>30 | Bet 10<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 10 gold | – |
| <span id="stage-100"></span>100 | Seat taken<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | – | – |
| <span id="stage-110"></span>110 | Started talking to Zimsko | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | – | – |
| <span id="stage-120"></span>120 | Bought Zimsko beer | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | pay 2 gold | – |
| <span id="stage-130"></span>130 | Zimsko talked about loosing money | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | – | – |
| <span id="stage-140"></span>140 | Played blackjack for higher amounts<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 10 gold, pay 5 gold | – |
| <span id="stage-150"></span>150 | Allowed to enter backroom<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span> | [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md))<br>stepping on a trigger on [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md) | – | sets stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40)<br>spawns monsters on brimhaven_tavern_west_back |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “1 Gold” — **conditions:** pay 1 gold → **stage 1**
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “1 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 1 gold → **stage 1**

???+ note "Stage 10: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “2 Gold” — **conditions:** pay 2 gold → **stage 10**
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “2 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 2 gold → **stage 10**

???+ note "Stage 20: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “5 Gold” — **conditions:** pay 5 gold; faction “brv_blackjack_won” ≥ 3 → **stage 20**
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “5 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 5 gold; faction “brv_blackjack_won” ≥ 3 → **stage 20**

???+ note "Stage 30: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “10 Gold” — **conditions:** pay 10 gold; faction “brv_blackjack_won” ≥ 3 → **stage 30**
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “10 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 10 gold; faction “brv_blackjack_won” ≥ 3 → **stage 30**

???+ note "Stage 100: 1 route"

    1. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → the conversation leads here automatically → **stage 100**

???+ note "Stage 110: 1 route"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically → **stage 110**. NPC: “What do you want from me?”

???+ note "Stage 120: 1 route"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “Let's drink a beer together. I will pay. [Pay 2 gold]” — **conditions:** pay 2 gold → **stage 120**

???+ note "Stage 130: 1 route"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I want to join you for a beer.” → **stage 130**. NPC: “I lost all my money gambling and can't afford a beer.”

???+ note "Stage 140: 4 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “5 Gold” — **conditions:** pay 5 gold; faction “brv_blackjack_won” ≥ 3 → **stage 140**
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “5 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 5 gold; faction “brv_blackjack_won” ≥ 3 → **stage 140**
    3. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “10 Gold” — **conditions:** pay 10 gold; faction “brv_blackjack_won” ≥ 3 → **stage 140**
    4. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “10 Gold” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 10 gold; faction “brv_blackjack_won” ≥ 3 → **stage 140**

???+ note "Stage 150: 3 routes"

    1. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40) → **stage 150**; also sets stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40). NPC: “I wish you good luck. [Laughs]”
    2. stepping on a trigger on [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md) → choose “Sure I am. I'm on official Alkapoan business.” — **conditions:** reached stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150); reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Gambler](../monsters/brv_blackjack_gambler2_evil.md); killed 1× [Gambler](../monsters/brv_blackjack_gambler1_evil.md); killed 1× [Dealer](../monsters/brv_blackjack_dealer_evil.md); latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40 → **stage 150**; also spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back. NPC: “Oh, sorry. Please don't tell Alkapoan that I hassled you.”
    3. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “Sure I am. I'm on official Alkapoan business.” — **conditions:** reached stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60); latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40 → **stage 150**; also spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back. NPC: “Oh, sorry. Please don't tell Alkapoan that I hassled you.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_blackjack_hidden` |
    | showInLog | 0 |
    | Stage IDs | 1, 10, 20, 30, 100, 110, 120, 130, 140, 150 |
    | Dialogue nodes setting stages | 1: `blackjack_bet_1`, 10: `blackjack_bet_2`, 20: `blackjack_bet_5`, 30: `blackjack_bet_10`, 100: `blackjack_seat`, 110: `brv_zimsko_10`, 120: `brv_zimsko_20`, 130: `brv_zimsko_10_2`, 140: `blackjack_bet_5`, 140: `blackjack_bet_10`, 150: `brv_tavern_west_guard_20`, 150: `brv_tavern_west_guard_alkapaon_business_10` |
    | Dialogue nodes clearing stages | 100: `blackjack_left_seat`, 150: `brv_tavern_west_guard_90`, 1: `blackjack_bet`, 10: `blackjack_bet`, 20: `blackjack_bet`, 30: `blackjack_bet` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
