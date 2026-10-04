# misc_nondisplay

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `misc_nondisplay` |
| **In journal** | No (hidden flag) |
| **Stages** | 2 |
| **Started by** | stepping on a trigger on [blackwater_mountain5a](../maps/blackwater_mountain5a.md) |
| **NPCs involved** | [Umar](../monsters/umar.md) |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) |
| **Related quests** | 3 |

</div>

## Overview

> Found silver bar at bwm

## Prerequisites to start

Start with stepping on a trigger on [blackwater_mountain5a](../maps/blackwater_mountain5a.md). Required:

- NOT reached stage 10 of [misc_nondisplay (hidden flag)](../quests/misc_nondisplay.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Immaculate kidnapping](Thieves02.md#stage-76) | stage 76 reached, for stage 20 here |
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stage 20 here |
| Blocked by | [Immaculate kidnapping](Thieves02.md#stage-75) | stage 75 must NOT be reached, for stage 20 here |
| Blocked by | [The ruthless Crackshot](Thieves03.md#stage-1) | stage 1 must NOT be reached, for stage 20 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Found silver bar at bwm<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain5a](../maps/blackwater_mountain5a.md).</span> | stepping on a trigger on [blackwater_mountain5a](../maps/blackwater_mountain5a.md) | – | gives 1× [Silver bar](../items/silver_bar.md) |
| <span id="stage-20"></span>20 | Told by Umar to say he sent you at the inn. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [blackwater_mountain5a](../maps/blackwater_mountain5a.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [misc_nondisplay (hidden flag)](../quests/misc_nondisplay.md#stage-10) → **stage 10**; also gives 1× [Silver bar](../items/silver_bar.md). NPC: “You have found a small, shiny, metal bar.”

???+ note "Stage 20: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I expected that. See you tomorrow then.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76); NOT reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75); NOT reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1) → **stage 20**. NPC: “I'm afraid all the beds at the guild are taken for the night. We have arrangements at the inn in town though. If you…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=misc_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=misc_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=misc_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=misc_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=misc_nondisplay.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `misc_nondisplay` |
    | showInLog | 0 |
    | Stage IDs | 10, 20 |
    | Dialogue nodes setting stages | 10: `blackwater_mountain5a_01`, 20: `umar_guild02_27d` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
