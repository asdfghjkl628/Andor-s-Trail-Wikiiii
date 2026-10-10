---
description: "A Wicked witch is a quest in Andor's Trail, started by Bela. 14 stages, 46,182 XP in total. Bela, the Fallhaven tavern keeper heard from a customer about a possible kidnapping of a girl. I should ask around town if anyone knows more."
---

# A Wicked witch

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `wicked_witch` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 50, 70, 95, 96) |
| **Started by** | [Bela](../monsters/bela.md) |
| **NPCs involved** | [Bela](../monsters/bela.md), [Bonicksa](../monsters/wicked_witch_first.md#v-wicked_witch_third), [Bonicksa](../monsters/wicked_witch_first.md), [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer), [Emmeline](../monsters/captive_girl.md) |
| **Locations** | [Fallhaven south-east](../maps/fallhaven_se.md), [Lake shore road 1](../maps/lake_shore_road_1.md), [Witch house](../maps/witch_house.md) |
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


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [A giant snake](bela_gsnake.md#stage-90) | stage 90 reached, for stage 10 here |
| Unlocks | [Sutdover story flags (hidden flag)](sutdover_hidden.md#stage-1) | stage 1 there needs stage 65 here |
| Blocks | [Sutdover story flags (hidden flag)](sutdover_hidden.md#stage-1) | reaching stages 90, 95, 96 here closes stage 1 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Bela, the Fallhaven tavern keeper heard from a customer about a… ▸</span><span class="l">▴ less</span></summary>Bela, the Fallhaven tavern keeper heard from a customer about a possible kidnapping of a girl. I should ask around town if anyone knows more.</details> | [Bela](../monsters/bela.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The "busy farmer", in the southeastern part of Fallhaven knows… ▸</span><span class="l">▴ less</span></summary>The "busy farmer", in the southeastern part of Fallhaven knows something about the witch.</details> | [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">The "busy farmer" and his best friend, Addie, were kept captive by… ▸</span><span class="l">▴ less</span></summary>The "busy farmer" and his best friend, Addie, were kept captive by the witch a very long time ago when they were just kids. He never saw Addie again.</details> | [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">The "busy farmer" told me that the witch's house is just south of… ▸</span><span class="l">▴ less</span></summary>The "busy farmer" told me that the witch's house is just south of Fallhaven. Covered in beautiful flowers.</details><br><span class="qnote">🗺️ Part of [Lake shore road 1](../maps/lake_shore_road_1.md) visibly changes.</span> | [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">After meeting Bonicksa, the wicked witch, I decided to let her live… ▸</span><span class="l">▴ less</span></summary>After meeting Bonicksa, the wicked witch, I decided to let her live and she did likewise, but not before leaving me with a very cryptic response. Saying I was "confident in my path" and that "we shall see". I wonder what that meant?</details> **(ends quest)** | [Bonicksa](../monsters/wicked_witch_first.md) | – |
| <span id="stage-55"></span>55 | I have attacked Bonicksa. | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I killed what I thought was Bonicksa, but I quickly realized that I… ▸</span><span class="l">▴ less</span></summary>I killed what I thought was Bonicksa, but I quickly realized that I killed an innocent girl.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Witch house](../maps/witch_house.md).</span> | stepping on a trigger on [Witch house](../maps/witch_house.md) | spawns monsters on witch_house |
| <span id="stage-65"></span>[65](#route-65) | I "killed" Bonicksa again, only for her to reappear.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Witch house](../maps/witch_house.md).</span> | stepping on a trigger on [Witch house](../maps/witch_house.md) | spawns monsters on witch_house |
| <span id="stage-70"></span>[70](#route-70) | Bonicksa lives and could not be defeated. But I learned a huge life lesson. **(ends quest)** | [Bonicksa](../monsters/wicked_witch_first.md#v-wicked_witch_third) | 1,000 XP, spawns monsters on lake_shore_road_0, changes map lake_shore_road_0 |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">I discovered a young girl named Emmeline just behind the 'wicked… ▸</span><span class="l">▴ less</span></summary>I discovered a young girl named Emmeline just behind the 'wicked witch's' house. The witch was really Emmeline under a spell from Bonicksa.</details> | [Emmeline](../monsters/captive_girl.md) | spawns monsters on lake_shore_road_0, changes map lake_shore_road_0 |
| <span id="stage-85"></span>[85](#route-85) | Emmeline asked me to get her "a lot" of those "Tonics of Blood". | [Emmeline](../monsters/captive_girl.md) | – |
| <span id="stage-90"></span>[90](#route-90) | <details class="jt"><summary><span class="s">Emmeline told me to head east of the witch's house to find the… ▸</span><span class="l">▴ less</span></summary>Emmeline told me to head east of the witch's house to find the undead that know about the 'Tonic of Blood'.</details> | [Emmeline](../monsters/captive_girl.md) | – |
| <span id="stage-95"></span>[95](#route-95) | <details class="jt"><summary><span class="s">I gave Emmeline 25 of the "Tonics of Blood" that she asked for and… ▸</span><span class="l">▴ less</span></summary>I gave Emmeline 25 of the "Tonics of Blood" that she asked for and she was then able to leave that terrible place.</details> **(ends quest)** | [Emmeline](../monsters/captive_girl.md) | 24,097 XP |
| <span id="stage-96"></span>[96](#route-96) | <details class="jt"><summary><span class="s">I gave Emmeline 20 of the 25 "Tonics of Blood" that she asked for… ▸</span><span class="l">▴ less</span></summary>I gave Emmeline 20 of the 25 "Tonics of Blood" that she asked for and she was then able to leave that terrible place.</details> **(ends quest)** | [Emmeline](../monsters/captive_girl.md) | 21,085 XP |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Bela · 1 way"

    **Way 1:** Talk to [Bela](../monsters/bela.md), choose “So?”

    - **Needs:** not yet stage 50, 70, 95, 96; reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90)
    - *“A customer with a very interesting report about a kidnapped girl and a witch.”*


<span id="route-20"></span>

??? note "Stage 20 · Busy farmer · 1 way"

    **Way 1:** Talk to [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer), choose “Great, more stories with grandpa.”

    - **Needs:** stage 20; not yet stage 40
    - *“She was a young beautiful woman, but terrifyingly alluring. So much so, that she easily coerced us into following her into her house.”*


<span id="route-30"></span>

??? note "Stage 30 · Busy farmer · 1 way"

    **Way 1:** Talk to [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer), choose “You think?”

    - **Needs:** stage 20; not yet stage 40
    - *“Yes. You see, after I escaped, I never saw Addie again.”*


<span id="route-40"></span>

??? note "Stage 40 · Busy farmer · 1 way"

    **Way 1:** Talk to [Busy farmer](../monsters/busy_farmer.md#v-fallhaven_outdoor_farmer), choose “Thank you for telling me your story. I want to stop this witch once and for all. Where can I find her?”

    - **Needs:** stage 20; not yet stage 40
    - *“Thank you! You can find her house just south of here. You can't miss it as it is covered in beautiful flowers.”*


<span id="route-50"></span>

??? note "Stage 50 · Bonicksa · 1 way"

    **Way 1:** Talk to [Bonicksa](../monsters/wicked_witch_first.md), choose “Witches don't bother me. I'll leave you be.”

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-40) is 40
    - <small>Also: starts timer “wicked_witch_despawn_timer”</small>
    - *“How intriguing. Such confidence in your path. We shall see, won't we?”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on witch_house · 1 way"

    **Way 1:** Stepping on a trigger on [Witch house](../maps/witch_house.md)

    - **Needs:** not yet stage 60; killed 1× [Bonicksa](../monsters/wicked_witch_first.md)
    - **Gives:** spawns monsters on witch_house
    - *“As the "witch" dies, she begins to transform into her true form, revealing a young girl and you quickly realize the tragedy of your…”*


<span id="route-65"></span>

??? note "Stage 65 · stepping on a trigger on witch_house · 1 way"

    **Way 1:** Stepping on a trigger on [Witch house](../maps/witch_house.md)

    - **Needs:** not yet stage 65; killed 1× [Bonicksa](../monsters/wicked_witch_first.md#v-wicked_witch_second)
    - **Gives:** spawns monsters on witch_house
    - *“After defeating the real witch, she quickly reappears.”*


<span id="route-70"></span>

??? note "Stage 70 · Bonicksa · 1 way"

    **Way 1:** Talk to [Bonicksa](../monsters/wicked_witch_first.md#v-wicked_witch_third), choose “[disgruntled] Is this some kind of sick game to you?”

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-65) is 65
    - **Gives:** spawns monsters on lake_shore_road_0, changes map lake_shore_road_0
    - <small>Also: sets stage 1 of [Sutdover story flags (hidden flag)](../quests/sutdover_hidden.md#stage-1)</small>
    - *“[smirks] Perhaps. But remember, hero, life's full of surprises. You may have won this time, but who's to say what lies ahead?”*


<span id="route-80"></span>

??? note "Stage 80 · Emmeline · 1 way"

    **Way 1:** Talk to [Emmeline](../monsters/captive_girl.md), choose “What ... do I know you? You're just a young girl?”

    - **Needs:** not yet stage 90, 95, 96
    - **Gives:** spawns monsters on lake_shore_road_0, changes map lake_shore_road_0
    - <small>Also: sets stage 1 of [Sutdover story flags (hidden flag)](../quests/sutdover_hidden.md#stage-1)</small>
    - *“Yes, I was under a spell that made me appear as the witch. She wanted to test your heart. I'm glad you proved kind.”*


<span id="route-85"></span>

??? note "Stage 85 · Emmeline · 1 way"

    **Way 1:** Talk to [Emmeline](../monsters/captive_girl.md), automatic

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90
    - *“I really need to get my hands on a lot of those 'Tonic of Blood' potions. Can you help me? I need a lot.”*


<span id="route-90"></span>

??? note "Stage 90 · Emmeline · 1 way"

    **Way 1:** Talk to [Emmeline](../monsters/captive_girl.md), choose “Can you help me out a little bit? Do you know anything about them?”

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; carry 10× [Tonic of blood](../items/tonic_of_blood.md); not carry 20× [Tonic of blood](../items/tonic_of_blood.md)
    - *“Ah, YES. I remember her saying that an "undead" friend of her's east of here taught her how to make them.”*


<span id="route-95"></span>

??? note "Stage 95 · Emmeline · 1 way"

    **Way 1:** Talk to [Emmeline](../monsters/captive_girl.md), choose “Well, I have twenty-five of those for you.”

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; hand over 25× [Tonic of blood](../items/tonic_of_blood.md)
    - *“WOW! You actually managed to find twenty-five! I am so grateful.”*


<span id="route-96"></span>

??? note "Stage 96 · Emmeline · 1 way"

    **Way 1:** Talk to [Emmeline](../monsters/captive_girl.md), choose “I know that you "asked" for twenty-five, but I have twenty and they are hard to get. Please take these.”

    - **Needs:** latest stage of [A Wicked witch](../quests/wicked_witch.md#stage-90) is 90; carry 20× [Tonic of blood](../items/tonic_of_blood.md); not carry 25× [Tonic of blood](../items/tonic_of_blood.md); hand over 20× [Tonic of blood](../items/tonic_of_blood.md)
    - *“OK. I won't make you go back just for five more when you've already brought me twenty.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 13 lines added |
| [v0.8.9](../versions/0.8.9.md) | Dialogue: 1 line changed<br>· text: “Ah, YES. I remember her saying that an "undead" friend of her's east …” → “Ah, YES. I remember her saying that an "undead" friend of her's east …” |
| [v0.8.18](../versions/0.8.18.md) | Stage 30 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wicked_witch.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
