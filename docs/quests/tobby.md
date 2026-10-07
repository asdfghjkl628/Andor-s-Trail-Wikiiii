# Sobby's Trail

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `tobby` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 30, 40) |
| **Started by** | [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) |
| **NPCs involved** | [Tobby](../monsters/tobby6.md), [Tobby](../monsters/tobby2.md), [Tobby](../monsters/tobby4a.md), [Tobby](../monsters/tobby3.md), [Tobby](../monsters/tobby.md), [Tobby](../monsters/tobby5.md) +1 |
| **Locations** | [guynmart_wood_17](../maps/guynmart_wood_17.md), [guynmart_wood_17b](../maps/guynmart_wood_17b.md), [guynmart_wood_18](../maps/guynmart_wood_18.md), [guynmart_wood_19](../maps/guynmart_wood_19.md) |
| **Total XP** | 1,560 |

</div>

## Overview

> On the road to Feygard I have met a boy named Tobby. He is looking for his brother Sobby.

## Prerequisites to start

None: talk to [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | On the road to Feygard I have met a boy named Tobby. He is looking for his brother Sobby. | [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) | – | – |
| <span id="stage-20"></span>20 | I have promised to help Tobby get past the kobolds to the south. | [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) | – | – |
| <span id="stage-21"></span>21 | I have killed the rat in Tobby's garden. | [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) | stage 20 | 30 XP |
| <span id="stage-22"></span>22 | I gave Tobby a loaf of bread for his father. | [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) | hand over 1× [Bread](../items/bread.md), stage 20 | 30 XP |
| <span id="stage-23"></span>23 | Tobby has followed me to the beginning of the ravine with the kobolds.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 18](../maps/guynmart_wood_18.md).</span> | stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) | stage 20 | removes monsters from guynmart_wood_19<br>spawns monsters on guynmart_wood_18 |
| <span id="stage-24"></span>24 | Tobby has made it through the ravine.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17b](../maps/guynmart_wood_17b.md).</span> | stepping on a trigger on [guynmart_wood_17b](../maps/guynmart_wood_17b.md) | stage 23 | removes monsters from guynmart_wood_18<br>spawns monsters on guynmart_wood_17b |
| <span id="stage-25"></span>25 | Tobby followed me further to the south.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span> | stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md) | stage 24 | removes monsters from guynmart_wood_17b<br>spawns monsters on guynmart_wood_17 |
| <span id="stage-30"></span>30 | I have attacked poor Tobby, but he ran away. Now he will never find his brother. **(completes quest)** | [Tobby](../monsters/tobby2.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) | – | removes monsters from guynmart_wood_19<br>removes monsters from guynmart_wood_18<br>removes monsters from guynmart_wood_17b |
| <span id="stage-40"></span>40 | We have parted. Tobby was sure now to find his brother. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guynmart wood 17](../maps/guynmart_wood_17.md).</span> | stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md)<br>[Tobby](../monsters/tobby5.md) ([guynmart_wood_17](../maps/guynmart_wood_17.md)) | stage 25 | 1,500 XP<br>removes monsters from guynmart_wood_17<br>spawns monsters on woodhouse1 |
| <span id="stage-50"></span>50 | I have met Tobby again, together with Sobby in the little village in the woods. | [Tobby](../monsters/tobby6.md) ([woodhouse1](../maps/woodhouse1.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) → choose “I am $playername. What can I do for you?” → **stage 10**. NPC: “I can't seem to find my brother, Sobby. He hasn't been back since he left last year.”

???+ note "Stage 20: 1 route"

    1. Talk to [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20) → **stage 20**. NPC: “I am glad you want to help me.”

???+ note "Stage 21: 1 route"

    1. Talk to [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) → choose “OK. And tell your father that his rat problem is solved.” — **conditions:** reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20); killed 1× [Tiny rat](../monsters/tobby_trainingrat.md) → **stage 21**. NPC: “Oh, how did you know?”

???+ note "Stage 22: 1 route"

    1. Talk to [Tobby](../monsters/tobby.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) → choose “OK. And bring your father this loaf of bread.” — **conditions:** reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20); NOT killed 1× [Tiny rat](../monsters/tobby_trainingrat.md); hand over 1× [Bread](../items/bread.md) → **stage 22**. NPC: “Now I'm speechless - thank you!”

???+ note "Stage 23: 1 route"

    1. stepping on a trigger on [guynmart_wood_18](../maps/guynmart_wood_18.md) → the conversation leads here automatically — **conditions:** reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20); NOT reached stage 23 of [Sobby's Trail](../quests/tobby.md#stage-23); NOT reached stage 30 of [Sobby's Trail](../quests/tobby.md#stage-30) → **stage 23**; also removes monsters from guynmart_wood_19, spawns monsters on guynmart_wood_18

???+ note "Stage 24: 2 routes"

    1. stepping on a trigger on [guynmart_wood_17b](../maps/guynmart_wood_17b.md) → the conversation leads here automatically — **conditions:** reached stage 23 of [Sobby's Trail](../quests/tobby.md#stage-23); NOT reached stage 24 of [Sobby's Trail](../quests/tobby.md#stage-24); NOT reached stage 30 of [Sobby's Trail](../quests/tobby.md#stage-30) → **stage 24**; also removes monsters from guynmart_wood_18, spawns monsters on guynmart_wood_17b
    2. stepping on a trigger on [guynmart_wood_17b](../maps/guynmart_wood_17b.md) → the conversation leads here automatically — **conditions:** reached stage 23 of [Sobby's Trail](../quests/tobby.md#stage-23); NOT reached stage 24 of [Sobby's Trail](../quests/tobby.md#stage-24); NOT reached stage 30 of [Sobby's Trail](../quests/tobby.md#stage-30) → **stage 24**; also removes monsters from guynmart_wood_18, spawns monsters on guynmart_wood_17b

???+ note "Stage 25: 1 route"

    1. stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md) → the conversation leads here automatically — **conditions:** reached stage 24 of [Sobby's Trail](../quests/tobby.md#stage-24); NOT reached stage 25 of [Sobby's Trail](../quests/tobby.md#stage-25); NOT reached stage 30 of [Sobby's Trail](../quests/tobby.md#stage-30) → **stage 25**; also removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b, spawns monsters on guynmart_wood_17

???+ note "Stage 30: 1 route"

    1. Talk to [Tobby](../monsters/tobby2.md) ([guynmart_wood_19](../maps/guynmart_wood_19.md)) → choose “I'll show you - attack!” → **stage 30**; also removes monsters from guynmart_wood_19, removes monsters from guynmart_wood_18, removes monsters from guynmart_wood_17b, removes monsters from guynmart_wood_17b. NPC: “Tobby cried out aloud and ran away like the wind. You monster!”

???+ note "Stage 40: 2 routes"

    1. stepping on a trigger on [guynmart_wood_17](../maps/guynmart_wood_17.md) → choose “Was it? I have got used to such things by now.” — **conditions:** reached stage 25 of [Sobby's Trail](../quests/tobby.md#stage-25); NOT reached stage 40 of [Sobby's Trail](../quests/tobby.md#stage-40) → **stage 40**; also removes monsters from guynmart_wood_17, spawns monsters on woodhouse1. NPC: “I think that I'll find Sobby by myself now. Thank you - hope we'll meet again!”
    2. Talk to [Tobby](../monsters/tobby5.md) ([guynmart_wood_17](../maps/guynmart_wood_17.md)) → choose “Was it? I have got used to such things by now.” → **stage 40**; also removes monsters from guynmart_wood_17, spawns monsters on woodhouse1. NPC: “I think that I'll find Sobby by myself now. Thank you - hope we'll meet again!”

???+ note "Stage 50: 1 route"

    1. Talk to [Tobby](../monsters/tobby6.md) ([woodhouse1](../maps/woodhouse1.md)) → choose “Tobby? What are you doing here?” → **stage 50**. NPC: “Thanks to you I have found my brother Sobby.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=tobby.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `tobby` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 22, 23, 24, 25, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `tobby_3`, 20: `tobby_20`, 21: `tobby_30`, 22: `tobby_32`, 23: `tobby2_mce_1`, 24: `tobby3_mcea_1`, 24: `tobby3_mceb_1`, 25: `tobby4_mce_1`, 30: `tobby2_2`, 40: `tobby5_10`, 50: `tobby6_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
