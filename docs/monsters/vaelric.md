# ![](../assets/icons/monsters/monsters_tometik7_12.png){ .sprite } Vaelric

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik7_12.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `vaelric` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | galmore_17_house |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Vaelric's elixir of vitality](../items/vaelric_pot_health.md) | 100% | 5 to 9 |
| [Vaelric's purging wash](../items/vaelric_purging_wash.md) | 100% | 1 to 2 |
| [Burn ointment](../items/burn_ointment.md) | 50% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_17_house](../maps/galmore_17_house.md) | – | 1 | – |


## Quests

- [Restless in the grave](../quests/mg_restless_grave.md): stages 20, 63, 70, 80, 95, 97, 115, 120
- [Search for Andor](../quests/andor.md): stages 125, 999
- [The swamp healer](../quests/swamp_healer.md): stages 10, 30
- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stages 59

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Vaelric. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/vaelric_selector.json" data-npc="Vaelric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (68 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-vaelric_selector"></span>**`vaelric_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 125 of [Search for Andor](../quests/andor.md#stage-125))* → [vaelric_andor_10](#d-vaelric_andor_10)
    - branch 2 *(if NOT reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10))* → [vaelric_alone_10](#d-vaelric_alone_10)
    - branch 3 *(if latest stage of [The swamp healer](../quests/swamp_healer.md#stage-10) is 10)* → [vaelric_need_to_kill_creature_10](#d-vaelric_need_to_kill_creature_10)
    - branch 4 *(if latest stage of [The swamp healer](../quests/swamp_healer.md#stage-20) is 20)* → [vaelric_creature_killed_5](#d-vaelric_creature_killed_5)
    - branch 5 *(if reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); NOT reached stage 59 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59))* → [vaelric_creature_talk_leech_10](#d-vaelric_creature_talk_leech_10)
    - branch 6 *(if reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30); carry 1× [Corrupted swamp core](../items/corrupted_swamp_core.md))* → [vaelric_creature_killed_70](#d-vaelric_creature_killed_70)
    - branch 7 *(if reached stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30))* → [vaelric_met](#d-vaelric_met)

    <span id="d-vaelric_andor_10"></span>**`vaelric_andor_10`** Vaelric: “Step lightly, wanderer. The swamp doesn't take kindly to strangers, and neither do I. What brings you to my domain?”

    - “I'm searching for someone, my brother, Andor. He looks like...” → [vaelric_andor_20](#d-vaelric_andor_20)

    <span id="d-vaelric_alone_10"></span>**`vaelric_alone_10`** Vaelric: “Step lightly, wanderer. The swamp doesn't take kindly to just anyone, and neither do I. Why are you before me?”

    - “Why are you living out here alone?” → [vaelric_alone_25](#d-vaelric_alone_25)

    <span id="d-vaelric_need_to_kill_creature_10"></span>**`vaelric_need_to_kill_creature_10`** Vaelric: “Why are you still here? Go kill that massive, venomous, and ravenous creature for me, then we will talk!”


    <span id="d-vaelric_creature_killed_5"></span>**`vaelric_creature_killed_5`** Vaelric: “Have you killed the creature that threatens my way of life?”

    - “Yes, and here, I have this thing that proves it. [shows the 'Corrupted swamp core' to Vaelric]” *(if carry 1× [Corrupted swamp core](../items/corrupted_swamp_core.md))* → [vaelric_creature_killed_10](#d-vaelric_creature_killed_10)
    - “Yes, but I can't prove it. I will return with proof.” *(if NOT carry 1× [Corrupted swamp core](../items/corrupted_swamp_core.md))* → *conversation ends*

    <span id="d-vaelric_creature_talk_leech_10"></span>**`vaelric_creature_talk_leech_10`** Vaelric: “Yes?”

    - “You mentioned leeches earlier. What did you mean by that?” → [vaelric_creature_killed_20](#d-vaelric_creature_killed_20)

    <span id="d-vaelric_creature_killed_70"></span>**`vaelric_creature_killed_70`** Vaelric: “By the way, I'll take that 'Corrupted swamp core' now.”

    - “Oh, yeah, sure. I don't need that thing.” *(if hand over 1× [Corrupted swamp core](../items/corrupted_swamp_core.md))* → *conversation ends*

    <span id="d-vaelric_met"></span>**`vaelric_met`** Vaelric: “So, you've returned. Tell me, do the leeches whisper their secrets to you yet? Or are you still grasping at the edges of what this swamp has to offer?”

    - “You stated that if I helped you kill that venomous creature that you would tell more about Andor.” → [vaelric_met_10](#d-vaelric_met_10)
    - “That graveyard, the one directly south of here, who were those people?” *(if reached stage 5 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-5); NOT reached stage 60 of [Restless in the grave](../quests/mg_restless_grave.md#stage-60))* → [vaelric_graveyard_10](#d-vaelric_graveyard_10)
    - “Actually, I am here to give you an update on that graveyard exploration you sent me on.” *(if reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65); NOT reached stage 80 of [Restless in the grave](../quests/mg_restless_grave.md#stage-80))* → [mg_lie_to_vaelric_10](#d-mg_lie_to_vaelric_10)
    - “I spoke to a ghost in the Galmore encampment. His name is Eryndor...” *(if reached stage 60 of [Restless in the grave](../quests/mg_restless_grave.md#stage-60); NOT reached stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70); NOT reached stage 65 of [Restless in the grave](../quests/mg_restless_grave.md#stage-65))* → [mg_vaelric_story_10](#d-mg_vaelric_story_10)
    - “No, that's old news. Try and keep up, won't you? I'm here to collect my reward?” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-90) is 90)* → [mg_vaelric_reward_10](#d-mg_vaelric_reward_10)
    - “No, that's old news. Try and keep up, won't you? I'm here to inform you that I've defeted Eryndor's spirit.” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-111) is 111)* → [mg_vaelric_defeated_eryndor_10](#d-mg_vaelric_defeated_eryndor_10)
    - “What do I need to give you in order for you to make those Insectbane tonics? I want some now.” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-95) is 95)* → [mg_vaelric_reward_40](#d-mg_vaelric_reward_40)
    - “Can we talk about the Insectbane tonic?” *(if reached stage 97 of [Restless in the grave](../quests/mg_restless_grave.md#stage-97))* → [mg_vaelric_reward_selector](#d-mg_vaelric_reward_selector)
    - “I would like to see your other potions for sale.” *(if reached stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115))* → *shop opens*

    <span id="d-vaelric_andor_20"></span>**`vaelric_andor_20`** Vaelric: “Ah, the one with fire in his eyes and fear in his heart. He came here seeking knowledge, though knowledge often demands a price. Are you here to pay it as well?”

    - “What did he want from you?” → [vaelric_andor_22](#d-vaelric_andor_22)

    <span id="d-vaelric_alone_25"></span>**`vaelric_alone_25`** Vaelric: “Once, I was a celebrated healer. They called me a miracle worker for curing the incurable. My methods were...unconventional. Leeches, parasitic creatures, even plants most would call poisonous. I used whatever the swamp could offer.”

    - “What happened?” → [vaelric_alone_28](#d-vaelric_alone_28)

    <span id="d-vaelric_creature_killed_10"></span>**`vaelric_creature_killed_10`** Vaelric: “You've proven resourceful. Perhaps you are worthy of the knowledge I carry. The swamp holds more than muck and mire, and so do the creatures that call it home.”

    - “You mentioned leeches earlier. What did you mean by that?” → [vaelric_creature_killed_20](#d-vaelric_creature_killed_20)

    <span id="d-vaelric_creature_killed_20"></span>**`vaelric_creature_killed_20`** Vaelric: “Leeches are simple creatures, but they hold incredible power. With the right knowledge, they can purge poison, stop bleeding, and heal wounds that no salve can touch. Few have the courage to learn their secrets.”

    - “Can you teach me?” → [vaelric_creature_killed_30](#d-vaelric_creature_killed_30)

    <span id="d-vaelric_met_10"></span>**`vaelric_met_10`** Vaelric: “No, no, no. I said "if you want my aid, you'll need to earn it", and indeed you did receive my aid as I taught you about the leeches.”


    <span id="d-vaelric_graveyard_10"></span>**`vaelric_graveyard_10`** Vaelric: “Oh, those people? They are nobody.”

    - “Really? "Nobody" you say? Nobody is a "nobody".” → [vaelric_graveyard_20](#d-vaelric_graveyard_20)

    <span id="d-mg_lie_to_vaelric_10"></span>**`mg_lie_to_vaelric_10`** Vaelric: “And?”

    - “I wasn't able to find any clues surrounding the grave site. Is there something you're not telling me?” → [mg_lie_to_vaelric_20](#d-mg_lie_to_vaelric_20)

    <span id="d-mg_vaelric_story_10"></span>**`mg_vaelric_story_10`** [Dummy NPC](../monsters/none.md): “Vaelric's expression darkens, his fingers tightening around his staff. He turns away for a moment, exhaling slowly before speaking.”

    - “He says you treated him once, but you buried him alive. That's why he haunts you. He wants his ring back, or the…” → [mg_vaelric_story_20](#d-mg_vaelric_story_20)
    - “Please tell me more about Eryndor.” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-63) is 63)* → [mg_vaelric_story_50](#d-mg_vaelric_story_50)

    <span id="d-mg_vaelric_reward_10"></span>**`mg_vaelric_reward_10`** Vaelric: “You did it? You were able to help me? You have prevented the future hauntings?”

    - “Yes. Hence my being here with my hand out.” → [mg_vaelric_reward_20](#d-mg_vaelric_reward_20)

    <span id="d-mg_vaelric_defeated_eryndor_10"></span>**`mg_vaelric_defeated_eryndor_10`** Vaelric: “So, it is done? You struck him down, ended his torment by force?”

    - Next → [mg_vaelric_defeated_eryndor_15](#d-mg_vaelric_defeated_eryndor_15)

    <span id="d-mg_vaelric_reward_40"></span>**`mg_vaelric_reward_40`** Vaelric: “But such a remedy does not come cheaply. If you wish for me to prepare this tonic, you must gather the necessary ingredients yourself. Here is what I require: Five Duskbloom flowers. These rare blossoms can be found in the deepest parts…” — **effects:** sets stage 97 of [Restless in the grave](../quests/mg_restless_grave.md#stage-97), gives 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md)

    - “Great, more work for me.” → [mg_vaelric_reward_50](#d-mg_vaelric_reward_50)

    <span id="d-mg_vaelric_reward_selector"></span>**`mg_vaelric_reward_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT have 4,800 gold)* → [mg_vaelric_reward_Not_enough_gold](#d-mg_vaelric_reward_Not_enough_gold)
    - branch 2 *(if carry 5× [Duskbloom](../items/duskbloom_flower.md); carry 10× [Pondslime extract](../items/pondslime_extract.md); carry 5× [Mosquito proboscis](../items/mosquito_proboscis.md); reached stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115); have 4,800 gold)* → [mg_vaelric_buy_insectbance_10](#d-mg_vaelric_buy_insectbance_10)
    - branch 3 *(if NOT reached stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115); carry 5× [Duskbloom](../items/duskbloom_flower.md); carry 10× [Pondslime extract](../items/pondslime_extract.md); carry 5× [Mosquito proboscis](../items/mosquito_proboscis.md); carry 1× [Mudfiend goo](../items/mudfiend.md); have 4,800 gold)* → [mg_vaelric_reward_60](#d-mg_vaelric_reward_60)
    - Next *(if reached stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115); carry 0× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md); NOT reached stage 18 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-18))* → [mg_vaelric_reward_45](#d-mg_vaelric_reward_45)
    - branch 5 → [mg_vaelric_reward_missing_ing_10](#d-mg_vaelric_reward_missing_ing_10)

    <span id="d-vaelric_andor_22"></span>**`vaelric_andor_22`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 999 of [Search for Andor](../quests/andor.md#stage-999), sets stage 125 of [Search for Andor](../quests/andor.md#stage-125)

    - branch 1 → [vaelric_andor_30](#d-vaelric_andor_30)

    <span id="d-vaelric_alone_28"></span>**`vaelric_alone_28`** Vaelric: “Innovation often breeds fear. When a Laumwill noble entrusted me with his life, I used every method I knew to save him. But he died under my care, and the courts called it murder. The Laumwills made certain there was no place for me among…”

    - “And so you fled here?” → [vaelric_alone_30](#d-vaelric_alone_30)

    <span id="d-vaelric_creature_killed_30"></span>**`vaelric_creature_killed_30`** Vaelric: “I don't waste my time on fools, but you've proven yourself. Watch closely.”

    - Next → [vaelric_creature_killed_narrator](#d-vaelric_creature_killed_narrator)

    <span id="d-vaelric_graveyard_20"></span>**`vaelric_graveyard_20`** Vaelric: “Well, one or two of them may have been those that sought my aid and it was too late for them. The others? Most likely unfortunate Galmore miners who lost their lives under false promises of riches.”

    - “I see. Thank you for explaining this.” → *conversation ends*
    - “I noticed that one of the graves looks to have been dug-up in the not-so-distant past.” → [vaelric_graveyard_30](#d-vaelric_graveyard_30)

    <span id="d-mg_lie_to_vaelric_20"></span>**`mg_lie_to_vaelric_20`** Vaelric: “No, just a suspicion I had. In any event, thanks for looking into it for me. Good luck on your search for Andor.” — **effects:** sets stage 80 of [Restless in the grave](../quests/mg_restless_grave.md#stage-80)


    <span id="d-mg_vaelric_story_20"></span>**`mg_vaelric_story_20`** [Vaelric](../monsters/vaelric.md): “Eryndor... Yes, I remember. He came to me alone, desperate, barely able to stand. His condition was severe, far beyond anything my tinctures and poultices could mend. I did everything I knew. I bled out the sickness, cooled his fever,…”

    - Next → [mg_vaelric_story_30](#d-mg_vaelric_story_30)

    <span id="d-mg_vaelric_story_50"></span>**`mg_vaelric_story_50`** [Dummy NPC](../monsters/none.md): “His jaw tightens, regret flashing in his eyes.”

    - Next → [mg_vaelric_story_60](#d-mg_vaelric_story_60)

    <span id="d-mg_vaelric_reward_20"></span>**`mg_vaelric_reward_20`** Vaelric: “Well, let me start by saying that you have done me a great service, and for that, I will offer you something few others could. I am no merchant, but I do have remedies, ones you will not find elsewhere. One in particular may prove…”

    - Next → [mg_vaelric_reward_30](#d-mg_vaelric_reward_30)

    <span id="d-mg_vaelric_defeated_eryndor_15"></span>**`mg_vaelric_defeated_eryndor_15`** [Dummy NPC](../monsters/none.md): “He exhales sharply, shaking his head.”

    - Next → [mg_vaelric_defeated_eryndor_20](#d-mg_vaelric_defeated_eryndor_20)

    <span id="d-mg_vaelric_reward_50"></span>**`mg_vaelric_reward_50`** Vaelric: “Bring me these, and I shall prepare ten vials of the tonic for you. But understand this: my craft is no charity. If you seek to replenish your supply, you must pay the price. Four hundred and eighty gold per vial. A steep price, perhaps,…”


    <span id="d-mg_vaelric_reward_Not_enough_gold"></span>**`mg_vaelric_reward_Not_enough_gold`** Vaelric: “You see, I have to make ten tonics at a time and because I refuse to waste any of them, you must buy all ten at a cost of 4,800 gold. Do you have the gold?”

    - “No.” → *conversation ends*

    <span id="d-mg_vaelric_buy_insectbance_10"></span>**`mg_vaelric_buy_insectbance_10`** Vaelric: “I'll take all of the ingredients and your 4,800 gold now and I will mix you up a batch of ten tonics”

    - “Here, take them, please.” *(if pay 4,800 gold; hand over 10× [Pondslime extract](../items/pondslime_extract.md); hand over 5× [Duskbloom](../items/duskbloom_flower.md); hand over 5× [Mosquito proboscis](../items/mosquito_proboscis.md))* → [mg_vaelric_reward_70](#d-mg_vaelric_reward_70)

    <span id="d-mg_vaelric_reward_60"></span>**`mg_vaelric_reward_60`** Vaelric: “I'll take all of the ingredients and your 4,800 gold now and I will mix you up a batch of ten tonics” — **effects:** sets stage 115 of [Restless in the grave](../quests/mg_restless_grave.md#stage-115)

    - “Here, take them, please.” *(if hand over 5× [Duskbloom](../items/duskbloom_flower.md); hand over 5× [Mosquito proboscis](../items/mosquito_proboscis.md); hand over 10× [Pondslime extract](../items/pondslime_extract.md); hand over 1× [Mudfiend goo](../items/mudfiend.md); pay 4,800 gold)* → [mg_vaelric_reward_70](#d-mg_vaelric_reward_70)

    <span id="d-mg_vaelric_reward_45"></span>**`mg_vaelric_reward_45`** Vaelric: “I require: Five Duskbloom flowers. These rare blossoms can be found in the deepest parts of the swamp, but the creatures there tend to be attracted to them. Their properties are delicate, so bring them fresh. Five Mosquito proboscises.…” — **effects:** gives 10× [Vaelric's empty bottle](../items/vaelrics_empty_bottle.md)


    <span id="d-mg_vaelric_reward_missing_ing_10"></span>**`mg_vaelric_reward_missing_ing_10`** Vaelric: “You don't have what I require in order to make them.”

    - “I don't?” → [mg_vaelric_reward_missing_ing_20](#d-mg_vaelric_reward_missing_ing_20)

    <span id="d-vaelric_andor_30"></span>**`vaelric_andor_30`** Vaelric: “What every ambitious fool wants: power and mastery over forces that should be left alone. Your brother was in a hurry when he left, clutching what he came for. You might ask yourself why.” — **effects:** sets stage 999 of [Search for Andor](../quests/andor.md#stage-999)

    - “Why are you living out here alone?” → [vaelric_alone_25](#d-vaelric_alone_25)

    <span id="d-vaelric_alone_30"></span>**`vaelric_alone_30`** Vaelric: “You ask for much considering you are someone who has given me nothing in return. If you want my aid, you'll need to earn it. A creature stalks my property, not an ordinary beast but one corrupted by the same darkness that haunts this…”

    - “What kind of creature?” → [vaelric_alone_40](#d-vaelric_alone_40)

    <span id="d-vaelric_creature_killed_narrator"></span>**`vaelric_creature_killed_narrator`** [Dummy NPC](../monsters/none.md): “Vaelric produces a jar filled with wriggling leeches and demonstrates their use on a wounded arm.”

    - Next → [vaelric_creature_killed_40](#d-vaelric_creature_killed_40)

    <span id="d-vaelric_graveyard_30"></span>**`vaelric_graveyard_30`** Vaelric: “What?! Which one?”

    - “The northwest one near the river.” → [vaelric_restless_grave_10](#d-vaelric_restless_grave_10)

    <span id="d-mg_vaelric_story_30"></span>**`mg_vaelric_story_30`** [Dummy NPC](../monsters/none.md): “He rubs his temple, his voice quieter now.”

    - Next → [mg_vaelric_story_40](#d-mg_vaelric_story_40)

    <span id="d-mg_vaelric_story_60"></span>**`mg_vaelric_story_60`** [Vaelric](../monsters/vaelric.md): “But I was wrong. I was wrong. Somehow, he still lived. I don't know if it was some illness that mimicked death or if I simply failed to see the life still in him. Either way, my hands put him in that grave, and now his suffering is on me.”

    - Next → [mg_vaelric_story_70](#d-mg_vaelric_story_70)

    <span id="d-mg_vaelric_reward_30"></span>**`mg_vaelric_reward_30`** Vaelric: “This tonic does more than ease a fever or numb the pain of a bite. It eliminates the infection entirely. If you have already fallen victim to the Insect contagion poison, one dose will purge it from your body. But more than that, it…” — **effects:** sets stage 95 of [Restless in the grave](../quests/mg_restless_grave.md#stage-95)

    - Next → [mg_vaelric_reward_40](#d-mg_vaelric_reward_40)

    <span id="d-mg_vaelric_defeated_eryndor_20"></span>**`mg_vaelric_defeated_eryndor_20`** [Vaelric](../monsters/vaelric.md): “I suppose I should have expected as much.”

    - Next → [mg_vaelric_defeated_eryndor_30](#d-mg_vaelric_defeated_eryndor_30)

    <span id="d-mg_vaelric_reward_70"></span>**`mg_vaelric_reward_70`** Vaelric: “Here you go, ten Insectbane tonics.” — **effects:** gives 10× [Insectbane tonic](../items/insectbane_tonic.md), clears stage 18 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-18)

    - Next → [mg_vaelric_other_potions_10](#d-mg_vaelric_other_potions_10)

    <span id="d-mg_vaelric_reward_missing_ing_20"></span>**`mg_vaelric_reward_missing_ing_20`** Vaelric: “No, you don't. I already told you, if you wish for me to prepare this tonic, you must gather the necessary ingredients yourself. Here is what I require: Five Duskbloom flowers. These rare blossoms can be found in the deepest parts of the…”


    <span id="d-vaelric_alone_40"></span>**`vaelric_alone_40`** Vaelric: “A swamp creature, but far from the kind you'd expect to see. This one is massive, venomous, and ravenous. It's draining the life from my medicinal pools. Strength alone won't save you. You'll need to learn the ways of the swamp.” — **effects:** sets stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10), spawns monsters on galmore_28


    <span id="d-vaelric_creature_killed_40"></span>**`vaelric_creature_killed_40`** [Vaelric](../monsters/vaelric.md): “See how the leech attaches itself? It draws out the bad humors, cleansing the blood. Placement is everything. Here, take this.” — **effects:** sets stage 30 of [The swamp healer](../quests/swamp_healer.md#stage-30)

    - “[Extend my hand and take the leech.]” *(if NOT reached stage 59 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59))* → [vaelric_creature_killed_narrator_2](#d-vaelric_creature_killed_narrator_2)
    - “[Extend my hand and take the leech.]” *(if reached stage 59 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59))* → [vaelric_creature_killed_50](#d-vaelric_creature_killed_50)

    <span id="d-vaelric_restless_grave_10"></span>**`vaelric_restless_grave_10`** [Dummy NPC](../monsters/none.md): “Vaelric pauses, his expression tense as if piecing something together.”

    - Next → [vaelric_restless_grave_11](#d-vaelric_restless_grave_11)

    <span id="d-mg_vaelric_story_40"></span>**`mg_vaelric_story_40`** [Vaelric](../monsters/vaelric.md): “I had no choice but to lay him to rest. There was no kin to claim him, no priest to see to his rites. So I carried him to the graveyard myself, dug the earth with my own hands, and gave him what peace I could. It was the right thing to…” — **effects:** sets stage 63 of [Restless in the grave](../quests/mg_restless_grave.md#stage-63)

    - Next → [mg_vaelric_story_50](#d-mg_vaelric_story_50)

    <span id="d-mg_vaelric_story_70"></span>**`mg_vaelric_story_70`** [Dummy NPC](../monsters/none.md): “He hesitates, then steps toward a cabinet, opening a drawer with a sigh.”

    - Next → [mg_vaelric_story_80](#d-mg_vaelric_story_80)

    <span id="d-mg_vaelric_defeated_eryndor_30"></span>**`mg_vaelric_defeated_eryndor_30`** [Dummy NPC](../monsters/none.md): “His gaze lingers on you, his expression hard to read. Somewhere between frustration and resignation.”

    - Next → [mg_vaelric_defeated_eryndor_40](#d-mg_vaelric_defeated_eryndor_40)

    <span id="d-mg_vaelric_other_potions_10"></span>**`mg_vaelric_other_potions_10`** Vaelric: “I also have other potions for sale. Would you like to take a look?”

    - “Of course.” → *shop opens*
    - “No thanks.” → *conversation ends*

    <span id="d-vaelric_creature_killed_narrator_2"></span>**`vaelric_creature_killed_narrator_2`** [Dummy NPC](../monsters/none.md): “Vaelric hands you a leech.” — **effects:** gives 1× [Leech](../items/leech_usable.md), sets stage 59 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-59)

    - Next → [vaelric_creature_killed_50](#d-vaelric_creature_killed_50)

    <span id="d-vaelric_creature_killed_50"></span>**`vaelric_creature_killed_50`** [Vaelric](../monsters/vaelric.md): “Don't underestimate them. In skilled hands, they are as effective as any blade or potion. Use them wisely.”

    - “Thank you. Is there anything else I should know?” → [vaelric_creature_killed_60](#d-vaelric_creature_killed_60)

    <span id="d-vaelric_restless_grave_11"></span>**`vaelric_restless_grave_11`** [Vaelric](../monsters/vaelric.md): “That's... unsettling. If what you say is true, we need to understand what happened there. Something doesn't sit right with this. Please go back to the graveyard and search for clues.”

    - “No, I don't think so. Not this time. I'm tired of helping the pathetic with their problems.” *(if NOT reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20))* → [vaelric_restless_grave_end](#d-vaelric_restless_grave_end)
    - “OK, but this better be worth my time.” *(if NOT reached stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20))* → [vaelric_restless_grave_15](#d-vaelric_restless_grave_15)
    - “Actually, I found some clues already.” *(if carry 1× [Broken bell](../items/mg_broken_bell.md); carry 1× [Mysterious music box](../items/mg_music_box.md))* → [vaelric_restless_grave_found_clues_10](#d-vaelric_restless_grave_found_clues_10)
    - “I found this bell in the graveyard. [Show Vaelric]” *(if carry 1× [Broken bell](../items/mg_broken_bell.md); NOT carry 1× [Mysterious music box](../items/mg_music_box.md))* → [vaelric_restless_grave_found_clue_10](#d-vaelric_restless_grave_found_clue_10)
    - “I found this music box in the graveyard. [Show Vaelric]” *(if NOT carry 1× [Broken bell](../items/mg_broken_bell.md); carry 1× [Mysterious music box](../items/mg_music_box.md))* → [vaelric_restless_grave_found_clue_10](#d-vaelric_restless_grave_found_clue_10)

    <span id="d-mg_vaelric_story_80"></span>**`mg_vaelric_story_80`** [Vaelric](../monsters/vaelric.md): “If his spirit will rest with this ring, take it. If that will end this curse, then let it be done.” — **effects:** sets stage 70 of [Restless in the grave](../quests/mg_restless_grave.md#stage-70), gives 1× [Cursed ring of focus](../items/cursed_ring_focus.md)


    <span id="d-mg_vaelric_defeated_eryndor_40"></span>**`mg_vaelric_defeated_eryndor_40`** [Vaelric](../monsters/vaelric.md): “And what of the hauntings? Is it over?”

    - Next → [mg_vaelric_defeated_eryndor_50](#d-mg_vaelric_defeated_eryndor_50)

    <span id="d-vaelric_creature_killed_60"></span>**`vaelric_creature_killed_60`** Vaelric: “Yes. Don't waste them on minor cuts or trifling ailments. Save them for when they're truly needed. The swamp still has more to teach you, if you are willing to learn.”

    - Next → [vaelric_creature_killed_70](#d-vaelric_creature_killed_70)

    <span id="d-vaelric_restless_grave_end"></span>**`vaelric_restless_grave_end`** Vaelric: “Well that's unfortunate...for you.”

    - “Bye.” → *conversation ends*

    <span id="d-vaelric_restless_grave_15"></span>**`vaelric_restless_grave_15`** Vaelric: “Look for anything that might tell us more about who was buried there and why the grave was disturbed.” — **effects:** sets stage 20 of [Restless in the grave](../quests/mg_restless_grave.md#stage-20)


    <span id="d-vaelric_restless_grave_found_clues_10"></span>**`vaelric_restless_grave_found_clues_10`** Vaelric: “What are they?”

    - “I found this broken bell and a music box. [Show Vaelric.]” → [vaelric_restless_grave_found_clues_20](#d-vaelric_restless_grave_found_clues_20)

    <span id="d-vaelric_restless_grave_found_clue_10"></span>**`vaelric_restless_grave_found_clue_10`** Vaelric: “Interesting, but not helpful. Go back and search for something useful. It makes sense if you search close by to where you found this other item. And don't keep running back to me every time you find something so mundane.”


    <span id="d-mg_vaelric_defeated_eryndor_50"></span>**`mg_vaelric_defeated_eryndor_50`** [Dummy NPC](../monsters/none.md): “With your hesitation preventing you from getting a word in...”

    - Next → [mg_vaelric_defeated_eryndor_60](#d-mg_vaelric_defeated_eryndor_60)

    <span id="d-vaelric_restless_grave_found_clues_20"></span>**`vaelric_restless_grave_found_clues_20`** Vaelric: “I see. Interesting, but not very helpful. Go explore the Galmore encampment east of the graveyard and report back to me when you find something helpful.”


    <span id="d-mg_vaelric_defeated_eryndor_60"></span>**`mg_vaelric_defeated_eryndor_60`** [Vaelric](../monsters/vaelric.md): “I see. You took the ring for yourself and left his spirit unfulfilled. That was your choice.”

    - “But, but...” → [mg_vaelric_defeated_eryndor_70](#d-mg_vaelric_defeated_eryndor_70)

    <span id="d-mg_vaelric_defeated_eryndor_70"></span>**`mg_vaelric_defeated_eryndor_70`** [Dummy NPC](../monsters/none.md): “He lets out a slow breath, his voice quieter now, laced with disappointment.”

    - Next → [mg_vaelric_defeated_eryndor_80](#d-mg_vaelric_defeated_eryndor_80)

    <span id="d-mg_vaelric_defeated_eryndor_80"></span>**`mg_vaelric_defeated_eryndor_80`** [Vaelric](../monsters/vaelric.md): “Andor would have done better.”

    - Next → [mg_vaelric_defeated_eryndor_90](#d-mg_vaelric_defeated_eryndor_90)

    <span id="d-mg_vaelric_defeated_eryndor_90"></span>**`mg_vaelric_defeated_eryndor_90`** Vaelric: “[Turning away, he mutters:] I will take what peace I can, while it lasts. But do not expect my gratitude.” — **effects:** sets stage 120 of [Restless in the grave](../quests/mg_restless_grave.md#stage-120)




## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 68 lines added |
| [v0.8.15](../versions/0.8.15.md) | Dialogue: 1 line changed<br>· text: “Interesting, but not helpful. Go back to search for something useful …” → “Interesting, but not helpful. Go back and search for something useful…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines changed<br>· text: “I'll take all of the ingredients and your 4800 gold now and I will mi…” → “I'll take all of the ingredients and your {4800} gold now and I will …”<br>· text: “I'll take all of the ingredients and your 4800 gold now and I will mi…” → “I'll take all of the ingredients and your {4800} gold now and I will …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `vaelric` |
    | Spawn group | `vaelric` |
    | Loot table | `mg_vaelric_dl` |
    | Conversation | `vaelric_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik7:12` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "vaelric",
     "name": "Vaelric",
     "iconID": "monsters_tometik7:12",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "vaelric_selector",
     "droplistID": "mg_vaelric_dl"
    }
    ```


<small>Data from v0.8.18</small>
