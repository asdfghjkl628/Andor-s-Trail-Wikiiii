---
description: "Minarra is a non-player character (NPC) in Andor's Trail, found in Houseatcrossroads 4. Shopkeeper; starts Flows through the veins, The path is clear to me."
---

# ![](../assets/icons/monsters/monsters_rltiles1_86.png){ .sprite } Minarra

**Where to find Minarra:** [Houseatcrossroads 4](../maps/houseatcrossroads4.md#pin-npc-minarra)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_86.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper; starts [Flows through the veins](../quests/loneford.md), [The path is clear to me](../quests/rogorn.md) |
| **Found in** | Houseatcrossroads 4 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Challenger's iron sword](../items/sword_challengers.md) | 100% | 1 |
| [Steel sword](../items/steelsword1.md) | 100% | 1 |
| [Defender's blade](../items/sword_defenders.md) | 100% | 1 |
| [Balanced steel sword](../items/sword_balanced_steel.md) | 100% | 1 |
| [Two-handed iron claymore](../items/clmr_irn2.md) | 100% | 1 |
| [Superior wooden shield](../items/shield5.md) | 100% | 1 |
| [Wooden defender](../items/shield_wooden_defender.md) | 100% | 1 |
| [Superior chain mail](../items/armour_superior_chain.md) | 100% | 1 |
| [Champion's chain mail](../items/armour_chain_champ.md) | 100% | 1 |
| [Lightweight chainmail](../items/ltbdy_chmail.md) | 100% | 1 |
| [Sturdy leather cuirass](../items/ltbdy_lthr.md) | 100% | 1 |
| [Guard's gloves](../items/gloves_guards.md) | 100% | 1 |
| [Heavy plated gloves](../items/hglv_plat2.md) | 100% | 1 |
| [Reinforced steel gloves](../items/hglv_stl.md) | 100% | 1 |
| [Defender's boots](../items/boots_defender.md) | 100% | 1 |
| [Challenger's ring](../items/ring_challenger.md) | 100% | 1 |
| [Ring of block](../items/ring_block.md) | 100% | 1 |
| [Polished ring of block](../items/ring_block2.md) | 100% | 1 |
| [Iron halberd](../items/halberd_iron.md) | 100% | 1 |

## Quests

- [Flows through the veins](../quests/loneford.md): stages 10, 11, 21
- [The path is clear to me](../quests/rogorn.md): stages 10, 20, 21, 50, 55, 60

## Dialogue simulator

Set your quest stages and items, then talk to Minarra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/minarra.json" data-npc="Minarra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (45 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-minarra"></span>**`minarra`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The path is clear to me](../quests/rogorn.md#stage-60))* → [minarra_completed_1](#d-minarra_completed_1)
    - branch 2 *(if reached stage 55 of [The path is clear to me](../quests/rogorn.md#stage-55))* → [minarra_completing_1](#d-minarra_completing_1)
    - branch 3 *(if reached stage 50 of [The path is clear to me](../quests/rogorn.md#stage-50))* → [minarra_completing_1](#d-minarra_completing_1)
    - branch 4 *(if reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20))* → [minarra_look_1](#d-minarra_look_1)
    - branch 5 *(if reached stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10))* → [minarra_return_1](#d-minarra_return_1)
    - branch 6 → [minarra_first_1](#d-minarra_first_1)

    <span id="d-minarra_completed_1"></span>**`minarra_completed_1`** Minarra: “Thank you for helping me investigate the men earlier.”

    - “Do you have anything to trade?” → [minarra_trade_1](#d-minarra_trade_1)
    - “You must have a good view of the surroundings up here. Have you seen anything interesting lately?” → [minarra_first_2](#d-minarra_first_2)

    <span id="d-minarra_completing_1"></span>**`minarra_completing_1`** Minarra: “Thank you for helping me investigate this matter.” — **effects:** sets stage 60 of [The path is clear to me](../quests/rogorn.md#stage-60)

    - “Do you have anything to trade?” → [minarra_trade_1](#d-minarra_trade_1)
    - “You must have a good view of the surroundings up here. Have you seen anything interesting lately?” → [minarra_first_2](#d-minarra_first_2)

    <span id="d-minarra_look_1"></span>**`minarra_look_1`** Minarra: “You return. Did you find those men that we talked about?”

    - “I am still looking for them.” → [minarra_look_2](#d-minarra_look_2)
    - “Yes, I killed them and recovered the three pieces of the painting.” *(if reached stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40); hand over 3× [Piece of painting](../items/rogorn_qitem.md))* → [minarra_look_3](#d-minarra_look_3)
    - “I travelled west and found a travelling group of men, but they did not match the men you described.” *(if reached stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45))* → [minarra_look_5](#d-minarra_look_5)
    - “I'd rather talk about the troubles in Loneford that you had mentioned.” *(if NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [cr_loneford_st_1](#d-cr_loneford_st_1)

    <span id="d-minarra_return_1"></span>**`minarra_return_1`** Minarra: “You return. Was there something else you wanted?”

    - “Can you tell me again about those men you saw?” → [minarra_story_1](#d-minarra_story_1)
    - “Do you have anything to trade?” → [minarra_trade_rej](#d-minarra_trade_rej)
    - “What do you do up here?” → [minarra_first_5](#d-minarra_first_5)

    <span id="d-minarra_first_1"></span>**`minarra_first_1`** Minarra: “Hello there. Can I help you?”

    - “You seem to have a lot of equipment around here. Do you have anything to trade?” → [minarra_trade_rej](#d-minarra_trade_rej)
    - “What do you do up here?” → [minarra_first_5](#d-minarra_first_5)
    - “You must have a good view of the surroundings up here. Have you seen anything interesting lately?” → [minarra_first_2](#d-minarra_first_2)

    <span id="d-minarra_trade_1"></span>**`minarra_trade_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 18 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-18))* → [minarra_trade_2](#d-minarra_trade_2)
    - branch 2 → [minarra_trade_rej](#d-minarra_trade_rej)

    <span id="d-minarra_first_2"></span>**`minarra_first_2`** Minarra: “Mostly, I see the travellers on the Duleian road from and to Feygard here.”

    - Next → [minarra_first_3](#d-minarra_first_3)

    <span id="d-minarra_look_2"></span>**`minarra_look_2`** Minarra: “Good. Return to me as soon as you have anything to report. We would really like to recover those three pieces of the painting they stole.”


    <span id="d-minarra_look_3"></span>**`minarra_look_3`** Minarra: “That is excellent news indeed! I knew that we could trust you.” — **effects:** sets stage 50 of [The path is clear to me](../quests/rogorn.md#stage-50)

    - Next → [minarra_look_4](#d-minarra_look_4)

    <span id="d-minarra_look_5"></span>**`minarra_look_5`** Minarra: “Are you sure that they were not the ones? I have a keen eyesight, that's why I am up here. I was sure that they matched the description of the men.”

    - Next → [minarra_look_6](#d-minarra_look_6)

    <span id="d-cr_loneford_st_1"></span>**`cr_loneford_st_1`** Minarra: “Didn't you hear? They have all gotten ill.”

    - Next → [cr_loneford_st_2](#d-cr_loneford_st_2)

    <span id="d-minarra_story_1"></span>**`minarra_story_1`** Minarra: “I saw a band of rough looking men travelling up the Duleian road. Usually, a band of rough looking men is not something that's worth getting all excited about.”

    - Next → [minarra_story_2](#d-minarra_story_2)

    <span id="d-minarra_trade_rej"></span>**`minarra_trade_rej`** Minarra: “I might, but you would have to clear it with Gandoren downstairs. We don't trade with just anyone.”


    <span id="d-minarra_first_5"></span>**`minarra_first_5`** Minarra: “I handle the equipment storage for us guards here in the Crossroads guardhouse, and I keep a lookout of the surrounding areas.”

    - “Do you have anything to trade?” → [minarra_trade_rej](#d-minarra_trade_rej)
    - “Have you seen anything interesting lately?” → [minarra_first_2](#d-minarra_first_2)

    <span id="d-minarra_trade_2"></span>**`minarra_trade_2`** Minarra: “Sure, take a look.”

    - Next → *shop opens*

    <span id="d-minarra_first_3"></span>**`minarra_first_3`** Minarra: “Recently however, there have been a lot of movements to and from Loneford. I guess it is because of the problems they have been having up there.”

    - Next → [minarra_first_4_s](#d-minarra_first_4_s)

    <span id="d-minarra_look_4"></span>**`minarra_look_4`** Minarra: “Your services to Feygard will be greatly appreciated.”

    - Next → [minarra_completing_1](#d-minarra_completing_1)

    <span id="d-minarra_look_6"></span>**`minarra_look_6`** Minarra: “I guess I will have to take your word for it.” — **effects:** sets stage 55 of [The path is clear to me](../quests/rogorn.md#stage-55)

    - Next → [minarra_completing_1](#d-minarra_completing_1)

    <span id="d-cr_loneford_st_2"></span>**`cr_loneford_st_2`** Minarra: “It all started a few days ago. As the story goes, someone found one of the farmers passed out in one of the fields, completely white faced and shivering.”

    - Next → [cr_loneford_st_3](#d-cr_loneford_st_3)

    <span id="d-minarra_story_2"></span>**`minarra_story_2`** Minarra: “But these men matched the description of some people that are wanted by the Feygard patrol.”

    - Next → [minarra_story_3](#d-minarra_story_3)

    <span id="d-minarra_first_4_s"></span>**`minarra_first_4_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The path is clear to me](../quests/rogorn.md#stage-60))* → [minarra_first_4_1](#d-minarra_first_4_1)
    - branch 2 → [minarra_first_4](#d-minarra_first_4)

    <span id="d-cr_loneford_st_3"></span>**`cr_loneford_st_3`** Minarra: “A few days later, the same symptoms started to show on a lot more people.”

    - Next → [cr_loneford_st_4](#d-cr_loneford_st_4)

    <span id="d-minarra_story_3"></span>**`minarra_story_3`** Minarra: “If I saw correctly, these men were the band of rogues led by a man called Rogorn, that we are looking to apprehend for several ruthless cases of murder and theft.”

    - Next → [minarra_story_4](#d-minarra_story_4)

    <span id="d-minarra_first_4_1"></span>**`minarra_first_4_1`** Minarra: “Some farm animals today as well.”

    - “You mentioned the Duleian road, what's that?” → [minarra_first_6_1](#d-minarra_first_6_1)
    - “You mentioned some problems in Loneford, what problems were you referring to?” → [cr_loneford_st_1](#d-cr_loneford_st_1)

    <span id="d-minarra_first_4"></span>**`minarra_first_4`** Minarra: “I did see something very interesting yesterday though.”

    - “What was that?” → [minarra_story_1](#d-minarra_story_1)
    - “You mentioned the Duleian road, what's that?” → [minarra_first_6](#d-minarra_first_6)
    - “You mentioned some problems in Loneford, what problems were you referring to?” → [cr_loneford_st_1](#d-cr_loneford_st_1)
    - “Never mind that, I wanted to ask you what your duty is up here?” → [minarra_first_5](#d-minarra_first_5)

    <span id="d-cr_loneford_st_4"></span>**`cr_loneford_st_4`** Minarra: “Then, all people showed the symptoms in one way or another.”

    - Next → [cr_loneford_st_5](#d-cr_loneford_st_5)

    <span id="d-minarra_story_4"></span>**`minarra_story_4`** Minarra: “Their leader, Rogorn, is a particularly savage man according to the reports from Feygard that I have read.”

    - Next → [minarra_story_5](#d-minarra_story_5)

    <span id="d-minarra_first_6_1"></span>**`minarra_first_6_1`** Minarra: “See this wide road that goes outside this guardhouse? That's the Duleian road. It goes all the way from the glorious city of Feygard up in the northwest down to the wretched Nor City in the southeast.”

    - “You mentioned some problems in Loneford, what problems are that?” → [cr_loneford_st_1](#d-cr_loneford_st_1)

    <span id="d-minarra_first_6"></span>**`minarra_first_6`** Minarra: “See this wide road that goes outside this guardhouse? That's the Duleian road. It goes all the way from the glorious city of Feygard up in the northwest down to the wretched Nor City in the southeast.”

    - “You mentioned some problems in Loneford, what problems are that?” → [cr_loneford_st_1](#d-cr_loneford_st_1)
    - “I wanted to ask you what your duty is up here?” → [minarra_first_5](#d-minarra_first_5)

    <span id="d-cr_loneford_st_5"></span>**`cr_loneford_st_5`** Minarra: “Some old people even died.”

    - Next → [cr_loneford_st_6](#d-cr_loneford_st_6)

    <span id="d-minarra_story_5"></span>**`minarra_story_5`** Minarra: “Now, usually, we would go out searching for them, to verify that the men I saw were indeed these men. However, now with the trouble up in Loneford, we cannot afford to spare any guards other than to guarding Loneford.”

    - Next → [minarra_story_6](#d-minarra_story_6)

    <span id="d-cr_loneford_st_6"></span>**`cr_loneford_st_6`** Minarra: “Everyone started investigating what could be the cause. Currently, the cause is still unknown.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [cr_loneford_st_7](#d-cr_loneford_st_7)

    <span id="d-minarra_story_6"></span>**`minarra_story_6`** Minarra: “I am sure that those were the men. If we were to catch and kill them, the people of Feygard would be much safer.” — **effects:** sets stage 10 of [The path is clear to me](../quests/rogorn.md#stage-10)

    - “I could go look for them if you want.” → [minarra_story_8](#d-minarra_story_8)
    - “Well, good luck with that.” → [minarra_story_7](#d-minarra_story_7)

    <span id="d-cr_loneford_st_7"></span>**`cr_loneford_st_7`** Minarra: “Luckily, now Feygard has sent patrols up there to help guard the village at least. The people are still suffering though.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)

    - Next → [cr_loneford_st_8](#d-cr_loneford_st_8)

    <span id="d-minarra_story_8"></span>**`minarra_story_8`** Minarra: “Hey, that's a great idea. Are you sure you are up to it though? The people of Feygard would indeed be grateful if you were to find them.”

    - Next → [minarra_story_9](#d-minarra_story_9)

    <span id="d-minarra_story_7"></span>**`minarra_story_7`** Minarra: “Thank you. Good luck yourself. Now, if you will excuse me, I need to keep my eyes on the road.”


    <span id="d-cr_loneford_st_8"></span>**`cr_loneford_st_8`** Minarra: “Me, I am certain that this is the work of those savages from Nor City somehow. They probably sabotaged something up there.”

    - Next → [cr_loneford_st_9](#d-cr_loneford_st_9)

    <span id="d-minarra_story_9"></span>**`minarra_story_9`** Minarra: “Anyway, I saw them travelling the road west of here. You know that road that leads to Carn Tower? That's the last I saw of them. You might want to follow that road and see if you can spot them.”

    - Next → [minarra_story_10](#d-minarra_story_10)

    <span id="d-cr_loneford_st_9"></span>**`cr_loneford_st_9`** Minarra: “What do they call it, the 'Shadow'? They are willing to do almost anything to upset the law and order around here.”

    - Next → [cr_loneford_st_10](#d-cr_loneford_st_10)

    <span id="d-minarra_story_10"></span>**`minarra_story_10`** Minarra: “They have stolen three pieces of a very valuable painting from Feygard, from the report that I have read. For their crimes and the savageness of their way, they are wanted dead by the Feygard patrol.” — **effects:** sets stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20)

    - “I will be back once they are dead. Anything else?” → [minarra_story_11](#d-minarra_story_11)

    <span id="d-cr_loneford_st_10"></span>**`cr_loneford_st_10`** Minarra: “I tell you. Savages - that's what they are. No respect for the laws or authority.” — **effects:** sets stage 21 of [Flows through the veins](../quests/loneford.md#stage-21)


    <span id="d-minarra_story_11"></span>**`minarra_story_11`** Minarra: “Yes, I should also tell you that they most likely will try to persuade you into believing their story.”

    - Next → [minarra_story_12](#d-minarra_story_12)

    <span id="d-minarra_story_12"></span>**`minarra_story_12`** Minarra: “In particular, their leader, Rogorn, is a well known villain by Feygard. Nothing he says should be trusted.”

    - Next → [minarra_story_13](#d-minarra_story_13)

    <span id="d-minarra_story_13"></span>**`minarra_story_13`** Minarra: “I urge you not to listen to their lies. Their crimes must be punished in order to uphold the law.” — **effects:** sets stage 21 of [The path is clear to me](../quests/rogorn.md#stage-21)

    - “I will return once the task is done.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `minarra` |
    | Type (wiki) | NPC |
    | Spawn group | `minarra` |
    | Loot table | `shop_minarra` |
    | Conversation | `minarra` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:86` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "minarra",
     "name": "Minarra",
     "iconID": "monsters_rltiles1:86",
     "monsterClass": "humanoid",
     "spawnGroup": "minarra",
     "phraseID": "minarra",
     "droplistID": "shop_minarra"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=minarra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=minarra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=minarra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=minarra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
