# Priceful vengeance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brightport_goons` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 136, 90, 100, 120, 140) |
| **Started by** | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) |
| **NPCs involved** | [Barthold](../monsters/brightportgoons1.md), [Gunfryk](../monsters/brightport_gunfrykstill.md), [Silvear](../monsters/brightportthieves1.md) |
| **Locations** | [brightport1](../maps/brightport1.md), [brightport_bakery](../maps/brightport_bakery.md), [brightport_benbyr](../maps/brightport_benbyr.md) |
| **Total XP** | 14,770 |
| **Related quests** | 2 |

</div>

## Overview

> Inside a house in Brightport, I met two people named Dynes and Barthold. It turned out that they are the friends Benbyr told me to visit. Rather lacking in hospitality, they offered me work.

## Prerequisites to start

Start with [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)). Required:

- NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139)
- NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130)
- reached stage 129 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-129)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-15) | stage 15 reached, for stage 40 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-30) | stage 30 reached, for stage 40 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-129) | stage 129 reached, for stage 10 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-132) | stage 132 reached, for stage 40 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-211) | stage 211 reached, for stage 120 here |
| Requires | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-240) | stage 240 reached, for stages 120, 150 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-133) | stage 133 must NOT be reached, for stage 40 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 must NOT be reached, for stage 50 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-139) | stage 139 must NOT be reached, for stages 10, 20, 30, 40, 50, 60, 80, 90, 100, 110, 120, 130, 135, 136, 140, 150 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-154) | stage 154 must NOT be reached, for stage 110 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-211) | stage 211 must NOT be reached, for stages 135, 140 here |
| Mutually exclusive | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-240) | stage 240 must NOT be reached, for stages 135, 140 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-133) | stage 133 there needs stage 30 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-135) | stage 135 there needs stage 50 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-136) | stage 136 there needs stage 50 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-137) | stage 137 there needs stage 50 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-139) | stage 139 there needs stages 30, 60, 70, 80, 130, 135 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-144) | stage 144 there needs stage 60 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-150) | stage 150 there needs stage 40 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-154) | stage 154 there needs stage 80 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-223) | stage 223 there needs stage 80 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-234) | stage 234 there needs stage 50 here |
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-240) | stage 240 there needs stages 80, 110, 130 here |
| Unlocks | [Boxed in](brightport_thieves.md#stage-30) | stage 30 there needs stages 60, 120 here |
| Unlocks | [Boxed in](brightport_thieves.md#stage-32) | stage 32 there needs stage 120 here |
| Unlocks | [Boxed in](brightport_thieves.md#stage-35) | stage 35 there needs stage 60 here |
| Unlocks | [Boxed in](brightport_thieves.md#stage-60) | stage 60 there needs stage 50 here |
| Blocks | [Boxed in](brightport_thieves.md#stage-30) | reaching stage 60 here closes stage 30 there |
| Blocks | [Boxed in](brightport_thieves.md#stage-32) | reaching stage 60 here closes stage 32 there |
| Blocks | [Boxed in](brightport_thieves.md#stage-60) | reaching stage 60 here closes stage 60 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Inside a house in Brightport, I met two people named Dynes and Barthold. It turned out that they are the friends Benbyr told me to visit. Rather lacking in hospitality, they offered me work. | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | – | – |
| <span id="stage-20"></span>20 | Barthold was hesitant because any job I could do for them would put me at odds with Gunfryk the guard commander. Taking that into account I offered to rid them of him. | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | – | – |
| <span id="stage-30"></span>30 | I was told not to kill him, but surely it won't be a problem if I do. Either way I'll resolve things for them. | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I received some records from silvear that could be useful as blackmail against Gunfryk. | [Silvear](../monsters/brightportthieves1.md) ([brightport1](../maps/brightport1.md)) | pay 1,000 gold, stage 30 | – |
| <span id="stage-50"></span>50 | I lied to the commander that there are some lizardmen in the derelict house east of town, I should go there and prepare an ambush.  | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | – | removes monsters from brightport_bakery<br>sets stage 234 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-234) |
| <span id="stage-60"></span>60 | I used the records to blackmail Gunfryk. To save his reputation he begrudgingly agreed to give Barthold and Dynes some leeway. | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | stage 40 | – |
| <span id="stage-70"></span>70 | I ambushed and killed Gunfryk in the house to the east, along with the two guards he brought.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brightport abandoned](../maps/brightport_abandoned.md).</span> | stepping on a trigger on [brightport_abandoned](../maps/brightport_abandoned.md) | – | starts timer “brightport_new”<br>clears stage 234 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-234) |
| <span id="stage-80"></span>80 | I informed the commander about Barthold and Dynes' scheme. He requested that I find some incriminating evidence of their role.  | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | stage 30 | – |
| <span id="stage-90"></span>90 | Barthold was happy with my work and gave me a reward, he said I could find more work like this in Nor City.  **(completes quest)** | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | stage 30, stage 60 | 4,420 XP<br>gives 1200× [Gold coins](../items/gold.md)<br>sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139) |
| <span id="stage-100"></span>100 | Barthold was a little disappointed about me killing Gunfryk. It's possible that now Feygard might take more severe action with Brightport. **(completes quest)** | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | stage 30, stage 70 | 6,950 XP<br>gives 1000× [Gold coins](../items/gold.md)<br>sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139) |
| <span id="stage-110"></span>110 | I found some of the duo's merchandise in the smuggling cave east of brightport.  | walking into a blocked passage on [brightport_smugglercave1](../maps/brightport_smugglercave1.md) | stage 80 | sets stage 154 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-154)<br>gives 1× [Nor city made blade](../items/brightport_sword0.md) |
| <span id="stage-119"></span>119 | I gave the commander the blade, even though I already got paid not to. If there's any honor among Nor City's thieves, they will surely have none to spare for me. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-120"></span>120 | Gunfryk was happy with my work, the duo will soon be jailed. He said Feygard needs more brave youngsters like me and that I should give the military academy a try. **(completes quest)** | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | – | 3,400 XP<br>sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139)<br>spawns monsters on brightport_benbyr<br>starts timer “brightport_arrest”<br>sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212)<br>gives 700× [Gold coins](../items/gold.md) |
| <span id="stage-130"></span>130 | I opted to blackmail the duo instead for some quick gold. Should've had the Guild's protection, suckers! | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | carry 1× [Nor city made blade](../items/brightport_sword0.md), stage 110, stage 30 | gives 1869× [Gold coins](../items/gold.md) |
| <span id="stage-135"></span>135 | I told the commander I couldn't find anything | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | stage 110, stage 80 | – |
| <span id="stage-136"></span>136 | Barthold was disappointed in me for having done nothing about Gunfryk. Little did he know I lined my pockets with his merchandise. **(completes quest)** | [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) | stage 135, stage 30 | sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139) |
| <span id="stage-140"></span>140 | I told the commander I couldn't find anything, even though I had the blade I blackmailed Barthold and Dynes with. **(completes quest)** | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | stage 130, stage 80 | sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139) |
| <span id="stage-150"></span>150 |  | [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) | – | sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139)<br>spawns monsters on brightport_benbyr<br>starts timer “brightport_arrest”<br>sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → choose “Benbyr said to come and see you.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 129 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-129) → **stage 10**. NPC: “Benbyr did? Ha! I guess that guy's still up for business! Say, you want to work for us?”

???+ note "Stage 20: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 20 of [Priceful vengeance](../quests/brightport_goons.md#stage-20); NOT reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30) → **stage 20**. NPC: “That's a dangerous thing you're saying, there is no way you can do that. He's not exactly a sheep; Gunfryk is a…”

???+ note "Stage 30: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 20 of [Priceful vengeance](../quests/brightport_goons.md#stage-20); NOT reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30) → **stage 30**. NPC: “Dang it, Dynes, don't egg on the kid. Killing is off the list, understood? Just make him less of a problem for us.”

???+ note "Stage 40: 1 route"

    1. Talk to [Silvear](../monsters/brightportthieves1.md) ([brightport1](../maps/brightport1.md)) → choose “Is this convincing enough? [Offer 1,000 gold.]” — **conditions:** reached stage 15 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-15); reached stage 30 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-30); reached stage 132 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-132); NOT reached stage 40 of [Priceful vengeance](../quests/brightport_goons.md#stage-40); NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); NOT reached stage 133 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-133); pay 1,000 gold → **stage 40**. NPC: “When he arrived here and some of my acquaintances were sent to the Feygard prisons, I had to collect some information…”

???+ note "Stage 50: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); NOT reached stage 135 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-135) → **stage 50**; also removes monsters from brightport_bakery, sets stage 234 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-234). NPC: “Lizardman you say? That is extremely serious. I will call my men and we will hurry to save him!”

???+ note "Stage 60: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “You've put my two acquaintances, Dynes and Barthold, in a tough spot with your rules. I'd appreciate it if…” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 40 of [Priceful vengeance](../quests/brightport_goons.md#stage-40); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135) → **stage 60**. NPC: “Have it your way, and keep those papers away from my subordinates. If word got out, my reputation would be ruined! But…”

???+ note "Stage 70: 1 route"

    1. stepping on a trigger on [brightport_abandoned](../maps/brightport_abandoned.md) → the conversation leads here automatically — **conditions:** killed 1× [Gunfryk](../monsters/brightportguardcaptain.md); killed 2× [Brightport guard](../monsters/brightport_guardfight.md); NOT reached stage 70 of [Priceful vengeance](../quests/brightport_goons.md#stage-70) → **stage 70**; also starts timer “brightport_new”, clears stage 234 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-234). NPC: “Phew. Job well done!”

???+ note "Stage 80: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “I think I heard them mention a smuggling cave of sorts, that they use to evade the law.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); NOT reached stage 50 of [Priceful vengeance](../quests/brightport_goons.md#stage-50); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135) → **stage 80**. NPC: “If you came here to tell me, there may be some truth to your words, kid. If you want to do the right thing for the…”

???+ note "Stage 90: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → choose “Good news. The commander's going to be turning a blind eye to your deals for a while. [Show him the…” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60) → **stage 90**; also gives 1200× [Gold coins](../items/gold.md), sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139). NPC: “And for a job well done here is your reward; rather generous I say. You'll surely find more work to do in Nor City,…”

???+ note "Stage 100: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → choose “It was a hard fight, but I killed him, They'll probably think a lizardman got him.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); reached stage 70 of [Priceful vengeance](../quests/brightport_goons.md#stage-70) → **stage 100**; also gives 1000× [Gold coins](../items/gold.md), sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139). NPC: “Anyway, here's your reward. With skills like yours, you'll surely find more work to do for our friends in Nor City.”

???+ note "Stage 110: 1 route"

    1. walking into a blocked passage on [brightport_smugglercave1](../maps/brightport_smugglercave1.md) → choose “Meh, no one will notice. [Smash it open.]” — **conditions:** NOT reached stage 154 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-154); reached stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80); NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139) → **stage 110**; also sets stage 154 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-154), gives 1× [Nor city made blade](../items/brightport_sword0.md). NPC: “After smashing the lid open with a rock, you see a dozen unsharpened blades, even at first glance the material they're…”

???+ note "Stage 120: 2 routes"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “[I do feel a little bad.]” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240) → **stage 120**; also sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139), spawns monsters on brightport_benbyr, starts timer “brightport_arrest”, sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212). NPC: “We sure need more brave, law-upholding youngsters like you around! I'll make sure to write to my superiors about it.…”
    2. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “Barthold and Dynes sir.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211) → **stage 120**; also gives 700× [Gold coins](../items/gold.md), spawns monsters on brightport_benbyr, sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139), sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212), starts timer “brightport_arrest”. NPC: “We sure need more brave, law-upholding youngsters like you around! I'll make sure to write to my superiors about it.…”

???+ note "Stage 130: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → choose “You don't have the Guild's protection. Either I give this blade I took from your hideout to the guards. Or…” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); carry 1× [Nor city made blade](../items/brightport_sword0.md); reached stage 110 of [Priceful vengeance](../quests/brightport_goons.md#stage-110); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135) → **stage 130**; also gives 1869× [Gold coins](../items/gold.md). NPC: “Dynes begrudgingly takes out a bag of gold and throws it your way.”

???+ note "Stage 135: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “Sorry, I couldn't find anything.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); NOT reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240); NOT reached stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135); reached stage 110 of [Priceful vengeance](../quests/brightport_goons.md#stage-110); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); NOT carry 1× [Nor city made blade](../items/brightport_sword0.md) → **stage 135**. NPC: “This time was a miss, but we sure need more brave youngsters like you who are not afraid to speak up. Glory to Feygard!”

???+ note "Stage 136: 1 route"

    1. Talk to [Barthold](../monsters/brightportgoons1.md) ([brightport_benbyr](../maps/brightport_benbyr.md)) → choose “I tried so hard, and got so far. But in the end, I couldn't find anything.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130); reached stage 30 of [Priceful vengeance](../quests/brightport_goons.md#stage-30); reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135) → **stage 136**; also sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139). NPC: “Is that so? I'm a little disappointed, thought you're more than just a sheep butcher.”

???+ note "Stage 140: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “Sorry, I couldn't find anything.” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 80 of [Priceful vengeance](../quests/brightport_goons.md#stage-80); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); NOT reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240); NOT reached stage 211 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-211); NOT reached stage 135 of [Priceful vengeance](../quests/brightport_goons.md#stage-135); reached stage 130 of [Priceful vengeance](../quests/brightport_goons.md#stage-130) → **stage 140**; also sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139). NPC: “This time was a miss, but we sure need more brave youngsters like you who are not afraid to speak up. Glory to Feygard!”

???+ note "Stage 150: 1 route"

    1. Talk to [Gunfryk](../monsters/brightport_gunfrykstill.md) ([brightport_bakery](../maps/brightport_bakery.md)) → choose “[I do feel a little bad.]” — **conditions:** NOT reached stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); reached stage 240 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-240) → **stage 150**; also sets stage 139 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-139), spawns monsters on brightport_benbyr, starts timer “brightport_arrest”, sets stage 212 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-212). NPC: “We sure need more brave, law-upholding youngsters like you around! I'll make sure to write to my superiors about it.…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 17 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_goons.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_goons.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_goons.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_goons.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brightport_goons.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brightport_goons` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 119, 120, 130, 135, 136, 140, 150 |
    | Dialogue nodes setting stages | 10: `brightport_goons8`, 20: `brightport_goons21`, 30: `brightport_goons23`, 40: `brightport_silvear_gunfryk`, 50: `brightport_gunfryk2`, 60: `brightport_gunfryk5`, 70: `brightport_gunfrykdead_check2`, 80: `brightport_gunfryk8`, 90: `brightport_goons32`, 100: `brightport_goons29`, 110: `brightport_smuggler_selector4`, 120: `brightport_gunfryk19`, 120: `brightport_gunfryk13`, 130: `brightport_goons35`, 135: `brightport_gunfryk22`, 136: `brightport_barthold1`, 140: `brightport_gunfryk15`, 150: `brightport_gunfryk19` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
