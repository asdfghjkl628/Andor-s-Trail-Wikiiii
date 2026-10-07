---
description: "A cat and mouse game is a quest in Andor's Trail, started by Seviron (brimhaven_church). 9 stages, 2,500 XP in total. I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks."
---

# A cat and mouse game

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `cat_and_mouse` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 70, 90) |
| **Started by** | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Seviron](../monsters/brv_churchman.md) |
| **Locations** | [brimhaven_church](../maps/brimhaven_church.md), [brimhaven_church_upstairs](../maps/brimhaven_church_upstairs.md), [brimhaven_general1](../maps/brimhaven_general1.md) |
| **Total XP** | 2,500 |
| **Related quests** | 1 |

</div>

## Overview

> I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks.

## Prerequisites to start

Start with [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)). Required:

- NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10)
- NOT reached stage 30 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-30)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [brv_nondisplay2 (hidden flag)](brv_nondisplay2.md#stage-60) | stage 60 there needs stage 60 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I agreed to help Seviron trap the mouse that the cat cannot catch. I need to get some cheese, a large empty bottle, and three rocks. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | – | – |
| <span id="stage-20"></span>20 | I have given Seviron the rocks. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | hand over 3× [Small rock](../items/rock.md), stage 10, stage 30 | – |
| <span id="stage-30"></span>30 | I have given Seviron the cheese. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | hand over 1× [Cheese](../items/cheese.md), hand over 3× [Small rock](../items/rock.md), stage 10, stage 20 | – |
| <span id="stage-40"></span>40 | I obtained a suitable bottle from Arlish. | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 20, stage 30 | gives [Large empty bottle](../items/large_bottle.md) |
| <span id="stage-50"></span>50 | I have given Seviron the bottle. Seviron will set the trap, but it may take some time to catch the mouse. I should come back later. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | hand over 1× [Large empty bottle](../items/large_bottle.md), stage 20, stage 30 | starts timer “mouse_trap” |
| <span id="stage-60"></span>60 | The mouse has been caught! Seviron gave it to me in the bottle. He said I can decide what to do with it. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | stage 50 | gives [Trapped mouse](../items/trapped_mouse.md), [Gold coins](../items/gold.md) |
| <span id="stage-70"></span>70 | I decided to give the mouse to the cat. The cat would have eventually killed it anyway. **(completes quest)** | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | carry 1× [Trapped mouse](../items/trapped_mouse.md), hand over 1× [Trapped mouse](../items/trapped_mouse.md), stage 60 | 1,000 XP<br>gives [Large empty bottle](../items/large_bottle.md) |
| <span id="stage-80"></span>80 | I decided to release the mouse outside. Seviron told me to do that outside the town. | [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) | carry 1× [Trapped mouse](../items/trapped_mouse.md), stage 60 | – |
| <span id="stage-90"></span>90 | I released the mouse. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven exit](../maps/brimhaven_exit.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven7](../maps/brimhaven7.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterway12](../maps/waterway12.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven3](../maps/waytobrimhaven3.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytobrimhaven6](../maps/waytobrimhaven6.md).</span> | stepping on a trigger on [brimhaven7](../maps/brimhaven7.md) | carry 1× [Trapped mouse](../items/trapped_mouse.md), hand over 1× [Trapped mouse](../items/trapped_mouse.md) | 1,500 XP<br>gives [Large empty bottle](../items/large_bottle.md) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “OK. I'll help.” — **conditions:** NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); NOT reached stage 30 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-30) → **stage 10**. NPC: “Thanks. Just bring me the items. I think three rocks should be enough.”

???+ note "Stage 20: 2 routes"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I have the rocks.” — **conditions:** reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); hand over 3× [Small rock](../items/rock.md); NOT carry 1× [Cheese](../items/cheese.md); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20) → **stage 20**. NPC: “Thanks. Now we just need the cheese and the bottle.”
    2. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I have the rocks.” — **conditions:** reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); hand over 3× [Small rock](../items/rock.md); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20) → **stage 20**. NPC: “Thanks. Now we just need the bottle. You should ask around town. Someone must have one.”

???+ note "Stage 30: 2 routes"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I have the cheese.” — **conditions:** reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); hand over 1× [Cheese](../items/cheese.md); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT carry 3× [Small rock](../items/rock.md) → **stage 30**. NPC: “Thanks. Now we just need the rocks and the bottle.”
    2. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I have the rocks.” — **conditions:** reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); hand over 3× [Small rock](../items/rock.md); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20) → **stage 30**. NPC: “Thanks. Now we just need the bottle. You should ask around town. Someone must have one.”

???+ note "Stage 40: 1 route"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “Seviron at the church needs it. I'm just helping out.” — **conditions:** reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 40 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-40) → **stage 40**; also gives [Large empty bottle](../items/large_bottle.md). NPC: “Well, I do happen to have one. I don't display it as shop inventory because I've never been asked for such a thing…”

???+ note "Stage 50: 1 route"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “Yes. Here it is.” — **conditions:** reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 50 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-50); hand over 1× [Large empty bottle](../items/large_bottle.md) → **stage 50**; also starts timer “mouse_trap”. NPC: “Excellent. I'll set the trap. This will require some patience though, so you should come back later to see if it worked.”

???+ note "Stage 60: 1 route"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-50); NOT reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60); reached stage 40 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-40) → **stage 60**; also gives [Trapped mouse](../items/trapped_mouse.md), [Gold coins](../items/gold.md). NPC: “We caught the mouse! Here it is, in the bottle. You can decide what to do with it. And here's a little gold for your…”

???+ note "Stage 70: 1 route"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I'll give it to the cat. That should solve the problem.” — **conditions:** reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60); NOT reached stage 70 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-70); NOT reached stage 80 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-80); NOT reached stage 90 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-90); carry 1× [Trapped mouse](../items/trapped_mouse.md); hand over 1× [Trapped mouse](../items/trapped_mouse.md) → **stage 70**; also gives [Large empty bottle](../items/large_bottle.md). NPC: “Hmm. I'm sure the cat will be happy, but I doubt the mouse will!”

???+ note "Stage 80: 1 route"

    1. Talk to [Seviron](../monsters/brv_churchman.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I'll release it outside.” — **conditions:** reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60); NOT reached stage 70 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-70); NOT reached stage 80 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-80); NOT reached stage 90 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-90); carry 1× [Trapped mouse](../items/trapped_mouse.md) → **stage 80**. NPC: “Well, don't release it in the town. It will just go into another building.”

???+ note "Stage 90: 1 route"

    1. stepping on a trigger on [brimhaven7](../maps/brimhaven7.md) → choose “[Open the bottle]” — **conditions:** carry 1× [Trapped mouse](../items/trapped_mouse.md); hand over 1× [Trapped mouse](../items/trapped_mouse.md) → **stage 90**; also gives [Large empty bottle](../items/large_bottle.md). NPC: “You look after as it disappears quickly.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=cat_and_mouse.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `cat_and_mouse` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `brv_churchman_08`, 20: `brv_churchman_09a`, 20: `brv_churchman_09c`, 30: `brv_churchman_09b`, 30: `brv_churchman_09c`, 40: `arlish_bottle_2`, 50: `brv_churchman_b2`, 60: `brv_churchman_trap2`, 70: `brv_churchman_trap3a`, 80: `brv_churchman_trap3b`, 90: `release_mouse1a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
