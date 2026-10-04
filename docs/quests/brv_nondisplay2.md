# brv_nondisplay2

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_nondisplay2` |
| **In journal** | No (hidden flag) |
| **Stages** | 9 |
| **Started by** | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md), stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) |
| **NPCs involved** | [Arlish](../monsters/arlish.md), [Golin](../monsters/golin.md), [Pupil](../monsters/brv_pupil5.md), [Pupil](../monsters/brv_pupil8.md), [Pupil](../monsters/brv_pupil4.md), [Pupil](../monsters/brv_pupil2.md) +6 |
| **Locations** | [brimhaven_general1](../maps/brimhaven_general1.md), [brimhaven_school](../maps/brimhaven_school.md) |
| **Related quests** | 2 |

</div>

## Overview

> You run around in classroom.

## Prerequisites to start

**Route 1** (stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)):

- NOT reached stage 10 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-10)
- NOT reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60)

**Route 2** ([Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Lessons learned](brv_school2.md#stage-30) | stage 30 reached, for stages 20, 21 here |
| Requires | [Lessons learned](brv_school2.md#stage-60) | stage 60 reached, for stage 50 here |
| Requires | [Lessons learned](brv_school2.md#stage-100) | stage 100 reached, for stages 22, 50 here |
| Requires | [Lessons learned](brv_school2.md#stage-102) | stage 102 reached, for stage 50 here |
| Requires | [Lessons learned](brv_school2.md#stage-104) | stage 104 reached, for stage 40 here |
| Requires | [Lessons learned](brv_school2.md#stage-120) | stage 120 reached, for stages 40, 50 here |
| Requires | [Lessons learned](brv_school2.md#stage-124) | stage 124 reached, for stage 40 here |
| Requires | [Lessons learned](brv_school2.md#stage-150) | stage 150 reached, for stage 50 here |
| Requires | [Lessons learned](brv_school2.md#stage-152) | stage 152 reached, for stage 40 here |
| Requires | [A cat and mouse game](cat_and_mouse.md#stage-60) | stage 60 reached, for stage 60 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-60) | stage 60 must NOT be reached, for stage 10 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-100) | stage 100 must NOT be reached, for stage 30 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-102) | stage 102 must NOT be reached, for stage 30 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-104) | stage 104 must NOT be reached, for stage 30 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-120) | stage 120 must NOT be reached, for stage 30 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-122) | stage 122 must NOT be reached, for stage 30 here |
| Blocked by | [Lessons learned](brv_school2.md#stage-124) | stage 124 must NOT be reached, for stage 30 here |
| Unlocks | [Lessons learned](brv_school2.md#stage-40) | stage 40 there needs stage 21 here |
| Unlocks | [Lessons learned](brv_school2.md#stage-150) | stage 150 there needs stage 30 here |
| Unlocks | [Lessons learned](brv_school2.md#stage-220) | stage 220 there needs stage 22 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | You run around in classroom.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-20"></span>20 | Talked to Golin.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-21"></span>21 | Thieves?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-22"></span>22 | Dueled Golin with school weapons.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | wearing [Paper shield](../items/brv_school_shield.md), wearing [Wooden sword](../items/brv_school_sword.md) | – |
| <span id="stage-30"></span>30 | Talked to the statue. | [Statue](../monsters/brv_school_statue.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | – |
| <span id="stage-40"></span>40 | Reward: cake<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md))<br>stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) | stage 22 | sets stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220) |
| <span id="stage-42"></span>42 | Reward: cake got | [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) | stage 40 | gives 1× [Cake](../items/cake.md)<br>gives 8× [Piece of cake](../items/cake_piece.md) |
| <span id="stage-50"></span>50 | Pupils ran out<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven school](../maps/brimhaven_school.md).</span> | stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md)<br>[Pupil](../monsters/brv_pupil1.md) ([brimhaven_school](../maps/brimhaven_school.md)) | – | removes monsters from brimhaven_school<br>sets stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122)<br>clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120)<br>faction “brv_fct_school_duel” set to 10<br>sets stage 110 of [Lessons learned](../quests/brv_school2.md#stage-110) |
| <span id="stage-60"></span>60 | 60=banned fromtower<br><span class="qnote">⚡ A scripted event can now trigger on [Brimhaven2](../maps/brimhaven2.md).</span><br><span class="qnote">🔒 An area on [Brimhaven church](../maps/brimhaven_church.md) becomes blocked off.</span> | walking into a blocked passage on [brimhaven_church_upstairs](../maps/brimhaven_church_upstairs.md) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 3 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-10); NOT reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60) → **stage 10**. NPC: “No walking around in my lessons! Please sit down.”
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-10); NOT reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60) → **stage 10**. NPC: “No walking around in my lessons! Please sit down.”
    3. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically → **stage 10**. NPC: “No walking around in my lessons! Please sit down.”

???+ note "Stage 20: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “[whispering] What's up?” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30); NOT reached stage 20 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-20) → **stage 20**. NPC: “Be quiet, please. How can I concentrate if you are talking all the time? Where was I? I had better start anew.”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “[whispering] What's up?” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30); NOT reached stage 20 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-20) → **stage 20**. NPC: “Be quiet, please. How can I concentrate if you are talking all the time? Where was I? I had better start anew.”

???+ note "Stage 21: 2 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “Thieves?!” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30) → **stage 21**. NPC: “Yes thieves. Dishonorable men who cut cheeky children's neck for a few pennies. But ... where was I?”
    2. Talk to [Golin](../monsters/golin.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Thieves?!” — **conditions:** reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30) → **stage 21**. NPC: “Yes thieves. Dishonorable men who cut cheeky children's neck for a few pennies. But ... where was I?”

???+ note "Stage 22: 1 route"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); wearing [Wooden sword](../items/brv_school_sword.md); wearing [Paper shield](../items/brv_school_shield.md) → **stage 22**

???+ note "Stage 30: 1 route"

    1. Talk to [Statue](../monsters/brv_school_statue.md) ([brimhaven_school](../maps/brimhaven_school.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-30); NOT reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); NOT reached stage 102 of [Lessons learned](../quests/brv_school2.md#stage-102); NOT reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104); NOT reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120); NOT reached stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122); NOT reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124) → **stage 30**. NPC: “Leave me alone! What do you want of me?”

???+ note "Stage 40: 4 routes"

    1. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “It was no big thing...” — **conditions:** reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104); reached stage 22 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-22) → **stage 40**. NPC: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.”
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → choose “Thank you.” — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120) → **stage 40**; also sets stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220). NPC: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.”
    3. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “It was no big thing...” — **conditions:** reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124) → **stage 40**; also sets stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220). NPC: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.”
    4. Talk to [Teacher](../monsters/brv_teacher.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Yes, it seems that it had enchanted you all.” — **conditions:** reached stage 152 of [Lessons learned](../quests/brv_school2.md#stage-152) → **stage 40**. NPC: “We all owe our lives to you! As a reward, you can get yourself a cake from Arlish at the general store. Tell her I…”

???+ note "Stage 42: 2 routes"

    1. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “No, thank you. I prefer the cake as a whole.” — **conditions:** reached stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40); NOT reached stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42) → **stage 42**; also gives 1× [Cake](../items/cake.md). NPC: “I'm afraid you'll get a stomachache if you eat the whole cake at once. But well - here you have it.”
    2. Talk to [Arlish](../monsters/arlish.md) ([brimhaven_general1](../maps/brimhaven_general1.md)) → choose “Yes, please.” — **conditions:** reached stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40); NOT reached stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42) → **stage 42**; also gives 8× [Piece of cake](../items/cake_piece.md). NPC: “Well, I'm cutting the cake into 8 large pieces. I hope they taste good to you!”

???+ note "Stage 50: 4 routes"

    1. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 100 of [Lessons learned](../quests/brv_school2.md#stage-100); killed 1× [Golin](../monsters/golin.md); reached stage 102 of [Lessons learned](../quests/brv_school2.md#stage-102); NOT reached stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50) → **stage 50**; also removes monsters from brimhaven_school. NPC: “When the other students see how you killed Golin, a panic breaks out. Screaming, they all run out of the building.”
    2. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120); killed 1× [Teacher](../monsters/brv_teacher.md) → **stage 50**; also sets stage 122 of [Lessons learned](../quests/brv_school2.md#stage-122), clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), faction “brv_fct_school_duel” set to 10, removes monsters from brimhaven_school. NPC: “When the little students see how you killed their teacher, a panic breaks out. Screaming, they all run out of the…”
    3. stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) → the conversation leads here automatically — **conditions:** reached stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150); NOT reached stage 50 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-50) → **stage 50**; also removes monsters from brimhaven_school. NPC: “A panic breaks out. Screaming, all the little students run out of the building. Just Golin remains.”
    4. Talk to [Pupil](../monsters/brv_pupil1.md) ([brimhaven_school](../maps/brimhaven_school.md)) → choose “Wait, I'll show you...” — **conditions:** reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60) → **stage 50**; also sets stage 110 of [Lessons learned](../quests/brv_school2.md#stage-110), removes monsters from brimhaven_school. NPC: “[He jumps up and runs screaming out of the room. The other little students follow in panic.]”

???+ note "Stage 60: 1 route"

    1. walking into a blocked passage on [brimhaven_church_upstairs](../maps/brimhaven_church_upstairs.md) → the conversation leads here automatically — **conditions:** faction “brv_ring_bells” ≥ 6; reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60) → **stage 60**. NPC: “That does it! Leave this tower immediately! And don't you ever dare come back!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 14 lines added |
| [v0.7.12](../versions/0.7.12.md) | stages added: 60<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_nondisplay2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_nondisplay2` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 21, 22, 30, 40, 42, 50, 60 |
    | Dialogue nodes setting stages | 10: `brv_school_enter_20`, 20: `brv_school_history_52`, 21: `brv_school_history_84`, 22: `brv_school_check_duel_11`, 30: `brv_school_statue_20`, 40: `brv_teacher_104a_20`, 40: `brv_teacher_124_20`, 40: `brv_teacher_152_90`, 42: `arlish_14`, 42: `arlish_16`, 50: `brv_school_check_duel_14a`, 50: `brv_school_check_duel_20`, 50: `brv_school_check_duel_38`, 60: `brv_ring_bells_90` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
