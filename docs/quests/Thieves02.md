---
description: "Immaculate kidnapping is a quest in Andor's Trail, started by Umar (fallhaven_derelict2). 19 stages, 9,350 XP in total. After completing my first task I'm considered a member of Thieves' Guild. Now I have to perform a very risky task. Umar sent me to kidnap a noble woman from Feygard, without bei…"
---

# Immaculate kidnapping

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves02` |
| **In journal** | Yes |
| **Stages** | 19 (completes at 75, 76) |
| **Started by** | [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Ambelie](../monsters/ambelie.md), [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Troublemaker](../monsters/troublemaker.md), [Umar](../monsters/umar.md) |
| **Locations** | [Fallhaven derelict 2](../maps/fallhaven_derelict2.md), [Fallhaven derelict 2 t](../maps/fallhaven_derelict2_t.md), [Foaming flask](../maps/foaming_flask.md) |
| **Total XP** | 9,350 |
| **Related quests** | 5 |

</div>

## Overview

> After completing my first task I'm considered a member of Thieves' Guild. Now I have to perform a very risky task. Umar sent me to kidnap a noble woman from Feygard, without being discovered.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
- latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2
- NOT reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Thief apprentice](Thieves01.md#stage-60) | stage 60 reached, for stages 45, 60, 70 here |
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stages 2, 4, 6, 30, 35, 40, 75, 76 here |
| Unlocks | [The ruthless Crackshot](Thieves03.md#stage-1) | stage 1 there needs stage 76 here |
| Unlocks | [Miscellaneous story flags (hidden flag)](misc_nondisplay.md#stage-20) | stage 20 there needs stage 76 here |
| Unlocks | [Thieves story flags (hidden flag)](thieves_hidden.md#stage-20) | stage 20 there needs stages 15, 21 here |
| Blocks | [The ruthless Crackshot](Thieves03.md#stage-1) | reaching stage 75 here closes stage 1 there |
| Blocks | [Miscellaneous story flags (hidden flag)](misc_nondisplay.md#stage-20) | reaching stage 75 here closes stage 20 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-2"></span>[2](#route-2) | <details class="jt"><summary><span class="s">After completing my first task I'm considered a member of Thieves'… ▸</span><span class="l">▴ less</span></summary>After completing my first task I'm considered a member of Thieves' Guild. Now I have to perform a very risky task. Umar sent me to kidnap a noble woman from Feygard, without being discovered.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-4"></span>[4](#route-4) | She was recently seen in the Foaming Flask tavern. | [Umar](../monsters/umar.md) | – |
| <span id="stage-6"></span>[6](#route-6) | <details class="jt"><summary><span class="s">Umar gave me some advice. My strength is not always the solution. I… ▸</span><span class="l">▴ less</span></summary>Umar gave me some advice. My strength is not always the solution. I must "use my tongue" to avoid raising suspicion in the tavern.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Ambelie Laumwill doesn't want to come with me peacefully. I cannot… ▸</span><span class="l">▴ less</span></summary>Ambelie Laumwill doesn't want to come with me peacefully. I cannot make a scene, or the guards will alert other patrols. Maybe talking with them would solve the situation.</details> | [Ambelie](../monsters/ambelie.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">I have "used my tongue" with the main Feygard soldier in the Foaming… ▸</span><span class="l">▴ less</span></summary>I have "used my tongue" with the main Feygard soldier in the Foaming Flask tavern. He gave me permission to "escort back" Ambelie.</details> | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I knocked out Ambelie. I will take her back to the Guild. | [Ambelie](../monsters/ambelie.md) | removes monsters from foaming_flask, spawns monsters on road1, applies condition carrying_ambelie |
| <span id="stage-21"></span>[21](#route-21) | I have decided not to kidnap Ambelie. I must think of another solution. | [Ambelie](../monsters/ambelie.md) | – |
| <span id="stage-24"></span>[24](#route-24) | <details class="jt"><summary><span class="s">Ambelie gave me a very valuable necklace. I must talk with Umar and… ▸</span><span class="l">▴ less</span></summary>Ambelie gave me a very valuable necklace. I must talk with Umar and persuade him to no longer pursue her.</details> | [Ambelie](../monsters/ambelie.md) | 1× [Sapphire Necklace](../items/g02_ambelie.md), spawns monsters on road1 |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">I safely brought Ambelie to the basement. However, keeping her here… ▸</span><span class="l">▴ less</span></summary>I safely brought Ambelie to the basement. However, keeping her here could be dangerous.</details> | [Umar](../monsters/umar.md) | 1,200 XP |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">Umar believes there is a secure room for these types of "visitors".… ▸</span><span class="l">▴ less</span></summary>Umar believes there is a secure room for these types of "visitors". I should talk to Troublemaker.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">I have talked to Troublemaker about the place Umar believes it's… ▸</span><span class="l">▴ less</span></summary>I have talked to Troublemaker about the place Umar believes it's okay to safely keep the hostage.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-45"></span>[45](#route-45) | <details class="jt"><summary><span class="s">Troublemaker has given me the key to the Guild brig. I should take… ▸</span><span class="l">▴ less</span></summary>Troublemaker has given me the key to the Guild brig. I should take Ambelie there and leave her to wake up.</details> | [Troublemaker](../monsters/troublemaker.md) | 1,000 XP, 1× [Guild brig key](../items/guildbrigK.md) |
| <span id="stage-50"></span>[50](#route-50) | I've inserted the key and moved the lever. A hatchway has opened in the room.<br><span class="qnote">🗺️ Part of [Fallhaven gravedigger](../maps/fallhaven_gravedigger.md) visibly changes.</span> | walking into a blocked passage on [Fallhaven gravedigger](../maps/fallhaven_gravedigger.md) | changes map fallhaven_gravedigger |
| <span id="stage-55"></span>[55](#route-55) | I left Ambelie in that ugly, dark, and cold place. I should go back.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guildbrig 2](../maps/guildbrig2.md).</span> | walking into a blocked passage on [Guildbrig 2](../maps/guildbrig2.md) | spawns monsters on guildbrig2, applies condition carrying_ambelie |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">Troublemaker gave me some bread for Ambelie. The guild doesn't want… ▸</span><span class="l">▴ less</span></summary>Troublemaker gave me some bread for Ambelie. The guild doesn't want her to starve to death. Indeed, they want her to be as comfortable as possible. I must go to the brig again.</details> | [Troublemaker](../monsters/troublemaker.md) | 5× [Bread](../items/bread.md) |
| <span id="stage-65"></span>[65](#route-65) | <details class="jt"><summary><span class="s">I gave the bread to Ambelie. I should report Troublemaker that I… ▸</span><span class="l">▴ less</span></summary>I gave the bread to Ambelie. I should report Troublemaker that I completed the job.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guildbrig 2](../maps/guildbrig2.md).</span> | stepping on a trigger on [Guildbrig 2](../maps/guildbrig2.md), [Ambelie](../monsters/ambelie.md) | 400 XP |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">The job finally seems to be finished. I just have to talk with Umar… ▸</span><span class="l">▴ less</span></summary>The job finally seems to be finished. I just have to talk with Umar again. However, I do not feel good about this. Kidnappings are definitely not my kind of job.</details> | [Troublemaker](../monsters/troublemaker.md) | – |
| <span id="stage-75"></span>[75](#route-75) | <details class="jt"><summary><span class="s">I completed this task successfully. Umar told me they have sent… ▸</span><span class="l">▴ less</span></summary>I completed this task successfully. Umar told me they have sent couriers to Feygard, and the ransom is almost guaranteed. He paid me for my work.</details> **(ends quest)** | [Umar](../monsters/umar.md) | 4,500 XP, faction “ThievesGuild” +10, 2500× [Gold coins](../items/gold.md) |
| <span id="stage-76"></span>[76](#route-76) | Umar took the necklace as compensation for my errors. Everything is fine again. **(ends quest)** | [Umar](../monsters/umar.md) | 2,250 XP, faction “ThievesGuild” +10 |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-2"></span>

??? note "Stage 2 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Anything more about my new task?”

    - **Needs:** not yet stage 4; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2
    - *“I want you to bring the noble woman here, so that we can ask for a substantial ransom from her generous father.”*


<span id="route-4"></span>

??? note "Stage 4 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Where can I find this woman?”

    - **Needs:** not yet stage 4; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2
    - *“Scouts have seen the lady in the Foaming flask tavern. We do not want to be discovered, so act quietly. Guards are a problem though. It's…”*


<span id="route-6"></span>

??? note "Stage 6 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Anything more about my new task?”

    - **Needs:** not yet stage 6, 15; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-4) is 4
    - *“Use your tongue, young man. Sometimes it is more important than your sword skills.”*


<span id="route-10"></span>

??? note "Stage 10 · Ambelie · 1 way"

    **Way 1:** Talk to [Ambelie](../monsters/ambelie.md), choose “But I'm not a commoner! I'm a ... Feygard spy. These clothes are my disguise!”

    - **Needs:** stage 4; not yet stage 10
    - *“Anyway, I prefer to stay in this place for now. Get away from me!”*


<span id="route-15"></span>

??? note "Stage 15 · Feygard patrol captain · 1 way"

    **Way 1:** Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md), choose “Ergh ... Mr Laumwill is grateful for your protection. However ... Ah! He has given this reward of 1,000 gold…”

    - **Needs:** stage 10; not yet stage 15; pay 1,000 gold
    - *“I have to stay here to supervise my guards. They sometimes need educating about what to do. I assume you're able to escort her without…”*


<span id="route-20"></span>

??? note "Stage 20 · Ambelie · 1 way"

    **Way 1:** Talk to [Ambelie](../monsters/ambelie.md), choose “(Knock her out) Time to sleep!”

    - **Needs:** stage 15
    - **Gives:** removes monsters from foaming_flask, spawns monsters on road1, applies condition carrying_ambelie
    - <small>Also: sets stage 20 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-20)</small>
    - *“(You tap her on the back of the head with the handle of your weapon, and she falls unconscious)”*


<span id="route-21"></span>

??? note "Stage 21 · Ambelie · 1 way"

    **Way 1:** Talk to [Ambelie](../monsters/ambelie.md), choose “I'm not going to hurt you.”

    - **Needs:** stage 21
    - *“Then get out of my sight now!”*


<span id="route-24"></span>

??? note "Stage 24 · Ambelie · 1 way"

    **Way 1:** Talk to [Ambelie](../monsters/ambelie.md), choose “Give me something of value, and you won't see me again.”

    - **Needs:** stage 21
    - **Gives:** 1× [Sapphire Necklace](../items/g02_ambelie.md), spawns monsters on road1
    - <small>Also: sets stage 20 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-20)</small>
    - *“Take this and leave me, please.”*


<span id="route-30"></span>

??? note "Stage 30 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “I have brought the hostage.”

    - **Needs:** stage 20; not yet stage 21, 24, 30; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“(You put Ambelie, who is still unconscious, in a chair next to you) Oh! How did you get here so fast? I've heard reports of a barricade…”*


<span id="route-35"></span>

??? note "Stage 35 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “What am I supposed to do with the noblewoman?”

    - **Needs:** stage 30; not yet stage 35; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“We are supposed to have one room for receiving "visitors". However, I don't know if It's finished.”*


<span id="route-40"></span>

??? note "Stage 40 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “What am I supposed to do with the noblewoman?”

    - **Needs:** stage 35; not yet stage 40; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“Hmm, I believe Troublemaker knows the actual state of that place. Ask him, and if it's possible leave our guest there.”*


<span id="route-45"></span>

??? note "Stage 45 · Troublemaker · 1 way"

    **Way 1:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “Whatever, anything more?”

    - **Needs:** stage 40; not yet stage 45; latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60
    - **Gives:** 1× [Guild brig key](../items/guildbrigK.md)
    - *“I almost forgot. Take this key. Make sure you put it in correctly to open the hatchway.”*


<span id="route-50"></span>

??? note "Stage 50 · walking into a blocked passage on fallhaven_gravedigger · 1 way"

    **Way 1:** Walking into a blocked passage on [Fallhaven gravedigger](../maps/fallhaven_gravedigger.md), choose “Put the key into the lock.”

    - **Needs:** stage 45; carry 1× [Guild brig key](../items/guildbrigK.md); hand over 1× [Guild brig key](../items/guildbrigK.md)
    - **Gives:** changes map fallhaven_gravedigger
    - *“You insert the key in the lock. You can hear strange noises and creaks as you turn the key. You make an extra effort, and finally the…”*


<span id="route-55"></span>

??? note "Stage 55 · walking into a blocked passage on guildbrig2 · 1 way"

    **Way 1:** Walking into a blocked passage on [Guildbrig 2](../maps/guildbrig2.md), choose “Put Ambelie inside the room.”

    - **Needs:** stage 50
    - **Gives:** spawns monsters on guildbrig2, applies condition carrying_ambelie
    - *“You leave Ambelie in the cell and close the door.”*


<span id="route-60"></span>

??? note "Stage 60 · Troublemaker · 1 way"

    **Way 1:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “I've dealt with the lady.”

    - **Needs:** not yet stage 65; latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-55) is 55
    - **Gives:** 5× [Bread](../items/bread.md)
    - *“Ah, yes ... that captive. Take this food and make sure she is comfortable enough. We don't want her starving right? (Troublemaker gives…”*


<span id="route-65"></span>

??? note "Stage 65 · stepping on a trigger on guildbrig2, Ambelie · 2 ways"

    **Way 1:** Stepping on a trigger on [Guildbrig 2](../maps/guildbrig2.md), choose “[Give the Bread]”

    - **Needs:** latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-60) is 60; hand over 5× [Bread](../items/bread.md)
    - *“Th..thanks. Now, please tell me, where am I?”*

    **Way 2:** Talk to [Ambelie](../monsters/ambelie.md), choose “[Give the Bread]”

    - **Needs:** stage 60; hand over 5× [Bread](../items/bread.md)
    - *“Th..thanks. Now, please tell me, where am I?”*


<span id="route-70"></span>

??? note "Stage 70 · Troublemaker · 2 ways"

    **Way 1:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “Very well. I will go and talk to Umar again. Bye.”

    - **Needs:** stage 65; not yet stage 70; latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60
    - *“Do that.”*

    **Way 2:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “But ...”

    - **Needs:** stage 65; not yet stage 70; latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60
    - *“Hey, what are you waiting for? Leave me and go talk with Umar or something!”*


<span id="route-75"></span>

??? note "Stage 75 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Urgh ... I just need better tasks! Do you still think I'm not yet ready?”

    - **Needs:** stage 70; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); not latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-75) is 75
    - **Gives:** faction “ThievesGuild” +10, 2500× [Gold coins](../items/gold.md)
    - *“First of all, take this gold for a job well done. We have already sent people to ask for the ransom.”*


<span id="route-76"></span>

??? note "Stage 76 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “I brought a valuable necklace from the noblewoman.”

    - **Needs:** stage 21, 24; not yet stage 20, 30, 76; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); hand over 1× [Sapphire Necklace](../items/g02_ambelie.md)
    - **Gives:** faction “ThievesGuild” +10
    - *“Well. I will take it as compensation for your mistakes.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 20 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 2 lines changed<br>· text: “(You tap her on the back of the head with the handle of your weapon, …” → “(You tap her on the back of the head with the handle of your weapon, …”<br>· text: “(You put Ambelie, who is still unconsicious, in a chair next to you) …” → “(You put Ambelie, who is still unconscious, in a chair next to you) O…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves02.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves02.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves02.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves02.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves02.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `Thieves02` |
    | showInLog | 1 |
    | Stage IDs | 2, 4, 6, 10, 15, 20, 21, 24, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 76 |
    | Dialogue nodes setting stages | 2: `umar_guild02_10`, 4: `umar_guild02_11b`, 6: `umar_guild02_13`, 10: `ambelie_guild02_2`, 15: `ff_captain_guild02_3`, 20: `ambelie_guild02_4b`, 21: `ambelie_guild02_16a`, 24: `ambelie_guild02_19`, 30: `umar_guild02_16`, 35: `umar_guild02_19`, 40: `umar_guild02_20`, 45: `troublemaker_guild02_6`, 50: `guild02_hatchlever_3a`, 55: `guild02_door_2`, 60: `troublemaker_guild02_8`, 65: `ambelie_guild02_12`, 70: `troublemaker_guild02_9_1`, 70: `troublemaker_guild02_10`, 75: `umar_guild02_25`, 76: `umar_guild02_32` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
