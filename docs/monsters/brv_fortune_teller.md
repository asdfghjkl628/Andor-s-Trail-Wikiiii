---
description: "Pangitain is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Teaches Merchant, Cleave, Treasure Hunter, Dodge, Increased Fortitude, Magic Finder, Weapon Accuracy."
---

# ![](../assets/icons/monsters/monsters_tometik6_17.png){ .sprite } Pangitain

**Where to find Pangitain:** Brimhaven: [brimhaven_fortune_teller](../maps/brimhaven_fortune_teller.md#pin-npc-brv_fortune_teller)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_17.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Teaches [Merchant](../skills/barter.md), [Cleave](../skills/cleave.md), [Treasure Hunter](../skills/coinfinder.md), [Dodge](../skills/dodge.md), [Increased Fortitude](../skills/fortitude.md), [Magic Finder](../skills/magicfinder.md), [Weapon Accuracy](../skills/weaponChance.md) |
| **Found in** | Brimhaven |
| **Entry ID** | `brv_fortune_teller` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [The exploded star](../quests/mg2_exploded_star.md): stages 60, 62
- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 100
- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 144, 145, 147, 148, 149, 150, 151

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Pangitain. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_fortune_select.json" data-npc="Pangitain" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (48 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_fortune_select"></span>**`brv_fortune_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144))* → [brv_fortune_back](#d-brv_fortune_back)
    - Next → [brv_fortune](#d-brv_fortune)

    <span id="d-brv_fortune_back"></span>**`brv_fortune_back`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_10](#d-brv_fortune_back_10)
    - branch 2 → [brv_fortune_back_2](#d-brv_fortune_back_2)

    <span id="d-brv_fortune"></span>**`brv_fortune`** Pangitain: “Welcome to my house. Please come in.”

    - Next → [brv_fortune_10](#d-brv_fortune_10)

    <span id="d-brv_fortune_back_10"></span>**`brv_fortune_back_10`** Pangitain: “Welcome back. I see that you bring me interesting things that have fallen from the sky.”

    - “How do you know?” → [brv_fortune_back_12](#d-brv_fortune_back_12)
    - “The pieces that I have found in the area of Mt. Galmore? Yes, I have them with me.” → [brv_fortune_back_20](#d-brv_fortune_back_20)

    <span id="d-brv_fortune_back_2"></span>**`brv_fortune_back_2`** Pangitain: “Welcome back.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_10"></span>**`brv_fortune_10`** Pangitain: “What has brought you to me? It looks like you might need my help.”

    - “What help can you offer?” → [brv_fortune_20](#d-brv_fortune_20)
    - “I am searching...” → [brv_fortune_30](#d-brv_fortune_30)
    - “So you are the one who ordered a 'Crystal Globe'?” *(if hand over 1× [Crystal globe](../items/brv_wh_item_00.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110))* → [brv_wh_delivery_brv_fortune](#d-brv_wh_delivery_brv_fortune)

    <span id="d-brv_fortune_back_12"></span>**`brv_fortune_back_12`** Pangitain: “Sigh. I know many things. How often do I still have to prove it?”

    - “Well, OK. What about my fallen stones collection?” → [brv_fortune_back_20](#d-brv_fortune_back_20)

    <span id="d-brv_fortune_back_20"></span>**`brv_fortune_back_20`** Pangitain: “You can't do anything useful with them. Give them to me and I'll give you a kingly reward.”

    - “Here, you can have them for the greater glory.” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_30](#d-brv_fortune_back_30)
    - “Really? What can you offer?” → [brv_fortune_back_50](#d-brv_fortune_back_50)

    <span id="d-brv_fortune_choice"></span>**`brv_fortune_choice`** Pangitain: “Anything more I can help you with?”

    - “Please tell me something that you can see about me or my brother Andor. [Give him 100 gold]” *(if have 100 gold)* → [brv_fortune_pre_fortunes](#d-brv_fortune_pre_fortunes)
    - “I don't have 100 gold to pay you.” → [brv_fortune_end_10](#d-brv_fortune_end_10)
    - “Maybe I can help you.” → [brv_fortune_300](#d-brv_fortune_300)
    - “Are you the one who ordered a 'Crystal Globe'?” *(if hand over 1× [Crystal globe](../items/brv_wh_item_00.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110))* → [brv_wh_delivery_brv_fortune](#d-brv_wh_delivery_brv_fortune)

    <span id="d-brv_fortune_20"></span>**`brv_fortune_20`** Pangitain: “I can see what others can't see.”

    - “Really? I am searching...” → [brv_fortune_30](#d-brv_fortune_30)

    <span id="d-brv_fortune_30"></span>**`brv_fortune_30`** Pangitain: “Wait”

    - Next → [brv_fortune_40](#d-brv_fortune_40)

    <span id="d-brv_wh_delivery_brv_fortune"></span>**`brv_wh_delivery_brv_fortune`** Pangitain: “Ah yes, I need a new one. My current crystal globe has become a bit cloudy - otherwise I would of course have seen that you would bring me a new globe. Here is the gold for it.” — **effects:** clears stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110), sets stage 100 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-100), gives 100× [Gold coins](../items/gold.md)

    - “Do you want to try the crystal ball with me to see if it works?” → [brv_wh_delivery_brv_fortune_10](#d-brv_wh_delivery_brv_fortune_10)
    - “Thanks for choosing Facutloni's delivery.” → *conversation ends*

    <span id="d-brv_fortune_back_30"></span>**`brv_fortune_back_30`** Pangitain: “Thank you. Very wise of you. Indeed. Let - your - wisdom - grow ...” — **effects:** sets stage 60 of [The exploded star](../quests/mg2_exploded_star.md#stage-60)

    - “I already feel it.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_back_50"></span>**`brv_fortune_back_50`** Pangitain: “Look here in my chest with my most valuable items, that could transfer their powers to you.”

    - Next → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_pre_fortunes"></span>**`brv_fortune_pre_fortunes`** *(silent check: the first matching branch below is taken)*

    - Next *(if faction “brv_fortune” ≥ 6)* → [brv_fortune_come_back_much_later](#d-brv_fortune_come_back_much_later)
    - Next *(if NOT 0 rounds passed since timer “brv_fortune”)* → [brv_fortune_pre_fortunes_2](#d-brv_fortune_pre_fortunes_2)
    - Next *(if NOT 1 rounds passed since timer “brv_fortune”)* → [brv_fortune_come_back_later](#d-brv_fortune_come_back_later)
    - Next → [brv_fortune_pre_fortunes_2](#d-brv_fortune_pre_fortunes_2)

    <span id="d-brv_fortune_end_10"></span>**`brv_fortune_end_10`** Pangitain: “Then goodbye. I know you will return some time in the future.”


    <span id="d-brv_fortune_300"></span>**`brv_fortune_300`** Pangitain: “Yes, that would be good. I already have an idea. But not now. Please come back later and ask me again.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_40"></span>**`brv_fortune_40`** Pangitain: “I feel that you are on a search... at the beginning of a long and dangerous search for a relative of yours.” — **effects:** sets stage 144 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-144)

    - “I am impressed. Can you tell me more about my brother Andor or me?” → [brv_fortune_50](#d-brv_fortune_50)
    - “That doesn't impress me.” → [brv_fortune_end_10](#d-brv_fortune_end_10)

    <span id="d-brv_wh_delivery_brv_fortune_10"></span>**`brv_wh_delivery_brv_fortune_10`** Pangitain: “You say you want me to help you?”

    - “What help can you offer?” → [brv_fortune_20](#d-brv_fortune_20)
    - “I am searching...” → [brv_fortune_30](#d-brv_fortune_30)

    <span id="d-brv_fortune_back_90"></span>**`brv_fortune_back_90`** Pangitain: “Go now.”

    - “Bye.” → *conversation ends*

    <span id="d-brv_fortune_back_52"></span>**`brv_fortune_back_52`** Pangitain: “Which one do you want to learn more about?”

    - “Gem of star precision” → [brv_fortune_back_61](#d-brv_fortune_back_61)
    - “Wanderer's Vitality” *(if skillIncrease fortitude 1)* → [brv_fortune_back_62](#d-brv_fortune_back_62)
    - “Mountainroot gold nugget” → [brv_fortune_back_65](#d-brv_fortune_back_65)
    - “Shadowstep Favor” → [brv_fortune_back_66](#d-brv_fortune_back_66)
    - “Starbound grip stone” *(if skillIncrease cleave 1)* → [brv_fortune_back_68](#d-brv_fortune_back_68)
    - “Swirling orb of awareness.” → [brv_fortune_back_69](#d-brv_fortune_back_69)

    <span id="d-brv_fortune_come_back_much_later"></span>**`brv_fortune_come_back_much_later`** Pangitain: “I told you all I can see for now. But you can come back to me in a few months when you have had new experiences.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_pre_fortunes_2"></span>**`brv_fortune_pre_fortunes_2`** *(silent check: the first matching branch below is taken)* — **effects:** faction “brv_fortune” +1, gives -100× [Gold coins](../items/gold.md)

    - Next *(if faction “brv_fortune” = 2)* → [brv_fortunes_set_timer](#d-brv_fortunes_set_timer)
    - Next *(if faction “brv_fortune” = 4)* → [brv_fortunes_set_timer](#d-brv_fortunes_set_timer)
    - Next → [brv_fortune_fortunes_select](#d-brv_fortune_fortunes_select)

    <span id="d-brv_fortune_come_back_later"></span>**`brv_fortune_come_back_later`** Pangitain: “I am tired and can't see anything new now. If you come back in a little while maybe I can tell you more.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_50"></span>**`brv_fortune_50`** Pangitain: “It will cost you 100 gold.”

    - “[Give him 100 gold]” *(if pay 100 gold)* → [brv_fortune_pre_fortunes_2](#d-brv_fortune_pre_fortunes_2)
    - “That is too expensive for me.” → [brv_fortune_end_10](#d-brv_fortune_end_10)

    <span id="d-brv_fortune_back_61"></span>**`brv_fortune_back_61`** Pangitain: “Your hand steadies with celestial clarity. Touching the item will permanently increase your weapon accuracy.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_61b](#d-brv_fortune_back_61b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_back_62"></span>**`brv_fortune_back_62`** Pangitain: “Wanderer's Vitality. You carry the strength of the sky inside you. After touching this item, you will begin to learn how to improve your overall health faster.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_62b](#d-brv_fortune_back_62b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_back_65"></span>**`brv_fortune_back_65`** Pangitain: “Very down-to-earth. You will have more success in financial matters.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_65b](#d-brv_fortune_back_65b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_back_66"></span>**`brv_fortune_back_66`** Pangitain: “You move as if guided by starlight. Touching this item will permanently improve your abilities to avoid being hit by your enemies.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_66b](#d-brv_fortune_back_66b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_back_68"></span>**`brv_fortune_back_68`** Pangitain: “From the sky to your hilt, strength flows unseen. Touching the item will permanently let you refresh faster after a kill in a fight.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_68b](#d-brv_fortune_back_68b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortune_back_69"></span>**`brv_fortune_back_69`** Pangitain: “Touching the item will permanently increase your awareness of unearthy items.”

    - “Sounds great - I choose this one. [Touch the item]” *(if hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md))* → [brv_fortune_back_69b](#d-brv_fortune_back_69b)
    - “Let me have a look at the other items.” → [brv_fortune_back_52](#d-brv_fortune_back_52)

    <span id="d-brv_fortunes_set_timer"></span>**`brv_fortunes_set_timer`** *(silent check: the first matching branch below is taken)* — **effects:** starts timer “brv_fortune”

    - Next → [brv_fortune_fortunes_select](#d-brv_fortune_fortunes_select)

    <span id="d-brv_fortune_fortunes_select"></span>**`brv_fortune_fortunes_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (5%); reached stage 151 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-151))* → [brv_fortune_come_back_much_later](#d-brv_fortune_come_back_much_later)
    - branch 2 *(if random chance (17%); NOT reached stage 151 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-151))* → [brv_fortune_andor_10](#d-brv_fortune_andor_10)
    - branch 3 *(if random chance (20%); NOT reached stage 150 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-150))* → [brv_fortune_andor_30](#d-brv_fortune_andor_30)
    - branch 4 *(if random chance (25%); NOT reached stage 149 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-149))* → [brv_fortune_hero_10](#d-brv_fortune_hero_10)
    - branch 5 *(if random chance (33%); NOT reached stage 148 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-148))* → [brv_fortune_hero_30](#d-brv_fortune_hero_30)
    - branch 6 *(if random chance (50%); NOT reached stage 147 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-147))* → [brv_fortune_hero_130](#d-brv_fortune_hero_130)
    - branch 7 *(if NOT reached stage 145 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-145))* → [brv_fortune_hero_70](#d-brv_fortune_hero_70)
    - branch 8 → [brv_fortune_fortunes_select](#d-brv_fortune_fortunes_select)

    <span id="d-brv_fortune_back_61b"></span>**`brv_fortune_back_61b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Weapon Accuracy](../skills/weaponChance.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_back_62b"></span>**`brv_fortune_back_62b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Increased Fortitude](../skills/fortitude.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_back_65b"></span>**`brv_fortune_back_65b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Treasure Hunter](../skills/coinfinder.md), +1 [Merchant](../skills/barter.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → *conversation ends*

    <span id="d-brv_fortune_back_66b"></span>**`brv_fortune_back_66b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Dodge](../skills/dodge.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_back_68b"></span>**`brv_fortune_back_68b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Cleave](../skills/cleave.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_back_69b"></span>**`brv_fortune_back_69b`** Pangitain: “A good choice. Do you feel it already?” — **effects:** +1 [Magic Finder](../skills/magicfinder.md), sets stage 62 of [The exploded star](../quests/mg2_exploded_star.md#stage-62)

    - “Wow - yes! Thank you.” → [brv_fortune_back_90](#d-brv_fortune_back_90)

    <span id="d-brv_fortune_andor_10"></span>**`brv_fortune_andor_10`** Pangitain: “I see you talking to your brother, somewhere far from here in a big city. Feygard or Nor City, I think.” — **effects:** sets stage 151 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-151)

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_andor_30"></span>**`brv_fortune_andor_30`** Pangitain: “Your brother is in league with dark forces.” — **effects:** sets stage 150 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-150)

    - Next → [brv_fortune_andor_31](#d-brv_fortune_andor_31)

    <span id="d-brv_fortune_hero_10"></span>**`brv_fortune_hero_10`** Pangitain: “I see you walking up a path on a mountain. Beware! There is something waiting for you ahead. I see you being attacked by monsters and they kill you.” — **effects:** sets stage 149 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-149)

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_hero_30"></span>**`brv_fortune_hero_30`** Pangitain: “I see a thief. He will take something from you.” — **effects:** sets stage 148 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-148)

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_hero_130"></span>**`brv_fortune_hero_130`** Pangitain: “I see a man pacing up and down in a little house. He seems to be waiting for someone.” — **effects:** sets stage 147 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-147)

    - “That must be my father Mikhail, he is waiting for me and my brother!” → [brv_fortune_hero_131](#d-brv_fortune_hero_131)

    <span id="d-brv_fortune_hero_70"></span>**`brv_fortune_hero_70`** Pangitain: “I see you picking up a lot of coins from a hole in the ground. Can it be behind your father's house?” — **effects:** sets stage 145 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-145)

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_andor_31"></span>**`brv_fortune_andor_31`** Pangitain: “He needs your help. Something horrible ... argh.”

    - Next → [brv_fortune_andor_35](#d-brv_fortune_andor_35)

    <span id="d-brv_fortune_hero_131"></span>**`brv_fortune_hero_131`** Pangitain: “Then go and get your brother and go home to him.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)

    <span id="d-brv_fortune_andor_35"></span>**`brv_fortune_andor_35`** Pangitain: “I can't see more. My view seems to be blocked.”

    - Next → [brv_fortune_choice](#d-brv_fortune_choice)



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 26 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 2 lines added, 2 lines changed |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line changed<br>· text: “I see you walking up a path on a mountain. Beware! There is something…” → “I see you walking up a path on a mountain. Beware! There is something…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 20 lines added, 1 line changed<br>· text: “Welcome back.” → “null” |
| [v0.8.15](../versions/0.8.15.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_fortune_teller` |
    | Spawn group | `brv_fortune_teller` |
    | Loot table | – |
    | Conversation | `brv_fortune_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:17` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_fortune_teller",
     "name": "Pangitain",
     "iconID": "monsters_tometik6:17",
     "unique": 1,
     "phraseID": "brv_fortune_select"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fortune_teller.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fortune_teller.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fortune_teller.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_fortune_teller.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
