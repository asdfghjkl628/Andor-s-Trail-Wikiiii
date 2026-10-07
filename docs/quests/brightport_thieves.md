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
| **Started by** | [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) |
| **NPCs involved** | [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate), [Elysa](../monsters/brightportthieves6.md), [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill), [Nor agent](../monsters/brightport_agent.md) |
| **Locations** | [brightport_abandoned](../maps/brightport_abandoned.md), [brightport_bakery](../maps/brightport_bakery.md), [brightport_jail](../maps/brightport_jail.md), [brightport_thieves](../maps/brightport_thieves.md) |
| **Total XP** | 5,000 |
| **Related quests** | 2 |

</div>

## Overview

> The Thieves Guild was due to receive a package, but the guards in Brightport have been impeding their activities. They need a new face like me to pick the package up discretly. I was told to head east of the town.

## Prerequisites to start

Start with [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)). Required:

- reached stage 130 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-130)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Priceful vengeance](brightport_goons.md#stage-50) | stage 50 reached, for stage 60 here |
| Requires | [Priceful vengeance](brightport_goons.md#stage-60) | stage 60 reached, for stages 30, 35 here |
| Requires | [Priceful vengeance](brightport_goons.md#stage-120) | stage 120 reached, for stages 30, 32 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-130) | stage 130 reached, for stage 10 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 reached, for stage 60 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-148) | stage 148 reached, for stage 40 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-149) | stage 149 reached, for stage 45 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-220) | stage 220 reached, for stage 70 here |
| Blocked by | [Priceful vengeance](brightport_goons.md#stage-60) | stage 60 must NOT be reached, for stages 30, 32, 60 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-136) | stage 136 must NOT be reached, for stage 60 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-139) | stage 139 must NOT be reached, for stage 60 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-144) | stage 144 must NOT be reached, for stages 40, 45 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 there needs stage 10 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-137) | stage 137 there needs stages 10, 32 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-141) | stage 141 there needs stage 30 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-142) | stage 142 there needs stage 30 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-143) | stage 143 there needs stage 30 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-144) | stage 144 there needs stages 32, 40 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-159) | stage 159 there needs stage 32 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-196) | stage 196 there needs stages 20, 32, 40 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-208) | stage 208 there needs stage 30 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-220) | stage 220 there needs stage 32 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-256) | stage 256 there needs stages 20, 32 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | The Thieves Guild was due to receive a package, but the guards in Brightport have been impeding their activities. They need a new face like me to pick the package up discretly. I was told to head east of the town.<br><span class="qnote">⚡ A scripted event can now trigger on [Brightport8](../maps/brightport8.md).</span> | [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) | – | – |
| <span id="stage-20"></span>20 | I met the courier from Nor City inside the house. | [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) | – | – |
| <span id="stage-30"></span>30 | Before we could conclude the meeting we heard the town guard making noise outside. | [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) | – | – |
| <span id="stage-32"></span>32 | I received the package. | [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) | stage 30 | gives 1× [Package](../items/brightportpackage.md)<br>removes monsters from brightport_abandoned<br>starts timer “brightporthide”<br>sets stage 208 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-208) |
| <span id="stage-35"></span>35 | Thanks to some previous interactions I've had with the commander, I convinced the guards to let me go. | [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate) ([brightport_abandoned](../maps/brightport_abandoned.md)) | – | removes monsters from brightport_abandoned<br>sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144)<br>clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158) |
| <span id="stage-40"></span>40 | I couldn't fool the guards and got caught.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate1](../maps/brightport_crate1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate2](../maps/brightport_crate2.md).</span> | stepping on a trigger on [brightport_crate1](../maps/brightport_crate1.md)<br>stepping on a trigger on [brightport_crate2](../maps/brightport_crate2.md) | hand over 1× [Package](../items/brightportpackage.md), stage 32 | – |
| <span id="stage-45"></span>45 | I managed to hide inside a crate and waited. Eventually, the guards left. <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate1](../maps/brightport_crate1.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport crate2](../maps/brightport_crate2.md).</span> | stepping on a trigger on [brightport_crate1](../maps/brightport_crate1.md)<br>stepping on a trigger on [brightport_crate2](../maps/brightport_crate2.md) | – | sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144)<br>clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158) |
| <span id="stage-50"></span>50 | I delivered the package to Elysa, She was pleased with my work and said the Thieves Guild may have further opportunities for me in the future. **(completes quest)** | [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) | hand over 1× [Package](../items/brightportpackage.md), stage 20, stage 32 | 3,000 XP<br>sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196) |
| <span id="stage-60"></span>60 | I lied to Gunfryk in a plot to kill him, and in the process the courier I was supposed to meet got arrested. **(completes quest)** | [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill) ([brightport_bakery](../maps/brightport_bakery.md)) | – | sets stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136)<br>gives 1× [Agent's cloak](../items/brightport_cloak.md) |
| <span id="stage-70"></span>70 | I failed to deliver the package to Elysa. She was not happy. **(completes quest)** | [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) | stage 20, stage 32, stage 40 | 2,000 XP<br>sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) → choose “I don't have time, can't we get on with it already?” — **conditions:** reached stage 130 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-130) → **stage 10**. NPC: “We need you to pick up a package from the mediator of one of our clients. We've received word that he'll be waiting in…”

???+ note "Stage 20: 2 routes"

    1. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** 10 rounds passed since timer “Brightport_package” → **stage 20**. NPC: “You took your time.”
    2. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** NOT 10 rounds passed since timer “Brightport_package” → **stage 20**. NPC: “That was a quick arrival.”

???+ note "Stage 30: 3 routes"

    1. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30); reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60) → **stage 30**. NPC: “That is my partner on the lookout, the signal means the guards are coming.”
    2. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60) → **stage 30**. NPC: “That is my partner on the lookout, the signal means the guards are coming.”
    3. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30) → **stage 30**. NPC: “That is my partner on the lookout, the signal means the guards are coming.”

???+ note "Stage 32: 2 routes"

    1. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → choose “I'll be fine, I'm in good standing with the guards.” — **conditions:** reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30) → **stage 32**; also gives 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned, starts timer “brightporthide”. NPC: “Then take the package and deliver it, I will escape through the chimney. Shadow be with you.”
    2. Talk to [Nor agent](../monsters/brightport_agent.md) ([brightport_abandoned](../maps/brightport_abandoned.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); random chance (30%) → **stage 32**; also gives 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned, starts timer “brightporthide”, sets stage 208 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-208). NPC: “Take this package and hide somewhere before the guards get here, I will escape through the chimney. Shadow be with you.”

???+ note "Stage 35: 1 route"

    1. Talk to [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate) ([brightport_abandoned](../maps/brightport_abandoned.md)) → choose “Think about it twice. You try and arrest me, and by tomorrow morning you might find yourself discharged, or…” — **conditions:** reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); random chance (100%) → **stage 35**; also removes monsters from brightport_abandoned, sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158). NPC: “The two guards exchange a glance, then turn and leave the building.”

???+ note "Stage 40: 2 routes"

    1. stepping on a trigger on [brightport_crate1](../maps/brightport_crate1.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); NOT reached stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144) → **stage 40**. NPC: “Let me see. [The guard takes the package out of your hands.]”
    2. stepping on a trigger on [brightport_crate2](../maps/brightport_crate2.md) → choose “I found it inside the crate.” — **conditions:** NOT reached stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; reached stage 148 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-148); reached stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32); hand over 1× [Package](../items/brightportpackage.md) → **stage 40**. NPC: “Let me see. [The guard takes the package out of your hands.]”

???+ note "Stage 45: 2 routes"

    1. stepping on a trigger on [brightport_crate1](../maps/brightport_crate1.md) → choose “[Uh oh.]” — **conditions:** NOT reached stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; NOT reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); reached stage 149 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-149) → **stage 45**; also sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158). NPC: “After what seems like a minute the footsteps move away, you hear the guards discuss something then silence.”
    2. stepping on a trigger on [brightport_crate2](../maps/brightport_crate2.md) → choose “[Uh oh.]” — **conditions:** NOT reached stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144); 3 rounds passed since timer “brightporthide”; reached stage 149 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-149) → **stage 45**; also sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158). NPC: “After what seems like a minute the footsteps move away, you hear the guards discuss something then silence.”

???+ note "Stage 50: 1 route"

    1. Talk to [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) → choose “Here it is.” — **conditions:** reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20); NOT reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); reached stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32); hand over 1× [Package](../items/brightportpackage.md) → **stage 50**; also sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196). NPC: “Very good work, $playername. I heard the guards went on patrol while you were there, and you skillfully avoided them.…”

???+ note "Stage 60: 1 route"

    1. Talk to [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “Umm. Ermm. He is alright sir.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); reached stage 135 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-135); NOT reached stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136) → **stage 60**; also sets stage 136 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-136), gives 1× [Agent's cloak](../items/brightport_cloak.md). NPC: “Then that is good, and if not for you we wouldn't have gone there and found that spy. You can have his cloak, well done.”

???+ note "Stage 70: 3 routes"

    1. Talk to [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20); reached stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220) → **stage 70**; also sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196). NPC: “You don't have to tell me, I know $playername, you got caught and they took the package. We don't have much left to…”
    2. Talk to [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) → choose “Yes. [Tell her what happened.]” — **conditions:** reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20); reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); NOT carry 1× [Package](../items/brightportpackage.md) → **stage 70**; also sets stage 196 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-196). NPC: “And now, let's talk about you, $playername. I'm a bit disheartened that you got caught, but I'm still willing to tell…”
    3. Talk to [Elysa](../monsters/brightportthieves6.md) ([brightport_thieves](../maps/brightport_thieves.md)) → choose “It's lost, and I can't find it.” — **conditions:** reached stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20); NOT reached stage 40 of [Boxed in](../quests/brightport_thieves.md#stage-40); reached stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32); NOT carry 1× [Package](../items/brightportpackage.md) → **stage 70**. NPC: “You lost it? Sigh. I had higher expectations of you, my mood is soured. I'll still tell you about Andor, but only for…”


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
