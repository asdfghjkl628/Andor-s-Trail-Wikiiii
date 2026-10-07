# ![](../assets/icons/monsters/monsters_men2_9.png){ .sprite } Torilo

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_9.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `torilo` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Foaming Flask Tavern |
| **Introduced** | v0.7.0 or earlier |

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
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Bread](../items/bread.md) | 100% | 5 |
| [Mushroom](../items/mushroom.md) | 100% | 5 |
| [Eggs](../items/eggs.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |
| [Pear](../items/pear.md) | 100% | 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [foaming_flask](../maps/foaming_flask.md) | Foaming Flask Tavern | 1 | – |


## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 20
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Torilo. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/torilo_1.json" data-npc="Torilo" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-torilo_1"></span>**`torilo_1`** Torilo: “Welcome to the Foaming Flask tavern. We welcome all travelers in here.”

    - “Thank you. Are you the innkeeper here?” → [torilo_2](#d-torilo_2)
    - “Have you seen a boy called Rincel around here recently?” *(if reached stage 41 of [Uncertain cause](../quests/wrye.md#stage-41))* → [torilo_rincel_1](#d-torilo_rincel_1)
    - “Hey, I noticted all of those beer barrels outside and all those drunk guards over there.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10) is 10)* → [torilo_beer](#d-torilo_beer)

    <span id="d-torilo_2"></span>**`torilo_2`** Torilo: “I am Torilo, the proprietor of this establishment. Please have a seat anywhere you like.”

    - “Can I see what you have available for food and drink?” → [torilo_shop_1](#d-torilo_shop_1)
    - “Do you have somewhere I can rest?” → [torilo_rest_select](#d-torilo_rest_select)
    - “Are those guards always shouting and yelling that much?” → [torilo_guards_1](#d-torilo_guards_1)

    <span id="d-torilo_rincel_1"></span>**`torilo_rincel_1`** Torilo: “Rincel? No, not that I can recall. Actually, we don't get many children in here. *chuckle*”

    - Next → [torilo_default](#d-torilo_default)

    <span id="d-torilo_beer"></span>**`torilo_beer`** Torilo: “OK, and this is your business why?”

    - “Well, of course it is not my business, but I am just wondering...” → [torilo_beer_10](#d-torilo_beer_10)

    <span id="d-torilo_shop_1"></span>**`torilo_shop_1`** Torilo: “Absolutely. We have a wide selection of food and beverages.”

    - Next → *shop opens*

    <span id="d-torilo_rest_select"></span>**`torilo_rest_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-10))* → [torilo_rest_1](#d-torilo_rest_1)
    - branch 2 → [torilo_rest_3](#d-torilo_rest_3)

    <span id="d-torilo_guards_1"></span>**`torilo_guards_1`** Torilo: “*Sigh* Yes. Those guards have been here for quite some time now.”

    - Next → [torilo_guards_2](#d-torilo_guards_2)

    <span id="d-torilo_default"></span>**`torilo_default`** Torilo: “Was there anything else you wanted?”

    - “Can I see what you have available for food and drink?” → [torilo_shop_1](#d-torilo_shop_1)
    - “Are those guards always shouting and yelling that much?” → [torilo_guards_1](#d-torilo_guards_1)
    - “Have you seen a boy called Rincel around here recently?” *(if reached stage 41 of [Uncertain cause](../quests/wrye.md#stage-41))* → [torilo_rincel_1](#d-torilo_rincel_1)

    <span id="d-torilo_beer_10"></span>**`torilo_beer_10`** Torilo: “Wondering what?”

    - “Why you have so much beer for such a small-sized tavern and where you got it? I would like some to bring home to father.” → [torilo_beer_20](#d-torilo_beer_20)
    - “Why you're such a jerk?” → [torilo_beer_jerk](#d-torilo_beer_jerk)

    <span id="d-torilo_rest_1"></span>**`torilo_rest_1`** Torilo: “Yes, you already rented the back room.”

    - Next → [torilo_rest_2](#d-torilo_rest_2)

    <span id="d-torilo_rest_3"></span>**`torilo_rest_3`** Torilo: “Oh yes. We have a very comfortable back room here in the Foaming Flask tavern.”

    - Next → [torilo_rest_4](#d-torilo_rest_4)

    <span id="d-torilo_guards_2"></span>**`torilo_guards_2`** Torilo: “They seem to be looking for something or someone, but I am not sure who or what.”

    - Next → [torilo_guards_3](#d-torilo_guards_3)

    <span id="d-torilo_beer_20"></span>**`torilo_beer_20`** Torilo: “Well, for as why I have so much, that is none of your business. As for where I got it, that information will cost you.”

    - “What? Are you asking me to buy information from you? Why would I want to do that?” → [torilo_beer_30](#d-torilo_beer_30)

    <span id="d-torilo_beer_jerk"></span>**`torilo_beer_jerk`** Torilo: “Well, it's because of little snot-nosed kids like you”


    <span id="d-torilo_rest_2"></span>**`torilo_rest_2`** Torilo: “Please feel free to use it in any way you like. I hope you can get some sleep even with these guards yelling their songs.”

    - “Thanks.” → [torilo_default](#d-torilo_default)

    <span id="d-torilo_rest_4"></span>**`torilo_rest_4`** Torilo: “Available for only 250 gold. Then you can use it as much as you like.”

    - “250 gold? Sure, that's nothing to me. Here you go.” *(if pay 250 gold)* → [torilo_rest_6](#d-torilo_rest_6)
    - “250 gold is a lot, but I guess it is worth it. Here you go.” *(if pay 250 gold)* → [torilo_rest_6](#d-torilo_rest_6)
    - “That sounds a bit too much for me.” → [torilo_rest_5](#d-torilo_rest_5)

    <span id="d-torilo_guards_3"></span>**`torilo_guards_3`** Torilo: “I hope the Shadow watches over us so that nothing bad happens to the Foaming Flask tavern because of them.”

    - Next → [torilo_default](#d-torilo_default)

    <span id="d-torilo_beer_30"></span>**`torilo_beer_30`** Torilo: “Well, for the same reason why my bed is so expensive to rent...It's valuable.”

    - “Forget it.” → *conversation ends*
    - “Funny, I thought it was because you are a jerk.” → *conversation ends*
    - “Oh, fine! What do you want? Gold? How much?” → [torilo_beer_40](#d-torilo_beer_40)

    <span id="d-torilo_rest_6"></span>**`torilo_rest_6`** Torilo: “Thank you. The room is now rented to you.” — **effects:** sets stage 10 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-10)

    - Next → [torilo_rest_2](#d-torilo_rest_2)

    <span id="d-torilo_rest_5"></span>**`torilo_rest_5`** Torilo: “Oh well, it's your loss.”

    - Next → [torilo_default](#d-torilo_default)

    <span id="d-torilo_beer_40"></span>**`torilo_beer_40`** Torilo: “Hmm...let me think...how does 10,000 gold sound?”

    - “That sounds fair. Take it. Now the information please!” *(if pay 10,000 gold)* → [torilo_beer_pay](#d-torilo_beer_pay)
    - “That sounds ridiculous! I won't pay that.” *(if have 10,000 gold)* → [torilo_beer_bribe7500](#d-torilo_beer_bribe7500)
    - “I can't afford that.” *(if NOT have 10,000 gold)* → [torilo_beer_bribe7500](#d-torilo_beer_bribe7500)

    <span id="d-torilo_beer_pay"></span>**`torilo_beer_pay`** Torilo: “Oh, I love the sound of clanking coins. Anyways...myself and other tavern owners have a 'business agreement' with a group of 'distributors'.”

    - “What does that mean?” → [torilo_beer_pay_10](#d-torilo_beer_pay_10)

    <span id="d-torilo_beer_bribe7500"></span>**`torilo_beer_bribe7500`** Torilo: “OK. How does 7,500 gold sound?”

    - “That sounds fair. Take it. Now the information please!” *(if pay 7,500 gold)* → [torilo_beer_pay](#d-torilo_beer_pay)
    - “That still sounds ridiculous and I won't pay it.” *(if have 7,500 gold)* → [torilo_beer_bribe6000](#d-torilo_beer_bribe6000)
    - “I can't afford that.” *(if NOT have 7,500 gold)* → [torilo_beer_bribe6000](#d-torilo_beer_bribe6000)

    <span id="d-torilo_beer_pay_10"></span>**`torilo_beer_pay_10`** Torilo: “It means that that is all I will tell you and I suggest you talk to another tavern owner.” — **effects:** sets stage 20 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-20)


    <span id="d-torilo_beer_bribe6000"></span>**`torilo_beer_bribe6000`** Torilo: “OK. How does 6,000 gold sound?”

    - “That sounds ridiculous too, but I've had enough negotiating with you. [You reach into your bag, grab the coins and…” *(if pay 6,000 gold)* → [torilo_beer_pay](#d-torilo_beer_pay)
    - “That sounds ridiculous! I won't pay that” *(if have 6,000 gold)* → [torilo_beer_bribe6000_10](#d-torilo_beer_bribe6000_10)
    - “I can't afford that.” → [torilo_beer_bribe6000_10](#d-torilo_beer_bribe6000_10)

    <span id="d-torilo_beer_bribe6000_10"></span>**`torilo_beer_bribe6000_10`** Torilo: “That's fine with me, but no information for you.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 11 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines changed<br>· text: “Hmm...let me think...how does 10000 gold sound?” → “Hmm...let me think...how does {10000} gold sound?”<br>· text: “OK. How does 7500 gold sound?” → “OK. How does {7500} gold sound?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=torilo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=torilo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=torilo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=torilo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `torilo` |
    | Spawn group | `torilo` |
    | Loot table | `shop_torilo` |
    | Conversation | `torilo_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:9` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "torilo",
     "name": "Torilo",
     "iconID": "monsters_men2:9",
     "monsterClass": "humanoid",
     "spawnGroup": "torilo",
     "phraseID": "torilo_1",
     "droplistID": "shop_torilo"
    }
    ```


<small>Data from v0.8.18</small>
