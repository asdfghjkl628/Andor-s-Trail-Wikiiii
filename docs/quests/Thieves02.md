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
| **Started by** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Ambelie](../monsters/ambelie.md), [Feygard patrol captain](../monsters/feygard_patrol_captain.md), [Troublemaker](../monsters/troublemaker.md), [Umar](../monsters/umar.md) |
| **Locations** | [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md), [foaming_flask](../maps/foaming_flask.md) |
| **Total XP** | 9,350 |
| **Related quests** | 5 |

</div>

## Overview

> After completing my first task I'm considered a member of Thieves' Guild. Now I have to perform a very risky task. Umar sent me to kidnap a noble woman from Feygard, without being discovered.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)). Required:

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
| Unlocks | [misc_nondisplay (hidden flag)](misc_nondisplay.md#stage-20) | stage 20 there needs stage 76 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-20) | stage 20 there needs stages 15, 21 here |
| Blocks | [The ruthless Crackshot](Thieves03.md#stage-1) | reaching stage 75 here closes stage 1 there |
| Blocks | [misc_nondisplay (hidden flag)](misc_nondisplay.md#stage-20) | reaching stage 75 here closes stage 20 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-2"></span>2 | After completing my first task I'm considered a member of Thieves' Guild. Now I have to perform a very risky task. Umar sent me to kidnap a noble woman from Feygard, without being discovered. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-4"></span>4 | She was recently seen in the Foaming Flask tavern. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 2 | – |
| <span id="stage-6"></span>6 | Umar gave me some advice. My strength is not always the solution. I must "use my tongue" to avoid raising suspicion in the tavern. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 4 | – |
| <span id="stage-10"></span>10 | Ambelie Laumwill doesn't want to come with me peacefully. I cannot make a scene, or the guards will alert other patrols. Maybe talking with them would solve the situation. | [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 4 | – |
| <span id="stage-15"></span>15 | I have "used my tongue" with the main Feygard soldier in the Foaming Flask tavern. He gave me permission to "escort back" Ambelie. | [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) | pay 1,000 gold, stage 10 | – |
| <span id="stage-20"></span>20 | I knocked out Ambelie. I will take her back to the Guild. | [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 15 | removes monsters from foaming_flask<br>spawns monsters on road1<br>applies condition carrying_ambelie<br>sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20) |
| <span id="stage-21"></span>21 | I have decided not to kidnap Ambelie. I must think of another solution. | [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) | – | – |
| <span id="stage-24"></span>24 | Ambelie gave me a very valuable necklace. I must talk with Umar and persuade him to no longer pursue her. | [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) | stage 21 | gives 1× [Sapphire Necklace](../items/g02_ambelie.md)<br>spawns monsters on road1<br>sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20) |
| <span id="stage-30"></span>30 | I safely brought Ambelie to the basement. However, keeping her here could be dangerous. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 20 | 1,200 XP |
| <span id="stage-35"></span>35 | Umar believes there is a secure room for these types of "visitors". I should talk to Troublemaker. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 30 | – |
| <span id="stage-40"></span>40 | I have talked to Troublemaker about the place Umar believes it's okay to safely keep the hostage. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 35 | – |
| <span id="stage-45"></span>45 | Troublemaker has given me the key to the Guild brig. I should take Ambelie there and leave her to wake up. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 40 | 1,000 XP<br>gives 1× [Guild brig key](../items/guildbrigK.md) |
| <span id="stage-50"></span>50 | I've inserted the key and moved the lever. A hatchway has opened in the room.<br><span class="qnote">🗺️ Part of [Fallhaven gravedigger](../maps/fallhaven_gravedigger.md) visibly changes.</span> | walking into a blocked passage on [fallhaven_gravedigger](../maps/fallhaven_gravedigger.md) | carry 1× [Guild brig key](../items/guildbrigK.md), hand over 1× [Guild brig key](../items/guildbrigK.md), stage 45 | changes map fallhaven_gravedigger |
| <span id="stage-55"></span>55 | I left Ambelie in that ugly, dark, and cold place. I should go back.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Guildbrig2](../maps/guildbrig2.md).</span> | walking into a blocked passage on [guildbrig2](../maps/guildbrig2.md) | stage 50 | spawns monsters on guildbrig2<br>applies condition carrying_ambelie |
| <span id="stage-60"></span>60 | Troublemaker gave me some bread for Ambelie. The guild doesn't want her to starve to death. Indeed, they want her to be as comfortable as possible. I must go to the brig again. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 55 | gives 5× [Bread](../items/bread.md) |
| <span id="stage-65"></span>65 | I gave the bread to Ambelie. I should report Troublemaker that I completed the job.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Guildbrig2](../maps/guildbrig2.md).</span> | stepping on a trigger on [guildbrig2](../maps/guildbrig2.md)<br>[Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) | hand over 5× [Bread](../items/bread.md), stage 60 | 400 XP |
| <span id="stage-70"></span>70 | The job finally seems to be finished. I just have to talk with Umar again. However, I do not feel good about this. Kidnappings are definitely not my kind of job. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 65 | – |
| <span id="stage-75"></span>75 | I completed this task successfully. Umar told me they have sent couriers to Feygard, and the ransom is almost guaranteed. He paid me for my work. **(completes quest)** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 70 | 4,500 XP<br>faction “ThievesGuild” +10<br>gives 2500× [Gold coins](../items/gold.md) |
| <span id="stage-76"></span>76 | Umar took the necklace as compensation for my errors. Everything is fine again. **(completes quest)** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | hand over 1× [Sapphire Necklace](../items/g02_ambelie.md), stage 21, stage 24 | 2,250 XP<br>faction “ThievesGuild” +10 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 2: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Anything more about my new task?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2; NOT reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4) → **stage 2**. NPC: “I want you to bring the noble woman here, so that we can ask for a substantial ransom from her generous father.”

???+ note "Stage 4: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Where can I find this woman?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-2) is 2; NOT reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4) → **stage 4**. NPC: “Scouts have seen the lady in the Foaming flask tavern. We do not want to be discovered, so act quietly. Guards are a…”

???+ note "Stage 6: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Anything more about my new task?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-4) is 4; NOT reached stage 6 of [Immaculate kidnapping](../quests/Thieves02.md#stage-6); NOT reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15) → **stage 6**. NPC: “Use your tongue, young man. Sometimes it is more important than your sword skills.”

???+ note "Stage 10: 1 route"

    1. Talk to [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “But I'm not a commoner! I'm a ... Feygard spy. These clothes are my disguise!” — **conditions:** reached stage 4 of [Immaculate kidnapping](../quests/Thieves02.md#stage-4); NOT reached stage 10 of [Immaculate kidnapping](../quests/Thieves02.md#stage-10) → **stage 10**. NPC: “Anyway, I prefer to stay in this place for now. Get away from me!”

???+ note "Stage 15: 1 route"

    1. Talk to [Feygard patrol captain](../monsters/feygard_patrol_captain.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “Ergh ... Mr Laumwill is grateful for your protection. However ... Ah! He has given this reward of 1,000 gold…” — **conditions:** reached stage 10 of [Immaculate kidnapping](../quests/Thieves02.md#stage-10); NOT reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15); pay 1,000 gold → **stage 15**. NPC: “I have to stay here to supervise my guards. They sometimes need educating about what to do. I assume you're able to…”

???+ note "Stage 20: 1 route"

    1. Talk to [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “(Knock her out) Time to sleep!” — **conditions:** reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15) → **stage 20**; also removes monsters from foaming_flask, spawns monsters on road1, applies condition carrying_ambelie, sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20). NPC: “(You tap her on the back of the head with the handle of your weapon, and she falls unconscious)”

???+ note "Stage 21: 1 route"

    1. Talk to [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “I'm not going to hurt you.” — **conditions:** reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21) → **stage 21**. NPC: “Then get out of my sight now!”

???+ note "Stage 24: 1 route"

    1. Talk to [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “Give me something of value, and you won't see me again.” — **conditions:** reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21) → **stage 24**; also gives 1× [Sapphire Necklace](../items/g02_ambelie.md), spawns monsters on road1, sets stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20). NPC: “Take this and leave me, please.”

???+ note "Stage 30: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I have brought the hostage.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20); NOT reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21); NOT reached stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24) → **stage 30**. NPC: “(You put Ambelie, who is still unconscious, in a chair next to you) Oh! How did you get here so fast? I've heard…”

???+ note "Stage 35: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “What am I supposed to do with the noblewoman?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 35 of [Immaculate kidnapping](../quests/Thieves02.md#stage-35) → **stage 35**. NPC: “We are supposed to have one room for receiving "visitors". However, I don't know if It's finished.”

???+ note "Stage 40: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “What am I supposed to do with the noblewoman?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 35 of [Immaculate kidnapping](../quests/Thieves02.md#stage-35); NOT reached stage 40 of [Immaculate kidnapping](../quests/Thieves02.md#stage-40) → **stage 40**. NPC: “Hmm, I believe Troublemaker knows the actual state of that place. Ask him, and if it's possible leave our guest there.”

???+ note "Stage 45: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Whatever, anything more?” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; reached stage 40 of [Immaculate kidnapping](../quests/Thieves02.md#stage-40); NOT reached stage 45 of [Immaculate kidnapping](../quests/Thieves02.md#stage-45) → **stage 45**; also gives 1× [Guild brig key](../items/guildbrigK.md). NPC: “I almost forgot. Take this key. Make sure you put it in correctly to open the hatchway.”

???+ note "Stage 50: 1 route"

    1. walking into a blocked passage on [fallhaven_gravedigger](../maps/fallhaven_gravedigger.md) → choose “Put the key into the lock.” — **conditions:** reached stage 45 of [Immaculate kidnapping](../quests/Thieves02.md#stage-45); carry 1× [Guild brig key](../items/guildbrigK.md); hand over 1× [Guild brig key](../items/guildbrigK.md) → **stage 50**; also changes map fallhaven_gravedigger. NPC: “You insert the key in the lock. You can hear strange noises and creaks as you turn the key. You make an extra effort,…”

???+ note "Stage 55: 1 route"

    1. walking into a blocked passage on [guildbrig2](../maps/guildbrig2.md) → choose “Put Ambelie inside the room.” — **conditions:** reached stage 50 of [Immaculate kidnapping](../quests/Thieves02.md#stage-50) → **stage 55**; also spawns monsters on guildbrig2, applies condition carrying_ambelie. NPC: “You leave Ambelie in the cell and close the door.”

???+ note "Stage 60: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I've dealt with the lady.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-55) is 55; NOT reached stage 65 of [Immaculate kidnapping](../quests/Thieves02.md#stage-65) → **stage 60**; also gives 5× [Bread](../items/bread.md). NPC: “Ah, yes ... that captive. Take this food and make sure she is comfortable enough. We don't want her starving right?…”

???+ note "Stage 65: 2 routes"

    1. stepping on a trigger on [guildbrig2](../maps/guildbrig2.md) → choose “[Give the Bread]” — **conditions:** latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-60) is 60; hand over 5× [Bread](../items/bread.md) → **stage 65**. NPC: “Th..thanks. Now, please tell me, where am I?”
    2. Talk to [Ambelie](../monsters/ambelie.md) ([foaming_flask](../maps/foaming_flask.md)) → choose “[Give the Bread]” — **conditions:** reached stage 60 of [Immaculate kidnapping](../quests/Thieves02.md#stage-60); hand over 5× [Bread](../items/bread.md) → **stage 65**. NPC: “Th..thanks. Now, please tell me, where am I?”

???+ note "Stage 70: 2 routes"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Very well. I will go and talk to Umar again. Bye.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; reached stage 65 of [Immaculate kidnapping](../quests/Thieves02.md#stage-65); NOT reached stage 70 of [Immaculate kidnapping](../quests/Thieves02.md#stage-70) → **stage 70**. NPC: “Do that.”
    2. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “But ...” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; reached stage 65 of [Immaculate kidnapping](../quests/Thieves02.md#stage-65); NOT reached stage 70 of [Immaculate kidnapping](../quests/Thieves02.md#stage-70) → **stage 70**. NPC: “Hey, what are you waiting for? Leave me and go talk with Umar or something!”

???+ note "Stage 75: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Urgh ... I just need better tasks! Do you still think I'm not yet ready?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); NOT latest stage of [Immaculate kidnapping](../quests/Thieves02.md#stage-75) is 75; reached stage 70 of [Immaculate kidnapping](../quests/Thieves02.md#stage-70) → **stage 75**; also faction “ThievesGuild” +10, gives 2500× [Gold coins](../items/gold.md). NPC: “First of all, take this gold for a job well done. We have already sent people to ask for the ransom.”

???+ note "Stage 76: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I brought a valuable necklace from the noblewoman.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24); reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21); NOT reached stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20); NOT reached stage 30 of [Immaculate kidnapping](../quests/Thieves02.md#stage-30); NOT reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76); hand over 1× [Sapphire Necklace](../items/g02_ambelie.md) → **stage 76**; also faction “ThievesGuild” +10. NPC: “Well. I will take it as compensation for your mistakes.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 20 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 2 lines changed<br>· text: “(You put Ambelie, who is still unconsicious, in a chair next to you) …” → “(You put Ambelie, who is still unconscious, in a chair next to you) O…”<br>· text: “(You tap her on the back of the head with the handle of your weapon, …” → “(You tap her on the back of the head with the handle of your weapon, …” |

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
