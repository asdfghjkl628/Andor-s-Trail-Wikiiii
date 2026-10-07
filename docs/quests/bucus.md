# Key of Luthor

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bucus` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 100) |
| **Started by** | [Bucus](../monsters/bucus.md) |
| **NPCs involved** | [Athamyr](../monsters/athamyr.md), [Bucus](../monsters/bucus.md), [Thoronir](../monsters/thoronir.md) |
| **Locations** | [fallhaven_church](../maps/fallhaven_church.md) |
| **Total XP** | 2,850 |
| **Related quests** | 4 |

</div>

## Overview

> Bucus in Fallhaven might know something about Andor. He wants me to bring him the key of Luthor from the catacombs beneath Fallhaven church.

## Prerequisites to start

Start with [Bucus](../monsters/bucus.md). Required:

- reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [scores (hidden flag)](scores.md#stage-18) | stage 18 reached, for stage 20 here |
| Unlocks | [Thief apprentice](Thieves01.md#stage-5) | stage 5 there needs stage 100 here |
| Unlocks | [Search for Andor](andor.md#stage-50) | stage 50 there needs stage 100 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-60) | stage 60 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Bucus in Fallhaven might know something about Andor. He wants me to bring him the key of Luthor from the catacombs beneath Fallhaven church. | [Bucus](../monsters/bucus.md) | – | – |
| <span id="stage-20"></span>20 | The catacombs beneath Fallhaven church are closed off. Athamyr is the only one with both permission and the bravery to enter them. I should go see him in his house southwest of the church. | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | Athamyr wants me to bring him some cooked meat, then maybe he will want to talk more. | [Athamyr](../monsters/athamyr.md) | stage 20 | – |
| <span id="stage-40"></span>40 | I brought some cooked meat to Athamyr. | [Athamyr](../monsters/athamyr.md) | hand over 1× [Cooked meat](../items/meat_cooked.md), stage 20 | 700 XP |
| <span id="stage-50"></span>50 | Athamyr has given me permission to enter the catacombs beneath Fallhaven church.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven church](../maps/fallhaven_church.md).</span> | [Athamyr](../monsters/athamyr.md) | stage 20, stage 40 | – |
| <span id="stage-100"></span>100 | I brought Bucus the key of Luthor. **(completes quest)** | [Bucus](../monsters/bucus.md) | hand over 1× [Key of Luthor](../items/key_luthor.md), stage 10 | 2,150 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Bucus](../monsters/bucus.md) → choose “What was I supposed to do again?” — **conditions:** reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10) → **stage 10**. NPC: “Bring me the key of Luthor and we can talk more. I don't know anything about the key itself, but rumor has it that it…”

???+ note "Stage 20: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “Has anyone entered the catacombs?” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10) → **stage 20**. NPC: “No one is allowed down in the catacombs, except for Athamyr, my apprentice. He is the only one that has been down…”

???+ note "Stage 30: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “How can I get permission to go down there?” — **conditions:** reached stage 20 of [Key of Luthor](../quests/bucus.md#stage-20); NOT reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100) → **stage 30**. NPC: “Bring me some of that delicious cooked meat from the tavern and I will give you my permission to enter the catacombs…”

???+ note "Stage 40: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Here, I have cooked meat for you.” — **conditions:** reached stage 20 of [Key of Luthor](../quests/bucus.md#stage-20); NOT reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); hand over 1× [Cooked meat](../items/meat_cooked.md) → **stage 40**. NPC: “Thanks, this will do nicely.”

???+ note "Stage 50: 1 route"

    1. Talk to [Athamyr](../monsters/athamyr.md) → choose “Have you been down in the catacombs?” — **conditions:** reached stage 20 of [Key of Luthor](../quests/bucus.md#stage-20); NOT reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); reached stage 40 of [Key of Luthor](../quests/bucus.md#stage-40) → **stage 50**. NPC: “You have my permission to enter the catacombs of Fallhaven Church.”

???+ note "Stage 100: 1 route"

    1. Talk to [Bucus](../monsters/bucus.md) → choose “Here, I have it. The key of Luthor.” — **conditions:** reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10); hand over 1× [Key of Luthor](../items/key_luthor.md) → **stage 100**. NPC: “Wow, you actually got the key of Luthor? I didn't think you would make it out of there.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bucus.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bucus` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 100 |
    | Dialogue nodes setting stages | 10: `bucus_thieves_4`, 20: `thoronir_church_4`, 30: `athamyr_4`, 40: `athamyr_complete`, 50: `athamyr_complete_2`, 100: `bucus_thieves_complete_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
