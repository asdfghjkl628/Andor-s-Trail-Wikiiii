# A lost potion

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lodar` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 110) |
| **Started by** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Afflicted Feygard guard](../monsters/lodar_fg3.md), [Feygard guard](../monsters/lodar_fg1.md), [Forest guardian](../monsters/lodar0_g.md), [Insane Feygard guard](../monsters/lodar_fg4.md), [Lodar](../monsters/lodar.md), [Ogam](../monsters/ogam.md) +2 |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md), [lodar0](../maps/lodar0.md), [lodar11](../maps/lodar11.md) |
| **Total XP** | 15,500 |
| **Related quests** | 2 |

</div>

## Overview

> I should find a potion maker called Lodar. Umar in the Fallhaven Thieves' Guild told me that I will need to know the right words to pass a guardian in order to reach Lodar's hideaway.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stages 10, 15 here |
| Unlocks | [Searching for madness](lodar2.md#stage-10) | stage 10 there needs stage 110 here |
| Unlocks | [Searching for madness](lodar2.md#stage-15) | stage 15 there needs stage 110 here |
| Unlocks | [Searching for madness](lodar2.md#stage-20) | stage 20 there needs stage 110 here |
| Unlocks | [Searching for madness](lodar2.md#stage-30) | stage 30 there needs stage 100 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I should find a potion maker called Lodar. Umar in the Fallhaven Thieves' Guild told me that I will need to know the right words to pass a guardian in order to reach Lodar's hideaway. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-15"></span>15 | Umar told me I should go see someone called Ogam in Vilegard. Ogam can supply me with the right words to reach Lodar's hideaway. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-20"></span>20 | I have visited Ogam in southwest Vilegard. He was talking in what seemed like riddles. I could barely make out some details when I asked about Lodar's hideaway. 'Halfway between the Shadow and the light. Rocky formations.' and the words 'Glow of the Shadow.' were among the things he said. I am not sure what they mean. | [Ogam](../monsters/ogam.md) ([vilegard_ogam](../maps/vilegard_ogam.md)) | stage 15 | – |
| <span id="stage-30"></span>30 | I have found a formation of rocks on the Duleian Road. It does not look like they were naturally placed, but rather that they are meant to symbolize something. | reading a sign on [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) | – | – |
| <span id="stage-31"></span>31 | Could this be the 'rocky formation' that the old man Ogam mentioned? If that is the case, then this might be a clue as to where Andor went. | reading a sign on [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) | stage 20 | 1,500 XP |
| <span id="stage-40"></span>40 | In the woods close to the rocky formation, I encountered a creature blocking the way into the forest. | [Forest guardian](../monsters/lodar0_g.md) ([lodar0](../maps/lodar0.md)) | – | – |
| <span id="stage-45"></span>45 | By speaking the words that Ogam had mentioned, the creature moved out of the way, and almost seemed to welcome me further into the forest. | [Forest guardian](../monsters/lodar0_g.md) ([lodar0](../maps/lodar0.md)) | – | 3,000 XP |
| <span id="stage-50"></span>50 | I encountered a guard from Feygard in the woods. He told me a tale of a madman that the guards from Feygard are searching for. The madman is wanted for a number of reasons that he would not disclose. He warned me both about the twisty mazes ahead, and about the madman. Apparently, several guards have gone missing after venturing forth, either by getting lost in the maze, or by something that the madman has done to them. | [Feygard guard](../monsters/lodar_fg1.md) ([lodar2](../maps/lodar2.md)) | – | – |
| <span id="stage-51"></span>51 | Before leaving, the guard warned me both about the twisty mazes ahead, and about the madman. Apparently, several guards have gone missing after venturing forth, either by getting lost in the maze, or by something that the madman has done to them. | [Feygard guard](../monsters/lodar_fg1.md) ([lodar2](../maps/lodar2.md)) | – | – |
| <span id="stage-60"></span>60 | I found another rocky formation that looked out of place. | reading a sign on [lodar4](../maps/lodar4.md) | – | 2,000 XP |
| <span id="stage-71"></span>71 | I encountered another guard from Feygard, disoriented and lost. The things he said did not make sense. | [Rambling Feygard guard](../monsters/lodar_fg2.md) ([lodar2](../maps/lodar2.md)) | – | – |
| <span id="stage-72"></span>72 | I encountered another guard from Feygard, that seemed to be affected by something. He attacked me without provocation. | [Afflicted Feygard guard](../monsters/lodar_fg3.md) ([lodar11](../maps/lodar11.md)) | – | – |
| <span id="stage-73"></span>73 | I encountered another guard from Feygard, that rambled of something that 'lurks underneath'. He attacked me without provocation. | [Insane Feygard guard](../monsters/lodar_fg4.md) ([lodar8](../maps/lodar8.md)) | – | – |
| <span id="stage-80"></span>80 | I found yet another rocky formation that looked out of place. | reading a sign on [lodar14](../maps/lodar14.md) | – | 2,000 XP |
| <span id="stage-90"></span>90 | In a well-hidden cave, I encountered yet another rocky formation that looked similar to the other ones that I've already seen. I must be getting close to whatever these formations lead to. | reading a sign on [lodarcave0](../maps/lodarcave0.md) | – | 2,000 XP |
| <span id="stage-100"></span>100 | In the cave, I reached what looks like a tomb. I was unable to venture further into the tomb because of something that held me back. | walking into a blocked passage on [lodarcave4a](../maps/lodarcave4a.md) | – | – |
| <span id="stage-110"></span>110 | After navigating through the immense twisty green maze and the damp cave, I have reached a cabin in a clearing. The cabin is occupied by the potion-maker called Lodar. **(completes quest)** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | 5,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “OK, I'll promise to keep it a secret.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51) → **stage 10**. NPC: “The only one that understands the language of the guardian is the old man Ogam in Vilegard.”

???+ note "Stage 15: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “OK, I'll promise to keep it a secret.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51) → **stage 15**. NPC: “You should travel to the town of Vilegard and find Ogam. He can help you get the right words to enter Lodar's Hideaway.”

???+ note "Stage 20: 1 route"

    1. Talk to [Ogam](../monsters/ogam.md) ([vilegard_ogam](../maps/vilegard_ogam.md)) → choose “OK, halfway between two places. Some rocks?” — **conditions:** reached stage 15 of [A lost potion](../quests/lodar.md#stage-15) → **stage 20**. NPC: “Guardian. Glow of the Shadow.”

???+ note "Stage 30: 1 route"

    1. reading a sign on [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) → the conversation leads here automatically → **stage 30**. NPC: “You notice that these rocks seem out of place compared to the surroundings. Maybe they are meant to symbolize something?”

???+ note "Stage 31: 1 route"

    1. reading a sign on [roadbeforecrossroads1](../maps/roadbeforecrossroads1.md) → choose “[Examine the stones more closely]” — **conditions:** reached stage 20 of [A lost potion](../quests/lodar.md#stage-20) → **stage 31**. NPC: “While examining them, you recall the old man Ogam in Vilegard spoke of some 'Rocky Formations'. Could this be what he…”

???+ note "Stage 40: 1 route"

    1. Talk to [Forest guardian](../monsters/lodar0_g.md) ([lodar0](../maps/lodar0.md)) → the conversation leads here automatically → **stage 40**. NPC: “Master says only ones with password can pass. You have password?”

???+ note "Stage 45: 1 route"

    1. Talk to [Forest guardian](../monsters/lodar0_g.md) ([lodar0](../maps/lodar0.md)) → the conversation leads here automatically — **conditions:** reached stage 45 of [A lost potion](../quests/lodar.md#stage-45) → **stage 45**. NPC: “[The creature moves out of the way, and gestures with its hands almost like it is welcoming you further into the forest]”

???+ note "Stage 50: 1 route"

    1. Talk to [Feygard guard](../monsters/lodar_fg1.md) ([lodar2](../maps/lodar2.md)) → choose “What could be causing them to behave that way?” — **conditions:** reached stage 50 of [A lost potion](../quests/lodar.md#stage-50) → **stage 50**. NPC: “Maybe it's something that the madman that we were looking for has done.”

???+ note "Stage 51: 1 route"

    1. Talk to [Feygard guard](../monsters/lodar_fg1.md) ([lodar2](../maps/lodar2.md)) → the conversation leads here automatically — **conditions:** reached stage 51 of [A lost potion](../quests/lodar.md#stage-51) → **stage 51**. NPC: “I don't know if it's the twisty paths themselves or something that the madman has done that caused my fellow guards to…”

???+ note "Stage 60: 1 route"

    1. reading a sign on [lodar4](../maps/lodar4.md) → the conversation leads here automatically → **stage 60**. NPC: “On the ledge, you notice another formation of rocks that seem out of place compared to the surroundings.”

???+ note "Stage 71: 1 route"

    1. Talk to [Rambling Feygard guard](../monsters/lodar_fg2.md) ([lodar2](../maps/lodar2.md)) → choose “See what?” → **stage 71**. NPC: “[The guard continues with his mumbling]”

???+ note "Stage 72: 1 route"

    1. Talk to [Afflicted Feygard guard](../monsters/lodar_fg3.md) ([lodar11](../maps/lodar11.md)) → choose “Fight!” → **stage 72**

???+ note "Stage 73: 1 route"

    1. Talk to [Insane Feygard guard](../monsters/lodar_fg4.md) ([lodar8](../maps/lodar8.md)) → choose “Let's see who's victorious!” → **stage 73**

???+ note "Stage 80: 1 route"

    1. reading a sign on [lodar14](../maps/lodar14.md) → the conversation leads here automatically → **stage 80**. NPC: “On the ledge, you notice another formation of rocks that seem out of place compared to the surroundings. The rocks…”

???+ note "Stage 90: 1 route"

    1. reading a sign on [lodarcave0](../maps/lodarcave0.md) → the conversation leads here automatically → **stage 90**. NPC: “The rocks in this formation give off a distinct pulsating glow.”

???+ note "Stage 100: 1 route"

    1. walking into a blocked passage on [lodarcave4a](../maps/lodarcave4a.md) → the conversation leads here automatically → **stage 100**. NPC: “As you try to step further into the cave, you feel your steps becoming more and more heavy.”

???+ note "Stage 110: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “I'm $playername.” — **conditions:** reached stage 110 of [A lost potion](../quests/lodar.md#stage-110) → **stage 110**. NPC: “Well, it doesn't matter who you are anyway. I am Lodar, maker of potions.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “(the guard continues with his mumbling)” → “[The guard continues with his mumbling]” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “While examining them, you recall the the old man Ogam in Vilegard spo…” → “While examining them, you recall the old man Ogam in Vilegard spoke o…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lodar` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 31, 40, 45, 50, 51, 60, 71, 72, 73, 80, 90, 100, 110 |
    | Dialogue nodes setting stages | 10: `umar_lodar_5`, 15: `umar_lodar_6`, 20: `ogam_lodar_3`, 30: `sign_rbfcr1_1`, 31: `sign_rbfcr1_3`, 40: `lodar0_g2`, 45: `lodar0_g4`, 50: `lodar_fg1_13`, 51: `lodar_fg1_17`, 60: `sign_lodar4_0`, 71: `lodar_fg2_6`, 72: `lodar_fg3_4`, 73: `lodar_fg4_8`, 80: `sign_lodar14_0`, 90: `sign_lodarcave0_0`, 100: `sign_lodarcave4a`, 110: `lodar_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
