---
description: "Gael is a non-player character (NPC) in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/monsters_karvis2_2.png){ .sprite } Gael

**Where to find Gael:** Fallhaven: [Mywild 20 houseright](../maps/mywild20_houseright.md#pin-npc-gael)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_karvis2_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Fallhaven |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Dialogue simulator

Talk to Gael as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/gael.json" data-npc="Gael" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (22 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gael"></span>**`gael`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Gison's mushroom soup](../items/gison_soup.md))* → [gael_soup](#d-gael_soup)
    - branch 2 *(if carry 1× [Nimael's vegetable soup](../items/nimael_soup.md))* → [gael_soup](#d-gael_soup)
    - branch 3 *(if carry 1× [Gison and Nimael's soup of the forest](../items/soup_forest.md))* → [gael_soup](#d-gael_soup)
    - branch 4 *(if carry 1× [Gloriosa mushroom soup](../items/gloriosa_mushroom_soup.md))* → [gael_soup](#d-gael_soup)
    - branch 5 *(if reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20))* → [gael_20](#d-gael_20)
    - branch 6 *(if reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10))* → [gael_10](#d-gael_10)
    - branch 7 → [gael_1](#d-gael_1)

    <span id="d-gael_soup"></span>**`gael_soup`** Gael: “I hate this smell!”

    - Next → [gael_soup_1](#d-gael_soup_1)

    <span id="d-gael_20"></span>**`gael_20`** Gael: “Hi kid. I am Gael, son of those people in the house over there.”

    - Next → [gael_20_1](#d-gael_20_1)

    <span id="d-gael_10"></span>**`gael_10`** Gael: “No, I am not Gison!”

    - “What?” → [gael_10_1](#d-gael_10_1)

    <span id="d-gael_1"></span>**`gael_1`** Gael: “Shut the door, please!”

    - “Sure.” → [gael_2](#d-gael_2)

    <span id="d-gael_soup_1"></span>**`gael_soup_1`** Gael: “You have some of that disgusting soup in your bag! I can smell it.”

    - Next → [gael_soup_2](#d-gael_soup_2)

    <span id="d-gael_20_1"></span>**`gael_20_1`** Gael: “I moved out here because I couldn't stand the suffocating smell of mushroom soup anymore. Or vegetable soup, for that matter.”

    - Next → [gael_20_2](#d-gael_20_2)

    <span id="d-gael_10_1"></span>**`gael_10_1`** Gael: “And no, I have no soup for anyone!”

    - “But...” → [gael_1](#d-gael_1)

    <span id="d-gael_2"></span>**`gael_2`** Gael: “From the outside.”

    - “Very friendly.” → *conversation ends*

    <span id="d-gael_soup_2"></span>**`gael_soup_2`** Gael: “Out with you!”


    <span id="d-gael_20_2"></span>**`gael_20_2`** Gael: “I like meat. Wolves, boars, dogs, puppies. Any kind, really.”

    - Next → [gael_20_3](#d-gael_20_3)

    <span id="d-gael_20_3"></span>**`gael_20_3`** Gael: “And snakes, of course. They give the finest meat of all.”

    - Next → [gael_20_4](#d-gael_20_4)

    <span id="d-gael_20_4"></span>**`gael_20_4`** Gael: “Cooked, grilled, baked, fried, stewed...ahh, snake meat - nothing compares to it!”

    - “Yes, I love it too!” → [gael_20_5](#d-gael_20_5)
    - “To each his own, I guess.” → [gael_20_5](#d-gael_20_5)
    - “Cooked meat? Who cooks your meat?” → [gael_cook](#d-gael_cook)

    <span id="d-gael_20_5"></span>**`gael_20_5`** Gael: “Now that I mention it: I am running out of meat. I'll have to go out hunting again.”

    - “Would you like me to give you some meat?” → [gael_20_6](#d-gael_20_6)
    - “Good luck! I am leaving then.” → *conversation ends*

    <span id="d-gael_cook"></span>**`gael_cook`** Gael: “I cook my own meat, thank you very much!”

    - “I've been looking for a way to cook my meat.” → [gael_cook_10](#d-gael_cook_10)

    <span id="d-gael_20_6"></span>**`gael_20_6`** Gael: “Really?”

    - “Oh, I just noticed that I don't have enough meat with me. I will be back soon with 10 pieces of meat, just you wait.” *(if NOT carry 10× [Meat](../items/meat.md))* → *conversation ends*
    - “Here, I have 10 nice pieces of meat for you. I cannot promise that it is all from snakes, though.” *(if hand over 10× [Meat](../items/meat.md))* → [gael_20_7](#d-gael_20_7)
    - “Here, I have 10 nice pieces of lamb meat for you. Maybe not as good as snake though.” *(if hand over 10× [Raw lamb meat](../items/lamb_meat_raw.md))* → [gael_20_7](#d-gael_20_7)
    - “Here, I have 8 nice pieces of snake meat for you.” *(if hand over 8× [Snake meat](../items/snake_meat.md))* → [gael_20_7](#d-gael_20_7)

    <span id="d-gael_cook_10"></span>**`gael_cook_10`** Gael: “I could use some extra gold. So I can cook them for you for let's say 30 gold a piece.”

    - “Well, here is 1 piece and 30 gold.” *(if pay 30 gold; hand over 1× [Meat](../items/meat.md))* → [get_one_cooked_meat](#d-get_one_cooked_meat)
    - “OK, I have 5 pieces and 150 gold.” *(if pay 150 gold; hand over 5× [Meat](../items/meat.md))* → [get_five_cooked_meat](#d-get_five_cooked_meat)
    - “Here, I have 10 pieces that I would like cooked. Here are 300 gold pieces too.” *(if pay 300 gold; hand over 10× [Meat](../items/meat.md))* → [get_ten_cooked_meat](#d-get_ten_cooked_meat)
    - “I'm hungry! Here are 20 pieces and 600 gold.” *(if pay 600 gold; hand over 20× [Meat](../items/meat.md))* → [get_twenty_cooked_meat](#d-get_twenty_cooked_meat)
    - “Oh, my mistake, I forgot that I have no meat.” *(if NOT carry 1× [Meat](../items/meat.md))* → *conversation ends*
    - “Oops, I'm still poor. I can't afford to pay your price.” *(if NOT have 30 gold)* → *conversation ends*

    <span id="d-gael_20_7"></span>**`gael_20_7`** Gael: “Excellent! In return, I can give you this nice little purse, made of the finest snake leather. Look here, isn't it beautiful?” — **effects:** gives 1× [Snake leather purse](../items/gael_purse.md)

    - “Wow, it is magnificent! Thank you!” → *conversation ends*

    <span id="d-get_one_cooked_meat"></span>**`get_one_cooked_meat`** Gael: “Only one? That's no problem. Here's your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_five_cooked_meat"></span>**`get_five_cooked_meat`** Gael: “Just five? That's no problem. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_ten_cooked_meat"></span>**`get_ten_cooked_meat`** Gael: “10 meat at once? That's no problem. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_twenty_cooked_meat"></span>**`get_twenty_cooked_meat`** Gael: “20 meat at once?! You may even love this stuff more than I do. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)




## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 16 lines added |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 6 lines added, 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `gael` |
    | Type (wiki) | NPC |
    | Spawn group | `gael` |
    | Loot table | – |
    | Conversation | `gael` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gael",
     "name": "Gael",
     "iconID": "monsters_karvis2:2",
     "spawnGroup": "gael",
     "phraseID": "gael"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
