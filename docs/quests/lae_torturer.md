---
description: "Shadow of the torturer is a quest in Andor's Trail, started by Laeroth prisoner (laerothprison4). 16 stages. In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story."
---

# Shadow of the torturer

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lae_torturer` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 80, 130) |
| **Started by** | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4a) |
| **NPCs involved** | [Dark watch](../monsters/lae_demon4.md#v-lae_demon4b), [Dark watch](../monsters/lae_demon4.md), [Dark watch](../monsters/lae_demon4.md#v-lae_demon9), [Kotheses](../monsters/kotheses.md), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4), [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4i) +1 |
| **Locations** | [laerothprison4](../maps/laerothprison4.md), [laerothprison7](../maps/laerothprison7.md) |
| **Related quests** | 1 |

</div>

## Overview

> In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story.

## Prerequisites to start

Start with [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)). Required:

- reached stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31)
- reached stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33)
- reached stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-31) | stage 31 reached, for stages 5, 10 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-33) | stage 33 reached, for stages 5, 10 here |
| Requires | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-34) | stage 34 reached, for stages 5, 10 here |
| Blocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-31) | reaching stage 110 here closes stage 31 there |
| Blocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-32) | reaching stage 110 here closes stage 32 there |
| Blocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-33) | reaching stage 110 here closes stage 33 there |
| Blocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-34) | reaching stage 110 here closes stage 34 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | In the dungeon of the mansion I found some ghosts of prisoners. One of them told me their story.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) | – | changes map laerothprison4 |
| <span id="stage-10"></span>10 | I have agreed to help the spirits in the prison be free of the prison torturer. | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) | – | – |
| <span id="stage-20"></span>20 | I didn't want to help the spirits in the prison be free of the prison torturer.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md))<br>stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) | stage 25 | – |
| <span id="stage-25"></span>25 | Kotheses the torturer offered to teach me his art, as he had done for Andor before.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothprison7](../maps/laerothprison7.md).</span> | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | – | removes monsters from laerothprison4<br>spawns monsters on laerothprison4 |
| <span id="stage-30"></span>30 | I accepted his offer to apprentice with him.<br><span class="qnote">⚡ A scripted event can now trigger on [Laerothprison7](../maps/laerothprison7.md).</span> | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | – | – |
| <span id="stage-35"></span>35 | Kotheses gave me an Oegyth crystal. | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | – | gives 1× [Oegyth crystal](../items/oegyth.md) |
| <span id="stage-40"></span>40 | In order to imprison the released prisoners again, I should call the demon guard by throwing an Oegyth crystal into the abyss. | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | stage 35 | – |
| <span id="stage-50"></span>50 | Kotheses scolded me because I killed his precious demons. | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | – | – |
| <span id="stage-60"></span>60 | I declined the offer to become his apprentice. | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | – | – |
| <span id="stage-70"></span>70 | Kotheses attacked me. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-80"></span>80 | I told the prisoners that I had killed their torturer. Now they could get peace. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md))<br>stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) | stage 25 | – |
| <span id="stage-100"></span>100 | I have thrown an Oegyth crystal down into the abyss to call for the dark watch.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison7](../maps/laerothprison7.md).</span> | stepping on a trigger on [laerothprison7](../maps/laerothprison7.md) | hand over 1× [Oegyth crystal](../items/oegyth.md) | spawns monsters on laerothprison7 |
| <span id="stage-110"></span>110 | I got back the Oegyth crystal from the chief of the Demon guard. | [Dark watch](../monsters/lae_demon4.md#v-lae_demon9) ([laerothprison7](../maps/laerothprison7.md)) | – | gives 1× [Oegyth crystal](../items/oegyth.md)<br>removes monsters from laerothprison7<br>spawns monsters on laerothprison7 |
| <span id="stage-114"></span>114 | I ordered the demons to watch over the prisoners. | [Dark watch](../monsters/lae_demon4.md) ([laerothprison7](../maps/laerothprison7.md)) | – | removes monsters from laerothprison7<br>spawns monsters on laerothprison4<br>changes map laerothprison4<br>removes monsters from laerothprison4<br>clears stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31)<br>clears stage 32 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-32)<br>clears stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33)<br>clears stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34) |
| <span id="stage-120"></span>120 | I took my leave from Kotheses, who, incidentally, forgot to reclaim his Oegyth crystal. | [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) | stage 110 | – |
| <span id="stage-130"></span>130 | Everything was in order when I left. The prisoners were back in their cells, and the Demon guard were on duty again. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Laerothprison4](../maps/laerothprison4.md).</span> | [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md))<br>stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) | stage 114, stage 25 | – |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) → choose “What sort of help?” — **conditions:** reached stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34) → **stage 5**; also changes map laerothprison4. NPC: “It didn't work, because we had so little life left anyway.”

???+ note "Stage 10: 1 route"

    1. Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) → choose “OK. I'll do it. I am not afraid of a few monsters!” — **conditions:** reached stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31); reached stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33); reached stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34); NOT reached stage 20 of [Shadow of the torturer](../quests/lae_torturer.md#stage-20) → **stage 10**. NPC: “Thank you! But beware! He has guards that are like him. They may appear to be human at first glance, but they are not!”

???+ note "Stage 20: 2 routes"

    1. Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) → the conversation leads here automatically — **conditions:** reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); NOT killed 1× [Kotheses](../monsters/kotheses.md) → **stage 20**. NPC: “Ohhh! What will become of us?”
    2. stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) → the conversation leads here automatically — **conditions:** reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); NOT killed 1× [Kotheses](../monsters/kotheses.md) → **stage 20**. NPC: “Ohhh! What will become of us?”

???+ note "Stage 25: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → the conversation leads here automatically — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md) → **stage 25**; also removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4. NPC: “Would you like to learn the trade of a torturer?”

???+ note "Stage 30: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → choose “Very gladly. I always like to learn new things.” — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md); NOT reached stage 60 of [Shadow of the torturer](../quests/lae_torturer.md#stage-60) → **stage 30**. NPC: “OK, then let's get started. This is a very important job, you know?”

???+ note "Stage 35: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → choose “Sigh.” — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md); NOT reached stage 60 of [Shadow of the torturer](../quests/lae_torturer.md#stage-60); NOT reached stage 35 of [Shadow of the torturer](../quests/lae_torturer.md#stage-35) → **stage 35**; also gives 1× [Oegyth crystal](../items/oegyth.md). NPC: “Here take this Oegyth crystal.”

???+ note "Stage 40: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → choose “What?!” — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md); NOT reached stage 60 of [Shadow of the torturer](../quests/lae_torturer.md#stage-60); reached stage 35 of [Shadow of the torturer](../quests/lae_torturer.md#stage-35) → **stage 40**. NPC: “Do it. Then run for your life back to me so that I can protect you from them.”

???+ note "Stage 50: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → the conversation leads here automatically → **stage 50**. NPC: “Why do you kill my precious demons?! I told you to stay here beside me!”

???+ note "Stage 60: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → choose “That is no job for me.” — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md); NOT reached stage 30 of [Shadow of the torturer](../quests/lae_torturer.md#stage-30) → **stage 60**. NPC: “What a pity. At least let me warn you about the prisoners above.”

???+ note "Stage 80: 2 routes"

    1. Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) → the conversation leads here automatically — **conditions:** reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); killed 1× [Kotheses](../monsters/kotheses.md) → **stage 80**. NPC: “Ooooh! We are eternally grateful!”
    2. stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) → the conversation leads here automatically — **conditions:** killed 1× [Kotheses](../monsters/kotheses.md) → **stage 80**. NPC: “Ooooh! We are eternally grateful!”

???+ note "Stage 100: 1 route"

    1. stepping on a trigger on [laerothprison7](../maps/laerothprison7.md) → choose “Let's throw an oegyth crystal down there.” — **conditions:** NOT reached stage 100 of [Shadow of the torturer](../quests/lae_torturer.md#stage-100); hand over 1× [Oegyth crystal](../items/oegyth.md) → **stage 100**; also spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7, spawns monsters on laerothprison7. NPC: “You hear an uproar from far away. But coming nearer and nearer.”

???+ note "Stage 110: 1 route"

    1. Talk to [Dark watch](../monsters/lae_demon4.md#v-lae_demon9) ([laerothprison7](../maps/laerothprison7.md)) → the conversation leads here automatically → **stage 110**; also gives 1× [Oegyth crystal](../items/oegyth.md), removes monsters from laerothprison7, spawns monsters on laerothprison7. NPC: “[hollow voice] Take back your glass ball, brave little human.”

???+ note "Stage 114: 1 route"

    1. Talk to [Dark watch](../monsters/lae_demon4.md) ([laerothprison7](../maps/laerothprison7.md)) → the conversation leads here automatically → **stage 114**; also removes monsters from laerothprison7, removes monsters from laerothprison7, spawns monsters on laerothprison4, spawns monsters on laerothprison4, changes map laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, removes monsters from laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, spawns monsters on laerothprison4, clears stage 31 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-31), clears stage 32 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-32), clears stage 33 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-33), clears stage 34 of [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-34). NPC: “Command us!”

???+ note "Stage 120: 1 route"

    1. Talk to [Kotheses](../monsters/kotheses.md) ([laerothprison7](../maps/laerothprison7.md)) → the conversation leads here automatically — **conditions:** NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon9); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon7); NOT killed 1× [Dark watch](../monsters/lae_demon4.md#v-lae_demon5); NOT killed 1× [Dark watch](../monsters/lae_demon4.md); reached stage 110 of [Shadow of the torturer](../quests/lae_torturer.md#stage-110) → **stage 120**. NPC: “I see it in your eyes - you want to leave too. Like your brother.”

???+ note "Stage 130: 2 routes"

    1. Talk to [Laeroth prisoner](../monsters/lae_prisoner.md#v-lae_prisoner4) ([laerothprison4](../maps/laerothprison4.md)) → the conversation leads here automatically — **conditions:** reached stage 25 of [Shadow of the torturer](../quests/lae_torturer.md#stage-25); reached stage 114 of [Shadow of the torturer](../quests/lae_torturer.md#stage-114); NOT reached stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130) → **stage 130**. NPC: “Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.”
    2. stepping on a trigger on [laerothprison4](../maps/laerothprison4.md) → the conversation leads here automatically — **conditions:** reached stage 114 of [Shadow of the torturer](../quests/lae_torturer.md#stage-114); NOT reached stage 130 of [Shadow of the torturer](../quests/lae_torturer.md#stage-130) → **stage 130**. NPC: “Everything is in order now. The prisoners are back in their cells, and the Demon guards are on duty again.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.8.12.1](../versions/0.8.12.1.md) | stage 40 journal text changed; stage 100 journal text changed; stage 130 journal text changed<br>Dialogue: 1 line changed<br>· text: “Okay, then let's get started. This is a very important job, you know?” → “OK, then let's get started. This is a very important job, you know?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lae_torturer.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lae_torturer` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 20, 25, 30, 35, 40, 50, 60, 70, 80, 100, 110, 114, 120, 130 |
    | Dialogue nodes setting stages | 5: `lae_prison_02b`, 10: `lae_prison_03`, 20: `lae_prison_3a`, 25: `lae_torturer_10a`, 30: `lae_torturer_30`, 35: `lae_torturer_44`, 40: `lae_torturer_48`, 50: `lae_torturer_2`, 60: `lae_torturer_60`, 80: `lae_prison_end_20`, 100: `lae_demon_call_20`, 110: `lae_demon9`, 114: `lae_demon4`, 120: `lae_torturer_110`, 130: `lae_prison_end_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
