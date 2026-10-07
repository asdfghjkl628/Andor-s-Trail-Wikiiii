---
description: "Just the beginning is a quest in Andor's Trail, started by Cithurn (waterwaybhouse). 13 stages, 11,500 XP in total. In a lonely house east of Loneford, I met an old man named Cithurn."
---

# Just the beginning

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `waterwayacave` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 60, 70) |
| **Started by** | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) |
| **NPCs involved** | [Cithurn](../monsters/waterwayhermit.md), [Tesrekan](../monsters/tesrekan.md) |
| **Locations** | [waterwayacave4](../maps/waterwayacave4.md), [waterwaybhouse](../maps/waterwaybhouse.md) |
| **Total XP** | 11,500 |
| **Related quests** | 2 |

</div>

## Overview

> In a lonely house east of Loneford, I met an old man named Cithurn.

## Prerequisites to start

Start with [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)). Required:

- NOT reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10)
- NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Trial by fire](charwood2.md#stage-50) | stage 50 reached, for stages 15, 20, 25, 30, 35 here |
| Blocked by | [Trial by fire](charwood2.md#stage-50) | stage 50 must NOT be reached, for stage 12 here |
| Mutually exclusive | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-90) | stage 90 must NOT be reached, for stages 10, 60, 70 here |
| Unlocks | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-10) | stage 10 there needs stage 35 here |
| Unlocks | [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](nondisplay_2.md#stage-120) | stage 120 there needs stage 70 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In a lonely house east of Loneford, I met an old man named Cithurn. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | – | – |
| <span id="stage-12"></span>12 | Cithurn told me he needs an experienced fighter to help with his problem. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-15"></span>15 | Cithurn told me that the surrounding forest has been under invasion by monsters for several weeks. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-20"></span>20 | Cithurn heard something similar was occurring in Charwood until a young adventurer killed a vile beast in the mine beneath the city. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-25"></span>25 | I told Cithurn about my role in Charwood and of my battle with Thukuzun. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | Cithurn did not remember if the forest invasion began before the events in Charwood or after. However, based on my experiences in Charwood, Cithurn believes there is a connection between the two. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-35"></span>35 | I promised Cithurn I would investigate the source of the monster invasion in the forest. I will have to pass through the forest to access an entrance to a cave east of Cithurn's home. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | stage 10 | – |
| <span id="stage-40"></span>40 | I found the entrance to the cave.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwayacave1](../maps/waterwayacave1.md).</span> | stepping on a trigger on [waterwayacave1](../maps/waterwayacave1.md) | stage 35 | – |
| <span id="stage-45"></span>45 | I reached the end of the cave system. The air became damper the deeper I went.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwayacave3](../maps/waterwayacave3.md).</span> | stepping on a trigger on [waterwayacave3](../maps/waterwayacave3.md) | – | – |
| <span id="stage-50"></span>50 | Among the cold and damp lower parts of the cave, I encountered another dragon-like creature. This must be the source of all the chaos in the forest above. I should attempt to kill it. | [Tesrekan](../monsters/tesrekan.md) ([waterwayacave4](../maps/waterwayacave4.md)) | – | – |
| <span id="stage-55"></span>55 | I killed the monster called Tesrekan and took one of its bones as proof. I should venture back to Cithurn to tell him about it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwayacave4](../maps/waterwayacave4.md).</span> | stepping on a trigger on [waterwayacave4](../maps/waterwayacave4.md) | carry 1× [Tesrekan's bone](../items/tesrekanbone.md) | – |
| <span id="stage-60"></span>60 | I presented one of the bones from the corpse of Tesrekan to Cithurn. He was happy to hear that I killed the source of the monster invasion. As we agreed, I returned his talisman. **(completes quest)** | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | carry 1× [Tesrekan's bone](../items/tesrekanbone.md), hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md), hand over 1× [Tesrekan's bone](../items/tesrekanbone.md), stage 55 | 7,000 XP |
| <span id="stage-70"></span>70 | I presented one of the bones from the corpse of Tesrekan to Cithurn. He was happy to hear that I killed the source of the monster invasion. I decided to keep his talisman as payment for my hard work. **(completes quest)** | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | carry 1× [Tesrekan's bone](../items/tesrekanbone.md), hand over 1× [Tesrekan's bone](../items/tesrekanbone.md), stage 55 | 4,500 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “Sorry. I didn't mean to be rude. I'm $playername. I come from a small village where people tend to leave…” — **conditions:** NOT reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90) → **stage 10**. NPC: “Well $playername, you are young, and you apologized, so perhaps I will be a little forgiving. Just remember that not…”

???+ note "Stage 12: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “Dangerous? Perhaps I can help?” — **conditions:** reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 12 of [Just the beginning](../quests/waterwayacave.md#stage-12); NOT reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50) → **stage 12**. NPC: “I don't think so. It would need an experienced fighter to help with this problem.”

???+ note "Stage 15: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35) → **stage 15**. NPC: “The surrounding forest is usually quiet, but for some time now it has been under a monster invasion. I am surprised…”

???+ note "Stage 20: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35) → **stage 20**. NPC: “I heard something similar was occurring in Charwood until a young adventurer killed a vile beast in the mine beneath…”

???+ note "Stage 25: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “I was in Charwood recently and what you heard was true. [You describe your experiences in Charwood and the…” — **conditions:** reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35) → **stage 25**. NPC: “I do not know if it began happening here before the events in Charwood or after. However, from what you tell me, maybe…”

???+ note "Stage 30: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “I was in Charwood recently and what you heard was true. [You describe your experiences in Charwood and the…” — **conditions:** reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35) → **stage 30**. NPC: “There is a cave system that runs underneath the forest. If something sinister is afoot, it could be emanating from the…”

???+ note "Stage 35: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “OK, I will help you.” — **conditions:** reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35) → **stage 35**. NPC: “Thank you. You will have to pass through the forest to reach an opening to the cave where you can enter. The opening…”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [waterwayacave1](../maps/waterwayacave1.md) → the conversation leads here automatically — **conditions:** reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35); NOT reached stage 40 of [Just the beginning](../quests/waterwayacave.md#stage-40) → **stage 40**. NPC: “You have found the entrance to the cave Cithurn was talking about.”

???+ note "Stage 45: 1 route"

    1. stepping on a trigger on [waterwayacave3](../maps/waterwayacave3.md) → the conversation leads here automatically — **conditions:** NOT reached stage 45 of [Just the beginning](../quests/waterwayacave.md#stage-45) → **stage 45**. NPC: “You notice that the air has become much damper as you make your way towards the end of the cave system.”

???+ note "Stage 50: 1 route"

    1. Talk to [Tesrekan](../monsters/tesrekan.md) ([waterwayacave4](../maps/waterwayacave4.md)) → the conversation leads here automatically → **stage 50**. NPC: “Ah, another puny mortal that has come to die and serve Tesrekan.”

???+ note "Stage 55: 1 route"

    1. stepping on a trigger on [waterwayacave4](../maps/waterwayacave4.md) → the conversation leads here automatically — **conditions:** carry 1× [Tesrekan's bone](../items/tesrekanbone.md) → **stage 55**

???+ note "Stage 60: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “Certainly. Here you are.” — **conditions:** NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90); NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); reached stage 55 of [Just the beginning](../quests/waterwayacave.md#stage-55); carry 1× [Tesrekan's bone](../items/tesrekanbone.md); hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md); hand over 1× [Tesrekan's bone](../items/tesrekanbone.md) → **stage 60**. NPC: “Thank you. I see you are not just a great fighter, but also an adventurer that keeps his word.”

???+ note "Stage 70: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “You are right about that debt. I think I'll keep the talisman as payment.” — **conditions:** NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90); NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); reached stage 55 of [Just the beginning](../quests/waterwayacave.md#stage-55); carry 1× [Tesrekan's bone](../items/tesrekanbone.md); hand over 1× [Tesrekan's bone](../items/tesrekanbone.md) → **stage 70**. NPC: “I see. You are apparently a great fighter, but not a very honorable one.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 13 lines added |
| [v0.7.4](../versions/0.7.4.md) | Stage 35 journal text changed<br>Dialogue: 1 line changed<br>· text: “You have found the enterance to the cave Cithurn was talking about.” → “You have found the entrance to the cave Cithurn was talking about.” |
| [v0.7.17](../versions/0.7.17.md) | Stage 35 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=waterwayacave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=waterwayacave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=waterwayacave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=waterwayacave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=waterwayacave.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `waterwayacave` |
    | showInLog | 1 |
    | Stage IDs | 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70 |
    | Dialogue nodes setting stages | 10: `cithurn_62`, 12: `cithurn_66`, 15: `cithurn_10`, 20: `cithurn_20`, 25: `cithurn_30`, 30: `cithurn_40`, 35: `cithurn_50`, 40: `waterwayacaveenter_20`, 45: `waterwayacave1_20`, 50: `tesrekan`, 55: `waterwayacavekillboss_20`, 60: `cithurn_100`, 70: `cithurn_101` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
