# Missing pieces

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `vacor` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 60, 61) |
| **Started by** | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) |
| **NPCs involved** | [Unzel](../monsters/unzel.md), [Vacor](../monsters/vacor.md) |
| **Locations** | [fallhaven_sw](../maps/fallhaven_sw.md), [wild6](../maps/wild6.md) |
| **Total XP** | 4,400 |
| **Related quests** | 1 |

</div>

## Overview

> A mage called Vacor in southwest Fallhaven has been trying to cast a rift spell. There was something not right about him, he seemed very obsessed with his spell. Something about him gaining a power from it.

## Prerequisites to start

Start with [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)). Required:

- reached stage 20 of [Missing pieces](../quests/vacor.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Old friends?](kaverin.md#stage-30) | stage 30 there needs stage 61 here |
| Unlocks | [Old friends?](kaverin.md#stage-70) | stage 70 there needs stage 60 here |
| Unlocks | [Old friends?](kaverin.md#stage-75) | stage 75 there needs stage 60 here |
| Unlocks | [Old friends?](kaverin.md#stage-90) | stage 90 there needs stage 60 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | A mage called Vacor in southwest Fallhaven has been trying to cast a rift spell. There was something not right about him, he seemed very obsessed with his spell. Something about him gaining a power from it. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 20 | – |
| <span id="stage-20"></span>20 | Vacor wants me to bring him the four pieces of the rift spell that he claims was stolen from him. The four bandits should be somewhere south of Fallhaven. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | – | – |
| <span id="stage-30"></span>30 | I have brought the four pieces of the rift spell to Vacor. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | hand over 4× [Piece of Vacor's spell](../items/vacor_spell.md), stage 20 | 1,200 XP |
| <span id="stage-40"></span>40 | Vacor tells me about his former apprentice Unzel, who had started to question Vacor. Vacor now wants me to kill Unzel. I should be able to find him to the southwest outside of Fallhaven. I should bring his signet ring to Vacor once I have killed him. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | – | – |
| <span id="stage-50"></span>50 | Unzel gives me a choice to side with either Vacor or him. | [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) | stage 40 | – |
| <span id="stage-51"></span>51 | I have chosen to side with Unzel. I should go to southwest Fallhaven to talk to Vacor about Unzel and the Shadow. | [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) | stage 40, stage 50 | – |
| <span id="stage-53"></span>53 | I started a fight with Unzel. I should bring his ring to Vacor once he is dead. | [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) | stage 40 | – |
| <span id="stage-54"></span>54 | I started a fight with Vacor. I should bring his ring to Unzel once he is dead. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 40, stage 51 | – |
| <span id="stage-60"></span>60 | I have killed Unzel and told Vacor about the deed. **(completes quest)** | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | hand over 1× [Unzel's ring](../items/ring_unzel.md), stage 40 | 1,600 XP |
| <span id="stage-61"></span>61 | I have killed Vacor and told Unzel about the deed. **(completes quest)** | [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) | hand over 1× [Vacor's ring](../items/ring_vacor.md), stage 51 | 1,600 XP<br>gives [Gold coins](../items/gold.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Could you tell me the whole story again?” — **conditions:** reached stage 20 of [Missing pieces](../quests/vacor.md#stage-20) → **stage 10**. NPC: “Oh, the power I could have had. My dear rift spell.”

???+ note "Stage 20: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 20 of [Missing pieces](../quests/vacor.md#stage-20) → **stage 20**. NPC: “OK, find the four pieces of my rift spell that the bandits took, and bring the pieces to me.”

???+ note "Stage 30: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “I have found all the pieces.” — **conditions:** reached stage 20 of [Missing pieces](../quests/vacor.md#stage-20); hand over 4× [Piece of Vacor's spell](../items/vacor_spell.md) → **stage 30**. NPC: “Oh, you found all four pieces? Hurry, give them to me.”

???+ note "Stage 40: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Could you tell me the story again?” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40) → **stage 40**. NPC: “I need you to find Unzel and kill him for me. He can probably be found somewhere southwest of Fallhaven.”

???+ note "Stage 50: 1 route"

    1. Talk to [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) → choose “I will listen to your story.” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40); reached stage 50 of [Missing pieces](../quests/vacor.md#stage-50) → **stage 50**. NPC: “Either you side with Vacor and his rift spell, or side with the Shadow, and help me get rid of him. Who will you help?”

???+ note "Stage 51: 1 route"

    1. Talk to [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) → choose “I will side with you. The Shadow must not be disturbed.” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40); reached stage 50 of [Missing pieces](../quests/vacor.md#stage-50) → **stage 51**. NPC: “Thank you my friend. We will keep the Shadow safe from Vacor.”

???+ note "Stage 53: 1 route"

    1. Talk to [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) → choose “Hah, I will enjoy killing you!” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40) → **stage 53**. NPC: “Very well, let's fight then.”

???+ note "Stage 54: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “No. You must be stopped.” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40); reached stage 51 of [Missing pieces](../quests/vacor.md#stage-51) → **stage 54**. NPC: “Bah, lowly creature. I knew I shouldn't have trusted you. Now you will die along with your precious Shadow.”

???+ note "Stage 60: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “I have dealt with him. Here is his ring.” — **conditions:** reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40); hand over 1× [Unzel's ring](../items/ring_unzel.md) → **stage 60**. NPC: “Ha ha, Unzel is dead! That pathetic creature is gone!”

???+ note "Stage 61: 1 route"

    1. Talk to [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) → choose “Yes, I have dealt with him.” — **conditions:** reached stage 51 of [Missing pieces](../quests/vacor.md#stage-51); hand over 1× [Vacor's ring](../items/ring_vacor.md) → **stage 61**; also gives [Gold coins](../items/gold.md). NPC: “You killed him? You have my thanks friend. Now we are safe from Vacor's rift spell. Here, take these coins for your…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Ok, find the four pieces of my rift spell that the bandits took, and …” → “OK, find the four pieces of my rift spell that the bandits took, and …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vacor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vacor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vacor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vacor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vacor.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `vacor` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 51, 53, 54, 60, 61 |
    | Dialogue nodes setting stages | 10: `vacor_11`, 20: `vacor_18`, 30: `vacor_40`, 40: `vacor_49`, 50: `unzel_19`, 51: `unzel_20`, 53: `unzel_fight`, 54: `vacor_72`, 60: `vacor_60`, 61: `unzel_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
