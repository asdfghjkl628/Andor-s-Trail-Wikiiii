# Rumblings

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `rumblings` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 100, 103, 106) |
| **Started by** | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)), [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) |
| **NPCs involved** | [Glasforn](../monsters/stoutford_innkeeper.md), [Quiet thief](../monsters/stoutford_thief.md), [Tahalendor](../monsters/tahalendor.md), [Yolgen](../monsters/yolgen.md) |
| **Locations** | [stoutford_church](../maps/stoutford_church.md), [stoutford_tavern](../maps/stoutford_tavern.md) |
| **Total XP** | 7,000 |
| **Related quests** | 7 |

</div>

## Overview

> The priest in Stoutford looks scared of me and of what I did, but we never met before. Can this have something to do with Andor?

## Prerequisites to start

None: talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Night visit](farrik.md#stage-70) | stage 70 reached, for stage 25 here |
| Unlocks | [Search for Andor](andor.md#stage-85) | stage 85 there needs stage 10 here |
| Unlocks | [Search for Andor](andor.md#stage-86) | stage 86 there needs stage 60 here |
| Unlocks | [Ancient secrets](flagstone.md#stage-5) | stage 5 there needs stage 80 here |
| Unlocks | [Ancient secrets](flagstone.md#stage-100) | stage 100 there needs stage 80 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-23) | stage 23 there needs stage 106 here |
| Unlocks | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-180) | stage 180 there needs stage 80 here |
| Unlocks | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-190) | stage 190 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-10) | stage 10 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-12) | stage 12 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-14) | stage 14 there needs stage 106 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-20) | stage 20 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-30) | stage 30 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-42) | stage 42 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-50) | stage 50 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-60) | stage 60 there needs stage 80 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-70) | stage 70 there needs stage 80 here |
| Unlocks | [The thorns of vengeance](thorns_vengeance.md#stage-65) | stage 65 there needs stage 106 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | The priest in Stoutford looks scared of me and of what I did, but we never met before. Can this have something to do with Andor? | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-20"></span>20 | The priest's acolyte, Yolgen, told me that Andor was here a while ago, and since then, scary noises resonate in the church, seemingly coming from underground. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 10 | – |
| <span id="stage-25"></span>25 | A member of the Thieve's Guild in the tavern of Stoutford told me that the tavern owner dealt with Andor. | [Quiet thief](../monsters/stoutford_thief.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | stage 20 | – |
| <span id="stage-30"></span>30 | Glasforn, the owner of the tavern of Stoutford, admits to knowing Andor, but evades all my questions by boasting about his beds' quality.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Stoutford tavern](../maps/stoutford_tavern.md).</span> | [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | stage 20 | – |
| <span id="stage-50"></span>50 | After sleeping in Glasforn's bed, I woke up in a cave, and was attacked by a monster. I killed it, but I should go see Glasforn again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford cellar2](../maps/stoutford_cellar2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Stoutford cellar2](../maps/stoutford_cellar2.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Stoutford cellar](../maps/stoutford_cellar.md).</span> | stepping on a trigger on [stoutford_cellar2](../maps/stoutford_cellar2.md) | – | changes map stoutford_tavern |
| <span id="stage-60"></span>60 | When Glasforn saw me, he was really scared. Hopefully I'll get some information from him. | [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | – | – |
| <span id="stage-70"></span>70 | I confronted Glasforn. He admited everything, but blamed Andor for it. How can Andor be involved in this? | [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) | stage 60 | gives 1× [Necklace of the Undead](../items/necklace_undead.md) |
| <span id="stage-80"></span>80 | Yolgen told me the rumbles have stopped. I should talk to the priest. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 50 | – |
| <span id="stage-85"></span>85 | The priest told me the monster was a lich. I should keep its heart safe. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-90"></span>90 | The priest thanked me for saving his church and asked who the culprit was. | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | carry 1× [Demon heart](../items/eliszylae_heart.md), stage 80 | gives [Green apple](../items/apple_green.md), [Bread](../items/bread.md), [Major potion of health](../items/health_major2.md) |
| <span id="stage-100"></span>100 | I told him I do not know who was responsible. **(completes quest)** | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 90 | 2,000 XP |
| <span id="stage-103"></span>103 | I told him Glasforn was responsible. **(completes quest)** | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 70, stage 90 | 2,500 XP<br>removes monsters from stoutford_tavern |
| <span id="stage-106"></span>106 | I told him Andor was responsible. **(completes quest)** | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 70, stage 90 | 2,500 XP |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 2 routes"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “What?” → **stage 10**. NPC: “Go away! You're not welcome here!”
    2. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Actually, it's the first time we have met.” → **stage 10**. NPC: “Nonsense! Go away!”

???+ note "Stage 20: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “That must be my brother Andor!” — **conditions:** reached stage 10 of [Rumblings](../quests/rumblings.md#stage-10) → **stage 20**. NPC: “This church is the refuge for all the villagers when monsters attack. We are really worried now.”

???+ note "Stage 25: 1 route"

    1. Talk to [Quiet thief](../monsters/stoutford_thief.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “Help me do what?” — **conditions:** reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20); reached stage 70 of [Night visit](../quests/farrik.md#stage-70) → **stage 25**. NPC: “A kid that looked like you was here. He apparently did some business with the owner and the regulars.”

???+ note "Stage 30: 1 route"

    1. Talk to [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “Why?” — **conditions:** reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20) → **stage 30**. NPC: “Well, you see, I keep some beds for occasions like this one. You can use the one in the corner, near the painting, if…”

???+ note "Stage 50: 1 route"

    1. stepping on a trigger on [stoutford_cellar2](../maps/stoutford_cellar2.md) → the conversation leads here automatically — **conditions:** killed 1× [Eliszylae](../monsters/stoutford_lich.md); NOT reached stage 50 of [Rumblings](../quests/rumblings.md#stage-50) → **stage 50**; also changes map stoutford_tavern. NPC: “You hear a loud rumble, then nothing. Silence. What was that monster?”

???+ note "Stage 60: 1 route"

    1. Talk to [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Rumblings](../quests/rumblings.md#stage-60) → **stage 60**. NPC: “Wait. OK. I stand no chance against you. I'll tell you all I know.”

???+ note "Stage 70: 1 route"

    1. Talk to [Glasforn](../monsters/stoutford_innkeeper.md) ([stoutford_tavern](../maps/stoutford_tavern.md)) → choose “I guess you are lucky I visited, although just asking me to kill it would have been easier. And nicer.” — **conditions:** reached stage 60 of [Rumblings](../quests/rumblings.md#stage-60) → **stage 70**; also gives 1× [Necklace of the Undead](../items/necklace_undead.md). NPC: “I'm sorry! How was I to know you could actually kill it? You're just a kid! Anyway, now I can remove the necklace.…”

???+ note "Stage 80: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Yes. I think I found the cause.” — **conditions:** reached stage 50 of [Rumblings](../quests/rumblings.md#stage-50) → **stage 80**. NPC: “Great. You should talk to my master. I told him you were not who he thought you were.”

???+ note "Stage 90: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “These? You mean there are others?” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); carry 1× [Demon heart](../items/eliszylae_heart.md) → **stage 90**; also gives [Green apple](../items/apple_green.md), [Bread](../items/bread.md), [Major potion of health](../items/health_major2.md). NPC: “You know, since those monsters' attacks, we don't have much to offer, but take these. By the way, do you have any idea…”

???+ note "Stage 100: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Not really.” — **conditions:** reached stage 90 of [Rumblings](../quests/rumblings.md#stage-90) → **stage 100**. NPC: “It's a shame we cannot punish the culprits. Thank you for your help kid.”

???+ note "Stage 103: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “It was all Glasforn's doing. The tavern owner.” — **conditions:** reached stage 90 of [Rumblings](../quests/rumblings.md#stage-90); reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70) → **stage 103**; also removes monsters from stoutford_tavern. NPC: “That fool! We'll make him pay. Thank you for your help kid.”

???+ note "Stage 106: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “It was my brother Andor. I need to find him.” — **conditions:** reached stage 90 of [Rumblings](../quests/rumblings.md#stage-90); reached stage 70 of [Rumblings](../quests/rumblings.md#stage-70) → **stage 106**. NPC: “That is troublesome. I have no idea where he went when he left Stoutford, but Kazaul has always been linked to the…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rumblings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rumblings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rumblings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rumblings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=rumblings.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `rumblings` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 25, 30, 50, 60, 70, 80, 85, 90, 100, 103, 106 |
    | Dialogue nodes setting stages | 10: `tahalendor_initial_1`, 10: `tahalendor_initial_2`, 20: `yolgen_rumblings10_5`, 25: `stoutford_thief_rumblings20_2`, 30: `glasforn_rumblings20_3`, 50: `stoutford_lich_killed_1`, 60: `glasforn_rumblings60_0`, 70: `glasforn_rumblings60_6`, 80: `yolgen_rumblings50_1`, 90: `tahalendor_rumblings80_5`, 100: `tahalendor_rumblings100_0`, 103: `tahalendor_rumblings103_0`, 106: `tahalendor_rumblings106_0` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
