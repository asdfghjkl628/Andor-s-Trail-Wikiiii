# The ruthless Crackshot

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves03` |
| **In journal** | Yes |
| **Stages** | 26 (completes at 50) |
| **Started by** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Benbyr](../monsters/benbyr.md), [Dying Patrol](../monsters/g03_deadpatrol_2.md), [Dying patrol](../monsters/g03_deadpatrol_1.md), [Feygard barricade guard](../monsters/Feygard_BG.md), [Feygard patrol sergeant](../monsters/g03_sergeant.md), [Guard](../monsters/crossroads_guard.md) +1 |
| **Locations** | [crackshot_hideout2](../maps/crackshot_hideout2.md), [crackshot_hideout3](../maps/crackshot_hideout3.md), [crossroads](../maps/crossroads.md), [fallhaven_derelict2](../maps/fallhaven_derelict2.md) |
| **Total XP** | 9,625 |
| **Related quests** | 7 |

</div>

## Overview

> Time to rest and prepare myself to start the next job. I should go to the tavern.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
- reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76)
- NOT reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75)
- NOT reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Immaculate kidnapping](Thieves02.md#stage-76) | stage 76 reached, for stage 1 here |
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stages 1, 4, 5, 10, 45, 50 here |
| Requires | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-40) | stage 40 reached, for stage 26 here |
| Blocked by | [Immaculate kidnapping](Thieves02.md#stage-75) | stage 75 must NOT be reached, for stage 1 here |
| Mutually exclusive | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-40) | stage 40 must NOT be reached, for stage 27 here |
| Mutually exclusive | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-50) | stage 50 must NOT be reached, for stage 25 here |
| Blocked by | [Troubling times](troubling_times.md#stage-210) | stage 210 must NOT be reached, for stages 36, 41 here |
| Unlocks | [Beer Bootlegging](beer_bootlegging.md#stage-40) | stage 40 there needs stage 50 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-20) | stage 20 there needs stage 50 here |
| Blocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-130) | reaching stage 50 here closes stage 130 there |
| Blocks | [misc_nondisplay (hidden flag)](misc_nondisplay.md#stage-20) | reaching stage 1 here closes stage 20 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | Time to rest and prepare myself to start the next job. I should go to the tavern. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | changes map fallhaven_tavern<br>changes map fallhaven_nw<br>removes monsters from fallhaven_nw<br>removes monsters from guildbrig2 |
| <span id="stage-2"></span>2 | I really need to take a break ....<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span> | stepping on a trigger on [fallhaven_tavern](../maps/fallhaven_tavern.md) | – | changes map fallhaven_tavern |
| <span id="stage-3"></span>3 | I am now fully rested, so I should go back to Umar.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven north-west](../maps/fallhaven_nw.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span> | stepping on a trigger on [fallhaven_tavern](../maps/fallhaven_tavern.md) | – | changes map fallhaven_tavern<br>spawns monsters on fallhaven_nw |
| <span id="stage-4"></span>4 | Umar told me about a group of traitors led by a veteran of the Guild. It seems he stole the Key of Luthor. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 3 | – |
| <span id="stage-5"></span>5 | Umar went on to say that this team leader  was known as "Crackshot". He is probably also the responsible for a murder on the Duleian road. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 4 | – |
| <span id="stage-10"></span>10 | Crackshot and his henchmen are probably hiding somewhere near the Duleian road. I must ask people there whether they have seen them. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 5 | – |
| <span id="stage-11"></span>11 | It seems that Benbyr, a suspicious man outside Crossroads Guardhouse, doesn't know what I'm talking about. | [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) | stage 10 | – |
| <span id="stage-15"></span>15 | A Crossroads guard told me that Feygard has sent more soldiers to the south, to try and find the criminals' hideout. | [Guard](../monsters/crossroads_guard.md) ([crossroads](../maps/crossroads.md)) | stage 10 | – |
| <span id="stage-20"></span>20 | The barricade guard has a big mouth, and told me all I needed to know. The hideout is near a place full of larval burrowers. I need to move faster than the patrols to reach the hideout before them.<br><span class="qnote">🗺️ Part of [Woodcave0](../maps/woodcave0.md) visibly changes.</span> | [Feygard barricade guard](../monsters/Feygard_BG.md) ([road1](../maps/road1.md)) | stage 15 | changes map woodcave0 |
| <span id="stage-21"></span>21 | I found a small hole which seems to lead to a cave. Crackshot and his henchmen are probably hiding there.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Woodcave0](../maps/woodcave0.md).</span> | stepping on a trigger on [woodcave0](../maps/woodcave0.md) | – | – |
| <span id="stage-22"></span>22 | I reached the hideout and saw some recent blood stains. Maybe there was a fight there.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) | – | – |
| <span id="stage-23"></span>23 | The blood trail goes further ....<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) | – | – |
| <span id="stage-24"></span>24 | I heard screams and sword clashes nearby. I should take a look.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) | – | – |
| <span id="stage-25"></span>25 | There was a massacre. The Feygard patrol reached this place, but they seem to have all been killed. I must continue. | [Dying patrol](../monsters/g03_deadpatrol_1.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) | – | – |
| <span id="stage-26"></span>26 | As I progressed down the corridor the air became thicker. The blood smell was stronger, and I found another dying soldier. He said something about his sergeant and some other guy. | [Dying Patrol](../monsters/g03_deadpatrol_2.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) | – | – |
| <span id="stage-27"></span>27 | As I progressed down the corridor the air became thicker. The blood smell was stronger, and I found a dying soldier. He said something about his sergeant and some other guy. | [Dying Patrol](../monsters/g03_deadpatrol_2.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) | – | – |
| <span id="stage-28"></span>28 | I found another dying soldier. There was a massacre. The Feygard patrol reached this place, but they seem to have all been killed. I must continue. | [Dying patrol](../monsters/g03_deadpatrol_1.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) | – | – |
| <span id="stage-30"></span>30 | I've found the patrol sergeant. He advised me to leave this dangerous place. | [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) | – | – |
| <span id="stage-31"></span>31 | The patrol sergeant told me about what happened before. He's tired and wounded, so I willl avenge his fellows.  | [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) | stage 30 | – |
| <span id="stage-32"></span>32 | The patrol sergeant has left to call for backup. Now I'm alone again. Time to defeat Crackshot. | [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) | stage 31 | 1,125 XP<br>removes monsters from crackshot_hideout3 |
| <span id="stage-35"></span>35 | I killed Crackshot and he had the key of Luthor with him. I have to go back and report to Umar.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout3](../maps/crackshot_hideout3.md).</span> | stepping on a trigger on [crackshot_hideout3](../maps/crackshot_hideout3.md) | – | – |
| <span id="stage-36"></span>36 | I tried to open the door behind Crackshot, but for some reason I cannot get the key into the lock. | walking into a blocked passage on [crackshot_hideout3](../maps/crackshot_hideout3.md) | carry 1× [Key of Luthor](../items/g03_luthor.md) | – |
| <span id="stage-40"></span>40 | The dying Crackshot said something about the key. If he told the truth, it could be cursed.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout3](../maps/crackshot_hideout3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven derelict2 t](../maps/fallhaven_derelict2_t.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven derelict2](../maps/fallhaven_derelict2.md).</span> | stepping on a trigger on [crackshot_hideout3](../maps/crackshot_hideout3.md) | – | 1,000 XP<br>clears stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20)<br>removes monsters from road1<br>sets stage 30 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-30) |
| <span id="stage-41"></span>41 | I tried to open the door behind Crackshot, but for some reason I could not get the key turned in the lock. | walking into a blocked passage on [crackshot_hideout3](../maps/crackshot_hideout3.md) | carry 1× [Key of Luthor](../items/g03_luthor.md) | – |
| <span id="stage-45"></span>45 | I reported about the situation to Umar, and gave him the key. He did not seem to want to tell me more about the key - yet. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | hand over 1× [Key of Luthor](../items/g03_luthor.md), stage 40 | – |
| <span id="stage-50"></span>50 | Finally, this job is done. Now I should take a rest and regain my strength. **(completes quest)** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 45 | 7,500 XP<br>gives 4000× [Gold coins](../items/gold.md)<br>gives 10× [Mead](../items/mead.md)<br>faction “ThievesGuild” +20 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Good idea.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76); NOT reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75); NOT reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1) → **stage 1**; also changes map fallhaven_tavern, changes map fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from guildbrig2. NPC: “Come back to me when you're prepared. Bear in mind that your next task isn't going to be as easy as the ones you…”

???+ note "Stage 2: 1 route"

    1. stepping on a trigger on [fallhaven_tavern](../maps/fallhaven_tavern.md) → the conversation leads here automatically → **stage 2**; also changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern. NPC: “(You should go to the bed now. You take off your bag and grab the blanket. This bed is more comfortable than you…”

???+ note "Stage 3: 1 route"

    1. stepping on a trigger on [fallhaven_tavern](../maps/fallhaven_tavern.md) → the conversation leads here automatically → **stage 3**; also changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw. NPC: “(The sun rises and you open your eyes. You feel fully rested and eager to talk with Umar. He's probably waiting for…”

???+ note "Stage 4: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “And what happened then?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 3 of [The ruthless Crackshot](../quests/Thieves03.md#stage-3); NOT reached stage 4 of [The ruthless Crackshot](../quests/Thieves03.md#stage-4) → **stage 4**. NPC: “The team leader and others loyal to him killed the rest of the team and escaped with the key, before entering the…”

???+ note "Stage 5: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “And you think the traitors are involved in that?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 4 of [The ruthless Crackshot](../quests/Thieves03.md#stage-4); NOT reached stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5) → **stage 5**. NPC: “I'm pretty sure about it. The team leader is the one we call "Crackshot", as he is a master of murder, torture and the…”

???+ note "Stage 10: 2 routes"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “What? How I will find him then?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5); NOT reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10) → **stage 10**. NPC: “Probably people near the Duleian road guard tower know more. See if you can ask them for tips.”
    2. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “He will show up sooner or later ...” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 5 of [The ruthless Crackshot](../quests/Thieves03.md#stage-5); NOT reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10) → **stage 10**. NPC: “Maybe, but it will be faster if you question people near the Duleian road guard tower. The Duleian road is the place…”

???+ note "Stage 11: 1 route"

    1. Talk to [Benbyr](../monsters/benbyr.md) ([crossroads](../maps/crossroads.md)) → choose “Hi. Have you heard about the murder not far from here?” — **conditions:** reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 11 of [The ruthless Crackshot](../quests/Thieves03.md#stage-11) → **stage 11**. NPC: “What? A murder? I don't know what you're talking about, sorry.”

???+ note "Stage 15: 1 route"

    1. Talk to [Guard](../monsters/crossroads_guard.md) ([crossroads](../maps/crossroads.md)) → choose “Sorry, have you heard anything about a murder?” — **conditions:** reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15) → **stage 15**. NPC: “Yeah, Feygard authorities have sent more patrols to the south. Apparently there is a group of criminals hiding in the…”

???+ note "Stage 20: 1 route"

    1. Talk to [Feygard barricade guard](../monsters/Feygard_BG.md) ([road1](../maps/road1.md)) → choose “Anything else?” — **conditions:** reached stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15); NOT reached stage 20 of [The ruthless Crackshot](../quests/Thieves03.md#stage-20) → **stage 20**; also changes map woodcave0. NPC: “Yes! Those crimin ... Wait, you don't have to know this information! Forget everything I've said!”

???+ note "Stage 21: 1 route"

    1. stepping on a trigger on [woodcave0](../maps/woodcave0.md) → the conversation leads here automatically → **stage 21**. NPC: “(You see a hole leading to a cave. Maybe this is a good place to start searching.)”

???+ note "Stage 22: 1 route"

    1. stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 22 of [The ruthless Crackshot](../quests/Thieves03.md#stage-22) → **stage 22**. NPC: “(You look at the floor. The blood hasn't coagulated yet. It seems there has been a recent fight between two or more…”

???+ note "Stage 23: 1 route"

    1. stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 23 of [The ruthless Crackshot](../quests/Thieves03.md#stage-23) → **stage 23**. NPC: “(More blood. There's no doubt, there has been a fight here.)”

???+ note "Stage 24: 1 route"

    1. stepping on a trigger on [crackshot_hideout1](../maps/crackshot_hideout1.md) → the conversation leads here automatically — **conditions:** NOT reached stage 24 of [The ruthless Crackshot](../quests/Thieves03.md#stage-24) → **stage 24**. NPC: “ARGH!! *sword clashing* Sergeant! Sergeant! ... *laughter*”

???+ note "Stage 25: 1 route"

    1. Talk to [Dying patrol](../monsters/g03_deadpatrol_1.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 50 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-50) → **stage 25**

???+ note "Stage 26: 1 route"

    1. Talk to [Dying Patrol](../monsters/g03_deadpatrol_2.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) → choose “What guy?” — **conditions:** reached stage 40 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-40) → **stage 26**

???+ note "Stage 27: 1 route"

    1. Talk to [Dying Patrol](../monsters/g03_deadpatrol_2.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) → choose “What guy?” — **conditions:** NOT reached stage 40 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-40) → **stage 27**

???+ note "Stage 28: 1 route"

    1. Talk to [Dying patrol](../monsters/g03_deadpatrol_1.md) ([crackshot_hideout2](../maps/crackshot_hideout2.md)) → the conversation leads here automatically → **stage 28**

???+ note "Stage 30: 1 route"

    1. Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) → choose “Eh ... I am ...” → **stage 30**. NPC: “Wait! That's not actually important. Leave this dangerous place, right now!”

???+ note "Stage 31: 1 route"

    1. Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) → choose “Unexpected?” — **conditions:** reached stage 30 of [The ruthless Crackshot](../quests/Thieves03.md#stage-30) → **stage 31**. NPC: “Don't you understand? You must leave this place before you can't. He's playing with us!”

???+ note "Stage 32: 1 route"

    1. Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([crackshot_hideout3](../maps/crackshot_hideout3.md)) → choose “Don't be rude! I'm here to help you. Please leave and go to a safer place.” — **conditions:** reached stage 31 of [The ruthless Crackshot](../quests/Thieves03.md#stage-31) → **stage 32**; also removes monsters from crackshot_hideout3. NPC: “Agh, thank you. You are valiant, kid. I hope to see you when we are both out of here. I'll invite you for a drink!”

???+ note "Stage 35: 1 route"

    1. stepping on a trigger on [crackshot_hideout3](../maps/crackshot_hideout3.md) → the conversation leads here automatically — **conditions:** killed 1× [Crackshot](../monsters/g03_crackshot.md) → **stage 35**

???+ note "Stage 36: 1 route"

    1. walking into a blocked passage on [crackshot_hideout3](../maps/crackshot_hideout3.md) → choose “Insert the key of Luthor into the lock.” — **conditions:** NOT reached stage 210 of [Troubling times](../quests/troubling_times.md#stage-210); carry 1× [Key of Luthor](../items/g03_luthor.md); NOT reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40) → **stage 36**

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [crackshot_hideout3](../maps/crackshot_hideout3.md) → choose “What are you talking about?” — **conditions:** killed 1× [Crackshot](../monsters/g03_crackshot.md); NOT reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40) → **stage 40**; also clears stage 20 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-20), removes monsters from road1, sets stage 30 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-30). NPC: “The key is cursed .... She ... I am ... (Crackshot finally dies, emitting a soft bluish breath)”

???+ note "Stage 41: 1 route"

    1. walking into a blocked passage on [crackshot_hideout3](../maps/crackshot_hideout3.md) → choose “Insert the key of Luthor into the lock.” — **conditions:** NOT reached stage 210 of [Troubling times](../quests/troubling_times.md#stage-210); carry 1× [Key of Luthor](../items/g03_luthor.md); NOT reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); NOT reached stage 36 of [The ruthless Crackshot](../quests/Thieves03.md#stage-36) → **stage 41**

???+ note "Stage 45: 3 routes"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Oh. Yes, I remember now that I found the key. Here, take it.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40); NOT reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); hand over 1× [Key of Luthor](../items/g03_luthor.md) → **stage 45**. NPC: “Why did it take so long? And do not look at me that way. I can not tell you anything about the key for now.”
    2. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Yes ... [give key]. Why is this key so important to us?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40); NOT reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); hand over 1× [Key of Luthor](../items/g03_luthor.md) → **stage 45**. NPC: “I'm sorry, but for now I can't say more.”
    3. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Sure, here, take it. And maybe it's time to give me some more information.” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40); NOT reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); hand over 1× [Key of Luthor](../items/g03_luthor.md) → **stage 45**. NPC: “Be patient, my friend. Everything will come in due time.”

???+ note "Stage 50: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Understood ....” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 45 of [The ruthless Crackshot](../quests/Thieves03.md#stage-45); NOT reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50) → **stage 50**; also gives 4000× [Gold coins](../items/gold.md), gives 10× [Mead](../items/mead.md), faction “ThievesGuild” +20. NPC: “Take 4,000 gold coins, and some bottles of my favorite mead. Now you deserve a good rest, my friend. You have earned…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 29 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Yeah, Feygard authorities have sent more patrols to the south. Appear…” → “Yeah, Feygard authorities have sent more patrols to the south. Appare…” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “Take 4000 gold coins, and some bottles of my favourite mead. Now you …” → “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line changed<br>· text: “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” → “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Take 4000 gold coins, and some bottles of my favorite mead. Now you d…” → “Take {4000} gold coins, and some bottles of my favorite mead. Now you…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `Thieves03` |
    | showInLog | 1 |
    | Stage IDs | 1, 2, 3, 4, 5, 10, 11, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 35, 36, 40, 41, 45, 50 |
    | Dialogue nodes setting stages | 1: `umar_guild02_27c`, 2: `guild03_rest1`, 3: `guild03_rest4`, 4: `umar_guild03_10b`, 5: `umar_guild03_13`, 10: `umar_guild03_18a`, 10: `umar_guild03_18b`, 11: `benbyr_guild03_2`, 15: `crossroads_guild03_2`, 20: `Feygard_BG_guild03_5`, 21: `guild03_Hentrance_1`, 22: `guild03_blood_1a`, 23: `guild03_blood_2a`, 24: `guild03_sword_clashing`, 25: `guild03_deadpatrol1_was_first`, 26: `guild03_deadpatrol_2_was_second`, 27: `guild03_deadpatrol_2_was_first`, 28: `guild03_deadpatrol1_was_second`, 30: `FeygardSerg_guild03_2`, 31: `FeygardSerg_guild03_9a`, 32: `FeygardSerg_guild03_10`, 35: `guild03_crackshot_is_dead`, 36: `guild03_hideout3_lock3`, 40: `guild03_hideout3_exit_3`, 41: `guild03_hideout3_lock4`, 45: `umar_guild03_25_3`, 45: `umar_guild03_26a`, 45: `umar_guild03_26b`, 50: `umar_guild03_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
