# ![](../assets/icons/monsters/monsters_rltiles1_66.png){ .sprite } Reinkarr

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

- [remgard3](../maps/remgard3.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Reinkarr. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/reinkarr.json" data-npc="Reinkarr" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-reinkarr"></span>**`reinkarr`** Reinkarr: “You look just like an adventurer. Tell me child, what brings you here?”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)
    - “I'm looking for my brother Andor.” → [reinkarr_1](#d-reinkarr_1)
    - “I'm just looking for trouble.” → [reinkarr_2](#d-reinkarr_2)

    <span id="d-reinkarr_3"></span>**`reinkarr_3`** Reinkarr: “I am Reinkarr. I guess you could call me an adventurer of sorts.”

    - “Any good tales to tell?” → [reinkarr_4](#d-reinkarr_4)

    <span id="d-reinkarr_1"></span>**`reinkarr_1`** Reinkarr: “OK then. Good luck with that.”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)

    <span id="d-reinkarr_2"></span>**`reinkarr_2`** Reinkarr: “Ha ha, that sure sounds like an adventurer! Guts, that's what you need to be a successful adventurer, child. You don't seem to lack courage, if I may say so.”

    - “Who are you?” → [reinkarr_3](#d-reinkarr_3)

    <span id="d-reinkarr_4"></span>**`reinkarr_4`** Reinkarr: “No, not really. I never got the hang of the whole adventuring business. Me and some other fellows went looking for these ... crystals ... that we had heard about.”

    - “What crystals?” → [reinkarr_5](#d-reinkarr_5)

    <span id="d-reinkarr_5"></span>**`reinkarr_5`** Reinkarr: “Doesn't really matter. We never found any of them anyway.”

    - “What crystals were you looking for?” → [reinkarr_6](#d-reinkarr_6)

    <span id="d-reinkarr_6"></span>**`reinkarr_6`** Reinkarr: “They were called 'Oegyth crystals'. Supposedly very powerful and worth a fortune.”

    - “I have one of those.” *(if carry 1× [Oegyth crystal](../items/oegyth.md))* → [reinkarr_oeg_1](#d-reinkarr_oeg_1)
    - “So what made you stop looking?” → [reinkarr_8](#d-reinkarr_8)
    - “What are they?” → [reinkarr_7](#d-reinkarr_7)

    <span id="d-reinkarr_oeg_1"></span>**`reinkarr_oeg_1`** Reinkarr: “What!? You actually have one of those things? Let me see. Yes, that sure matches the description I read.”

    - Next → [reinkarr_oeg_2](#d-reinkarr_oeg_2)

    <span id="d-reinkarr_8"></span>**`reinkarr_8`** Reinkarr: “Just the boredom of it, I guess. We never were any good at the whole fighting thing, and as such we never found one of those things.”

    - Next → [reinkarr_9](#d-reinkarr_9)

    <span id="d-reinkarr_7"></span>**`reinkarr_7`** Reinkarr: “Actually, all I know is that they are some sort of crystal. As I said, they are supposedly very powerful. We were only looking for them so that we could sell them and become rich.”

    - “What made you stop looking?” → [reinkarr_8](#d-reinkarr_8)

    <span id="d-reinkarr_oeg_2"></span>**`reinkarr_oeg_2`** Reinkarr: “You would do well to keep that to yourself, kid. Whatever you do, don't lose it, and don't go around showing it to everyone you might meet. You could get in serious trouble.”

    - “What can I do with it?” → [reinkarr_oeg_3](#d-reinkarr_oeg_3)

    <span id="d-reinkarr_9"></span>**`reinkarr_9`** Reinkarr: “Anyway, it's been nice talking to you, kid. Take care.”


    <span id="d-reinkarr_oeg_3"></span>**`reinkarr_oeg_3`** Reinkarr: “I hear there are merchants that would do anything to get their hands on some of those crystals. You should seek out the merchants in one of the larger cities, and ask them.”

    - Next → [reinkarr_oeg_4](#d-reinkarr_oeg_4)

    <span id="d-reinkarr_oeg_4"></span>**`reinkarr_oeg_4`** Reinkarr: “Please be careful though!”

    - Next → [reinkarr_9](#d-reinkarr_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “No, not really. I never got the hang of the whole adventuring busines…” → “No, not really. I never got the hang of the whole adventuring busines…”<br>· text: “Ok then. Good luck with that.” → “OK then. Good luck with that.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=reinkarr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `reinkarr` · Data from v0.8.18</small>
