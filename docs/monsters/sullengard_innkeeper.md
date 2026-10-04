# ![](../assets/icons/monsters/monsters_ld1_97.png){ .sprite } Godfrey

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
| [Cooked meat](../items/meat_cooked.md) | 100% | 1 to 4 |
| [Watermelon slice](../items/watermelon_slice.md) | 100% | 1 to 5 |
| [Hard biscuits](../items/biscuit_hard.md) | 100% | 1 to 7 |

## Found on

- [sullengard_inn](../maps/sullengard_inn.md)

## Quests

- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 1

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Godfrey. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_godrey_0.json" data-npc="Godfrey" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_godrey_0"></span>**`sullengard_godrey_0`** Godfrey: “Hello. I'm Godfrey, and I own this place, but I'm forced to work today because somebody quit on me.”

    - Next → [sullengard_godrey_10](#d-sullengard_godrey_10)

    <span id="d-sullengard_godrey_10"></span>**`sullengard_godrey_10`** Godfrey: “What can I help you with?”

    - “I need somewhere to relax and refresh. Do you have a bed available?” *(if NOT reached stage 1 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-1))* → [sullengard_godrey_30](#d-sullengard_godrey_30)
    - “I'm hungry. Do you have any food to sell?” → [sullengard_godrey_sell](#d-sullengard_godrey_sell)
    - “Do you know by chance where this lost travelor is?” *(if reached stage 40 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40); NOT reached stage 50 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-50))* → [sullengard_godrey_10a](#d-sullengard_godrey_10a)
    - “Where I can find Celdar?” *(if latest stage of [Restless in the grave](../quests/mg_restless_grave.md#stage-123) is 123)* → [sullengard_godrey_celdar](#d-sullengard_godrey_celdar)

    <span id="d-sullengard_godrey_30"></span>**`sullengard_godrey_30`** Godfrey: “Well, it will cost you 700 gold! Beds are always in high demand before and during the Beer Festival.”

    - “That's too expensive. Let's talk about something else.” → [sullengard_godrey_10](#d-sullengard_godrey_10)
    - “I'll take it, but I have to say that you really should join the Thieves' Guild with that attitude!” *(if pay 700 gold)* → [sullengard_godrey_40](#d-sullengard_godrey_40)

    <span id="d-sullengard_godrey_sell"></span>**`sullengard_godrey_sell`** Godfrey: “Certainly. Please take a look at what I can offer.”

    - “Great! Let's take a look.” → *shop opens*

    <span id="d-sullengard_godrey_10a"></span>**`sullengard_godrey_10a`** Godfrey: “Sure. Look at the table over there. He is my best customer at the moment.” — **effects:** spawns monsters on sullengard_inn


    <span id="d-sullengard_godrey_celdar"></span>**`sullengard_godrey_celdar`** Godfrey: “Now there's a name I haven't heard in a long time. I don't think she's been in town for a long time.”

    - “Oh, OK, thanks.” → *conversation ends*

    <span id="d-sullengard_godrey_40"></span>**`sullengard_godrey_40`** Godfrey: “Thank you! It pays to be the owner. You can use any available bed.” — **effects:** sets stage 1 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-1)




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 6 lines added |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 3 lines changed<br>· text: “Sure. Look at the table over there. He is my best customer at he mome…” → “Sure. Look at the table over there. He is my best customer at the mom…” |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_innkeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sullengard_innkeeper` · Data from v0.8.18</small>
