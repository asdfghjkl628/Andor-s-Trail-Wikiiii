# Trusting an outsider

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `vilegard` |
| **In journal** | Yes |
| **Stages** | 3 (completes at 30) |
| **Started by** | [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)), [Tharwyn](../monsters/tharwyn.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) |
| **NPCs involved** | [Grumpy Vilegard villager](../monsters/grumpy_vilegard_villager.md), [Jolnor](../monsters/jolnor.md), [Kaori](../monsters/kaori.md), [Tharwyn](../monsters/tharwyn.md), [Vilegard armorer](../monsters/vilegard_armorer.md), [Vilegard smith](../monsters/vilegard_smith.md) +1 |
| **Locations** | [vilegard_armorer](../maps/vilegard_armorer.md), [vilegard_chapel](../maps/vilegard_chapel.md), [vilegard_kaori](../maps/vilegard_kaori.md), [vilegard_n](../maps/vilegard_n.md) |
| **Total XP** | 2,100 |
| **Related quests** | 6 |

</div>

## Overview

> The people of Vilegard are very suspicious of outsiders. I was told to go see Jolnor in the Vilegard chapel if I want to gain their trust.

## Prerequisites to start

None: talk to [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) to begin.

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Spies in the foam](jolnor.md#stage-30) | stage 30 reached, for stage 30 here |
| Requires | [Kaori's errands](kaori.md#stage-20) | stage 20 reached, for stage 30 here |
| Requires | [Uncertain cause](wrye.md#stage-90) | stage 90 reached, for stage 30 here |
| Unlocks | [Beer Bootlegging](beer_bootlegging.md#stage-30) | stage 30 there needs stage 30 here |
| Unlocks | [Spies in the foam](jolnor.md#stage-10) | stage 10 there needs stage 10 here |
| Unlocks | [Spies in the foam](jolnor.md#stage-30) | stage 30 there needs stage 20 here |
| Unlocks | [Kaori's errands](kaori.md#stage-5) | stage 5 there needs stage 10 here |
| Unlocks | [Shadows](shadows.md#stage-110) | stage 110 there needs stage 30 here |
| Unlocks | [Shadows](shadows.md#stage-120) | stage 120 there needs stage 30 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-32) | stage 32 there needs stage 30 here |
| Unlocks | [Uncertain cause](wrye.md#stage-10) | stage 10 there needs stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | The people of Vilegard are very suspicious of outsiders. I was told to go see Jolnor in the Vilegard chapel if I want to gain their trust. | [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md))<br>[Tharwyn](../monsters/tharwyn.md) ([vilegard_tavern](../maps/vilegard_tavern.md))<br>[Vilegard armorer](../monsters/vilegard_armorer.md) ([vilegard_armorer](../maps/vilegard_armorer.md))<br>+3 more | – | – |
| <span id="stage-20"></span>20 | I have talked to Jolnor in the Vilegard chapel. He suggests I help three influential people in order to gain the trust of the people in Vilegard. I should help Kaori, Wrye and Jolnor in Vilegard. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | – | – |
| <span id="stage-30"></span>30 | I have helped all three people in Vilegard that Jolnor suggested. Now the people of Vilegard should trust me more. **(completes quest)** | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | stage 20 | 2,100 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 6 routes"

    1. Talk to [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) → choose “Why is everyone in Vilegard so afraid of outsiders?” → **stage 10**. NPC: “I don't want to talk to you. Go talk to Jolnor in the chapel if you want to help us.”
    2. Talk to [Tharwyn](../monsters/tharwyn.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) → choose “Why is everyone in Vilegard so suspicious of outsiders?” → **stage 10**. NPC: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.”
    3. Talk to [Vilegard armorer](../monsters/vilegard_armorer.md) ([vilegard_armorer](../maps/vilegard_armorer.md)) → choose “Why is everyone in Vilegard so suspicious of outsiders?” → **stage 10**. NPC: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.”
    4. Talk to [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) → choose “Why is everyone in Vilegard so suspicious of outsiders?” → **stage 10**. NPC: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.”
    5. Talk to [Grumpy Vilegard villager](../monsters/grumpy_vilegard_villager.md) ([vilegard_n](../maps/vilegard_n.md)) → choose “Why is everyone in Vilegard so afraid of outsiders?” → **stage 10**. NPC: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.”
    6. Talk to [Vilegard woman](../monsters/vilegard_woman.md) ([vilegard_s](../maps/vilegard_s.md)) → choose “Why is everyone in Vilegard so afraid of outsiders?” → **stage 10**. NPC: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.”

???+ note "Stage 20: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “No, but I am working on it.” — **conditions:** reached stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20) → **stage 20**. NPC: “So, in order to gain our trust here in Vilegard, I would suggest you help Kaori, Wrye and me.”

???+ note "Stage 30: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “I have done all the tasks you asked me to do.” — **conditions:** reached stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20); reached stage 30 of [Spies in the foam](../quests/jolnor.md#stage-30); reached stage 20 of [Kaori's errands](../quests/kaori.md#stage-20); reached stage 90 of [Uncertain cause](../quests/wrye.md#stage-90) → **stage 30**. NPC: “Good. You helped all three of us.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vilegard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vilegard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vilegard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vilegard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=vilegard.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `vilegard` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30 |
    | Dialogue nodes setting stages | 10: `kaori_2`, 10: `vilegard_shop_notrust_2`, 10: `vilegard_villager_5_1`, 20: `jolnor_gaintrust_15`, 30: `jolnor_quests_completed` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
