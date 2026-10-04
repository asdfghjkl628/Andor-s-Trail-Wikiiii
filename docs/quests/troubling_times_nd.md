# troubling_times_nd

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `troubling_times_nd` |
| **In journal** | No (hidden flag) |
| **Stages** | 3 |
| **Started by** | [Sly Seraphina](../monsters/tt_seraphina5.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) |
| **NPCs involved** | [Sly Seraphina](../monsters/tt_seraphina2.md), [Sly Seraphina](../monsters/tt_seraphina4.md), [Sly Seraphina](../monsters/tt_seraphina5.md) |
| **Locations** | [crackshot_hideout3](../maps/crackshot_hideout3.md), [crackshot_hideout4](../maps/crackshot_hideout4.md) |
| **Related quests** | 1 |

</div>

## Overview

> Seraphina search

## Prerequisites to start

None: talk to [Sly Seraphina](../monsters/tt_seraphina5.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Troubling times](troubling_times.md#stage-260) | stage 260 there needs stage 10 here |
| Unlocks | [Troubling times](troubling_times.md#stage-270) | stage 270 there needs stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Seraphina search | [Sly Seraphina](../monsters/tt_seraphina5.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) | – | – |
| <span id="stage-20"></span>20 | Crackshot's door unsealed<br><span class="qnote">🔓 You can finally access a previously blocked area on [Crackshot hideout3](../maps/crackshot_hideout3.md).</span><br><span class="qnote">🗺️ Part of [Crackshot hideout3](../maps/crackshot_hideout3.md) visibly changes.</span> | [Sly Seraphina](../monsters/tt_seraphina2.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) | hand over 1× [Key of Luthor](../items/key_luthor.md) | sets stage 210 of [Troubling times](../quests/troubling_times.md#stage-210)<br>removes monsters from crackshot_hideout3 |
| <span id="stage-30"></span>30 | 1=standing north of Sly while she blocks the passage<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout4](../maps/crackshot_hideout4.md).</span> | stepping on a trigger on [crackshot_hideout4](../maps/crackshot_hideout4.md)<br>[Sly Seraphina](../monsters/tt_seraphina4.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) | – | faction “tt_sly_attack2” +1<br>moves you to [crackshot_hideout4](../maps/crackshot_hideout4.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Sly Seraphina](../monsters/tt_seraphina5.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) → choose “[Sarcastic] Truly royal.” → **stage 10**. NPC: “In fact, I am King Luthor's heir. He's my ancestor.”

???+ note "Stage 20: 1 route"

    1. Talk to [Sly Seraphina](../monsters/tt_seraphina2.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) → choose “Here it is. Let's do it.” — **conditions:** hand over 1× [Key of Luthor](../items/key_luthor.md) → **stage 20**; also sets stage 210 of [Troubling times](../quests/troubling_times.md#stage-210), removes monsters from crackshot_hideout3. NPC: “Seraphina takes the key and easily unlocks the door. As quick as a weasel, she slips into the dark corridor.”

???+ note "Stage 30: 2 routes"

    1. stepping on a trigger on [crackshot_hideout4](../maps/crackshot_hideout4.md) → the conversation leads here automatically → **stage 30**; also faction “tt_sly_attack2” +1
    2. Talk to [Sly Seraphina](../monsters/tt_seraphina4.md) ([crackshot_hideout4](../maps/crackshot_hideout4.md)) → choose “Hey, I'm back. Don't be alarmed, I'll squeeze past you.” — **conditions:** NOT reached stage 30 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-30) → **stage 30**; also moves you to [crackshot_hideout4](../maps/crackshot_hideout4.md)


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=troubling_times_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=troubling_times_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=troubling_times_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=troubling_times_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=troubling_times_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `troubling_times_nd` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30 |
    | Dialogue nodes setting stages | 10: `tt_sly5_3`, 20: `tt_sly2_20`, 30: `tt_sly_attack2`, 30: `tt_sly4_6` |
    | Dialogue nodes clearing stages | 20: `nanath_302`, 30: `tt_sly_attack0` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
