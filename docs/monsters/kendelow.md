# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Kendelow

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
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Carrot](../items/carrot.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

## Found on

- [remgard_tavern0](../maps/remgard_tavern0.md)

## Quests

- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 21

??? quote "Dialogue (24 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kendelow"></span>**`kendelow`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [kendelow_1](#d-kendelow_1)
    - branch 2 → [kendelow_2](#d-kendelow_2)

    <span id="d-kendelow_1"></span>**`kendelow_1`** Kendelow: “I heard that you helped us get rid of that witch Algangror. Thank you.”

    - Next → [kendelow_d](#d-kendelow_d)

    <span id="d-kendelow_2"></span>**`kendelow_2`** Kendelow: “Welcome to my tavern. I hope you will find your stay a pleasant one.”

    - Next → [kendelow_d](#d-kendelow_d)

    <span id="d-kendelow_d"></span>**`kendelow_d`** Kendelow: “How may I be of service?”

    - “What is there to do around here?” → [kendelow_3](#d-kendelow_3)
    - “Do you have anything to trade?” → [kendelow_shop](#d-kendelow_shop)
    - “Are there any rooms available?” → [kendelow_room_1](#d-kendelow_room_1)
    - “Actually, I am wondering if it would be possible if I could cook some meat in your kitchen?” → [kendelow_meat](#d-kendelow_meat)

    <span id="d-kendelow_3"></span>**`kendelow_3`** Kendelow: “Most people here in Remgard tend to their crops. Other than that, I hear that Arnal the armorer over on the western shore has some good business trading.”

    - Next → [kendelow_4](#d-kendelow_4)

    <span id="d-kendelow_shop"></span>**`kendelow_shop`** Kendelow: “Oh sure. Here, have a look.”

    - Next → *shop opens*

    <span id="d-kendelow_room_1"></span>**`kendelow_room_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-21))* → [kendelow_room_2](#d-kendelow_room_2)
    - branch 2 → [kendelow_room_3](#d-kendelow_room_3)

    <span id="d-kendelow_meat"></span>**`kendelow_meat`** Kendelow: “No, sorry. I can't let you use my kitchen. But...”

    - Next → [gael_cook_10](#d-gael_cook_10)

    <span id="d-kendelow_4"></span>**`kendelow_4`** Kendelow: “Also, we usually get a lot of visitors here in the tavern. Lately, it has been a lot fewer people in here though, with the closing of the bridge because of those missing people and all.”

    - Next → [kendelow_5](#d-kendelow_5)

    <span id="d-kendelow_room_2"></span>**`kendelow_room_2`** Kendelow: “You have already rented my last room. We don't have any more rooms other than that one.”


    <span id="d-kendelow_room_3"></span>**`kendelow_room_3`** Kendelow: “Why, yes, as a matter of fact, there is. I have one very fine room available upstairs.”

    - Next → [kendelow_room_4](#d-kendelow_room_4)

    <span id="d-gael_cook_10"></span>**`gael_cook_10`** Kendelow: “I could use some extra gold. So I can cook them for you for let's say 30 gold a piece.”

    - “Well, here is 1 piece and 30 gold.” *(if pay 30 gold; hand over 1× [Meat](../items/meat.md))* → [get_one_cooked_meat](#d-get_one_cooked_meat)
    - “OK, I have 5 pieces and 150 gold.” *(if pay 150 gold; hand over 5× [Meat](../items/meat.md))* → [get_five_cooked_meat](#d-get_five_cooked_meat)
    - “Here, I have 10 pieces that I would like cooked. Here are 300 gold pieces too.” *(if pay 300 gold; hand over 10× [Meat](../items/meat.md))* → [get_ten_cooked_meat](#d-get_ten_cooked_meat)
    - “I'm hungry! Here are 20 pieces and 600 gold.” *(if pay 600 gold; hand over 20× [Meat](../items/meat.md))* → [get_twenty_cooked_meat](#d-get_twenty_cooked_meat)
    - “Oh, my mistake, I forgot that I have no meat.” *(if NOT carry 1× [Meat](../items/meat.md))* → *conversation ends*
    - “Oops, I'm still poor. I can't afford to pay your price.” *(if NOT have 30 gold)* → *conversation ends*

    <span id="d-kendelow_5"></span>**`kendelow_5`** Kendelow: “On your way in, maybe you noticed that we even have a visit from the Knights of Elythom here in the tavern? It seems that more and more people are becoming aware of the hospitality of Remgard.”

    - “Thank you. I had some other questions.” → [kendelow_d](#d-kendelow_d)

    <span id="d-kendelow_room_4"></span>**`kendelow_room_4`** Kendelow: “The previous tenant left in a hurry some days ago.”

    - Next → [kendelow_room_5](#d-kendelow_room_5)

    <span id="d-get_one_cooked_meat"></span>**`get_one_cooked_meat`** Kendelow: “Only one? That's no problem. Here's your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_five_cooked_meat"></span>**`get_five_cooked_meat`** Kendelow: “Just five? That's no problem. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_ten_cooked_meat"></span>**`get_ten_cooked_meat`** Kendelow: “10 meat at once? That's no problem. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-get_twenty_cooked_meat"></span>**`get_twenty_cooked_meat`** Kendelow: “20 meat at once?! You may even love this stuff more than I do. Here's all your cooked meat.” — **effects:** gives [Cooked meat](../items/meat_cooked.md)


    <span id="d-kendelow_room_5"></span>**`kendelow_room_5`** Kendelow: “You may rent the room for as long as you like for only 600 gold.”

    - “600 gold, are you mad!? That's a fortune.” → [kendelow_room_6s](#d-kendelow_room_6s)
    - “Is there anything you can do to lower the price?” → [kendelow_room_6s](#d-kendelow_room_6s)
    - “I'll take it. Here is the gold.” *(if pay 600 gold)* → [kendelow_room_8](#d-kendelow_room_8)
    - “I don't have that much gold.” → [kendelow_room_7](#d-kendelow_room_7)

    <span id="d-kendelow_room_6s"></span>**`kendelow_room_6s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [kendelow_room_6b](#d-kendelow_room_6b)
    - branch 2 → [kendelow_room_6a](#d-kendelow_room_6a)

    <span id="d-kendelow_room_8"></span>**`kendelow_room_8`** Kendelow: “Thank you. The room is upstairs. You may rent it for as long as you wish.” — **effects:** sets stage 21 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-21)


    <span id="d-kendelow_room_7"></span>**`kendelow_room_7`** Kendelow: “You are welcome to return once you have the gold, if you are still interested.”

    - Next → [kendelow_d](#d-kendelow_d)

    <span id="d-kendelow_room_6b"></span>**`kendelow_room_6b`** Kendelow: “Since you helped us here in Remgard with that witch Algangror, I am prepared to offer you a discount. How about we say 400 gold for it instead?”

    - “I'll take it. Here is the gold.” *(if pay 400 gold)* → [kendelow_room_8](#d-kendelow_room_8)
    - “I don't have that much gold.” → [kendelow_room_7](#d-kendelow_room_7)

    <span id="d-kendelow_room_6a"></span>**`kendelow_room_6a`** Kendelow: “The price is fixed. I cannot go around handing out discounts to just anyone. Also, keep in mind that you may rent it for as long as you wish.”

    - “I'll take it. Here is the gold.” *(if pay 600 gold)* → [kendelow_room_8](#d-kendelow_room_8)
    - “I don't have that much gold.” → [kendelow_room_7](#d-kendelow_room_7)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kendelow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kendelow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kendelow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kendelow.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `kendelow` · Data from v0.8.18</small>
