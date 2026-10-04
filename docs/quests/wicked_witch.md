# A Wicked witch

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `wicked_witch` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 50, 70, 95, 96) |
| **Started by** | [Bela](../monsters/bela.md) |
| **NPCs involved** | [Bela](../monsters/bela.md), [Bonicksa](../monsters/wicked_witch_third.md), [Bonicksa](../monsters/wicked_witch_first.md), [Busy farmer](../monsters/fallhaven_outdoor_farmer.md), [Emmeline](../monsters/captive_girl.md) |
| **Locations** | [fallhaven_se](../maps/fallhaven_se.md), [lake_shore_road_1](../maps/lake_shore_road_1.md), [witch_house](../maps/witch_house.md) |
| **Total XP** | 46,182 |
| **Related quests** | 2 |

</div>

## Overview

> Bela, the Fallhaven tavern keeper heard from a customer about a possible kidnapping of a girl. I should ask around town if anyone knows more.

## Prerequisites to start

Start with [Bela](../monsters/bela.md). Required:

- reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90)
- NOT reached stage 50 of [A Wicked witch](../quests/wicked_witch.md#stage-50)
- NOT reached stage 70 of [A Wicked witch](../quests/wicked_witch.md#stage-70)
- NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95)
- NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96)

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A giant snake](bela_gsnake.md#stage-90) | stage 90 reached, for stage 10 here |
| Unlocks | [Sutdove_nondisplay (hidden flag)](sutdover_hidden.md#stage-1) | stage 1 there needs stage 65 here |
| Blocks | [Sutdove_nondisplay (hidden flag)](sutdover_hidden.md#stage-1) | reaching stages 90, 95, 96 here closes stage 1 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Bela, the Fallhaven tavern keeper heard from a customer about a possible kidnapping of a girl. I should ask around town if anyone knows more. | [Bela](../monsters/bela.md) | – | – |
| <span id="stage-20"></span>20 | The "busy farmer", in the southeastern part of Fallhaven knows something about the witch. | [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) | – | – |
| <span id="stage-30"></span>30 | The "busy farmer" and his best friend, Addie, were kept captive by the witch a very long time ago when they were just kids. He never saw Addie again. | [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | The "busy farmer" told me that the witch's house is just south of Fallhaven. Covered in beautiful flowers.<br><span class="qnote">🗺️ Part of [Lake shore road 1](../maps/lake_shore_road_1.md) visibly changes.</span> | [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) | stage 20 | – |
| <span id="stage-50"></span>50 | After meeting Bonicksa, the wicked witch, I decided to let her live and she did likewise, but not before leaving me with a very cryptic response. Saying I was "confident in my path" and that "we shall see". I wonder what that meant? **(completes quest)** | [Bonicksa](../monsters/wicked_witch_first.md) ([witch_house](../maps/witch_house.md)) | stage 40 | starts timer “wicked_witch_despawn_timer” |
| <span id="stage-55"></span>55 | I have attacked Bonicksa. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-60"></span>60 | I killed what I thought was Bonicksa, but I quickly realized that I killed an innocent girl.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Witch house](../maps/witch_house.md).</span> | stepping on a trigger on [witch_house](../maps/witch_house.md) | – | spawns monsters on witch_house |
| <span id="stage-65"></span>65 | I "killed" Bonicksa again, only for her to reappear.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Witch house](../maps/witch_house.md).</span> | stepping on a trigger on [witch_house](../maps/witch_house.md) | – | spawns monsters on witch_house |
| <span id="stage-70"></span>70 | Bonicksa lives and could not be defeated. But I learned a huge life lesson. **(completes quest)** | [Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md)) | stage 65 | 1,000 XP<br>sets stage 1 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-1)<br>spawns monsters on lake_shore_road_0<br>changes map lake_shore_road_0 |
| <span id="stage-80"></span>80 | I discovered a young girl named Emmeline just behind the 'wicked witch's' house. The witch was really Emmeline under a spell from Bonicksa. | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) | – | sets stage 1 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-1)<br>spawns monsters on lake_shore_road_0<br>changes map lake_shore_road_0 |
| <span id="stage-85"></span>85 | Emmeline asked me to get her "a lot" of those "Tonics of Blood". | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) | stage 90 | – |
| <span id="stage-90"></span>90 | Emmeline told me to head east of the witch's house to find the undead that know about the 'Tonic of Blood'. | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) | carry 10× [Tonic of blood](../items/tonic_of_blood.md) | – |
| <span id="stage-95"></span>95 | I gave Emmeline 25 of the "Tonics of Blood" that she asked for and she was then able to leave that terrible place. **(completes quest)** | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) | hand over 25× [Tonic of blood](../items/tonic_of_blood.md), stage 90 | 24,097 XP |
| <span id="stage-96"></span>96 | I gave Emmeline 20 of the 25 "Tonics of Blood" that she asked for and she was then able to leave that terrible place. **(completes quest)** | [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) | carry 20× [Tonic of blood](../items/tonic_of_blood.md), hand over 20× [Tonic of blood](../items/tonic_of_blood.md), stage 90 | 21,085 XP |

<span id="untraced"></span>*No trigger*: nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Bela](../monsters/bela.md) → choose “So?” — **conditions:** reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90); NOT reached stage 50 of [A Wicked witch](../quests/wicked_witch.md#stage-50); NOT reached stage 70 of [A Wicked witch](../quests/wicked_witch.md#stage-70); NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95); NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96) → **stage 10**. NPC: “A customer with a very interesting report about a kidnapped girl and a witch.”

???+ note "Stage 20: 1 route"

    1. Talk to [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) → choose “Great, more stories with grandpa.” — **conditions:** reached stage 20 of [A Wicked witch](../quests/wicked_witch.md#stage-20); NOT reached stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40) → **stage 20**. NPC: “She was a young beautiful woman, but terrifyingly alluring. So much so, that she easily coerced us into following her…”

???+ note "Stage 30: 1 route"

    1. Talk to [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) → choose “You think?” — **conditions:** reached stage 20 of [A Wicked witch](../quests/wicked_witch.md#stage-20); NOT reached stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40) → **stage 30**. NPC: “Yes. You see, after I escaped, I never saw Addie again.”

???+ note "Stage 40: 1 route"

    1. Talk to [Busy farmer](../monsters/fallhaven_outdoor_farmer.md) ([fallhaven_se](../maps/fallhaven_se.md)) → choose “Thank you for telling me your story. I want to stop this witch once and for all. Where can I find her?” — **conditions:** reached stage 20 of [A Wicked witch](../quests/wicked_witch.md#stage-20); NOT reached stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40) → **stage 40**. NPC: “Thank you! You can find her house just south of here. You can't miss it as it is covered in beautiful flowers.”

???+ note "Stage 50: 1 route"

    1. Talk to [Bonicksa](../monsters/wicked_witch_first.md) ([witch_house](../maps/witch_house.md)) → choose “Witches don't bother me. I'll leave you be.” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-40) is 40 → **stage 50**; also starts timer “wicked_witch_despawn_timer”. NPC: “How intriguing. Such confidence in your path. We shall see, won't we?”

???+ note "Stage 60: 1 route"

    1. stepping on a trigger on [witch_house](../maps/witch_house.md) → the conversation leads here automatically — **conditions:** killed 1× [Bonicksa](../monsters/wicked_witch_first.md); NOT reached stage 60 of [A Wicked witch](../quests/wicked_witch.md#stage-60) → **stage 60**; also spawns monsters on witch_house. NPC: “As the "witch" dies, she begins to transform into her true form, revealing a young girl and you quickly realize the…”

???+ note "Stage 65: 1 route"

    1. stepping on a trigger on [witch_house](../maps/witch_house.md) → the conversation leads here automatically — **conditions:** NOT reached stage 65 of [A Wicked witch](../quests/wicked_witch.md#stage-65); killed 1× [Bonicksa](../monsters/wicked_witch_second.md) → **stage 65**; also spawns monsters on witch_house. NPC: “After defeating the real witch, she quickly reappears.”

???+ note "Stage 70: 1 route"

    1. Talk to [Bonicksa](../monsters/wicked_witch_third.md) ([witch_house](../maps/witch_house.md)) → choose “[disgruntled] Is this some kind of sick game to you?” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-65) is 65 → **stage 70**; also sets stage 1 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-1), spawns monsters on lake_shore_road_0, changes map lake_shore_road_0. NPC: “[smirks] Perhaps. But remember, hero, life's full of surprises. You may have won this time, but who's to say what lies…”

???+ note "Stage 80: 1 route"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → choose “What ... do I know you? You're just a young girl?” — **conditions:** NOT reached stage 90 of [A Wicked witch](../quests/wicked_witch.md#stage-90); NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95); NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96) → **stage 80**; also sets stage 1 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-1), spawns monsters on lake_shore_road_0, changes map lake_shore_road_0. NPC: “Yes, I was under a spell that made me appear as the witch. She wanted to test your heart. I'm glad you proved kind.”

???+ note "Stage 85: 1 route"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → the conversation leads here automatically — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90 → **stage 85**. NPC: “I really need to get my hands on a lot of those 'Tonic of Blood' potions. Can you help me? I need a lot.”

???+ note "Stage 90: 1 route"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → choose “Can you help me out a little bit? Do you know anything about them?” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; carry 10× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 20× [Tonic of blood](../items/tonic_of_blood.md) → **stage 90**. NPC: “Ah, YES. I remember her saying that an "undead" friend of her's east of here taught her how to make them.”

???+ note "Stage 95: 1 route"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → choose “Well, I have twenty-five of those for you.” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; hand over 25× [Tonic of blood](../items/tonic_of_blood.md) → **stage 95**. NPC: “WOW! You actually managed to find twenty-five! I am so grateful.”

???+ note "Stage 96: 1 route"

    1. Talk to [Emmeline](../monsters/captive_girl.md) ([lake_shore_road_1](../maps/lake_shore_road_1.md)) → choose “I know that you "asked" for twenty-five, but I have twenty and they are hard to get. Please take these.” — **conditions:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; carry 20× [Tonic of blood](../items/tonic_of_blood.md); NOT carry 25× [Tonic of blood](../items/tonic_of_blood.md); hand over 20× [Tonic of blood](../items/tonic_of_blood.md) → **stage 96**. NPC: “OK. I won't make you go back just for five more when you've already brought me twenty.”


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `wicked_witch` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 55, 60, 65, 70, 80, 85, 90, 95, 96 |
    | Dialogue nodes setting stages | 10: `bela_witch_25`, 20: `fallhaven_outdoor_farmer_79`, 30: `fallhaven_outdoor_farmer_82`, 40: `fallhaven_outdoor_farmer_84`, 50: `wicked_witch_first_25`, 60: `wicked_witch_first_killed_script`, 65: `wicked_witch_second_killed`, 70: `wicked_witch_third_30`, 80: `captive_girl_20`, 85: `captive_girl_50`, 90: `captive_girl_65`, 95: `captive_girl_71`, 96: `captive_girl_70` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
