# ![](../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite } Tavern guest

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

- [remgard_tavern0](../maps/remgard_tavern0.md)

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tavern guest. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_drunk2.json" data-npc="Tavern guest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-remgard_drunk2"></span>**`remgard_drunk2`** Tavern guest: “*burp* This is the best place in all of the northern lands!”

    - Next → [remgard_drunk2_2](#d-remgard_drunk2_2)

    <span id="d-remgard_drunk2_2"></span>**`remgard_drunk2_2`** Tavern guest: “Oh, hello there. *burp* Kid, I tell you, don't go looking for trouble even if you think you can handle it.”

    - Next → [remgard_drunk2_3](#d-remgard_drunk2_3)

    <span id="d-remgard_drunk2_3"></span>**`remgard_drunk2_3`** Tavern guest: “I did once, and ended up in those horrid caverns of Mount Galmore.”

    - Next → [remgard_drunk2_4](#d-remgard_drunk2_4)

    <span id="d-remgard_drunk2_4"></span>**`remgard_drunk2_4`** Tavern guest: “That place twists your mind. I tell you, don't go there, even if you think you want to!”

    - “Mount Galmore, where is that?” *(if NOT reached stage 10 of [The swamp healer](../quests/swamp_healer.md#stage-10))* → [remgard_drunk2_5](#d-remgard_drunk2_5)
    - “Mount Galmore twists your mind? Oh, I see. You mean Undertell?” *(if reached stage 5 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-5))* → [remgard_drunk2_5](#d-remgard_drunk2_5)
    - “I'll keep that in mind.” → *conversation ends*
    - “Get out of my way!” → *conversation ends*

    <span id="d-remgard_drunk2_5"></span>**`remgard_drunk2_5`** Tavern guest: “[burp] What was that? Were you saying something?”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “That place twists your mind. I tell you, don't go there, even if you …” → “That place twists your mind. I tell you, don't go there, even if you …” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “*burp* What was that? Were you saying something?” → “[burp] What was that? Were you saying something?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_d2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_d2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_d2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_d2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `remgard_d2` · Data from v0.8.18</small>
