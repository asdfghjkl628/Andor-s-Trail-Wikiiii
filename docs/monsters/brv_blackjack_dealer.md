---
description: "Dealer is an NPC who can also be fought in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_130.png){ .sprite } Dealer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_130.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Brimhaven |
| **Class** | Humanoid |
| **HP** | 30 |
| **XP when defeated** | 84 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Dealer. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`brv_blackjack_dealer`](#v-brv_blackjack_dealer) | NPC | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_dealer) | – | – |
| [`brv_blackjack_dealer_evil`](#v-brv_blackjack_dealer_evil) | Enemy | Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | – | 30 |

## Brimhaven, Brimhaven tavern west back (brv_blackjack_dealer) { #v-brv_blackjack_dealer }

**Entry ID:** `brv_blackjack_dealer` · **Type:** NPC

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md#pin-npc-brv_blackjack_dealer)

### Quests

- [A place to forge](../quests/place_to_forge.md): stage 45
- [Fair play?](../quests/brv_blackjack.md): stages 45, 50
- [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md): stages 1, 10, 20, 30, 140

### Dialogue simulator

Set your quest stages and items, then talk to Dealer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blackjack_dealer_select.json" data-npc="Dealer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (99 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_blackjack_dealer-blackjack_dealer_select"></span>**`blackjack_dealer_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 100 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-100))* → [blackjack_dealer_20](#d-brv_blackjack_dealer-blackjack_dealer_20)
    - branch 2 → [blackjack_dealer_30](#d-brv_blackjack_dealer-blackjack_dealer_30)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_20"></span>**`blackjack_dealer_20`** [Dealer](../monsters/brv_blackjack_dealer.md): “Take a seat on the empty chair if you want to play a round.”

    - Next *(if reached stage 40 of [A place to forge](../quests/place_to_forge.md#stage-40); NOT reached stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45))* → [blackjack_dealer_collect_tax_10](#d-brv_blackjack_dealer-blackjack_dealer_collect_tax_10)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_30"></span>**`blackjack_dealer_30`** [Dealer](../monsters/brv_blackjack_dealer.md): “Do you want to play a round?”

    - “Yes” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)
    - “No” → *conversation ends*

    <span id="d-brv_blackjack_dealer-blackjack_dealer_collect_tax_10"></span>**`blackjack_dealer_collect_tax_10`** Dealer: “...Unless you're not here to play. Don't tell me Alkapoan sent you for his damned tax again?”

    - “Yes. He sent me to collect the operation tax.” → [blackjack_dealer_collect_tax_20](#d-brv_blackjack_dealer-blackjack_dealer_collect_tax_20)
    - “You owe Alkapoan. I'm here to take what's his.” → [blackjack_dealer_collect_tax_25](#d-brv_blackjack_dealer-blackjack_dealer_collect_tax_25)

    <span id="d-brv_blackjack_dealer-blackjack_bet_select"></span>**`blackjack_bet_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_blackjack_won” ≥ 3; NOT reached stage 45 of [Fair play?](../quests/brv_blackjack.md#stage-45))* → [blackjack_play_higher_amounts](#d-brv_blackjack_dealer-blackjack_play_higher_amounts)
    - branch 2 → [blackjack_bet](#d-brv_blackjack_dealer-blackjack_bet)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_collect_tax_20"></span>**`blackjack_dealer_collect_tax_20`** Dealer: “[Grumbles] Always the same story. Alkapoan's cut, never mine. Fine, here. Take your five thousand gold and tell him I'm clear...until next month.” — **effects:** sets stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45), gives 5000× [Gold coins](../items/gold.md)


    <span id="d-brv_blackjack_dealer-blackjack_dealer_collect_tax_25"></span>**`blackjack_dealer_collect_tax_25`** Dealer: “Take what's his? Ha! He already bleeds me dry every month. How much is it this time?”

    - “[lie]Six thousand. Collector's fees, you understand.” → [blackjack_dealer_collect_tax_30](#d-brv_blackjack_dealer-blackjack_dealer_collect_tax_30)

    <span id="d-brv_blackjack_dealer-blackjack_play_higher_amounts"></span>**`blackjack_play_higher_amounts`** Dealer: “Now let's stop this child's game and play for higher amounts.” — **effects:** sets stage 45 of [Fair play?](../quests/brv_blackjack.md#stage-45)

    - Next → [blackjack_bet](#d-brv_blackjack_dealer-blackjack_bet)

    <span id="d-brv_blackjack_dealer-blackjack_bet"></span>**`blackjack_bet`** Dealer: “What is your 17+4 bet?” — **effects:** clears stage 1 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-1), clears stage 10 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-10), clears stage 20 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-20), clears stage 30 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-30)

    - “1 Gold” *(if pay 1 gold)* → [blackjack_bet_1](#d-brv_blackjack_dealer-blackjack_bet_1)
    - “2 Gold” *(if pay 2 gold)* → [blackjack_bet_2](#d-brv_blackjack_dealer-blackjack_bet_2)
    - “5 Gold” *(if pay 5 gold; faction “brv_blackjack_won” ≥ 3)* → [blackjack_bet_5](#d-brv_blackjack_dealer-blackjack_bet_5)
    - “10 Gold” *(if pay 10 gold; faction “brv_blackjack_won” ≥ 3)* → [blackjack_bet_10](#d-brv_blackjack_dealer-blackjack_bet_10)
    - “Please explain the rules to me.” → [blackjack_rules](#d-brv_blackjack_dealer-blackjack_rules)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_collect_tax_30"></span>**`blackjack_dealer_collect_tax_30`** Dealer: “Slams the table, six?! That greedy vulture...fine, here. Just get out before I change my mind.” — **effects:** sets stage 45 of [A place to forge](../quests/place_to_forge.md#stage-45), gives 6000× [Gold coins](../items/gold.md)


    <span id="d-brv_blackjack_dealer-blackjack_bet_1"></span>**`blackjack_bet_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 1 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-1)

    - branch 1 → [blackjack_draw_at_0](#d-brv_blackjack_dealer-blackjack_draw_at_0)

    <span id="d-brv_blackjack_dealer-blackjack_bet_2"></span>**`blackjack_bet_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 10 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-10)

    - branch 1 → [blackjack_draw_at_0](#d-brv_blackjack_dealer-blackjack_draw_at_0)

    <span id="d-brv_blackjack_dealer-blackjack_bet_5"></span>**`blackjack_bet_5`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 20 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-20), sets stage 140 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140)

    - branch 1 → [blackjack_draw_at_0](#d-brv_blackjack_dealer-blackjack_draw_at_0)

    <span id="d-brv_blackjack_dealer-blackjack_bet_10"></span>**`blackjack_bet_10`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 30 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-30), sets stage 140 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140)

    - branch 1 → [blackjack_draw_at_0](#d-brv_blackjack_dealer-blackjack_draw_at_0)

    <span id="d-brv_blackjack_dealer-blackjack_rules"></span>**`blackjack_rules`** Dealer: “We play with several 32-piece card decks from 7 to 10, jack (2 points), queen (3 points), king (4 points) and ace (11 points). You can draw as many cards as you want and you will get them face down so only you can take a look at them.…”

    - Next → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_0"></span>**`blackjack_draw_at_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_2](#d-brv_blackjack_dealer-blackjack_draw_2)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_3](#d-brv_blackjack_dealer-blackjack_draw_3)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_4](#d-brv_blackjack_dealer-blackjack_draw_4)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_7](#d-brv_blackjack_dealer-blackjack_draw_7)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_8](#d-brv_blackjack_dealer-blackjack_draw_8)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_9](#d-brv_blackjack_dealer-blackjack_draw_9)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 8 → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)

    <span id="d-brv_blackjack_dealer-blackjack_draw_2"></span>**`blackjack_draw_2`** Dealer: “[You have 2 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_2](#d-brv_blackjack_dealer-blackjack_draw_at_2)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_3"></span>**`blackjack_draw_3`** Dealer: “[You have 3 points.] Are you finished?”

    - “Give me one more card.” → [blackjack_draw_at_3](#d-brv_blackjack_dealer-blackjack_draw_at_3)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_4"></span>**`blackjack_draw_4`** Dealer: “[You have 4 points.] Do you risk taking another card?”

    - “Give me one more card.” → [blackjack_draw_at_4](#d-brv_blackjack_dealer-blackjack_draw_at_4)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_7"></span>**`blackjack_draw_7`** Dealer: “[You have 7 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_7](#d-brv_blackjack_dealer-blackjack_draw_at_7)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_8"></span>**`blackjack_draw_8`** Dealer: “[You have 8 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_8](#d-brv_blackjack_dealer-blackjack_draw_at_8)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_9"></span>**`blackjack_draw_9`** Dealer: “[You have 9 points.] Are you finished?”

    - “Give me one more card.” → [blackjack_draw_at_9](#d-brv_blackjack_dealer-blackjack_draw_at_9)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_10"></span>**`blackjack_draw_10`** Dealer: “[You have 10 points.] Do you risk taking another card? [Laughs]”

    - “Give me one more card.” → [blackjack_draw_at_10](#d-brv_blackjack_dealer-blackjack_draw_at_10)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_11"></span>**`blackjack_draw_11`** Dealer: “[You have 11 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_11](#d-brv_blackjack_dealer-blackjack_draw_at_11)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_2"></span>**`blackjack_draw_at_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_4](#d-brv_blackjack_dealer-blackjack_draw_4)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_5](#d-brv_blackjack_dealer-blackjack_draw_5)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_6](#d-brv_blackjack_dealer-blackjack_draw_6)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_9](#d-brv_blackjack_dealer-blackjack_draw_9)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 8 → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)

    <span id="d-brv_blackjack_dealer-blackjack_finish_below_16"></span>**`blackjack_finish_below_16`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_lose_15](#d-brv_blackjack_dealer-blackjack_lose_15)
    - branch 2 *(if random chance (13%))* → [blackjack_lose_16](#d-brv_blackjack_dealer-blackjack_lose_16)
    - branch 3 *(if random chance (15%))* → [blackjack_lose_17](#d-brv_blackjack_dealer-blackjack_lose_17)
    - branch 4 *(if random chance (12%))* → [blackjack_lose_18](#d-brv_blackjack_dealer-blackjack_lose_18)
    - branch 5 *(if random chance (7%))* → [blackjack_lose_19](#d-brv_blackjack_dealer-blackjack_lose_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_3"></span>**`blackjack_draw_at_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_5](#d-brv_blackjack_dealer-blackjack_draw_5)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_6](#d-brv_blackjack_dealer-blackjack_draw_6)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_7](#d-brv_blackjack_dealer-blackjack_draw_7)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 8 → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_4"></span>**`blackjack_draw_at_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_6](#d-brv_blackjack_dealer-blackjack_draw_6)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_7](#d-brv_blackjack_dealer-blackjack_draw_7)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_8](#d-brv_blackjack_dealer-blackjack_draw_8)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 8 → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_7"></span>**`blackjack_draw_at_7`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_9](#d-brv_blackjack_dealer-blackjack_draw_9)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 8 → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_8"></span>**`blackjack_draw_at_8`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 8 → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_9"></span>**`blackjack_draw_at_9`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_11](#d-brv_blackjack_dealer-blackjack_draw_11)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 8 → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_10"></span>**`blackjack_draw_at_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 8 → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_11"></span>**`blackjack_draw_at_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 8 → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)

    <span id="d-brv_blackjack_dealer-blackjack_draw_5"></span>**`blackjack_draw_5`** Dealer: “[You have 5 points.] Are you finished [laughs]?”

    - “Give me one more card.” → [blackjack_draw_at_5](#d-brv_blackjack_dealer-blackjack_draw_at_5)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_6"></span>**`blackjack_draw_6`** Dealer: “[You have 6 points.] Was that your last card?”

    - “Give me one more card.” → [blackjack_draw_at_6](#d-brv_blackjack_dealer-blackjack_draw_at_6)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_12"></span>**`blackjack_draw_12`** Dealer: “[You have 12 points.] Was that your last card?”

    - “Give me one more card.” → [blackjack_draw_at_12](#d-brv_blackjack_dealer-blackjack_draw_at_12)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_13"></span>**`blackjack_draw_13`** Dealer: “[You have 13 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_13](#d-brv_blackjack_dealer-blackjack_draw_at_13)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_lose_15"></span>**`blackjack_lose_15`** Dealer: “I have 15 points. Bad luck for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_16"></span>**`blackjack_lose_16`** Dealer: “[You show each other your cards]. I have 16 points and you lose. Next time you will be lucky.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_17"></span>**`blackjack_lose_17`** Dealer: “[You show each other your cards.] I have 17 points so you lose. Don't give up.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_18"></span>**`blackjack_lose_18`** Dealer: “[You show each other your cards.] I have 18 points and you lose. Next game next chance for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_19"></span>**`blackjack_lose_19`** Dealer: “[You show each other your cards.] I have 19 points and you lose. Double your bet and win back what you lost.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_20"></span>**`blackjack_lose_20`** Dealer: “[You show each other your cards.] I have 20 points. Bad luck for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_lose_21"></span>**`blackjack_lose_21`** Dealer: “[You show each other your cards.] I have 21 points and you lose. Next time, you will be lucky.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_22"></span>**`blackjack_win_22`** Dealer: “[You show each other your cards.] I have 22 points. You will take my last coin if you stay that lucky.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_win_23"></span>**`blackjack_win_23`** Dealer: “[You show each other your cards.] I have 23 points. Give me a chance to win my money back.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_win_24"></span>**`blackjack_win_24`** Dealer: “[You show each other your cards.] I have 24 points. You have a lot of luck.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_win_25"></span>**`blackjack_win_25`** Dealer: “[You show each other your cards.] I have 25 points. In my opinion you are a bit too lucky.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_14"></span>**`blackjack_draw_14`** Dealer: “[You have 14 points.] Do you want to stop now?”

    - “Give me one more card.” → [blackjack_draw_at_14](#d-brv_blackjack_dealer-blackjack_draw_at_14)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_15"></span>**`blackjack_draw_15`** Dealer: “[You have 15 points.] Do you want one more card?”

    - “Give me one more card.” → [blackjack_draw_at_15](#d-brv_blackjack_dealer-blackjack_draw_at_15)
    - “I am finished.” → [blackjack_finish_below_16](#d-brv_blackjack_dealer-blackjack_finish_below_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_16"></span>**`blackjack_draw_16`** Dealer: “[You have 16 points.] Are you finished?”

    - “Give me one more card.” → [blackjack_draw_at_16](#d-brv_blackjack_dealer-blackjack_draw_at_16)
    - “I am finished.” → [blackjack_finish_16](#d-brv_blackjack_dealer-blackjack_finish_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_17"></span>**`blackjack_draw_17`** Dealer: “[You have 17 points.] Do you risk to take another card?”

    - “Give me one more card.” → [blackjack_draw_at_17](#d-brv_blackjack_dealer-blackjack_draw_at_17)
    - “I am finished.” → [blackjack_finish_17](#d-brv_blackjack_dealer-blackjack_finish_17)

    <span id="d-brv_blackjack_dealer-blackjack_draw_18"></span>**`blackjack_draw_18`** Dealer: “[You have 18 points.] Do you want to stop?”

    - “Give me one more card.” → [blackjack_draw_at_18](#d-brv_blackjack_dealer-blackjack_draw_at_18)
    - “I am finished.” → [blackjack_finish_18](#d-brv_blackjack_dealer-blackjack_finish_18)

    <span id="d-brv_blackjack_dealer-blackjack_draw_19"></span>**`blackjack_draw_19`** Dealer: “[You have 19 points.] Was that your last card?”

    - “Give me one more card.” → [blackjack_draw_at_19](#d-brv_blackjack_dealer-blackjack_draw_at_19)
    - “I am finished.” → [blackjack_finish_19](#d-brv_blackjack_dealer-blackjack_finish_19)

    <span id="d-brv_blackjack_dealer-blackjack_draw_20"></span>**`blackjack_draw_20`** Dealer: “[You have 20 points.] Do you want one more card?”

    - “Sounds stupid, but give me one more card.” → [blackjack_draw_at_20](#d-brv_blackjack_dealer-blackjack_draw_at_20)
    - “Of course I am finished.” → [blackjack_finish_20](#d-brv_blackjack_dealer-blackjack_finish_20)

    <span id="d-brv_blackjack_dealer-blackjack_draw_21"></span>**`blackjack_draw_21`** Dealer: “[You have 21 points.] Do you want one more card?”

    - “I know what I am doing. Give me one more card.” → [blackjack_draw_at_21](#d-brv_blackjack_dealer-blackjack_draw_at_21)
    - “Of course I am finished.” → [blackjack_finish_21](#d-brv_blackjack_dealer-blackjack_finish_21)

    <span id="d-brv_blackjack_dealer-blackjack_draw_22"></span>**`blackjack_draw_22`** Dealer: “[You have 22 points and overdraw.] Bad luck for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_5"></span>**`blackjack_draw_at_5`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_7](#d-brv_blackjack_dealer-blackjack_draw_7)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_8](#d-brv_blackjack_dealer-blackjack_draw_8)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_9](#d-brv_blackjack_dealer-blackjack_draw_9)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_12](#d-brv_blackjack_dealer-blackjack_draw_12)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 8 → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_6"></span>**`blackjack_draw_at_6`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_8](#d-brv_blackjack_dealer-blackjack_draw_8)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_9](#d-brv_blackjack_dealer-blackjack_draw_9)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_10](#d-brv_blackjack_dealer-blackjack_draw_10)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_13](#d-brv_blackjack_dealer-blackjack_draw_13)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 8 → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_12"></span>**`blackjack_draw_at_12`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_14](#d-brv_blackjack_dealer-blackjack_draw_14)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 8 → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_13"></span>**`blackjack_draw_at_13`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_15](#d-brv_blackjack_dealer-blackjack_draw_15)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 8 → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_40"></span>**`blackjack_dealer_40`** Dealer: “Do you want to play another round?”

    - “Let's go on.” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)
    - “I have had enough.” → *conversation ends*
    - “You are cheating. Give me my money back.” *(if NOT reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); NOT reached stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80); faction “brv_blackjack_won” ≥ 3)* → [blackjack_dealer_40_1](#d-brv_blackjack_dealer-blackjack_dealer_40_1)

    <span id="d-brv_blackjack_dealer-blackjack_win"></span>**`blackjack_win`** *(silent check: the first matching branch below is taken)* — **effects:** faction “brv_blackjack_won” +1

    - branch 1 *(if reached stage 1 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-1))* → [blackjack_win_1gold](#d-brv_blackjack_dealer-blackjack_win_1gold)
    - branch 2 *(if reached stage 10 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-10))* → [blackjack_win_2gold](#d-brv_blackjack_dealer-blackjack_win_2gold)
    - branch 3 *(if reached stage 20 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-20))* → [blackjack_win_5gold](#d-brv_blackjack_dealer-blackjack_win_5gold)
    - branch 4 *(if reached stage 30 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-30))* → [blackjack_win_10gold](#d-brv_blackjack_dealer-blackjack_win_10gold)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_14"></span>**`blackjack_draw_at_14`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_16](#d-brv_blackjack_dealer-blackjack_draw_16)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 8 → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_15"></span>**`blackjack_draw_at_15`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_17](#d-brv_blackjack_dealer-blackjack_draw_17)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)
    - branch 8 → [blackjack_draw_26](#d-brv_blackjack_dealer-blackjack_draw_26)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_16"></span>**`blackjack_draw_at_16`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_18](#d-brv_blackjack_dealer-blackjack_draw_18)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_26](#d-brv_blackjack_dealer-blackjack_draw_26)
    - branch 8 → [blackjack_draw_27](#d-brv_blackjack_dealer-blackjack_draw_27)

    <span id="d-brv_blackjack_dealer-blackjack_finish_16"></span>**`blackjack_finish_16`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_lose_16](#d-brv_blackjack_dealer-blackjack_lose_16)
    - branch 3 *(if random chance (15%))* → [blackjack_lose_17](#d-brv_blackjack_dealer-blackjack_lose_17)
    - branch 4 *(if random chance (12%))* → [blackjack_lose_18](#d-brv_blackjack_dealer-blackjack_lose_18)
    - branch 5 *(if random chance (7%))* → [blackjack_lose_19](#d-brv_blackjack_dealer-blackjack_lose_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_17"></span>**`blackjack_draw_at_17`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_19](#d-brv_blackjack_dealer-blackjack_draw_19)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_26](#d-brv_blackjack_dealer-blackjack_draw_26)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_27](#d-brv_blackjack_dealer-blackjack_draw_27)
    - branch 8 → [blackjack_draw_28](#d-brv_blackjack_dealer-blackjack_draw_28)

    <span id="d-brv_blackjack_dealer-blackjack_finish_17"></span>**`blackjack_finish_17`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_win_16](#d-brv_blackjack_dealer-blackjack_win_16)
    - branch 3 *(if random chance (15%))* → [blackjack_lose_17](#d-brv_blackjack_dealer-blackjack_lose_17)
    - branch 4 *(if random chance (12%))* → [blackjack_lose_18](#d-brv_blackjack_dealer-blackjack_lose_18)
    - branch 5 *(if random chance (7%))* → [blackjack_lose_19](#d-brv_blackjack_dealer-blackjack_lose_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_18"></span>**`blackjack_draw_at_18`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_20](#d-brv_blackjack_dealer-blackjack_draw_20)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_26](#d-brv_blackjack_dealer-blackjack_draw_26)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_27](#d-brv_blackjack_dealer-blackjack_draw_27)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_28](#d-brv_blackjack_dealer-blackjack_draw_28)
    - branch 8 → [blackjack_draw_29](#d-brv_blackjack_dealer-blackjack_draw_29)

    <span id="d-brv_blackjack_dealer-blackjack_finish_18"></span>**`blackjack_finish_18`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_win_16](#d-brv_blackjack_dealer-blackjack_win_16)
    - branch 3 *(if random chance (15%))* → [blackjack_win_17](#d-brv_blackjack_dealer-blackjack_win_17)
    - branch 4 *(if random chance (12%))* → [blackjack_lose_18](#d-brv_blackjack_dealer-blackjack_lose_18)
    - branch 5 *(if random chance (7%))* → [blackjack_lose_19](#d-brv_blackjack_dealer-blackjack_lose_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_19"></span>**`blackjack_draw_at_19`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_21](#d-brv_blackjack_dealer-blackjack_draw_21)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_26](#d-brv_blackjack_dealer-blackjack_draw_26)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_27](#d-brv_blackjack_dealer-blackjack_draw_27)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_28](#d-brv_blackjack_dealer-blackjack_draw_28)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_29](#d-brv_blackjack_dealer-blackjack_draw_29)
    - branch 8 → [blackjack_draw_30](#d-brv_blackjack_dealer-blackjack_draw_30)

    <span id="d-brv_blackjack_dealer-blackjack_finish_19"></span>**`blackjack_finish_19`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_win_16](#d-brv_blackjack_dealer-blackjack_win_16)
    - branch 3 *(if random chance (15%))* → [blackjack_win_17](#d-brv_blackjack_dealer-blackjack_win_17)
    - branch 4 *(if random chance (12%))* → [blackjack_win_18](#d-brv_blackjack_dealer-blackjack_win_18)
    - branch 5 *(if random chance (7%))* → [blackjack_lose_19](#d-brv_blackjack_dealer-blackjack_lose_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_20"></span>**`blackjack_draw_at_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_22](#d-brv_blackjack_dealer-blackjack_draw_22)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_27](#d-brv_blackjack_dealer-blackjack_draw_27)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_28](#d-brv_blackjack_dealer-blackjack_draw_28)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_29](#d-brv_blackjack_dealer-blackjack_draw_29)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_30](#d-brv_blackjack_dealer-blackjack_draw_30)
    - branch 8 → [blackjack_draw_31](#d-brv_blackjack_dealer-blackjack_draw_31)

    <span id="d-brv_blackjack_dealer-blackjack_finish_20"></span>**`blackjack_finish_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_win_16](#d-brv_blackjack_dealer-blackjack_win_16)
    - branch 3 *(if random chance (15%))* → [blackjack_win_17](#d-brv_blackjack_dealer-blackjack_win_17)
    - branch 4 *(if random chance (12%))* → [blackjack_win_18](#d-brv_blackjack_dealer-blackjack_win_18)
    - branch 5 *(if random chance (7%))* → [blackjack_win_19](#d-brv_blackjack_dealer-blackjack_win_19)
    - branch 6 *(if random chance (15%))* → [blackjack_lose_20](#d-brv_blackjack_dealer-blackjack_lose_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_at_21"></span>**`blackjack_draw_at_21`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (12%))* → [blackjack_draw_23](#d-brv_blackjack_dealer-blackjack_draw_23)
    - branch 2 *(if random chance (14%))* → [blackjack_draw_24](#d-brv_blackjack_dealer-blackjack_draw_24)
    - branch 3 *(if random chance (16%))* → [blackjack_draw_25](#d-brv_blackjack_dealer-blackjack_draw_25)
    - branch 4 *(if random chance (20%))* → [blackjack_draw_28](#d-brv_blackjack_dealer-blackjack_draw_28)
    - branch 5 *(if random chance (25%))* → [blackjack_draw_29](#d-brv_blackjack_dealer-blackjack_draw_29)
    - branch 6 *(if random chance (33%))* → [blackjack_draw_30](#d-brv_blackjack_dealer-blackjack_draw_30)
    - branch 7 *(if random chance (50%))* → [blackjack_draw_31](#d-brv_blackjack_dealer-blackjack_draw_31)
    - branch 8 → [blackjack_draw_32](#d-brv_blackjack_dealer-blackjack_draw_32)

    <span id="d-brv_blackjack_dealer-blackjack_finish_21"></span>**`blackjack_finish_21`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (8%))* → [blackjack_win_15](#d-brv_blackjack_dealer-blackjack_win_15)
    - branch 2 *(if random chance (13%))* → [blackjack_win_16](#d-brv_blackjack_dealer-blackjack_win_16)
    - branch 3 *(if random chance (15%))* → [blackjack_win_17](#d-brv_blackjack_dealer-blackjack_win_17)
    - branch 4 *(if random chance (12%))* → [blackjack_win_18](#d-brv_blackjack_dealer-blackjack_win_18)
    - branch 5 *(if random chance (7%))* → [blackjack_win_19](#d-brv_blackjack_dealer-blackjack_win_19)
    - branch 6 *(if random chance (15%))* → [blackjack_win_20](#d-brv_blackjack_dealer-blackjack_win_20)
    - branch 7 *(if random chance (27%))* → [blackjack_lose_21](#d-brv_blackjack_dealer-blackjack_lose_21)
    - branch 8 *(if random chance (37%))* → [blackjack_win_22](#d-brv_blackjack_dealer-blackjack_win_22)
    - branch 9 *(if random chance (40%))* → [blackjack_win_23](#d-brv_blackjack_dealer-blackjack_win_23)
    - branch 10 *(if random chance (66%))* → [blackjack_win_24](#d-brv_blackjack_dealer-blackjack_win_24)
    - branch 11 → [blackjack_win_25](#d-brv_blackjack_dealer-blackjack_win_25)

    <span id="d-brv_blackjack_dealer-blackjack_draw_23"></span>**`blackjack_draw_23`** Dealer: “[You have 23 points and you overdraw.] Next time you will be lucky.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_draw_24"></span>**`blackjack_draw_24`** Dealer: “[You have 24 points and you overdraw.] Don't give up.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_40_1"></span>**`blackjack_dealer_40_1`** Dealer: “Who do you think you are, calling me a cheater? Shut up or I will shut your mouth with my fist.”

    - “OK, I am sorry.” → [blackjack_dealer_30](#d-brv_blackjack_dealer-blackjack_dealer_30)
    - “Let's fight it out. [Killing him in town is a bad idea. I will try to only knock him out.]” → [blackjack_dealer_40_2](#d-brv_blackjack_dealer-blackjack_dealer_40_2)

    <span id="d-brv_blackjack_dealer-blackjack_win_1gold"></span>**`blackjack_win_1gold`** Dealer: “You win 1 gold.” — **effects:** gives 2× [Gold coins](../items/gold.md)

    - “I am lucky since I was a child.” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)

    <span id="d-brv_blackjack_dealer-blackjack_win_2gold"></span>**`blackjack_win_2gold`** Dealer: “You win 2 gold.” — **effects:** gives 4× [Gold coins](../items/gold.md)

    - “One more game please.” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)

    <span id="d-brv_blackjack_dealer-blackjack_win_5gold"></span>**`blackjack_win_5gold`** Dealer: “You win 5 gold.” — **effects:** gives 10× [Gold coins](../items/gold.md)

    - “I am a good player.” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)

    <span id="d-brv_blackjack_dealer-blackjack_win_10gold"></span>**`blackjack_win_10gold`** Dealer: “You win 10 gold.” — **effects:** gives 20× [Gold coins](../items/gold.md)

    - “One more game.” → [blackjack_bet_select](#d-brv_blackjack_dealer-blackjack_bet_select)

    <span id="d-brv_blackjack_dealer-blackjack_draw_25"></span>**`blackjack_draw_25`** Dealer: “[You have 25 points and you overdraw.] Double your bet and win back what you lost.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_draw_26"></span>**`blackjack_draw_26`** Dealer: “[You have 26 points and you overdraw.] Bad luck for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_draw_27"></span>**`blackjack_draw_27`** Dealer: “[You have 27 points and you overdraw.] Next game next chance for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_15"></span>**`blackjack_win_15`** Dealer: “I have 15 points. You have a lot of luck.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_28"></span>**`blackjack_draw_28`** Dealer: “[You have 28 points and you overdraw.] Next time you will be lucky.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_16"></span>**`blackjack_win_16`** Dealer: “[You show each other your cards.] I have 16 points. In my opinion, you are a bit too lucky.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_29"></span>**`blackjack_draw_29`** Dealer: “[You have 29 points and you overdraw.] Don't give up.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_17"></span>**`blackjack_win_17`** Dealer: “[You show each other your cards.] I have 17 points. You will take my last coin if you stay that lucky.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_30"></span>**`blackjack_draw_30`** Dealer: “[You have 30 points and you overdraw.] Next game next chance for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_18"></span>**`blackjack_win_18`** Dealer: “[You show each other your cards.] I have 18 points and you win. Give me a chance to win my money back.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_31"></span>**`blackjack_draw_31`** Dealer: “[You have 31 points and you overdraw.] Double your bet and win back what you lost.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_19"></span>**`blackjack_win_19`** Dealer: “[You show each other your cards.] I have 19 points. You have a lot of luck.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_draw_32"></span>**`blackjack_draw_32`** Dealer: “[You have 32 points and you overdraw.] Bad luck for you.”

    - Next → [blackjack_dealer_40](#d-brv_blackjack_dealer-blackjack_dealer_40)

    <span id="d-brv_blackjack_dealer-blackjack_win_20"></span>**`blackjack_win_20`** Dealer: “[You show each other your cards.] I have 20 points. In my opinion you are a bit too lucky.”

    - Next → [blackjack_win](#d-brv_blackjack_dealer-blackjack_win)

    <span id="d-brv_blackjack_dealer-blackjack_dealer_40_2"></span>**`blackjack_dealer_40_2`** Dealer: “Let us start the tavern brawl!” — **effects:** removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, sets stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50)




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 95 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 2 lines changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 20 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_dealer)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_dealer` |
    | Spawn group | `brv_blackjack_dealer` |
    | Loot table | – |
    | Conversation | `blackjack_dealer_select` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:130` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_dealer",
     "name": "Dealer",
     "iconID": "monsters_ld1:130",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "brv_blackjack_dealer",
     "phraseID": "blackjack_dealer_select"
    }
    ```


## Brimhaven, Brimhaven tavern west back (brv_blackjack_dealer_evil) { #v-brv_blackjack_dealer_evil }

**Entry ID:** `brv_blackjack_dealer_evil` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 30 |
| XP when defeated | 84 |
| Damage | 2 to 4 |
| Attack chance | 80 |
| Block chance | 30 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 2 AP |
| Attacks per turn | 5 |
| Move cost | 5 AP |
| Critical skill | 50 |
| Critical multiplier | 2.0 |
| Critical hit chance | 26% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Cards of luck](../items/card_deck.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 100 to 200 |
| [Iron dagger](../items/dagger0.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | Brimhaven | 1 | Appears later, during a quest |

### Quests that count defeats

- [Fair play?](../quests/brv_blackjack.md#stage-60) with [Guard](../monsters/guard.md#v-brv_tavern_west_guard) ([Brimhaven tavern west](../maps/brimhaven_tavern_west.md)), walking into a blocked passage on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) checks that this enemy has been defeated.
- [Fair play?](../quests/brv_blackjack.md#stage-60) with stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_blackjack_dealer_evil)"

    | | |
    |---|---|
    | Entry ID | `brv_blackjack_dealer_evil` |
    | Spawn group | `brv_blackjack_dealer_evil` |
    | Loot table | `brv_dealer` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:130` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_blackjack_dealer_evil",
     "name": "Dealer",
     "iconID": "monsters_ld1:130",
     "maxHP": 30,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "spawnGroup": "brv_blackjack_dealer_evil",
     "droplistID": "brv_dealer",
     "attackCost": 2,
     "attackChance": 80,
     "criticalSkill": 50,
     "criticalMultiplier": 2.0,
     "blockChance": 30,
     "damageResistance": 1
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_dealer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_dealer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_dealer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_blackjack_dealer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
