---
description: "Disallowed substance is a quest in Andor's Trail, started by Leonid. 7 stages, 1,800 XP in total. Leonid in Crossglen town hall tells me that there was a disturbance in the village some weeks ago. Apparently, Lord Geomyr has banned all use of bonemeal as a healing substance. Tharal, the town prie…"
---

# Disallowed substance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bonemeal` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 100, 110) |
| **Started by** | [Leonid](../monsters/leonid.md) |
| **NPCs involved** | [Leonid](../monsters/leonid.md), [Tharal](../monsters/tharal.md), [Thoronir](../monsters/thoronir.md) |
| **Locations** | [fallhaven_church](../maps/fallhaven_church.md) |
| **Total XP** | 1,800 |
| **Related quests** | 5 |

</div>

## Overview

> Leonid in Crossglen town hall tells me that there was a disturbance in the village some weeks ago. Apparently, Lord Geomyr has banned all use of bonemeal as a healing substance. Tharal, the town priest should know more.

## Prerequisites to start

None: talk to [Leonid](../monsters/leonid.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [scores (hidden flag)](scores.md#stage-18) | stage 18 reached, for stages 40, 50, 100, 110 here |
| Unlocks | [Thief apprentice](Thieves01.md#stage-50) | stage 50 there needs stage 100 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 there needs stage 30 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-2) | stage 2 there needs stage 30 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 there needs stage 30 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-10) | stage 10 there needs stage 30 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-80) | stage 80 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Leonid in Crossglen town hall tells me that there was a disturbance in the village some weeks ago. Apparently, Lord Geomyr has banned all use of bonemeal as a healing substance.  Tharal, the town priest should know more. | [Leonid](../monsters/leonid.md) | – | – |
| <span id="stage-20"></span>20 | Tharal does not want to talk about bonemeal. I might be able to persuade him by bringing him 5 insect wings. | [Tharal](../monsters/tharal.md) | stage 10 | – |
| <span id="stage-30"></span>30 | Tharal tells me that bonemeal is a very potent healing substance, and is quite upset that it is not allowed anymore. I should go see Thoronir in Fallhaven if I want to learn more. I should tell him the password 'Glow of the Shadow'. | [Tharal](../monsters/tharal.md) | hand over 5× [Insect wing](../items/insectwing.md), stage 10 | – |
| <span id="stage-40"></span>40 | I have talked to Thoronir in Fallhaven. He might be able to mix me a bonemeal potion if I bring him 5 skeletal bones. There should be some skeletons in an abandoned house north of Fallhaven. | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | Thoronir in Fallhaven explained to me that bonemeal potions are banned by Lord Geomyr, so I have refused his request to provide him with fresh ingredients for new bonemeal potions. I could do him a favour though to bring him 5 skeletal bones for church matters. There should be some skeletons in an abandoned house north of Fallhaven. | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | stage 30 | – |
| <span id="stage-100"></span>100 | I have brought the bones to Thoronir. He is now able to supply me with bonemeal potions. I should be careful when using them though, since Lord Geomyr has banned their use. **(completes quest)** | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | hand over 5× [Bone](../items/bone.md), stage 30 | 900 XP |
| <span id="stage-110"></span>110 | I have brought the bones to Thoronir. Of course he wouldn't produce any bonemeal potion from them though, since Lord Geomyr has banned their use. **(completes quest)** | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | hand over 5× [Bone](../items/bone.md), stage 30, stage 50 | 900 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Leonid](../monsters/leonid.md) → choose “Has there been any recent activity in the village?” → **stage 10**. NPC: “Lord Geomyr issued a statement regarding the unlawful use of bonemeal as healing substance. Some villagers argued that…”

???+ note "Stage 20: 1 route"

    1. Talk to [Tharal](../monsters/tharal.md) → choose “Oh come on.” — **conditions:** reached stage 10 of [Disallowed substance](../quests/bonemeal.md#stage-10) → **stage 20**. NPC: “Well if you really are that persistent. Bring me 5 insect wings that I can use for making potions and maybe we can…”

???+ note "Stage 30: 1 route"

    1. Talk to [Tharal](../monsters/tharal.md) → choose “Here, I have the insect wings.” — **conditions:** reached stage 10 of [Disallowed substance](../quests/bonemeal.md#stage-10); hand over 5× [Insect wing](../items/insectwing.md) → **stage 30**. NPC: “Thanks kid. I knew I could count on you.”

???+ note "Stage 40: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “Sure, I might be able to do that.” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30) → **stage 40**. NPC: “Thank you, please come back soon. I heard there were some undead near an old abandoned house just north of Fallhaven.…”

???+ note "Stage 50: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “Sure, I might be able to do that.” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); reached stage 50 of [Disallowed substance](../quests/bonemeal.md#stage-50) → **stage 50**. NPC: “Thank you, please come back soon. I heard there were some undead near an old abandoned house just north of Fallhaven.…”

???+ note "Stage 100: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “I have those bones for you.” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); hand over 5× [Bone](../items/bone.md) → **stage 100**. NPC: “Thank you, these bones will do fine. Now I can start creating some bonemeal healing potions for you.”

???+ note "Stage 110: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “I have those bones for you.” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 30 of [Disallowed substance](../quests/bonemeal.md#stage-30); reached stage 50 of [Disallowed substance](../quests/bonemeal.md#stage-50); hand over 5× [Bone](../items/bone.md) → **stage 110**. NPC: “Thank you, these bones will do fine. Now I can start creating some ... things.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Lord Geomyr issued a statement regarding the unlawful use of Bonemeal…” → “Lord Geomyr issued a statement regarding the unlawful use of bonemeal…” |
| [v0.8.16.1](../versions/0.8.16.1.md) | stages added: 50, 110<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bonemeal.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bonemeal.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bonemeal.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bonemeal.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bonemeal.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bonemeal` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 100, 110 |
    | Dialogue nodes setting stages | 10: `leonid_crossglen4`, 20: `tharal_bonemeal2`, 30: `tharal_bonemeal3`, 40: `thoronir_tharal_5`, 50: `thoronir_tharal_5a`, 100: `thoronir_tharal_complete`, 110: `thoronir_tharal_complete_a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
