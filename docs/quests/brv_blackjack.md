# Fair play?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_blackjack` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 70, 80) |
| **Started by** | [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)), walking into a blocked passage on [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md) |
| **NPCs involved** | [Dealer](../monsters/brv_blackjack_dealer.md), [Guard](../monsters/brv_tavern_west_guard.md), [Zimsko](../monsters/zimsko.md) |
| **Locations** | [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md), [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) |
| **Total XP** | 2,450 |
| **Related quests** | 2 |

</div>

## Overview

> I heard noices from the back room but I was not allowed to enter because I didn't know the password.

## Prerequisites to start

**Route 1** ([Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md))):

- reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20)

**Route 2** ([Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-110) | stage 110 reached, for stages 20, 30, 31, 70, 80 here |
| Requires | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-140) | stage 140 reached, for stages 70, 80 here |
| Requires | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 reached, for stage 60 here |
| Unlocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-150) | stage 150 there needs stages 40, 50, 60 here |
| Blocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-1) | reaching stage 50 here closes stage 1 there |
| Blocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-10) | reaching stage 50 here closes stage 10 there |
| Blocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-20) | reaching stage 50 here closes stage 20 there |
| Blocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-30) | reaching stage 50 here closes stage 30 there |
| Blocks | [brv_blackjack_hidden (hidden flag)](brv_blackjack_hidden.md#stage-140) | reaching stage 50 here closes stage 140 there |
| Blocks | [A place to forge](place_to_forge.md#stage-45) | reaching stage 50 here closes stage 45 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I heard noices from the back room but I was not allowed to enter because I didn't know the password. | [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 20 | – |
| <span id="stage-20"></span>20 | Zimsko told me about gambling in the back room and that he lost a lot of money. He thinks that they are cheating. | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 10, stage 70 | – |
| <span id="stage-30"></span>30 | I told Zimsko that I want to find out more about the gambling and he told me the password to access the back room. | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 10, stage 20, stage 70 | – |
| <span id="stage-31"></span>31 | I have to win and lose a few times until they trust me and play for higher amounts. Then they start cheating. | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 10, stage 20, stage 70 | – |
| <span id="stage-40"></span>40 | With the password, I was allowed to enter the back room. | [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | – | 300 XP<br>sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150) |
| <span id="stage-45"></span>45 | They trust me and now and are playing for higher amounts. | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | – | 500 XP |
| <span id="stage-50"></span>50 | After I accused the dealer of cheating, a tavern brawl started.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west back](../maps/brimhaven_tavern_west_back.md).</span> | [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md))<br>stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) | pay 1 gold | removes monsters from brimhaven_tavern_west_back<br>spawns monsters on brimhaven_tavern_west_back |
| <span id="stage-60"></span>60 | All the people involved in the tavern brawl survived, but I am no longer allowed to enter the back room.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven tavern west](../maps/brimhaven_tavern_west.md).</span> | stepping on a trigger on [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)<br>[Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 50 | clears stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150) |
| <span id="stage-70"></span>70 | I told Zimsko that I believe the gamblers are cheating. **(completes quest)** | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 30, stage 50 | 500 XP |
| <span id="stage-80"></span>80 | I told Zimsko that I believe the gamblers are not cheating. **(completes quest)** | [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) | stage 30 | 1,150 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 2 routes"

    1. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20) → **stage 10**. NPC: “[You hear noises from the back room...] Stop! Tell me the password, if you want to enter.”
    2. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically → **stage 10**

???+ note "Stage 20: 1 route"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “Do you know something about the back room?” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20) → **stage 20**. NPC: “I lost all my money gambling in the backroom. I think they are cheating.”

???+ note "Stage 30: 2 routes"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I want to find out what's happening in the back room.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); NOT reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30) → **stage 30**. NPC: “Thanks for trying to find out more. But you will need a password for entering the back room. [He whispers the password…”
    2. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I want to find out what's happening in the back room, but they want a password.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30) → **stage 30**. NPC: “Thanks for trying to find out more. The password for entering the back room is... [he whispers the password in your…”

???+ note "Stage 31: 2 routes"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I want to find out what's happening in the back room.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); NOT reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30) → **stage 31**. NPC: “Thanks for trying to find out more. But you will need a password for entering the back room. [He whispers the password…”
    2. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I want to find out what's happening in the back room, but they want a password.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20); reached stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10); NOT reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30) → **stage 31**. NPC: “Thanks for trying to find out more. The password for entering the back room is... [he whispers the password in your…”

???+ note "Stage 40: 1 route"

    1. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40) → **stage 40**; also sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150). NPC: “I wish you good luck. [Laughs]”

???+ note "Stage 45: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “Yes” — **conditions:** faction “brv_blackjack_won” ≥ 3; NOT reached stage 45 of [Fair play?](../quests/brv_blackjack.md#stage-45) → **stage 45**. NPC: “Now let's stop this child's game and play for higher amounts.”
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “Yes” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); faction “brv_blackjack_won” ≥ 3; NOT reached stage 45 of [Fair play?](../quests/brv_blackjack.md#stage-45) → **stage 45**. NPC: “Now let's stop this child's game and play for higher amounts.”

???+ note "Stage 50: 2 routes"

    1. Talk to [Dealer](../monsters/brv_blackjack_dealer.md) ([brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md)) → choose “Let's fight it out. [Killing him in town is a bad idea. I will try to only knock him out.]” — **conditions:** pay 1 gold; random chance (12%); random chance (8%); NOT reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); NOT reached stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80); faction “brv_blackjack_won” ≥ 3 → **stage 50**; also removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back. NPC: “Let us start the tavern brawl!”
    2. stepping on a trigger on [brimhaven_tavern_west_back](../maps/brimhaven_tavern_west_back.md) → choose “Let's fight it out. [Killing him in town is a bad idea. I will try to only knock him out.]” — **conditions:** NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); pay 1 gold; random chance (12%); random chance (8%); NOT reached stage 70 of [Fair play?](../quests/brv_blackjack.md#stage-70); NOT reached stage 80 of [Fair play?](../quests/brv_blackjack.md#stage-80); faction “brv_blackjack_won” ≥ 3 → **stage 50**; also removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, removes monsters from brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back. NPC: “Let us start the tavern brawl!”

???+ note "Stage 60: 2 routes"

    1. stepping on a trigger on [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md) → the conversation leads here automatically — **conditions:** reached stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150); reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Gambler](../monsters/brv_blackjack_gambler2_evil.md); killed 1× [Gambler](../monsters/brv_blackjack_gambler1_evil.md); killed 1× [Dealer](../monsters/brv_blackjack_dealer_evil.md) → **stage 60**; also clears stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150). NPC: “I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.”
    2. Talk to [Guard](../monsters/brv_tavern_west_guard.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Dealer](../monsters/brv_blackjack_dealer_evil.md); killed 1× [Gambler](../monsters/brv_blackjack_gambler1_evil.md) → **stage 60**; also clears stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150). NPC: “I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.”

???+ note "Stage 70: 2 routes"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I gambled with them and it seems they are cheating.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30); reached stage 140 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140); NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50) → **stage 70**. NPC: “Thats what I thought. Thank you for your help.”
    2. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I gambled with them and it seems they are cheating. I even had a fight with them.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30); reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50) → **stage 70**. NPC: “That's what I thought. Thank you for your help and the fight. Someone had to do it.”

???+ note "Stage 80: 1 route"

    1. Talk to [Zimsko](../monsters/zimsko.md) ([brimhaven_tavern_west](../maps/brimhaven_tavern_west.md)) → choose “I gambled with them and I think they are playing fair.” — **conditions:** reached stage 110 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-110); reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30); reached stage 140 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-140); NOT reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50) → **stage 80**. NPC: “I still believe they are cheating. Thanks anyway.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 12 lines added |
| [v0.7.13](../versions/0.7.13.md) | stage 45 journal text changed; stage 50 journal text changed; stage 70 XP 1000 → 500; stage 80 XP 800 → 1150<br>Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_blackjack.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
