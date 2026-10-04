# ![](../assets/icons/monsters/monsters_ld1_100.png){ .sprite } Zaccheria

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
| [Boots of Swiftness](../items/boots_6.md) | 100% | 1 |
| [Fancy shirt](../items/fancy_shirt.md) | 100% | 1 |
| [Quilted tunic](../items/tunic_quilted.md) | 100% | 1 |
| [Rigid chain mail](../items/armour_rigid_chain.md) | 100% | 2 |
| [Grips of the warrior](../items/warrior_gloves.md) | 50% | 1 |
| [Bronzed grasps](../items/bronzed_gloves.md) | 100% | 2 |
| [Brutality boots](../items/brutality_boots.md) | 85% | 1 |
| [Bronze helmet](../items/bronze_helmet.md) | 100% | 1 |

## Found on

- [sullengard2_armory](../maps/sullengard2_armory.md)

## Quests

- [Recovering stolen property](../quests/sullengard_recover_items.md): stages 10, 20, 70
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 40

??? quote "Dialogue (21 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_zaccheria_selector"></span>**`sullengard_zaccheria_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60; NOT latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70) is 70)* → [sullengard_zaccheria_0](#d-sullengard_zaccheria_0)
    - Next *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-60) is 60; carry 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md))* → [sullengard_zaccheria_80](#d-sullengard_zaccheria_80)
    - Next *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-50) is 50)* → [sullengard_zaccheria_85](#d-sullengard_zaccheria_85)
    - Next *(if latest stage of [Wanted men](../quests/wanted_men.md#stage-57) is 57; NOT reached stage 40 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-40))* → [sullengard_zaccheria_ask_about_lt](#d-sullengard_zaccheria_ask_about_lt)
    - Next *(if latest stage of [Wanted men](../quests/wanted_men.md#stage-80) is 80; NOT reached stage 40 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-40))* → [sullengard_zaccheria_ask_about_lt](#d-sullengard_zaccheria_ask_about_lt)
    - Next *(if reached stage 70 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70))* → [sullengard_zaccheria_sell_0](#d-sullengard_zaccheria_sell_0)

    <span id="d-sullengard_zaccheria_0"></span>**`sullengard_zaccheria_0`** Zaccheria: “How can I help you?”

    - “I would like to see your wares.” → [sullengard_zaccheria_10](#d-sullengard_zaccheria_10)

    <span id="d-sullengard_zaccheria_80"></span>**`sullengard_zaccheria_80`** Zaccheria: “Are you carrying what I think you are carrying?”

    - “Yes. I tracked them down to this lost traveler who recently came into town. He was desperate for gold and a place to…” → [sullengard_zaccheria_90](#d-sullengard_zaccheria_90)

    <span id="d-sullengard_zaccheria_85"></span>**`sullengard_zaccheria_85`** Zaccheria: “Have you found my stuff yet?”

    - “Nope. Sorry, I am still looking.” → *conversation ends*

    <span id="d-sullengard_zaccheria_ask_about_lt"></span>**`sullengard_zaccheria_ask_about_lt`** Zaccheria: “Hey, you are just the person that I wanted to see. I've been wondering that with all of your adventures, have you encountered "the lost traveler" again?”

    - “Actually, yes. Yes, I have.” → [sullengard_zaccheria_ask_about_lt_10](#d-sullengard_zaccheria_ask_about_lt_10)

    <span id="d-sullengard_zaccheria_sell_0"></span>**`sullengard_zaccheria_sell_0`** Zaccheria: “How can I be of service?”

    - “Can I see your wares?” → [sullengard_zaccheria_sell_10](#d-sullengard_zaccheria_sell_10)

    <span id="d-sullengard_zaccheria_10"></span>**`sullengard_zaccheria_10`** Zaccheria: “I would like to show you, but my inventory has been stolen.”

    - “Stolen? How? That is extremely unfortunate for you as I have lots of gold to spend.” → [sullengard_zaccheria_20](#d-sullengard_zaccheria_20)

    <span id="d-sullengard_zaccheria_90"></span>**`sullengard_zaccheria_90`** Zaccheria: “And where is this person now?”

    - “I wish I knew. After he told me where to find your stuff, he took off and I was unable to see in what direction he…” *(if hand over 1× [Zaccheria's shop inventory](../items/zaccheria_inventory.md))* → [sullengard_zaccheria_100](#d-sullengard_zaccheria_100)
    - “I wish I knew. After he told me where to find your stuff, he took off and I was unable to see in what direction he…” *(if carry 0× [Zaccheria's shop inventory](../items/zaccheria_inventory.md))* → *conversation ends*

    <span id="d-sullengard_zaccheria_ask_about_lt_10"></span>**`sullengard_zaccheria_ask_about_lt_10`** Zaccheria: “Where? Can you get him back here to be punished?”

    - “Actually, he is in a Fallhaven jail. Locked up with Defy in fact. I was able to capture them and lock them up there.” *(if latest stage of [Wanted men](../quests/wanted_men.md#stage-57) is 57)* → [sullengard_zaccheria_ask_about_lt_11](#d-sullengard_zaccheria_ask_about_lt_11)
    - “Actually, I had a chance encounter with him and after attempting to drag him back here, he attacked me and I had no…” *(if latest stage of [Wanted men](../quests/wanted_men.md#stage-80) is 80)* → [sullengard_zaccheria_ask_about_lt_12](#d-sullengard_zaccheria_ask_about_lt_12)

    <span id="d-sullengard_zaccheria_sell_10"></span>**`sullengard_zaccheria_sell_10`** Zaccheria: “Absolutetly.”

    - Next → *shop opens*

    <span id="d-sullengard_zaccheria_20"></span>**`sullengard_zaccheria_20`** Zaccheria: “[With a smirk] Gee, how fortunate for you that I have job for you if you want it.”

    - “Great! Let's hear it.” → [sullengard_zaccheria_30](#d-sullengard_zaccheria_30)

    <span id="d-sullengard_zaccheria_100"></span>**`sullengard_zaccheria_100`** Zaccheria: “Well that's unfortunate that we cannot punish this individual. But very fortunate that you worked hard to recover my items and I am very grateful for that. So grateful in fact, here is 15,000 gold for your hard work. Also, I am now able…” — **effects:** sets stage 70 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-70), gives 15000× [Gold coins](../items/gold.md)

    - “Thank you so much.” → *conversation ends*

    <span id="d-sullengard_zaccheria_ask_about_lt_11"></span>**`sullengard_zaccheria_ask_about_lt_11`** Zaccheria: “Oh, thank you so much!”

    - “Of course. It was my pleasure.” → [sullengard_zaccheria_ask_about_lt_13](#d-sullengard_zaccheria_ask_about_lt_13)

    <span id="d-sullengard_zaccheria_ask_about_lt_12"></span>**`sullengard_zaccheria_ask_about_lt_12`** Zaccheria: “Well, I would have preferred to see him punished instead of killed, but thank you so much for putting an end to all this.”

    - “Of course. It was my pleasure.” → [sullengard_zaccheria_ask_about_lt_13](#d-sullengard_zaccheria_ask_about_lt_13)

    <span id="d-sullengard_zaccheria_30"></span>**`sullengard_zaccheria_30`** Zaccheria: “I need you to ask around town to see if anyone knows where my supply is or if they have seen anything.”

    - “I'll take it, but can you give me some more details?” → [sullengard_zaccheria_40](#d-sullengard_zaccheria_40)

    <span id="d-sullengard_zaccheria_ask_about_lt_13"></span>**`sullengard_zaccheria_ask_about_lt_13`** Zaccheria: “Please, take this as a gift of gratitude.” — **effects:** sets stage 40 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-40), gives [Feygard's might](../items/feygard_might.md)

    - “Thank you!” → [sullengard_zaccheria_ask_about_lt_14](#d-sullengard_zaccheria_ask_about_lt_14)

    <span id="d-sullengard_zaccheria_40"></span>**`sullengard_zaccheria_40`** Zaccheria: “Sure. You see, I was at the tavern last night enjoying a couple "Southernhaze" beers like I almost always do after work, when someone or some people broke into my shop and stole my entire inventory.” — **effects:** sets stage 10 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-10)

    - “I see. Anything else? Is there anyone in town that you can think of that would want to hurt you?” → [sullengard_zaccheria_50](#d-sullengard_zaccheria_50)

    <span id="d-sullengard_zaccheria_ask_about_lt_14"></span>**`sullengard_zaccheria_ask_about_lt_14`** Zaccheria: “I don't know if you will like it, but let me tell you, nobody down here wants it.”

    - “Oh, really? I will play with it. Thanks again.” → *conversation ends*

    <span id="d-sullengard_zaccheria_50"></span>**`sullengard_zaccheria_50`** Zaccheria: “Well, let me think...ah yes. Gaelian from the Briwerra family.”

    - “Why is that?” → [sullengard_zaccheria_60](#d-sullengard_zaccheria_60)

    <span id="d-sullengard_zaccheria_60"></span>**`sullengard_zaccheria_60`** Zaccheria: “Oh, it's not a big deal. Well, not from my side anyway, but he is mad about what he perceives as bad service on some repair work that I had recently done for him. He asked for his gold back, I refused.”

    - Next → [sullengard_zaccheria_70](#d-sullengard_zaccheria_70)

    <span id="d-sullengard_zaccheria_70"></span>**`sullengard_zaccheria_70`** Zaccheria: “Anyways, I think you should start there, but I suspect others too.” — **effects:** sets stage 20 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-20)




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_zaccheria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_zaccheria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_zaccheria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_zaccheria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sullengard_zaccheria` · Data from v0.8.18</small>
