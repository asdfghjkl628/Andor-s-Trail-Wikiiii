---
description: "Stoutford's old castle is a quest in Andor's Trail, started by stepping on a trigger on stoutford_castle0. 11 stages, 6,550 XP in total. I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help..."
---

# Stoutford's old castle

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `stoutford_castle` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 50, 60, 70) |
| **Started by** | stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) |
| **NPCs involved** | [Tahalendor](../monsters/tahalendor.md), [Yolgen](../monsters/yolgen.md) |
| **Locations** | [stoutford_church](../maps/stoutford_church.md) |
| **Total XP** | 6,550 |
| **Related quests** | 3 |

</div>

## Overview

> I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help...

## Prerequisites to start

Start with stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md). Required:

- killed 1× [Lord Erwyn](../monsters/erwyn.md)
- reached stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48)
- NOT reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49)
- killed 2× [Lord Erwyn](../monsters/erwyn.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-180) | stage 180 reached, for stages 10, 12 here |
| Requires | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-190) | stage 190 reached, for stages 10, 12 here |
| Requires | [Rumblings](rumblings.md#stage-80) | stage 80 reached, for stages 10, 12, 20, 30, 42, 50, 60, 70 here |
| Requires | [Rumblings](rumblings.md#stage-106) | stage 106 reached, for stage 14 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-46) | stage 46 reached, for stages 20, 30 here |
| Requires | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-48) | stage 48 reached, for stages 5, 16 here |
| Blocked by | [stn_nondisplay (hidden flag)](stn_nondisplay.md#stage-49) | stage 49 must NOT be reached, for stage 5 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | I tried to free this castle from the undead Lord Erwyn. But whenever I kill him, he reappears. I should seek help...<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) | – | – |
| <span id="stage-10"></span>10 | I talked to Yolgen, the Shadow priest of Stoutford, and he told me that the mighty Lord Erwyn used to reside here, but Lord Erwyn and his army were crushed during a war, the castle was sacked and the house extinguished. But recently Erwyn's knights have risen from the dead. Yolgen asked me to rid Stoutford of these undead once and for all. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-12"></span>12 | I should ask Tahalendor for some special artifact that I can use to defeat powerful undead. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-14"></span>14 | Tahalendor gave me a pair of special coins that I can use to defeat powerful undead. | [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) | pay 2 gold, stage 12 | gives 2× [Gold coins](../items/erwyn_coin.md) |
| <span id="stage-16"></span>16 | I slew Lord Erwyn himself and ensured that he remains dead now.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Stoutford castle0](../maps/stoutford_castle0.md).</span> | stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) | – | 500 XP<br>clears stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48)<br>removes monsters from stoutford_castle0 |
| <span id="stage-20"></span>20 | I slew all the undead knights. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 10 | 2,000 XP |
| <span id="stage-30"></span>30 | I slew Lord Erwyn's commander. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 10 | 1,000 XP |
| <span id="stage-42"></span>42 | Among his remains I found a strange ring. I should show it to Yolgen. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md), stage 10, stage 40 | – |
| <span id="stage-50"></span>50 | Yolgen examined the ring thoroughly. He suspects it has somehow come from Mt. Galmore and reanimated the long dead soldiers. I should be wary of the evil grasp of Mt. Galmore and whatever lurks there... **(completes quest)** | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md), hand over 1× [Lord Erwyn's ring](../items/erwyn_ring.md), stage 10, stage 40 | 2,050 XP |
| <span id="stage-60"></span>60 | I kept the ring for myself, which upset Yolgen. I should keep looking for its previous owner. **(completes quest)** | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 10, stage 40 | 500 XP |
| <span id="stage-70"></span>70 | I kept the ring for myself and didn't tell Yolgen about it. He was suspicious but couldn't do anything about it. I should keep looking for its previous owner. **(completes quest)** | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 10, stage 40 | 500 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** killed 1× [Lord Erwyn](../monsters/erwyn.md); reached stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48); NOT reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49); killed 2× [Lord Erwyn](../monsters/erwyn.md) → **stage 5**. NPC: “I'm not dead, so you can't kill me. Haha. You don't know much about the undead, do you kid? You can't destroy me!”

???+ note "Stage 10: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “No problem. They are already as good as dead.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190); NOT reached stage 10 of [stoutford_reinforcements (hidden flag)](../quests/stoutford_reinforcements.md#stage-10); reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10); NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10) → **stage 10**. NPC: “Before you leave, go to Tahalendor. He might give you something that helps against undead.”

???+ note "Stage 12: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “No problem. They are already as good as dead.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190); NOT reached stage 10 of [stoutford_reinforcements (hidden flag)](../quests/stoutford_reinforcements.md#stage-10); reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10); NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10) → **stage 12**. NPC: “Before you leave, go to Tahalendor. He might give you something that helps against undead.”

???+ note "Stage 14: 1 route"

    1. Talk to [Tahalendor](../monsters/tahalendor.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “OK.” — **conditions:** reached stage 106 of [Rumblings](../quests/rumblings.md#stage-106); reached stage 12 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-12); NOT reached stage 14 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-14); killed 1× [Lord Erwyn](../monsters/erwyn.md); pay 2 gold → **stage 14**; also gives 2× [Gold coins](../items/erwyn_coin.md). NPC: “Here you go. As soon as the undead lord appears to be destroyed, place one coin on each eye. This will prevent him…”

???+ note "Stage 16: 1 route"

    1. stepping on a trigger on [stoutford_castle0](../maps/stoutford_castle0.md) → the conversation leads here automatically — **conditions:** killed 1× [Lord Erwyn](../monsters/erwyn.md#v-erwyn2); reached stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48) → **stage 16**; also clears stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48), removes monsters from stoutford_castle0. NPC: “I followed Tahalendor's advice, and placed one coin in each eye socket. Not long after, Lord Erwyn's remains crumbled…”

???+ note "Stage 20: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “I have dealt with Erwyn's army.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 46 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46) → **stage 20**. NPC: “Let me see... OK, you killed all of the undead knights and soldiers who had worn Lord Erwyn's tattered banner.”

???+ note "Stage 30: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “I have dealt with Erwyn's army.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 46 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46); killed 1× [Karth the Unbowed](../monsters/erwyn_commander.md) → **stage 30**. NPC: “And you slew Lord Erwyn's commander.”

???+ note "Stage 42: 2 routes"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Sure. I found this ring among his remains.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md) → **stage 42**. NPC: “I am very pleased to hear this. A ring you say? Let me take a look.”
    2. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Sure. I found this ring among his remains.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md) → **stage 42**. NPC: “Hmm. This looks most interesting. I suspected something like this. It is certainly some magical item and seems to have…”

???+ note "Stage 50: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Sounds fine to me. Anything for the safety of the people of Stoutford.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40); carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md); hand over 1× [Lord Erwyn's ring](../items/erwyn_ring.md) → **stage 50**. NPC: “That is it. The ring is destroyed. I wonder where it came from. Maybe from the depths of Mt. Galmore, or some…”

???+ note "Stage 60: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “No, I don't think so. I wonder who had owned the ring before Erwyn?” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40) → **stage 60**. NPC: “Do not play with ancient forces that are beyond your power.”

???+ note "Stage 70: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “[Lie] Yes, but I found nothing worth having.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70); reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40) → **stage 70**. NPC: “If you say so. I suspect Lord Erwyn had a ring, and if you find it you must bring it to me. It is dangerous.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.7.11](../versions/0.7.11.md) | stage 12 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=stoutford_castle.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `stoutford_castle` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 12, 14, 16, 20, 30, 42, 50, 60, 70 |
    | Dialogue nodes setting stages | 5: `check_erwyn_2b`, 10: `yolgen_castle_0_1`, 12: `yolgen_castle_0_1`, 14: `tahalendor_erwyn_6`, 16: `check_erwyn_1`, 20: `yolgen_castle_1_1a`, 30: `yolgen_castle_1_2a`, 42: `yolgen_castle_3`, 42: `yolgen_castle_4`, 50: `yolgen_castle_6`, 60: `yolgen_castle_13`, 70: `yolgen_castle_11` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
