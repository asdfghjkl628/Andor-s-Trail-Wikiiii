# A Feygard delicacy

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `feygard_delicacy` |
| **In journal** | Yes |
| **Stages** | 8 (completes at 8) |
| **Started by** | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) |
| **NPCs involved** | [Philippa](../monsters/village_philippa.md) |
| **Locations** | [wexlow_village_se_house](../maps/wexlow_village_se_house.md) |
| **Total XP** | 5,049 |
| **Related quests** | 2 |

</div>

## Overview

> Philippa, one of the lovely Feygard loyalist ladies from Wexlow that I rescued from Gamjee the troll has informed me that she is a master baker.

## Prerequisites to start

Start with [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)). Required:

- NOT reached stage 1 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-1)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-188) | stage 188 there needs stage 5 here |
| Unlocks | [feygard_nondisplayed (hidden flag)](feygard_nondisplayed.md#stage-12) | stage 12 there needs stage 7 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | Philippa, one of the lovely Feygard loyalist ladies from Wexlow that I rescued from Gamjee the troll has informed me that she is a master baker. | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | – | – |
| <span id="stage-2"></span>2 | Philippa has educated me about what a "Feydelight" is. | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | stage 1 | – |
| <span id="stage-3"></span>3 | In return for my helping to rescue Philippa, she's stated that she could make a "Feydelight" for me if I provide her with all of the ingredients necessary to bake one. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-4"></span>4 | I need to find dough, two eggs, wine, butter, honey and five Feygard fig fruits. I can find the figs in Feygard, but maybe I could find some along the Duleian Road too? | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | – | – |
| <span id="stage-5"></span>5 | She told me that I can find the dough in Brightport or Feygard, but I could find a baker in just about any town. | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | stage 4 | – |
| <span id="stage-6"></span>6 | Philippa told me that I can get honey from a beekeeper. But where to find one? | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | carry 0× [Honey](../items/honey.md), stage 4 | – |
| <span id="stage-7"></span>7 | I gave Philippa all the ingredients needed to bake the Feydelight. Now I just need to come back later. | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | carry 1× [Butter](../items/butter.md), carry 1× [Honey](../items/honey.md), carry 1× [Raw dough](../items/dough.md), carry 1× [Wine](../items/guynmart_wine.md), carry 2× [Eggs](../items/eggs.md), carry 5× [Fig](../items/fig_fruit.md), hand over 1× [Butter](../items/butter.md), hand over 1× [Honey](../items/honey.md), hand over 1× [Raw dough](../items/dough.md), hand over 1× [Wine](../items/guynmart_wine.md), hand over 2× [Eggs](../items/eggs.md), hand over 5× [Fig](../items/fig_fruit.md), stage 4 | starts timer “feydelight_baking” |
| <span id="stage-8"></span>8 | I have received my Feydelight from Philippa.  **(completes quest)** | [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | stage 7 | 5,049 XP<br>gives 1× [Feydelight](../items/feydelight.md) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “No. Should I?” — **conditions:** NOT reached stage 1 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-1) → **stage 1**. NPC: “Well, you see? I make them. Not to brag, but I am in fact, the best baker in Feygard.”

???+ note "Stage 2: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “You said that you bake them, but what is a "feydelight"?” — **conditions:** latest stage of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-1) is 1 → **stage 2**. NPC: “Child, they are a delicious fig pie enjoyed by most Feygardians as an after dinner delicacy, often reserved for…”

???+ note "Stage 4: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “What?” — **conditions:** reached stage 4 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-4); NOT reached stage 7 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) → **stage 4**. NPC: “Yes. You need to get me some dough, two eggs, butter, honey and five Feygard fig fruits. I also need a bottle of wine.…”

???+ note "Stage 5: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “Dough! Where am I supposed to find dough?” — **conditions:** reached stage 4 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-4); NOT reached stage 7 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) → **stage 5**. NPC: “Well, Brightport is known for its wondeful bakeries. I would start there. Of course, you could get some in Feygard…”

???+ note "Stage 6: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “I've been across a great amount of Dhayavar and I've not seen honey anywhere.” — **conditions:** reached stage 4 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-4); NOT reached stage 7 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7); carry 0× [Honey](../items/honey.md) → **stage 6**. NPC: “How about trying a beekeeper? Geez, you are not the smartest are you?”

???+ note "Stage 7: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “Here, take them all.” — **conditions:** reached stage 4 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-4); carry 1× [Honey](../items/honey.md); carry 1× [Butter](../items/butter.md); carry 1× [Wine](../items/guynmart_wine.md); carry 1× [Raw dough](../items/dough.md); carry 5× [Fig](../items/fig_fruit.md); NOT reached stage 7 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7); carry 2× [Eggs](../items/eggs.md); hand over 1× [Honey](../items/honey.md); hand over 1× [Butter](../items/butter.md); hand over 1× [Raw dough](../items/dough.md); hand over 5× [Fig](../items/fig_fruit.md); hand over 1× [Wine](../items/guynmart_wine.md); hand over 2× [Eggs](../items/eggs.md) → **stage 7**; also starts timer “feydelight_baking”. NPC: “Come back later and it will be ready.”

???+ note "Stage 8: 1 route"

    1. Talk to [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) → choose “I am wondering, is my Feydelight ready yet?” — **conditions:** latest stage of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) is 7; 18 rounds passed since timer “feydelight_baking” → **stage 8**; also gives 1× [Feydelight](../items/feydelight.md). NPC: “Yes. Please enjoy while it's hot.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_delicacy.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_delicacy.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_delicacy.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_delicacy.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=feygard_delicacy.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `feygard_delicacy` |
    | showInLog | 1 |
    | Stage IDs | 1, 2, 3, 4, 5, 6, 7, 8 |
    | Dialogue nodes setting stages | 1: `village_philippa_fd_4`, 2: `village_philippa_fd_6`, 4: `village_philippa_fd_10`, 5: `village_philippa_fd_11`, 6: `village_philippa_fd_12`, 7: `village_philippa_fd_all_items_2`, 8: `village_philippa_fd_complete_yes` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
