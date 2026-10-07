---
description: "The ruthless Crackshot is a quest in Andor's Trail, started by Umar (fallhaven_derelict2). 26 stages, 9,625 XP in total. Time to rest and prepare myself to start the next job. I should go to the tavern."
---

# The ruthless Crackshot

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves03` |
| **In journal** | Yes |
| **Stages** | 26 (completes at 50) |
| **Started by** | [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Benbyr](../monsters/benbyr.md), [Dying Patrol](../monsters/g03_deadpatrol_2.md), [Dying patrol](../monsters/g03_deadpatrol_1.md), [Feygard barricade guard](../monsters/Feygard_BG.md), [Feygard patrol sergeant](../monsters/g03_sergeant.md), [Guard](../monsters/guard.md#v-crossroads_guard) +1 |
| **Locations** | [Crackshot hideout 2](../maps/crackshot_hideout2.md), [Crackshot hideout 3](../maps/crackshot_hideout3.md), [Crossroads](../maps/crossroads.md), [Fallhaven derelict 2](../maps/fallhaven_derelict2.md) |
| **Total XP** | 9,625 |
| **Related quests** | 7 |

</div>

## Overview

> Time to rest and prepare myself to start the next job. I should go to the tavern.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)). Required:

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
| Requires | [Thieves story flags (hidden flag)](thieves_hidden.md#stage-40) | stage 40 reached, for stage 26 here |
| Blocked by | [Immaculate kidnapping](Thieves02.md#stage-75) | stage 75 must NOT be reached, for stage 1 here |
| Mutually exclusive | [Thieves story flags (hidden flag)](thieves_hidden.md#stage-40) | stage 40 must NOT be reached, for stage 27 here |
| Mutually exclusive | [Thieves story flags (hidden flag)](thieves_hidden.md#stage-50) | stage 50 must NOT be reached, for stage 25 here |
| Blocked by | [Troubling times](troubling_times.md#stage-210) | stage 210 must NOT be reached, for stages 36, 41 here |
| Unlocks | [Beer Bootlegging](beer_bootlegging.md#stage-40) | stage 40 there needs stage 50 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-20) | stage 20 there needs stage 50 here |
| Blocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-130) | reaching stage 50 here closes stage 130 there |
| Blocks | [Miscellaneous story flags (hidden flag)](misc_nondisplay.md#stage-20) | reaching stage 1 here closes stage 20 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-1"></span>[1](#route-1) | <details class="jt"><summary><span class="s">Time to rest and prepare myself to start the next job. I should go… ▸</span><span class="l">▴ less</span></summary>Time to rest and prepare myself to start the next job. I should go to the tavern.</details> | [Umar](../monsters/umar.md) | changes map fallhaven_tavern, changes map fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from guildbrig2 |
| <span id="stage-2"></span>[2](#route-2) | I really need to take a break ....<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span> | stepping on a trigger on [Fallhaven tavern](../maps/fallhaven_tavern.md) | changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern |
| <span id="stage-3"></span>[3](#route-3) | I am now fully rested, so I should go back to Umar.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven north-west](../maps/fallhaven_nw.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven tavern](../maps/fallhaven_tavern.md).</span> | stepping on a trigger on [Fallhaven tavern](../maps/fallhaven_tavern.md) | changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw |
| <span id="stage-4"></span>[4](#route-4) | <details class="jt"><summary><span class="s">Umar told me about a group of traitors led by a veteran of the… ▸</span><span class="l">▴ less</span></summary>Umar told me about a group of traitors led by a veteran of the Guild. It seems he stole the Key of Luthor.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-5"></span>[5](#route-5) | <details class="jt"><summary><span class="s">Umar went on to say that this team leader was known as "Crackshot".… ▸</span><span class="l">▴ less</span></summary>Umar went on to say that this team leader was known as "Crackshot". He is probably also the responsible for a murder on the Duleian road.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">Crackshot and his henchmen are probably hiding somewhere near the… ▸</span><span class="l">▴ less</span></summary>Crackshot and his henchmen are probably hiding somewhere near the Duleian road. I must ask people there whether they have seen them.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-11"></span>[11](#route-11) | <details class="jt"><summary><span class="s">It seems that Benbyr, a suspicious man outside Crossroads… ▸</span><span class="l">▴ less</span></summary>It seems that Benbyr, a suspicious man outside Crossroads Guardhouse, doesn't know what I'm talking about.</details> | [Benbyr](../monsters/benbyr.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">A Crossroads guard told me that Feygard has sent more soldiers to… ▸</span><span class="l">▴ less</span></summary>A Crossroads guard told me that Feygard has sent more soldiers to the south, to try and find the criminals' hideout.</details> | [Guard](../monsters/guard.md#v-crossroads_guard) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">The barricade guard has a big mouth, and told me all I needed to… ▸</span><span class="l">▴ less</span></summary>The barricade guard has a big mouth, and told me all I needed to know. The hideout is near a place full of larval burrowers. I need to move faster than the patrols to reach the hideout before them.</details><br><span class="qnote">🗺️ Part of [Woodcave 0](../maps/woodcave0.md) visibly changes.</span> | [Feygard barricade guard](../monsters/Feygard_BG.md) | changes map woodcave0 |
| <span id="stage-21"></span>[21](#route-21) | <details class="jt"><summary><span class="s">I found a small hole which seems to lead to a cave. Crackshot and… ▸</span><span class="l">▴ less</span></summary>I found a small hole which seems to lead to a cave. Crackshot and his henchmen are probably hiding there.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Woodcave 0](../maps/woodcave0.md).</span> | stepping on a trigger on [Woodcave 0](../maps/woodcave0.md) | – |
| <span id="stage-22"></span>[22](#route-22) | <details class="jt"><summary><span class="s">I reached the hideout and saw some recent blood stains. Maybe there… ▸</span><span class="l">▴ less</span></summary>I reached the hideout and saw some recent blood stains. Maybe there was a fight there.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md) | – |
| <span id="stage-23"></span>[23](#route-23) | The blood trail goes further ....<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md) | – |
| <span id="stage-24"></span>[24](#route-24) | I heard screams and sword clashes nearby. I should take a look.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 1](../maps/crackshot_hideout1.md).</span> | stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md) | – |
| <span id="stage-25"></span>[25](#route-25) | <details class="jt"><summary><span class="s">There was a massacre. The Feygard patrol reached this place, but… ▸</span><span class="l">▴ less</span></summary>There was a massacre. The Feygard patrol reached this place, but they seem to have all been killed. I must continue.</details> | [Dying patrol](../monsters/g03_deadpatrol_1.md) | – |
| <span id="stage-26"></span>[26](#route-26) | <details class="jt"><summary><span class="s">As I progressed down the corridor the air became thicker. The blood… ▸</span><span class="l">▴ less</span></summary>As I progressed down the corridor the air became thicker. The blood smell was stronger, and I found another dying soldier. He said something about his sergeant and some other guy.</details> | [Dying Patrol](../monsters/g03_deadpatrol_2.md) | – |
| <span id="stage-27"></span>[27](#route-27) | <details class="jt"><summary><span class="s">As I progressed down the corridor the air became thicker. The blood… ▸</span><span class="l">▴ less</span></summary>As I progressed down the corridor the air became thicker. The blood smell was stronger, and I found a dying soldier. He said something about his sergeant and some other guy.</details> | [Dying Patrol](../monsters/g03_deadpatrol_2.md) | – |
| <span id="stage-28"></span>[28](#route-28) | <details class="jt"><summary><span class="s">I found another dying soldier. There was a massacre. The Feygard… ▸</span><span class="l">▴ less</span></summary>I found another dying soldier. There was a massacre. The Feygard patrol reached this place, but they seem to have all been killed. I must continue.</details> | [Dying patrol](../monsters/g03_deadpatrol_1.md) | – |
| <span id="stage-30"></span>[30](#route-30) | I've found the patrol sergeant. He advised me to leave this dangerous place. | [Feygard patrol sergeant](../monsters/g03_sergeant.md) | – |
| <span id="stage-31"></span>[31](#route-31) | <details class="jt"><summary><span class="s">The patrol sergeant told me about what happened before. He's tired… ▸</span><span class="l">▴ less</span></summary>The patrol sergeant told me about what happened before. He's tired and wounded, so I willl avenge his fellows.</details> | [Feygard patrol sergeant](../monsters/g03_sergeant.md) | – |
| <span id="stage-32"></span>[32](#route-32) | <details class="jt"><summary><span class="s">The patrol sergeant has left to call for backup. Now I'm alone… ▸</span><span class="l">▴ less</span></summary>The patrol sergeant has left to call for backup. Now I'm alone again. Time to defeat Crackshot.</details> | [Feygard patrol sergeant](../monsters/g03_sergeant.md) | 1,125 XP, removes monsters from crackshot_hideout3 |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">I killed Crackshot and he had the key of Luthor with him. I have to… ▸</span><span class="l">▴ less</span></summary>I killed Crackshot and he had the key of Luthor with him. I have to go back and report to Umar.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 3](../maps/crackshot_hideout3.md).</span> | stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – |
| <span id="stage-36"></span>[36](#route-36) | <details class="jt"><summary><span class="s">I tried to open the door behind Crackshot, but for some reason I… ▸</span><span class="l">▴ less</span></summary>I tried to open the door behind Crackshot, but for some reason I cannot get the key into the lock.</details> | walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – |
| <span id="stage-40"></span>[40](#route-40) | <details class="jt"><summary><span class="s">The dying Crackshot said something about the key. If he told the… ▸</span><span class="l">▴ less</span></summary>The dying Crackshot said something about the key. If he told the truth, it could be cursed.</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 3](../maps/crackshot_hideout3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven derelict 2 t](../maps/fallhaven_derelict2_t.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven derelict 2](../maps/fallhaven_derelict2.md).</span> | stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | 1,000 XP, removes monsters from road1 |
| <span id="stage-41"></span>[41](#route-41) | <details class="jt"><summary><span class="s">I tried to open the door behind Crackshot, but for some reason I… ▸</span><span class="l">▴ less</span></summary>I tried to open the door behind Crackshot, but for some reason I could not get the key turned in the lock.</details> | walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – |
| <span id="stage-45"></span>[45](#route-45) | <details class="jt"><summary><span class="s">I reported about the situation to Umar, and gave him the key. He did… ▸</span><span class="l">▴ less</span></summary>I reported about the situation to Umar, and gave him the key. He did not seem to want to tell me more about the key - yet.</details> | [Umar](../monsters/umar.md) | – |
| <span id="stage-50"></span>[50](#route-50) | Finally, this job is done. Now I should take a rest and regain my strength. **(ends quest)** | [Umar](../monsters/umar.md) | 7,500 XP, 4000× [Gold coins](../items/gold.md), 10× [Mead](../items/mead.md), faction “ThievesGuild” +20 |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-1"></span>

??? note "Stage 1 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Good idea.”

    - **Needs:** not yet stage 1; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76); not reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75)
    - **Gives:** changes map fallhaven_tavern, changes map fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from fallhaven_nw, removes monsters from guildbrig2
    - *“Come back to me when you're prepared. Bear in mind that your next task isn't going to be as easy as the ones you already did. We'll talk…”*


<span id="route-2"></span>

??? note "Stage 2 · stepping on a trigger on fallhaven_tavern · 1 way"

    **Way 1:** Stepping on a trigger on [Fallhaven tavern](../maps/fallhaven_tavern.md)

    - **Gives:** changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern
    - *“(You should go to the bed now. You take off your bag and grab the blanket. This bed is more comfortable than you thought, but maybe that's…”*


<span id="route-3"></span>

??? note "Stage 3 · stepping on a trigger on fallhaven_tavern · 1 way"

    **Way 1:** Stepping on a trigger on [Fallhaven tavern](../maps/fallhaven_tavern.md)

    - **Gives:** changes map fallhaven_tavern, changes map fallhaven_tavern, changes map fallhaven_tavern, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw, spawns monsters on fallhaven_nw
    - *“(The sun rises and you open your eyes. You feel fully rested and eager to talk with Umar. He's probably waiting for you.)”*


<span id="route-4"></span>

??? note "Stage 4 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “And what happened then?”

    - **Needs:** stage 3; not yet stage 4; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“The team leader and others loyal to him killed the rest of the team and escaped with the key, before entering the church. They have…”*


<span id="route-5"></span>

??? note "Stage 5 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “And you think the traitors are involved in that?”

    - **Needs:** stage 4; not yet stage 5; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“I'm pretty sure about it. The team leader is the one we call "Crackshot", as he is a master of murder, torture and the subjugation arts.…”*


<span id="route-10"></span>

??? note "Stage 10 · Umar · 2 ways"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “What? How I will find him then?”

    - **Needs:** stage 5; not yet stage 10; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“Probably people near the Duleian road guard tower know more. See if you can ask them for tips.”*

    **Way 2:** Talk to [Umar](../monsters/umar.md), choose “He will show up sooner or later ...”

    - **Needs:** stage 5; not yet stage 10; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - *“Maybe, but it will be faster if you question people near the Duleian road guard tower. The Duleian road is the place where we think he was…”*


<span id="route-11"></span>

??? note "Stage 11 · Benbyr · 1 way"

    **Way 1:** Talk to [Benbyr](../monsters/benbyr.md), choose “Hi. Have you heard about the murder not far from here?”

    - **Needs:** stage 10; not yet stage 11
    - *“What? A murder? I don't know what you're talking about, sorry.”*


<span id="route-15"></span>

??? note "Stage 15 · Guard · 1 way"

    **Way 1:** Talk to [Guard](../monsters/guard.md#v-crossroads_guard), choose “Sorry, have you heard anything about a murder?”

    - **Needs:** stage 10; not yet stage 15
    - *“Yeah, Feygard authorities have sent more patrols to the south. Apparently there is a group of criminals hiding in the forest”*


<span id="route-20"></span>

??? note "Stage 20 · Feygard barricade guard · 1 way"

    **Way 1:** Talk to [Feygard barricade guard](../monsters/Feygard_BG.md), choose “Anything else?”

    - **Needs:** stage 15; not yet stage 20
    - **Gives:** changes map woodcave0
    - *“Yes! Those crimin ... Wait, you don't have to know this information! Forget everything I've said!”*


<span id="route-21"></span>

??? note "Stage 21 · stepping on a trigger on woodcave0 · 1 way"

    **Way 1:** Stepping on a trigger on [Woodcave 0](../maps/woodcave0.md)

    - *“(You see a hole leading to a cave. Maybe this is a good place to start searching.)”*


<span id="route-22"></span>

??? note "Stage 22 · stepping on a trigger on crackshot_hideout1 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md)

    - **Needs:** not yet stage 22
    - *“(You look at the floor. The blood hasn't coagulated yet. It seems there has been a recent fight between two or more people.)”*


<span id="route-23"></span>

??? note "Stage 23 · stepping on a trigger on crackshot_hideout1 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md)

    - **Needs:** not yet stage 23
    - *“(More blood. There's no doubt, there has been a fight here.)”*


<span id="route-24"></span>

??? note "Stage 24 · stepping on a trigger on crackshot_hideout1 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 1](../maps/crackshot_hideout1.md)

    - **Needs:** not yet stage 24
    - *“ARGH!! *sword clashing* Sergeant! Sergeant! ... *laughter*”*


<span id="route-25"></span>

??? note "Stage 25 · Dying patrol · 1 way"

    **Way 1:** Talk to [Dying patrol](../monsters/g03_deadpatrol_1.md), automatic

    - **Needs:** not reached stage 50 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-50)


<span id="route-26"></span>

??? note "Stage 26 · Dying Patrol · 1 way"

    **Way 1:** Talk to [Dying Patrol](../monsters/g03_deadpatrol_2.md), choose “What guy?”

    - **Needs:** reached stage 40 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-40)


<span id="route-27"></span>

??? note "Stage 27 · Dying Patrol · 1 way"

    **Way 1:** Talk to [Dying Patrol](../monsters/g03_deadpatrol_2.md), choose “What guy?”

    - **Needs:** not reached stage 40 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-40)


<span id="route-28"></span>

??? note "Stage 28 · Dying patrol · 1 way"

    **Way 1:** Talk to [Dying patrol](../monsters/g03_deadpatrol_1.md), automatic



<span id="route-30"></span>

??? note "Stage 30 · Feygard patrol sergeant · 1 way"

    **Way 1:** Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md), choose “Eh ... I am ...”

    - *“Wait! That's not actually important. Leave this dangerous place, right now!”*


<span id="route-31"></span>

??? note "Stage 31 · Feygard patrol sergeant · 1 way"

    **Way 1:** Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md), choose “Unexpected?”

    - **Needs:** stage 30
    - *“Don't you understand? You must leave this place before you can't. He's playing with us!”*


<span id="route-32"></span>

??? note "Stage 32 · Feygard patrol sergeant · 1 way"

    **Way 1:** Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md), choose “Don't be rude! I'm here to help you. Please leave and go to a safer place.”

    - **Needs:** stage 31
    - **Gives:** removes monsters from crackshot_hideout3
    - *“Agh, thank you. You are valiant, kid. I hope to see you when we are both out of here. I'll invite you for a drink!”*


<span id="route-35"></span>

??? note "Stage 35 · stepping on a trigger on crackshot_hideout3 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md)

    - **Needs:** killed 1× [Crackshot](../monsters/g03_crackshot.md)


<span id="route-36"></span>

??? note "Stage 36 · walking into a blocked passage on crackshot_hideout3 · 1 way"

    **Way 1:** Walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md), choose “Insert the key of Luthor into the lock.”

    - **Needs:** not yet stage 40; not reached stage 210 of [Troubling times](../quests/troubling_times.md#stage-210); carry 1× [Key of Luthor](../items/g03_luthor.md)


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on crackshot_hideout3 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md), choose “What are you talking about?”

    - **Needs:** not yet stage 40; killed 1× [Crackshot](../monsters/g03_crackshot.md)
    - **Gives:** removes monsters from road1
    - <small>Also: clears stage 20 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-20), sets stage 30 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-30)</small>
    - *“The key is cursed .... She ... I am ... (Crackshot finally dies, emitting a soft bluish breath)”*


<span id="route-41"></span>

??? note "Stage 41 · walking into a blocked passage on crackshot_hideout3 · 1 way"

    **Way 1:** Walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md), choose “Insert the key of Luthor into the lock.”

    - **Needs:** not yet stage 36, 45; not reached stage 210 of [Troubling times](../quests/troubling_times.md#stage-210); carry 1× [Key of Luthor](../items/g03_luthor.md)


<span id="route-45"></span>

??? note "Stage 45 · Umar · 3 ways"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Oh. Yes, I remember now that I found the key. Here, take it.”

    - **Needs:** stage 40; not yet stage 45; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); hand over 1× [Key of Luthor](../items/g03_luthor.md)
    - *“Why did it take so long? And do not look at me that way. I can not tell you anything about the key for now.”*

    **Way 2:** Talk to [Umar](../monsters/umar.md), choose “Yes ... [give key]. Why is this key so important to us?”

    - **Needs:** stage 40; not yet stage 45; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); hand over 1× [Key of Luthor](../items/g03_luthor.md)
    - *“I'm sorry, but for now I can't say more.”*

    **Way 3:** Talk to [Umar](../monsters/umar.md), choose “Sure, here, take it. And maybe it's time to give me some more information.”

    - **Needs:** stage 40; not yet stage 45; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); hand over 1× [Key of Luthor](../items/g03_luthor.md)
    - *“Be patient, my friend. Everything will come in due time.”*


<span id="route-50"></span>

??? note "Stage 50 · Umar · 1 way"

    **Way 1:** Talk to [Umar](../monsters/umar.md), choose “Understood ....”

    - **Needs:** stage 45; not yet stage 50; reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
    - **Gives:** 4000× [Gold coins](../items/gold.md), 10× [Mead](../items/mead.md), faction “ThievesGuild” +20
    - *“Take 4,000 gold coins, and some bottles of my favorite mead. Now you deserve a good rest, my friend. You have earned the trust of the…”*



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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves03.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
