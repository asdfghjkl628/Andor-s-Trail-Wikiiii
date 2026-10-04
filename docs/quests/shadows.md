# Shadows

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `shadows` |
| **In journal** | Yes |
| **Stages** | 32 (completes at 20, 290) |
| **Started by** | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)), [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) |
| **NPCs involved** | [Andor](../monsters/dds_andor.md), [Borvis](../monsters/dds_borvis.md), [Dark priest](../monsters/dds_dark_priest.md), [Dark priest](../monsters/dds_dark_priest2.md), [Favlon](../monsters/dds_favlon.md), [Jolnor](../monsters/jolnor.md) +2 |
| **Locations** | [galmore_41](../maps/galmore_41.md), [galmore_45](../maps/galmore_45.md), [loneford4](../maps/loneford4.md), [nw_sullengard_1](../maps/nw_sullengard_1.md) |
| **Total XP** | 27,001 |
| **Related quests** | 7 |

</div>

## Overview

> I met Borvis on the great road near Alynndir's hut.

## Prerequisites to start

**Route 1** ([Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))):

- nothing

**Route 2** ([Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))):

- NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82)
- NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120)

**Route 3** ([Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))):

- NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120)

**Route 4** ([Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))):

- NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Darkness in the Daylight](darkness_in_daylight.md#stage-280) | stage 280 reached, for stage 290 here |
| Requires | [I have it in me](maggots.md#stage-51) | stage 51 reached, for stages 90, 100 here |
| Requires | [Trusting an outsider](vilegard.md#stage-30) | stage 30 reached, for stages 110, 120 here |
| Blocked by | [Beer Bootlegging](beer_bootlegging.md#stage-120) | stage 120 must NOT be reached, for stages 10, 20, 30 here |
| Blocked by | [Feygard errands](feygard_shipment.md#stage-82) | stage 82 must NOT be reached, for stages 10, 20, 30 here |
| Unlocks | [Search for Andor](andor.md#stage-147) | stage 147 there needs stage 260 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-3) | stage 3 there needs stage 40 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-6) | stage 6 there needs stage 240 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met Borvis on the great road near Alynndir's hut. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | removes monsters from loneford4 |
| <span id="stage-20"></span>20 | Since I had told Gandoren about the switch of the weapons, and also the truth about the bootlegging of beer from Sullengard, he told me to leave. **(completes quest)** | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | 1 XP |
| <span id="stage-30"></span>30 | Since I aided the Shadow once or twice earlier, he requested my further help for an urgent task. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-40"></span>40 | He wanted me to investigate something bad in the Purple Hills in the weird areas to the south of Stoutford. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | sets stage 3 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-3)<br>spawns monsters on galmore_45 |
| <span id="stage-50"></span>50 | I went to the area to the south of Stoutford, and encountered an impassable force there. | walking into a blocked passage on [galmore_45](../maps/galmore_45.md) | stage 40 | – |
| <span id="stage-60"></span>60 | There were strange glowing, immovable pebbles there. I had to inform Borvis. | walking into a blocked passage on [galmore_45](../maps/galmore_45.md) | stage 40, stage 50 | – |
| <span id="stage-70"></span>70 | Borvis told me that was the basic, but effective, Shadow shield, to protect Shadow incantations from outside interference.  | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | stage 60 | – |
| <span id="stage-80"></span>80 | For that, he would give me a chant. But I had to get him energies in the form of four 'blessings' - Shadow's Strength, Shadow Awareness, Fatigue, and Life Drain - within myself. He told me to go to Talion in Loneford for the first blessing, and for information about the others. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-90"></span>90 | Talion bestowed me with Shadow's Strength. | [Talion](../monsters/talion.md) | have 300 gold, pay 300 gold, stage 100 | applies condition shadowbless_str |
| <span id="stage-100"></span>100 | Talion told me to seek out Jolnor in Vilegard for the rest of the 'blessings'. | [Talion](../monsters/talion.md) | stage 90 | – |
| <span id="stage-110"></span>110 | Jolnor bestowed me with Shadow Awareness. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | have 300 gold, pay 300 gold | applies condition shadowsleep |
| <span id="stage-120"></span>120 | Jolnor told me to seek Favlon to the west of Sullengard for the remaining two. | [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) | stage 110 | spawns monsters on nw_sullengard_1 |
| <span id="stage-130"></span>130 | I reached Favlon who asked me for 10 Cooked Meat. | [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) | – | – |
| <span id="stage-140"></span>140 | I gave Favlon 10 Cooked Meat. He bestowed me with 'blessings' of Fatigue and Life Drain. | [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) | carry 10× [Cooked meat](../items/meat_cooked.md), hand over 10× [Cooked meat](../items/meat_cooked.md) | applies condition fatigue1<br>applies condition life_drain |
| <span id="stage-150"></span>150 | After a grueling travel back, I returned to Borvis. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | stage 90 | – |
| <span id="stage-160"></span>160 | Borvis removed the 'blessings' from me, and made a chant. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | applies condition shadowbless_str<br>applies condition shadowsleep<br>applies condition fatigue1<br>applies condition life_drain |
| <span id="stage-165"></span>165 | Borvis told me to hurry back to the barrier. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-170"></span>170 | I passed the barrier. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-178"></span>178 | After destroying the ritual statue of Kazaul, beyond the barrier I found a crying woman. | [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 165 | 5,000 XP |
| <span id="stage-180"></span>180 | She was performing a ritual that should bring her husband back to life. | [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 165 | spawns monsters on galmore_45 |
| <span id="stage-190"></span>190 | Borvis, who followed me, convinced the woman that it was actually an evil ritual to overrun Dhayar with Kazaul's monsters. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 165 | – |
| <span id="stage-200"></span>200 | The mourning woman told us that the ritual was given to her by a priest in the lava wastelands. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 165, stage 190 | removes monsters from galmore_45<br>spawns monsters on loneford4 |
| <span id="stage-210"></span>210 | We let the mourning woman go. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-212"></span>212 | The mourning woman cried that she would never be happy again. | [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 200 | 2,000 XP |
| <span id="stage-220"></span>220 | I had to travel to the lava wastelands. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) | stage 165, stage 200 | spawns monsters on galmore_41 |
| <span id="stage-230"></span>230 | There, after fighting monsters, I met a priest in red. | [Dark priest](../monsters/dds_dark_priest.md) ([galmore_41](../maps/galmore_41.md)) | stage 165 | – |
| <span id="stage-240"></span>240 | He accused me of interfering again and again. Borvis, who again followed me, revealed the red priest to be a monster. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md))<br>[Dark priest](../monsters/dds_dark_priest2.md) ([galmore_41](../maps/galmore_41.md)) | stage 165 | removes monsters from galmore_41<br>spawns monsters on galmore_41 |
| <span id="stage-250"></span>250 | I defeated the monster. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | stage 240 | – |
| <span id="stage-260"></span>260 | Borvis fulfilled his promise and told me that Andor would be refilling his supplies from Alynndir. | [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) | stage 240 | 15,000 XP<br>removes monsters from galmore_41<br>spawns monsters on road5<br>sets stage 6 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-6)<br>spawns monsters on road5_house |
| <span id="stage-270"></span>270 | I ran to Alynndir's hut.  | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-280"></span>280 | I found Andor there. | [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) | stage 260 | – |
| <span id="stage-290"></span>290 | He told me he couldn't come home now, and vanished. **(completes quest)** | [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) | stage 260 | 5,000 XP<br>sets stage 147 of [Search for Andor](../quests/andor.md#stage-147) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 5 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically → **stage 10**. NPC: “Hello, $playername”
    2. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120) → **stage 10**. NPC: “Begone, you Feygard lackey! I refuse to talk to you! You reek of Feygard!”
    3. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120) → **stage 10**. NPC: “You have betrayed our work by telling the truth about Beer Bootlegging from Sullengard. At least you did the right…”
    4. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82) → **stage 10**. NPC: “You have betrayed our work by providing the Feygardians with weapons. At least you did the right thing when you didn't…”
    5. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically → **stage 10**; also removes monsters from loneford4. NPC: “Shadow bless you, child!”

???+ note "Stage 20: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120) → **stage 20**. NPC: “Begone, you Feygard lackey! I refuse to talk to you! You reek of Feygard!”

???+ note "Stage 30: 4 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120) → **stage 30**. NPC: “You have betrayed our work by telling the truth about Beer Bootlegging from Sullengard. At least you did the right…”
    2. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82) → **stage 30**. NPC: “You have betrayed our work by providing the Feygardians with weapons. At least you did the right thing when you didn't…”
    3. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “And you, sir!” → **stage 30**. NPC: “A very polite kid! Plus, as the Shadow has been whispering to me, a helpful one.”
    4. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [Shadows](../quests/shadows.md#stage-30) → **stage 30**. NPC: “Listen, do you want help the Shadow?”

???+ note "Stage 40: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Shadows](../quests/shadows.md#stage-40) → **stage 40**; also sets stage 3 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-3), spawns monsters on galmore_45, spawns monsters on galmore_45. NPC: “Journey to the south of Stoutford, into the forests there. See what that Shadow priest is doing there, and stop him…”

???+ note "Stage 50: 1 route"

    1. walking into a blocked passage on [galmore_45](../maps/galmore_45.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Shadows](../quests/shadows.md#stage-40) → **stage 50**. NPC: “I have never seen such a barrier.”

???+ note "Stage 60: 1 route"

    1. walking into a blocked passage on [galmore_45](../maps/galmore_45.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Shadows](../quests/shadows.md#stage-40); reached stage 50 of [Shadows](../quests/shadows.md#stage-50); NOT reached stage 60 of [Shadows](../quests/shadows.md#stage-60); random chance (20%) → **stage 60**. NPC: “Near the shield you find some small black stones with strange markings. The stones seem to be fixed and can't be moved.”

???+ note "Stage 70: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Unfortunately the stones could not be picked up or moved - as if they had some kind of energy in them.” — **conditions:** reached stage 60 of [Shadows](../quests/shadows.md#stage-60) → **stage 70**. NPC: “That sounds like a Shadow shield! Used to protect our incantations from outside interference, like those Feygard…”

???+ note "Stage 80: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Sigh. From where?” — **conditions:** reached stage 80 of [Shadows](../quests/shadows.md#stage-80) → **stage 80**. NPC: “Go to my friend Talion in Loneford. He'll give you the blessing of Shadow's Strength.”

???+ note "Stage 90: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “If that's all - here you go.” — **conditions:** reached stage 51 of [I have it in me](../quests/maggots.md#stage-51); reached stage 100 of [Shadows](../quests/shadows.md#stage-100); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by shadowbless_str; have 300 gold; pay 300 gold → **stage 90**; also applies condition shadowbless_str. NPC: “There. I hope Borvis knows what he is doing.”

???+ note "Stage 100: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Borvis wants my help in breaking a Shadow shield in the south of Stoutford. He says someone is misusing…” — **conditions:** reached stage 51 of [I have it in me](../quests/maggots.md#stage-51); reached stage 90 of [Shadows](../quests/shadows.md#stage-90); NOT reached stage 100 of [Shadows](../quests/shadows.md#stage-100) → **stage 100**. NPC: “Very well. Go to my friend Jolnor for Shadow Sleepiness. Rest you get even in spite of bad dreams - but not…”

???+ note "Stage 110: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “[Thinking to himself] He's probably just doing this to distract me so I can't figure out how to do it.” — **conditions:** reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30); reached stage 110 of [Shadows](../quests/shadows.md#stage-110); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by shadowsleep; have 300 gold; pay 300 gold → **stage 110**; also applies condition shadowsleep. NPC: “Here you go. Take it to Borvis with care.”

???+ note "Stage 120: 1 route"

    1. Talk to [Jolnor](../monsters/jolnor.md) ([vilegard_chapel](../maps/vilegard_chapel.md)) → choose “If you say so.” — **conditions:** reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30); reached stage 110 of [Shadows](../quests/shadows.md#stage-110); NOT reached stage 120 of [Shadows](../quests/shadows.md#stage-120) → **stage 120**; also spawns monsters on nw_sullengard_1. NPC: “There's one priest, Favlon, who can give you both. However, he went researching in the area west of Sullengard and…”

???+ note "Stage 130: 1 route"

    1. Talk to [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) → choose “How many do you need?” → **stage 130**. NPC: “Ten should be enough.”

???+ note "Stage 140: 1 route"

    1. Talk to [Favlon](../monsters/dds_favlon.md) ([nw_sullengard_1](../maps/nw_sullengard_1.md)) → choose “Yes, I'm sure.” — **conditions:** reached stage 140 of [Shadows](../quests/shadows.md#stage-140); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by fatigue1; carry 10× [Cooked meat](../items/meat_cooked.md); hand over 10× [Cooked meat](../items/meat_cooked.md) → **stage 140**; also applies condition fatigue1, applies condition life_drain. NPC: “Here you go. Take them to Borvis with care.”

???+ note "Stage 150: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 90 of [Shadows](../quests/shadows.md#stage-90) → **stage 150**. NPC: “It took you a while. I thought you had given up.”

???+ note "Stage 160: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 160 of [Shadows](../quests/shadows.md#stage-160) → **stage 160**; also applies condition shadowbless_str, applies condition shadowsleep, applies condition fatigue1, applies condition life_drain. NPC: “While you slept I've prepared a tiny chant that nevertheless will destroy the Shadow shield. Here, read it.”

???+ note "Stage 165: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 165**. NPC: “Go now and destroy the shield, and then the renegade priest. Make haste!”

???+ note "Stage 178: 1 route"

    1. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → the conversation leads here automatically — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 178**. NPC: “Nooooo!”

???+ note "Stage 180: 1 route"

    1. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → choose “Do you know what you were doing?” — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 180**; also spawns monsters on galmore_45. NPC: “I was getting my husband back from the afterlife!”

???+ note "Stage 190: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Borvis? I didn't expect you already.” — **conditions:** reached stage 190 of [Shadows](../quests/shadows.md#stage-190) → **stage 190**. NPC: “Then why did the ritual not include something that links to your husband? Something precious to him?”
    2. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → choose “Borvis? I didn't expect you already.” — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 190**. NPC: “Then why did the ritual not include something that links to your husband? Something precious to him?”

???+ note "Stage 200: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Yes, who put you up to this?” — **conditions:** reached stage 190 of [Shadows](../quests/shadows.md#stage-190) → **stage 200**; also removes monsters from galmore_45, spawns monsters on loneford4. NPC: “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn…”
    2. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → choose “Yes, who put you up to this?” — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 200**; also removes monsters from galmore_45, spawns monsters on loneford4. NPC: “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn…”

???+ note "Stage 212: 1 route"

    1. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Shadows](../quests/shadows.md#stage-200) → **stage 212**. NPC: “Go away. I will never be happy in my life.”

???+ note "Stage 220: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 200 of [Shadows](../quests/shadows.md#stage-200) → **stage 220**; also spawns monsters on galmore_41. NPC: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?”
    2. Talk to [Mourning woman](../monsters/dds_mourning_woman.md) ([galmore_45](../maps/galmore_45.md)) → choose “Nice job.” — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 220**; also spawns monsters on galmore_41. NPC: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?”

???+ note "Stage 230: 1 route"

    1. Talk to [Dark priest](../monsters/dds_dark_priest.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 230**. NPC: “How dare you stop my spell?”

???+ note "Stage 240: 2 routes"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “But it's unfair to ...” — **conditions:** reached stage 240 of [Shadows](../quests/shadows.md#stage-240) → **stage 240**; also removes monsters from galmore_41, spawns monsters on galmore_41. NPC: “Are we going to do this now, or are you two going to talk all day?”
    2. Talk to [Dark priest](../monsters/dds_dark_priest2.md) ([galmore_41](../maps/galmore_41.md)) → choose “But it's unfair to ...” — **conditions:** reached stage 165 of [Shadows](../quests/shadows.md#stage-165) → **stage 240**; also removes monsters from galmore_41, spawns monsters on galmore_41. NPC: “Are we going to do this now, or are you two going to talk all day?”

???+ note "Stage 250: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 240 of [Shadows](../quests/shadows.md#stage-240); killed 1× [Dark priest](../monsters/dds_dark_priest_monster.md) → **stage 250**. NPC: “Finally. Well done, kid.”

???+ note "Stage 260: 1 route"

    1. Talk to [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) → choose “Really? Tell me!” — **conditions:** reached stage 240 of [Shadows](../quests/shadows.md#stage-240); killed 1× [Dark priest](../monsters/dds_dark_priest_monster.md) → **stage 260**; also removes monsters from galmore_41, spawns monsters on road5, sets stage 6 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-6), spawns monsters on road5_house. NPC: “Andor is going to visit Alynndir to refill his travel supplies.”

???+ note "Stage 280: 1 route"

    1. Talk to [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) → choose “Hey, Andor!” — **conditions:** reached stage 260 of [Shadows](../quests/shadows.md#stage-260) → **stage 280**

???+ note "Stage 290: 1 route"

    1. Talk to [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) → choose “Are you just going to disappear again? Please don't!” — **conditions:** reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280); reached stage 260 of [Shadows](../quests/shadows.md#stage-260) → **stage 290**; also sets stage 147 of [Search for Andor](../quests/andor.md#stage-147)


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 33 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shadows.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shadows.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shadows.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shadows.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=shadows.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `shadows` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 165, 170, 178, 180, 190, 200, 210, 212, 220, 230, 240, 250, 260, 270, 280, 290 |
    | Dialogue nodes setting stages | 10: `dds_borvis`, 10: `dds_borvis_5`, 10: `dds_borvis_7`, 20: `dds_borvis_5`, 30: `dds_borvis_7`, 30: `dds_borvis_8`, 30: `dds_borvis_20`, 40: `dds_borvis_100`, 50: `dds_dark_shadow_110`, 60: `dds_dark_shadow_120`, 70: `dds_borvis_160`, 80: `dds_borvis_210`, 90: `dds_talion_30`, 100: `dds_talion_72`, 110: `dds_jolnor_80`, 120: `dds_jolnor_120`, 130: `dds_favlon_44`, 140: `dds_favlon_60`, 150: `dds_borvis_250`, 160: `dds_borvis_280`, 165: `dds_borvis_290`, 178: `dds_mourning_woman_222`, 180: `dds_mourning_woman_240`, 190: `dds_mourning_woman_282`, 200: `dds_mourning_woman_300`, 212: `dds_mourning_woman_4`, 220: `dds_borvis_500`, 230: `dds_dark_priest_4`, 240: `dds_dark_priest2_140`, 250: `dds_borvis_550`, 260: `dds_borvis_590`, 280: `dds_andor_4`, 290: `dds_andor_54` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
