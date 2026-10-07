---
description: "Talion is a non-player character (NPC) in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men2_8.png){ .sprite } Talion

**Where to find Talion:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Entry ID** | `talion` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Necklace of the guardian](../items/necklace_shield1.md) | 100% | 1 |
| [Necklace of the protector](../items/necklace_protector.md) | 100% | 1 |
| [Lesser ring of block](../items/ring_block1.md) | 100% | 1 |
| [Ring of the protector](../items/ring_protector.md) | 100% | 1 |
| [Ring of damage +5](../items/ring_dmg5.md) | 100% | 1 |

## Quests

- [Flows through the veins](../quests/loneford.md): stages 23, 25
- [I have it in me](../quests/maggots.md): stages 30, 40, 41, 42, 43, 45, 50, 51
- [Shadows](../quests/shadows.md): stages 90, 100
- [Troubling times](../quests/troubling_times.md): stages 70, 80, 170, 280, 290, 300

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Talion. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/talion.json" data-npc="Talion" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (131 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-talion"></span>**`talion`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 51 of [I have it in me](../quests/maggots.md#stage-51))* → [talion_0](#d-talion_0)
    - branch 2 *(if reached stage 50 of [I have it in me](../quests/maggots.md#stage-50))* → [talion_cured_1](#d-talion_cured_1)
    - branch 3 *(if reached stage 45 of [I have it in me](../quests/maggots.md#stage-45))* → [talion_cure_5](#d-talion_cure_5)
    - branch 4 *(if reached stage 30 of [I have it in me](../quests/maggots.md#stage-30))* → [talion_infect_30](#d-talion_infect_30)
    - branch 5 *(if reached stage 10 of [I have it in me](../quests/maggots.md#stage-10))* → [talion_infect_1](#d-talion_infect_1)
    - branch 6 → [talion_0](#d-talion_0)

    <span id="d-talion_0"></span>**`talion_0`** Talion: “Shadow be with you.”

    - “Do you know anything about the illness here in Loneford?” *(if reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11))* → [talion_1](#d-talion_1)
    - “Do you have anything to trade?” → *shop opens*
    - “What blessings can you provide?” *(if reached stage 51 of [I have it in me](../quests/maggots.md#stage-51))* → [talion_bless_1](#d-talion_bless_1)
    - “I need some help finding out who is responsible for casting a Shadow spell that causes a person to become noticeable.” *(if reached stage 50 of [Troubling times](../quests/troubling_times.md#stage-50); NOT reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70))* → [tt_talion_10](#d-tt_talion_10)
    - “Sorry, we were interrupted. You were just talking about the Striking Spectacle Shadow spell.” *(if reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70); NOT reached stage 80 of [Troubling times](../quests/troubling_times.md#stage-80))* → [tt_talion_10](#d-tt_talion_10)
    - “Here I've brought you the things that you require for the dispelling.” *(if reached stage 80 of [Troubling times](../quests/troubling_times.md#stage-80); NOT reached stage 280 of [Troubling times](../quests/troubling_times.md#stage-280))* → [tt_talion_64](#d-tt_talion_64)
    - “Do you know the whereabouts of Sly Seraphina?” *(if reached stage 140 of [Troubling times](../quests/troubling_times.md#stage-140); NOT reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [tt_talion_90](#d-tt_talion_90)
    - “I've brought you the things you had required for dispelling.” *(if reached stage 280 of [Troubling times](../quests/troubling_times.md#stage-280); NOT reached stage 290 of [Troubling times](../quests/troubling_times.md#stage-290))* → [tt_talion_100](#d-tt_talion_100)
    - “Haven't you forgotten something?” *(if reached stage 290 of [Troubling times](../quests/troubling_times.md#stage-290); NOT reached stage 300 of [Troubling times](../quests/troubling_times.md#stage-300))* → [tt_talion_300](#d-tt_talion_300)
    - “Borvis said you could provide me with some information.” *(if reached stage 90 of [Shadows](../quests/shadows.md#stage-90); NOT reached stage 100 of [Shadows](../quests/shadows.md#stage-100))* → [dds_talion_50](#d-dds_talion_50)
    - “The blessing has worn off too early. Could you give it again?” *(if reached stage 100 of [Shadows](../quests/shadows.md#stage-100); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by shadowbless_str)* → [dds_talion_80](#d-dds_talion_80)

    <span id="d-talion_cured_1"></span>**`talion_cured_1`** Talion: “Ah, that seems to have worked. Frankly, I was a little worried that it might not have worked, but seeing you spit out that worm really confirms it. Ha ha.”

    - “Yuck! Those things were inside of me?” → [talion_cured_2](#d-talion_cured_2)
    - “What now?” → [talion_cured_3](#d-talion_cured_3)

    <span id="d-talion_cure_5"></span>**`talion_cure_5`** Talion: “[He gives the potion a thorough shake for quite a while]”

    - Next → [talion_cure_6](#d-talion_cure_6)

    <span id="d-talion_infect_30"></span>**`talion_infect_30`** Talion: “You return. Have you gathered those things that I asked for?”

    - “What was I supposed to collect again?” → [talion_infect_11](#d-talion_infect_11)
    - “I brought five bones for you.” → [talion_bone_s](#d-talion_bone_s)
    - “I brought two pieces of animal hair for you.” → [talion_hair_s](#d-talion_hair_s)
    - “I brought an irdegh poison gland for you.” → [talion_irdegh_s](#d-talion_irdegh_s)
    - “I brought an empty vial for you.” → [talion_vial_s](#d-talion_vial_s)
    - “Do you know anything about the illness here in Loneford?” *(if reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11))* → [talion_1](#d-talion_1)
    - “Do you have anything to trade?” → *shop opens*

    <span id="d-talion_infect_1"></span>**`talion_infect_1`** Talion: “Oh my, what has happened to you? You don't look too well.”

    - “I was infected with something by a lich of Kazaul.” → [talion_infect_5](#d-talion_infect_5)
    - “A man called Ulirfendor told me he thought I might be infected with Kazaul rotworms.” → [talion_infect_2](#d-talion_infect_2)
    - “I was told to find you, and that you might be able to help me.” → [talion_infect_4](#d-talion_infect_4)

    <span id="d-talion_1"></span>**`talion_1`** Talion: “The people of Loneford are very keen on following the will of Feygard, whatever it may be.”

    - Next → [talion_2](#d-talion_2)

    <span id="d-talion_bless_1"></span>**`talion_bless_1`** Talion: “I am able to bless you with either the Shadow's strength, regeneration, accuracy, or even the blessing of the Shadow guardian.”

    - “I'm interested in the blessing of Shadow strength.” → [talion_bless_str_1](#d-talion_bless_str_1)
    - “I'm interested in the blessing of Shadow regeneration.” → [talion_bless_heal_1](#d-talion_bless_heal_1)
    - “I'm interested in the blessing of Shadow accuracy.” → [talion_bless_acc_1](#d-talion_bless_acc_1)
    - “I'm interested in the Shadow guardian blessing.” → [talion_bless_guard_1](#d-talion_bless_guard_1)
    - “Never mind.” → [talion_0](#d-talion_0)

    <span id="d-tt_talion_10"></span>**`tt_talion_10`** Talion: “Oh, that lovely spell! The Striking Spectacle Shadow spell!”

    - Next → [tt_talion_12](#d-tt_talion_12)

    <span id="d-tt_talion_64"></span>**`tt_talion_64`** Talion: “Indeed? We'll see. I need the following things:”

    - Next → [tt_talion_72](#d-tt_talion_72)

    <span id="d-tt_talion_90"></span>**`tt_talion_90`** Talion: “I don't know anybody with that name. Sorry.”

    - Next → [tt_talion_92](#d-tt_talion_92)

    <span id="d-tt_talion_100"></span>**`tt_talion_100`** Talion: “Behold - Luthor's ring! And this much gold! I didn't expect that you would manage this so soon.” — **effects:** sets stage 280 of [Troubling times](../quests/troubling_times.md#stage-280)

    - “An easy thing for me.” → [tt_talion_110](#d-tt_talion_110)

    <span id="d-tt_talion_300"></span>**`tt_talion_300`** Talion: “What are you talking about?”

    - “The rings. I need them back of course.” → [tt_talion_310](#d-tt_talion_310)

    <span id="d-dds_talion_50"></span>**`dds_talion_50`** Talion: “Just tell me what you need to know.”

    - “Where can I receive blessings of Shadow Sleepiness, Fatigue and Life Drain?” → [dds_talion_60](#d-dds_talion_60)

    <span id="d-dds_talion_80"></span>**`dds_talion_80`** Talion: “That's no problem at all.”

    - “I'm glad about that.” → [dds_talion_82](#d-dds_talion_82)

    <span id="d-talion_cured_2"></span>**`talion_cured_2`** Talion: “Yes. Nasty, aren't they? *chuckle*”

    - Next → [talion_cured_3](#d-talion_cured_3)

    <span id="d-talion_cured_3"></span>**`talion_cured_3`** Talion: “That one worm you spit out, you should make sure you hold on to that. It might be valuable in the future.”

    - “For what?” → [talion_cured_4](#d-talion_cured_4)
    - “OK, I will hold on to it.” → [talion_cured_7](#d-talion_cured_7)
    - “I think I had better put it under my boot.” → [talion_cured_5](#d-talion_cured_5)

    <span id="d-talion_cure_6"></span>**`talion_cure_6`** Talion: “There. Drink this. This should do it.”

    - “Drink the potion.” → [talion_cure_7](#d-talion_cure_7)

    <span id="d-talion_infect_11"></span>**`talion_infect_11`** Talion: “For this particular cure to work, I would need help with gathering four items.”

    - Next → [talion_infect_12](#d-talion_infect_12)

    <span id="d-talion_bone_s"></span>**`talion_bone_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [I have it in me](../quests/maggots.md#stage-40))* → [talion_gather_r](#d-talion_gather_r)
    - branch 2 → [talion_bone_1](#d-talion_bone_1)

    <span id="d-talion_hair_s"></span>**`talion_hair_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 41 of [I have it in me](../quests/maggots.md#stage-41))* → [talion_gather_r](#d-talion_gather_r)
    - branch 2 → [talion_hair_1](#d-talion_hair_1)

    <span id="d-talion_irdegh_s"></span>**`talion_irdegh_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 42 of [I have it in me](../quests/maggots.md#stage-42))* → [talion_gather_r](#d-talion_gather_r)
    - branch 2 → [talion_irdegh_1](#d-talion_irdegh_1)

    <span id="d-talion_vial_s"></span>**`talion_vial_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 43 of [I have it in me](../quests/maggots.md#stage-43))* → [talion_gather_r](#d-talion_gather_r)
    - branch 2 → [talion_vial_1](#d-talion_vial_1)

    <span id="d-talion_infect_5"></span>**`talion_infect_5`** Talion: “A lich of Kazaul eh? Then I am sure that whatever ails you are those cursed rotworms.”

    - Next → [talion_infect_3](#d-talion_infect_3)

    <span id="d-talion_infect_2"></span>**`talion_infect_2`** Talion: “Ah, my old friend Ulirfendor. It's good to hear that he is still alive. Wait! What was that? Rotworms you say, eh?”

    - Next → [talion_infect_3](#d-talion_infect_3)

    <span id="d-talion_infect_4"></span>**`talion_infect_4`** Talion: “It's good that you came to see me. I might be able to help you.”

    - Next → [talion_demon_1](#d-talion_demon_1)

    <span id="d-talion_2"></span>**`talion_2`** Talion: “Normally, this would not be a problem. But Lord Geomyr seems to have something against the Shadow. He will do almost anything to oppose all actions that in some way extend the reach of the Shadow.”

    - Next → [talion_3](#d-talion_3)

    <span id="d-talion_bless_str_1"></span>**`talion_bless_str_1`** Talion: “The blessing of Shadow strength grants you more strength while attacking, thus increasing the amount of damage you do on each hit. I can give you the blessing for 300 gold.”

    - “OK, I'll take it for 300 gold.” *(if pay 300 gold; NOT latest stage of [Shadows](../quests/shadows.md#stage-80) is 80)* → [talion_bless_str_2](#d-talion_bless_str_2)
    - “Never mind, let's go back to those other blessings.” → [talion_bless_1](#d-talion_bless_1)
    - “OK, I'll take it for 300 gold. I need it for Borvis to work an enchantment. He is waiting far to the south.” *(if have 300 gold; latest stage of [Shadows](../quests/shadows.md#stage-80) is 80)* → [dds_talion_10](#d-dds_talion_10)

    <span id="d-talion_bless_heal_1"></span>**`talion_bless_heal_1`** Talion: “The blessing of Shadow regeneration will slowly heal you back if you get hurt. I can give you the blessing for 250 gold.”

    - “OK, I'll take it for 250 gold.” *(if pay 250 gold)* → [talion_bless_heal_2](#d-talion_bless_heal_2)
    - “Never mind, let's go back to those other blessings.” → [talion_bless_1](#d-talion_bless_1)

    <span id="d-talion_bless_acc_1"></span>**`talion_bless_acc_1`** Talion: “The blessing of Shadow accuracy grants you a keen sense of where best to strike your opponent, thus increasing the chance of a successful hit while fighting. I can give you the blessing for 250 gold.”

    - “OK, I'll take it for 250 gold.” *(if pay 250 gold)* → [talion_bless_acc_2](#d-talion_bless_acc_2)
    - “Never mind, let's go back to those other blessings.” → [talion_bless_1](#d-talion_bless_1)

    <span id="d-talion_bless_guard_1"></span>**`talion_bless_guard_1`** Talion: “Ah yes, the blessing of the Shadow guardian. The Shadow protects you in dark places, and keeps you safe where others might not see. I can give you the blessing for 400 gold.”

    - “OK, I'll take it for 400 gold.” *(if pay 400 gold)* → [talion_bless_guard_2](#d-talion_bless_guard_2)
    - “Never mind, let's go back to those other blessings.” → [talion_bless_1](#d-talion_bless_1)

    <span id="d-tt_talion_12"></span>**`tt_talion_12`** Talion: “One of my specials! I just had an opportunity to use it again recently. It went great!”

    - “Why did you do that? People can get hurt!” → [tt_talion_20](#d-tt_talion_20)

    <span id="d-tt_talion_72"></span>**`tt_talion_72`** Talion: “Villain's ring, Troublemaker's ring, Ring of backstabbing, Tears of the Shadow potion. And most important, Luthor's ring. Together with 50,000 gold.” — **effects:** sets stage 80 of [Troubling times](../quests/troubling_times.md#stage-80)

    - “You don't ask for much! Where do I find all that?” → [tt_talion_80](#d-tt_talion_80)
    - “I don't have Troublemaker's ring yet.” *(if NOT carry 1× [Troublemaker's ring](../items/ring_troublemaker.md); reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [tt_talion_74](#d-tt_talion_74)
    - “I don't have the Ring of backstabbing yet.” *(if NOT carry 1× [Ring of backstabbing](../items/ring_backstab.md); reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [tt_talion_74](#d-tt_talion_74)
    - “I don't have the Villain's ring yet.” *(if NOT carry 1× [Villain's ring](../items/ring_villain.md); reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [tt_talion_74](#d-tt_talion_74)
    - “I don't have the Tears of the Shadow yet.” *(if NOT carry 1× [Tears of the Shadow](../items/pot_shadowtear.md); reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [tt_talion_74](#d-tt_talion_74)
    - “I don't have Luthor's ring yet.” *(if NOT carry 1× [Luthor's Ring](../items/ring_luthor.md); reached stage 100 of [Troubling times](../quests/troubling_times.md#stage-100))* → [tt_talion_74](#d-tt_talion_74)
    - “I don't have the 50,000 gold yet.” *(if NOT have 50,000 gold)* → [tt_talion_74](#d-tt_talion_74)
    - “I have everthing other than Luthor's ring” *(if carry 1× [Troublemaker's ring](../items/ring_troublemaker.md); carry 1× [Ring of backstabbing](../items/ring_backstab.md); carry 1× [Villain's ring](../items/ring_villain.md); carry 1× [Tears of the Shadow](../items/pot_shadowtear.md); NOT carry 1× [Luthor's Ring](../items/ring_luthor.md); have 50,000 gold)* → [tt_talion_76](#d-tt_talion_76)
    - “Here's all you have asked for.” *(if hand over 1× [Troublemaker's ring](../items/ring_troublemaker.md); hand over 1× [Ring of backstabbing](../items/ring_backstab.md); hand over 1× [Villain's ring](../items/ring_villain.md); hand over 1× [Tears of the Shadow](../items/pot_shadowtear.md); hand over 1× [Luthor's Ring](../items/ring_luthor.md); pay 50,000 gold)* → [tt_talion_100](#d-tt_talion_100)

    <span id="d-tt_talion_92"></span>**`tt_talion_92`** Talion: “Did you find the things I asked? Especially Luthor's Ring?”

    - “That is hard to get. No one knows where it is.” → [tt_talion_94](#d-tt_talion_94)

    <span id="d-tt_talion_110"></span>**`tt_talion_110`** Talion: “[muttering] With all that gold and rings I could start a new and wealthy life in Nor City. Hmm ...”

    - “You know that I can hear you?” → [tt_talion_112](#d-tt_talion_112)

    <span id="d-tt_talion_310"></span>**`tt_talion_310`** Talion: “Oh no, you don't. And it's not possible.”

    - “What?” → [tt_talion_320](#d-tt_talion_320)

    <span id="d-dds_talion_60"></span>**`dds_talion_60`** Talion: “Why do you need all those? I hope you are not helping the Shadow's enemies get through a Shadow shield!”

    - “No, of course not!” → [dds_talion_62](#d-dds_talion_62)

    <span id="d-dds_talion_82"></span>**`dds_talion_82`** Talion: “It'll just cost you another 300 gold pieces.”

    - “If that's all - here you go.” *(if have 300 gold)* → [dds_talion_20](#d-dds_talion_20)
    - “I don't have that much with me. I'll be back.” *(if NOT have 300 gold)* → *conversation ends*

    <span id="d-talion_cured_4"></span>**`talion_cured_4`** Talion: “Well, you never know. Some people really like ... exotic things.”

    - Next → [talion_cured_7](#d-talion_cured_7)

    <span id="d-talion_cured_7"></span>**`talion_cured_7`** Talion: “Now, I know you must have gone through a lot to get infected with these things. You seem like the experienced type.”

    - Next → [talion_cured_8](#d-talion_cured_8)

    <span id="d-talion_cured_5"></span>**`talion_cured_5`** Talion: “It's your choice of course.”

    - Next → [talion_cured_7](#d-talion_cured_7)

    <span id="d-talion_cure_7"></span>**`talion_cure_7`** Talion: “[The potion smells rancid, but you manage to drink it all down. The pain from the stomach decreases, and you feel one of the rotworms crawling up into your mouth. You quickly spit the worm out into the now empty vial.]” — **effects:** sets stage 50 of [I have it in me](../quests/maggots.md#stage-50), gives [Kazaul rotworm](../items/potion_rotworm.md), applies condition rotworm

    - Next → [talion_cured_1](#d-talion_cured_1)

    <span id="d-talion_infect_12"></span>**`talion_infect_12`** Talion: “Or ... well ... actually, nine items in total, but four different types. Eh ... well, you get the idea.”

    - Next → [talion_infect_13](#d-talion_infect_13)

    <span id="d-talion_gather_r"></span>**`talion_gather_r`** Talion: “No need, you already brought me that before. But thank you anyway.”

    - Next → [talion_gather_s](#d-talion_gather_s)

    <span id="d-talion_bone_1"></span>**`talion_bone_1`** Talion: “Oh, good. Please, give them to me.”

    - “Here you go.” *(if hand over 5× [Bone](../items/bone.md))* → [talion_bone_2](#d-talion_bone_2)
    - “On second thought, I'll be right back.” → *conversation ends*

    <span id="d-talion_hair_1"></span>**`talion_hair_1`** Talion: “Oh, good. Please, give them to me.”

    - “Here you go.” *(if hand over 2× [Animal hair](../items/hair.md))* → [talion_hair_2](#d-talion_hair_2)
    - “On second thought, I'll be right back.” → *conversation ends*

    <span id="d-talion_irdegh_1"></span>**`talion_irdegh_1`** Talion: “Oh, good. Please, give it to me.”

    - “Here you go.” *(if hand over 1× [Irdegh poison gland](../items/irdegh.md))* → [talion_irdegh_2](#d-talion_irdegh_2)
    - “On second thought, I'll be right back.” → *conversation ends*

    <span id="d-talion_vial_1"></span>**`talion_vial_1`** Talion: “Oh, good. Please, give it to me.”

    - “Here you go, one small empty vial.” *(if hand over 1× [Small empty vial](../items/vial_empty1.md))* → [talion_vial_2](#d-talion_vial_2)
    - “Here you go, one empty vial.” *(if hand over 1× [Empty vial](../items/vial_empty2.md))* → [talion_vial_2](#d-talion_vial_2)
    - “On second thought, I'll be right back.” → *conversation ends*

    <span id="d-talion_infect_3"></span>**`talion_infect_3`** Talion: “Nasty things, they are. I have seen people going mad from the stomach pains, and I have seen people being eaten alive from the inside.”

    - “Are you able to help me?” → [talion_infect_4](#d-talion_infect_4)
    - “It's not that bad. I have had worse.” → [talion_infect_4](#d-talion_infect_4)

    <span id="d-talion_demon_1"></span>**`talion_demon_1`** Talion: “Just to be sure, you did kill whatever creature that infected you with this, right?”

    - “Yes, I killed that lich.” *(if reached stage 10 of [The dark protector](../quests/darkprotector.md#stage-10))* → [talion_demon_2](#d-talion_demon_2)
    - “No, I have not killed it yet.” → [talion_demon_3](#d-talion_demon_3)

    <span id="d-talion_3"></span>**`talion_3`** Talion: “Because of this, the people of Loneford are now actively abolishing the thought of the Shadow guiding them through their lives.”

    - Next → [talion_4](#d-talion_4)

    <span id="d-talion_bless_str_2"></span>**`talion_bless_str_2`** Talion: “Very well. *starts chanting*” — **effects:** applies condition shadowbless_str

    - Next → [talion_bless_2](#d-talion_bless_2)

    <span id="d-dds_talion_10"></span>**`dds_talion_10`** Talion: “Oh, it's good that you said that.”

    - Next → [dds_talion_12](#d-dds_talion_12)

    <span id="d-talion_bless_heal_2"></span>**`talion_bless_heal_2`** Talion: “Very well. *starts chanting*” — **effects:** applies condition shadowbless_heal

    - Next → [talion_bless_2](#d-talion_bless_2)

    <span id="d-talion_bless_acc_2"></span>**`talion_bless_acc_2`** Talion: “Very well. *starts chanting*” — **effects:** applies condition shadowbless_acc

    - Next → [talion_bless_2](#d-talion_bless_2)

    <span id="d-talion_bless_guard_2"></span>**`talion_bless_guard_2`** Talion: “Very well. *starts chanting*” — **effects:** applies condition shadowbless_guard

    - Next → [talion_bless_2](#d-talion_bless_2)

    <span id="d-tt_talion_20"></span>**`tt_talion_20`** Talion: “Nonsense! How can it hurt to be more noticeable? It makes one stand out more, makes one more popular.”

    - “Not if you want to be a thief or similar.” → [tt_talion_30](#d-tt_talion_30)

    <span id="d-tt_talion_80"></span>**`tt_talion_80`** Talion: “Check with your thief friends, they should know. All these rings form part of your thievery business.”

    - “Luthor's ring ...” *(if NOT carry 1× [Tears of the Shadow](../items/pot_shadowtear.md))* → [tt_talion_82](#d-tt_talion_82)

    <span id="d-tt_talion_74"></span>**`tt_talion_74`** Talion: “Well, then go and find it.”

    - Next → [tt_talion_75](#d-tt_talion_75)

    <span id="d-tt_talion_76"></span>**`tt_talion_76`** Talion: “Good, that's a start.”

    - “Now I am going to find Luthor's ring.” → [tt_talion_82](#d-tt_talion_82)
    - “I am glad you approve.” → *conversation ends*

    <span id="d-tt_talion_94"></span>**`tt_talion_94`** Talion: “Good thieves don't have to search for the things they want. They know where they are.”

    - “Can't you cast the counterspell without the ring?” → [tt_talion_96](#d-tt_talion_96)

    <span id="d-tt_talion_112"></span>**`tt_talion_112`** Talion: “Eh, well. Now it's time to keep my promise and dispell your friends.”

    - “That sounds better.” → [tt_talion_120](#d-tt_talion_120)

    <span id="d-tt_talion_320"></span>**`tt_talion_320`** Talion: “I said you don't need the rings. Also it's not possible ...” — **effects:** sets stage 290 of [Troubling times](../quests/troubling_times.md#stage-290)

    - “OK, it was just a question. Bye.” → *conversation ends*
    - “I'll show you what's possible ...” → [tt_talion_330](#d-tt_talion_330)

    <span id="d-dds_talion_62"></span>**`dds_talion_62`** Talion: “Then what for? Speak!”

    - “Borvis wants my help in breaking a Shadow shield in the south of Stoutford. He says someone is misusing Shadow powers…” → [dds_talion_70](#d-dds_talion_70)

    <span id="d-dds_talion_20"></span>**`dds_talion_20`** Talion: “Very well. [starts chanting]”

    - Next *(if pay 300 gold)* → [dds_talion_30](#d-dds_talion_30)

    <span id="d-talion_cured_8"></span>**`talion_cured_8`** Talion: “Tell you what, I don't normally offer this to anyone, but you seem like you could use the help.”

    - Next → [talion_cured_9](#d-talion_cured_9)

    <span id="d-talion_infect_13"></span>**`talion_infect_13`** Talion: “Anyway, what you need to bring me is, first and foremost, some more fresh bones. Five bones will do I think. Make sure they are fresh. Any old skeleton will do, but I'd rather take some fresh bones of some nasty animal.”

    - Next → [talion_infect_14](#d-talion_infect_14)

    <span id="d-talion_gather_s"></span>**`talion_gather_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [I have it in me](../quests/maggots.md#stage-40))* → [talion_gather_s2](#d-talion_gather_s2)
    - branch 2 → [talion_infect_31](#d-talion_infect_31)

    <span id="d-talion_bone_2"></span>**`talion_bone_2`** Talion: “Thank you.” — **effects:** sets stage 40 of [I have it in me](../quests/maggots.md#stage-40)

    - Next → [talion_gather_s](#d-talion_gather_s)

    <span id="d-talion_hair_2"></span>**`talion_hair_2`** Talion: “Thank you.” — **effects:** sets stage 41 of [I have it in me](../quests/maggots.md#stage-41)

    - Next → [talion_gather_s](#d-talion_gather_s)

    <span id="d-talion_irdegh_2"></span>**`talion_irdegh_2`** Talion: “Thank you.” — **effects:** sets stage 42 of [I have it in me](../quests/maggots.md#stage-42)

    - Next → [talion_gather_s](#d-talion_gather_s)

    <span id="d-talion_vial_2"></span>**`talion_vial_2`** Talion: “Thank you.” — **effects:** sets stage 43 of [I have it in me](../quests/maggots.md#stage-43)

    - Next → [talion_gather_s](#d-talion_gather_s)

    <span id="d-talion_demon_2"></span>**`talion_demon_2`** Talion: “Good. Then I am able to help you.”

    - Next → [talion_infect_6](#d-talion_infect_6)

    <span id="d-talion_demon_3"></span>**`talion_demon_3`** Talion: “Then you better go take care of that first!”

    - “OK, I will be back once the lich is defeated.” → *conversation ends*

    <span id="d-talion_4"></span>**`talion_4`** Talion: “People around here would rather follow the law of Feygard than follow the old ways.”

    - Next → [talion_5](#d-talion_5)

    <span id="d-talion_bless_2"></span>**`talion_bless_2`** Talion: “There. I hope you will find it useful on your travels.”

    - “Thank you, goodbye.” → *conversation ends*
    - “How about some of those other blessings?” → [talion_bless_1](#d-talion_bless_1)

    <span id="d-dds_talion_12"></span>**`dds_talion_12`** Talion: “Then I have to slightly modify the chant so that it stays fresh and will still work after your long journey.”

    - “Great.” → [dds_talion_20](#d-dds_talion_20)

    <span id="d-tt_talion_30"></span>**`tt_talion_30`** Talion: “Why would these so-called thieves approach you?”

    - “I'm a kid. No one notices me ...” → [tt_talion_40](#d-tt_talion_40)

    <span id="d-tt_talion_82"></span>**`tt_talion_82`** Talion: “Yes, this ring might be a little harder to find. I trust in you.”

    - “Don't you have any idea where it could be?” → [tt_talion_84](#d-tt_talion_84)

    <span id="d-tt_talion_75"></span>**`tt_talion_75`** Talion: “By the way, don't come to me with polished rings. The counterspell works with the unmeddled ones only. Hurry now!”


    <span id="d-tt_talion_96"></span>**`tt_talion_96`** Talion: “No ring - no help, sorry.” — **effects:** sets stage 170 of [Troubling times](../quests/troubling_times.md#stage-170)

    - Next → [tt_talion_98](#d-tt_talion_98)

    <span id="d-tt_talion_120"></span>**`tt_talion_120`** Talion: “[muttering strange words]”

    - Next → [tt_talion_122](#d-tt_talion_122)

    <span id="d-tt_talion_330"></span>**`tt_talion_330`** Talion: “[Hasty] Now here is Luthor's ring. It is the only one that was powerfull enough to survive the spell. The others are broken.” — **effects:** gives 1× [Luthor's Ring](../items/ring_luthor.md), sets stage 300 of [Troubling times](../quests/troubling_times.md#stage-300)

    - “Hmm, thanks.” → *conversation ends*

    <span id="d-dds_talion_70"></span>**`dds_talion_70`** Talion: “Sending a kid to do a priest's job! Isn't Borvis strong enough?”

    - Next → [dds_talion_72](#d-dds_talion_72)

    <span id="d-dds_talion_30"></span>**`dds_talion_30`** Talion: “There. I hope Borvis knows what he is doing.” — **effects:** applies condition shadowbless_str, sets stage 90 of [Shadows](../quests/shadows.md#stage-90)

    - “Thank you. Bye” → *conversation ends*
    - “Thank you. And I need to ask you something.” → [dds_talion_50](#d-dds_talion_50)
    - “Where can I receive blessings of Shadow Sleepiness, Fatigue and Life Drain?” → [dds_talion_40](#d-dds_talion_40)

    <span id="d-talion_cured_9"></span>**`talion_cured_9`** Talion: “Seeing as you managed to pull through all of this, I would be willing to offer you the help of giving you blessings of the Shadow if you want.” — **effects:** sets stage 51 of [I have it in me](../quests/maggots.md#stage-51)

    - “Blessings of the Shadow?” → [talion_cured_10](#d-talion_cured_10)

    <span id="d-talion_infect_14"></span>**`talion_infect_14`** Talion: “Secondly, I will need some animal fur to go with that. Two pieces of animal hair will surely do. I'm sure any old animal fur from the wilderness outside town will do.”

    - Next → [talion_infect_15](#d-talion_infect_15)

    <span id="d-talion_gather_s2"></span>**`talion_gather_s2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 41 of [I have it in me](../quests/maggots.md#stage-41))* → [talion_gather_s3](#d-talion_gather_s3)
    - branch 2 → [talion_infect_31](#d-talion_infect_31)

    <span id="d-talion_infect_31"></span>**`talion_infect_31`** Talion: “There are still some more of those items that I need.”

    - “What was I supposed to collect again?” → [talion_infect_11](#d-talion_infect_11)
    - “I brought five bones for you.” → [talion_bone_s](#d-talion_bone_s)
    - “I brought two pieces of animal hair for you.” → [talion_hair_s](#d-talion_hair_s)
    - “I brought an irdegh poison gland for you.” → [talion_irdegh_s](#d-talion_irdegh_s)
    - “I brought an empty vial for you.” → [talion_vial_s](#d-talion_vial_s)

    <span id="d-talion_infect_6"></span>**`talion_infect_6`** Talion: “However, there is a slight problem. You see, normally my supply of potions and ingredients would be fully stocked. However with this trouble that we have here in Loneford, my supplies are lower than they have ever been before.”

    - Next → [talion_infect_7](#d-talion_infect_7)

    <span id="d-talion_5"></span>**`talion_5`** Talion: “My feeling is that this illness is caused by the Shadow, as punishment to all of us here in Loneford.” — **effects:** sets stage 23 of [Flows through the veins](../quests/loneford.md#stage-23)

    - Next → [loneford_ill_c_1](#d-loneford_ill_c_1)

    <span id="d-tt_talion_40"></span>**`tt_talion_40`** Talion: “That's debatable in your case, but I see the point.”

    - “Thanks! So, why did you do it?” → [tt_talion_50](#d-tt_talion_50)

    <span id="d-tt_talion_84"></span>**`tt_talion_84`** Talion: “No. Ask your thief friends.”

    - “But ...” → [tt_talion_86](#d-tt_talion_86)

    <span id="d-tt_talion_98"></span>**`tt_talion_98`** Talion: “Find it or your friends may have to retire or go into another honest business. He he!”

    - “Very funny.” → [talion_0](#d-talion_0)

    <span id="d-tt_talion_122"></span>**`tt_talion_122`** Talion: “[muttering more strange words]”

    - Next → [tt_talion_124](#d-tt_talion_124)

    <span id="d-dds_talion_72"></span>**`dds_talion_72`** Talion: “Very well. Go to my friend Jolnor for Shadow Sleepiness. Rest you get even in spite of bad dreams - but not permanently, and potion effects don't help.” — **effects:** sets stage 100 of [Shadows](../quests/shadows.md#stage-100)

    - “Right. I got that ... I think.” → [dds_talion_74](#d-dds_talion_74)
    - “Thank you.” → [dds_talion_74](#d-dds_talion_74)

    <span id="d-dds_talion_40"></span>**`dds_talion_40`** Talion: “How about a word of thanks first?”

    - Next → [dds_talion_42](#d-dds_talion_42)

    <span id="d-talion_cured_10"></span>**`talion_cured_10`** Talion: “Yes. Well ... for a fee of course.”

    - “What blessings can you provide?” → [talion_bless_1](#d-talion_bless_1)

    <span id="d-talion_infect_15"></span>**`talion_infect_15`** Talion: “Third, I will need a gland of poison from a creature called the irdegh.”

    - Next → [talion_infect_16](#d-talion_infect_16)

    <span id="d-talion_gather_s3"></span>**`talion_gather_s3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 42 of [I have it in me](../quests/maggots.md#stage-42))* → [talion_gather_s4](#d-talion_gather_s4)
    - branch 2 → [talion_infect_31](#d-talion_infect_31)

    <span id="d-talion_infect_7"></span>**`talion_infect_7`** Talion: “I am not even able to go out and gather new supplies, what with the illness and all.”

    - “Then what can you do?” → [talion_infect_8](#d-talion_infect_8)
    - “Is there anything I can do to help?” → [talion_infect_8](#d-talion_infect_8)
    - “Bah! Then you are useless to me. Guess you should have prepared better before then.” → [talion_infect_9](#d-talion_infect_9)

    <span id="d-loneford_ill_c_1"></span>**`loneford_ill_c_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [loneford_ill_c_2](#d-loneford_ill_c_2)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-tt_talion_50"></span>**`tt_talion_50`** Talion: “Because of the gold! Why else?”

    - Next → [tt_talion_52](#d-tt_talion_52)

    <span id="d-tt_talion_86"></span>**`tt_talion_86`** Talion: “I said no. Go now, child.”


    <span id="d-tt_talion_124"></span>**`tt_talion_124`** Talion: “[muttering even more strange words]”

    - Next → [tt_talion_130](#d-tt_talion_130)

    <span id="d-dds_talion_74"></span>**`dds_talion_74`** Talion: “Ask Jolnor of Vilegard.”


    <span id="d-dds_talion_42"></span>**`dds_talion_42`** Talion: “Oh times, oh customs. These ill-behaved children these days...”

    - “Thank you.” → [dds_talion_44](#d-dds_talion_44)

    <span id="d-talion_infect_16"></span>**`talion_infect_16`** Talion: “Now, I have not seen an irdegh myself, but I hear they are particularly nasty creatures. Venomous like nothing I've heard of.”

    - “OK, one irdegh poison gland. Where can I find one?” → [talion_infect_17](#d-talion_infect_17)
    - “Got it. Anything else?” → [talion_infect_18](#d-talion_infect_18)

    <span id="d-talion_gather_s4"></span>**`talion_gather_s4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 43 of [I have it in me](../quests/maggots.md#stage-43))* → [talion_cure_1](#d-talion_cure_1)
    - branch 2 → [talion_infect_31](#d-talion_infect_31)

    <span id="d-talion_infect_8"></span>**`talion_infect_8`** Talion: “You know what, maybe you can go out and gather some items for me. With your condition, it is important that we hurry as much as we can.”

    - “What would you like me to do?” → [talion_infect_11](#d-talion_infect_11)
    - “Argh! The pains are getting worse! Isn't there anything you can do?” → [talion_infect_10](#d-talion_infect_10)

    <span id="d-talion_infect_9"></span>**`talion_infect_9`** Talion: “Yes, I guess I should have.”


    <span id="d-loneford_ill_c_2"></span>**`loneford_ill_c_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → [loneford_ill_c_3](#d-loneford_ill_c_3)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_n"></span>**`loneford_ill_c_n`** Talion: “That's what I think anyway.”


    <span id="d-tt_talion_52"></span>**`tt_talion_52`** Talion: “Of course I use it for the church ...”

    - “Well, what will it take to remove the spell?” → [tt_talion_60](#d-tt_talion_60)

    <span id="d-tt_talion_130"></span>**`tt_talion_130`** Talion: “Done. Go back to your friends, everything is as it was before.” — **effects:** sets stage 290 of [Troubling times](../quests/troubling_times.md#stage-290)

    - “Great! Thank you.” → [tt_talion_132](#d-tt_talion_132)

    <span id="d-dds_talion_44"></span>**`dds_talion_44`** Talion: “Well, you see - was that really so difficult?”

    - “Hmpf.” → [dds_talion_50](#d-dds_talion_50)

    <span id="d-talion_infect_17"></span>**`talion_infect_17`** Talion: “Some people have talked about seeing some of them far to the east, across the bridges.”

    - “Anything else?” → [talion_infect_18](#d-talion_infect_18)

    <span id="d-talion_infect_18"></span>**`talion_infect_18`** Talion: “Lastly, I would need a clean empty vial to make the potion in. I hear that the potion-maker in Fallhaven has the best vials available.”

    - Next → [talion_infect_19](#d-talion_infect_19)

    <span id="d-talion_cure_1"></span>**`talion_cure_1`** Talion: “That's all I need to cure you. Good work.” — **effects:** sets stage 45 of [I have it in me](../quests/maggots.md#stage-45)

    - Next → [talion_cure_2](#d-talion_cure_2)

    <span id="d-talion_infect_10"></span>**`talion_infect_10`** Talion: “No, unfortunately not. Not with this few supplies I'm sorry.”

    - “Fine. What would you like me to do?” → [talion_infect_11](#d-talion_infect_11)
    - “Bah! Then you are useless to me. Guess you should have prepared better before then.” → [talion_infect_9](#d-talion_infect_9)

    <span id="d-loneford_ill_c_3"></span>**`loneford_ill_c_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23))* → [loneford_ill_c_4](#d-loneford_ill_c_4)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-tt_talion_60"></span>**`tt_talion_60`** Talion: “Around 50,000 gold, of which a large portion will go back to the mysterious Lady Dameni, who had me do the spell. I would need to pacify her, otherwise her toughs will kill me.” — **effects:** sets stage 70 of [Troubling times](../quests/troubling_times.md#stage-70)

    - “50,000 gold! I hope the guild can reimburse me!” → [tt_talion_62](#d-tt_talion_62)

    <span id="d-tt_talion_132"></span>**`tt_talion_132`** Talion: “[to himself] I hope.”


    <span id="d-talion_infect_19"></span>**`talion_infect_19`** Talion: “Bring me these things and I will be able to help you with your ... condition.” — **effects:** sets stage 30 of [I have it in me](../quests/maggots.md#stage-30)

    - “Very well, I will be back shortly.” → *conversation ends*

    <span id="d-talion_cure_2"></span>**`talion_cure_2`** Talion: “Now, let's get this cure started. I just need to grind this ... and mix those ... and...”

    - Next → [talion_cure_3](#d-talion_cure_3)

    <span id="d-loneford_ill_c_4"></span>**`loneford_ill_c_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24))* → [loneford_ill_c_5](#d-loneford_ill_c_5)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-tt_talion_62"></span>**`tt_talion_62`** Talion: “I also need a few more items ...”

    - “Which items?” → [tt_talion_70](#d-tt_talion_70)

    <span id="d-talion_cure_3"></span>**`talion_cure_3`** Talion: “Give me a minute.”

    - Next → [talion_cure_4](#d-talion_cure_4)

    <span id="d-loneford_ill_c_5"></span>**`loneford_ill_c_5`** Talion: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but didn't dare tell me what it was.” — **effects:** sets stage 25 of [Flows through the veins](../quests/loneford.md#stage-25)

    - “Thank you, I will go talk to him.” → *conversation ends*
    - “Great, another drunk that I have to talk to.” → *conversation ends*

    <span id="d-tt_talion_70"></span>**`tt_talion_70`** Talion: “Oh, just a few little things, easy to get.”

    - Next → [tt_talion_72](#d-tt_talion_72)

    <span id="d-talion_cure_4"></span>**`talion_cure_4`** Talion: “[Talion mixes the ground up ingredients together in the vial you brought, with some leaves and berries that he kept with him]”

    - Next → [talion_cure_5](#d-talion_cure_5)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 34 lines changed<br>· text: “Third, I will need a gland of poison from a creature called the Irdeg…” → “Third, I will need a gland of poison from a creature called the irdeg…”<br>· text: “Now, let's get this cure started. I just need to grind this .. and mi…” → “Now, let's get this cure started. I just need to grind this ... and m…” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 36 lines added, 1 line changed |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 15 lines added, 2 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Villain's ring, Troublemaker's ring, Ring of backstabbing, Tears of t…” → “Villain's ring, Troublemaker's ring, Ring of backstabbing, Tears of t…”<br>· text: “Around 50000 gold, of which a large portion will go back to the myste…” → “Around {50000} gold, of which a large portion will go back to the mys…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `talion` |
    | Spawn group | `talion` |
    | Loot table | `shop_talion` |
    | Conversation | `talion` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "talion",
     "name": "Talion",
     "iconID": "monsters_men2:8",
     "monsterClass": "humanoid",
     "spawnGroup": "talion",
     "phraseID": "talion",
     "droplistID": "shop_talion"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=talion.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=talion.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=talion.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=talion.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
