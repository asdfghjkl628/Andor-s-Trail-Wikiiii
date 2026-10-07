---
description: "Nocmar is a non-player character (NPC) in Andor's Trail. Shopkeeper; starts A place to forge."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Nocmar

**Where to find Nocmar:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper; starts [A place to forge](../quests/place_to_forge.md) |
| **Entry ID** | `nocmar` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Heartsteel trident](../items/heartstone_glaive.md) | 100% | 1 |
| [Heartsteel handaxe](../items/heartstone_handaxe.md) | 100% | 1 |
| [Heartsteel greataxe](../items/heartstone_greataxe.md) | 100% | 1 |
| [Heartsteel blade breaker](../items/heartstone_blade_breaker.md) | 100% | 1 |
| [Heartsteel mace](../items/heartstone_mace.md) | 100% | 1 |
| [Heartsteel warblade](../items/heartstone_1h_sword.md) | 100% | 1 |
| [Heartsteel claymore](../items/heartstone_2h_sword.md) | 100% | 1 |
| [Heartsteel dagger](../items/heartstone_dagger.md) | 100% | 1 |
| [Heartsteel doomhammer](../items/heartsteel_2h_hammer.md) | 100% | 1 |

## Quests

- [A place to forge](../quests/place_to_forge.md): stages 10, 20, 60
- [Lost treasures](../quests/nocmar.md): stages 20, 30, 48, 80, 90, 100, 200
- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): stages 10, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Nocmar. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/nocmar_selector.json" data-npc="Nocmar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (63 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-nocmar_selector"></span>**`nocmar_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 90 of [Lost treasures](../quests/nocmar.md#stage-90))* → [nocmar](#d-nocmar)
    - branch 2 *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-90) is 90)* → [nocmar_forge_10](#d-nocmar_forge_10)
    - branch 3 *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-100) is 100)* → [nocmar_forge_one_item_10](#d-nocmar_forge_one_item_10)
    - branch 4 *(if reached stage 200 of [Lost treasures](../quests/nocmar.md#stage-200))* → [nocmar_post_heartsteel_10](#d-nocmar_post_heartsteel_10)

    <span id="d-nocmar"></span>**`nocmar`** Nocmar: “Hello and welcome to my place.”

    - “This place looks like a smithy. Do you have anything to trade?” → [nocmar_trade_select](#d-nocmar_trade_select)
    - “Unnmir sent me.” *(if reached stage 10 of [Lost treasures](../quests/nocmar.md#stage-10); NOT reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60))* → [nocmar_quest_select](#d-nocmar_quest_select)
    - “Bye.” → *conversation ends*
    - “What will you do now?” *(if reached stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60))* → [nocmar_deed_receive_10](#d-nocmar_deed_receive_10)

    <span id="d-nocmar_forge_10"></span>**`nocmar_forge_10`** Nocmar: “There you are. The forge has been lit. Truth be told, it never truly dies, not while the thing below sleeps. Come, sit by the anvil if you can steady your hands.”

    - “It never dies?” → [nocmar_dragon_reveal_10](#d-nocmar_dragon_reveal_10)

    <span id="d-nocmar_forge_one_item_10"></span>**`nocmar_forge_one_item_10`** Nocmar: “Heartsteel answers to shape and intent. Tell me which form you demand and I will pour the heartstone's essence into that blade or head. Choose wisely; only one may be made from this stone.”

    - “What?! I only get one? But how will I decide which one I want?” → [nocmar_forge_one_item_20](#d-nocmar_forge_one_item_20)
    - “I've made a decision.” *(if reached stage 25 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-25); NOT reached stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39))* → [nocmar_forge_one_item_picked_10](#d-nocmar_forge_one_item_picked_10)
    - “I chose the claymore.” *(if reached stage 30 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-30))* → [nocmar_claymore_10](#d-nocmar_claymore_10)
    - “I chose the one-handed sword” *(if reached stage 31 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-31))* → [nocmar_onehanded_10](#d-nocmar_onehanded_10)
    - “I chose the dagger” *(if reached stage 32 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-32))* → [nocmar_dagger_10](#d-nocmar_dagger_10)
    - “I chose the glaive” *(if reached stage 33 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-33))* → [nocmar_glaive_10](#d-nocmar_glaive_10)
    - “I chose the greate axe” *(if reached stage 34 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-34))* → [nocmar_greateaxe_10](#d-nocmar_greateaxe_10)
    - “I chose the hand axe” *(if reached stage 35 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-35))* → [nocmar_handaxe_10](#d-nocmar_handaxe_10)
    - “I chose the mace” *(if reached stage 36 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-36))* → [nocmar_mace_10](#d-nocmar_mace_10)
    - “I chose the parrying weapon” *(if reached stage 37 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-37))* → [nocmar_bladeBreaker_10](#d-nocmar_bladeBreaker_10)

    <span id="d-nocmar_post_heartsteel_10"></span>**`nocmar_post_heartsteel_10`** Nocmar: “This place is a mess, I have a lot of work ahead of me to make this place usable.”


    <span id="d-nocmar_trade_select"></span>**`nocmar_trade_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [Lost treasures](../quests/nocmar.md#stage-200))* → *shop opens*
    - branch 2 → [nocmar_trade_1](#d-nocmar_trade_1)

    <span id="d-nocmar_quest_select"></span>**`nocmar_quest_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [Lost treasures](../quests/nocmar.md#stage-80))* → [nocmar_complete_5](#d-nocmar_complete_5)
    - branch 2 *(if reached stage 20 of [Lost treasures](../quests/nocmar.md#stage-20))* → [nocmar_continue](#d-nocmar_continue)
    - branch 3 → [nocmar_quest](#d-nocmar_quest)

    <span id="d-nocmar_deed_receive_10"></span>**`nocmar_deed_receive_10`** Nocmar: “Meet me at the white house south of town. The lock will no longer bar your entry. I must prepare the forge and make certain the place is safe.” — **effects:** sets stage 90 of [Lost treasures](../quests/nocmar.md#stage-90), removes monsters from fallhaven_nocmar


    <span id="d-nocmar_dragon_reveal_10"></span>**`nocmar_dragon_reveal_10`** Nocmar: “Below this floor lies more than stone and ash. A dragon slumbers beneath, bound by the magic of this place since long before my time. Its breath seeps upward through cracks in the rock, feeding the forge with endless heat.”

    - Next → [nocmar_dragon_reveal_10a](#d-nocmar_dragon_reveal_10a)

    <span id="d-nocmar_forge_one_item_20"></span>**`nocmar_forge_one_item_20`** Nocmar: “Oh, that's easier than you might think. Here, I will show you a list of the items and their capabilities. Then after you think about it, you can come back to me and I will forge it for you.” — **effects:** sets stage 25 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-25)

    - “Very well. Let us see this list.” → *shop opens*

    <span id="d-nocmar_forge_one_item_picked_10"></span>**`nocmar_forge_one_item_picked_10`** Nocmar: “Excellent. Which one do you desire?”

    - “Forge me the two-handed claymore.” → [nocmar_claymore_10](#d-nocmar_claymore_10)
    - “Of course, I will take the one-handed sword.” → [nocmar_onehanded_10](#d-nocmar_onehanded_10)
    - “Forge me a dagger.” → [nocmar_dagger_10](#d-nocmar_dagger_10)
    - “Forge me a glaive.” → [nocmar_glaive_10](#d-nocmar_glaive_10)
    - “I want that powerful great axe.” → [nocmar_greateaxe_10](#d-nocmar_greateaxe_10)
    - “Forge me a hand axe.” → [nocmar_handaxe_10](#d-nocmar_handaxe_10)
    - “Forge me a mace.” → [nocmar_mace_10](#d-nocmar_mace_10)
    - “I really want that parrying weapon.” → [nocmar_bladeBreaker_10](#d-nocmar_bladeBreaker_10)
    - “I adventure without a weapon, so I desire none of these.” → [nocmar_no_weapon_10](#d-nocmar_no_weapon_10)

    <span id="d-nocmar_claymore_10"></span>**`nocmar_claymore_10`** Nocmar: “The bellows heave and the dragon's breath draws down into the furnace. I fold the heartstone's cooled core into the molten vein and shape the claymore. The metal sings to the hammer. Stand back while I temper and finish it.” — **effects:** sets stage 30 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-30), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “I will wait.” → [nocmar_claymore_20](#d-nocmar_claymore_20)

    <span id="d-nocmar_onehanded_10"></span>**`nocmar_onehanded_10`** Nocmar: “A one-handed war blade, balanced and quick. Heartsteel will make it sing in your hand and cleave with a will of its own.” — **effects:** sets stage 31 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-31), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Make it so.” → [nocmar_onehanded_20](#d-nocmar_onehanded_20)

    <span id="d-nocmar_dagger_10"></span>**`nocmar_dagger_10`** Nocmar: “I work the heartstone down to a keen edge fit for a dagger. The heartsteel takes to a small shape with a bitter bite. This will be a precise and deadly blade.” — **effects:** sets stage 32 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-32), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Very well.” → [nocmar_dagger_20](#d-nocmar_dagger_20)

    <span id="d-nocmar_glaive_10"></span>**`nocmar_glaive_10`** Nocmar: “A glaive demands balance and spring. I ring the shaft and bind the heartsteel head to it, coaxing a reach that will cut through ranks.” — **effects:** sets stage 33 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-33), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Proceed.” → [nocmar_glaive_20](#d-nocmar_glaive_20)

    <span id="d-nocmar_greateaxe_10"></span>**`nocmar_greateaxe_10`** Nocmar: “A great axe needs weight and a true center. I work the heartsteel into a ferocious head, then temper it in the dragon-warmed coals.” — **effects:** sets stage 34 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-34), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Do it.” → [nocmar_greateaxe_20](#d-nocmar_greateaxe_20)

    <span id="d-nocmar_handaxe_10"></span>**`nocmar_handaxe_10`** Nocmar: “The hand axe will be compact and reliable. I shape the edge and set the haft so it fits your grip like a second thought.” — **effects:** sets stage 35 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-35), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Good.” → [nocmar_handaxe_20](#d-nocmar_handaxe_20)

    <span id="d-nocmar_mace_10"></span>**`nocmar_mace_10`** Nocmar: “A mace it is. I imbue the head to carry both blunt force and uncanny true weight. This will crush bone and resolve alike.” — **effects:** sets stage 36 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-36), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Carry on.” → [nocmar_mace_20](#d-nocmar_mace_20)

    <span id="d-nocmar_bladeBreaker_10"></span>**`nocmar_bladeBreaker_10`** Nocmar: “A parrying weapon it is. This will hinder your attacker's weapon.” — **effects:** sets stage 37 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-37), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)

    - “Carry on.” → [nocmar_bladeBreaker_20](#d-nocmar_bladeBreaker_20)

    <span id="d-nocmar_trade_1"></span>**`nocmar_trade_1`** Nocmar: “I don't have any items for sale. I used to have a lot of things for sale, but nowadays I'm not allowed to sell anything.”

    - Next → [nocmar_trade_2](#d-nocmar_trade_2)

    <span id="d-nocmar_complete_5"></span>**`nocmar_complete_5`** [Nocmar](../monsters/nocmar.md): “There was a time, before all this, when I had a place. A house. Not just any house...a white house on the edge of Fallhaven, glowing as if lit by the gods themselves. That glow comes from the forge inside. A forge unlike any other, always…” — **effects:** sets stage 10 of [A place to forge](../quests/place_to_forge.md#stage-10)

    - “Wait, that's your house?” *(if NOT reached stage 50 of [A place to forge](../quests/place_to_forge.md#stage-50))* → [nocmar_white_house_10](#d-nocmar_white_house_10)
    - “Well, that time has come back! I have the deed and the key to your forge house. [hand them to Nocmar]” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-50) is 50; hand over 1× [White house deed](../items/white_house_deed.md); hand over 1× [White house key](../items/white_house_key.md))* → [nocmar_wh_10](#d-nocmar_wh_10)

    <span id="d-nocmar_continue"></span>**`nocmar_continue`** Nocmar: “Have you found a heartstone yet?”

    - “Yes, at last I found it.” *(if carry 1× [Heartstone](../items/heartstone_unrefined.md); NOT carry 1× [Heartstone](../items/heartstone.md))* → [nocmar_unrefined_stone_10](#d-nocmar_unrefined_stone_10)
    - “Could you tell me the story again?” → [nocmar_quest_1](#d-nocmar_quest_1)
    - “No, not yet.” → [nocmar_continue_2](#d-nocmar_continue_2)
    - “Actually, I found two. [extend your hands, one stone in each]” *(if carry 1× [Heartstone](../items/heartstone_unrefined.md); carry 1× [Heartstone](../items/heartstone.md))* → [nocmar_two_stones_10](#d-nocmar_two_stones_10)
    - “Yes, at last I found it.” *(if hand over 1× [Heartstone](../items/heartstone.md); NOT carry 1× [Heartstone](../items/heartstone_unrefined.md))* → [nocmar_complete](#d-nocmar_complete)
    - “[while shaking your head] It's in your hand.” *(if reached stage 10 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-10))* → [nocmar_complete_2](#d-nocmar_complete_2)

    <span id="d-nocmar_quest"></span>**`nocmar_quest`** Nocmar: “Unnmir sent you huh? I guess it must be important then.” — **effects:** sets stage 20 of [Lost treasures](../quests/nocmar.md#stage-20)

    - Next → [nocmar_quest_1](#d-nocmar_quest_1)

    <span id="d-nocmar_dragon_reveal_10a"></span>**`nocmar_dragon_reveal_10a`** Nocmar: “Even when no fire burns, the stones themselves glow with its warmth. The light you see spilling from under the door isn't flame - it's the dragon's breath, alive and eternal. I sealed the forge years ago when Geomyr banned heartsteel, but…”

    - “That explains the glow under the door?” → [nocmar_dragon_reveal_15](#d-nocmar_dragon_reveal_15)
    - “A dragon? You've been living above a dragon?” → [nocmar_dragon_reveal_17](#d-nocmar_dragon_reveal_17)

    <span id="d-nocmar_no_weapon_10"></span>**`nocmar_no_weapon_10`** Nocmar: “Are you sure that I can't provide you a nice weapon?”

    - “Yeah, I'm sure. Thanks anyway.” → [nocmar_no_weapon_15](#d-nocmar_no_weapon_15)
    - “Umm, no, I am not so sure. Maybe I do want one.” → [nocmar_forge_one_item_picked_10](#d-nocmar_forge_one_item_picked_10)

    <span id="d-nocmar_claymore_20"></span>**`nocmar_claymore_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it. And tell no one where you got this.” — **effects:** gives 1× [Heartsteel claymore](../items/heartstone_2h_sword.md), sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_onehanded_20"></span>**`nocmar_onehanded_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel warblade](../items/heartstone_1h_sword.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_dagger_20"></span>**`nocmar_dagger_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel dagger](../items/heartstone_dagger.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_glaive_20"></span>**`nocmar_glaive_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel trident](../items/heartstone_glaive.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_greateaxe_20"></span>**`nocmar_greateaxe_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel greataxe](../items/heartstone_greataxe.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_handaxe_20"></span>**`nocmar_handaxe_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel handaxe](../items/heartstone_handaxe.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_mace_20"></span>**`nocmar_mace_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel mace](../items/heartstone_mace.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_bladeBreaker_20"></span>**`nocmar_bladeBreaker_20`** Nocmar: “It is done. The weapon cools beneath my hand. Take it, and guard it well. There will never be another like it.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), gives 1× [Heartsteel blade breaker](../items/heartstone_blade_breaker.md)

    - “Thank you. I will guard it.” → *conversation ends*

    <span id="d-nocmar_trade_2"></span>**`nocmar_trade_2`** Nocmar: “I was once one of the greatest smiths in Fallhaven. Then that bastard Lord Geomyr banned my use of heartsteel.”

    - Next → [nocmar_trade_3](#d-nocmar_trade_3)

    <span id="d-nocmar_white_house_10"></span>**`nocmar_white_house_10`** Nocmar: “Yes, but I lost it. When Geomyr banned heartsteel, my gold dried up. I went to Alkapoan for a loan. Fool that I was, I could not repay him, and so he took the house...my house...as his prize. He holds the deed, and he holds the key.”

    - “Who's Alkapoan?” *(if NOT reached stage 130 of [Much water](../quests/brv_flood.md#stage-130))* → [nocmar_alkapoan_unknown_10](#d-nocmar_alkapoan_unknown_10)
    - “That's a lot to lose, indeed.” *(if reached stage 130 of [Much water](../quests/brv_flood.md#stage-130))* → [nocmar_white_house_20](#d-nocmar_white_house_20)

    <span id="d-nocmar_wh_10"></span>**`nocmar_wh_10`** Nocmar: “Ah, all these years and at last I have a chance to see it again.” — **effects:** sets stage 60 of [A place to forge](../quests/place_to_forge.md#stage-60)

    - “What will you do now?” → [nocmar_deed_receive_10](#d-nocmar_deed_receive_10)

    <span id="d-nocmar_unrefined_stone_10"></span>**`nocmar_unrefined_stone_10`** Nocmar: “Well, I can tell from here that it is unrefined. Still forming. No heartsteel can be forged from this. If you tried, the forge would sputter and crack. Return it back where you found it, it will continue drawing heat and pressure from the…” — **effects:** sets stage 48 of [Lost treasures](../quests/nocmar.md#stage-48)


    <span id="d-nocmar_quest_1"></span>**`nocmar_quest_1`** Nocmar: “OK, these old weapons have lost their inner glow now that they haven't been used in a while.”

    - Next → [nocmar_quest_2](#d-nocmar_quest_2)

    <span id="d-nocmar_continue_2"></span>**`nocmar_continue_2`** Nocmar: “Please keep looking. Unnmir must have something important planned for you.”


    <span id="d-nocmar_two_stones_10"></span>**`nocmar_two_stones_10`** Nocmar: “Well, I can tell from here that the one in your right hand is not ready. It is unrefined. Still forming. No heartsteel can be forged from this. If you tried, the forge would sputter and crack.”

    - Next → [nocmar_two_stones_11](#d-nocmar_two_stones_11)

    <span id="d-nocmar_complete"></span>**`nocmar_complete`** Nocmar: “So you truly have it? The heartstone...beautiful and intact. Remarkable. You've done what few would dare. Can you see the glow? It's literally pulsating.” — **effects:** sets stage 10 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-10)

    - Next → [nocmar_complete_2](#d-nocmar_complete_2)

    <span id="d-nocmar_complete_2"></span>**`nocmar_complete_2`** [Dummy NPC](../monsters/none.md): “He studies it with reverence, then grows troubled.”

    - “Oh, no!” → [nocmar_complete_3](#d-nocmar_complete_3)

    <span id="d-nocmar_dragon_reveal_15"></span>**`nocmar_dragon_reveal_15`** Nocmar: “Aye. The forge's light is fed by its breath, not by any flame of mine.”

    - Next *(if NOT reached stage 100 of [Lost treasures](../quests/nocmar.md#stage-100))* → [nocmar_dragon_reveal_20](#d-nocmar_dragon_reveal_20)

    <span id="d-nocmar_dragon_reveal_17"></span>**`nocmar_dragon_reveal_17`** Nocmar: “Aye. Respect it and it respects us. Disturb it and you wake things that cannot be bargained with. That is why I will work here and not in my shop.”

    - Next *(if NOT reached stage 100 of [Lost treasures](../quests/nocmar.md#stage-100))* → [nocmar_dragon_reveal_20](#d-nocmar_dragon_reveal_20)

    <span id="d-nocmar_no_weapon_15"></span>**`nocmar_no_weapon_15`** Nocmar: “Okay.” — **effects:** sets stage 200 of [Lost treasures](../quests/nocmar.md#stage-200), sets stage 38 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-38), sets stage 39 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-39)


    <span id="d-nocmar_trade_3"></span>**`nocmar_trade_3`** Nocmar: “By decree of Lord Geomyr, no one in Fallhaven is allowed to even use heartsteel weapons. Much less sell any.”

    - Next → [nocmar_trade_4](#d-nocmar_trade_4)

    <span id="d-nocmar_alkapoan_unknown_10"></span>**`nocmar_alkapoan_unknown_10`** Nocmar: “You've not been to Brimhaven and had to deal with him?”

    - “No, I guess I haven't.” → [nocmar_alkapoan_unknown_20](#d-nocmar_alkapoan_unknown_20)

    <span id="d-nocmar_white_house_20"></span>**`nocmar_white_house_20`** Nocmar: “If I am to work again, I must have that house returned to me. Speak to Alkapoan. Persuade him, pay him, bargain with him. Do what must be done. Bring me the deed and the key, and only then shall I forge for you once more.” — **effects:** sets stage 20 of [A place to forge](../quests/place_to_forge.md#stage-20)

    - “This is exciting. I will not let you down.” → *conversation ends*
    - “Who is Alkapoan?” → [nocmar_white_house_forget_alkapoan_10](#d-nocmar_white_house_forget_alkapoan_10)

    <span id="d-nocmar_quest_2"></span>**`nocmar_quest_2`** Nocmar: “To make the heartsteel glow again, we will need a heartstone.”

    - Next → [nocmar_quest_3](#d-nocmar_quest_3)

    <span id="d-nocmar_two_stones_11"></span>**`nocmar_two_stones_11`** Nocmar: “Return it back where you found it, it will continue drawing heat and pressure from the Rift, hardening over years. But taken from its cradle? It will never become whole. You must return it to the exact place you found it.” — **effects:** sets stage 48 of [Lost treasures](../quests/nocmar.md#stage-48)

    - “What about this other one? [showing Nocmar the stone in your left hand]” *(if hand over 1× [Heartstone](../items/heartstone.md))* → [nocmar_complete](#d-nocmar_complete)

    <span id="d-nocmar_complete_3"></span>**`nocmar_complete_3`** [Nocmar](../monsters/nocmar.md): “But no, I cannot work it here. Too many eyes, too many whispers. If I were caught forging heartsteel in this shop, it would mean ruin for me. I need a place that is safe, hidden, yet...proper. Somewhere I can work without Lord Geomyr's…” — **effects:** sets stage 80 of [Lost treasures](../quests/nocmar.md#stage-80)

    - Next → [nocmar_complete_4](#d-nocmar_complete_4)

    <span id="d-nocmar_dragon_reveal_20"></span>**`nocmar_dragon_reveal_20`** Nocmar: “Now, you brought one cooled heartstone. We can forge only one item from it.” — **effects:** sets stage 100 of [Lost treasures](../quests/nocmar.md#stage-100)

    - Next → [nocmar_forge_one_item_10](#d-nocmar_forge_one_item_10)

    <span id="d-nocmar_trade_4"></span>**`nocmar_trade_4`** Nocmar: “So now I have to hide the few weapons I have left. I won't dare sell any of them anymore.”

    - Next → [nocmar_trade_4_1](#d-nocmar_trade_4_1)

    <span id="d-nocmar_alkapoan_unknown_20"></span>**`nocmar_alkapoan_unknown_20`** Nocmar: “Oh, then you must do so first as I need you to understand the man before you can accomplish what it is that I need from you.”


    <span id="d-nocmar_white_house_forget_alkapoan_10"></span>**`nocmar_white_house_forget_alkapoan_10`** Nocmar: “You've not been to Brimhaven and had to deal with him?”

    - “Oh, the rich guy up on his high hill? I remember now.” → *conversation ends*

    <span id="d-nocmar_quest_3"></span>**`nocmar_quest_3`** Nocmar: “Years ago, we used to fight the liches of Undertell. I have no idea if they still haunt the place.”

    - “Undertell? What's that?” → [nocmar_quest_4](#d-nocmar_quest_4)
    - “Undertell? Is that where I could find a heartstone?” → [nocmar_quest_3a](#d-nocmar_quest_3a)

    <span id="d-nocmar_complete_4"></span>**`nocmar_complete_4`** [Dummy NPC](../monsters/none.md): “While pausing, Nocmar looks down, then sighs.”

    - Next → [nocmar_complete_5](#d-nocmar_complete_5)

    <span id="d-nocmar_trade_4_1"></span>**`nocmar_trade_4_1`** Nocmar: “I haven't seen the heartsteel glow in several years now that Lord Geomyr has banned them.”

    - Next → [nocmar_trade_5](#d-nocmar_trade_5)

    <span id="d-nocmar_quest_4"></span>**`nocmar_quest_4`** Nocmar: “Undertell; the pits of the lost souls. Travel south to the devastated wastelands of Galmore Mountain and follow the tracks from there.”

    - Next → [nocmar_quest_5](#d-nocmar_quest_5)

    <span id="d-nocmar_quest_3a"></span>**`nocmar_quest_3a`** Nocmar: “Yes...”

    - Next → [nocmar_quest_4a](#d-nocmar_quest_4a)

    <span id="d-nocmar_trade_5"></span>**`nocmar_trade_5`** Nocmar: “So, unfortunately I can't sell you any of my weapons.”


    <span id="d-nocmar_quest_5"></span>**`nocmar_quest_5`** Nocmar: “Beware the liches of Undertell, if they are still around. Those things can kill you by their gaze alone.”


    <span id="d-nocmar_quest_4a"></span>**`nocmar_quest_4a`** Nocmar: “Undertell; the pits of the lost souls. Travel south to the devastated wastelands of Galmore Mountain and follow the tracks from there.” — **effects:** sets stage 30 of [Lost treasures](../quests/nocmar.md#stage-30)

    - Next → [nocmar_quest_5](#d-nocmar_quest_5)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “Beware the liches of Undertell, if they are still are around. Those t…” → “Beware the liches of Undertell, if they are still around. Those thing…”<br>· text: “Ok, these old weapons have lost their inner glow now that they haven'…” → “OK, these old weapons have lost their inner glow now that they haven'…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 2 lines added, 2 lines changed<br>· text: “Undertell; the pits of the lost souls. Travel south and enter the cav…” → “Undertell; the pits of the lost souls. Travel south to the devastated…” |
| [v0.8.18](../versions/0.8.18.md) | Conversation changed<br>Dialogue: 39 lines added, 8 lines changed<br>· text: “Can you see the glow? It's literally pulsating.” → “He studies it with reverence, then grows troubled.”<br>· text: “Hello. I'm Nocmar.” → “Hello and welcome to my place.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `nocmar` |
    | Spawn group | `nocmar` |
    | Loot table | `nocmar` |
    | Conversation | `nocmar_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "nocmar",
     "name": "Nocmar",
     "iconID": "monsters_men:8",
     "monsterClass": "humanoid",
     "spawnGroup": "nocmar",
     "phraseID": "nocmar_selector",
     "droplistID": "nocmar"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nocmar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nocmar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nocmar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=nocmar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
