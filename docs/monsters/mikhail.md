# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Mikhail

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

## Found on

- [home](../maps/home.md)
- [waytogalmore0](../maps/waytogalmore0.md)

## Quests

- [A familiar shadow](../quests/familiar_shadow.md): stages 30
- [Breakfast bread](../quests/mikhail_bread.md): stages 10, 100
- [Honor your parents](../quests/brv_present.md): stages 30, 40, 50, 60
- [More rats!](../quests/ratdom_mikhail.md): stages 10, 20, 52, 54, 70, 74, 90
- [Rats!](../quests/mikhail_rats.md): stages 10, 100
- [Search for Andor](../quests/andor.md): stages 1
- [Unusual experiences and achievements](../quests/achievements.md): stages 1
- [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md): stages 20
- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stages 90
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 1
- [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Mikhail. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/mikhail_start_select.json" data-npc="Mikhail" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (69 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mikhail_start_select"></span>**`mikhail_start_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1))* → [ratdom_mikhail](#d-ratdom_mikhail)
    - branch 2 *(if reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100))* → [mikhail_start_select2](#d-mikhail_start_select2)
    - branch 3 *(if reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10))* → [mikhail_bread_continue](#d-mikhail_bread_continue)
    - branch 4 → [mikhail_start_select2](#d-mikhail_start_select2)

    <span id="d-ratdom_mikhail"></span>**`ratdom_mikhail`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90))* → [ratdom_mikhail_90](#d-ratdom_mikhail_90)
    - branch 2 *(if reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54))* → [ratdom_mikhail_50](#d-ratdom_mikhail_50)
    - branch 3 *(if reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70))* → [ratdom_mikhail_10_10](#d-ratdom_mikhail_10_10)
    - branch 4 *(if reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70))* → [ratdom_mikhail_70](#d-ratdom_mikhail_70)
    - branch 5 → [ratdom_mikhail_01](#d-ratdom_mikhail_01)

    <span id="d-mikhail_start_select2"></span>**`mikhail_start_select2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_start_select_default](#d-mikhail_start_select_default)
    - branch 2 *(if reached stage 10 of [Rats!](../quests/mikhail_rats.md#stage-10))* → [mikhail_rats_continue](#d-mikhail_rats_continue)
    - branch 3 → [mikhail_start_select_default](#d-mikhail_start_select_default)

    <span id="d-mikhail_bread_continue"></span>**`mikhail_bread_continue`** Mikhail: “Did you get my bread from Mara at the town hall yet?”

    - “Yes, here you go.” *(if hand over 1× [Bread](../items/bread.md))* → [mikhail_bread_complete](#d-mikhail_bread_complete)
    - “No, not yet.” → [mikhail_default](#d-mikhail_default)

    <span id="d-ratdom_mikhail_90"></span>**`ratdom_mikhail_90`** [Dummy NPC](../monsters/none.md): “The huge rat ignores you now.”


    <span id="d-ratdom_mikhail_50"></span>**`ratdom_mikhail_50`** Mikhail: “Is my garden clean of filthy two-legs again?”

    - “No, not yet” → *conversation ends*
    - “Yes, I killed Mara and Tharal in the garden for you.” *(if killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md))* → [ratdom_mikhail_50_2](#d-ratdom_mikhail_50_2)
    - “(lie) I killed Mara and Tharal in the garden for you.” *(if NOT killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md))* → [ratdom_mikhail_50_4](#d-ratdom_mikhail_50_4)
    - “(lie) I killed Mara and Tharal in the garden for you.” *(if killed 1× [Mara](../monsters/ratdom_mara.md); NOT killed 1× [Tharal](../monsters/ratdom_tharal.md))* → [ratdom_mikhail_50_4](#d-ratdom_mikhail_50_4)
    - “(lie) I killed Mara and Tharal in the garden for you.” *(if NOT killed 1× [Mara](../monsters/ratdom_mara.md); NOT killed 1× [Tharal](../monsters/ratdom_tharal.md))* → [ratdom_mikhail_50_4](#d-ratdom_mikhail_50_4)

    <span id="d-ratdom_mikhail_10_10"></span>**`ratdom_mikhail_10_10`** Mikhail: “And I am hungry. Go to the town hall and bring me some bread.” — **effects:** sets stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70)

    - “OK.” → *conversation ends*
    - “Forget it.” → *conversation ends*
    - “Here I have some bread for you.” *(if hand over 1× [Bread](../items/bread.md))* → [ratdom_mikhail_10_20](#d-ratdom_mikhail_10_20)

    <span id="d-ratdom_mikhail_70"></span>**`ratdom_mikhail_70`** Mikhail: “Where is my bread? Why does it need to take so long?”

    - “Just a minute.” → *conversation ends*
    - “Forget it.” → *conversation ends*
    - “Here I have some bread for you.” *(if hand over 1× [Bread](../items/bread.md))* → [ratdom_mikhail_74](#d-ratdom_mikhail_74)
    - “Hey - I have brought some bread already.” *(if reached stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74))* → [ratdom_mikhail_80](#d-ratdom_mikhail_80)

    <span id="d-ratdom_mikhail_01"></span>**`ratdom_mikhail_01`** Mikhail: “Good. You are awake at last.”

    - “A rat? Here?” → [ratdom_mikhail_02](#d-ratdom_mikhail_02)

    <span id="d-mikhail_start_select_default"></span>**`mikhail_start_select_default`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [Search for Andor](../quests/andor.md#stage-1))* → [mikhail_default](#d-mikhail_default)
    - branch 2 → [mikhail_gamestart](#d-mikhail_gamestart)

    <span id="d-mikhail_rats_continue"></span>**`mikhail_rats_continue`** Mikhail: “Did you kill those two rats in our garden?”

    - “Yes, I have dealt with the rats now.” *(if hand over 2× [Small rat tail](../items/tail_trainingrat.md))* → [mikhail_rats_complete](#d-mikhail_rats_complete)
    - “No, not yet.” → [mikhail_rats_start2](#d-mikhail_rats_start2)

    <span id="d-mikhail_bread_complete"></span>**`mikhail_bread_complete`** Mikhail: “Thanks a lot, now I can make my breakfast. Here, take these coins for your help.” — **effects:** sets stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100), gives [Gold coins](../items/gold.md)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_default"></span>**`mikhail_default`** Mikhail: “Anything else I can help you with?”

    - “Do you have any more tasks for me?” *(if reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_all_tasks_done](#d-mikhail_all_tasks_done)
    - “Do you have any more tasks for me?” *(if reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); NOT reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_bread_done](#d-mikhail_bread_done)
    - “Do you have any more tasks for me?” *(if NOT reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_rats_done](#d-mikhail_rats_done)
    - “Do you have any tasks for me?” *(if NOT reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); NOT reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_tasks](#d-mikhail_tasks)
    - “Is there anything else you can tell me about Andor?” → [mikhail_andor1](#d-mikhail_andor1)
    - “I have a present for you.” *(if reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40))* → [mikhail_present_20](#d-mikhail_present_20)
    - “I have a present for you.” *(if reached stage 20 of [Honor your parents](../quests/brv_present.md#stage-20); NOT reached stage 40 of [Honor your parents](../quests/brv_present.md#stage-40); NOT reached stage 50 of [Honor your parents](../quests/brv_present.md#stage-50); NOT reached stage 60 of [Honor your parents](../quests/brv_present.md#stage-60); NOT reached stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40))* → [mikhail_present_10](#d-mikhail_present_10)
    - “I was searching for Andor.” → [mikhail_news_10](#d-mikhail_news_10)
    - “What kind of book is it that you have in your hand?” *(if NOT reached stage 1 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-1); NOT reached stage 1 of [Unusual experiences and achievements](../quests/achievements.md#stage-1); reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100); reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_achievements_10](#d-mikhail_achievements_10)
    - “Yes, I'm here to deliver the order for a 'Plush Pillow'. But what for?” *(if hand over 1× [Plush pillow](../items/brv_wh_item_01.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100))* → [brv_wh_delivery_mikhail](#d-brv_wh_delivery_mikhail)
    - “I don't know...something feels wrong. I thought maybe you were in danger.” *(if latest stage of [A familiar shadow](../quests/familiar_shadow.md#stage-20) is 20)* → [galmore_marked_stone_mikhail](#d-galmore_marked_stone_mikhail)

    <span id="d-ratdom_mikhail_50_2"></span>**`ratdom_mikhail_50_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52)

    - branch 1 → [ratdom_mikhail_50_10](#d-ratdom_mikhail_50_10)

    <span id="d-ratdom_mikhail_50_4"></span>**`ratdom_mikhail_50_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54)

    - branch 1 → [ratdom_mikhail_50_10](#d-ratdom_mikhail_50_10)

    <span id="d-ratdom_mikhail_10_20"></span>**`ratdom_mikhail_10_20`** Mikhail: “It's about time.” — **effects:** sets stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74)

    - “What - no thanks? Rats.” → *conversation ends*

    <span id="d-ratdom_mikhail_74"></span>**`ratdom_mikhail_74`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74)

    - branch 1 *(if reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52))* → [ratdom_mikhail_80](#d-ratdom_mikhail_80)
    - branch 2 *(if reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54))* → [ratdom_mikhail_80](#d-ratdom_mikhail_80)
    - branch 3 → [ratdom_mikhail_10_20](#d-ratdom_mikhail_10_20)

    <span id="d-ratdom_mikhail_80"></span>**`ratdom_mikhail_80`** Mikhail: “Good! Now I don't need you anymore!” — **effects:** sets stage 90 of [More rats!](../quests/ratdom_mikhail.md#stage-90)

    - “OK.” → *conversation ends*
    - “I would have gone anyway.” → *conversation ends*

    <span id="d-ratdom_mikhail_02"></span>**`ratdom_mikhail_02`** Mikhail: “As you see. Did you find your brother Andor already? He hasn't been back home for a while now.”

    - “Eh, what? No, I am still looking for Andor.” → [ratdom_mikhail_03](#d-ratdom_mikhail_03)

    <span id="d-mikhail_gamestart"></span>**`mikhail_gamestart`** Mikhail: “Oh good, you are awake.”

    - Next → [mikhail_visited](#d-mikhail_visited)

    <span id="d-mikhail_rats_complete"></span>**`mikhail_rats_complete`** Mikhail: “Oh you did? Wow, thanks a lot for your help! Please take Andor's training shield - you're going to need it. If you are hurt, use your bed over there to rest and regain your strength.” — **effects:** sets stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100), gives 1× [Kid's shield](../items/kids_shield.md)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_rats_start2"></span>**`mikhail_rats_start2`** Mikhail: “If you get hurt by the rats, come back here and rest in your bed. That way you can regain your strength.”

    - Next → [mikhail_rats_start2a](#d-mikhail_rats_start2a)

    <span id="d-mikhail_all_tasks_done"></span>**`mikhail_all_tasks_done`** Mikhail: “Not for now. Thanks for taking care of the bread and rats.”

    - “Never mind, let's talk about the other things.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_bread_done"></span>**`mikhail_bread_done`** Mikhail: “Thanks for getting me the bread. There are still the rats.”

    - “What about the rats?” → [mikhail_rats_select](#d-mikhail_rats_select)
    - “Never mind, let's talk about the other things.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_rats_done"></span>**`mikhail_rats_done`** Mikhail: “Thanks for taking care of the rats. I'd still love some bread.”

    - “What about the bread?” → [mikhail_bread_select](#d-mikhail_bread_select)
    - “Never mind, let's talk about the other things.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_tasks"></span>**`mikhail_tasks`** Mikhail: “Oh yes, there were some things I need help with, bread and rats. Which one would you like to talk about?”

    - “What about the bread?” → [mikhail_bread_select](#d-mikhail_bread_select)
    - “What about the rats?” → [mikhail_rats_select](#d-mikhail_rats_select)
    - “Never mind, let's talk about the other things.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_andor1"></span>**`mikhail_andor1`** Mikhail: “As I said, Andor went out and hasn't been back since. I worry about him. Please go look for your brother. He said he would only be out for a short while.”

    - Next → [mikhail_andor2](#d-mikhail_andor2)

    <span id="d-mikhail_present_20"></span>**`mikhail_present_20`** Mikhail: “Oh, you are such a nice child.”

    - “[Give him the cheap necklace]” *(if hand over 1× [Necklace for father (cheap)](../items/necklace_for_father1.md))* → [mikhail_present_20_1](#d-mikhail_present_20_1)
    - “[Give him the necklace]” *(if hand over 1× [Necklace for father](../items/necklace_for_father2.md))* → [mikhail_present_20_2](#d-mikhail_present_20_2)
    - “[Give him the expensive necklace]” *(if hand over 1× [Necklace for father (expensive)](../items/necklace_for_father3.md))* → [mikhail_present_20_3](#d-mikhail_present_20_3)
    - “Maybe I promised too much.” *(if NOT carry 1× [Necklace for father (cheap)](../items/necklace_for_father1.md); NOT carry 1× [Necklace for father](../items/necklace_for_father2.md); NOT carry 1× [Necklace for father (expensive)](../items/necklace_for_father3.md))* → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_present_10"></span>**`mikhail_present_10`** Mikhail: “I asked you to search for your brother Andor and you did not find out anything and instead you are bringing me a necklace? Go and search for your brother!” — **effects:** sets stage 30 of [Honor your parents](../quests/brv_present.md#stage-30)

    - “Sorry father. I will go and search for Andor.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_news_10"></span>**`mikhail_news_10`** Mikhail: “Did you find out something?”

    - “I asked around in Crossglen and they sent me to Fallhaven.” *(if reached stage 30 of [Search for Andor](../quests/andor.md#stage-30))* → [mikhail_news_20](#d-mikhail_news_20)
    - “Someone in Fallhaven told me that he met Andor and that he was searching for a man called Lodar.” *(if NOT reached stage 30 of [Search for Andor](../quests/andor.md#stage-30); reached stage 55 of [Search for Andor](../quests/andor.md#stage-55))* → [mikhail_news_30](#d-mikhail_news_30)
    - “I met a man called Lodar and he told me that Andor probably went to Nor City.” *(if NOT reached stage 30 of [Search for Andor](../quests/andor.md#stage-30); NOT reached stage 55 of [Search for Andor](../quests/andor.md#stage-55); reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [mikhail_news_40](#d-mikhail_news_40)
    - “No I did not find out anything yet.” *(if NOT reached stage 30 of [Search for Andor](../quests/andor.md#stage-30); NOT reached stage 55 of [Search for Andor](../quests/andor.md#stage-55); NOT reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [mikhail_default](#d-mikhail_default)
    - “I found Andor far north of here, at a fruit seller's stand.” *(if reached stage 310 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-310); NOT reached stage 20 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-20))* → [mikhail_news_60](#d-mikhail_news_60)
    - “I found Andor far south of here, at Alynndir's house.” *(if reached stage 290 of [Shadows](../quests/shadows.md#stage-290); NOT reached stage 20 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-20))* → [mikhail_news_60](#d-mikhail_news_60)

    <span id="d-mikhail_achievements_10"></span>**`mikhail_achievements_10`** Mikhail: “Just like my father once did, I want to give you a book to take with you on your way.”

    - Next → [mikhail_achievements_20](#d-mikhail_achievements_20)

    <span id="d-brv_wh_delivery_mikhail"></span>**`brv_wh_delivery_mikhail`** Mikhail: “Oh wow! Finally, your brother's gift has arrived and we only have to wait for his arrival.” — **effects:** clears stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100), sets stage 90 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-90)

    - “Sigh. I hope so.” → [brv_wh_delivery_mikhail2](#d-brv_wh_delivery_mikhail2)
    - “What?! Where's my gift?” → [brv_wh_delivery_mikhail3](#d-brv_wh_delivery_mikhail3)

    <span id="d-galmore_marked_stone_mikhail"></span>**`galmore_marked_stone_mikhail`** Mikhail: “What's gotten into you? I'm fine, but the same can't be said for Leta. I've seen her pacing in that house of hers, muttering to herself like a madwoman. You might want to check on her.” — **effects:** sets stage 30 of [A familiar shadow](../quests/familiar_shadow.md#stage-30)


    <span id="d-ratdom_mikhail_50_10"></span>**`ratdom_mikhail_50_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70))* → [ratdom_mikhail_10_10](#d-ratdom_mikhail_10_10)
    - branch 2 *(if NOT reached stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74))* → [ratdom_mikhail_70](#d-ratdom_mikhail_70)
    - branch 3 → [ratdom_mikhail_80](#d-ratdom_mikhail_80)

    <span id="d-ratdom_mikhail_03"></span>**`ratdom_mikhail_03`** Mikhail: “I should have guessed. Anyway.”

    - “What are you doing in my house? Where is Mikhail?” → [ratdom_mikhail_04](#d-ratdom_mikhail_04)

    <span id="d-mikhail_visited"></span>**`mikhail_visited`** Mikhail: “I can't seem to find your brother Andor anywhere. He hasn't been back since he left yesterday.” — **effects:** sets stage 1 of [Search for Andor](../quests/andor.md#stage-1)

    - Next → [mikhail3](#d-mikhail3)

    <span id="d-mikhail_rats_start2a"></span>**`mikhail_rats_start2a`** Mikhail: “Another way to regain your strength is to eat some food. You can buy some for yourself from Mara at the town hall. But watch out - I hear that raw meat can sometimes give you food poisoning.”

    - Next → [mikhail_rats_start2b](#d-mikhail_rats_start2b)

    <span id="d-mikhail_rats_select"></span>**`mikhail_rats_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Rats!](../quests/mikhail_rats.md#stage-100))* → [mikhail_rats_complete2](#d-mikhail_rats_complete2)
    - branch 2 *(if reached stage 10 of [Rats!](../quests/mikhail_rats.md#stage-10))* → [mikhail_rats_continue](#d-mikhail_rats_continue)
    - branch 3 → [mikhail_rats_start](#d-mikhail_rats_start)

    <span id="d-mikhail_bread_select"></span>**`mikhail_bread_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Breakfast bread](../quests/mikhail_bread.md#stage-100))* → [mikhail_bread_complete2](#d-mikhail_bread_complete2)
    - branch 2 *(if reached stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10))* → [mikhail_bread_continue](#d-mikhail_bread_continue)
    - branch 3 → [mikhail_bread_start](#d-mikhail_bread_start)

    <span id="d-mikhail_andor2"></span>**`mikhail_andor2`** Mikhail: “Maybe he went into that supply cave again and got stuck. Or maybe he's in Leta's basement training with that wooden sword again. Please go look for him in town.”

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_present_20_1"></span>**`mikhail_present_20_1`** Mikhail: “Hm, thank you. Looks like you spent all your pocket money for this.” — **effects:** sets stage 40 of [Honor your parents](../quests/brv_present.md#stage-40)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_present_20_2"></span>**`mikhail_present_20_2`** Mikhail: “Thank you my child for this wonderful necklace. Oh and it is in our family colors!” — **effects:** sets stage 50 of [Honor your parents](../quests/brv_present.md#stage-50)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_present_20_3"></span>**`mikhail_present_20_3`** Mikhail: “Oh, where did you get the money to buy this? Maybe I don't want to know...” — **effects:** sets stage 60 of [Honor your parents](../quests/brv_present.md#stage-60)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_news_20"></span>**`mikhail_news_20`** Mikhail: “Did you go the dangerous way to Fallhaven?” — **effects:** sets stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40)

    - “Yes and someone in Fallhaven told me that he met Andor and that he was searching for a man called Lodar.” *(if reached stage 55 of [Search for Andor](../quests/andor.md#stage-55))* → [mikhail_news_30](#d-mikhail_news_30)
    - “Then I met a man called Lodar and he told me that Andor probably went to Nor City.” *(if NOT reached stage 55 of [Search for Andor](../quests/andor.md#stage-55); reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [mikhail_news_40](#d-mikhail_news_40)
    - “Not yet.” *(if NOT reached stage 80 of [Search for Andor](../quests/andor.md#stage-80); NOT reached stage 55 of [Search for Andor](../quests/andor.md#stage-55))* → [mikhail_news_50](#d-mikhail_news_50)

    <span id="d-mikhail_news_30"></span>**`mikhail_news_30`** Mikhail: “Did you find this Lodar?” — **effects:** sets stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40)

    - “Yes, and he told me that Andor probably went to Nor City.” *(if reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [mikhail_news_40](#d-mikhail_news_40)
    - “No, not yet.” *(if NOT reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [mikhail_news_50](#d-mikhail_news_50)

    <span id="d-mikhail_news_40"></span>**`mikhail_news_40`** Mikhail: “Did you go to Nor City?” — **effects:** sets stage 40 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-40)

    - “No, not yet.” → [mikhail_news_50](#d-mikhail_news_50)

    <span id="d-mikhail_news_60"></span>**`mikhail_news_60`** Mikhail: “Great! But where is he?”

    - “He just said that he couldn't come now. Then he ran away before I could ask him what he was up to.” → [mikhail_news_62](#d-mikhail_news_62)

    <span id="d-mikhail_achievements_20"></span>**`mikhail_achievements_20`** Mikhail: “This book is some kind of diary, in which you can record unusual experiences and achievements that you may have on your way.”

    - Next → [mikhail_achievements_30](#d-mikhail_achievements_30)

    <span id="d-brv_wh_delivery_mikhail2"></span>**`brv_wh_delivery_mikhail2`** Mikhail: “Anyway, it's been a very long time so please go look for your brother.”

    - “OK, bye.” → *conversation ends*
    - “I'm still looking for him.” → *conversation ends*
    - “Eh, you have to pay for it...” → [brv_wh_delivery_mikhail4](#d-brv_wh_delivery_mikhail4)

    <span id="d-brv_wh_delivery_mikhail3"></span>**`brv_wh_delivery_mikhail3`** Mikhail: “I already gave you his shield.”

    - Next → [brv_wh_delivery_mikhail2](#d-brv_wh_delivery_mikhail2)

    <span id="d-ratdom_mikhail_04"></span>**`ratdom_mikhail_04`** Mikhail: “We rats took over this village. I am Gruiik, their leader.” — **effects:** sets stage 10 of [More rats!](../quests/ratdom_mikhail.md#stage-10)

    - Next → [ratdom_mikhail_10](#d-ratdom_mikhail_10)

    <span id="d-mikhail3"></span>**`mikhail3`** Mikhail: “Never mind, he will probably be back soon.”

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_rats_start2b"></span>**`mikhail_rats_start2b`** Mikhail: “If that happens, perhaps the town priest can do something to help you. Otherwise, just rest until you feel better.”

    - Next → [mikhail_rats_start2c](#d-mikhail_rats_start2c)

    <span id="d-mikhail_rats_complete2"></span>**`mikhail_rats_complete2`** Mikhail: “Thanks for your help with the rats earlier. If you are hurt, use your bed over there to rest and regain your strength.”

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_rats_start"></span>**`mikhail_rats_start`** Mikhail: “I saw some rats out back in our garden earlier. Could you please go kill any rats that you see out there?” — **effects:** sets stage 10 of [Rats!](../quests/mikhail_rats.md#stage-10)

    - “I have already dealt with the rats.” *(if hand over 2× [Small rat tail](../items/tail_trainingrat.md))* → [mikhail_rats_complete](#d-mikhail_rats_complete)
    - “OK, I'll go check out in our garden.” → [mikhail_rats_start2](#d-mikhail_rats_start2)

    <span id="d-mikhail_bread_complete2"></span>**`mikhail_bread_complete2`** Mikhail: “Thanks for the bread earlier.”

    - “You're welcome.” → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_bread_start"></span>**`mikhail_bread_start`** Mikhail: “Oh, I almost forgot. If you have time, please go see Mara at the town hall and buy me some more bread.” — **effects:** sets stage 10 of [Breakfast bread](../quests/mikhail_bread.md#stage-10)

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_news_50"></span>**`mikhail_news_50`** Mikhail: “Thank you my child. Keep on searching for Andor.”

    - Next → [mikhail_default](#d-mikhail_default)

    <span id="d-mikhail_news_62"></span>**`mikhail_news_62`** Mikhail: “[While shaking his head] Oh $playername, you have disappointed me.”

    - Next → [mikhail_news_64](#d-mikhail_news_64)

    <span id="d-mikhail_achievements_30"></span>**`mikhail_achievements_30`** Mikhail: “Would you like to have it?”

    - “Yes, sounds great.” → [mikhail_achievements_50](#d-mikhail_achievements_50)
    - “No, thanks.” → [mikhail_achievements_40](#d-mikhail_achievements_40)

    <span id="d-brv_wh_delivery_mikhail4"></span>**`brv_wh_delivery_mikhail4`** Mikhail: “Ah, yes, I almost forgot. Here you are.” — **effects:** gives 10× [Gold coins](../items/gold.md)

    - “Thanks. I'm on my way again, bye.” → *conversation ends*
    - “Hmm... Bye” → *conversation ends*

    <span id="d-ratdom_mikhail_10"></span>**`ratdom_mikhail_10`** Mikhail: “However, there are two-legs running around in my garden again. Go and kill them.” — **effects:** sets stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20)

    - “I'll have a look.” → [ratdom_mikhail_10_10](#d-ratdom_mikhail_10_10)
    - “I would never do that!” → [ratdom_mikhail_10_10](#d-ratdom_mikhail_10_10)

    <span id="d-mikhail_rats_start2c"></span>**`mikhail_rats_start2c`** Mikhail: “Me, I can't really afford the meat, so I just stick to my bread!”

    - Next → [mikhail_rats_start3](#d-mikhail_rats_start3)

    <span id="d-mikhail_news_64"></span>**`mikhail_news_64`** [Valentina](../monsters/crossglen_valentina.md): “Mikhail! Don't you dare talk to our child like that!” — **effects:** sets stage 20 of [Darkness in the Daylight and Shadows - Non displayed (hidden flag)](../quests/dds_nd.md#stage-20)

    - “I better go.” → [mikhail_news_66](#d-mikhail_news_66)
    - “Sigh.” → [mikhail_news_66](#d-mikhail_news_66)

    <span id="d-mikhail_achievements_50"></span>**`mikhail_achievements_50`** Mikhail: “Here you are.” — **effects:** sets stage 1 of [Unusual experiences and achievements](../quests/achievements.md#stage-1)


    <span id="d-mikhail_achievements_40"></span>**`mikhail_achievements_40`** Mikhail: “No problem. I won't bother you with it again.” — **effects:** sets stage 1 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-1)


    <span id="d-mikhail_rats_start3"></span>**`mikhail_rats_start3`** Mikhail: “Also, don't forget to check your inventory. You probably still have that old ring I gave you. Make sure you wear it.”

    - “OK, I understand. I can rest here if I get hurt, and I should check my inventory for useful items.” → [mikhail_rats_start3a](#d-mikhail_rats_start3a)

    <span id="d-mikhail_news_66"></span>**`mikhail_news_66`** Mikhail: “[Loudly complaining] When shall we three meet Andor again?”

    - “In thunder, lightning or on rain?” → *conversation ends*
    - “Now I'm definitely going.” → *conversation ends*

    <span id="d-mikhail_rats_start3a"></span>**`mikhail_rats_start3a`** Mikhail: “One more thing: Look at that basket on the floor over there. It belongs to Andor and he might have left something useful inside.”

    - Next → [mikhail_default](#d-mikhail_default)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines added, 9 lines changed |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line changed<br>· text: “As I said, Andor went out yesterday and hasn't been back since. I'm s…” → “As I said, Andor went out and hasn't been back since. I worry about h…” |
| [v0.7.10](../versions/0.7.10.md) | Dialogue: 1 line changed |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 10 lines added, 1 line changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 4 lines changed<br>· text: “Oh, you are such a good son.” → “Oh, you are such a nice child.”<br>· text: “Oh you did? Wow, thanks a lot for your help! If you are hurt, use you…” → “Oh you did? Wow, thanks a lot for your help! Please take Andor's trai…” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 5 lines added, 1 line changed |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 4 lines added, 1 line changed |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 17 lines added, 2 lines changed |
| [v0.8.6](../versions/0.8.6.md) | Dialogue: 1 line changed<br>· text: “One more thing: Look at that basket on the floor over there. It belon…” → “One more thing: Look at that basket on the floor over there. It belon…” |
| [v0.8.6.1](../versions/0.8.6.1.md) | Dialogue: 3 lines changed |
| [v0.8.7](../versions/0.8.7.md) | Dialogue: 1 line changed<br>· text: “I saw some rats out back in our garden earlier. Could you please go k…” → “I saw some rats out back in our garden earlier. Could you please go k…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 5 lines added, 2 lines changed |
| [v0.8.15](../versions/0.8.15.md) | horizontalFlipChance added (100) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mikhail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mikhail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mikhail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mikhail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `mikhail` · Data from v0.8.18</small>
