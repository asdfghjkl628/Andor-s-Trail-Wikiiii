# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Yolgen

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Stoutford combat amulet](../items/necklace_stfrd_combat.md) | 100% | 1 |
| [Ring of the protector](../items/ring_protector.md) | 100% | 1 |
| [Ring of damage resistance](../items/ring_dr1.md) | 100% | 1 |

## Found on

- [stoutford_church](../maps/stoutford_church.md)

## Quests

- [Ancient secrets](../quests/flagstone.md): stages 5, 100
- [Rumblings](../quests/rumblings.md): stages 20, 80
- [Search for Andor](../quests/andor.md): stages 85
- [Stoutford's old castle](../quests/stoutford_castle.md): stages 10, 12, 20, 30, 42, 50, 60, 70
- [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md): stages 180, 190

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Yolgen. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/yolgen_0.json" data-npc="Yolgen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (67 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-yolgen_0"></span>**`yolgen_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80))* → [yolgen_initial_0](#d-yolgen_initial_0)
    - Next *(if reached stage 50 of [Rumblings](../quests/rumblings.md#stage-50))* → [yolgen_rumblings50_0](#d-yolgen_rumblings50_0)
    - Next *(if reached stage 20 of [Rumblings](../quests/rumblings.md#stage-20))* → [yolgen_rumblings20_0](#d-yolgen_rumblings20_0)
    - Next *(if reached stage 10 of [Rumblings](../quests/rumblings.md#stage-10))* → [yolgen_rumblings10_0](#d-yolgen_rumblings10_0)
    - Next → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_initial_0"></span>**`yolgen_initial_0`** Yolgen: “Go with the shadow.”

    - “Shadow be with you.” → *conversation ends*
    - “Whatever.” → *conversation ends*
    - “Tahalendor told me that you may have items to trade.” *(if reached stage 23 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-23))* → *shop opens*
    - “What can you tell me about the area around here?” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)
    - “I have dealt with Erwyn's army.” *(if reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70))* → [yolgen_castle_1](#d-yolgen_castle_1)
    - “I cleared Flagstone of an evil demon.” *(if reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60); NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100))* → [yolgen_flagstone_10](#d-yolgen_flagstone_10)
    - “Is there anything I can do to help?” *(if reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180); reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190))* → [yolgen_task_0](#d-yolgen_task_0)
    - “I need some help finding out who is responsible for casting a Shadow spell that causes a person to become noticeable.” *(if reached stage 50 of [Troubling times](../quests/troubling_times.md#stage-50); NOT reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70))* → [tt_yolgen_10](#d-tt_yolgen_10)

    <span id="d-yolgen_rumblings50_0"></span>**`yolgen_rumblings50_0`** Yolgen: “Hello again. Have you found anything about what is causing the noises in the church? It seems they have stopped.”

    - “No. Not yet.” → *conversation ends*
    - “Yes. I think I found the cause.” → [yolgen_rumblings50_1](#d-yolgen_rumblings50_1)
    - “Let us talk about something different.” → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_rumblings20_0"></span>**`yolgen_rumblings20_0`** Yolgen: “Hello again. Have you found anything about what is causing the noises in the church?”

    - “No. Not yet.” → [yolgen_rumblings10_7](#d-yolgen_rumblings10_7)
    - “Let us talk about something different.” → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_rumblings10_0"></span>**`yolgen_rumblings10_0`** Yolgen: “Walk in the shadow kid. I have to apologize for my master, Tahalendor.”

    - “Crazy old geezer... What's wrong with him?” → [yolgen_rumblings10_1](#d-yolgen_rumblings10_1)
    - “Can you explain?” → [yolgen_rumblings10_1](#d-yolgen_rumblings10_1)
    - “Let us talk about something different.” → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_surroundings_0"></span>**`yolgen_surroundings_0`** Yolgen: “Well, to the east, there's Flagstone prison. To the south, there's Mt. Galmore. That's definitely a place that you don't want to go to. To the northwest, we have our railway terminal, and going west beyond that, you come to our border…”

    - “Can you tell me more about Flagstone?” → [yolgen_surroundings_1](#d-yolgen_surroundings_1)
    - “Can you tell me more about Mt. Galmore?” → [yolgen_surroundings_2](#d-yolgen_surroundings_2)
    - “Can you tell me more about the railway terminal northwest of here?” → [yolgen_surroundings_3](#d-yolgen_surroundings_3)
    - “Can you tell me more about Blackwater mountain?” → [yolgen_surroundings_4](#d-yolgen_surroundings_4)
    - “There is something else I wanted to know.” → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_castle_1"></span>**`yolgen_castle_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-40))* → [yolgen_castle_2](#d-yolgen_castle_2)
    - branch 2 *(if reached stage 46 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46))* → [yolgen_castle_1_1a](#d-yolgen_castle_1_1a)
    - branch 3 *(if killed 2× [Erwyn's soldier](../monsters/erwyn_soldier.md))* → [yolgen_castle_1_1b](#d-yolgen_castle_1_1b)
    - branch 4 → [yolgen_castle_1_1c](#d-yolgen_castle_1_1c)

    <span id="d-yolgen_flagstone_10"></span>**`yolgen_flagstone_10`** Yolgen: “Oh that is good news! I am very pleased that the citizens of Stoutford have one thing less to worry about. It is a pity that we didn't send guards to investigate the prison earlier. Then all of this wouldn't have happened. Here, take this…” — **effects:** removes monsters from flagstone4, sets stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100), gives [Gold coins](../items/gold.md)

    - “Thank you kindly. I am happy to help.” → *conversation ends*
    - “Thank you kindly. Shadow be with you.” → *conversation ends*

    <span id="d-yolgen_task_0"></span>**`yolgen_task_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [stoutford_reinforcements (hidden flag)](../quests/stoutford_reinforcements.md#stage-10); reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10))* → [yolgen_task_0_2](#d-yolgen_task_0_2)
    - branch 2 *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10))* → [yolgen_task_0_2](#d-yolgen_task_0_2)
    - branch 3 *(if NOT reached stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5))* → [yolgen_task_0_2](#d-yolgen_task_0_2)
    - branch 4 *(if NOT reached stage 10 of [prim_tunnel (hidden flag)](../quests/prim_tunnel.md#stage-10); reached stage 10 of [not_yet_realized (hidden flag)](../quests/not_yet_realized.md#stage-10))* → [yolgen_task_0_2](#d-yolgen_task_0_2)
    - branch 5 *(if NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100))* → [yolgen_task_0_2_1](#d-yolgen_task_0_2_1)
    - branch 6 *(if NOT reached stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50); NOT reached stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60); NOT reached stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70))* → [yolgen_task_0_2_2](#d-yolgen_task_0_2_2)
    - branch 7 → [yolgen_task_0_1](#d-yolgen_task_0_1)

    <span id="d-tt_yolgen_10"></span>**`tt_yolgen_10`** Yolgen: “I don't understand ... What are you talking about?”

    - “Never mind.” → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_rumblings50_1"></span>**`yolgen_rumblings50_1`** Yolgen: “Great. You should talk to my master. I told him you were not who he thought you were.” — **effects:** sets stage 80 of [Rumblings](../quests/rumblings.md#stage-80)

    - Next → [yolgen_initial_0](#d-yolgen_initial_0)

    <span id="d-yolgen_rumblings10_7"></span>**`yolgen_rumblings10_7`** Yolgen: “Shadow be with you.”


    <span id="d-yolgen_rumblings10_1"></span>**`yolgen_rumblings10_1`** Yolgen: “My master is wise and old, but his sight is not as sharp as it once was. He took you for someone else.”

    - “Who?” → [yolgen_rumblings10_2](#d-yolgen_rumblings10_2)

    <span id="d-yolgen_surroundings_1"></span>**`yolgen_surroundings_1`** Yolgen: “Flagstone Prison was built four hundred years ago by house Gorland of Stoutford, and was used until the Noble Wars, when the house was vanquished by its enemies. They mostly used it to detain people that were worshipping the "old gods".” — **effects:** sets stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190)

    - Next → [yolgen_surroundings_1a](#d-yolgen_surroundings_1a)

    <span id="d-yolgen_surroundings_2"></span>**`yolgen_surroundings_2`** Yolgen: “Mt. Galmore? It has been our bane for a long time. Garthan I, the founder of Aewhata Kingdom, ordered the excavation of the mountain for gold and gems 430 years ago.”

    - Next → [yolgen_surroundings_2a](#d-yolgen_surroundings_2a)

    <span id="d-yolgen_surroundings_3"></span>**`yolgen_surroundings_3`** Yolgen: “As I said, we've got our railway terminal to the west.”

    - Next → [yolgen_surroundings_3a](#d-yolgen_surroundings_3a)

    <span id="d-yolgen_surroundings_4"></span>**`yolgen_surroundings_4`** Yolgen: “Ah. Blackwater mountain. I will try to keep a long story short. We used to trade food and tools with Prim and the miners from Elm mine, and get loads of iron ingots in return. We shipped them on to Nor City and Feygard and prospered from…”

    - Next → [yolgen_surroundings_5](#d-yolgen_surroundings_5)

    <span id="d-yolgen_castle_2"></span>**`yolgen_castle_2`** Yolgen: “That is unbelievable!”

    - “Well, it was a tough fight, but I managed to slay Lord Erwyn himself.” → [yolgen_castle_2a](#d-yolgen_castle_2a)
    - “The undead are no match for me.” → [yolgen_castle_2a](#d-yolgen_castle_2a)

    <span id="d-yolgen_castle_1_1a"></span>**`yolgen_castle_1_1a`** Yolgen: “Let me see... OK, you killed all of the undead knights and soldiers who had worn Lord Erwyn's tattered banner.” — **effects:** sets stage 20 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-20)

    - Next → [yolgen_castle_1_2](#d-yolgen_castle_1_2)

    <span id="d-yolgen_castle_1_1b"></span>**`yolgen_castle_1_1b`** Yolgen: “Let me see... You already killed some of Erwyn's undead knights and soldiers - if killed is the correct word for undead. But there are some still around.”

    - “OK, I will go and look for the rest.” → *conversation ends*
    - “How do you know?” → [yolgen_castle_1_1d](#d-yolgen_castle_1_1d)

    <span id="d-yolgen_castle_1_1c"></span>**`yolgen_castle_1_1c`** Yolgen: “Let me see... No, the castle is still crowded with undead soldiers.”

    - “How do you know?” → [yolgen_castle_1_1d](#d-yolgen_castle_1_1d)

    <span id="d-yolgen_task_0_2"></span>**`yolgen_task_0_2`** Yolgen: “Well, you look a bit young. But I guess we could still make use of you in these dark times. Let me think about some tasks I can offer you.”

    - “What about the undead in the castle?” *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10); reached stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180))* → [yolgen_castle_0](#d-yolgen_castle_0)
    - “What about Flagstone prison?” *(if NOT reached stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5); NOT reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60); NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100); reached stage 190 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-190))* → [yolgen_flagstone_0](#d-yolgen_flagstone_0)
    - “OK, bye.” → *conversation ends*

    <span id="d-yolgen_task_0_2_1"></span>**`yolgen_task_0_2_1`** Yolgen: “Could you help with Flagstone?”

    - “OK. I will go to the prison.” *(if NOT reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60))* → *conversation ends*
    - “I cleared Flagstone of an evil demon.” *(if reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60))* → [yolgen_flagstone_10](#d-yolgen_flagstone_10)

    <span id="d-yolgen_task_0_2_2"></span>**`yolgen_task_0_2_2`** Yolgen: “Can you clear the castle?”

    - “Sure. All the undead will soon be dead!” → *conversation ends*

    <span id="d-yolgen_task_0_1"></span>**`yolgen_task_0_1`** Yolgen: “Well, you already were of great help. Thank you again!”


    <span id="d-yolgen_rumblings10_2"></span>**`yolgen_rumblings10_2`** Yolgen: “To his credit, I have to admit you do look a bit like him. I don't know his name.” — **effects:** sets stage 85 of [Search for Andor](../quests/andor.md#stage-85)

    - “That must be my brother Andor!” → [yolgen_rumblings10_3](#d-yolgen_rumblings10_3)
    - “Go on.” → [yolgen_rumblings10_3](#d-yolgen_rumblings10_3)

    <span id="d-yolgen_surroundings_1a"></span>**`yolgen_surroundings_1a`** Yolgen: “That dreadful place has been left abandoned ever since. Recently, however, undead have started pouring out of the prison, and we had to send guards to keep them away from the road.”

    - “I took care of that.” *(if reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100))* → [yolgen_surroundings_flagstone_4](#d-yolgen_surroundings_flagstone_4)
    - “Can I help you with Flagstone?” *(if NOT reached stage 70 of [Ancient secrets](../quests/flagstone.md#stage-70); NOT reached stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5); NOT reached stage 100 of [Ancient secrets](../quests/flagstone.md#stage-100))* → [yolgen_flagstone_0](#d-yolgen_flagstone_0)
    - “Is there anything I could help you with?” → [yolgen_task_0](#d-yolgen_task_0)
    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)

    <span id="d-yolgen_surroundings_2a"></span>**`yolgen_surroundings_2a`** Yolgen: “Local lore says that fortifications were built to protect against monster attacks, and an enormous network of mine tunnels was dug under the mountain. They found rich ore veins and the mine flourished.”

    - Next → [yolgen_surroundings_2b](#d-yolgen_surroundings_2b)

    <span id="d-yolgen_surroundings_3a"></span>**`yolgen_surroundings_3a`** Yolgen: “We used to trade food and tools with Prim and the miners from Elm mine and get loads of iron ingots in return. We shipped them on to Nor City and Feygard and prospered from the trade.”

    - Next → [yolgen_surroundings_3b](#d-yolgen_surroundings_3b)

    <span id="d-yolgen_surroundings_5"></span>**`yolgen_surroundings_5`** Yolgen: “A few months ago, everything changed. A sudden violent earthquake shook the mountain and our railway tunnel to Prim collapsed.”

    - Next → [yolgen_surroundings_5a](#d-yolgen_surroundings_5a)

    <span id="d-yolgen_castle_2a"></span>**`yolgen_castle_2a`** Yolgen: “Did you search him?”

    - “Sure. I found this ring among his remains.” *(if carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md))* → [yolgen_castle_3](#d-yolgen_castle_3)
    - “[Lie] He had nothing of any worth on him.” → [yolgen_castle_10](#d-yolgen_castle_10)

    <span id="d-yolgen_castle_1_2"></span>**`yolgen_castle_1_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Karth the Unbowed](../monsters/erwyn_commander.md))* → [yolgen_castle_1_2a](#d-yolgen_castle_1_2a)
    - branch 2 → [yolgen_castle_1_2b](#d-yolgen_castle_1_2b)

    <span id="d-yolgen_castle_1_1d"></span>**`yolgen_castle_1_1d`** Yolgen: “I just know. Don't try to fool me.”


    <span id="d-yolgen_castle_0"></span>**`yolgen_castle_0`** Yolgen: “We do have a problem. Our soldiers usually guard the castle gate to Mt. Galmore to keep the monsters away from the Kingdom.”

    - Next → [yolgen_castle_0a](#d-yolgen_castle_0a)

    <span id="d-yolgen_flagstone_0"></span>**`yolgen_flagstone_0`** Yolgen: “If you could help with Flagstone, it would take a big burden off us.” — **effects:** sets stage 5 of [Ancient secrets](../quests/flagstone.md#stage-5)

    - “I have been inside Flagstone, but I will go back and find out more.” *(if reached stage 20 of [Ancient secrets](../quests/flagstone.md#stage-20); NOT reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60))* → *conversation ends*
    - “OK, I will take a look.” → *conversation ends*
    - “Maybe.” → *conversation ends*

    <span id="d-yolgen_rumblings10_3"></span>**`yolgen_rumblings10_3`** Yolgen: “He came around here not long ago, with a shady looking travelling companion. He stayed a couple of days from what I heard. Since then, we have been hearing frequent rumbles in the church, coming from underground.”

    - Next → [yolgen_rumblings10_4](#d-yolgen_rumblings10_4)

    <span id="d-yolgen_surroundings_flagstone_4"></span>**`yolgen_surroundings_flagstone_4`** Yolgen: “Yes, thanks to you my friend, we don't need to worry about the undead anymore.”

    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)
    - “Where do you think they came from?” → [yolgen_1](#d-yolgen_1)

    <span id="d-yolgen_surroundings_2b"></span>**`yolgen_surroundings_2b`** Yolgen: “But their success didn't last long. It is said that after a few years unspeakable horrors overwhelmed the knights and miners of the King, and the mine has been abandoned ever since.”

    - Next → [yolgen_surroundings_2c](#d-yolgen_surroundings_2c)

    <span id="d-yolgen_surroundings_3b"></span>**`yolgen_surroundings_3b`** Yolgen: “Further to the west, there's the border outpost next to Blackwater River. Anyway, from what I have heard there's nothing but bogs, marshes and grasslands west of the river, along with a few native tribes.”

    - “Is there anything I could do to help?” → [yolgen_task_0](#d-yolgen_task_0)
    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)

    <span id="d-yolgen_surroundings_5a"></span>**`yolgen_surroundings_5a`** Yolgen: “At almost the same time, those Gornaud beasts attacked us, and with all the trouble we're having we haven't been able to restore the tunnel yet.”

    - Next → [yolgen_surroundings_5b](#d-yolgen_surroundings_5b)

    <span id="d-yolgen_castle_3"></span>**`yolgen_castle_3`** Yolgen: “I am very pleased to hear this. A ring you say? Let me take a look.” — **effects:** sets stage 42 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-42)

    - Next → [yolgen_castle_4](#d-yolgen_castle_4)

    <span id="d-yolgen_castle_10"></span>**`yolgen_castle_10`** Yolgen: “He was there without any of his ... special items? Did you look thoroughly?”

    - “[Lie] Yes, but I found nothing worth having.” → [yolgen_castle_11](#d-yolgen_castle_11)
    - “I found a strange glowing ring. But I prefer to keep it. You have enough such toys, I am sure.” → [yolgen_castle_12](#d-yolgen_castle_12)
    - “Yes, indeed, look at this ring.” *(if carry 1× [Lord Erwyn's ring](../items/erwyn_ring.md))* → [yolgen_castle_4](#d-yolgen_castle_4)

    <span id="d-yolgen_castle_1_2a"></span>**`yolgen_castle_1_2a`** Yolgen: “And you slew Lord Erwyn's commander.” — **effects:** sets stage 30 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-30)

    - Next → [yolgen_castle_1_3](#d-yolgen_castle_1_3)

    <span id="d-yolgen_castle_1_2b"></span>**`yolgen_castle_1_2b`** Yolgen: “But their commander is still around.”

    - “OK, I will go and look for him.” → *conversation ends*

    <span id="d-yolgen_castle_0a"></span>**`yolgen_castle_0a`** Yolgen: “However, five days ago, the undead knights of Lord Erwyn started to rise from their grave. I have no idea why this happened. We haven't been able to recapture the castle yet. I would ask you to rid us of this plague.”

    - “It sounds more like a task for the guards. I'll go and talk to the captain of the guard.” → *conversation ends*
    - “No problem. They are already as good as dead.” → [yolgen_castle_0_1](#d-yolgen_castle_0_1)
    - “Hmm, I wonder where they came from.” → [yolgen_1](#d-yolgen_1)
    - “No thanks. I think that's way over my head.” → *conversation ends*

    <span id="d-yolgen_rumblings10_4"></span>**`yolgen_rumblings10_4`** Yolgen: “It can be so loud as to make the whole church shake. It has even damaged the walls and the roof.”

    - Next → [yolgen_rumblings10_5](#d-yolgen_rumblings10_5)

    <span id="d-yolgen_1"></span>**`yolgen_1`** Yolgen: “Oh, that is a long story my friend. This town has existed for ages and it used to be a prosperous and well visited outpost on the border of the Aewhata Kingdom. We used to trade with Fallhaven and Prim.”

    - Next → [yolgen_1a](#d-yolgen_1a)

    <span id="d-yolgen_surroundings_2c"></span>**`yolgen_surroundings_2c`** Yolgen: “However, recently more and more of the most foul monsters are coming from the mountain and we have to fend them off. There are rumors that the mines are once gain being worked. If true, that is very foolish, and dangerous. With the rise…” — **effects:** sets stage 180 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-180)

    - “That sounds dreadful. Can I help you with the castle?” *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10))* → [yolgen_castle_0](#d-yolgen_castle_0)
    - “Is there anything I could do to help?” → [yolgen_task_0](#d-yolgen_task_0)
    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)

    <span id="d-yolgen_surroundings_5b"></span>**`yolgen_surroundings_5b`** Yolgen: “There hasn't been any contact with Prim since then, so we no longer have any trade with them. That means there are also fewer travellers coming from Fallhaven and Nor City. It's a shame.”

    - “Is there anything I can help with?” → [yolgen_task_0](#d-yolgen_task_0)
    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)

    <span id="d-yolgen_castle_4"></span>**`yolgen_castle_4`** Yolgen: “Hmm. This looks most interesting. I suspected something like this. It is certainly some magical item and seems to have the powers to reanimate the dead. I am indeed very grateful that you brought this ring to me. We should destroy it once…” — **effects:** sets stage 42 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-42)

    - “Sounds fine to me. Anything for the safety of the people of Stoutford.” *(if hand over 1× [Lord Erwyn's ring](../items/erwyn_ring.md))* → [yolgen_castle_5](#d-yolgen_castle_5)
    - “I prefer to keep it.” → [yolgen_castle_12](#d-yolgen_castle_12)

    <span id="d-yolgen_castle_11"></span>**`yolgen_castle_11`** Yolgen: “If you say so. I suspect Lord Erwyn had a ring, and if you find it you must bring it to me. It is dangerous.” — **effects:** sets stage 70 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-70)

    - “Thank you for the warning. I wonder who had owned the ring before Erwyn.” → *conversation ends*

    <span id="d-yolgen_castle_12"></span>**`yolgen_castle_12`** Yolgen: “You're insane! Lord Erwyn's ring is dangerous. It must be destroyed!”

    - “No, I don't think so. I wonder who had owned the ring before Erwyn?” → [yolgen_castle_13](#d-yolgen_castle_13)
    - “You are probably right. Here is the ring.” *(if hand over 1× [Lord Erwyn's ring](../items/erwyn_ring.md))* → [yolgen_castle_5](#d-yolgen_castle_5)

    <span id="d-yolgen_castle_1_3"></span>**`yolgen_castle_1_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Lord Erwyn](../monsters/erwyn2.md))* → [yolgen_castle_1_3a](#d-yolgen_castle_1_3a)
    - branch 2 → [yolgen_castle_1_3b](#d-yolgen_castle_1_3b)

    <span id="d-yolgen_castle_0_1"></span>**`yolgen_castle_0_1`** Yolgen: “Before you leave, go to Tahalendor. He might give you something that helps against undead.” — **effects:** sets stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10), sets stage 12 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-12)

    - “Thank you.” → *conversation ends*
    - “There was something else I wanted to ask you about.” → [yolgen_surroundings_0](#d-yolgen_surroundings_0)

    <span id="d-yolgen_rumblings10_5"></span>**`yolgen_rumblings10_5`** Yolgen: “This church is the refuge for all the villagers when monsters attack. We are really worried now.” — **effects:** sets stage 20 of [Rumblings](../quests/rumblings.md#stage-20)

    - “I can't believe Andor has anything to do with this. Can you tell me more?” → [yolgen_rumblings10_6](#d-yolgen_rumblings10_6)
    - “Is there anything I can do to help?” → [yolgen_rumblings10_6](#d-yolgen_rumblings10_6)
    - “Whatever... It's none of my business.” → *conversation ends*

    <span id="d-yolgen_1a"></span>**`yolgen_1a`** Yolgen: “Stoutford used to be the seat of Lord Erwyn of house Gorland. But during the Noble Wars 17 years ago, everything changed.”

    - “The Noble Wars?” → [yolgen_2](#d-yolgen_2)

    <span id="d-yolgen_castle_5"></span>**`yolgen_castle_5`** [Dummy NPC](../monsters/none.md): “Yolgen puts the ring on his altar and chants a spell. Suddenly the altar seems to be getting darker and darker and then the ring cracks.”

    - Next → [yolgen_castle_6](#d-yolgen_castle_6)

    <span id="d-yolgen_castle_13"></span>**`yolgen_castle_13`** Yolgen: “Do not play with ancient forces that are beyond your power.” — **effects:** sets stage 60 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-60)

    - “Now I'm even more curious who the ring belonged to. Farewell, Yolgen.” → *conversation ends*

    <span id="d-yolgen_castle_1_3a"></span>**`yolgen_castle_1_3a`** Yolgen: “And you slew Lord Erwyn himself.”

    - “An unfriendly guy, yes.” → [yolgen_castle_2](#d-yolgen_castle_2)

    <span id="d-yolgen_castle_1_3b"></span>**`yolgen_castle_1_3b`** Yolgen: “But Lord Erwyn is still around.”

    - “OK, I will go and look for him.” → *conversation ends*

    <span id="d-yolgen_rumblings10_6"></span>**`yolgen_rumblings10_6`** Yolgen: “I told you all I know. Maybe others in town have seen him.”

    - “Thank you for your help.” → [yolgen_rumblings10_7](#d-yolgen_rumblings10_7)
    - “Guess I'll have to look into it.” → [yolgen_rumblings10_7](#d-yolgen_rumblings10_7)

    <span id="d-yolgen_2"></span>**`yolgen_2`** Yolgen: “Well, the Noble Wars were one of the darkest periods of our history. They lasted only 3 years but brought great misery to most of the area.”

    - Next → [yolgen_2a](#d-yolgen_2a)

    <span id="d-yolgen_castle_6"></span>**`yolgen_castle_6`** [Yolgen](../monsters/yolgen.md): “That is it. The ring is destroyed. I wonder where it came from. Maybe from the depths of Mt. Galmore, or some mischievous traveller put it on Lord Erwyn's remains? Anyway, my friend, I and the people of Stoutford are most grateful.” — **effects:** sets stage 50 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-50)

    - “Thank you.” → *conversation ends*
    - “Thank you. Shadow be with you.” → *conversation ends*

    <span id="d-yolgen_2a"></span>**`yolgen_2a`** Yolgen: “When our great King Luthor died and left the throne with no heir the three mighty lords of the land soon enough began fighting over the title as successor. They were Lord Erwyn of Stoutford, Lord Geomyr of Feygard, who used to be the…”

    - Next → [yolgen_3](#d-yolgen_3)

    <span id="d-yolgen_3"></span>**`yolgen_3`** Yolgen: “While Erwyn and Emeric fought to capture the central area, Lord Geomyr waited for the right moment and crushed his enemies with his great army. He has ruled the Kingdom ever since with an iron hand.”

    - “Why do you say iron hand?” → [yolgen_4](#d-yolgen_4)

    <span id="d-yolgen_4"></span>**`yolgen_4`** Yolgen: “Well, he has installed garrisons in pretty much every village, introduced a tax system and now he even wants to prohibit the worship of the mighty Shadow! This is outrageous!”

    - “Thanks.” → [yolgen_initial_0](#d-yolgen_initial_0)
    - “And bonemeal is forbidden.” → [yolgen_4a](#d-yolgen_4a)
    - “I will clear the castle of undead for you.” *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10))* → [yolgen_castle_0_1](#d-yolgen_castle_0_1)

    <span id="d-yolgen_4a"></span>**`yolgen_4a`** Yolgen: “Yes, incredible! Although kids like you should not play with such things.”

    - “Hmph.” → [yolgen_initial_0](#d-yolgen_initial_0)
    - “I will clear the castle of undead for you.” *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10))* → [yolgen_castle_0_1](#d-yolgen_castle_0_1)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 66 lines added |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line changed<br>· text: “Flagstone Prison was built four hundred years ago by house Gorland of…” → “Flagstone Prison was built four hundred years ago by house Gorland of…” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line changed<br>· text: “However, recently more and more of the most foul monsters are coming …” → “However, recently more and more of the most foul monsters are coming …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yolgen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yolgen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yolgen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yolgen.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `yolgen` · Data from v0.8.18</small>
