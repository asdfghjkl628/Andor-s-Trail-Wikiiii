---
description: "Darkness in the Daylight is a quest in Andor's Trail, started by Miri (galmore_41). 32 stages, 27,002 XP in total. I met Miri in the Crossroads Guardhouse."
---

# Darkness in the Daylight

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `darkness_in_daylight` |
| **In journal** | Yes |
| **Stages** | 32 (completes at 20, 30, 310) |
| **Started by** | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) |
| **NPCs involved** | [Andor](../monsters/dds_andor.md), [Dark priest](../monsters/dds_dark_priest.md), [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2), [Miri](../monsters/dds_miri.md), [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman), [Old hermit](../monsters/dds_oldhermit.md) +2 |
| **Locations** | [blackwater_mountain50](../maps/blackwater_mountain50.md), [fallhaven_nw](../maps/fallhaven_nw.md), [galmore_41](../maps/galmore_41.md), [galmore_45](../maps/galmore_45.md) |
| **Total XP** | 27,002 |
| **Related quests** | 5 |

</div>

## Overview

> I met Miri in the Crossroads Guardhouse.

## Prerequisites to start

None: talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Beer Bootlegging](beer_bootlegging.md#stage-120) | stage 120 reached, for stage 30 here |
| Requires | [Feygard errands](feygard_shipment.md#stage-82) | stage 82 reached, for stage 20 here |
| Unlocks | [Search for Andor](andor.md#stage-145) | stage 145 there needs stage 280 here |
| Unlocks | [Search for Andor](andor.md#stage-147) | stage 147 there needs stage 280 here |
| Unlocks | [Search for Andor](andor.md#stage-999) | stage 999 there needs stage 280 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-2) | stage 2 there needs stage 150 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-3) | stage 3 there needs stage 50 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-6) | stage 6 there needs stage 260 here |
| Unlocks | [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](dds_nd.md#stage-20) | stage 20 there needs stage 310 here |
| Unlocks | [Shadows](shadows.md#stage-290) | stage 290 there needs stage 280 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met Miri in the Crossroads Guardhouse. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-20"></span>20 | Since I had helped Ailshara, she wouldn't tell me about Andor. **(completes quest)** | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | 1 XP |
| <span id="stage-30"></span>30 | Since I had hidden the truth about the bootlegging of beer from Sullengard, she wouldn't tell me about Andor. **(completes quest)** | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | 1 XP<br>removes monsters from loneford4 |
| <span id="stage-40"></span>40 | Since I had aided Feygard once or twice earlier, she would tell me about Andor, after I had completed an investigation for her. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-50"></span>50 | Since Miri was poisoned by slitherers near Sullengard, and healing is taking time, she wanted me to investigate something bad in the Purple Hills in the strange areas to the south of Stoutford. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | sets stage 3 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-3)<br>spawns monsters on galmore_45 |
| <span id="stage-60"></span>60 | I went to the area to the south of Stoutford and encountered an impassable force there. | walking into a blocked passage on [galmore_45](../maps/galmore_45.md) | stage 50 | – |
| <span id="stage-70"></span>70 | There was a piece of Kazaul ritual there, which I had encountered before. I should inform Miri. | walking into a blocked passage on [galmore_45](../maps/galmore_45.md) | stage 50, stage 60 | – |
| <span id="stage-80"></span>80 | Miri asked me where I had seen this before. I told her about a task I had carried out on behalf of Throdna of the Blackwater settlement. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 60, stage 70 | – |
| <span id="stage-90"></span>90 | Miri told me to meet him and enquire further. And gave me a phrase to use whenever he started rambling. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | – |
| <span id="stage-100"></span>100 | Throdna told me it was part of a ritual to break the barrier which forms when one does a ritual to call strong Kazaul monsters. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 90 | – |
| <span id="stage-110"></span>110 | The ritual consisted of two parts which I had found earlier, and a chant in a book called Calomyran Secrets. I need to report this to Miri. | [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) | stage 90 | – |
| <span id="stage-120"></span>120 | I told Miri about finding the book for an Old Man in Fallhaven.  She told me to talk to him. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 100, stage 110 | – |
| <span id="stage-130"></span>130 | The Old Man would not let me borrow the book, so I started noting the chant in front of him. | [Old man](../monsters/old_man.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) | stage 110 | – |
| <span id="stage-140"></span>140 | The book contained half the chant. The rest was to be found in another book Azimyran Secrets. | [Old man](../monsters/old_man.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) | stage 110 | – |
| <span id="stage-150"></span>150 | Miri told me she'd trace the book. She told me to wait for her return. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 120, stage 140 | removes monsters from houseatcrossroads0<br>starts timer “dds_miri” |
| <span id="stage-160"></span>160 | Miri came back and told me that the book Azimyran Secrets was with an old hermit near Arulir mountain. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 150 | – |
| <span id="stage-170"></span>170 | I met the old hermit and asked him about the book, Azimyran Secrets. | [Old hermit](../monsters/dds_oldhermit.md) ([waytolake12](../maps/waytolake12.md)) | stage 160 | – |
| <span id="stage-180"></span>180 | He refused to give it to me, so I copied the chant sitting with him. I needed to tell Miri. | [Old hermit](../monsters/dds_oldhermit.md) ([waytolake12](../maps/waytolake12.md)) | stage 160 | – |
| <span id="stage-190"></span>190 | Miri told me to hurry, and pass the barrier. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | – | removes monsters from houseatcrossroads0 |
| <span id="stage-198"></span>198 | After destroying the ritual statue of Kazaul, beyond the barrier I found a crying woman. | [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 190 | 5,000 XP |
| <span id="stage-200"></span>200 | She was performing a ritual that should bring her husband back to life. | [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 190 | spawns monsters on galmore_45 |
| <span id="stage-210"></span>210 | Miri, who followed me, convinced the woman that it was actually an evil ritual to overrun Dhayavar with Kazaul's monsters. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 190 | – |
| <span id="stage-220"></span>220 | The mourning woman told us that the ritual was given to her by a priest who walks on lava east of the Purple Hills. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 190, stage 210 | removes monsters from galmore_45<br>spawns monsters on loneford4 |
| <span id="stage-230"></span>230 | We let the mourning woman go. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-232"></span>232 | The mourning woman cried that she would never be happy again. | [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 220 | 2,000 XP |
| <span id="stage-240"></span>240 | I had to travel to the lava wastelands. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md))<br>[Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) | stage 190, stage 220 | spawns monsters on galmore_41 |
| <span id="stage-250"></span>250 | There, after fighting monsters, I met a priest in red. | [Dark priest](../monsters/dds_dark_priest.md) ([galmore_41](../maps/galmore_41.md)) | stage 190 | – |
| <span id="stage-260"></span>260 | He accused me of interfering. Miri, who again followed me, revealed the red priest to be a monster. | [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2) ([galmore_41](../maps/galmore_41.md))<br>[Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 190 | removes monsters from galmore_41<br>spawns monsters on galmore_41 |
| <span id="stage-270"></span>270 | I defeated the monster. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 260 | – |
| <span id="stage-280"></span>280 | Miri fulfilled her promise and told me that Andor would be refilling his food supplies at Rosmara's food stand. | [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) | stage 260 | 15,000 XP<br>removes monsters from galmore_41<br>spawns monsters on houseatcrossroads0<br>sets stage 6 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-6)<br>spawns monsters on wayto_feygard_duleian_2 |
| <span id="stage-300"></span>300 | Indeed, I have found Andor there. | [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) | stage 280 | – |
| <span id="stage-310"></span>310 | He told me he couldn't come home now, and vanished. **(completes quest)** | [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) | stage 280 | 5,000 XP<br>sets stage 145 of [Search for Andor](../quests/andor.md#stage-145) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki cannot yet trace. Claims about how to reach it should be treated as unverified.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically → **stage 10**. NPC: “Ah, one of the kids who've been causing trouble around Dhayavar.”

???+ note "Stage 20: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Tell me please.” — **conditions:** reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82) → **stage 20**. NPC: “By switching Gandoren's shipment with degraded ones, you have proved not to be. Suffice to say, when I was last there…”

???+ note "Stage 30: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Tell me please.” — **conditions:** reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120) → **stage 30**; also removes monsters from loneford4. NPC: “By hiding the truth of the beer bootlegging from Sullengard, you have proved not to be. Suffice to say, when I was…”

???+ note "Stage 40: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-40) → **stage 40**. NPC: “You've aided Feygard once before. Now, investigate something for me. If you succeed, I'll tell you what I know of Andor.”

???+ note "Stage 50: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50) → **stage 50**; also sets stage 3 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-3), spawns monsters on galmore_45, spawns monsters on galmore_45. NPC: “Journey to the south of Stoutford, into the weird lands there. Investigate what's going on in the Purple Hills.”

???+ note "Stage 60: 1 route"

    1. walking into a blocked passage on [galmore_45](../maps/galmore_45.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50) → **stage 60**. NPC: “I have never seen such a barrier.”

???+ note "Stage 70: 1 route"

    1. walking into a blocked passage on [galmore_45](../maps/galmore_45.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-50); reached stage 60 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-60); NOT reached stage 70 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-70); random chance (20%) → **stage 70**. NPC: “You stumble upon a piece of paper.”

???+ note "Stage 80: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “When I was at the Blackwater settlement, I had used this, on the guidance of Throdna, as part of purifying…” — **conditions:** reached stage 60 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-60); reached stage 70 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-70) → **stage 80**. NPC: “That is bad news indeed. We must act.”

???+ note "Stage 90: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 90 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-90) → **stage 90**. NPC: “Go meet Throdna. Since he's known to ramble, just say 'Kazaul est' to focus him again.”

???+ note "Stage 100: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “Not again - Kazaul Est!” — **conditions:** reached stage 90 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-90); NOT reached stage 100 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-100) → **stage 100**. NPC: “Yes. This piece of the ritual is of Kazaul. Along with the first part, one can raise Kazaul monsters, use in…”

???+ note "Stage 110: 1 route"

    1. Talk to [Throdna](../monsters/throdna.md) ([blackwater_mountain50](../maps/blackwater_mountain50.md)) → choose “So, nothing to be done?” — **conditions:** reached stage 90 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-90); NOT reached stage 100 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-100) → **stage 110**. NPC: “I didn't say that! There was a traveler a long time back - he wrote a book Calomyran Secrets. It has the chant of…”

???+ note "Stage 120: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “I know! I helped find this book for that old man in Fallhaven. He must still have it. Let me talk to him.” — **conditions:** reached stage 100 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-100); reached stage 110 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-110); NOT reached stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140) → **stage 120**. NPC: “Good thinking! Do that, seek the old man with the book.”

???+ note "Stage 130: 1 route"

    1. Talk to [Old man](../monsters/old_man.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) → choose “I need a chant from it to break a Kazaul spell.” — **conditions:** reached stage 110 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-110); NOT reached stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140) → **stage 130**. NPC: “Copy it then.”

???+ note "Stage 140: 1 route"

    1. Talk to [Old man](../monsters/old_man.md) ([fallhaven_nw](../maps/fallhaven_nw.md)) → choose “However, it is not complete. Do you also have the book Azimyran Secrets?” — **conditions:** reached stage 110 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-110); NOT reached stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140) → **stage 140**. NPC: “No, sorry. Do let me know if you come across a copy.”

???+ note "Stage 150: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “I don't know.” — **conditions:** reached stage 120 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-120); reached stage 140 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-140) → **stage 150**; also removes monsters from houseatcrossroads0, starts timer “dds_miri”. NPC: “You have run around enough. Let me ask around. Why don't you rest? Stroll around outside a bit to refresh!”

???+ note "Stage 160: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Tell me.” — **conditions:** reached stage 150 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-150) → **stage 160**. NPC: “You know, at the old watch tower. The Hermit is said to have a copy of Azimyran Secrets. Go ...”

???+ note "Stage 170: 1 route"

    1. Talk to [Old hermit](../monsters/dds_oldhermit.md) ([waytolake12](../maps/waytolake12.md)) → choose “You are not no one. You have a copy of Azimyran Secrets.” — **conditions:** reached stage 160 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-160); NOT reached stage 180 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-180) → **stage 170**. NPC: “So? I'm not giving it to anyone. I'm too old to be threatened. And I want nothing.”

???+ note "Stage 180: 1 route"

    1. Talk to [Old hermit](../monsters/dds_oldhermit.md) ([waytolake12](../maps/waytolake12.md)) → choose “Sounds oddly appealing. Can I copy the rest of the chant?” — **conditions:** reached stage 160 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-160); NOT reached stage 180 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-180) → **stage 180**. NPC: “Sure. Here you go.”

???+ note "Stage 190: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 190**; also removes monsters from houseatcrossroads0. NPC: “Great. And now off to the barrier! Make haste - I'll join you as fast as my injuries allow.”

???+ note "Stage 198: 1 route"

    1. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → the conversation leads here automatically — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 198**. NPC: “Nooooo!”

???+ note "Stage 200: 1 route"

    1. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → choose “Do you know what you were doing?” — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 200**; also spawns monsters on galmore_45. NPC: “I was getting my husband back from the afterlife!”

???+ note "Stage 210: 2 routes"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Miri? When did you get here?” — **conditions:** reached stage 210 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-210) → **stage 210**. NPC: “Then why did the ritual not include something that links to your husband? Something precious to him?”
    2. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → choose “Miri? When did you get here?” — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 210**. NPC: “Then why did the ritual not include something that links to your husband? Something precious to him?”

???+ note "Stage 220: 2 routes"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Yes, who put you up to this?” — **conditions:** reached stage 210 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-210) → **stage 220**; also removes monsters from galmore_45, spawns monsters on loneford4. NPC: “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn…”
    2. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → choose “Yes, who put you up to this?” — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 220**; also removes monsters from galmore_45, spawns monsters on loneford4. NPC: “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn…”

???+ note "Stage 232: 1 route"

    1. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → the conversation leads here automatically — **conditions:** reached stage 220 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-220) → **stage 232**. NPC: “Go away. I will never be happy in my life.”

???+ note "Stage 240: 2 routes"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 220 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-220) → **stage 240**; also spawns monsters on galmore_41. NPC: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?”
    2. Talk to [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman) ([galmore_45](../maps/galmore_45.md)) → choose “Nice job.” — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 240**; also spawns monsters on galmore_41. NPC: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?”

???+ note "Stage 250: 1 route"

    1. Talk to [Dark priest](../monsters/dds_dark_priest.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 250**. NPC: “How dare you stop my spell?”

???+ note "Stage 260: 2 routes"

    1. Talk to [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2) ([galmore_41](../maps/galmore_41.md)) → choose “But it's unfair to ...” — **conditions:** reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190) → **stage 260**; also removes monsters from galmore_41, spawns monsters on galmore_41. NPC: “Are we going to do this now, or are you two going to talk all day?”
    2. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “But it's unfair to ...” — **conditions:** reached stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260) → **stage 260**; also removes monsters from galmore_41, spawns monsters on galmore_41. NPC: “Are we going to do this now, or are you two going to talk all day?”

???+ note "Stage 270: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → the conversation leads here automatically — **conditions:** reached stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260); killed 1× [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest_monster) → **stage 270**. NPC: “Finally. Well done, kid.”

???+ note "Stage 280: 1 route"

    1. Talk to [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) → choose “Really? Tell me!” — **conditions:** reached stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260); killed 1× [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest_monster) → **stage 280**; also removes monsters from galmore_41, spawns monsters on houseatcrossroads0, sets stage 6 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-6), spawns monsters on wayto_feygard_duleian_2. NPC: “Andor is going to visit Rosmara to refill his travel supplies.”

???+ note "Stage 300: 1 route"

    1. Talk to [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) → choose “Hey, Andor!” — **conditions:** reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280) → **stage 300**

???+ note "Stage 310: 1 route"

    1. Talk to [Andor](../monsters/dds_andor.md) ([road5_house](../maps/road5_house.md)) → choose “Are you just going to disappear again? Please don't!” — **conditions:** reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280) → **stage 310**; also sets stage 145 of [Search for Andor](../quests/andor.md#stage-145)


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 31 lines added |
| [v0.8.15](../versions/0.8.15.md) | Stage 70 journal text changed<br>Stage 80 journal text changed<br>Stage 110 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkness_in_daylight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkness_in_daylight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkness_in_daylight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkness_in_daylight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=darkness_in_daylight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `darkness_in_daylight` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 198, 200, 210, 220, 230, 232, 240, 250, 260, 270, 280, 300, 310 |
    | Dialogue nodes setting stages | 10: `dds_miri_5`, 20: `dds_miri_22`, 30: `dds_miri_32`, 40: `dds_miri_42`, 50: `dds_miri_110`, 60: `dds_dark_shadow_10`, 70: `dds_dark_shadow_20`, 80: `dds_miri_220`, 90: `dds_miri_222`, 100: `dds_throdna_60`, 110: `dds_throdna_100`, 120: `dds_miri_320`, 130: `dds_oldman_50`, 140: `dds_oldman_70`, 150: `dds_miri_372`, 160: `dds_miri_422`, 170: `dds_oldhermit_30`, 180: `dds_oldhermit_60`, 190: `dds_miri_460`, 198: `dds_mourning_woman_22`, 200: `dds_mourning_woman_40`, 210: `dds_mourning_woman_82`, 220: `dds_mourning_woman_100`, 232: `dds_mourning_woman_2`, 240: `dds_miri_500`, 250: `dds_dark_priest_2`, 260: `dds_dark_priest2_40`, 270: `dds_miri_550`, 280: `dds_miri_590`, 300: `dds_andor_2`, 310: `dds_andor_52` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
