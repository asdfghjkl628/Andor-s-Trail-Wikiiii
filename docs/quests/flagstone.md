---
description: "Ancient secrets is a quest in Andor's Trail, started by Yolgen (stoutford_church). 10 stages, 4,600 XP in total. Yolgen asked me to have a look at what is wrong with Flagstone prison."
---

# Ancient secrets

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `flagstone` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 100) |
| **Started by** | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) |
| **NPCs involved** | [Flagstone sentry](../monsters/flagstone_sentry.md), [Narael](../monsters/narael.md), [Undead warden](../monsters/undead_warden.md), [Winged demon](../monsters/winged_demon.md), [Yolgen](../monsters/yolgen.md) |
| **Locations** | [flagstone0](../maps/flagstone0.md), [flagstone4](../maps/flagstone4.md), [flagstone_upper](../maps/flagstone_upper.md), [stoutford_church](../maps/stoutford_church.md) |
| **Total XP** | 4,600 |
| **Related quests** | 2 |

</div>

## Overview

> Yolgen asked me to have a look at what is wrong with Flagstone prison.

## Prerequisites to start

Start with [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)). Required:

- reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80)
- reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180)
- reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190)
- NOT reached stage 10 of [stoutford_reinforcements (hidden flag)](../quests/stoutford_reinforcements.md#stage-10)
- reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10)
- NOT reached stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5)
- NOT reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60)
- NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-180) | stage 180 reached, for stage 5 here |
| Requires | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-190) | stage 190 reached, for stage 5 here |
| Requires | [Rumblings](rumblings.md#stage-80) | stage 80 reached, for stages 5, 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | Yolgen asked me to have a look at what is wrong with Flagstone prison. | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-10"></span>10 | I met a guard from Stoutford on sentry duty outside a fortress called Flagstone. He told me that Flagstone used to serve as a prison for house Gorland of Stoutford, but it is now abandoned. Recently, undead have started pouring out of Flagstone. I should investigate the source of the undead monsters. The guard tells me to return to him if I need help. | [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) | – | – |
| <span id="stage-20"></span>20 | I found a dug out tunnel beneath Flagstone, that seems to lead to a larger cave. The cave is guarded by a demon that I am not even able to approach. Maybe the guard outside Flagstone knows more? | reading a sign on [flagstone2](../maps/flagstone2.md) | – | – |
| <span id="stage-30"></span>30 | The guard suggested that the former warden may have something to do with this, and I should go and look for him. If I find him I should return to the guard with any important news. | [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) | stage 10, stage 20 | – |
| <span id="stage-31"></span>31 | I found the former warden of Flagstone on the upper level. Among his remains I found a necklace with some inscriptions. I should return to the guard now. | [Undead warden](../monsters/undead_warden.md) ([flagstone_upper](../maps/flagstone_upper.md)) | – | – |
| <span id="stage-40"></span>40 | I have learned the words required to approach the demon beneath Flagstone. 'Daylight Shadow'. It seems like the warden has something to do with the monster invasion.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Flagstone2](../maps/flagstone2.md).</span> | [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) | hand over 1× [Flagstone Warden's necklace](../items/necklace_flagstone.md), stage 30 | 1,600 XP |
| <span id="stage-50"></span>50 | Deep beneath Flagstone, I found a powerful winged demon. It seems like the warden kept on running the prison and experimented with necromancy. | [Winged demon](../monsters/winged_demon.md) ([flagstone4](../maps/flagstone4.md)) | – | – |
| <span id="stage-60"></span>60 | I found one prisoner, Narael, alive deep beneath Flagstone. Narael was once a citizen of Nor City. He is too weak to walk by himself, but if I can find his wife in Nor City, I would be handsomely rewarded. | [Narael](../monsters/narael.md) ([flagstone4](../maps/flagstone4.md)) | – | – |
| <span id="stage-70"></span>70 | I approached the sentry again and he was happy to hear the source of the undead is gone. I should talk to Yolgen, the priest of Stoutford, for a reward. | [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) | stage 60 | removes monsters from flagstone4 |
| <span id="stage-100"></span>100 | Yolgen rewarded me handsomely for my efforts and is happy that there is one thing less the citizens of Stoutford have to worry about. **(completes quest)** | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | stage 60 | 3,000 XP<br>removes monsters from flagstone4<br>gives [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “What about Flagstone prison?” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190); NOT reached stage 10 of [stoutford_reinforcements (hidden flag)](../quests/stoutford_reinforcements.md#stage-10); reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10); NOT reached stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5); NOT reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60); NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100) → **stage 5**. NPC: “If you could help with Flagstone, it would take a big burden off us.”

???+ note "Stage 10: 1 route"

    1. Talk to [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) → choose “Can I investigate the Flagstone ruins?” — **conditions:** reached stage 10 of [Ancient secrets](../quests/flagstone.md#stage-10) → **stage 10**. NPC: “Return here if you need my advice.”

???+ note "Stage 20: 1 route"

    1. reading a sign on [flagstone2](../maps/flagstone2.md) → the conversation leads here automatically → **stage 20**. NPC: “You notice that this tunnel seems to be dug out from below Flagstone. Probably the work of one of the former prisoners…”

???+ note "Stage 30: 1 route"

    1. Talk to [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) → choose “There is a guardian in the lower levels of Flagstone that cannot be approached and the former prisoners are…” — **conditions:** reached stage 10 of [Ancient secrets](../quests/flagstone.md#stage-10); reached stage 20 of [Ancient secrets](../quests/flagstone.md#stage-20) → **stage 30**. NPC: “You should look for the former warden. Maybe he has something to do with all of this. If you find him you should…”

???+ note "Stage 31: 1 route"

    1. Talk to [Undead warden](../monsters/undead_warden.md) ([flagstone_upper](../maps/flagstone_upper.md)) → the conversation leads here automatically → **stage 31**. NPC: “Ah, another mortal. Prepare to become part of my undead army!”

???+ note "Stage 40: 1 route"

    1. Talk to [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) → choose “I slew the former warden and found a peculiar necklace among his remains.” — **conditions:** reached stage 30 of [Ancient secrets](../quests/flagstone.md#stage-30); hand over 1× [Flagstone Warden's necklace](../items/necklace_flagstone.md) → **stage 40**. NPC: “Oh this looks most interesting. Let's take a look. Hmm. It has got some weird inscriptions on it that say 'Daylight…”

???+ note "Stage 50: 1 route"

    1. Talk to [Winged demon](../monsters/winged_demon.md) ([flagstone4](../maps/flagstone4.md)) → the conversation leads here automatically → **stage 50**. NPC: “What, a mortal in here that is not marked by my touch?”

???+ note "Stage 60: 1 route"

    1. Talk to [Narael](../monsters/narael.md) ([flagstone4](../maps/flagstone4.md)) → the conversation leads here automatically → **stage 60**. NPC: “Now leave me to my fate. I do not have the strength to leave this place.”

???+ note "Stage 70: 1 route"

    1. Talk to [Flagstone sentry](../monsters/flagstone_sentry.md) ([flagstone0](../maps/flagstone0.md)) → choose “In the depths of Flagstone, I had to fight a winged demon and found a prisoner called Narael. He told me…” — **conditions:** reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60) → **stage 70**; also removes monsters from flagstone4. NPC: “This is both good and bad news. I am truly grateful that you rid us of the warden and his thralls. Talk to Yolgen for…”

???+ note "Stage 100: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “I cleared Flagstone of an evil demon.” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80); reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60); NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100) → **stage 100**; also removes monsters from flagstone4, gives [Gold coins](../items/gold.md). NPC: “Oh that is good news! I am very pleased that the citizens of Stoutford have one thing less to worry about. It is a…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Stages added: 5, 70, 100<br>Stage 10 journal text changed<br>Stage 30 journal text changed<br>Stage 31 journal text changed<br>Stage 40 journal text changed<br>Stage 50 journal text changed<br>Stage 60 no longer completes the quest<br>Stage 60 XP 2100 → 0<br>Dialogue: 3 lines added, 3 lines changed<br>· text: “Have you found the former warden of Flagstone? The warden used to hav…” → “You should look for the former warden. Maybe he has something to do w…”<br>· text: “If you find the warden and retrieve the necklace, then please return …” → “Oh this looks most interesting. Let's take a look. Hmm. It has got so…” |
| [v0.7.11](../versions/0.7.11.md) | Stage 31 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=flagstone.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=flagstone.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=flagstone.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=flagstone.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=flagstone.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `flagstone` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 30, 31, 40, 50, 60, 70, 100 |
    | Dialogue nodes setting stages | 5: `yolgen_flagstone_0`, 10: `flagstone_sentry_15`, 20: `flagstone_brokensteps`, 30: `flagstone_sentry_21`, 31: `flagstone_guard0`, 40: `flagstone_sentry_23`, 40: `flagstone_sentry_40`, 50: `flagstone_guard2`, 60: `narael_8`, 70: `flagstone_sentry_45`, 100: `yolgen_flagstone_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
