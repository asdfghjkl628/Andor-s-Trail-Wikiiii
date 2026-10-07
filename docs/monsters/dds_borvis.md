---
description: "Borvis is a non-player character (NPC) in Andor's Trail, found in Mt. Galmore. Starts Shadows."
---

# ![](../assets/icons/monsters/monsters_men2_8.png){ .sprite } Borvis

**Where to find Borvis:** Mt. Galmore: [Galmore 45](../maps/galmore_45.md#pin-npc-dds_borvis), [Galmore 41](../maps/galmore_41.md#pin-npc-dds_borvis), [Road 5](../maps/road5.md#pin-npc-dds_borvis)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Shadows](../quests/shadows.md) |
| **Found in** | Mt. Galmore |
| **Entry ID** | `dds_borvis` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 41](../maps/galmore_41.md) | – | 1 | Appears later, during a quest |
| [Galmore 45](../maps/galmore_45.md) | Mt. Galmore | 1 | Appears later, during a quest |
| [Road 5](../maps/road5.md) | – | 1 | Appears later, during a quest |

## Quests

- [Shadows](../quests/shadows.md): stages 10, 20, 30, 40, 70, 80, 150, 160, 165, 190, 200, 220, 240, 250, 260
- [Darkness in the Daylight and Shadows story flags (hidden flag)](../quests/dds_nd.md): stages 3, 6

## Dialogue simulator

Set your quest stages and items, then talk to Borvis. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_borvis.json" data-npc="Borvis" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (77 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-dds_borvis"></span>**`dds_borvis`** Borvis: “Hello, $playername” — **effects:** sets stage 10 of [Shadows](../quests/shadows.md#stage-10)

    - Next → [dds_borvis_2](#d-dds_borvis_2)

    <span id="d-dds_borvis_2"></span>**`dds_borvis_2`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120))* → [dds_borvis_5](#d-dds_borvis_5)
    - branch 2 *(if reached stage 260 of [Shadows](../quests/shadows.md#stage-260))* → [dds_borvis_600](#d-dds_borvis_600)
    - branch 3 *(if reached stage 240 of [Shadows](../quests/shadows.md#stage-240); killed 1× [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest_monster))* → [dds_borvis_550](#d-dds_borvis_550)
    - branch 4 *(if reached stage 240 of [Shadows](../quests/shadows.md#stage-240))* → [dds_dark_priest2_110](#d-dds_dark_priest2_110)
    - branch 5 *(if reached stage 230 of [Shadows](../quests/shadows.md#stage-230))* → [dds_borvis_540](#d-dds_borvis_540)
    - branch 6 *(if reached stage 200 of [Shadows](../quests/shadows.md#stage-200))* → [dds_borvis_500](#d-dds_borvis_500)
    - branch 7 *(if reached stage 190 of [Shadows](../quests/shadows.md#stage-190))* → [dds_mourning_woman_250](#d-dds_mourning_woman_250)
    - branch 8 *(if reached stage 165 of [Shadows](../quests/shadows.md#stage-165))* → [dds_borvis_290](#d-dds_borvis_290)
    - branch 9 *(if reached stage 160 of [Shadows](../quests/shadows.md#stage-160))* → [dds_borvis_280](#d-dds_borvis_280)
    - branch 10 *(if reached stage 90 of [Shadows](../quests/shadows.md#stage-90))* → [dds_borvis_250](#d-dds_borvis_250)
    - branch 11 *(if reached stage 80 of [Shadows](../quests/shadows.md#stage-80))* → [dds_borvis_190](#d-dds_borvis_190)
    - branch 12 *(if reached stage 60 of [Shadows](../quests/shadows.md#stage-60))* → [dds_borvis_150](#d-dds_borvis_150)
    - branch 13 *(if reached stage 40 of [Shadows](../quests/shadows.md#stage-40))* → [dds_borvis_100](#d-dds_borvis_100)
    - branch 14 *(if reached stage 30 of [Shadows](../quests/shadows.md#stage-30))* → [dds_borvis_22](#d-dds_borvis_22)
    - branch 15 *(if NOT reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82))* → [dds_borvis_8](#d-dds_borvis_8)
    - branch 16 *(if NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120))* → [dds_borvis_7](#d-dds_borvis_7)
    - branch 17 → [dds_borvis_10](#d-dds_borvis_10)

    <span id="d-dds_borvis_5"></span>**`dds_borvis_5`** Borvis: “Begone, you Feygard lackey! I refuse to talk to you! You reek of Feygard!” — **effects:** sets stage 10 of [Shadows](../quests/shadows.md#stage-10), sets stage 20 of [Shadows](../quests/shadows.md#stage-20)

    - “I ... eh ... what?” → [dds_borvis_6](#d-dds_borvis_6)

    <span id="d-dds_borvis_600"></span>**`dds_borvis_600`** Borvis: “Isn't it a lovely day?”


    <span id="d-dds_borvis_550"></span>**`dds_borvis_550`** Borvis: “Finally. Well done, kid.” — **effects:** sets stage 250 of [Shadows](../quests/shadows.md#stage-250)

    - “Is it over?” → [dds_borvis_560](#d-dds_borvis_560)

    <span id="d-dds_dark_priest2_110"></span>**`dds_dark_priest2_110`** [Borvis](../monsters/dds_borvis.md): “You're no priest!”

    - “Borvis! At last!” → [dds_dark_priest2_120](#d-dds_dark_priest2_120)

    <span id="d-dds_borvis_540"></span>**`dds_borvis_540`** Borvis: “The monster is not dead. Go and finish it!”


    <span id="d-dds_borvis_500"></span>**`dds_borvis_500`** Borvis: “It's not done yet. Can you talk to this priest? And tackle him as he deserves?” — **effects:** sets stage 220 of [Shadows](../quests/shadows.md#stage-220), spawns monsters on galmore_41

    - “Of course! On my way!” → *conversation ends*
    - “Why not you?” → [dds_borvis_502](#d-dds_borvis_502)

    <span id="d-dds_mourning_woman_250"></span>**`dds_mourning_woman_250`** [Borvis](../monsters/dds_borvis.md): “Is that what you think?”

    - “Borvis? I didn't expect you already.” → [dds_mourning_woman_260](#d-dds_mourning_woman_260)

    <span id="d-dds_borvis_290"></span>**`dds_borvis_290`** Borvis: “Go now and destroy the shield, and then the renegade priest. Make haste!” — **effects:** sets stage 165 of [Shadows](../quests/shadows.md#stage-165)


    <span id="d-dds_borvis_280"></span>**`dds_borvis_280`** [Borvis](../monsters/dds_borvis.md): “While you slept I've prepared a tiny chant that nevertheless will destroy the Shadow shield. Here, read it.” — **effects:** sets stage 160 of [Shadows](../quests/shadows.md#stage-160), applies condition shadowbless_str, applies condition shadowsleep, applies condition fatigue1, applies condition life_drain

    - “This little thing?” → [dds_borvis_282](#d-dds_borvis_282)

    <span id="d-dds_borvis_250"></span>**`dds_borvis_250`** Borvis: “It took you a while. I thought you had given up.” — **effects:** sets stage 150 of [Shadows](../quests/shadows.md#stage-150)

    - “[panting] Here are your energies, Borvis. I'm exhausted!” → [dds_borvis_260](#d-dds_borvis_260)

    <span id="d-dds_borvis_190"></span>**`dds_borvis_190`** Borvis: “You'll need to get me the blessings of Shadow's Strength, Shadow Sleepiness, Fatigue and Life Drain. Through yourself.”

    - “Through myself?” → [dds_borvis_192](#d-dds_borvis_192)

    <span id="d-dds_borvis_150"></span>**`dds_borvis_150`** Borvis: “Ah, you're back! Don't tell me you have defeated the renegade priest already? Not that I detected any change in the Shadow energies, which are in turmoil.”

    - “There's some sort of force shield blocking the path.” → [dds_borvis_152](#d-dds_borvis_152)

    <span id="d-dds_borvis_100"></span>**`dds_borvis_100`** Borvis: “Journey to the south of Stoutford, into the forests there. See what that Shadow priest is doing there, and stop him from doing it.” — **effects:** sets stage 40 of [Shadows](../quests/shadows.md#stage-40), sets stage 3 of [Darkness in the Daylight and Shadows story flags (hidden flag)](../quests/dds_nd.md#stage-3), spawns monsters on galmore_45, spawns monsters on galmore_45

    - “Sounds easy. I'll do it.” → *conversation ends*

    <span id="d-dds_borvis_22"></span>**`dds_borvis_22`** Borvis: “Listen, do you want help the Shadow?” — **effects:** sets stage 30 of [Shadows](../quests/shadows.md#stage-30)

    - “That depends on what you want me to do.” → [dds_borvis_30](#d-dds_borvis_30)

    <span id="d-dds_borvis_8"></span>**`dds_borvis_8`** Borvis: “You have betrayed our work by providing the Feygardians with weapons. At least you did the right thing when you didn't tell the truth about the Beer Bootlegging from Sullengard. So I'll let it go this time.” — **effects:** sets stage 10 of [Shadows](../quests/shadows.md#stage-10), sets stage 30 of [Shadows](../quests/shadows.md#stage-30)

    - “I ... eh ... what?” → [dds_borvis_10](#d-dds_borvis_10)

    <span id="d-dds_borvis_7"></span>**`dds_borvis_7`** Borvis: “You have betrayed our work by telling the truth about Beer Bootlegging from Sullengard. At least you did the right thing when you provided the Feygardians with bad weapons. So I'll let it go this time.” — **effects:** sets stage 10 of [Shadows](../quests/shadows.md#stage-10), sets stage 30 of [Shadows](../quests/shadows.md#stage-30)

    - “I ... eh ... what?” → [dds_borvis_10](#d-dds_borvis_10)

    <span id="d-dds_borvis_10"></span>**`dds_borvis_10`** Borvis: “Shadow bless you, child!” — **effects:** sets stage 10 of [Shadows](../quests/shadows.md#stage-10), removes monsters from loneford4

    - “And you, sir!” → [dds_borvis_20](#d-dds_borvis_20)

    <span id="d-dds_borvis_6"></span>**`dds_borvis_6`** Borvis: “Begone!”


    <span id="d-dds_borvis_560"></span>**`dds_borvis_560`** Borvis: “This is over, yes.”

    - Next → [dds_borvis_562](#d-dds_borvis_562)

    <span id="d-dds_dark_priest2_120"></span>**`dds_dark_priest2_120`** Borvis: “My legs are not as young as yours anymore.”

    - “You made me fight alone all way here.” → [dds_dark_priest2_130](#d-dds_dark_priest2_130)

    <span id="d-dds_borvis_502"></span>**`dds_borvis_502`** Borvis: “You'll be faster. Don't worry, I'll follow you.”

    - “Of course! On my way!” → *conversation ends*

    <span id="d-dds_mourning_woman_260"></span>**`dds_mourning_woman_260`** Borvis: “I came with all haste. You were faster.”

    - Next → [dds_mourning_woman_262](#d-dds_mourning_woman_262)

    <span id="d-dds_borvis_282"></span>**`dds_borvis_282`** Borvis: “Yes.”

    - Next → [dds_borvis_290](#d-dds_borvis_290)

    <span id="d-dds_borvis_260"></span>**`dds_borvis_260`** Borvis: “Great! Let me quickly extract them from you.”

    - “[Weak voice] Please do.” → [dds_borvis_262](#d-dds_borvis_262)

    <span id="d-dds_borvis_192"></span>**`dds_borvis_192`** Borvis: “Yes.”

    - “That'll make things harder.” → [dds_borvis_200](#d-dds_borvis_200)

    <span id="d-dds_borvis_152"></span>**`dds_borvis_152`** Borvis: “Tell me more about it.”

    - “I found some stones with strange markings on them.” → [dds_borvis_154](#d-dds_borvis_154)

    <span id="d-dds_borvis_30"></span>**`dds_borvis_30`** Borvis: “A cautious one! Capital!”

    - Next → [dds_borvis_40](#d-dds_borvis_40)

    <span id="d-dds_borvis_20"></span>**`dds_borvis_20`** Borvis: “A very polite kid! Plus, as the Shadow has been whispering to me, a helpful one.” — **effects:** sets stage 30 of [Shadows](../quests/shadows.md#stage-30)

    - Next → [dds_borvis_22](#d-dds_borvis_22)

    <span id="d-dds_borvis_562"></span>**`dds_borvis_562`** Borvis: “And now for your reward.”

    - “Yes? Hope it is worth it.” → [dds_borvis_570](#d-dds_borvis_570)

    <span id="d-dds_dark_priest2_130"></span>**`dds_dark_priest2_130`** Borvis: “Don't worry - it's worth it.”

    - “But it's unfair to ...” → [dds_dark_priest2_140](#d-dds_dark_priest2_140)

    <span id="d-dds_mourning_woman_262"></span>**`dds_mourning_woman_262`** Borvis: “[To the mourning woman] The ritual was not to bring back your husband - it is to bring Kazaul's powerful monsters into Dhayavar.”

    - Next → [dds_mourning_woman_270](#d-dds_mourning_woman_270)

    <span id="d-dds_borvis_262"></span>**`dds_borvis_262`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if affected by shadowbless_str; affected by shadowsleep; affected by fatigue1; affected by life_drain)* → [dds_borvis_270](#d-dds_borvis_270)
    - branch 2 → [dds_borvis_264](#d-dds_borvis_264)

    <span id="d-dds_borvis_200"></span>**`dds_borvis_200`** Borvis: “This is the only way! Now, be a Shadow warrior! Go fetch them.”

    - “Sigh. From where?” → [dds_borvis_210](#d-dds_borvis_210)

    <span id="d-dds_borvis_154"></span>**`dds_borvis_154`** Borvis: “With strange markings? Hmm. Show me.”

    - “I don't have any of these stones.” → [dds_borvis_156](#d-dds_borvis_156)

    <span id="d-dds_borvis_40"></span>**`dds_borvis_40`** Borvis: “Listen carefully - you have met many of us Shadow priests across Dhayavar. But, not all of us are equal.”

    - “You mean, there are priests more powerful than you?” → [dds_borvis_50](#d-dds_borvis_50)

    <span id="d-dds_borvis_570"></span>**`dds_borvis_570`** Borvis: “You are still looking for your brother?”

    - “Of course.” → [dds_borvis_580](#d-dds_borvis_580)

    <span id="d-dds_dark_priest2_140"></span>**`dds_dark_priest2_140`** [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2): “Are we going to do this now, or are you two going to talk all day?” — **effects:** removes monsters from galmore_41, spawns monsters on galmore_41, sets stage 240 of [Shadows](../quests/shadows.md#stage-240)

    - “Ah, sorry: KAZAUL EST!” → [dds_dark_priest2_150](#d-dds_dark_priest2_150)

    <span id="d-dds_mourning_woman_270"></span>**`dds_mourning_woman_270`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “You lie! You don't want my happiness.”

    - Next → [dds_mourning_woman_272](#d-dds_mourning_woman_272)

    <span id="d-dds_borvis_270"></span>**`dds_borvis_270`** [Dummy NPC](../monsters/none.md): “Borvis did many obscure things, chanting all the way. But you were too tired to follow and dozed.”

    - Next → [dds_borvis_272](#d-dds_borvis_272)

    <span id="d-dds_borvis_264"></span>**`dds_borvis_264`** [Dummy NPC](../monsters/none.md): “Borvis examines you.”

    - Next → [dds_borvis_266](#d-dds_borvis_266)

    <span id="d-dds_borvis_210"></span>**`dds_borvis_210`** Borvis: “Go to my friend Talion in Loneford. He'll give you the blessing of Shadow's Strength.” — **effects:** sets stage 80 of [Shadows](../quests/shadows.md#stage-80)

    - Next → [dds_borvis_212](#d-dds_borvis_212)

    <span id="d-dds_borvis_156"></span>**`dds_borvis_156`** Borvis: “No? You didn't think of the obvious idea that I should see them?”

    - “Unfortunately the stones could not be picked up or moved - as if they had some kind of energy in them.” → [dds_borvis_160](#d-dds_borvis_160)

    <span id="d-dds_borvis_50"></span>**`dds_borvis_50`** Borvis: “Er ... well ... not exactly what I mean.”

    - Next → [dds_borvis_52](#d-dds_borvis_52)

    <span id="d-dds_borvis_580"></span>**`dds_borvis_580`** Borvis: “I know where he is. Or better, where he will be soon.”

    - “Really? Tell me!” → [dds_borvis_590](#d-dds_borvis_590)

    <span id="d-dds_dark_priest2_150"></span>**`dds_dark_priest2_150`** [Borvis](../monsters/dds_borvis.md): “That's its true form! A monster masquerading as a priest! Attack!”


    <span id="d-dds_mourning_woman_272"></span>**`dds_mourning_woman_272`** [Borvis](../monsters/dds_borvis.md): “Do you think monsters would have assisted you? And a barrier would have sprung up? Just for one person?”

    - Next → [dds_mourning_woman_280](#d-dds_mourning_woman_280)

    <span id="d-dds_borvis_272"></span>**`dds_borvis_272`** Borvis: “Suddenly you wake up, completely refreshed.”

    - “Ah! I feel like I could tear down trees!” → [dds_borvis_280](#d-dds_borvis_280)

    <span id="d-dds_borvis_266"></span>**`dds_borvis_266`** [Borvis](../monsters/dds_borvis.md): “Oh you useless kid!”

    - “What?” → [dds_borvis_267](#d-dds_borvis_267)

    <span id="d-dds_borvis_212"></span>**`dds_borvis_212`** Borvis: “Also he can tell you where to find the others.”


    <span id="d-dds_borvis_160"></span>**`dds_borvis_160`** Borvis: “That sounds like a Shadow shield! Used to protect our incantations from outside interference, like those Feygard interferers.” — **effects:** sets stage 70 of [Shadows](../quests/shadows.md#stage-70)

    - “But can't it recognize I am Shadow warrior, as you say, and let me pass?” → [dds_borvis_162](#d-dds_borvis_162)

    <span id="d-dds_borvis_52"></span>**`dds_borvis_52`** Borvis: “What I mean is this: there seems to be a priest who thinks the Shadow calls for the conquest of Dhayavar!”

    - “That's terrible!” → [dds_borvis_60](#d-dds_borvis_60)

    <span id="d-dds_borvis_590"></span>**`dds_borvis_590`** Borvis: “Andor is going to visit Alynndir to refill his travel supplies.” — **effects:** sets stage 260 of [Shadows](../quests/shadows.md#stage-260), removes monsters from galmore_41, spawns monsters on road5, sets stage 6 of [Darkness in the Daylight and Shadows story flags (hidden flag)](../quests/dds_nd.md#stage-6), spawns monsters on road5_house

    - “Thank you!” → *conversation ends*
    - “Who is Alynndir?” → [dds_borvis_592](#d-dds_borvis_592)

    <span id="d-dds_mourning_woman_280"></span>**`dds_mourning_woman_280`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “I don't believe you.”

    - Next → [dds_mourning_woman_282](#d-dds_mourning_woman_282)

    <span id="d-dds_borvis_267"></span>**`dds_borvis_267`** Borvis: “You didn't get them all! Go get the missing ones right now!”


    <span id="d-dds_borvis_162"></span>**`dds_borvis_162`** Borvis: “No.”

    - “But of course it would let you pass, wouldn't it?” → [dds_borvis_170](#d-dds_borvis_170)

    <span id="d-dds_borvis_60"></span>**`dds_borvis_60`** Borvis: “And I need your help to stop him!”

    - “Why? You can't take him on? Not powerful enough?” → [dds_borvis_70](#d-dds_borvis_70)

    <span id="d-dds_borvis_592"></span>**`dds_borvis_592`** Borvis: “Alynndir lives in a lonely house down the road to Nor City. Don't you know?”


    <span id="d-dds_mourning_woman_282"></span>**`dds_mourning_woman_282`** [Borvis](../monsters/dds_borvis.md): “Then why did the ritual not include something that links to your husband? Something precious to him?” — **effects:** sets stage 190 of [Shadows](../quests/shadows.md#stage-190)

    - Next → [dds_mourning_woman_290](#d-dds_mourning_woman_290)

    <span id="d-dds_borvis_170"></span>**`dds_borvis_170`** Borvis: “Kid, the world is more complex than you might think with that small brain of yours.”

    - Next → [dds_borvis_172](#d-dds_borvis_172)

    <span id="d-dds_borvis_70"></span>**`dds_borvis_70`** Borvis: “No! Not that! To stop him, one needs a Shadow warrior, like you!”

    - “Me a Shadow warrior! OK, what do I need to do?” → [dds_borvis_80](#d-dds_borvis_80)

    <span id="d-dds_mourning_woman_290"></span>**`dds_mourning_woman_290`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Oh no! What do I do now? He's gone.”

    - Next → [dds_mourning_woman_292](#d-dds_mourning_woman_292)

    <span id="d-dds_borvis_172"></span>**`dds_borvis_172`** Borvis: “A Shadow shield is a very basic shield, even if strong. It keeps everyone out after it is cast.”

    - Next → [dds_borvis_174](#d-dds_borvis_174)

    <span id="d-dds_borvis_80"></span>**`dds_borvis_80`** Borvis: “That's the spirit!”

    - Next → [dds_borvis_82](#d-dds_borvis_82)

    <span id="d-dds_mourning_woman_292"></span>**`dds_mourning_woman_292`** [Borvis](../monsters/dds_borvis.md): “Pray where have you been praying. And tell me who put you up to this?”

    - “Yes, who put you up to this?” → [dds_mourning_woman_300](#d-dds_mourning_woman_300)

    <span id="d-dds_borvis_174"></span>**`dds_borvis_174`** Borvis: “Those small stones are shadow wards. They need to be neutralized”

    - “But how?” → [dds_borvis_180](#d-dds_borvis_180)

    <span id="d-dds_borvis_82"></span>**`dds_borvis_82`** Borvis: “Now, in the wasteland south of Stoutford, there have been reports of some suspicious activities.”

    - Next → [dds_borvis_84](#d-dds_borvis_84)

    <span id="d-dds_mourning_woman_300"></span>**`dds_mourning_woman_300`** [Mourning woman](../monsters/chapelgoer.md#v-dds_mourning_woman): “Why? That famous miracle priest who walks on lava, west of here. Do you need me anymore? Then I'm going home to mourn again.” — **effects:** sets stage 200 of [Shadows](../quests/shadows.md#stage-200), removes monsters from galmore_45, spawns monsters on loneford4

    - Next → [dds_mourning_woman_310](#d-dds_mourning_woman_310)

    <span id="d-dds_borvis_180"></span>**`dds_borvis_180`** Borvis: “Let me conjure a chant. I'll need some Shadow energies for that.”

    - “Shadow what?” → [dds_borvis_181](#d-dds_borvis_181)

    <span id="d-dds_borvis_84"></span>**`dds_borvis_84`** Borvis: “I fear it is my fellow priest summoning monsters to conquer all of Dhayavar. If it is not stopped, we might see lots of really unstoppable monsters popping up all over Dhayavar.”

    - “I'll kill them all!” → [dds_borvis_90](#d-dds_borvis_90)

    <span id="d-dds_mourning_woman_310"></span>**`dds_mourning_woman_310`** [Borvis](../monsters/dds_borvis.md): “Yes, you go back to your village. And we will have a chat with this famous miracle priest.”

    - “Nice job.” → [dds_borvis_500](#d-dds_borvis_500)

    <span id="d-dds_borvis_181"></span>**`dds_borvis_181`** Borvis: “Sorry. Of course you can't have knowledge of such things.”

    - Next → [dds_borvis_182](#d-dds_borvis_182)

    <span id="d-dds_borvis_90"></span>**`dds_borvis_90`** Borvis: “Brave - but only few in Dhayavar have the skills to go toe-to-toe against these monsters.”

    - Next → [dds_borvis_92](#d-dds_borvis_92)

    <span id="d-dds_borvis_182"></span>**`dds_borvis_182`** Borvis: “Shadow priests can create and give energies in form of blessings to one.”

    - Next → [dds_borvis_184](#d-dds_borvis_184)

    <span id="d-dds_borvis_92"></span>**`dds_borvis_92`** Borvis: “We must stop them at the source.”

    - “Yes, but what can we do?” → [dds_borvis_100](#d-dds_borvis_100)

    <span id="d-dds_borvis_184"></span>**`dds_borvis_184`** Borvis: “You need get and carry those energies to me. I'll use them to create a chant to take down the Shadow shield.”

    - “OK. Now what exactly do I ask for? And from whom?” → [dds_borvis_190](#d-dds_borvis_190)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 77 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dds_borvis` |
    | Spawn group | `dds_borvis` |
    | Loot table | – |
    | Conversation | `dds_borvis` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:8` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_borvis",
     "name": "Borvis",
     "iconID": "monsters_men2:8",
     "monsterClass": "humanoid",
     "spawnGroup": "dds_borvis",
     "phraseID": "dds_borvis"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_borvis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_borvis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_borvis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_borvis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
