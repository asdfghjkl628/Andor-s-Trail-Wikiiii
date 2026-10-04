# ![](../assets/icons/monsters/monsters_rltiles1_66.png){ .sprite } Thorin

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
| [Scaradon extract](../items/pot_scaradon.md) | 100% | 30 |

## Found on

- [mountaincave3](../maps/mountaincave3.md)

## Quests

- [Bits and pieces](../quests/thorin.md): stages 20, 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Thorin. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/thorin.json" data-npc="Thorin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (30 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thorin"></span>**`thorin`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Bits and pieces](../quests/thorin.md#stage-40))* → [thorin_return_1](#d-thorin_return_1)
    - branch 2 *(if reached stage 20 of [Bits and pieces](../quests/thorin.md#stage-20))* → [thorin_search_1](#d-thorin_search_1)
    - branch 3 → [thorin_1](#d-thorin_1)

    <span id="d-thorin_return_1"></span>**`thorin_return_1`** Thorin: “My friend returns. What can Thorin do for you?”

    - “Mind if I use your bed over there to rest?” → [thorin_rest_1](#d-thorin_rest_1)
    - “Do you have anything to trade?” → [thorin_trade_1](#d-thorin_trade_1)

    <span id="d-thorin_search_1"></span>**`thorin_search_1`** Thorin: “Welcome back. Did you find all six of them?”

    - “No, not yet. I am still looking.” → [thorin_search_2](#d-thorin_search_2)
    - “Yes, this is what I found.” *(if hand over 6× [Chewed bone](../items/thorin_bone.md))* → [thorin_search_c_1](#d-thorin_search_c_1)
    - “Mind if I use your bed over there to rest?” → [thorin_rest_1](#d-thorin_rest_1)
    - “Do you have anything to trade?” → [thorin_trade_1](#d-thorin_trade_1)

    <span id="d-thorin_1"></span>**`thorin_1`** Thorin: “What's this, a visitor? How unexpected.”

    - Next → [thorin_2](#d-thorin_2)

    <span id="d-thorin_rest_1"></span>**`thorin_rest_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Bits and pieces](../quests/thorin.md#stage-40))* → [thorin_rest_y](#d-thorin_rest_y)
    - branch 2 → [thorin_rest_n](#d-thorin_rest_n)

    <span id="d-thorin_trade_1"></span>**`thorin_trade_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Bits and pieces](../quests/thorin.md#stage-40))* → [thorin_trade_y](#d-thorin_trade_y)
    - branch 2 → [thorin_trade_n](#d-thorin_trade_n)

    <span id="d-thorin_search_2"></span>**`thorin_search_2`** Thorin: “OK then. Please return when you have found them all. I would go search myself if those nasty bugs weren't there.”


    <span id="d-thorin_search_c_1"></span>**`thorin_search_c_1`** Thorin: “Thank you. I would have gone myself if those nasty bugs weren't there. This turned out to be much easier though.” — **effects:** sets stage 40 of [Bits and pieces](../quests/thorin.md#stage-40)

    - Next → [thorin_search_c_2](#d-thorin_search_c_2)

    <span id="d-thorin_2"></span>**`thorin_2`** Thorin: “Tell me, what can Thorin do for you?”

    - “What are you doing here?” → [thorin_what_1](#d-thorin_what_1)
    - “Who are you?” → [thorin_who_1](#d-thorin_who_1)
    - “Mind if I use your bed over there to rest?” → [thorin_rest_1](#d-thorin_rest_1)
    - “Do you have anything to trade?” → [thorin_trade_1](#d-thorin_trade_1)

    <span id="d-thorin_rest_y"></span>**`thorin_rest_y`** Thorin: “Please, go ahead. You may rest here as much as you like.”


    <span id="d-thorin_rest_n"></span>**`thorin_rest_n`** Thorin: “My bed? No, that's mine. Maybe I will let you use it if you help me with a small task.”

    - “What's that?” → [thorin_story_1](#d-thorin_story_1)

    <span id="d-thorin_trade_y"></span>**`thorin_trade_y`** Thorin: “Oh yes. The upside of this cave is that it literally is crawling with dead bodies of those scaradon bugs.”

    - Next → [thorin_trade_y2](#d-thorin_trade_y2)

    <span id="d-thorin_trade_n"></span>**`thorin_trade_n`** Thorin: “No. I might have something to trade if you help me with a small task.”

    - “What's that?” → [thorin_story_1](#d-thorin_story_1)

    <span id="d-thorin_search_c_2"></span>**`thorin_search_c_2`** Thorin: “As a token of my appreciation, you are welcome to use the bed over there to rest. Also, if you are interested in healing, I might be able to provide some help.”

    - “I think I should use the bed to rest right now. Thank you.” → *conversation ends*
    - “Do you have anything to trade?” → [thorin_trade_1](#d-thorin_trade_1)
    - “You are welcome. Goodbye.” → *conversation ends*

    <span id="d-thorin_what_1"></span>**`thorin_what_1`** Thorin: “Oh, not much. Well actually, I am waiting for someone - or rather, some people.”

    - Next → [thorin_story_1](#d-thorin_story_1)

    <span id="d-thorin_who_1"></span>**`thorin_who_1`** Thorin: “Oh, I did not introduce me, my apologies. I am Thorin.”

    - “What are you doing here?” → [thorin_what_1](#d-thorin_what_1)

    <span id="d-thorin_story_1"></span>**`thorin_story_1`** Thorin: “You see, me and my fellow gatherers were out investigating the poisonous nature of the irdegh.”

    - Next → [thorin_story_2](#d-thorin_story_2)

    <span id="d-thorin_trade_y2"></span>**`thorin_trade_y2`** Thorin: “By chance, I happened to find out that with the right mixture, they can be made into a healing substance.”

    - “Let's see what you have to trade.” → *shop opens*

    <span id="d-thorin_story_2"></span>**`thorin_story_2`** Thorin: “Apparently, I was the only one that was careful enough when handling our wares.”

    - Next → [thorin_story_3](#d-thorin_story_3)

    <span id="d-thorin_story_3"></span>**`thorin_story_3`** Thorin: “The others got ill quite quick, and we hid in this cave to rest up. However, we had not anticipated these bugs in here.”

    - Next → [thorin_story_4](#d-thorin_story_4)

    <span id="d-thorin_story_4"></span>**`thorin_story_4`** Thorin: “Those 'scaradon' things are tough! They did not even seem to take any damage when I hit them.”

    - Next → [thorin_story_5](#d-thorin_story_5)

    <span id="d-thorin_story_5"></span>**`thorin_story_5`** Thorin: “So, that's where I am now. The people that sent us to investigate told us to set up camp if we encountered any problems, and they would come help us.”

    - Next → [thorin_story_6](#d-thorin_story_6)

    <span id="d-thorin_story_6"></span>**`thorin_story_6`** Thorin: “So far, you are the first visitor here for quite a while.”

    - “You don't seem all that upset that your friends died.” → [thorin_story_6_1](#d-thorin_story_6_1)
    - “Anything I can do to help you meanwhile?” → [thorin_story_7](#d-thorin_story_7)
    - “Tough luck. I bet help will be here any day now. Goodbye.” → *conversation ends*

    <span id="d-thorin_story_6_1"></span>**`thorin_story_6_1`** Thorin: “Nah, it's just business. Just business.”

    - “Anything I can do to help you?” → [thorin_story_7](#d-thorin_story_7)
    - “Tough luck. I bet your rescue will be here any day now. Goodbye.” → *conversation ends*

    <span id="d-thorin_story_7"></span>**`thorin_story_7`** Thorin: “Hmm. Yes, actually there is something that you could do for me.”

    - Next → [thorin_story_8](#d-thorin_story_8)

    <span id="d-thorin_story_8"></span>**`thorin_story_8`** Thorin: “The others that I was travelling with, they did not make it this far into the cave, but got attacked by those bugs closer to the entrance.”

    - Next → [thorin_story_9](#d-thorin_story_9)

    <span id="d-thorin_story_9"></span>**`thorin_story_9`** Thorin: “Considering how they died, I would be very interested in seeing what effects both the irdegh and the scaradons had on them.”

    - Next → [thorin_story_10](#d-thorin_story_10)

    <span id="d-thorin_story_10"></span>**`thorin_story_10`** Thorin: “If you could find me their remains, I would be most grateful. Maybe I could continue my investigation based on their remains. Hmm, yes that would be great.”

    - “Sure, find their remains. Sounds easy enough, I'll do it.” → [thorin_story_11](#d-thorin_story_11)
    - “I'm all for finding dead things. I'll do it.” → [thorin_story_11](#d-thorin_story_11)
    - “Hmm, this sounds a bit shady to me. I'm not sure I should do this.” → [thorin_decline](#d-thorin_decline)

    <span id="d-thorin_story_11"></span>**`thorin_story_11`** Thorin: “Excellent. Bring me back the remains of all six of them. I would go search myself if those nasty bugs weren't there.” — **effects:** sets stage 20 of [Bits and pieces](../quests/thorin.md#stage-20)


    <span id="d-thorin_decline"></span>**`thorin_decline`** Thorin: “Too bad. Good day to you then.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “Ok then. Please return when you have found them all. I would go searc…” → “OK then. Please return when you have found them all. I would go searc…”<br>· text: “Oh yes. The upside of this cave is that it literally is crawling with…” → “Oh yes. The upside of this cave is that it literally is crawling with…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thorin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thorin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thorin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thorin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `thorin` · Data from v0.8.18</small>
