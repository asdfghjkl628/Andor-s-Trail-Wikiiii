---
description: "Boxed in is a quest in Andor's Trail, started by Elysa (brightport_thieves). 10 stages, 5,000 XP in total. The Thieves Guild was due to receive a package, but the guards in Brightport have been impeding their activities. They need a new face like me to pick the package up discretly. I was told to…"
---

# Boxed in

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brightport_thieves` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 50, 60, 70) |
| **Started by** | [Elysa](../monsters/brightportthieves6.md) ([Brightport thieves](../maps/brightport_thieves.md)) |
| **NPCs involved** | [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate), [Elysa](../monsters/brightportthieves6.md), [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill), [Nor agent](../monsters/brightport_agent.md) |
| **Locations** | [Brightport abandoned](../maps/brightport_abandoned.md), [Brightport bakery](../maps/brightport_bakery.md), [Brightport jail](../maps/brightport_jail.md), [Brightport thieves](../maps/brightport_thieves.md) |
| **Total XP** | 5,000 |
| **Related quests** | 2 |

</div>

## Overview

> The Thieves Guild was due to receive a package, but the guards in Brightport have been impeding their activities. They need a new face like me to pick the package up discretly. I was told to head east of the town.

## Prerequisites to start

Start with [Elysa](../monsters/brightportthieves6.md) ([Brightport thieves](../maps/brightport_thieves.md)). Required:

- reached stage 130 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-130)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Priceful vengeance](brightport_goons.md#stage-50) | stage 50 reached, for stage 60 here |
| Requires | [Priceful vengeance](brightport_goons.md#stage-60) | stage 60 reached, for stages 30, 35 here |
| Requires | [Priceful vengeance](brightport_goons.md#stage-120) | stage 120 reached, for stages 30, 32 here |
| Requires | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-130) | stage 130 reached, for stage 10 here |
| Requires | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 reached, for stage 60 here |
| Requires | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-148) | stage 148 reached, for stage 40 here |
| Requires | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-149) | stage 149 reached, for stage 45 here |
| Requires | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-220) | stage 220 reached, for stage 70 here |
| Blocked by | [Priceful vengeance](brightport_goons.md#stage-60) | stage 60 must NOT be reached, for stages 30, 32, 60 here |
| Mutually exclusive | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-136) | stage 136 must NOT be reached, for stage 60 here |
| Mutually exclusive | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-139) | stage 139 must NOT be reached, for stage 60 here |
| Mutually exclusive | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-144) | stage 144 must NOT be reached, for stages 40, 45 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 there needs stage 10 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-137) | stage 137 there needs stages 10, 32 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-141) | stage 141 there needs stage 30 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-142) | stage 142 there needs stage 30 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-143) | stage 143 there needs stage 30 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-144) | stage 144 there needs stages 32, 40 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-159) | stage 159 there needs stage 32 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-196) | stage 196 there needs stages 20, 32, 40 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-208) | stage 208 there needs stage 30 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-220) | stage 220 there needs stage 32 here |
| Unlocks | [Brightport story flags (hidden flag)](brightport_nondisplay.md#stage-256) | stage 256 there needs stages 20, 32 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">The Thieves Guild was due to receive a package, but the guards in… ▸</span><span class="l">▴ less</span></summary>The Thieves Guild was due to receive a package, but the guards in Brightport have been impeding their activities. They need a new face like me to pick the package up discretly. I was told to head east of the town.</details><br><span class="qnote">⚡ A scripted event can now trigger on [Brightport 8](../maps/brightport8.md).</span> | [Elysa](../monsters/brightportthieves6.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I met the courier from Nor City inside the house. | [Nor agent](../monsters/brightport_agent.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Before we could conclude the meeting we heard the town guard making… ▸</span><span class="l">▴ less</span></summary>Before we could conclude the meeting we heard the town guard making noise outside.</details> | [Nor agent](../monsters/brightport_agent.md) | – |
| <span id="stage-32"></span>[32](#route-32) | I received the package. | [Nor agent](../monsters/brightport_agent.md) | 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned |
| <span id="stage-35"></span>[35](#route-35) | <details class="jt"><summary><span class="s">Thanks to some previous interactions I've had with the commander, I… ▸</span><span class="l">▴ less</span></summary>Thanks to some previous interactions I've had with the commander, I convinced the guards to let me go.</details> | [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate) | removes monsters from brightport_abandoned |
| <span id="stage-40"></span>[40](#route-40) | I couldn't fool the guards and got caught.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate 1](../maps/brightport_crate1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate 2](../maps/brightport_crate2.md).</span> | stepping on a trigger on [Brightport crate 1](../maps/brightport_crate1.md), stepping on a trigger on [Brightport crate 2](../maps/brightport_crate2.md) | – |
| <span id="stage-45"></span>[45](#route-45) | I managed to hide inside a crate and waited. Eventually, the guards left.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate 1](../maps/brightport_crate1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate 2](../maps/brightport_crate2.md).</span> | stepping on a trigger on [Brightport crate 1](../maps/brightport_crate1.md), stepping on a trigger on [Brightport crate 2](../maps/brightport_crate2.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I delivered the package to Elysa, She was pleased with my work and… ▸</span><span class="l">▴ less</span></summary>I delivered the package to Elysa, She was pleased with my work and said the Thieves Guild may have further opportunities for me in the future.</details> **(ends quest)** | [Elysa](../monsters/brightportthieves6.md) | 3,000 XP |
| <span id="stage-60"></span>[60](#route-60) | <details class="jt"><summary><span class="s">I lied to Gunfryk in a plot to kill him, and in the process the… ▸</span><span class="l">▴ less</span></summary>I lied to Gunfryk in a plot to kill him, and in the process the courier I was supposed to meet got arrested.</details> **(ends quest)** | [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill) | 1× [Agent's cloak](../items/brightport_cloak.md) |
| <span id="stage-70"></span>[70](#route-70) | I failed to deliver the package to Elysa. She was not happy. **(ends quest)** | [Elysa](../monsters/brightportthieves6.md) | 2,000 XP |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Elysa · 1 way"

    **Way 1:** Talk to [Elysa](../monsters/brightportthieves6.md), choose “I don't have time, can't we get on with it already?”

    - **Needs:** reached stage 130 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-130)
    - *“We need you to pick up a package from the mediator of one of our clients. We've received word that he'll be waiting in the old building…”*


<span id="route-20"></span>

??? note "Stage 20 · Nor agent · 2 ways"

    **Way 1:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** 10 rounds passed since timer “Brightport_package”
    - *“You took your time.”*

    **Way 2:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** not 10 rounds passed since timer “Brightport_package”
    - *“That was a quick arrival.”*


<span id="route-30"></span>

??? note "Stage 30 · Nor agent · 3 ways"

    **Way 1:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** stage 30; reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60)
    - *“That is my partner on the lookout, the signal means the guards are coming.”*

    **Way 2:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** stage 30; not reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60)
    - *“That is my partner on the lookout, the signal means the guards are coming.”*

    **Way 3:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** stage 30; reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120)
    - *“That is my partner on the lookout, the signal means the guards are coming.”*


<span id="route-32"></span>

??? note "Stage 32 · Nor agent · 2 ways"

    **Way 1:** Talk to [Nor agent](../monsters/brightport_agent.md), choose “I'll be fine, I'm in good standing with the guards.”

    - **Needs:** stage 30; reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120)
    - **Gives:** 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned
    - <small>Also: starts timer “brightporthide”</small>
    - *“Then take the package and deliver it, I will escape through the chimney. Shadow be with you.”*

    **Way 2:** Talk to [Nor agent](../monsters/brightport_agent.md), automatic

    - **Needs:** stage 30; not reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); random chance (30%)
    - **Gives:** 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned
    - <small>Also: starts timer “brightporthide”, sets stage 208 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-208)</small>
    - *“Take this package and hide somewhere before the guards get here, I will escape through the chimney. Shadow be with you.”*


<span id="route-35"></span>

??? note "Stage 35 · Brightport guard · 1 way"

    **Way 1:** Talk to [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate), choose “Think about it twice. You try and arrest me, and by tomorrow morning you might find yourself discharged, or…”

    - **Needs:** reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); random chance (100%)
    - **Gives:** removes monsters from brightport_abandoned
    - <small>Also: sets stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-158)</small>
    - *“The two guards exchange a glance, then turn and leave the building.”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on brightport_crate1, stepping on a tr · 2 ways"

    **Way 1:** Stepping on a trigger on [Brightport crate 1](../maps/brightport_crate1.md)

    - **Needs:** stage 40; not reached stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144)
    - *“Let me see. [The guard takes the package out of your hands.]”*

    **Way 2:** Stepping on a trigger on [Brightport crate 2](../maps/brightport_crate2.md), choose “I found it inside the crate.”

    - **Needs:** stage 32; not reached stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; reached stage 148 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-148); hand over 1× [Package](../items/brightportpackage.md)
    - *“Let me see. [The guard takes the package out of your hands.]”*


<span id="route-45"></span>

??? note "Stage 45 · stepping on a trigger on brightport_crate1, stepping on a tr · 2 ways"

    **Way 1:** Stepping on a trigger on [Brightport crate 1](../maps/brightport_crate1.md), choose “[Uh oh.]”

    - **Needs:** not yet stage 40; not reached stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; reached stage 149 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-149)
    - <small>Also: sets stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-158)</small>
    - *“After what seems like a minute the footsteps move away, you hear the guards discuss something then silence.”*

    **Way 2:** Stepping on a trigger on [Brightport crate 2](../maps/brightport_crate2.md), choose “[Uh oh.]”

    - **Needs:** not reached stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; reached stage 149 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-149)
    - <small>Also: sets stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-158)</small>
    - *“After what seems like a minute the footsteps move away, you hear the guards discuss something then silence.”*


<span id="route-50"></span>

??? note "Stage 50 · Elysa · 1 way"

    **Way 1:** Talk to [Elysa](../monsters/brightportthieves6.md), choose “Here it is.”

    - **Needs:** stage 20, 32; not yet stage 40; hand over 1× [Package](../items/brightportpackage.md)
    - <small>Also: sets stage 196 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-196)</small>
    - *“Very good work, $playername. I heard the guards went on patrol while you were there, and you skillfully avoided them. The Guild would very…”*


<span id="route-60"></span>

??? note "Stage 60 · Gunfryk · 1 way"

    **Way 1:** Talk to [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill), choose “Umm. Ermm. He is alright sir.”

    - **Needs:** not reached stage 139 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-139); not reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); reached stage 135 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-135); not reached stage 136 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-136)
    - **Gives:** 1× [Agent's cloak](../items/brightport_cloak.md)
    - <small>Also: sets stage 136 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-136)</small>
    - *“Then that is good, and if not for you we wouldn't have gone there and found that spy. You can have his cloak, well done.”*


<span id="route-70"></span>

??? note "Stage 70 · Elysa · 3 ways"

    **Way 1:** Talk to [Elysa](../monsters/brightportthieves6.md), automatic

    - **Needs:** stage 20; reached stage 220 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-220)
    - <small>Also: sets stage 196 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-196)</small>
    - *“You don't have to tell me, I know $playername, you got caught and they took the package. We don't have much left to discuss. I will still…”*

    **Way 2:** Talk to [Elysa](../monsters/brightportthieves6.md), choose “Yes. [Tell her what happened.]”

    - **Needs:** stage 20, 40; not carry 1× [Package](../items/brightportpackage.md)
    - <small>Also: sets stage 196 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-196)</small>
    - *“And now, let's talk about you, $playername. I'm a bit disheartened that you got caught, but I'm still willing to tell you what I know of…”*

    **Way 3:** Talk to [Elysa](../monsters/brightportthieves6.md), choose “It's lost, and I can't find it.”

    - **Needs:** stage 20, 32; not yet stage 40; not carry 1× [Package](../items/brightportpackage.md)
    - *“You lost it? Sigh. I had higher expectations of you, my mood is soured. I'll still tell you about Andor, but only for some gold.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 16 lines added |
| [v0.8.18](../versions/0.8.18.md) | Stage 10 journal text changed<br>Stage 50 journal text changed<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_thieves.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_thieves.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_thieves.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_thieves.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_thieves.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brightport_thieves` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 32, 35, 40, 45, 50, 60, 70 |
    | Dialogue nodes setting stages | 10: `brightport_elysa3`, 20: `brightport_agent2`, 20: `brightport_agent1`, 30: `brightport_agent6_alt`, 30: `brightport_agent6`, 30: `brightport_agent6alt`, 32: `brightport_agent8`, 32: `brightport_agent7`, 35: `brightport_crateguard6`, 40: `brightport_crate_failure15`, 45: `brightport_crate_success`, 50: `brightport_elysa13`, 60: `brightport_gunfryk_killfail2`, 70: `brightport_elysa_jail`, 70: `brightport_elysa_caught3`, 70: `brightport_elysa_failsafe` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
