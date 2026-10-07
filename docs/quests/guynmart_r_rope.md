---
description: "guynmart rope is a hidden quest in Andor's Trail, started by stepping on a trigger on guynmart_wood_3. 3 stages. 1=up"
---

# guynmart rope

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `guynmart_r_rope` |
| **In journal** | No (hidden flag) |
| **Stages** | 3 |
| **Started by** | stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md), stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) |
| **NPCs involved** | [Rob](../monsters/guynmart_rob.md#v-guynmart_rob6) |
| **Locations** | [guynmart_wood_7](../maps/guynmart_wood_7.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1=up

## Prerequisites to start

None: talk to stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Roses](guynmart.md#stage-80) | stage 80 reached, for stage 11 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=up<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 3](../maps/guynmart_wood_3.md).</span> | stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) | – | – |
| <span id="stage-2"></span>2 | 2=down<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 3](../maps/guynmart_wood_3.md).</span> | stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) | stage 1 | clears stage 1 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-1)<br>applies condition stunned<br>applies condition bone_fracture |
| <span id="stage-11"></span>11 | 11=rope2 set<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 7](../maps/guynmart_wood_7.md).</span><br><span class="qnote">🗺️ Part of [Guynmart wood 7](../maps/guynmart_wood_7.md) visibly changes.</span> | stepping on a trigger on [guynmart_wood_7](../maps/guynmart_wood_7.md)<br>[Rob](../monsters/guynmart_rob.md#v-guynmart_rob6) ([guynmart_wood_7](../maps/guynmart_wood_7.md)) | – | removes monsters from guynmart_wood_7 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 2 routes"

    1. stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) → the conversation leads here automatically → **stage 1**
    2. stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) → the conversation leads here automatically → **stage 1**

???+ note "Stage 2: 2 routes"

    1. stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-1) → **stage 2**; also clears stage 1 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-1), applies condition stunned, applies condition bone_fracture
    2. stepping on a trigger on [guynmart_wood_3](../maps/guynmart_wood_3.md) → the conversation leads here automatically — **conditions:** reached stage 1 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-1) → **stage 2**; also clears stage 1 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-1), applies condition stunned, applies condition bone_fracture

???+ note "Stage 11: 3 routes"

    1. stepping on a trigger on [guynmart_wood_7](../maps/guynmart_wood_7.md) → choose “Let's try it.” → **stage 11**
    2. Talk to [Rob](../monsters/guynmart_rob.md#v-guynmart_rob6) ([guynmart_wood_7](../maps/guynmart_wood_7.md)) → choose “Yes. Could you drop the rope down?” → **stage 11**; also removes monsters from guynmart_wood_7. NPC: “Of course. There. But I am in a hurry and must leave now.”
    3. stepping on a trigger on [guynmart_wood_7](../maps/guynmart_wood_7.md) → choose “Yes. Could you drop the rope down?” — **conditions:** NOT reached stage 11 of [guynmart rope (hidden flag)](../quests/guynmart_r_rope.md#stage-11); reached stage 80 of [Roses](../quests/guynmart.md#stage-80) → **stage 11**; also removes monsters from guynmart_wood_7. NPC: “Of course. There. But I am in a hurry and must leave now.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_r_rope.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_r_rope.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_r_rope.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_r_rope.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=guynmart_r_rope.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `guynmart_r_rope` |
    | showInLog | 0 |
    | Stage IDs | 1, 2, 11 |
    | Dialogue nodes setting stages | 1: `guynmart_s_rope_u2`, 2: `guynmart_s_rope_d_10`, 11: `guynmart_s_rope2_20`, 11: `guynmart_rob6_30` |
    | Dialogue nodes clearing stages | 1: `guynmart_s_rope_r2`, 1: `guynmart_s_rope_d_10`, 2: `guynmart_s_rope_r2` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
