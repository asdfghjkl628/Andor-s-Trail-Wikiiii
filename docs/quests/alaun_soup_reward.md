# Alaun soup rewards

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `alaun_soup_reward` |
| **In journal** | No (hidden flag) |
| **Stages** | 7 |
| **Started by** | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) |
| **NPCs involved** | [Alaun](../monsters/alaun.md) |
| **Locations** | [fallhaven_alaun](../maps/fallhaven_alaun.md) |
| **Total XP** | 1,350 |
| **Related quests** | 1 |

</div>

## Overview

> 10 gold

## Prerequisites to start

Start with [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)). Required:

- NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Delicious soup](gison_soup.md#stage-10) | stage 10 reached, for stage 30 here |
| Requires | [Delicious soup](gison_soup.md#stage-20) | stage 20 reached, for stages 11, 16, 21 here |
| Requires | [Delicious soup](gison_soup.md#stage-50) | stage 50 reached, for stage 30 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-10) | stage 10 must NOT be reached, for stages 10, 15, 20 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-30) | stage 30 must NOT be reached, for stages 11, 16, 21 here |
| Blocked by | [Delicious soup](gison_soup.md#stage-50) | stage 50 must NOT be reached, for stages 11, 16, 21 here |
| Unlocks | [Delicious soup](gison_soup.md#stage-30) | stage 30 there needs stages 10, 15, 20 here |
| Unlocks | [Delicious soup](gison_soup.md#stage-35) | stage 35 there needs stages 10, 15, 20 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | 10 gold | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-11"></span>11 |  | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | hand over 1× [Gison's mushroom soup](../items/gison_soup.md), stage 10 | 500 XP<br>sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30)<br>gives 10× [Gold coins](../items/gold.md)<br>gives 5× [Bread](../items/bread.md)<br>gives 1× [Empty bottle](../items/bottle_empty.md)<br>sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-15"></span>15 | 15 gold | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-16"></span>16 |  | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | hand over 1× [Gison's mushroom soup](../items/gison_soup.md), stage 15 | 450 XP<br>gives 15× [Gold coins](../items/gold.md)<br>gives 1× [Empty bottle](../items/bottle_empty.md)<br>sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30)<br>sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-20"></span>20 | 20 gold | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) |
| <span id="stage-21"></span>21 |  | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | hand over 1× [Gison's mushroom soup](../items/gison_soup.md), stage 20 | 400 XP<br>sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30)<br>gives 20× [Gold coins](../items/gold.md)<br>gives 1× [Empty bottle](../items/bottle_empty.md)<br>sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35) |
| <span id="stage-30"></span>30 | Failure | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | applies condition fear |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds easy, I'll do it!” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 10**; also sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10). NPC: “That's really nice of you.”

???+ note "Stage 11: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 11**; also sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), gives 10× [Gold coins](../items/gold.md), gives 5× [Bread](../items/bread.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35). NPC: “Here is the money I promised you. And as a bonus I will give you some of this bread. Next time I will buy Nimael's soup.”

???+ note "Stage 15: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds good. I will do it.” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 15**; also sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10). NPC: “That's nice of you.”

???+ note "Stage 16: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 16**; also gives 15× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”

???+ note "Stage 20: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds good. I will do it.” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 20**; also sets stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10). NPC: “OK, please bring it hot!”

???+ note "Stage 21: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 21**; also sets stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30), gives 20× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”

???+ note "Stage 30: 1 route"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “I was not able to bring you the soup.” — **conditions:** latest stage of [Delicious soup](../quests/gison_soup.md#stage-10) is 10; reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50) → **stage 30**; also applies condition fear. NPC: “That can't be. Get out of here! [Alaun starts throwing things at you]”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=alaun_soup_reward.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `alaun_soup_reward` |
    | showInLog | 0 |
    | Stage IDs | 10, 11, 15, 16, 20, 21, 30 |
    | Dialogue nodes setting stages | 10: `alaun_startquest10`, 11: `alaun_return10`, 15: `alaun_startquest15`, 16: `alaun_return15`, 20: `alaun_startquest20`, 21: `alaun_return20`, 30: `alaun_return_fail` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
