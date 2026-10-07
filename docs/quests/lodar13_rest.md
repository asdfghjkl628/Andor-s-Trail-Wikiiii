---
description: "No rest for the guilty is a quest in Andor's Trail, started by Aulowenn (lodar13). 11 stages, 3,000 XP in total. In the maze of green vines east of the Duleian road, I met a guard named Aulowenn from Feygard, guarding some crates. She told me that she was part of a larger group of guards searchin…"
---

# No rest for the guilty

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lodar13_rest` |
| **In journal** | Yes |
| **Stages** | 11 (completes at 60, 65) |
| **Started by** | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) |
| **NPCs involved** | [Aulowenn](../monsters/aulowenn.md), [Tiqui](../monsters/tiqui.md) |
| **Locations** | [lodar13](../maps/lodar13.md), [lodar14](../maps/lodar14.md) |
| **Total XP** | 3,000 |

</div>

## Overview

> In the maze of green vines east of the Duleian road, I met a guard named Aulowenn from Feygard, guarding some crates. She told me that she was part of a larger group of guards searching for a madman that supposedly hides somewhere in the nearby hills, but that the other guards are now dead or missing.

## Prerequisites to start

None: talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In the maze of green vines east of the Duleian road, I met a guard named Aulowenn from Feygard, guarding some crates. She told me that she was part of a larger group of guards searching for a madman that supposedly hides somewhere in the nearby hills, but that the other guards are now dead or missing. | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) | – | – |
| <span id="stage-11"></span>11 | Aulowenn requested my help in defeating a monster that haunts the grave of her fellow guards to the east. She warned me that the foul beast will most likely try to trick me into listening to its story. | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) | – | – |
| <span id="stage-20"></span>20 | I have met the creature that Aulowenn spoke of. | [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | stage 11 | – |
| <span id="stage-22"></span>22 | I listened to the creature's story. Its name is Tiqui, and he is the head of his clan. Apparently, the guards have been ruthlessly killing off his kin. He asked me to kill the guard for him, as revenge for what they have done. | [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | – | – |
| <span id="stage-24"></span>24 | The creature tried to trick me into listening to its story. | [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | stage 30 | – |
| <span id="stage-30"></span>30 | I attacked the creature before it could spew out more of its foul lies. | [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | – | – |
| <span id="stage-31"></span>31 | I attacked Aulowenn. | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) | – | – |
| <span id="stage-40"></span>40 | Aulowenn thanked me for bringing peace to the grave of her fallen companions by killing the creature. | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) | – | – |
| <span id="stage-41"></span>41 | Tiqui was overjoyed that I helped him kill the guard for him. He promised that if we ever run into each other again, he'd help me somehow. | [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | – | – |
| <span id="stage-60"></span>60 | I am now able to use Aulowenn's bed whenever I wish to rest. **(completes quest)**<br><span class="qnote">🔓 You can finally access a previously blocked area on [Lodar13](../maps/lodar13.md).</span> | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md))<br>[Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | – | 3,000 XP |
| <span id="stage-65"></span>65 | I will not be able to resolve the conflict between Aulowenn and her attacker. **(completes quest)** | [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md))<br>[Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) | stage 30, stage 31 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → choose “What about the others?” → **stage 10**. NPC: “Some of my men were killed by the creatures that live in these woods, some ran away by themselves and some have never…”

???+ note "Stage 11: 1 route"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → choose “So, you want me to go visit the graves to the east and defeat whatever creature is there?” — **conditions:** reached stage 11 of [No rest for the guilty](../quests/lodar13_rest.md#stage-11) → **stage 11**. NPC: “Yes, that's it. I should also warn you that those creatures are intelligible, so I would urge you to act quickly when…”

???+ note "Stage 20: 1 route"

    1. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → choose “I am sent here by Aulowenn to take care of you.” — **conditions:** reached stage 11 of [No rest for the guilty](../quests/lodar13_rest.md#stage-11) → **stage 20**. NPC: “Tiqui not want fight. Tiqui angry that men who smell bad kill his friends.”

???+ note "Stage 22: 1 route"

    1. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → choose “What can I do to help?” — **conditions:** reached stage 22 of [No rest for the guilty](../quests/lodar13_rest.md#stage-22) → **stage 22**. NPC: “You go take care of last smelly person. Tiqui can be friend to you. Tiqui can have revenge.”

???+ note "Stage 24: 1 route"

    1. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30) → **stage 24**. NPC: “No, you die now! You one of them! Tiqui angry!”

???+ note "Stage 30: 1 route"

    1. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30) → **stage 30**. NPC: “No, you die now! You one of them! Tiqui angry!”

???+ note "Stage 31: 1 route"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → the conversation leads here automatically — **conditions:** reached stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31) → **stage 31**. NPC: “For Feygard!”

???+ note "Stage 40: 1 route"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [No rest for the guilty](../quests/lodar13_rest.md#stage-40) → **stage 40**. NPC: “Excellent. Maybe now my brethren can rest peacefully. Thank you so much for helping me.”

???+ note "Stage 41: 1 route"

    1. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → the conversation leads here automatically — **conditions:** reached stage 41 of [No rest for the guilty](../quests/lodar13_rest.md#stage-41) → **stage 41**. NPC: “Yes! Yes! The smell is gone. You friend of Tiqui now! Tiqui help you when we meet again!”

???+ note "Stage 60: 2 routes"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60) → **stage 60**. NPC: “In return, you are very welcome to use my bed to rest whenever you wish.”
    2. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60) → **stage 60**. NPC: “You also use bed of smelly men, and Tiqui keep you safe.”

???+ note "Stage 65: 2 routes"

    1. Talk to [Aulowenn](../monsters/aulowenn.md) ([lodar13](../maps/lodar13.md)) → the conversation leads here automatically — **conditions:** reached stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31); reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30) → **stage 65**
    2. Talk to [Tiqui](../monsters/tiqui.md) ([lodar14](../maps/lodar14.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30); reached stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31) → **stage 65**


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “Tiqui not want fight. Tiqui angry that men who smell bad kill his fri…” → “Tiqui not want fight. Tiqui angry that men who smell bad kill his fri…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar13_rest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar13_rest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar13_rest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar13_rest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar13_rest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lodar13_rest` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 20, 22, 24, 30, 31, 40, 41, 60, 65 |
    | Dialogue nodes setting stages | 10: `aulowenn9`, 11: `aulowenn20`, 20: `tiqui1`, 22: `tiqui14`, 24: `tiqui_atk0`, 30: `tiqui_atk0`, 31: `aulowenn_atk0`, 40: `aulowenn_k0`, 41: `tiqui_r1`, 60: `aulowenn_k1`, 60: `tiqui_r2`, 65: `aulowenn_atk1`, 65: `tiqui_atk1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
