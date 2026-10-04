# The last lord of Laeroth

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `last_lord` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 15, 70) |
| **Started by** | stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md), stepping on a trigger on [laerothisland1](../maps/laerothisland1.md) |
| **Total XP** | 1,001 |
| **Related quests** | 2 |

</div>

## Overview

> Before I leave Laeroth, perhaps I should try to find out where the last Lord went. Maybe there are clues somewhere in the manor.

## Prerequisites to start

Start with stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md). Required:

- NOT reached stage 10 of [The last lord of Laeroth](../quests/last_lord.md#stage-10)
- NOT reached stage 15 of [The last lord of Laeroth](../quests/last_lord.md#stage-15)
- reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Take care of the caretaker](laeroth_caretaker.md#stage-180) | stage 180 reached, for stages 10, 15 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-140) | stage 140 there needs stage 40 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Before I leave Laeroth, perhaps I should try to find out where the last Lord went. Maybe there are clues somewhere in the manor.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement1](../maps/laerothbasement1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothisland1](../maps/laerothisland1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor0](../maps/laerothmanor0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor3](../maps/laerothmanor3.md).</span> | stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) | – | – |
| <span id="stage-15"></span>15 | I didn't really care about where the last lord went. I left this place, and whatever happened to him didn't make any difference to me. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement1](../maps/laerothbasement1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothisland1](../maps/laerothisland1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor0](../maps/laerothmanor0.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor3](../maps/laerothmanor3.md).</span> | stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) | – | 1 XP |
| <span id="stage-20"></span>20 | I searched the caretakers room, and found a letter from "Adakin". It says he is leaving to explore his future, but little more than that except that it mentions a chest that contains a diary and other things he could not take with him. I should look for this chest.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | stage 10 | – |
| <span id="stage-30"></span>30 | I have found a chest, with an inscription "Adakin" on the top. It is locked though, so I need to find the key. Hopefully he did not take it with him.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement0](../maps/laerothbasement0.md).</span> | stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) | stage 20 | – |
| <span id="stage-40"></span>40 | I have found a key that looks like it should fit Adakin's chest.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor0](../maps/laerothmanor0.md).</span> | stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) | stage 30 | gives 1× [Key for Adakin's chest](../items/adakin_chest_key.md) |
| <span id="stage-50"></span>50 | I have opened Adakin's chest. There are some useful items in here, as well as his diary. The diary has a lock though, so it seems I must find a small key that fits this lock.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothbasement0](../maps/laerothbasement0.md).</span> | stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) | hand over 1× [Key for Adakin's chest](../items/adakin_chest_key.md), stage 40 | gives 1× [Adakin's diary](../items/adakin_diary.md) |
| <span id="stage-60"></span>60 | I have found a jeweled key that looks like it might be for the diary. Time to try it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | stage 50 | gives 1× [Key for Adakin's diary](../items/adakin_diary_key.md) |
| <span id="stage-70"></span>70 | The key unlocked the diary. The final entry did not really give an answer, except that he intended to go to either Nor City or Feygard, but had yet to decide which. Perhaps I will meet him some day. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothmanor1](../maps/laerothmanor1.md).</span> | stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) | hand over 1× [Adakin's diary](../items/adakin_diary.md), hand over 1× [Key for Adakin's diary](../items/adakin_diary_key.md), stage 60 | 1,000 XP |

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) → choose “Perhaps I should try to find out more.” — **conditions:** NOT reached stage 10 of [The last lord of Laeroth](../quests/last_lord.md#stage-10); NOT reached stage 15 of [The last lord of Laeroth](../quests/last_lord.md#stage-15); reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180) → **stage 10**. NPC: “I will look around. The main quarters are probably a good place to start.”

???+ note "Stage 15: 1 route"

    1. stepping on a trigger on [laerothbasement1](../maps/laerothbasement1.md) → choose “I am just wasting time here. Time to leave.” — **conditions:** NOT reached stage 10 of [The last lord of Laeroth](../quests/last_lord.md#stage-10); NOT reached stage 15 of [The last lord of Laeroth](../quests/last_lord.md#stage-15); reached stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180) → **stage 15**. NPC: “It doesn't matter where the last lord went.”

???+ note "Stage 20: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [The last lord of Laeroth](../quests/last_lord.md#stage-10); NOT reached stage 30 of [The last lord of Laeroth](../quests/last_lord.md#stage-30) → **stage 20**. NPC: “There is a chest here that contains what the caretaker left behind. Maybe there is something here about the last lord.…”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [The last lord of Laeroth](../quests/last_lord.md#stage-20); NOT reached stage 30 of [The last lord of Laeroth](../quests/last_lord.md#stage-30) → **stage 30**. NPC: “There is a chest here with "Adakin" written on the top. It is locked though. I need the key.”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [laerothmanor0](../maps/laerothmanor0.md) → the conversation leads here automatically — **conditions:** reached stage 30 of [The last lord of Laeroth](../quests/last_lord.md#stage-30); NOT reached stage 40 of [The last lord of Laeroth](../quests/last_lord.md#stage-40) → **stage 40**; also gives 1× [Key for Adakin's chest](../items/adakin_chest_key.md). NPC: “This small chest looks like it might contain something useful. Yes! A key that looks about the right size for Adakin's…”

???+ note "Stage 50: 1 route"

    1. stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [The last lord of Laeroth](../quests/last_lord.md#stage-40); hand over 1× [Key for Adakin's chest](../items/adakin_chest_key.md) → **stage 50**; also gives 1× [Adakin's diary](../items/adakin_diary.md). NPC: “The key works, and the chest is open! Here is his diary. It has its own lock though, so now I need a key for this!…”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [The last lord of Laeroth](../quests/last_lord.md#stage-50); NOT reached stage 60 of [The last lord of Laeroth](../quests/last_lord.md#stage-60) → **stage 60**; also gives 1× [Key for Adakin's diary](../items/adakin_diary_key.md). NPC: “I have found a smalled jeweled key that looks like it will fit Adakin's diary.”

???+ note "Stage 70: 1 route"

    1. stepping on a trigger on [laerothmanor1](../maps/laerothmanor1.md) → the conversation leads here automatically — **conditions:** reached stage 60 of [The last lord of Laeroth](../quests/last_lord.md#stage-60); hand over 1× [Key for Adakin's diary](../items/adakin_diary_key.md); NOT reached stage 70 of [The last lord of Laeroth](../quests/last_lord.md#stage-70); hand over 1× [Adakin's diary](../items/adakin_diary.md) → **stage 70**. NPC: “It reads: "I need to go and find my destiny. It is not here at the manor, so I must strike out and find what lies…”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=last_lord.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `last_lord` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 50, 60, 70 |
    | Dialogue nodes setting stages | 10: `laeroth_exit_1c`, 15: `laeroth_exit_1b`, 20: `caretaker_chest_1`, 30: `adakin_chest_1`, 40: `adakin_key_search_1`, 50: `adakin_chest_2`, 60: `nightstand_search_2`, 70: `last_lord_final_0b` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
