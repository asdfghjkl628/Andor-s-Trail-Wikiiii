# Echoes of enchantment

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `echoes_of_enchantment` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 14) |
| **Started by** | stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) |
| **NPCs involved** | [Gamjee](../monsters/gamjee_oc.md), [Gamjee](../monsters/gamjee.md), [Godelieve](../monsters/village_godelieve.md) |
| **Locations** | [gamjee_well_4_1](../maps/gamjee_well_4_1.md), [wexlow_village_nw_house](../maps/wexlow_village_nw_house.md) |
| **Total XP** | 5,200 |
| **Related quests** | 1 |

</div>

## Overview

> At the Wexlow well, I angered something evil and powerful (named Gamjee, I think) to the point that it pulled me down into the well. I've landed at the well's bottom severely injured, but alive.

## Prerequisites to start

Start with stepping on a trigger on [wexlow_village](../maps/wexlow_village.md). Required:

- NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10)
- NOT reached stage 11 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11)
- NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13)
- NOT reached stage 9 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9)
- hand over 1× [Small rock](../items/rock.md)
- hand over 1× [Leather boots](../items/boots1.md)
- hand over 1× [Rotten meat](../items/meat2.md)
- hand over 1× [Bone](../items/bone.md)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-3) | stage 3 reached, for stage 11 here |
| Requires | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-4) | stage 4 reached, for stage 9 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-4) | stage 4 there needs stage 5 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-5) | stage 5 there needs stage 5 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-6) | stage 6 there needs stages 5, 8 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-9) | stage 9 there needs stage 12 here |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-2) | reaching stages 9, 10, 11, 13 here closes stage 2 there |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-3) | reaching stages 5, 8, 13 here closes stage 3 there |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-4) | reaching stage 8 here closes stage 4 there |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-5) | reaching stages 5, 8, 13 here closes stage 5 there |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-6) | reaching stages 8, 12 here closes stage 6 there |
| Blocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-11) | reaching stage 10 here closes stage 11 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | At the Wexlow well, I angered something evil and powerful (named Gamjee, I think) to the point that it pulled me down into the well. I've landed at the well's bottom severely injured, but alive.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wexlow village](../maps/wexlow_village.md).</span> | stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) | hand over 1× [Bone](../items/bone.md), hand over 1× [Leather boots](../items/boots1.md), hand over 1× [Rotten meat](../items/meat2.md), hand over 1× [Small rock](../items/rock.md) | 500 XP<br>applies condition dazed<br>applies condition concussion<br>applies condition bleeding_wound<br>moves you to [gamjee_well_1](../maps/gamjee_well_1.md) |
| <span id="stage-2"></span>2 | After I landed with a thud at the bottom of the well and being concussed, I began to hear sounds off in the distance. Were they voices? Were they even real? Maybe a symptom of the concussion perhaps?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well 1 1](../maps/gamjee_well_1_1.md).</span> | stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) | – | – |
| <span id="stage-3"></span>3 | After I landed with a thud at the bottom of the well and being concussed, I began to hear sounds off in the distance. Were they voices? Were they even real? Are they the voices of something more sinister?<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well 1 1](../maps/gamjee_well_1_1.md).</span> | stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) | – | – |
| <span id="stage-4"></span>4 | The voices I thought I heard earlier seem to be persistent and seemed to be getting louder. It was hard to tell if they're real or just a figment of my imagination.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well 2 1](../maps/gamjee_well_2_1.md).</span> | stepping on a trigger on [gamjee_well_2_1](../maps/gamjee_well_2_1.md) | – | – |
| <span id="stage-5"></span>5 | Deep inside the well's tunnels, I found eight people being held captive inside a very deep pit.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).</span> | walking into a blocked passage on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) | – | – |
| <span id="stage-6"></span>6 | I learned that these people are held captive by a troll and they need me to find a way to free them.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).</span> | stepping on a trigger on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) | – | – |
| <span id="stage-7"></span>7 | I met the troll named Gamjee and listened to what he had to say. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-8"></span>8 | In an attempt to help Gamjee and the villagers, I have facilitated a conversation between Gamjee and one of the villagers. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | stage 5 | removes monsters from gamjee_well_jail_cells<br>spawns monsters on gamjee_well_4_1 |
| <span id="stage-9"></span>9 | I killed Gamjee and in doing so, I found a rope that I think might be helpful in freeing those people in that pit.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well 4 1](../maps/gamjee_well_4_1.md).</span> | stepping on a trigger on [gamjee_well_4_1](../maps/gamjee_well_4_1.md) | – | 1,200 XP |
| <span id="stage-10"></span>10 | The villagers have been freed. I should visit them back in their village of Wexlow.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Guynmart wood 7](../maps/guynmart_wood_7.md).</span><br><span class="qnote">🗺️ Part of [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md) visibly changes.</span><br><span class="qnote">🗺️ Part of [Guynmart wood 7](../maps/guynmart_wood_7.md) visibly changes.</span> | stepping on a trigger on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) | carry 1× [Gamjee's rope](../items/gamjee_rope.md), hand over 1× [Gamjee's rope](../items/gamjee_rope.md), stage 5 | removes monsters from gamjee_well_jail_cells<br>spawns monsters on gamjee_well_jail_cells<br>spawns monsters on wexlow_village<br>spawns monsters on wexlow_village_nw_house<br>spawns monsters on wexlow_village_sw_house<br>spawns monsters on wexlow_village_se_house<br>removes monsters from wexlow_village |
| <span id="stage-11"></span>11 | I killed Gamjee and in doing so, I realized that I really should go investigate the voices I heard earlier.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Gamjee well 4 1](../maps/gamjee_well_4_1.md).</span> | stepping on a trigger on [gamjee_well_4_1](../maps/gamjee_well_4_1.md) | – | 1,000 XP |
| <span id="stage-12"></span>12 | The villagers and Gamjee agreed to a schedule for using the well, ensuring everyone has access to water without conflict. But the villagers are still in the pit. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | stage 5, stage 8 | 2,000 XP<br>removes monsters from gamjee_well_4_1<br>sets stage 6 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-6)<br>spawns monsters on wexlow_village |
| <span id="stage-13"></span>13 | After the villagers and Gamjee agreed to a compromise, Gamjee gave me a rope and instructed me to use it to free the remaining villagers in the pit. | [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) | stage 12, stage 5, stage 8 | gives 1× [Gamjee's rope](../items/gamjee_rope.md) |
| <span id="stage-14"></span>14 | I've visited the people of Wexlow Village after they made it home. They are happy to sleep in their own beds now. **(completes quest)** | [Godelieve](../monsters/village_godelieve.md) ([wexlow_village_nw_house](../maps/wexlow_village_nw_house.md)) | – | 500 XP |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 1: 1 route"

    1. stepping on a trigger on [wexlow_village](../maps/wexlow_village.md) → choose “[Throw a bone into the well]” — **conditions:** NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10); NOT reached stage 11 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 9 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9); hand over 1× [Small rock](../items/rock.md); hand over 1× [Leather boots](../items/boots1.md); hand over 1× [Rotten meat](../items/meat2.md); hand over 1× [Bone](../items/bone.md) → **stage 1**; also applies condition dazed, applies condition concussion, applies condition bleeding_wound, moves you to [gamjee_well_1](../maps/gamjee_well_1.md). NPC: “Suddenly, a powerful force grabs you and drags you down into the darkness of the well. You find yourself dazed,…”

???+ note "Stage 2: 1 route"

    1. stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) → the conversation leads here automatically — **conditions:** affected by concussion; NOT reached stage 2 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-2) → **stage 2**. NPC: “As you begin to traverse the tunnels, the dim light and damp air create an eerie atmosphere. Suddenly, you stop in…”

???+ note "Stage 3: 1 route"

    1. stepping on a trigger on [gamjee_well_1_1](../maps/gamjee_well_1_1.md) → the conversation leads here automatically — **conditions:** NOT affected by concussion; NOT reached stage 3 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-3); NOT reached stage 2 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-2) → **stage 3**. NPC: “As you begin to traverse the tunnels, the dim light and damp air create an eerie atmosphere. Suddenly, you stop in…”

???+ note "Stage 4: 1 route"

    1. stepping on a trigger on [gamjee_well_2_1](../maps/gamjee_well_2_1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 4 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-4) → **stage 4**. NPC: “You press on, the voices you thought you heard earlier seem to be growing louder now. It's hard to tell if they're…”

???+ note "Stage 5: 1 route"

    1. walking into a blocked passage on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) → choose “This must be it... the source of those voices.” — **conditions:** NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5) → **stage 5**. NPC: “As you step further into the room, you notice a large pit in the center, deep below the surface. The voices are…”

???+ note "Stage 6: 1 route"

    1. stepping on a trigger on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) → choose “How?” — **conditions:** NOT reached stage 6 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-6); NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10) → **stage 6**. NPC: “Go kill the giant troll that is holding us here. Then come back here to free us.”

???+ note "Stage 8: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “I'll do what I can. Let's talk to the villagers.” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8) → **stage 8**; also removes monsters from gamjee_well_jail_cells, spawns monsters on gamjee_well_4_1. NPC: “Let Gamjee call human with magic water.”

???+ note "Stage 9: 1 route"

    1. stepping on a trigger on [gamjee_well_4_1](../maps/gamjee_well_4_1.md) → the conversation leads here automatically — **conditions:** reached stage 4 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-4); killed 1× [Gamjee](../monsters/gamjee_oc.md); reached stage 9 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9) → **stage 9**. NPC: “Gamjee has grasped his last breath and now it's time to rescue those people.”

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) → choose “[Tie the rope to the rock]” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10); carry 1× [Gamjee's rope](../items/gamjee_rope.md); hand over 1× [Gamjee's rope](../items/gamjee_rope.md) → **stage 10**; also removes monsters from gamjee_well_jail_cells, spawns monsters on gamjee_well_jail_cells, removes monsters from gamjee_well_jail_cells, spawns monsters on wexlow_village, spawns monsters on wexlow_village_nw_house, spawns monsters on wexlow_village_sw_house, spawns monsters on wexlow_village_se_house, removes monsters from wexlow_village. NPC: “We are finally free!”

???+ note "Stage 11: 1 route"

    1. stepping on a trigger on [gamjee_well_4_1](../maps/gamjee_well_4_1.md) → the conversation leads here automatically — **conditions:** reached stage 3 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-3); killed 1× [Gamjee](../monsters/gamjee_oc.md); NOT reached stage 11 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11) → **stage 11**. NPC: “Gamjee has grasped his last breath when you realize that you really need to follow those voices.”

???+ note "Stage 12: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “Alright. Let's make this work.” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12) → **stage 12**; also removes monsters from gamjee_well_4_1, sets stage 6 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-6), spawns monsters on wexlow_village. NPC: “You human, go back village now.”

???+ note "Stage 13: 1 route"

    1. Talk to [Gamjee](../monsters/gamjee.md) ([gamjee_well_4_1](../maps/gamjee_well_4_1.md)) → choose “So our business here is done?” — **conditions:** reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8); reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12) → **stage 13**; also gives 1× [Gamjee's rope](../items/gamjee_rope.md). NPC: “Not same. Take rope, use to free others from pit.”

???+ note "Stage 14: 1 route"

    1. Talk to [Godelieve](../monsters/village_godelieve.md) ([wexlow_village_nw_house](../maps/wexlow_village_nw_house.md)) → choose “I'm just happy to see you guys safe.” — **conditions:** NOT reached stage 14 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-14) → **stage 14**. NPC: “I'm just happy to curl up with Godwin in our own bed tonight.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 13 lines added |
| [v0.8.13](../versions/0.8.13.md) | stage 1 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=echoes_of_enchantment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=echoes_of_enchantment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=echoes_of_enchantment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=echoes_of_enchantment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=echoes_of_enchantment.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `echoes_of_enchantment` |
    | showInLog | 1 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
    | Dialogue nodes setting stages | 1: `wexlow_well_map_change`, 2: `gamjee_well_hear_voices_1_1`, 3: `gamjee_well_hear_voices_1_2`, 4: `gamjee_well_hear_voices_2_1`, 5: `gamjee_well_discover_villagers_2`, 6: `troll_hollow_godelieve_4`, 8: `gamjee_compromise_2`, 9: `gamjee_killed_villagers_known`, 10: `gamjee_well_post_troll_rescue_3`, 11: `gamjee_killed_wo_villagers_known`, 12: `gamjee_compromise_9`, 13: `gamjee_compromise_10_no_ac`, 14: `village_godelieve_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
