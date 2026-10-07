---
description: "Kaori's errands is a quest in Andor's Trail, started by Jolnor (vilegard_chapel). 3 stages, 520 XP in total. Jolnor in Vilegard chapel wants me to talk to Kaori in northern Vilegard, to see if she wants any help."
---

# Kaori's errands

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `kaori` |
| **In journal** | Yes |
| **Stages** | 3 (completes at 20) |
| **Started by** | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) |
| **NPCs involved** | [Jolnor](../monsters/jolnor.md), [Kaori](../monsters/kaori.md) |
| **Locations** | [vilegard_chapel](../maps/vilegard_chapel.md), [vilegard_kaori](../maps/vilegard_kaori.md) |
| **Total XP** | 520 |
| **Related quests** | 1 |

</div>

## Overview

> Jolnor in Vilegard chapel wants me to talk to Kaori in northern Vilegard, to see if she wants any help.

## Prerequisites to start

Start with [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)). Required:

- reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Trusting an outsider](vilegard.md#stage-10) | stage 10 reached, for stage 5 here |
| Unlocks | [Trusting an outsider](vilegard.md#stage-30) | stage 30 there needs stage 20 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | Jolnor in Vilegard chapel wants me to talk to Kaori in northern Vilegard, to see if she wants any help. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | – | – |
| <span id="stage-10"></span>10 | Kaori in northern Vilegard wants me to bring her 10 bonemeal potions. | [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) | stage 5 | – |
| <span id="stage-20"></span>20 | I have brought 10 bonemeal potions to Kaori. **(completes quest)** | [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) | hand over 10× [Bonemeal potion](../items/bonemeal_potion.md), stage 10 | 520 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “Is there anything I can do to gain your trust?” — **conditions:** reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10) → **stage 5**. NPC: “First, there is Kaori. She lives up in the northern part of Vilegard. Ask her if she wants help with anything.”

???+ note "Stage 10: 1 route"

    1. Talk to [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) → choose “Is there anything I can do to gain your trust?” — **conditions:** reached stage 5 of [Kaori's errands](../quests/kaori.md#stage-5) → **stage 10**. NPC: “I would really like to have a few more of those. If you can bring me 10 bonemeal potions, I might consider trusting…”

???+ note "Stage 20: 1 route"

    1. Talk to [Kaori](../monsters/kaori.md) ([vilegard_kaori](../maps/vilegard_kaori.md)) → choose “Yes, I brought your potions.” — **conditions:** reached stage 10 of [Kaori's errands](../quests/kaori.md#stage-10); hand over 10× [Bonemeal potion](../items/bonemeal_potion.md) → **stage 20**. NPC: “Good. Give them to me.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “I would really like to have a few more of those. If you can bring me …” → “I would really like to have a few more of those. If you can bring me …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaori.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaori.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaori.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaori.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaori.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `kaori` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20 |
    | Dialogue nodes setting stages | 5: `jolnor_gaintrust_2`, 10: `kaori_13`, 20: `kaori_20` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
