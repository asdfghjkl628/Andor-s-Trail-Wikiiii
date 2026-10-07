# About a girl

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `about_a_girl` |
| **In journal** | Yes |
| **Stages** | 9 (completes at 90) |
| **Started by** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) |
| **NPCs involved** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md), [Thalen](../monsters/thalen.md) |
| **Locations** | [undertell_3_00](../maps/undertell_3_00.md), [undertell_3_lava_00](../maps/undertell_3_lava_00.md) |
| **Total XP** | 10,207 |
| **Related quests** | 2 |

</div>

## Overview

> Two Elytharan slave ghosts spoke quietly of another who has not joined them at the table. They said she still hides east of them, afraid the Shades might return.

## Prerequisites to start

Start with [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)). Required:

- reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10)
- NOT reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The fifth master](fifth_master.md#stage-90) | stage 90 reached, for stage 50 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-85) | stage 85 reached, for stage 80 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-85) | stage 85 there needs stage 70 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-90) | stage 90 there needs stage 40 here |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-85) | reaching stage 80 here closes stage 85 there |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-90) | reaching stage 70 here closes stage 90 there |
| Blocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-95) | reaching stage 50 here closes stage 95 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Two Elytharan slave ghosts spoke quietly of another who has not joined them at the table. They said she still hides east of them, afraid the Shades might return. | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) | – | – |
| <span id="stage-20"></span>20 | The ghosts said the girl believed she could protect herself with a folded copper talisman she made long ago, but she lost it before she could hide it away from the evil of Undertell. | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | They remembered that such objects were sometimes taken during inspections, gathered with other personal effects and carried upward to the Masters. | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I was told that one of the Masters may still possess the folded copper talisman, kept not for protection, but for understanding. | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) | stage 30 | spawns monsters on undertell_3_12 |
| <span id="stage-50"></span>50 | A Master acknowledged the talisman when I asked about it. He spoke of fear made solid, and said such fear was useful to those who taught the Shadow obedience rather than faith. It can be found in the "lower records", whatever that means.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Undertell 4 00](../maps/undertell_4_00.md).</span> | [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) | stage 40 | – |
| <span id="stage-60"></span>60 | In the Undertell archival room, I found the folded coin talisman. | walking into a blocked passage on [undertell_archive2](../maps/undertell_archive2.md) | – | gives 1× [Folded copper talisman](../items/folded_copper_talisman.md) |
| <span id="stage-70"></span>70 | I found the terrified girl hiding behind a collapsed rock wall. She would not approach me, nor leave her hiding place. | walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) | stage 40 | – |
| <span id="stage-80"></span>80 | I tossed the folded copper talisman to her. Only then did she step forward, no longer clinging to the corner she had claimed as safety. | walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) | stage 70 | removes monsters from undertell_3_12<br>spawns monsters on undertell_3_00 |
| <span id="stage-90"></span>90 | The girl rejoined the others at the table. The Elytharan ghosts spoke her name softly, as if afraid to lose her again. **(completes quest)** | [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) | stage 80 | 10,207 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10); NOT reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20) → **stage 10**. NPC: “There is another. A girl. She never came back here when the shades fell. Instead, she hides east of here. Probably in…”

???+ note "Stage 20: 1 route"

    1. Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) → choose “What did she make?” — **conditions:** reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10); NOT reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20) → **stage 20**. NPC: “A folded coin. Copper. She believed evil could be trapped if it could not breathe.”

???+ note "Stage 30: 1 route"

    1. Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) → choose “I am still trying to understand what happened to the talisman.” — **conditions:** reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20); NOT reached stage 30 of [About a girl](../quests/about_a_girl.md#stage-30) → **stage 30**. NPC: “They used to gather our things. Count them. Decide what mattered.”

???+ note "Stage 40: 1 route"

    1. Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) → choose “Then where should I look?” — **conditions:** latest stage of [About a girl](../quests/about_a_girl.md#stage-30) is 30 → **stage 40**; also spawns monsters on undertell_3_12. NPC: “With those who believed fear could be shaped. Go to the Masters.”

???+ note "Stage 50: 1 route"

    1. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → choose “Where do I find it?” — **conditions:** reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90); reached stage 40 of [About a girl](../quests/about_a_girl.md#stage-40); NOT reached stage 50 of [About a girl](../quests/about_a_girl.md#stage-50) → **stage 50**. NPC: “In the lower records. Where discarded faith is kept for study, not mercy.”

???+ note "Stage 60: 1 route"

    1. walking into a blocked passage on [undertell_archive2](../maps/undertell_archive2.md) → choose “[Take the folded copper piece.]” — **conditions:** NOT reached stage 60 of [About a girl](../quests/about_a_girl.md#stage-60) → **stage 60**; also gives 1× [Folded copper talisman](../items/folded_copper_talisman.md). NPC: “You grab the coin off the shelf.”

???+ note "Stage 70: 1 route"

    1. walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [About a girl](../quests/about_a_girl.md#stage-40); NOT reached stage 70 of [About a girl](../quests/about_a_girl.md#stage-70) → **stage 70**. NPC: “THIS PERSON IS TRYING TO DESTROY ME!”

???+ note "Stage 80: 1 route"

    1. walking into a blocked passage on [undertell_3_12](../maps/undertell_3_12.md) → choose “I will meet you there.” — **conditions:** reached stage 70 of [About a girl](../quests/about_a_girl.md#stage-70); NOT reached stage 80 of [About a girl](../quests/about_a_girl.md#stage-80); reached stage 85 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-85) → **stage 80**; also removes monsters from undertell_3_12, spawns monsters on undertell_3_00. NPC: “My name is Syrra. Thank you for bringing it back.”

???+ note "Stage 90: 1 route"

    1. Talk to [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md) ([undertell_3_00](../maps/undertell_3_00.md)) → choose “Then this is enough.” — **conditions:** reached stage 80 of [About a girl](../quests/about_a_girl.md#stage-80); NOT reached stage 90 of [About a girl](../quests/about_a_girl.md#stage-90) → **stage 90**. NPC: “It is.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=about_a_girl.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `about_a_girl` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90 |
    | Dialogue nodes setting stages | 10: `elytharan_liberated_ghost_about_girl_10`, 20: `elytharan_liberated_ghost_about_girl_10c`, 30: `elytharan_liberated_ghost_about_girl_20b`, 40: `elytharan_liberated_ghost_about_girl_30b`, 50: `master_thalen_about_girl_90`, 60: `folded_coin_25`, 70: `about_girl_meet_10`, 80: `about_girl_meet_90`, 90: `about_girl_syrra_90c` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
