# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Bela

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
| [Green apple](../items/apple_green.md) | 100% | 5 |
| [Red apple](../items/apple_red.md) | 100% | 5 |
| [Meat](../items/meat.md) | 100% | 5 |
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Carrot](../items/carrot.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 5 |
| [Milk](../items/milk.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

## Quests

- [A Wicked witch](../quests/wicked_witch.md): stages 10
- [A giant snake](../quests/bela_gsnake.md): stages 10, 90
- [You shall pass](../quests/undertell_barricades.md): stages 150
- [Room to rent (hidden flag)](../quests/fallhaventavern.md): stages 10

??? quote "Dialogue (31 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bela_gsnake"></span>**`bela_gsnake`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90); NOT reached stage 50 of [A Wicked witch](../quests/wicked_witch.md#stage-50); NOT reached stage 70 of [A Wicked witch](../quests/wicked_witch.md#stage-70); NOT reached stage 95 of [A Wicked witch](../quests/wicked_witch.md#stage-95); NOT reached stage 96 of [A Wicked witch](../quests/wicked_witch.md#stage-96))* → [bela_witch_10](#d-bela_witch_10)
    - branch 2 *(if reached stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90))* → [bela](#d-bela)
    - branch 3 *(if killed 1× [Giant snake](../monsters/giant_snake.md))* → [bela_gsnake_20](#d-bela_gsnake_20)
    - branch 4 *(if reached stage 10 of [Everything in order](../quests/remgard.md#stage-10))* → [bela_gsnake_1](#d-bela_gsnake_1)
    - branch 5 → [bela](#d-bela)

    <span id="d-bela_witch_10"></span>**`bela_witch_10`** Bela: “Did you hear about the kidnapping?”

    - “It wasn't me!” *(if reached stage 75 of [Immaculate kidnapping](../quests/Thieves02.md#stage-75))* → [bela_witch_15](#d-bela_witch_15)
    - “Someone kidnapped Ambelie?” *(if reached stage 76 of [Immaculate kidnapping](../quests/Thieves02.md#stage-76))* → [bela_witch_16](#d-bela_witch_16)
    - “No, I don't think so.” → [bela_witch_20](#d-bela_witch_20)
    - “Not now, I have something else to talk about.” *(if reached stage 140 of [You shall pass](../quests/undertell_barricades.md#stage-140); NOT reached stage 150 of [You shall pass](../quests/undertell_barricades.md#stage-150); have 4,850 gold)* → [bela_rain_gold_10](#d-bela_rain_gold_10)

    <span id="d-bela"></span>**`bela`** Bela: “Welcome to Fallhaven Tavern. Have a seat anywhere.”

    - “Let me see what food and drinks you have available.” → [bela_select](#d-bela_select)
    - “Are there any rooms available?” → [bela_room_select](#d-bela_room_select)
    - “Torilo suggested that I ask other tavern owners such as yourself about a 'business agreement' that you may have with a…” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-20) is 20)* → [bela_beer](#d-bela_beer)
    - “Do you have strawberries?” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-11) is 11)* → [bela_lytwing_strawberries](#d-bela_lytwing_strawberries)
    - “Please keep these 4,850 gold coins for safekeeping. Rain asked for you until he gets over his hangover, he'll come…” *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-140) is 140; pay 4,850 gold)* → [bela_rain](#d-bela_rain)

    <span id="d-bela_gsnake_20"></span>**`bela_gsnake_20`** Bela: “You are back!”

    - “Sure. And your little snake monster is no more.” → [bela_gsnake_21](#d-bela_gsnake_21)

    <span id="d-bela_gsnake_1"></span>**`bela_gsnake_1`** Bela: “I'm glad you are still alive!”

    - “As you know I can handle myself.” → [bela](#d-bela)
    - “Why? Has something happened?” → [bela_gsnake_2](#d-bela_gsnake_2)

    <span id="d-bela_witch_15"></span>**`bela_witch_15`** Bela: “[Looking extermely confused and terrified] ... Well, why would it be you?”

    - “Nevermind.” → [bela_witch_20](#d-bela_witch_20)

    <span id="d-bela_witch_16"></span>**`bela_witch_16`** Bela: “[Looking extermely confused] ... Who?”

    - “Nevermind” → [bela_witch_20](#d-bela_witch_20)

    <span id="d-bela_witch_20"></span>**`bela_witch_20`** Bela: “Well, while you were off hunting and killing that giant snake, I had a customer.”

    - “So?” → [bela_witch_25](#d-bela_witch_25)

    <span id="d-bela_rain_gold_10"></span>**`bela_rain_gold_10`** Bela: “What is more important than a kidnapping?”

    - “Please keep these 4,850 gold coins for safekeeping. Rain has asked for you until he gets over his hangover, he'll come…” *(if pay 4,850 gold)* → [bela_rain](#d-bela_rain)

    <span id="d-bela_select"></span>**`bela_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120))* → [bela_trade_2](#d-bela_trade_2)
    - branch 2 → [bela_trade_1](#d-bela_trade_1)

    <span id="d-bela_room_select"></span>**`bela_room_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Room to rent (hidden flag)](../quests/fallhaventavern.md#stage-10))* → [bela_room_3](#d-bela_room_3)
    - branch 2 → [bela_room_1](#d-bela_room_1)

    <span id="d-bela_beer"></span>**`bela_beer`** Bela: “Who is Torilo?”

    - “Come on. You know who Torilo is.” → [bela_beer_10](#d-bela_beer_10)

    <span id="d-bela_lytwing_strawberries"></span>**`bela_lytwing_strawberries`** Bela: “I don't, but I believe the potion merchant here in Fallhaven has some.”

    - “OK.” → [bela](#d-bela)

    <span id="d-bela_rain"></span>**`bela_rain`** Bela: “Definitely. Count on me. Glad you could help him, the poor sod.” — **effects:** sets stage 150 of [You shall pass](../quests/undertell_barricades.md#stage-150), removes monsters from fallhaven_nw, spawns monsters on fallhaven_nw


    <span id="d-bela_gsnake_21"></span>**`bela_gsnake_21`** Bela: “Incredible! Let's feast now! Everyone have a free drink!” — **effects:** sets stage 90 of [A giant snake](../quests/bela_gsnake.md#stage-90), gives 1× [Mead](../items/mead.md)


    <span id="d-bela_gsnake_2"></span>**`bela_gsnake_2`** Bela: “Did you not hear of the most dangerous snake ever seen? It has been spotted on Fallhaven's southern border.”

    - “A snake?” → [bela_gsnake_3](#d-bela_gsnake_3)
    - “No, I didn't hear, and I also don't want to. Please give me something to drink.” → *shop opens*

    <span id="d-bela_witch_25"></span>**`bela_witch_25`** Bela: “A customer with a very interesting report about a kidnapped girl and a witch.” — **effects:** sets stage 10 of [A Wicked witch](../quests/wicked_witch.md#stage-10)

    - “Is this customer still here?” → [bela_witch_30](#d-bela_witch_30)

    <span id="d-bela_trade_2"></span>**`bela_trade_2`** [Bela](../monsters/bela_2.md): “I have some new soup now, from Gison and Nimael. It's expensive, but worth the money.”

    - “Sounds interesting.” → *shop opens*

    <span id="d-bela_trade_1"></span>**`bela_trade_1`** Bela: “I have a variety of food and drinks.”

    - “OK. Please show me.” → *shop opens*

    <span id="d-bela_room_3"></span>**`bela_room_3`** Bela: “I hope the room suits your needs. It's the last room down at the end of the hall.”

    - “Thank you. There was something else I wanted to talk about.” → [bela](#d-bela)
    - “Thanks, bye.” → *conversation ends*

    <span id="d-bela_room_1"></span>**`bela_room_1`** Bela: “A room will cost you only 10 gold.”

    - “[Buy for 10 gold]” *(if pay 10 gold)* → [bela_room_2](#d-bela_room_2)
    - “I really need to rest but I don't have 10 gold. I will wash the dishes. [Wash the dishes]” *(if NOT have 10 gold; reached stage 1 of [The ruthless Crackshot](../quests/Thieves03.md#stage-1))* → [bela_room_2](#d-bela_room_2)
    - “Umar sent me.” *(if reached stage 20 of [misc_nondisplay (hidden flag)](../quests/misc_nondisplay.md#stage-20))* → [bela_room_2](#d-bela_room_2)
    - “No thanks.” → [bela](#d-bela)

    <span id="d-bela_beer_10"></span>**`bela_beer_10`** Bela: “No, really, I don't know anyone by that name.”

    - “Sure you do. He is the owner of the Foaming flask.” → [bela_beer_20](#d-bela_beer_20)

    <span id="d-bela_gsnake_3"></span>**`bela_gsnake_3`** Bela: “No normal snake. Huge as a house! Making noise like a hundred galloping horses!”

    - Next → [bela_gsnake_4](#d-bela_gsnake_4)

    <span id="d-bela_witch_30"></span>**`bela_witch_30`** Bela: “That's the thing. He is no longer here. He just left before you walked in.”

    - Next → [bela_witch_31](#d-bela_witch_31)

    <span id="d-bela_room_2"></span>**`bela_room_2`** Bela: “OK. Take the last room down at the end of the hall.” — **effects:** sets stage 10 of [Room to rent (hidden flag)](../quests/fallhaventavern.md#stage-10)

    - “Thank you. There was something else I wanted to talk about.” → [bela](#d-bela)
    - “Thanks, bye.” → *conversation ends*

    <span id="d-bela_beer_20"></span>**`bela_beer_20`** Bela: “the 'Foaming flask', what is that? Is that a tavern?”

    - “I've had enough of you. If you want to play dumb, then I don't have time for you.” → *conversation ends*

    <span id="d-bela_gsnake_4"></span>**`bela_gsnake_4`** Bela: “Few people dare to walk outside of the city nowadays.”

    - “Sounds interesting.” → [bela_gsnake_10](#d-bela_gsnake_10)
    - “Thanks for the warning. I'll avoid that area.” → [bela_gsnake_5](#d-bela_gsnake_5)

    <span id="d-bela_witch_31"></span>**`bela_witch_31`** Bela: “You should ask around town if anyone has seen or heard about it.”

    - “OK. I think I will do that. Thanks.” → *conversation ends*
    - “OK, but first please give me something to drink.” → *shop opens*

    <span id="d-bela_gsnake_10"></span>**`bela_gsnake_10`** Bela: “Oh no - what have I done? I shouldn't have talked of the giant snake. Promise me you won't go there!”

    - “Well, if it makes you happy.” → [bela_gsnake_5](#d-bela_gsnake_5)
    - “Of course I'll go there.” → [bela_gsnake_11](#d-bela_gsnake_11)

    <span id="d-bela_gsnake_5"></span>**`bela_gsnake_5`** Bela: “Good. Enough of such dark words - now go, have a seat anywhere.”

    - “Let me see what food and drinks you have available.” → *shop opens*
    - “Are there any rooms available?” → [bela_room_select](#d-bela_room_select)

    <span id="d-bela_gsnake_11"></span>**`bela_gsnake_11`** Bela: “What a waste of such a young, promising life! Well...don't forget to pay your tab before you leave my tavern.” — **effects:** spawns monsters on gapfiller2, sets stage 10 of [A giant snake](../quests/bela_gsnake.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 2 lines changed<br>· text: “Thanks. Take the last room down at the end of the hall.” → “OK. Take the last room down at the end of the hall.” |
| [v0.7.13](../versions/0.7.13.md) | phraseID: bela → bela_gsnake<br>Dialogue: 13 lines added, 1 line changed |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 3 lines added, 1 line changed |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 7 lines added, 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines added, 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `bela` · Data from v0.8.18</small>
