---
description: "Facutloni is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Starts Delivery, Inventory."
---

# ![](../assets/icons/monsters/monsters_ld1_135.png){ .sprite } Facutloni

**Where to find Facutloni:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_boss)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_135.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Delivery](../quests/brv_wh_delivery.md), [Inventory](../quests/brv_wh.md) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [Delivery](../quests/brv_wh_delivery.md): stages 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130
- [Inventory](../quests/brv_wh.md): stages 10, 900
- [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md): stages 1, 2, 3
- [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md): stages 1, 2, 3

## Dialogue simulator

Talk to Facutloni as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_boss.json" data-npc="Facutloni" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (35 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_boss"></span>**`brv_wh_boss`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 3 of [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md#stage-3))* → [brv_wh_boss_900_10](#d-brv_wh_boss_900_10)
    - branch 2 *(if reached stage 2 of [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md#stage-2))* → [brv_wh_delivery_boss_10_10_yes](#d-brv_wh_delivery_boss_10_10_yes)
    - branch 3 *(if reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10))* → [brv_wh_delivery_boss_10_10](#d-brv_wh_delivery_boss_10_10)
    - branch 4 *(if reached stage 3 of [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-3))* → [brv_wh_delivery_boss_10](#d-brv_wh_delivery_boss_10)
    - branch 5 *(if reached stage 2 of [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2))* → [brv_wh_boss_10_32](#d-brv_wh_boss_10_32)
    - branch 6 *(if reached stage 900 of [Inventory](../quests/brv_wh.md#stage-900))* → [brv_wh_delivery_boss_10](#d-brv_wh_delivery_boss_10)
    - branch 7 *(if reached stage 10 of [Inventory](../quests/brv_wh.md#stage-10))* → [brv_wh_boss_10_10](#d-brv_wh_boss_10_10)
    - branch 8 → [brv_wh_boss_10](#d-brv_wh_boss_10)

    <span id="d-brv_wh_boss_900_10"></span>**`brv_wh_boss_900_10`** Facutloni: “I have no work for you at the moment.”


    <span id="d-brv_wh_delivery_boss_10_10_yes"></span>**`brv_wh_delivery_boss_10_10_yes`** Facutloni: “That's nice to hear. Then you can now give me the... eh...330 gold pieces that you should have received from the sales.”

    - “Sure. Here you are.” *(if pay 330 gold)* → [brv_wh_delivery_boss_10_10_yes_10](#d-brv_wh_delivery_boss_10_10_yes_10)
    - “Uh, I had expenses along the way and I don't have all the gold anymore.” → [brv_wh_delivery_boss_10_10_yes_1](#d-brv_wh_delivery_boss_10_10_yes_1)

    <span id="d-brv_wh_delivery_boss_10_10"></span>**`brv_wh_delivery_boss_10_10`** Facutloni: “You are back. Did you deliver all of the items?”

    - “Yes. I delivered everything.” *(if reached stage 10 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-10); reached stage 20 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-20); reached stage 30 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-30); reached stage 40 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-40); reached stage 50 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-50); reached stage 60 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-60); reached stage 70 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-70); reached stage 80 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-80); reached stage 90 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-90); reached stage 100 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-100))* → [brv_wh_delivery_boss_10_10_yes](#d-brv_wh_delivery_boss_10_10_yes)
    - “Not yet.” → [brv_wh_delivery_boss_10_10_no](#d-brv_wh_delivery_boss_10_10_no)

    <span id="d-brv_wh_delivery_boss_10"></span>**`brv_wh_delivery_boss_10`** Facutloni: “Ah! You have finally returned, my new worker.”

    - “How may I be of service?” → [brv_wh_delivery_boss_20](#d-brv_wh_delivery_boss_20)
    - “What is it this time?” → [brv_wh_delivery_boss_20](#d-brv_wh_delivery_boss_20)
    - “Ah! You are still insolent.” → *conversation ends*

    <span id="d-brv_wh_boss_10_32"></span>**`brv_wh_boss_10_32`** Facutloni: “Good work! I am very pleased with you.” — **effects:** sets stage 900 of [Inventory](../quests/brv_wh.md#stage-900)

    - “I am glad. How much do I actually get for this work?” → [brv_wh_boss_10_90](#d-brv_wh_boss_10_90)

    <span id="d-brv_wh_boss_10_10"></span>**`brv_wh_boss_10_10`** Facutloni: “How do you get on with the work?”

    - “I'm not quite done yet. I just want to take a short break.” → [brv_wh_boss_10_12](#d-brv_wh_boss_10_12)
    - “Please tell me again, what I should do.” → [brv_wh_boss_40](#d-brv_wh_boss_40)
    - “I found 10 pairs of each item.” *(if reached stage 100 of [Inventory](../quests/brv_wh.md#stage-100); reached stage 101 of [Inventory](../quests/brv_wh.md#stage-101); reached stage 102 of [Inventory](../quests/brv_wh.md#stage-102); reached stage 103 of [Inventory](../quests/brv_wh.md#stage-103); reached stage 104 of [Inventory](../quests/brv_wh.md#stage-104); reached stage 105 of [Inventory](../quests/brv_wh.md#stage-105); reached stage 106 of [Inventory](../quests/brv_wh.md#stage-106); reached stage 107 of [Inventory](../quests/brv_wh.md#stage-107); reached stage 108 of [Inventory](../quests/brv_wh.md#stage-108); reached stage 109 of [Inventory](../quests/brv_wh.md#stage-109))* → [brv_wh_boss_10_20](#d-brv_wh_boss_10_20)

    <span id="d-brv_wh_boss_10"></span>**`brv_wh_boss_10`** Facutloni: “Hey! Are you the new worker?”

    - “Do you need any help?” → [brv_wh_boss_20](#d-brv_wh_boss_20)
    - “Insolence! Who do you think you are?” → *conversation ends*
    - “Sure.” → [brv_wh_boss_12](#d-brv_wh_boss_12)

    <span id="d-brv_wh_delivery_boss_10_10_yes_10"></span>**`brv_wh_delivery_boss_10_10_yes_10`** Facutloni: “Good job! I am glad that you work responsibly.” — **effects:** sets stage 2 of [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md#stage-2)

    - “And seriously.” → [brv_wh_delivery_boss_reward](#d-brv_wh_delivery_boss_reward)
    - “I travelled far and wide.” → [brv_wh_delivery_boss_reward](#d-brv_wh_delivery_boss_reward)

    <span id="d-brv_wh_delivery_boss_10_10_yes_1"></span>**`brv_wh_delivery_boss_10_10_yes_1`** Facutloni: “And then you walk into my sight? Go get my gold!”

    - “[Run]” → *conversation ends*
    - “Yes boss.” → *conversation ends*
    - “Oh, I just found the 330 gold pieces in my pocket. Please take it.” *(if pay 330 gold)* → [brv_wh_delivery_boss_10_10_yes_10](#d-brv_wh_delivery_boss_10_10_yes_10)

    <span id="d-brv_wh_delivery_boss_10_10_no"></span>**`brv_wh_delivery_boss_10_10_no`** Facutloni: “Then what are you standing there for?! Get out and deliver everything!”

    - “[Run]” → *conversation ends*
    - “Yes boss.” → *conversation ends*

    <span id="d-brv_wh_delivery_boss_20"></span>**`brv_wh_delivery_boss_20`** Facutloni: “I need someone to deliver all of the items that are in storage.”

    - Next → [brv_wh_delivery_boss_30](#d-brv_wh_delivery_boss_30)

    <span id="d-brv_wh_boss_10_90"></span>**`brv_wh_boss_10_90`** Facutloni: “Good work gives good wages! Here is 100 gold.” — **effects:** sets stage 3 of [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-3), gives 100× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*
    - “Old scrooge.” → [brv_wh_boss_10_92](#d-brv_wh_boss_10_92)

    <span id="d-brv_wh_boss_10_12"></span>**`brv_wh_boss_10_12`** Facutloni: “I'm not paying you to laze around! Back to work!”


    <span id="d-brv_wh_boss_40"></span>**`brv_wh_boss_40`** Facutloni: “OK: Go to the storage and take out an item.”

    - Next → [brv_wh_boss_42](#d-brv_wh_boss_42)

    <span id="d-brv_wh_boss_10_20"></span>**`brv_wh_boss_10_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 2× [Crystal globe](../items/brv_wh_item_00.md); hand over 2× [Plush pillow](../items/brv_wh_item_01.md); hand over 2× [Lyre](../items/brv_wh_item_02.md); hand over 2× [Yellow boot](../items/brv_wh_item_03.md); hand over 2× [Chandelier](../items/brv_wh_item_04.md); hand over 2× [Mysterious green something](../items/brv_wh_item_05.md); hand over 2× [Old, worn cape](../items/brv_wh_item_06.md); hand over 2× [Pretty porcelain figure](../items/brv_wh_item_07.md); hand over 2× [Striped hammer](../items/brv_wh_item_08.md); hand over 2× [Dusty old book](../items/brv_wh_item_09.md))* → [brv_wh_boss_10_30](#d-brv_wh_boss_10_30)
    - branch 2 → [brv_wh_boss_10_22](#d-brv_wh_boss_10_22)

    <span id="d-brv_wh_boss_20"></span>**`brv_wh_boss_20`** Facutloni: “I need someone to check if all the items are still in the storage.”

    - Next → [brv_wh_boss_22](#d-brv_wh_boss_22)

    <span id="d-brv_wh_boss_12"></span>**`brv_wh_boss_12`** Facutloni: “It took you long to get here! I hope you are not always that slow.”

    - Next → [brv_wh_boss_20](#d-brv_wh_boss_20)

    <span id="d-brv_wh_delivery_boss_reward"></span>**`brv_wh_delivery_boss_reward`** Facutloni: “That is serious. And here you have your well-deserved reward: 100 gold.” — **effects:** sets stage 130 of [Delivery](../quests/brv_wh_delivery.md#stage-130), sets stage 3 of [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md#stage-3), gives 100× [Gold coins](../items/gold.md)

    - “Thanks.” → *conversation ends*
    - “What the?” → [brv_wh_delivery_boss_scrooge](#d-brv_wh_delivery_boss_scrooge)

    <span id="d-brv_wh_delivery_boss_30"></span>**`brv_wh_delivery_boss_30`** Facutloni: “Come back to me when you have delivered all of the items. The order is not important. Here is the list of customers.” — **effects:** sets stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10), sets stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20), sets stage 30 of [Delivery](../quests/brv_wh_delivery.md#stage-30), sets stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40), sets stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50), sets stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60), sets stage 70 of [Delivery](../quests/brv_wh_delivery.md#stage-70), sets stage 80 of [Delivery](../quests/brv_wh_delivery.md#stage-80), sets stage 90 of [Delivery](../quests/brv_wh_delivery.md#stage-90), sets stage 100 of [Delivery](../quests/brv_wh_delivery.md#stage-100), sets stage 110 of [Delivery](../quests/brv_wh_delivery.md#stage-110), sets stage 120 of [Delivery](../quests/brv_wh_delivery.md#stage-120), gives 1× [Crystal globe](../items/brv_wh_item_00.md), gives 1× [Plush pillow](../items/brv_wh_item_01.md), gives 1× [Lyre](../items/brv_wh_item_02.md), gives 1× [Yellow boot](../items/brv_wh_item_03.md), gives 1× [Chandelier](../items/brv_wh_item_04.md), gives 1× [Mysterious green something](../items/brv_wh_item_05.md), gives 1× [Old, worn cape](../items/brv_wh_item_06.md), gives 1× [Pretty porcelain figure](../items/brv_wh_item_07.md), gives 1× [Striped hammer](../items/brv_wh_item_08.md), gives 1× [Dusty old book](../items/brv_wh_item_09.md), sets stage 1 of [Brimhaven warehouse delivery reward (hidden flag)](../quests/brv_wh_delivery_reward_nondisplay.md#stage-1), gives 1× [Facutloni's Docket](../items/facutloni_docket.md)

    - “It will be done.” → [brv_wh_delivery_boss_40](#d-brv_wh_delivery_boss_40)
    - “You want me to deliver these items to your customers?” → [brv_wh_delivery_boss_40](#d-brv_wh_delivery_boss_40)

    <span id="d-brv_wh_boss_10_92"></span>**`brv_wh_boss_10_92`** Facutloni: “What?”

    - “Thank you so much.” → *conversation ends*

    <span id="d-brv_wh_boss_42"></span>**`brv_wh_boss_42`** Facutloni: “Then go and look for the another item of the same kind. So then you'll have a pair of them.”

    - “A pair.” → [brv_wh_boss_44](#d-brv_wh_boss_44)

    <span id="d-brv_wh_boss_10_30"></span>**`brv_wh_boss_10_30`** Facutloni: “10 pairs - that is correct. So everything is in order.” — **effects:** sets stage 900 of [Inventory](../quests/brv_wh.md#stage-900), sets stage 2 of [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-2)

    - Next → [brv_wh_boss_10_32](#d-brv_wh_boss_10_32)

    <span id="d-brv_wh_boss_10_22"></span>**`brv_wh_boss_10_22`** Facutloni: “10 pairs! Great - but where are they? I don't see them.”

    - “Oh, I must have lost some. Wait a second...” → *conversation ends*

    <span id="d-brv_wh_boss_22"></span>**`brv_wh_boss_22`** Facutloni: “I always buy a pair of any item. So it would be best if you find the pairs.”

    - Next → [brv_wh_boss_24](#d-brv_wh_boss_24)

    <span id="d-brv_wh_delivery_boss_scrooge"></span>**`brv_wh_delivery_boss_scrooge`** Facutloni: “Pardon?”

    - “Thank you.” → *conversation ends*

    <span id="d-brv_wh_delivery_boss_40"></span>**`brv_wh_delivery_boss_40`** Facutloni: “Yes yes, hurry now. I have work to do here.”

    - “I'm going now.” → *conversation ends*
    - “Hope I get paid better this time.” → *conversation ends*

    <span id="d-brv_wh_boss_44"></span>**`brv_wh_boss_44`** Facutloni: “After that take another item, and look for the second one to get a pair again.”

    - Next → [brv_wh_boss_46](#d-brv_wh_boss_46)

    <span id="d-brv_wh_boss_24"></span>**`brv_wh_boss_24`** Facutloni: “Each time you find a pair, take it out of the storage bin!”

    - Next → [brv_wh_boss_30](#d-brv_wh_boss_30)

    <span id="d-brv_wh_boss_46"></span>**`brv_wh_boss_46`** Facutloni: “Do this for all pairs, until you have found every one.”

    - “Sounds easy.” → [brv_wh_boss_48](#d-brv_wh_boss_48)

    <span id="d-brv_wh_boss_30"></span>**`brv_wh_boss_30`** Facutloni: “Come back to me when you found all the pairs and tell me how many there are.” — **effects:** sets stage 10 of [Inventory](../quests/brv_wh.md#stage-10), sets stage 1 of [Brimhaven warehouse inventory reward (hidden flag)](../quests/brv_wh_reward_nondisplay.md#stage-1)

    - “OK. I'll be back in a minute.” → *conversation ends*
    - “Eh, what do you want me to do exactly?” → [brv_wh_boss_40](#d-brv_wh_boss_40)

    <span id="d-brv_wh_boss_48"></span>**`brv_wh_boss_48`** Facutloni: “If you have one item in hand, and in the next there is an item that doesn't match, then both items automatically go back to their bin. So be sure to take the items in pairs.”

    - Next → [brv_wh_boss_50](#d-brv_wh_boss_50)

    <span id="d-brv_wh_boss_50"></span>**`brv_wh_boss_50`** Facutloni: “Understood? Repeat it to me!”

    - “I shall get the items, one by one.” → [brv_wh_boss_52](#d-brv_wh_boss_52)
    - “Not necessary. I'll be back in a minute.” → *conversation ends*

    <span id="d-brv_wh_boss_52"></span>**`brv_wh_boss_52`** Facutloni: “And?”

    - “I shall find them in the right order: Pair after pair.” → [brv_wh_boss_60](#d-brv_wh_boss_60)

    <span id="d-brv_wh_boss_60"></span>**`brv_wh_boss_60`** Facutloni: “OK. Hurry now.”




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 24 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 11 lines added, 4 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_wh_boss` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_boss` |
    | Loot table | – |
    | Conversation | `brv_wh_boss` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:135` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_boss",
     "name": "Facutloni",
     "iconID": "monsters_ld1:135",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_boss",
     "phraseID": "brv_wh_boss"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
