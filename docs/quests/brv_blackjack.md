---
description: "Fair play? is a quest in Andor's Trail, started by Guard (brimhaven_tavern_west). 10 stages, 2,450 XP in total. I heard noices from the back room but I was not allowed to enter because I didn't know the password."
---

# Fair play?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_blackjack` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 70, 80) |
| **Started by** | [Guard](../monsters/guard.md#v-brv_tavern_west_guard) ([Brimhaven tavern west](../maps/brimhaven_tavern_west.md)), walking into a blocked passage on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md) |
| **NPCs involved** | [Dealer](../monsters/brv_blackjack_dealer.md), [Guard](../monsters/guard.md#v-brv_tavern_west_guard), [Zimsko](../monsters/zimsko.md) |
| **Locations** | [Brimhaven tavern west](../maps/brimhaven_tavern_west.md), [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) |
| **Total XP** | 2,450 |
| **Related quests** | 2 |

</div>

## Overview

> I heard noices from the back room but I was not allowed to enter because I didn't know the password.

## Prerequisites to start

**Route 1** ([Guard](../monsters/guard.md#v-brv_tavern_west_guard) ([Brimhaven tavern west](../maps/brimhaven_tavern_west.md))):

- reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20)

**Route 2** ([Guard](../monsters/guard.md#v-brv_tavern_west_guard) ([Brimhaven tavern west](../maps/brimhaven_tavern_west.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-110) | stage 110 reached, for stages 20, 30, 31, 70, 80 here |
| Requires | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-140) | stage 140 reached, for stages 70, 80 here |
| Requires | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 reached, for stage 60 here |
| Unlocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 there needs stages 40, 50, 60 here |
| Blocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-1) | reaching stage 50 here closes stage 1 there |
| Blocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-10) | reaching stage 50 here closes stage 10 there |
| Blocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-20) | reaching stage 50 here closes stage 20 there |
| Blocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-30) | reaching stage 50 here closes stage 30 there |
| Blocks | [Brimhaven blackjack story flags (hidden flag)](brv_blackjack_hidden.md#stage-140) | reaching stage 50 here closes stage 140 there |
| Blocks | [A place to forge](place_to_forge.md#stage-45) | reaching stage 50 here closes stage 45 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I heard noices from the back room but I was not allowed to enter… ▸</span><span class="l">▴ less</span></summary>I heard noices from the back room but I was not allowed to enter because I didn't know the password.</details> | [Guard](../monsters/guard.md#v-brv_tavern_west_guard) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">Zimsko told me about gambling in the back room and that he lost a… ▸</span><span class="l">▴ less</span></summary>Zimsko told me about gambling in the back room and that he lost a lot of money. He thinks that they are cheating.</details> | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I told Zimsko that I want to find out more about the gambling and he… ▸</span><span class="l">▴ less</span></summary>I told Zimsko that I want to find out more about the gambling and he told me the password to access the back room.</details> | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-31"></span>[31](#route-31) | <details class="jt"><summary><span class="s">I have to win and lose a few times until they trust me and play for… ▸</span><span class="l">▴ less</span></summary>I have to win and lose a few times until they trust me and play for higher amounts. Then they start cheating.</details> | [Zimsko](../monsters/zimsko.md) | – |
| <span id="stage-40"></span>[40](#route-40) | With the password, I was allowed to enter the back room. | [Guard](../monsters/guard.md#v-brv_tavern_west_guard) | 300 XP |
| <span id="stage-45"></span>[45](#route-45) | They trust me and now and are playing for higher amounts. | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | 500 XP |
| <span id="stage-50"></span>[50](#route-50) | After I accused the dealer of cheating, a tavern brawl started.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md), stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md) | removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">All the people involved in the tavern brawl survived, but I am no… ▸</span><span class="l">▴ less</span></summary>All the people involved in the tavern brawl survived, but I am no longer allowed to enter the back room.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span> | stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md), [Guard](../monsters/guard.md#v-brv_tavern_west_guard) | – |
| <span id="stage-70"></span>[70](#route-70) | I told Zimsko that I believe the gamblers are cheating. **(ends quest)** | [Zimsko](../monsters/zimsko.md) | 500 XP |
| <span id="stage-80"></span>[80](#route-80) | I told Zimsko that I believe the gamblers are not cheating. **(ends quest)** | [Zimsko](../monsters/zimsko.md) | 1,150 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Guard · 2 ways"

    **Way 1:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), automatic

    - **Needs:** stage 20
    - *“[You hear noises from the back room...] Stop! Tell me the password, if you want to enter.”*

    **Way 2:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), automatic



<span id="route-20"></span>

??? note "Stage 20 · Zimsko · 1 way"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “Do you know something about the back room?”

    - **Needs:** stage 10, 70; not yet stage 20; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“I lost all my money gambling in the backroom. I think they are cheating.”*


<span id="route-30"></span>

??? note "Stage 30 · Zimsko · 2 ways"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “I want to find out what's happening in the back room.”

    - **Needs:** stage 20, 70; not yet stage 10, 30; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“Thanks for trying to find out more. But you will need a password for entering the back room. [He whispers the password in your ear.] You…”*

    **Way 2:** Talk to [Zimsko](../monsters/zimsko.md), choose “I want to find out what's happening in the back room, but they want a password.”

    - **Needs:** stage 10, 20, 70; not yet stage 30; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“Thanks for trying to find out more. The password for entering the back room is... [he whispers the password in your ear.] You have to win…”*


<span id="route-31"></span>

??? note "Stage 31 · Zimsko · 2 ways"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “I want to find out what's happening in the back room.”

    - **Needs:** stage 20, 70; not yet stage 10, 30; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“Thanks for trying to find out more. But you will need a password for entering the back room. [He whispers the password in your ear.] You…”*

    **Way 2:** Talk to [Zimsko](../monsters/zimsko.md), choose “I want to find out what's happening in the back room, but they want a password.”

    - **Needs:** stage 10, 20, 70; not yet stage 30; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“Thanks for trying to find out more. The password for entering the back room is... [he whispers the password in your ear.] You have to win…”*


<span id="route-40"></span>

??? note "Stage 40 · Guard · 1 way"

    **Way 1:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), automatic

    - **Needs:** stage 40
    - <small>Also: sets stage 150 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150)</small>
    - *“I wish you good luck. [Laughs]”*


<span id="route-45"></span>

??? note "Stage 45 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “Yes”

    - **Needs:** not yet stage 45; faction “brv_blackjack_won” ≥ 3
    - *“Now let's stop this child's game and play for higher amounts.”*

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “Yes”

    - **Needs:** not yet stage 45, 50; faction “brv_blackjack_won” ≥ 3
    - *“Now let's stop this child's game and play for higher amounts.”*


<span id="route-50"></span>

??? note "Stage 50 · Dealer, stepping on a trigger on brimhaven_tavern_west_back · 2 ways"

    **Way 1:** Talk to [Dealer](../monsters/brv_blackjack_dealer.md), choose “Let's fight it out. [Killing him in town is a bad idea. I will try to only knock him out.]”

    - **Needs:** not yet stage 70, 80; pay 1 gold; random chance (12%); random chance (8%); faction “brv_blackjack_won” ≥ 3
    - **Gives:** removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back
    - *“Let us start the tavern brawl!”*

    **Way 2:** Stepping on a trigger on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md), choose “Let's fight it out. [Killing him in town is a bad idea. I will try to only knock him out.]”

    - **Needs:** not yet stage 50, 70, 80; pay 1 gold; random chance (12%); random chance (8%); faction “brv_blackjack_won” ≥ 3
    - **Gives:** removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back
    - *“Let us start the tavern brawl!”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on brimhaven_tavern_west, Guard · 2 ways"

    **Way 1:** Stepping on a trigger on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md)

    - **Needs:** stage 50; reached stage 150 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler2_evil); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler1_evil); killed 1× [Dealer](../monsters/brv_blackjack_dealer.md#v-brv_blackjack_dealer_evil)
    - <small>Also: clears stage 150 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150)</small>
    - *“I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.”*

    **Way 2:** Talk to [Guard](../monsters/guard.md#v-brv_tavern_west_guard), automatic

    - **Needs:** stage 50; killed 1× [Dealer](../monsters/brv_blackjack_dealer.md#v-brv_blackjack_dealer_evil); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler1_evil)
    - <small>Also: clears stage 150 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150)</small>
    - *“I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.”*


<span id="route-70"></span>

??? note "Stage 70 · Zimsko · 2 ways"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “I gambled with them and it seems they are cheating.”

    - **Needs:** stage 30; not yet stage 50; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 140 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140)
    - *“Thats what I thought. Thank you for your help.”*

    **Way 2:** Talk to [Zimsko](../monsters/zimsko.md), choose “I gambled with them and it seems they are cheating. I even had a fight with them.”

    - **Needs:** stage 30, 50; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110)
    - *“That's what I thought. Thank you for your help and the fight. Someone had to do it.”*


<span id="route-80"></span>

??? note "Stage 80 · Zimsko · 1 way"

    **Way 1:** Talk to [Zimsko](../monsters/zimsko.md), choose “I gambled with them and I think they are playing fair.”

    - **Needs:** stage 30; not yet stage 50; reached stage 110 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 140 of [Brimhaven blackjack story flags (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140)
    - *“I still believe they are cheating. Thanks anyway.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 12 lines added |
| [v0.7.13](../versions/0.7.13.md) | Stage 45 journal text changed<br>Stage 50 journal text changed<br>Stage 70 XP 1000 → 500<br>Stage 80 XP 800 → 1150<br>Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_blackjack` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 31, 40, 45, 50, 60, 70, 80 |
    | Dialogue nodes setting stages | 10: `brv_tavern_west_guard_10`, 10: `brv_tavern_west_backroom_6`, 20: `brv_zimsko_30`, 30: `brv_zimsko_30_1`, 30: `brv_zimsko_30_2`, 31: `brv_zimsko_30_1`, 31: `brv_zimsko_30_2`, 40: `brv_tavern_west_guard_20`, 45: `blackjack_play_higher_amounts`, 50: `blackjack_dealer_40_2`, 60: `brv_tavern_west_guard_90`, 70: `brv_zimsko_40_2`, 70: `brv_zimsko_40_3`, 80: `brv_zimsko_40_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
